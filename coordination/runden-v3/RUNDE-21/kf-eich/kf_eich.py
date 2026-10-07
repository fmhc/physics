#!/usr/bin/env python3
"""KF-EICH (Runde 21, v3): positive Eichprobe des Familien-Klassifikators aus Runde 6.

Karte: coordination/runden-v3/RUNDE-21/kf-eich/KARTE.md; Plan (vor dem ersten echten Lauf eingefroren): PLAN.md daneben.
Importiert kf5_geburt.py aus Runde 6 unveraendert (/home/fmh/fmhc-physics-remote/runde6-kf5, nur gelesen, ohne Bytecode):
Gitter, kraft_fn, dichten, analyse_arm, fenster_start, fenster_probe, fenster_auswerten, Familie (familie_2d_m0.json
daneben) und die Konstanten (STUFEN, BOX0, FENSTER, DT_FENSTER, FAM_TOL, Schwellen).

Gesetzt werden einzelne Q-Baelle m = 0 der 2D-Familie (Box 96, Mitte (0, 0)). Die Familiendatei enthaelt keine Profile
und kf5_geburt.py keinen Profilloeser; daher hier ein Schiessverfahren (RK4, Bisektion auf f(0), bei Bedarf weitere
Stufen auf f'(r_j)) fuer f'' + f'/r = (1 - omega^2 - 2 f^2 + 1,5 f^4) f, f'(0) = 0, f -> 0; jenseits f < 1e-7 die
asymptotische K0-Form. Interpolation auf das Gitter kubisch nach Hermite (f und f').
    ruhend:  psi = A f(r), psi_t = -i omega A f(r)                      (A = 1 Satz E, A = 1,05 Satz A)
    bewegt:  Lorentz-Boost mit v in +x: psi = f(r') exp(i omega gamma v x), r' = sqrt((gamma x)^2 + y^2),
             psi_t = (-gamma^2 v x f'(r')/r' - i omega gamma f(r')) exp(i omega gamma v x)          (t = 0)
K-Pruefung je Ball bei t = 0 auf dem Gitter (Summen wie kf5_geburt.dichten): Q, E (bewegt: E/gamma) und omega aus der
Gittergleichung (Rayleigh-Quotient des Ruheprofils) gegen die Familiendatei; Satz E muss auf 1e-3 stimmen, sonst Abbruch.
Zeitentwicklung: Velocity-Verlet wie kf5_geburt.lauf() (Zeile fuer Zeile nachgebaut, dort nicht einzeln aufrufbar).
Urteil "zu T" = Messfenster [T - 40, T] wie in Runde 6 ("bei T = 800" = [760, 800]): Tropfen aus analyse_arm am
Fensterbeginn, fenster_probe alle 1, fenster_auswerten am Ende. Fuer T = 0 rechnet derselbe Verlet mit -dt von 0 nach
-40 zurueck; dann vorwaerts -40 -> 200 durchgehend (Fenster [-40, 0], [10, 50], [60, 100], [160, 200]).
Klassifikation mit S0 = 0,3 (Hauptarm s03, entscheidet E0 bis E3) und S0 = 0,1 (Arm s01, Zusatz) auf denselben Laeufen.

Aufruf:  python kf_eich.py lauf --stufe grob|fein --gruppe alle|E-ruhend|E-bewegt|A [--rauch] [--out D]
         python kf_eich.py zusammen [--out D] --geraet cpu
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import datetime  # noqa: E402
import glob  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402

R6 = "/home/fmh/fmhc-physics-remote/runde6-kf5"
sys.path.insert(0, R6)
import torch  # noqa: E402
import kf5_geburt as kg  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
F64 = torch.float64
C128 = torch.complex128
z7 = kg.z7

# ---- feste Parameter (PLAN.md, vor dem ersten echten Lauf) ----
W2_SATZ = (0.52, 0.60, 0.70)          # Knoten der Familiendatei; 0,52: omega 0,7211 (Bereich der R6/R20-Tropfen)
V_BEWEGT = 0.05
AMP_A = 1.05
T_AUSW = (0.0, 50.0, 100.0, 200.0)
S0_HAUPT, S0_ZUSATZ = 0.3, 0.1
K_TOL = 1e-3
BALL_SUCH = 5.0                       # Fenstertropfen gilt als der Ball, wenn er hoechstens so weit vom Sollort startet
H_R, R_TAB, F_ZIEL, AGREE, MAX_STUFEN = 0.005, 72.0, 1e-7, 1e-9, 8
ZEITGRENZE_S = 560.0
RAUCH_T, RAUCH_FENSTER = (0.0, 8.0), 4.0

BAELLE = {}
for _w2 in W2_SATZ:
    _k = f"{int(round(_w2 * 100))}"
    BAELLE["E" + _k + "r"] = {"satz": "E", "w2": _w2, "v": 0.0, "amp": 1.0}
    BAELLE["E" + _k + "b"] = {"satz": "E", "w2": _w2, "v": V_BEWEGT, "amp": 1.0}
    BAELLE["A" + _k + "r"] = {"satz": "A", "w2": _w2, "v": 0.0, "amp": AMP_A}
GRUPPEN = {"E-ruhend": ["E52r", "E60r", "E70r"], "E-bewegt": ["E52b", "E60b", "E70b"], "A": ["A52r", "A60r", "A70r"]}
GRUPPEN["alle"] = GRUPPEN["E-ruhend"] + GRUPPEN["E-bewegt"] + GRUPPEN["A"]


# ---------------------------------------------------------------- Hilfen

def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def sha(pfad):
    h = hashlib.sha256()
    with open(pfad, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def frei_pfad(pfad):
    if os.path.exists(pfad) or os.path.exists(pfad + ".tmp"):
        raise SystemExit(f"{pfad} existiert schon: nichts ueberschreiben")
    return pfad


def schreibe_json(pfad, obj):
    frei_pfad(pfad)
    with open(pfad + ".tmp", "w") as fh:
        json.dump(obj, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


def herkunft():
    return {"kf5_geburt": os.path.join(R6, "kf5_geburt.py"), "kf5_geburt_sha256": sha(os.path.join(R6, "kf5_geburt.py")),
            "familie": kg.FAMILIE_DATEI, "familie_sha256": sha(kg.FAMILIE_DATEI),
            "kf_eich_sha256": sha(os.path.abspath(__file__)), "torch": torch.__version__, "geraet": kg.geraet_name()}


def familien_knoten():
    with open(kg.FAMILIE_DATEI) as fh:
        d = json.load(fh)
    return {round(z["omega2"], 6): z for z in d["zeilen"] if z["gueltig"]}


def familien_abstaende(fam, tr):
    """Wie kf5_weiter.familien_abstaende (Runde 20, unveraendert uebernommen): dQ* = Q_net / Q_fam(omega_ruhe) - 1,
    E/Q-Abstand = (E/Q) / (E/Q)_fam(Q) - 1, omega-Abstand = omega_ruhe - omega_fam(Q)."""
    q, om = tr.get("Q_net"), tr.get("omega_ruhe")
    dqs = None
    if q is not None and om is not None and q > 0.0:
        qf = fam.q(om)
        dqs = (q / qf - 1.0) if qf else None
    eq, eqf = tr.get("E_zu_Q"), tr.get("E_zu_Q_familie")
    of = tr.get("omega_familie_bei_Q")
    return {"dQ_stern": z7(dqs), "EQ_abstand": z7(eq / eqf - 1.0) if (eq is not None and eqf) else None,
            "omega_abstand": z7(om - of) if (om is not None and of is not None) else None}


# ---------------------------------------------------------------- Profil (Schiessverfahren)

def _rk4(w2, r0, f, p, nmax):
    """RK4 nach aussen ab (r0, f, p), Schritt H_R. 'ueber' (f < 0), 'unter' (f' > 0), 'ziel' (0 < f < F_ZIEL), 'rand'."""
    a = 1.0 - w2
    h = H_R
    fs, ps = [f], [p]
    for i in range(nmax):
        r = r0 + i * h
        s = f * f
        k1f, k1p = p, (a - 2.0 * s + 1.5 * s * s) * f - p / r
        f2, p2 = f + 0.5 * h * k1f, p + 0.5 * h * k1p
        s = f2 * f2
        k2f, k2p = p2, (a - 2.0 * s + 1.5 * s * s) * f2 - p2 / (r + 0.5 * h)
        f3, p3 = f + 0.5 * h * k2f, p + 0.5 * h * k2p
        s = f3 * f3
        k3f, k3p = p3, (a - 2.0 * s + 1.5 * s * s) * f3 - p3 / (r + 0.5 * h)
        f4, p4 = f + h * k3f, p + h * k3p
        s = f4 * f4
        k4f, k4p = p4, (a - 2.0 * s + 1.5 * s * s) * f4 - p4 / (r + h)
        f = f + h * (k1f + 2.0 * k2f + 2.0 * k3f + k4f) / 6.0
        p = p + h * (k1p + 2.0 * k2p + 2.0 * k3p + k4p) / 6.0
        fs.append(f)
        ps.append(p)
        if f < 0.0:
            return "ueber", fs, ps
        if p > 0.0:
            return "unter", fs, ps
        if f < F_ZIEL:
            return "ziel", fs, ps
    return "rand", fs, ps


def _stufe(w2, start, x_ueber, x_unter):
    def lauf(x):
        r0, f, p = start(x)
        return (r0,) + _rk4(w2, r0, f, p, int(round((R_TAB - r0) / H_R)))
    ra, rb = lauf(x_ueber), lauf(x_unter)
    for x, rr in ((x_ueber, ra), (x_unter, rb)):
        if rr[1] == "ziel":
            return {"ziel": True, "x": x, "r0": rr[0], "f": rr[2], "p": rr[3], "n": 0}
    if ra[1] not in ("ueber", "rand") or rb[1] != "unter":
        return {"ziel": False, "klammer": False, "enden": [ra[1], rb[1]]}
    n = 0
    while n < 200:
        xm = 0.5 * (x_ueber + x_unter)
        if xm == x_ueber or xm == x_unter:
            break
        rm = lauf(xm)
        n += 1
        if rm[1] == "ziel":
            return {"ziel": True, "x": xm, "r0": rm[0], "f": rm[2], "p": rm[3], "n": n}
        if rm[1] in ("ueber", "rand"):
            x_ueber, ra = xm, rm
        else:
            x_unter, rb = xm, rm
    return {"ziel": False, "klammer": True, "x_ueber": x_ueber, "x_unter": x_unter, "r0": ra[0], "fa": ra[2],
            "pa": ra[3], "fb": rb[2], "pb": rb[3], "n": n}


def _k0a(z):
    return math.sqrt(math.pi / (2.0 * z)) * math.exp(-z) * (1.0 - 1.0 / (8.0 * z) + 9.0 / (128.0 * z * z))


def _k1a(z):
    return math.sqrt(math.pi / (2.0 * z)) * math.exp(-z) * (1.0 + 3.0 / (8.0 * z) - 15.0 / (128.0 * z * z))


def profil(w2):
    """Radialprofil des Q-Balls m = 0 bei omega^2 = w2 auf r = i H_R, i = 0 .. R_TAB / H_R (f und f')."""
    a = 1.0 - w2
    h = H_R
    s_null = 1.0 - math.sqrt(2.0 * w2 - 1.0)            # W(S) = 0, W = (omega^2 S - U(S)) / 2
    s_top = (2.0 + math.sqrt(6.0 * w2 - 2.0)) / 3.0      # Maximum von W

    def start0(f0):
        s0 = f0 * f0
        a1 = (a - 2.0 * s0 + 1.5 * s0 * s0) * f0 / 4.0
        a2 = (a - 6.0 * s0 + 7.5 * s0 * s0) * a1 / 16.0
        return h, f0 + a1 * h * h + a2 * h ** 4, 2.0 * a1 * h + 4.0 * a2 * h ** 3

    teile, protokoll = [], []
    start, xa, xb = start0, math.sqrt(s_top) * (1.0 - 1e-15), math.sqrt(s_null) * (1.0 + 1e-9)
    f0, p_j, dp = None, None, None
    for nr in range(MAX_STUFEN):
        erg = None
        for weite in ((1.0,) if nr == 0 else (1.0, 1e2, 1e4)):
            if nr > 0:
                xa, xb = p_j - dp * weite, p_j + dp * weite
            erg = _stufe(w2, start, xa, xb)
            if erg.get("ziel") or erg.get("klammer"):
                break
        if not (erg.get("ziel") or erg.get("klammer")):
            raise RuntimeError(f"Profil omega^2 {w2}: keine Klammer in Stufe {nr}: {erg.get('enden')}")
        if nr == 0:
            f0 = erg["x"] if erg.get("ziel") else 0.5 * (erg["x_ueber"] + erg["x_unter"])
        if erg.get("ziel"):
            teile.append((erg["r0"], erg["f"], erg["p"]))
            protokoll.append({"stufe": nr, "r0": erg["r0"], "iterationen": erg["n"], "ziel": True,
                              "r_ende": erg["r0"] + (len(erg["f"]) - 1) * h})
            break
        fa, pa, fb, pb = erg["fa"], erg["pa"], erg["fb"], erg["pb"]
        j = 0
        for i in range(min(len(fa), len(fb))):
            if abs(fa[i] - fb[i]) <= AGREE * abs(fb[i]) and pa[i] < 0.0 and pb[i] < 0.0:
                j = i
            else:
                break
        if j < 1:
            raise RuntimeError(f"Profil omega^2 {w2}: Stufe {nr} ohne Fortschritt")
        teile.append((erg["r0"], [0.5 * (fa[i] + fb[i]) for i in range(j + 1)],
                      [0.5 * (pa[i] + pb[i]) for i in range(j + 1)]))
        r_j = erg["r0"] + j * h
        f_j, p_j = teile[-1][1][-1], teile[-1][2][-1]
        dp = 1e-7 * abs(p_j) + 1e-14
        protokoll.append({"stufe": nr, "r0": erg["r0"], "iterationen": erg["n"], "ziel": False, "r_einig": r_j,
                          "f_einig": f_j})
        start = (lambda x, r_j=r_j, f_j=f_j: (r_j, f_j, x))
    else:
        raise RuntimeError(f"Profil omega^2 {w2}: keine Konvergenz in {MAX_STUFEN} Stufen")
    N = int(round(R_TAB / h))
    tf, tp = [0.0] * (N + 1), [0.0] * (N + 1)
    tf[0] = f0
    m = 0
    for r0, fl, pl in teile:
        i0 = int(round(r0 / h))
        for i in range(len(fl)):
            if i0 + i <= N:
                tf[i0 + i], tp[i0 + i] = fl[i], pl[i]
                m = max(m, i0 + i)
    kap = math.sqrt(a)
    zm, f_m = kap * m * h, tf[m]
    for i in range(m + 1, N + 1):
        z = kap * i * h
        tf[i] = f_m * _k0a(z) / _k0a(zm)
        tp[i] = -kap * f_m * _k1a(z) / _k0a(zm)
    om = math.sqrt(w2)
    q = e = 0.0
    for i in range(N + 1):
        r, wgt = i * h, (0.5 if i in (0, N) else 1.0)
        s = tf[i] * tf[i]
        q += wgt * s * r
        e += wgt * (w2 * s + tp[i] * tp[i] + s - s * s + 0.5 * s ** 3) * r
    r_maske = {}
    for thr in (2.0 * S0_HAUPT, 2.0 * S0_ZUSATZ):
        r_maske[f"{thr:g}"] = next((i * h for i in range(N + 1) if tf[i] * tf[i] < thr), None)
    return {"w2": w2, "omega": om, "f0": f0, "Q_rad": 2.0 * om * 2.0 * math.pi * q * h, "E_rad": 2.0 * math.pi * e * h,
            "r_ziel": m * h, "r_maske_S_gleich": r_maske, "stufen": protokoll, "tf": tf, "tp": tp}


def hermite(tf, tp, r):
    n = tf.numel() - 1
    x = r / H_R
    i = torch.clamp(torch.floor(x).long(), 0, n - 1)
    t = (x - i.to(F64)).clamp(0.0, 1.0)
    f0, f1, p0, p1 = tf[i], tf[i + 1], tp[i], tp[i + 1]
    t2 = t * t
    t3 = t2 * t
    f = (2 * t3 - 3 * t2 + 1) * f0 + (t3 - 2 * t2 + t) * H_R * p0 + (-2 * t3 + 3 * t2) * f1 + (t3 - t2) * H_R * p1
    fp = ((6 * t2 - 6 * t) / H_R * f0 + (3 * t2 - 4 * t + 1) * p0 + (-6 * t2 + 6 * t) / H_R * f1
          + (3 * t2 - 2 * t) * p1)
    aussen = r >= n * H_R
    return torch.where(aussen, torch.zeros_like(f), f), torch.where(aussen, torch.zeros_like(fp), fp)


def ball_feld(g, prof, ball):
    om, v, amp = math.sqrt(ball["w2"]), ball["v"], ball["amp"]
    gam = 1.0 / math.sqrt(1.0 - v * v)
    tf = torch.tensor(prof["tf"], dtype=F64, device=kg.DEV)
    tp = torch.tensor(prof["tp"], dtype=F64, device=kg.DEV)
    rp = torch.sqrt((gam * g.X) ** 2 + g.Y ** 2)
    f, fp = hermite(tf, tp, rp)
    phase = torch.exp(1j * (om * gam * v) * g.X)
    psi = (amp * f) * phase
    vel = amp * (-(gam * gam * v) * fp * g.X / rp.clamp(min=1e-300) - 1j * (om * gam) * f) * phase
    return psi.to(C128).contiguous(), vel.to(C128).contiguous()


def omega_gitter(g, prof):
    """omega aus der Gittergleichung fuer das Ruheprofil: Rayleigh-Quotient <f, -Lap f + U'(f^2) f> / <f, f>; dazu das
    relative Residuum |(-Lap + U') f - omega_fam^2 f| / |omega_fam^2 f|."""
    f, _ = ball_feld(g, prof, {"w2": prof["w2"], "v": 0.0, "amp": 1.0})
    lap = torch.fft.ifft2(torch.fft.fft2(f) * g.mk2)
    s = f.real ** 2 + f.imag ** 2
    hf = -lap + (1.0 - 2.0 * s + 1.5 * s * s) * f
    w2r = ((f.conj() * hf).real.sum() / s.sum()).item()
    res = torch.sqrt(((hf - prof["w2"] * f).abs() ** 2).sum() / ((prof["w2"] * f).abs() ** 2).sum()).item()
    return math.sqrt(w2r), res


# ---------------------------------------------------------------- Diagnose fuer E3 (Regel PLAN.md, vor dem Lauf)

def diagnose(e):
    kl = e["klasse"]
    if kl == "auf":
        return None
    if kl in ("kein Tropfen", "nicht rund", "gestoert"):
        return "Schwelle"
    if kl == "ausserhalb":
        return "omega-Messung"
    if e["d_set"] is not None and abs(e["d_set"]) > kg.FAM_TOL:
        return "Q-Messung"
    if e["dQ_stern"] is not None and abs(e["dQ_stern"]) > kg.FAM_TOL:
        return "omega-Messung"
    return "omega-Messung (Unsicherheit u)"


# ---------------------------------------------------------------- lauf

def befehl_lauf(args):
    start = jetzt()
    t_start = kg.uhr()
    fam = kg.Familie()
    knoten = familien_knoten()
    dx, dt = kg.STUFEN[args.stufe]
    g = kg.Gitter(kg.BOX0, dx)
    namen = GRUPPEN[args.gruppe]
    B = len(namen)
    rauch = args.rauch
    t_liste = RAUCH_T if rauch else T_AUSW
    fenster = RAUCH_FENSTER if rauch else kg.FENSTER
    name = f"{args.stufe}_{args.gruppe}" + ("_rauch" if rauch else "")
    out = args.out or os.path.join(HIER, "lauf-69", "rauch" if rauch else "ausgabe")
    os.makedirs(out, exist_ok=True)
    pfad_json = frei_pfad(os.path.join(out, name + "_ergebnis.json"))
    print(f"KF-EICH lauf {name}: Start {start} auf {kg.geraet_name()}, n {g.n}, B {B}, Baelle {','.join(namen)}",
          flush=True)
    # Profile
    tp0 = kg.uhr()
    profile = {}
    for w2 in sorted({BAELLE[nm]["w2"] for nm in namen}):
        profile[w2] = profil(w2)
    dauer = {"profile": kg.uhr() - tp0}
    prof_out = {}
    for w2, p in profile.items():
        kn = knoten[round(w2, 6)]
        prof_out[f"{w2:g}"] = {x: p[x] for x in ("w2", "omega", "f0", "Q_rad", "E_rad", "r_ziel", "r_maske_S_gleich",
                                                  "stufen")}
        prof_out[f"{w2:g}"].update({"Q_fam": kn["Q"], "E_fam": kn["E"], "f_max_fam": kn["f_max"],
                                    "Q_rad_rel": p["Q_rad"] / kn["Q"] - 1.0, "E_rad_rel": p["E_rad"] / kn["E"] - 1.0,
                                    "f0_rel": p["f0"] / kn["f_max"] - 1.0})
        print(f"  Profil omega^2 {w2:g}: f0 {p['f0']:.10f} (fam f_max {kn['f_max']:.10f}), Q_rad {p['Q_rad']:.6f} "
              f"(fam {kn['Q']:.6f}), E_rad {p['E_rad']:.6f} (fam {kn['E']:.6f}), r_ziel {p['r_ziel']:.2f}, "
              f"Stufen {len(p['stufen'])}", flush=True)
    # Baelle setzen, K-Pruefung
    felder = [ball_feld(g, profile[BAELLE[nm]["w2"]], BAELLE[nm]) for nm in namen]
    psi = torch.stack([f[0] for f in felder]).contiguous()
    vel = torch.stack([f[1] for f in felder]).contiguous()
    del felder
    nl = torch.ones((B, 1, 1), dtype=F64, device=kg.DEV)
    kraft = kg.kraft_fn(g, nl)
    s, rho, e = kg.dichten(g, psi, vel, nl)
    q_box = (rho.sum((1, 2)) * g.dA).tolist()
    e_box = (e.sum((1, 2)) * g.dA).tolist()
    om_git = {w2: omega_gitter(g, p) for w2, p in profile.items()}
    kpr, k_ok = {}, True
    for b, nm in enumerate(namen):
        ba = BAELLE[nm]
        kn = knoten[round(ba["w2"], 6)]
        gam = 1.0 / math.sqrt(1.0 - ba["v"] ** 2)
        om_f = math.sqrt(ba["w2"])
        omr, res = om_git[ba["w2"]]
        k = {"Q": q_box[b], "E": e_box[b], "E_ruhe": e_box[b] / gam, "Q_fam": kn["Q"], "E_fam": kn["E"],
             "omega_fam": om_f, "omega_gitter": omr, "residuum_gitter": res,
             "dQ_rel": q_box[b] / kn["Q"] - 1.0, "dE_rel": e_box[b] / gam / kn["E"] - 1.0,
             "domega_rel": omr / om_f - 1.0, "S_max": s[b].max().item()}
        if ba["satz"] == "E":
            k["bestanden"] = all(abs(k[x]) <= K_TOL for x in ("dQ_rel", "dE_rel", "domega_rel"))
            k_ok = k_ok and k["bestanden"]
        else:
            k["Q_zu_Qfam_erwartet"] = AMP_A ** 2
            k["bestanden"] = None
        kpr[nm] = k
        print(f"  K {nm}: Q {k['Q']:.6f} (fam {kn['Q']:.6f}, rel {k['dQ_rel']:+.2e}), E_ruhe {k['E_ruhe']:.6f} (fam "
              f"{kn['E']:.6f}, rel {k['dE_rel']:+.2e}), omega_gitter {omr:.8f} (fam {om_f:.8f}, rel {k['domega_rel']:+.2e}"
              f", Residuum {res:.1e}), S_max {k['S_max']:.4f} -> "
              f"{'-' if k['bestanden'] is None else ('bestanden' if k['bestanden'] else 'NICHT bestanden')}", flush=True)
    meta = {"karte": "KF-EICH (R21)", "name": name, "start": start, "rauch": rauch, "fertig": False, "stufe": args.stufe,
            "gruppe": args.gruppe, "baelle": {nm: BAELLE[nm] for nm in namen}, "dx": dx, "dt": dt, "n": g.n,
            "box": g.box, "t_auswertung": list(t_liste), "fenster": fenster, "herkunft": herkunft(),
            "profile": prof_out, "k_pruefung": kpr, "k_bestanden": k_ok}
    if not k_ok:
        meta["ende"] = jetzt()
        meta["abbruch"] = "K-Pruefung Satz E nicht bestanden: keine Zeitentwicklung (PLAN.md)"
        schreibe_json(pfad_json, meta)
        raise SystemExit(meta["abbruch"])
    # Zeitentwicklung
    n_fen = int(round(fenster / dt))
    je_fen = int(round(kg.DT_FENSTER / dt))
    n_start, n_ende = -n_fen, int(round(t_liste[-1] / dt))
    fen_start = {int(round((T - fenster) / dt)): T for T in t_liste}
    fen_ende = {int(round(T / dt)): T for T in t_liste}
    psi0 = psi.clone()
    tb = kg.uhr()
    F = kraft(psi)
    for _ in range(n_fen):
        vel.add_(F, alpha=-0.5 * dt)
        psi.add_(vel, alpha=-dt)
        F = kraft(psi)
        vel.add_(F, alpha=-0.5 * dt)
    dauer["rueckwaerts"] = kg.uhr() - tb
    S0s = (S0_HAUPT, S0_ZUSATZ)
    aktiv, ergebnisse = {}, []
    dauer.update({"analyse": 0.0, "fenster": 0.0})
    rueckkehr = None
    t_vor = kg.uhr()
    F = kraft(psi)
    for schritt in range(n_start, n_ende + 1):
        if schritt > n_start:
            vel.add_(F, alpha=0.5 * dt)
            psi.add_(vel, alpha=dt)
            F = kraft(psi)
            vel.add_(F, alpha=0.5 * dt)
        if schritt == 0:
            rueckkehr = ((psi - psi0).abs().max() / psi0.abs().max()).item()
            del psi0
        if schritt == n_start + 400 and not rauch:
            verg = kg.uhr() - t_vor
            rate = (verg - dauer["analyse"] - dauer["fenster"]) / 400.0
            prognose = (kg.uhr() - t_start) + rate * (n_ende - schritt) + 1.3 * len(t_liste) * (
                dauer["analyse"] + dauer["fenster"] * (n_fen // je_fen + 1) / max(1, (schritt - n_start) // je_fen + 1))
            print(f"  Prognose Gesamtdauer {prognose:.0f} s", flush=True)
            if prognose > ZEITGRENZE_S:
                meta["ende"] = jetzt()
                meta["abbruch"] = f"Prognose {prognose:.0f} s ueber {ZEITGRENZE_S:.0f} s"
                schreibe_json(pfad_json, meta)
                raise SystemExit(meta["abbruch"] + ": Aufruf teilen")
        neu = schritt in fen_start
        probe = neu or any(schritt >= a["start"] and (schritt - a["start"]) % je_fen == 0 for a in aktiv.values())
        if not probe:
            continue
        s, rho, e = kg.dichten(g, psi, vel, nl)
        if neu:
            ta = kg.uhr()
            T = fen_start[schritt]
            a = {"start": schritt, "fzs": {}, "zeilen": {}, "s_max": s.amax((1, 2)).tolist()}
            for b in range(B):
                for S0 in S0s:
                    zeile, _, tropfen = kg.analyse_arm(g, s[b], rho[b], e[b], psi[b], S0, fam, None)
                    a["fzs"][(b, S0)] = kg.fenster_start(tropfen)
                    a["zeilen"][(b, S0)] = zeile
            aktiv[T] = a
            dauer["analyse"] += kg.uhr() - ta
        tf_ = kg.uhr()
        for a in aktiv.values():
            if schritt >= a["start"] and (schritt - a["start"]) % je_fen == 0:
                for (b, S0), fz in a["fzs"].items():
                    if fz is not None:
                        kg.fenster_probe(g, fz, s[b], rho[b], e[b], psi[b])
        dauer["fenster"] += kg.uhr() - tf_
        if schritt in fen_ende:
            T = fen_ende[schritt]
            a = aktiv.pop(T)
            t0 = round(T - fenster, 6)
            for b, nm in enumerate(namen):
                ba = BAELLE[nm]
                om_set = math.sqrt(ba["w2"])
                x_soll = float(kg.wrap_x(torch.tensor(ba["v"] * t0, dtype=F64), g.box))
                for S0 in S0s:
                    fen = kg.fenster_auswerten(a["fzs"][(b, S0)], t0, kg.DT_FENSTER, fam, g.box)
                    zeile = a["zeilen"][(b, S0)]
                    ztr = zeile.get("tropfen", {})
                    beste, dbest = None, None
                    for tr in fen["tropfen"]:
                        ddx = (tr["x0"] - x_soll) - g.box * round((tr["x0"] - x_soll) / g.box)
                        ddy = tr["y0"] - g.box * round(tr["y0"] / g.box)
                        d = math.hypot(ddx, ddy)
                        if d <= BALL_SUCH and (dbest is None or d < dbest):
                            beste, dbest = tr, d
                    z2 = zeile["schwellen"]["2"]
                    eintrag = {"ball": nm, "satz": ba["satz"], "w2": ba["w2"], "v": ba["v"], "amp": ba["amp"],
                               "S0": S0, "T": T, "fenster": [t0, T], "N_fenstertropfen": len(fen["tropfen"]),
                               "zaehlung": fen["zaehlung"], "urteil_arm": fen["urteil"], "N_komp_2S0": z2["N_komp"],
                               "N_klein_2S0": z2["N_klein"], "N_tropfen_2S0": z2["N_tropfen"],
                               "S_max_box_start": z7(a["s_max"][b])}
                    if beste is None:
                        eintrag.update({"klasse": "kein Tropfen", "rund": None, "d_set": None, "dQ_stern": None})
                    else:
                        k = beste["k"]
                        eintrag.update({x: beste.get(x) for x in (
                            "klasse", "klasse_roh", "rund", "Q_net", "Q_roh", "E_ruhe_net", "E_zu_Q", "E_zu_Q_familie",
                            "omega_rot", "omega_ruhe", "u_omega", "omega_inst_mittel", "omega_geo",
                            "omega_familie_bei_Q", "v", "S_max_mittel", "Q_schwankung", "verloren", "stoss", "dQ",
                            "dQ_band", "x0", "y0")})
                        eintrag["v_mess"] = eintrag.pop("v")
                        eintrag["v"] = ba["v"]
                        eintrag["abstand_soll"] = z7(dbest)
                        eintrag["rmax_zu_ra"] = (ztr.get("rmax_zu_ra") or [None] * (k + 1))[k]
                        eintrag["A_maske"] = (ztr.get("A") or [None] * (k + 1))[k]
                        eintrag["S_max_start"] = (ztr.get("S_max") or [None] * (k + 1))[k]
                        eintrag.update(familien_abstaende(fam, beste))
                        qf = fam.q(om_set)
                        q = beste.get("Q_net")
                        eintrag["d_set"] = z7(q / qf - 1.0) if (q is not None and qf) else None
                        om = beste.get("omega_ruhe")
                        eintrag["domega_set"] = z7(om - om_set) if om is not None else None
                    eintrag["diagnose"] = diagnose(eintrag)
                    ergebnisse.append(eintrag)
    dauer["vorwaerts_gesamt"] = kg.uhr() - t_vor
    dauer["gesamt"] = kg.uhr() - t_start
    meta.update({"ende": jetzt(), "fertig": True, "dauer_s": dauer, "rueckkehr_t0_psi_max_rel": rueckkehr,
                 "gpu_speicher_mb": (torch.cuda.max_memory_allocated() / 2 ** 20) if kg.DEV.type == "cuda" else None,
                 "schritte": {"rueckwaerts": n_fen, "vorwaerts": n_ende - n_start}})
    if rauch:
        n_voll = int(round((T_AUSW[-1] + kg.FENSTER) / dt))
        n_r = n_fen + (n_ende - n_start)
        ent = dauer["rueckwaerts"] + dauer["vorwaerts_gesamt"] - dauer["analyse"] - dauer["fenster"]
        n_probe_r = len(t_liste) * (n_fen // je_fen + 1)
        n_probe_v = len(T_AUSW) * (int(round(kg.FENSTER / kg.DT_FENSTER)) + 1)
        meta["prognose_voll_s"] = (dauer["profile"] + ent / n_r * (n_voll + int(round(kg.FENSTER / dt)))
                                   + dauer["analyse"] / len(t_liste) * len(T_AUSW) * 1.5
                                   + dauer["fenster"] / n_probe_r * n_probe_v * 1.5)
        meta["ms_je_schritt"] = ent / n_r * 1e3
        schreibe_json(pfad_json, meta)
        print(f"RAUCH {name}: Durchlauf ok; Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
              + f"; {meta['ms_je_schritt']:.2f} ms je Schritt (B {B}); Prognose voller Aufruf "
              f"{meta['prognose_voll_s']:.0f} s; GPU max {meta['gpu_speicher_mb']:.0f} MB; Rueckkehr {rueckkehr:.1e}",
              flush=True)
        return
    meta["ergebnisse"] = ergebnisse
    schreibe_json(pfad_json, meta)
    L = [f"KF-EICH {name}: Ende {meta['ende']}, Dauer [s] " + ", ".join(f"{x} {y:.1f}" for x, y in dauer.items())
         + f", Rueckkehr t=0 {rueckkehr:.1e}"]
    for x in ergebnisse:
        L.append(f"  {x['ball']} S0 {x['S0']} T {x['T']:g}: {x['klasse']} | rund {x.get('rund')} rmax/ra "
                 f"{kg.fz(x.get('rmax_zu_ra'), '.3f')} | Q {kg.fz(x.get('Q_net'))} | E/Q {kg.fz(x.get('E_zu_Q'), '.4f')} "
                 f"(fam {kg.fz(x.get('E_zu_Q_familie'), '.4f')}) | omega {kg.fz(x.get('omega_ruhe'), '.5f')} +- "
                 f"{kg.fz(x.get('u_omega'), '.1e')} (soll {math.sqrt(x['w2']):.5f}) | v {kg.fz(x.get('v_mess'), '.4f')} | "
                 f"dQ* {kg.fz(x.get('dQ_stern'), '+.4f')} | d_set {kg.fz(x.get('d_set'), '+.4f')} | Diagnose "
                 f"{x['diagnose']}")
    with open(frei_pfad(os.path.join(out, name + "_bericht.txt")), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


# ---------------------------------------------------------------- zusammen (E0 bis E3, Regeln PLAN.md)

def befehl_zusammen(args):
    out = args.out or os.path.join(HIER, "lauf-69", "ausgabe")
    eintraege, kpr, dateien = [], {}, []
    for p in sorted(glob.glob(os.path.join(out, "*_ergebnis.json"))):
        with open(p) as fh:
            d = json.load(fh)
        if d.get("rauch") or not d.get("fertig"):
            continue
        dateien.append({"datei": os.path.basename(p), "sha256": sha(p), "stufe": d["stufe"], "gruppe": d["gruppe"]})
        for x in d["ergebnisse"]:
            x["stufe"] = d["stufe"]
            eintraege.append(x)
        for nm, k in d["k_pruefung"].items():
            kpr[f"{d['stufe']}/{nm}"] = k

    def auswahl(satz, bewegt, S0, nur_T=None):
        return [x for x in eintraege if x["satz"] == satz and (x["v"] > 0.0) == bewegt and abs(x["S0"] - S0) < 1e-12
                and (nur_T is None or abs(x["T"] - nur_T) < 1e-9)]

    erg = {"zeit": jetzt(), "dateien": dateien, "k_pruefung": kpr}
    for S0, tag in ((S0_HAUPT, "s03"), (S0_ZUSATZ, "s01")):
        z = {}
        for nr, satz, bew in (("E0", "E", False), ("E1", "E", True)):
            sel = auswahl(satz, bew, S0)
            if len(sel) < 3 * len(T_AUSW) * 2:
                z[nr] = f"offen (unvollstaendig: {len(sel)} von {3 * len(T_AUSW) * 2})"
            else:
                n_auf = sum(1 for x in sel if x["klasse"] == "auf" and x["rund"])
                z[nr] = "eingetroffen" if n_auf == len(sel) else "nicht eingetroffen"
                z[nr + "_zahl"] = f"{n_auf} von {len(sel)} 'auf' und rund"
        sel = auswahl("A", False, S0, nur_T=0.0)
        if len(sel) < 6:
            z["E2"] = f"offen (unvollstaendig: {len(sel)} von 6)"
        elif any(x["klasse"] == "auf" for x in sel):
            z["E2"] = "nicht eingetroffen"
        elif all(x["klasse"] in ("neben", "unentschieden") for x in sel):
            z["E2"] = "eingetroffen"
        else:
            z["E2"] = "offen (kein 'auf', aber nicht nur 'neben'/'unentschieden')"
        z["E2_klassen"] = [f"{x['stufe']}/{x['ball']}: {x['klasse']}" for x in sel]
        sel0 = [x for x in auswahl("E", False, S0) if x["diagnose"] is not None]
        z["E0_fehlschlaege"] = [{"stufe": x["stufe"], "ball": x["ball"], "T": x["T"], "klasse": x["klasse"],
                                 "diagnose": x["diagnose"], "d_set": x.get("d_set"), "dQ_stern": x.get("dQ_stern"),
                                 "u_omega": x.get("u_omega"), "domega_set": x.get("domega_set"),
                                 "rmax_zu_ra": x.get("rmax_zu_ra"), "Q_schwankung": x.get("Q_schwankung")}
                                for x in sel0]
        if z["E0"] == "nicht eingetroffen":
            erlaubt = ("Schwelle", "omega-Messung", "omega-Messung (Unsicherheit u)")
            z["E3"] = "eingetroffen" if all(x["diagnose"] in erlaubt for x in sel0) else "nicht eingetroffen"
        elif z["E0"] == "eingetroffen":
            z["E3"] = "offen (Bedingung nicht erfuellt: E0 nicht gescheitert)"
        else:
            z["E3"] = "offen (E0 offen)"
        if z["E0"] == "eingetroffen":
            z["bedeutung"] = ("E0 eingetroffen: Der Klassifikator kann 'auf' sagen; das 'nie auf' der Tropfen ist ein "
                              "Befund (Karte)")
        elif z["E0"] == "nicht eingetroffen":
            z["bedeutung"] = ("E0 nicht eingetroffen: bisherige 'nie auf'-Urteile ohne Aussage; Klassifikator vor jedem "
                              "weiteren Bildungsversuch reparieren, KF-5 bleibt geparkt (Karte)")
        else:
            z["bedeutung"] = "E0 offen"
        erg["vorhersagen_" + tag] = z
    pfad = frei_pfad(os.path.join(out, "zusammen.json"))
    schreibe_json(pfad, erg)
    L = [f"KF-EICH zusammen ({erg['zeit']}), {len(dateien)} Dateien"]
    for tag in ("s03", "s01"):
        z = erg["vorhersagen_" + tag]
        L.append(f"== S0 {'0,3 (Haupt)' if tag == 's03' else '0,1 (Zusatz)'}")
        for nr in ("E0", "E1", "E2", "E3"):
            L.append(f"  {nr}: {z[nr]}" + (f" ({z[nr + '_zahl']})" if nr + "_zahl" in z else ""))
        L.append(f"  E2 Klassen: {z['E2_klassen']}")
        for x in z["E0_fehlschlaege"]:
            L.append(f"  E0-Fehlschlag: {json.dumps(x)}")
        L.append(f"  Bedeutung: {z['bedeutung']}")
    with open(frei_pfad(os.path.join(out, "zusammen.txt")), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


def main():
    ap = argparse.ArgumentParser(description="KF-EICH (Runde 21, v3)")
    ap.add_argument("befehl", choices=["lauf", "zusammen"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--stufe", choices=list(kg.STUFEN), default="grob")
    ap.add_argument("--gruppe", choices=list(GRUPPEN), default="alle")
    ap.add_argument("--rauch", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        kg.DEV = torch.device("cuda")
    else:
        if args.befehl != "zusammen":
            raise SystemExit("Rechnungen nur auf der GPU (PLAN.md)")
        kg.DEV = torch.device("cpu")
        torch.set_num_threads(1)
    print(f"kf_eich {args.befehl}: Start {jetzt()}", flush=True)
    {"lauf": befehl_lauf, "zusammen": befehl_zusammen}[args.befehl](args)
    print(f"kf_eich {args.befehl}: Ende {jetzt()}", flush=True)


if __name__ == "__main__":
    main()
