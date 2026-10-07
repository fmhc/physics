# EIS-1 (Runde 34), Teil 1: klassisches Spin-Eis (T -> 0) mit genau zwei Defekten auf dem periodischen Pyrochlor-Gitter.
# Aufruf (nur ueber kleintest.sh): eis_mc.py <L> <seed> <einlauf_schritte> <block_schritte> <m_stich> <zeitgrenze_s> <ausgabe_praefix>
# Schreibt <praefix>.json (Zusammenfassung, Pruefungen) und <praefix>.npz (Histogramme je Block, Endzustand).
import sys, os, json, time, ctypes, subprocess, hashlib
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gitter

t_start = time.time()
L = int(sys.argv[1]); seed = int(sys.argv[2]); n_ein = int(float(sys.argv[3])); n_block = int(float(sys.argv[4]))
m_stich = int(sys.argv[5]); t_grenze = float(sys.argv[6]); praefix = sys.argv[7]

# ---- C-Kern uebersetzen (in den Laufordner, eindeutiger Name) ----
quelle = os.path.join(HIER, "eis_kern.c")
so = os.path.abspath("%s_kern_%d.so" % (praefix, os.getpid()))
r = subprocess.run(["gcc", "-O2", "-shared", "-fPIC", "-o", so, quelle], capture_output=True, text=True)
if r.returncode != 0:
    print(r.stderr); sys.exit(4)
kern = ctypes.CDLL(so)
P_i8 = np.ctypeslib.ndpointer(dtype=np.int8, flags="C_CONTIGUOUS")
P_i32 = np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS")
P_i64 = np.ctypeslib.ndpointer(dtype=np.int64, flags="C_CONTIGUOUS")
P_u64 = np.ctypeslib.ndpointer(dtype=np.uint64, flags="C_CONTIGUOUS")
kern.laufe.restype = ctypes.c_int64
kern.laufe.argtypes = [ctypes.c_int64, ctypes.c_int32, P_i8, P_i32, P_i32, P_i32, P_i32, ctypes.c_int32,
                       ctypes.c_int32, P_i32, P_u64, P_i64, P_i64]

# ---- Gitter ----
g = gitter.pyrochlor(L)
nup, P = g["nup"], g["P"]
nt = 2 * nup
tsite = np.ascontiguousarray(g["tsite"].ravel().astype(np.int32))
tup = np.ascontiguousarray(g["tup"]); tdown = np.ascontiguousarray(g["tdown"])
tkoord = np.ascontiguousarray(g["tkoord"].ravel().astype(np.int32))
sub = g["sub"]


def ladungen(spin):
    s = spin[g["tsite"]].astype(int).sum(1)
    s[nup:] *= -1
    return s  # = 2 Q


def moment(spin):
    # staggered Moment sum sigma_i * e_i (e_i Einheitsvektor Ecke -> oberes Zentrum), Einheiten 1
    e = gitter.D_PYR[sub] / np.sqrt(3.0)
    return (spin[:, None] * e).sum(0)


# ---- Anfangszustand: Eiszustand (Unterbitter 0,1 -> +1; 2,3 -> -1), dann Defektpaar durch einen Umklapp ----
spin = np.where(sub < 2, 1, -1).astype(np.int8)
q0 = ladungen(spin)
eis_anfang_ok = bool(np.all(q0 == 0))
spin[0] = -spin[0]
q1 = ladungen(spin)
tp = int(np.where(q1 == 2)[0][0]); tm = int(np.where(q1 == -2)[0][0])
paar_ok = bool((np.sum(q1 == 2) == 1) and (np.sum(q1 == -2) == 1) and (np.sum(q1 != 0) == 2))
defekt = np.array([tp, tm], dtype=np.int32)


def splitmix(x):
    out = []
    for _ in range(4):
        x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        z = x
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
        out.append(z ^ (z >> 31))
    return np.array(out, dtype=np.uint64)


rng = splitmix(seed * 1000003 + L)
r2max = 3 * (4 * L) ** 2
z = np.zeros(8, dtype=np.int64)


def voll_pruefen():
    q = ladungen(spin)
    ok = (q[defekt[0]] == 2) and (q[defekt[1]] == -2) and (np.sum(q != 0) == 2)
    return bool(ok), int(np.sum(np.abs(q) == 4))


# ---- Einlauf in Stuecken, mit Momentverlauf ----
verlauf = []
m = moment(spin); verlauf.append([0, float(np.linalg.norm(m))])
stuecke = 20
hist_dummy = np.zeros(r2max + 1, dtype=np.int64)
z_ein = np.zeros(8, dtype=np.int64)
t0 = time.time()
for k in range(stuecke):
    kern.laufe(n_ein // stuecke, 1 << 30, spin, tsite, tup, tdown, tkoord, nup, P, defekt, rng, hist_dummy, z_ein)
    m = moment(spin); verlauf.append([int((k + 1) * (n_ein // stuecke)), float(np.linalg.norm(m))])
t_ein = time.time() - t0
ein_ok, ein_q2 = voll_pruefen()

# ---- Messung in Bloecken bis zur Zeitgrenze ----
bloecke = []
zaehler_bloecke = []
pruef_bloecke = []
t1 = time.time()
dauer_block = None
while True:
    rest = t_grenze - (time.time() - t_start)
    if dauer_block is not None and rest < 1.3 * dauer_block + 5:
        break
    if dauer_block is None and rest < 60:
        break
    h = np.zeros(r2max + 1, dtype=np.int64)
    zb = np.zeros(8, dtype=np.int64)
    tb = time.time()
    kern.laufe(n_block, m_stich, spin, tsite, tup, tdown, tkoord, nup, P, defekt, rng, h, zb)
    dauer_block = time.time() - tb
    ok, q2 = voll_pruefen()
    bloecke.append(h)
    zaehler_bloecke.append(zb.copy())
    pruef_bloecke.append([ok, q2])
t_mess = time.time() - t1

bloecke = np.array(bloecke)
zb = np.array(zaehler_bloecke)
zs = zb.sum(0) if len(zb) else np.zeros(8, dtype=np.int64)
m_end = moment(spin)

np.savez_compressed(praefix + ".npz", hist_bloecke=bloecke, zaehler_bloecke=zb, spin=spin, defekt=defekt, rng=rng,
                    verlauf=np.array(verlauf))
quell_sha = hashlib.sha256(open(quelle, "rb").read()).hexdigest()
skript_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
aus = dict(
    teil="Spin-Eis", L=L, seed=seed, n_einlauf=n_ein, n_block=n_block, m_stich=m_stich, zeitgrenze_s=t_grenze,
    gitter_pruefung=g["pruef"], eis_anfang_ok=eis_anfang_ok, paar_nach_umklapp_ok=paar_ok,
    einlauf_s=t_ein, einlauf_zaehler=dict(angenommen=int(z_ein[0]), abgelehnt_orientierung=int(z_ein[1]),
                                          abgelehnt_vernichtung=int(z_ein[2]), eisregel_fehler_lokal=int(z_ein[3])),
    einlauf_voll_ok=ein_ok, einlauf_ladung2=ein_q2, moment_verlauf=verlauf,
    moment_anfang_betrag=verlauf[0][1], moment_ende_betrag=float(np.linalg.norm(m_end)),
    moment_ende=[float(x) for x in m_end],
    bloecke=int(len(bloecke)), mess_s=t_mess, schritte_je_s=float(len(bloecke) * n_block / max(t_mess, 1e-9)),
    zaehler=dict(angenommen=int(zs[0]), abgelehnt_orientierung=int(zs[1]), abgelehnt_vernichtung=int(zs[2]),
                 eisregel_fehler_lokal=int(zs[3]), stichproben=int(zs[4]), plus_auf_oben=int(zs[5]),
                 minus_auf_oben=int(zs[6]), gleiche_art=int(zs[7])),
    voll_pruefung_bloecke_ok=bool(all(p[0] for p in pruef_bloecke)) if pruef_bloecke else None,
    voll_pruefung_ladung2_summe=int(sum(p[1] for p in pruef_bloecke)) if pruef_bloecke else None,
    kern_sha256=quell_sha, skript_sha256=skript_sha, dauer_s=time.time() - t_start,
    ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
)
json.dump(aus, open(praefix + ".json", "w"), indent=1)
os.remove(so)
print(json.dumps({k: aus[k] for k in ("L", "seed", "bloecke", "schritte_je_s", "zaehler", "einlauf_voll_ok",
                                      "voll_pruefung_bloecke_ok", "moment_anfang_betrag", "moment_ende_betrag",
                                      "dauer_s")}, indent=1))
