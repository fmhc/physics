# FLUSS-1 (Runde 34): Pfeile auf Kanten ("Krafteinheiten fliessen entlang der Kanten"), Monte Carlo.
# Aufruf nur ueber kleintest.sh auf der .69:
#   fluss_mc.py paar <L> <seed> <einlauf_schritte> <block_schritte> <m_stich> <zeitgrenze_s> <praefix>
#       Netz A, Paar-Sektor (Defekte q = +2 / -2), Abstandshistogramme je Block (F1).
#   fluss_mc.py korr <A|B> <L> <seed> <einlauf> <einheiten_je_messung> <messungen_je_block> <zeitgrenze_s> <praefix> [start]
#       Netz A: Eis-Sektor mit geschlossenen Wuermern (Einheit = Wurm); Netz B: Einzelkanten-Zuege (Einheit = Durchgang
#       ueber alle Kanten). Pfeil-Korrelationen gleicher Richtungsklasse ueber FFT (F2, F3). start (nur B): kette | reparatur
#   fluss_mc.py pruef <praefix>
#       Geometrie beider Netze fuer L = 1, 2, 3, 4, 6; Netz B, L = 1: Vollaufzaehlung und Zusammenhang des Zug-Graphen.
import sys, os, json, time, ctypes, subprocess, hashlib
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gitter
import gitter_fluss as gf

T_START = time.time()
MAX_BLOECKE = 40


def sha(pfad):
    return hashlib.sha256(open(pfad, "rb").read()).hexdigest()


def kern_laden(praefix):
    quelle = os.path.join(HIER, "fluss_kern.c")
    so = os.path.abspath("%s_kern_%d.so" % (praefix, os.getpid()))
    r = subprocess.run(["gcc", "-O2", "-shared", "-fPIC", "-o", so, quelle], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr); sys.exit(4)
    k = ctypes.CDLL(so)
    I8 = np.ctypeslib.ndpointer(dtype=np.int8, flags="C_CONTIGUOUS")
    I32 = np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS")
    I64 = np.ctypeslib.ndpointer(dtype=np.int64, flags="C_CONTIGUOUS")
    U64 = np.ctypeslib.ndpointer(dtype=np.uint64, flags="C_CONTIGUOUS")
    k.ladungen.restype = None
    k.ladungen.argtypes = [I8, I32, I8, ctypes.c_int32, ctypes.c_int32, I32]
    k.paar_laufe.restype = ctypes.c_int64
    k.paar_laufe.argtypes = [ctypes.c_int64, ctypes.c_int32, I8, I32, I8, I32, I32, ctypes.c_int32, I32, U64, I64, I64]
    k.wurm_laufe.restype = ctypes.c_int64
    k.wurm_laufe.argtypes = [ctypes.c_int64, I8, I32, I8, I32, I32, I32, ctypes.c_int32, U64, I64]
    k.srs_laufe.restype = ctypes.c_int64
    k.srs_laufe.argtypes = [ctypes.c_int64, I8, I8, I32, I8, I32, I32, ctypes.c_int32, U64, I64]
    return k, so, quelle


def splitmix(x):
    out = []
    for _ in range(4):
        x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        z = x
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
        out.append(z ^ (z >> 31))
    return np.array(out, dtype=np.uint64)


def ladungen(kern, net, s):
    q = np.zeros(net["nv"], dtype=np.int32)
    kern.ladungen(s, net["inz"], net["vz"], net["nv"], net["G"], q)
    return q


def eis_start_ketten(net, seed):
    """Eiszustand: jede gerade Kette einheitlich, Richtung je Kette zufaellig."""
    rs = np.random.default_rng(seed + 7919)
    eps = rs.choice(np.array([-1, 1]), size=net["n_ketten"])
    return eps[net["kette"]].astype(np.int8)


def srs_start(net, seed, art):
    """Netz B: Anfangszustand mit q = +-1 an jeder Ecke.
    kette: Klassen [011] und [01-1] bilden eine perfekte Paarung; der Rest zerfaellt in Kreise, die einheitlich
    durchlaufen werden; Paarungskanten zufaellig. reparatur: zufaellige Pfeile, dann Ecken mit |q| = 3 reparieren."""
    rs = np.random.default_rng(seed + 104729)
    ne, nv = net["ne"], net["nv"]
    kopf, schwanz, kl = net["kopf"], net["schwanz"], net["kl"]
    s = np.zeros(ne, dtype=np.int8)
    info = {}
    if art == "kette":
        paar = np.isin(kl, (4, 5))
        grad_paar = np.bincount(np.concatenate([kopf[paar], schwanz[paar]]), minlength=nv)
        info["paarung_perfekt"] = bool(np.all(grad_paar == 1))
        s[paar] = rs.choice(np.array([-1, 1]), size=int(paar.sum())).astype(np.int8)
        rest = np.where(~paar)[0]
        nachbarn = {}
        for e in rest:
            for v in (int(kopf[e]), int(schwanz[e])):
                nachbarn.setdefault(v, []).append(int(e))
        info["rest_2_regulaer"] = bool(all(len(x) == 2 for x in nachbarn.values()) and len(nachbarn) == nv)
        besucht = np.zeros(ne, dtype=bool); kreise = 0; laengen = []
        for e0 in rest:
            if besucht[e0]:
                continue
            kreise += 1
            richtung = int(rs.choice([-1, 1]))
            e = int(e0); v = int(kopf[e]) if richtung > 0 else int(schwanz[e])  # Pfeil e zeigt nach v
            s[e] = richtung; besucht[e] = True; lg = 1
            while True:
                a, b = nachbarn[v]
                f = b if a == e else a
                if besucht[f]:
                    break
                # Pfeil von v weg
                if int(schwanz[f]) == v:
                    s[f] = 1; v_neu = int(kopf[f])
                else:
                    s[f] = -1; v_neu = int(schwanz[f])
                besucht[f] = True; e = f; v = v_neu; lg += 1
            laengen.append(lg)
        info["kreise"] = kreise; info["kreislaenge_min_max"] = [int(min(laengen)), int(max(laengen))]
    else:
        s[:] = rs.choice(np.array([-1, 1]), size=ne).astype(np.int8)
        nb2d = net["nb2d"]; inz2d = net["inz"].reshape(nv, 3); vz2d = net["vz"].reshape(nv, 3)
        q = (s[inz2d] * vz2d).sum(1).astype(int)
        schlecht = set(np.where(np.abs(q) == 3)[0].tolist())
        info["anfang_verletzt"] = len(schlecht)
        schritte = 0
        while schlecht:
            v = int(rs.choice(np.fromiter(schlecht, dtype=np.int64))) if schritte % 64 == 0 else next(iter(schlecht))
            k = int(rs.integers(3))
            e = int(inz2d[v, k]); w = int(nb2d[v, k])
            s[e] = -s[e]
            for x in (v, w):
                q[x] = int((s[inz2d[x]] * vz2d[x]).sum())
                if abs(q[x]) == 3:
                    schlecht.add(x)
                else:
                    schlecht.discard(x)
            schritte += 1
        info["reparatur_schritte"] = schritte
    return s, info


def tau_int(x):
    """integrierte Autokorrelationszeit (Einheiten: Messabstaende), Fenster nach Sokal (c = 6)."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n < 20 or np.var(x) == 0:
        return None
    y = x - x.mean()
    f = np.fft.rfft(y, 2 * n)
    ac = np.fft.irfft(f * np.conj(f))[:n]
    ac = ac / ac[0]
    tau = 0.5
    for t in range(1, n):
        tau += ac[t]
        if t >= 6 * tau:
            break
    return float(tau)


# ---------------------------------------------------------------------------------------------------------------
def modus_paar(argv):
    L = int(argv[0]); seed = int(argv[1]); n_ein = int(float(argv[2])); n_block = int(float(argv[3]))
    m_stich = int(argv[4]); t_grenze = float(argv[5]); praefix = argv[6]
    kern, so, quelle = kern_laden(praefix)
    net = gf.netz_a(L)
    P = net["P"]
    s = eis_start_ketten(net, seed)
    q0 = ladungen(kern, net, s)
    eis_anfang_ok = bool(np.all(q0 == 0))
    rs = np.random.default_rng(seed)
    e0 = int(rs.integers(net["ne"]))
    if s[e0] > 0:
        plus, minus = int(net["schwanz"][e0]), int(net["kopf"][e0])
    else:
        plus, minus = int(net["kopf"][e0]), int(net["schwanz"][e0])
    s[e0] = -s[e0]
    q1 = ladungen(kern, net, s)
    paar_ok = bool(q1[plus] == 2 and q1[minus] == -2 and np.sum(q1 != 0) == 2)
    defekt = np.array([plus, minus], dtype=np.int32)
    rng = splitmix(seed * 1000003 + L)
    koord = np.ascontiguousarray(net["ecken"].ravel().astype(np.int32))
    r2max = 3 * (4 * L) ** 2

    def voll():
        q = ladungen(kern, net, s)
        ok = (q[defekt[0]] == 2) and (q[defekt[1]] == -2) and (np.sum(q != 0) == 2)
        return bool(ok)

    z_ein = np.zeros(9, dtype=np.int64); h_dummy = np.zeros(r2max + 1, dtype=np.int64)
    t0 = time.time()
    for k in range(10):
        kern.paar_laufe(n_ein // 10, 1 << 30, s, net["inz"], net["vz"], net["nb"], koord, P, defekt, rng, h_dummy, z_ein)
    t_ein = time.time() - t0
    ein_ok = voll()
    bloecke = []; zb_liste = []; pruef_bl = []
    dauer = None
    t1 = time.time()
    while True:
        rest = t_grenze - (time.time() - T_START)
        if dauer is not None and rest < 1.3 * dauer + 5:
            break
        if dauer is None and rest < 30:
            break
        h = np.zeros(r2max + 1, dtype=np.int64); zb = np.zeros(9, dtype=np.int64)
        tb = time.time()
        kern.paar_laufe(n_block, m_stich, s, net["inz"], net["vz"], net["nb"], koord, P, defekt, rng, h, zb)
        dauer = time.time() - tb
        bloecke.append(h); zb_liste.append(zb.copy()); pruef_bl.append(voll())
    t_mess = time.time() - t1
    bloecke = np.array(bloecke); zb = np.array(zb_liste)
    zs = zb.sum(0) if len(zb) else np.zeros(9, dtype=np.int64)
    np.savez_compressed(praefix + ".npz", hist_bloecke=bloecke, zaehler_bloecke=zb, s=s, defekt=defekt)
    pr = net["pruef"]
    aus = dict(modus="paar", netz="A", L=L, seed=seed, n_einlauf=n_ein, n_block=n_block, m_stich=m_stich,
               zeitgrenze_s=t_grenze, gitter_pruefung=pr, eis_anfang_ok=eis_anfang_ok, paar_nach_umklapp_ok=paar_ok,
               einlauf_s=t_ein, einlauf_zaehler=[int(x) for x in z_ein], einlauf_voll_ok=ein_ok,
               bloecke=int(len(bloecke)), mess_s=t_mess,
               schritte_je_s=float(len(bloecke) * n_block / max(t_mess, 1e-9)),
               zaehler=dict(angenommen=int(zs[0]), abgelehnt_richtung=int(zs[1]), abgelehnt_vernichtung=int(zs[2]),
                            eisregel_fehler_lokal=int(zs[3] + z_ein[3]), stichproben=int(zs[4]),
                            plus_untergitter=[int(x) for x in zs[5:9]]),
               voll_pruefung_bloecke_ok=bool(all(pruef_bl)) if pruef_bl else None,
               kern_sha256=sha(quelle), skript_sha256=sha(os.path.abspath(__file__)),
               gitter_fluss_sha256=sha(os.path.join(HIER, "gitter_fluss.py")),
               gitter_sha256=sha(os.path.join(HIER, "gitter.py")),
               dauer_s=time.time() - T_START, ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    json.dump(aus, open(praefix + ".json", "w"), indent=1)
    os.remove(so)
    print(json.dumps({k: aus[k] for k in ("L", "seed", "bloecke", "schritte_je_s", "zaehler", "einlauf_voll_ok",
                                          "voll_pruefung_bloecke_ok", "dauer_s")}, indent=1))
    print("gitter alles_ok", pr["alles_ok"])


# ---------------------------------------------------------------------------------------------------------------
class Korrelator:
    """Pfeil-Korrelationen gleicher Richtungsklasse ueber FFT auf Klassengittern; Schalen nach |Delta|^2."""

    def __init__(self, net, sp):
        P = net["P"]; self.P = P; self.sp = sp; n = P // sp; self.n = n
        self.kl = net["kl"]; self.ne = net["ne"]
        self.idx = []; self.kanten = []; self.off = []
        pr = {}
        for c in range(6):
            sel = np.where(self.kl == c)[0]
            m = net["mitte"][sel]
            o = m[0] % sp
            if not np.all((m - o) % sp == 0):
                raise ValueError("Klassengitter passt nicht")
            g = ((m - o) % P) // sp
            lin = (g[:, 0] * n + g[:, 1]) * n + g[:, 2]
            if len(np.unique(lin)) != len(sel):
                raise ValueError("Klassengitter nicht eindeutig")
            self.idx.append((g[:, 0], g[:, 1], g[:, 2])); self.kanten.append(sel); self.off.append(o)
        # Paarzahlen m_c(Delta), Schalen, P2, Achse, senkrecht
        d = np.arange(n); d = ((d + n // 2) % n) - n // 2
        DX, DY, DZ = np.meshgrid(d * sp, d * sp, d * sp, indexing="ij")
        self.r2 = (DX ** 2 + DY ** 2 + DZ ** 2).astype(np.int64)
        self.nsch = int(self.r2.max()) + 1
        self.m = []; self.p2 = []; self.ax = []; self.senk = []
        for c in range(6):
            mask = np.zeros((n, n, n)); mask[self.idx[c]] = 1.0
            F = np.fft.rfftn(mask)
            mc = np.rint(np.fft.irfftn(F.real ** 2 + F.imag ** 2, s=(n, n, n), axes=(0, 1, 2))).astype(np.int64)
            self.m.append(mc)
            nc = gf.KLASSEN[c]
            dot = nc[0] * DX + nc[1] * DY + nc[2] * DZ
            with np.errstate(invalid="ignore", divide="ignore"):
                cos2 = np.where(self.r2 > 0, dot.astype(float) ** 2 / (2.0 * self.r2), 0.0)
            self.p2.append(np.where(self.r2 > 0, 1.5 * cos2 - 0.5, 0.0))
            kreuz2 = (nc[1] * DZ - nc[2] * DY) ** 2 + (nc[2] * DX - nc[0] * DZ) ** 2 + (nc[0] * DY - nc[1] * DX) ** 2
            self.ax.append((kreuz2 == 0) & (self.r2 > 0))
            self.senk.append((dot == 0) & (self.r2 > 0))
        pr["klassengitter_n"] = n; pr["paare_je_klasse_gesamt"] = [int(x.sum()) for x in self.m]
        self.pruef = pr
        # Nenner je Schale (fest)
        r2f = self.r2.ravel()
        self.den_bar = sum(np.bincount(r2f, weights=self.m[c].ravel(), minlength=self.nsch) for c in range(6))
        self.den_d = sum(np.bincount(r2f, weights=(self.m[c] * self.p2[c] ** 2).ravel(), minlength=self.nsch)
                         for c in range(6))
        self.den_ax = sum(np.bincount(r2f, weights=(self.m[c] * self.ax[c]).ravel(), minlength=self.nsch)
                          for c in range(6))
        self.den_senk = sum(np.bincount(r2f, weights=(self.m[c] * self.senk[c]).ravel(), minlength=self.nsch)
                            for c in range(6))
        # Strukturfaktor-Schnitt k_y = 0: Phasen je Klasse
        mx = np.fft.fftfreq(n, 1.0 / n).astype(int); mz = np.arange(n // 2 + 1)
        self.kx_idx = mx; self.kz_idx = mz
        self.phase = []
        for c in range(6):
            o = self.off[c]
            self.phase.append(np.exp(-2j * np.pi * (mx[:, None] * o[0] + mz[None, :] * o[2]) / P))
        self.einheit = gf.KLASSEN / np.sqrt(2.0)
        self.block_neu()
        self.Sxx = np.zeros((n, n // 2 + 1)); self.Syy = np.zeros_like(self.Sxx); self.Szz = np.zeros_like(self.Sxx)
        self.n_mess = 0
        self.C_bloecke = []; self.num_d = []; self.num_bar = []; self.num_ax = []; self.num_senk = []; self.ns_bl = []

    def block_neu(self):
        n = self.n
        self.S = [np.zeros((n, n, n // 2 + 1)) for _ in range(6)]
        self.ns = 0

    def messen(self, s):
        n = self.n
        Bx = np.zeros((n, n // 2 + 1), dtype=complex); By = np.zeros_like(Bx); Bz = np.zeros_like(Bx)
        for c in range(6):
            g = np.zeros((n, n, n)); g[self.idx[c]] = s[self.kanten[c]]
            F = np.fft.rfftn(g)
            self.S[c] += F.real ** 2 + F.imag ** 2
            sl = F[:, 0, :] * self.phase[c]
            Bx += self.einheit[c, 0] * sl; By += self.einheit[c, 1] * sl; Bz += self.einheit[c, 2] * sl
        self.Sxx += np.abs(Bx) ** 2 / self.ne; self.Syy += np.abs(By) ** 2 / self.ne; self.Szz += np.abs(Bz) ** 2 / self.ne
        self.ns += 1; self.n_mess += 1

    def block_ende(self):
        n = self.n
        r2f = self.r2.ravel()
        Cb = []; nd = 0; nb_ = 0; na = 0; nsk = 0
        for c in range(6):
            raw = np.fft.irfftn(self.S[c], s=(n, n, n), axes=(0, 1, 2))
            with np.errstate(invalid="ignore", divide="ignore"):
                C = np.where(self.m[c] > 0, raw / (self.ns * np.maximum(self.m[c], 1)), 0.0)
            Cb.append(C.astype(np.float32))
            w = (raw / self.ns) * (self.m[c] > 0)
            nd = nd + np.bincount(r2f, weights=(w * self.p2[c]).ravel(), minlength=self.nsch)
            nb_ = nb_ + np.bincount(r2f, weights=w.ravel(), minlength=self.nsch)
            na = na + np.bincount(r2f, weights=(w * self.ax[c]).ravel(), minlength=self.nsch)
            nsk = nsk + np.bincount(r2f, weights=(w * self.senk[c]).ravel(), minlength=self.nsch)
        self.C_bloecke.append(Cb); self.num_d.append(nd); self.num_bar.append(nb_); self.num_ax.append(na)
        self.num_senk.append(nsk); self.ns_bl.append(self.ns)
        self.block_neu()

    def quadrat_schaetzer(self):
        """unverzerrter Schalen-Mittelwert von C(Delta)^2 (Kreuzprodukte verschiedener Bloecke), m-gewichtet ueber alle
        Klassen; dazu derselbe Schaetzer fuer die Abweichung vom Schalenmittel (l >= 1). Jackknife je Block."""
        B = len(self.C_bloecke)
        r2f = self.r2.ravel()
        if B < 3:
            return None
        bar_b = [self.num_bar[b] / np.where(self.den_bar > 0, self.den_bar, 1) for b in range(B)]
        aus = {}
        for art in ("alle", "abw"):
            U_ges = np.zeros(self.nsch); U_jk = np.zeros((B, self.nsch))
            for c in range(6):
                m = self.m[c].astype(float)
                if art == "alle":
                    X = [self.C_bloecke[b][c].astype(float) for b in range(B)]
                else:
                    X = [self.C_bloecke[b][c].astype(float) - bar_b[b][self.r2] * (self.m[c] > 0) for b in range(B)]
                S1 = sum(X); S2 = sum(x * x for x in X)
                U = (S1 * S1 - S2) / (B * (B - 1))
                U_ges += np.bincount(r2f, weights=(m * U).ravel(), minlength=self.nsch)
                for j in range(B):
                    a1 = S1 - X[j]; a2 = S2 - X[j] * X[j]
                    Uj = (a1 * a1 - a2) / ((B - 1) * (B - 2))
                    U_jk[j] += np.bincount(r2f, weights=(m * Uj).ravel(), minlength=self.nsch)
            dn = np.where(self.den_bar > 0, self.den_bar, 1)
            aus[art] = (U_ges / dn, U_jk / dn[None, :])
        return aus


def modus_korr(argv):
    netz = argv[0]; L = int(argv[1]); seed = int(argv[2]); n_ein = int(float(argv[3]))
    je_mess = int(float(argv[4])); mess_je_block = int(argv[5]); t_grenze = float(argv[6]); praefix = argv[7]
    start = argv[8] if len(argv) > 8 else "kette"
    kern, so, quelle = kern_laden(praefix)
    t_geo = time.time()
    net = gf.netz_a(L) if netz == "A" else gf.netz_b(L)
    t_geo = time.time() - t_geo
    rng = splitmix(seed * 1000003 + L * 31 + (0 if netz == "A" else 17))
    info_start = {}
    if netz == "A":
        s = eis_start_ketten(net, seed)
        q = ladungen(kern, net, s)
        info_start["eis_anfang_ok"] = bool(np.all(q == 0))
        sp = 2
    else:
        s, info_start = srs_start(net, seed, start)
        q32 = ladungen(kern, net, s)
        info_start["anfang_q_pm1"] = bool(np.all(np.abs(q32) == 1))
        qm = q32.astype(np.int8)
        sp = 4
    if netz == "B":
        kz = [gf.bfs_kennzahlen(net, st, tiefe=10) for st in range(8)]
        net["pruef"]["bfs_je_basisecke"] = kz
        net["pruef"]["taillenweite"] = int(min(k["kuerzester_kreis"] for k in kz))
        net["pruef"]["taillenweite_10"] = bool(all(k["kuerzester_kreis"] == 10 for k in kz))
        net["pruef"]["alles_ok"] = bool(net["pruef"]["alles_ok"] and net["pruef"]["taillenweite_10"])
    kor = Korrelator(net, sp)
    z = np.zeros(9, dtype=np.int64)

    def einheiten(anz):
        if netz == "A":
            kern.wurm_laufe(anz, s, net["inz"], net["vz"], net["nb"], net["kopf"], net["schwanz"], net["ne"], rng, z)
        else:
            kern.srs_laufe(anz * net["ne"], s, qm, net["inz"], net["vz"], net["kopf"], net["schwanz"], net["ne"], rng, z)

    seite = net.get("seite")
    reihen = dict(phi2=[], c1=[], ms=[], f_flip=[])
    voll_fehler = 0

    def beobachten():
        nonlocal voll_fehler
        q = ladungen(kern, net, s)
        if netz == "A":
            if not np.all(q == 0):
                voll_fehler += 1
        else:
            if not (np.all(np.abs(q) == 1) and np.all(q == qm)):
                voll_fehler += 1
        Phi = (s[:, None].astype(float) * gf.KLASSEN[kor.kl]).sum(0)
        reihen["phi2"].append(float(Phi @ Phi / (2.0 * net["ne"])))
        if netz == "A":
            reihen["c1"].append(float(np.mean(s.astype(float) * s[net["nachfolger"]])))
        else:
            reihen["ms"].append(float((q[seite == 0].sum() - q[seite == 1].sum()) / net["nv"]))
            a = np.where(s > 0, net["schwanz"], net["kopf"]); b = np.where(s > 0, net["kopf"], net["schwanz"])
            reihen["f_flip"].append(float(np.mean((q[a] == -1) & (q[b] == 1))))

    t0 = time.time()
    z_vor = z.copy()
    for k in range(10):
        einheiten(max(n_ein // 10, 1))
    t_ein = time.time() - t0
    z_ein = (z - z_vor).copy()
    beobachten()
    t1 = time.time(); dauer = None; t_mc = 0.0; t_fft = 0.0
    reserve = 40.0 if netz == "A" else 20.0
    while True:
        rest = t_grenze - (time.time() - T_START)
        if dauer is not None and rest < 1.3 * dauer + reserve:
            break
        if dauer is None and rest < 60:
            break
        if len(kor.C_bloecke) >= MAX_BLOECKE:
            break
        tb = time.time()
        for i in range(mess_je_block):
            ta = time.time(); einheiten(je_mess); t_mc += time.time() - ta
            ta = time.time(); kor.messen(s); t_fft += time.time() - ta
            beobachten()
        kor.block_ende()
        dauer = time.time() - tb
    t_mess = time.time() - t1
    tq = time.time()
    qs = kor.quadrat_schaetzer()
    t_q = time.time() - tq
    B = len(kor.C_bloecke)
    erg = dict(r2=np.arange(kor.nsch), den_d=kor.den_d, den_bar=kor.den_bar, den_ax=kor.den_ax, den_senk=kor.den_senk,
               num_d=np.array(kor.num_d), num_bar=np.array(kor.num_bar), num_ax=np.array(kor.num_ax),
               num_senk=np.array(kor.num_senk), ns_bl=np.array(kor.ns_bl),
               Sxx=kor.Sxx / max(kor.n_mess, 1), Syy=kor.Syy / max(kor.n_mess, 1), Szz=kor.Szz / max(kor.n_mess, 1),
               kx_idx=kor.kx_idx, kz_idx=kor.kz_idx,
               phi2=np.array(reihen["phi2"]), c1=np.array(reihen["c1"]), ms=np.array(reihen["ms"]),
               f_flip=np.array(reihen["f_flip"]), s_ende=s)
    if qs is not None:
        erg["R2_alle"], erg["R2_alle_jk"] = qs["alle"]
        erg["R2_abw"], erg["R2_abw_jk"] = qs["abw"]
    # mittleres C(Delta) ueber Bloecke und Klassen (fuer Bilder), nur fuer |Delta| <= L/2
    np.savez_compressed(praefix + ".npz", **erg)
    pr = net["pruef"]
    reihe_tau = {k: tau_int(v) for k, v in reihen.items() if len(v)}
    aus = dict(modus="korr", netz=netz, L=L, seed=seed, start=start if netz == "B" else "ketten_zufaellig",
               n_einlauf=n_ein, einheiten_je_messung=je_mess, messungen_je_block=mess_je_block, zeitgrenze_s=t_grenze,
               einheit="Wurm" if netz == "A" else "Durchgang (E Vorschlaege)", klassengitter_abstand_1_8=sp,
               gitter_pruefung=pr, korrelator_pruefung=kor.pruef, start_info=info_start,
               geometrie_s=t_geo, einlauf_s=t_ein, einlauf_zaehler=[int(x) for x in z_ein],
               bloecke=B, messungen=int(kor.n_mess), mess_s=t_mess, mc_s=t_mc, fft_s=t_fft, quadrat_s=t_q,
               zaehler=[int(x) for x in z],
               zaehler_bedeutung=("A: 0 Versuche, 1 Umklappungen, 2 Wuermer, 3 Eisregel-Fehler lokal, 4 laengster Wurm"
                                  if netz == "A" else "B: 0 angenommen, 1 abgelehnt, 2 Regel-Fehler lokal"),
               regel_fehler_lokal=int(z[3] if netz == "A" else z[2]), voll_pruefung_fehler=int(voll_fehler),
               voll_pruefungen=int(len(reihen["phi2"])),
               tau_int_messabstaende=reihe_tau,
               mittel=dict((k, float(np.mean(v))) for k, v in reihen.items() if len(v)),
               kern_sha256=sha(quelle), skript_sha256=sha(os.path.abspath(__file__)),
               gitter_fluss_sha256=sha(os.path.join(HIER, "gitter_fluss.py")),
               gitter_sha256=sha(os.path.join(HIER, "gitter.py")),
               dauer_s=time.time() - T_START, ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    json.dump(aus, open(praefix + ".json", "w"), indent=1)
    os.remove(so)
    print(json.dumps({k: aus[k] for k in ("netz", "L", "seed", "start", "bloecke", "messungen", "mc_s", "fft_s",
                                          "quadrat_s", "zaehler", "regel_fehler_lokal", "voll_pruefung_fehler",
                                          "tau_int_messabstaende", "mittel", "dauer_s")}, indent=1))
    print("gitter alles_ok", pr["alles_ok"])


# ---------------------------------------------------------------------------------------------------------------
def modus_pruef(argv):
    praefix = argv[0]
    kern, so, quelle = kern_laden(praefix)
    aus = dict(netz_a={}, netz_b={})
    for L in (1, 2, 3, 4, 6):
        try:
            a = gf.netz_a(L)
            aus["netz_a"][str(L)] = dict((k, v) for k, v in a["pruef"].items() if k != "gitter_pyrochlor")
        except Exception as ex:
            aus["netz_a"][str(L)] = dict(fehler=repr(ex))
        b = gf.netz_b(L)
        eb = dict(b["pruef"])
        if L >= 2:
            kz = [gf.bfs_kennzahlen(b, st, tiefe=10) for st in range(8)]
            eb["bfs_je_basisecke"] = kz
        aus["netz_b"][str(L)] = eb
    # Netz B, L = 1: alle 2^12 Pfeilbelegungen, erlaubte Zustaende und Zug-Graph
    b = gf.netz_b(1)
    ne, nv = b["ne"], b["nv"]
    inz2d = b["inz"].reshape(nv, 3); vz2d = b["vz"].reshape(nv, 3)
    erlaubt = []
    for code in range(1 << ne):
        s = np.array([1 if (code >> e) & 1 else -1 for e in range(ne)], dtype=np.int8)
        q = (s[inz2d] * vz2d).sum(1)
        if np.all(np.abs(q) == 1):
            erlaubt.append(code)
    erlaubt_set = set(erlaubt)
    nachbar = {}
    for code in erlaubt:
        s = np.array([1 if (code >> e) & 1 else -1 for e in range(ne)], dtype=np.int8)
        q = (s[inz2d] * vz2d).sum(1)
        nb = []
        for e in range(ne):
            a, bb = (b["schwanz"][e], b["kopf"][e]) if s[e] > 0 else (b["kopf"][e], b["schwanz"][e])
            if q[a] == -1 and q[bb] == 1:
                c2 = code ^ (1 << e)
                if c2 not in erlaubt_set:
                    raise RuntimeError("Zug fuehrt aus der Regel")
                nb.append(c2)
        nachbar[code] = nb
    # Zusammenhang
    gesehen = {erlaubt[0]}; stapel = [erlaubt[0]]
    while stapel:
        x = stapel.pop()
        for y in nachbar[x]:
            if y not in gesehen:
                gesehen.add(y); stapel.append(y)
    symm = all(x in nachbar[y] for x in erlaubt for y in nachbar[x])
    # kurzer MC-Lauf mit dem C-Kern: Besuchshaeufigkeiten gegen Gleichverteilung
    s = np.array([1 if (erlaubt[0] >> e) & 1 else -1 for e in range(ne)], dtype=np.int8)
    qm = ((s[inz2d] * vz2d).sum(1)).astype(np.int8)
    rng = splitmix(4242); z = np.zeros(9, dtype=np.int64)
    zaehl = {c: 0 for c in erlaubt}
    gew = (1 << np.arange(ne))
    for i in range(200000):
        kern.srs_laufe(7, s, qm, b["inz"], b["vz"], b["kopf"], b["schwanz"], ne, rng, z)
        code = int(((s > 0).astype(np.int64) * gew).sum())
        zaehl[code] += 1
    h = np.array([zaehl[c] for c in erlaubt], dtype=float)
    erw = h.sum() / len(h)
    chi2 = float(((h - erw) ** 2 / erw).sum())
    aus["netz_b_L1_vollaufzaehlung"] = dict(zustaende_gesamt=1 << ne, erlaubt=len(erlaubt),
                                            zug_graph_zusammenhaengend=bool(len(gesehen) == len(erlaubt)),
                                            komponente_groesse=len(gesehen), zuege_symmetrisch=bool(symm),
                                            zuege_je_zustand_min_max=[min(len(v) for v in nachbar.values()),
                                                                      max(len(v) for v in nachbar.values())],
                                            mc_stichproben=int(h.sum()), mc_chi2=chi2, mc_freiheitsgrade=len(h) - 1,
                                            mc_min_max=[int(h.min()), int(h.max())],
                                            mc_regel_fehler_lokal=int(z[2]))
    aus["kern_sha256"] = sha(quelle); aus["skript_sha256"] = sha(os.path.abspath(__file__))
    aus["dauer_s"] = time.time() - T_START
    aus["ende_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    json.dump(aus, open(praefix + ".json", "w"), indent=1)
    os.remove(so)
    print(json.dumps(aus["netz_b_L1_vollaufzaehlung"], indent=1))
    for L, v in aus["netz_a"].items():
        print("A L=%s alles_ok %s" % (L, v.get("alles_ok")))
    for L, v in aus["netz_b"].items():
        print("B L=%s alles_ok %s %s" % (L, v.get("alles_ok"), [(k["kuerzester_kreis"], k["kuerzeste_kreise_durch_start"])
                                                             for k in v.get("bfs_je_basisecke", [])][:2]))
        if "bfs_je_basisecke" in v:
            print("   Koordinationsfolge", v["bfs_je_basisecke"][0]["koordinationsfolge"])


if __name__ == "__main__":
    modus = sys.argv[1]
    if modus == "paar":
        modus_paar(sys.argv[2:])
    elif modus == "korr":
        modus_korr(sys.argv[2:])
    elif modus == "pruef":
        modus_pruef(sys.argv[2:])
    else:
        print("unbekannter Modus", modus); sys.exit(2)
