#!/usr/bin/env python3
"""KF-5 (Runde 6, v3): Geburt in 2D. Zerfaellt ein modulationsinstabiles Kondensat in getrennte Tropfen oder bleibt ein
Netz, und liegen die Tropfen auf der stationaeren 2D-Familie Q(omega)? (Stufe 5 "bildungsfaehig" der Stabilitaetsleiter)

Karte: coordination/runden-v3/REVIEW-FABLE-20260930/KARTEN-FABLE.md, Abschnitt KF-5; Auftrag RUNDE-06/AUFTRAG-KF4-KF5.md.
Explorativ. Vom Autor ohne Testlauf abgegeben. Plan, Aufrufe, Vorhersagen und Latten in PLAN.md daneben.

Modell und Numerik wie RUNDE-03/tests2d-r3/tests2d_r3.py (d = 2):
    psi_tt = Lap psi - U'(S) psi,  S = |psi|^2,  U = S - S^2 + S^3/2,  U'(S) = 1 - 2 S + 1,5 S^2.
    Kontrolle "frei": U = S (freies Klein-Gordon-Feld, keine Modulationsinstabilitaet), gleicher Start wie S0 = 0,3.
    Ladungsdichte rho = 2 Im(psi conj(psi_t)), Energiedichte |psi_t|^2 + |grad psi|^2 + U(S).
    Laplace spektral (FFT), Velocity-Verlet, float64 bzw. complex128. Periodische Box [-Box/2, Box/2)^2 OHNE Randschicht:
    Ladung und Energie bleiben in der Box, abgestrahlte Wellen laufen mehrfach durch (Grenze der Karte).
Start (wie Codex pde3d): psi = sqrt(S0) (1 + EPS eta), psi_t = -i omega0 psi, omega0^2 = U'(S0) (frei: 1).
    eta reell aus allen Moden 0 < |n| <= N_CUT (k = 2 pi n / Box) mit Gauss-Koeffizienten (fester Seed), RMS 1.
    eta haengt nicht von dx ab: grob und fein starten mit derselben kontinuierlichen Anfangsfunktion (L3).
Auswertung (fest vor dem Lauf, PLAN.md):
    - alle T_KON: Kontrast std(S)/mittel(S) und S_max.
    - alle T_AUS, zwei Schwellen S >= 2 S0 und 3 S0 (wie I14): periodische 4-Nachbar-Komponenten; Flaeche >= A_MIN zaehlt.
      Tropfen = nicht umspannend und kompakt (groesster Abstand vom Schwerpunkt <= KOMPAKT * sqrt(Flaeche/pi)).
      Umspannend = die Projektion der Komponente deckt alle Zeilen oder alle Spalten (notwendig fuer eine Windung).
      Je Tropfen (untere Schwelle): Q und E in der Scheibe R_A + R_PLUS um den Schwerpunkt (Pixel gehoert zum naechsten
      Zentrum), Hintergrund = Median ausserhalb aller Scheiben mal Scheibenflaeche; omega = sum(rho S)/(2 sum S^2) ueber
      die Komponente; Verschmelzungen und Teilungen ueber Maskenueberlapp zwischen zwei Auswertezeiten.
    - Messfenster [T_Ende - FENSTER, T_Ende], Abtastung DT_FENSTER: Tropfen verfolgen (Schwerpunkt mit Gewicht S^2 im Kern
      R_A), Kernphase arg(sum S psi), omega aus der Phasendrehung (Geradenfit der abgewickelten Phase), Q und E je Probe.
      Familientest gegen die 2D-Familie m = 0 (familie_2d_m0.json: Bio 18 aus Runde 4, Gegenprobe R3-Profilkontrolle).

Aufruf:  python kf5_geburt.py lauf --stufe grob|fein --arme s03,s01,... [--box 96] [--rauch] [--geraet cuda|cpu] [--out D]
         python kf5_geburt.py vergleich --ordner D [--geraet cpu]
         python kf5_geburt.py familie [--geraet cpu]
Rauchtest: --rauch (T_Ende 40, Fenster 10; Zahlen ungueltig, nur Durchlauf und Hochrechnung fuer den vollen Aufruf).
Nur fuer kleine Probelaeufe: --t-ende und --fenster ueberschreiben T_Ende und Fensterlaenge (im Ergebnis vermerkt).
"""
import argparse
import datetime
import glob
import json
import math
import os
import time

import torch

F64 = torch.float64
C128 = torch.complex128
DEV = torch.device("cpu")          # wird in main() gesetzt

# ---- Feste Parameter (vor dem Lauf in PLAN.md festgehalten) ----
BOX0 = 96.0                                        # Seitenlaenge der periodischen Box (Karte: L = 96)
STUFEN = {"grob": (0.25, 0.04), "fein": (0.125, 0.02)}   # dx, dt; dt * k_max = 0,71 auf beiden Gittern
T_ENDE, FENSTER = 800.0, 40.0
RAUCH_T_ENDE, RAUCH_FENSTER = 40.0, 10.0
T_KON, T_AUS, T_BILD, T_ZWISCHEN = 1.0, 10.0, 50.0, 100.0
DT_FENSTER = 1.0
EPS, N_CUT = 0.01, 16                              # 1 % Feldamplitude (wie Codex), Moden |n| <= 16 bei Box 96
FAKTOREN = (2, 3)                                  # Dichteschwellen f * S0 (wie I14)
A_MIN, KOMPAKT, R_PLUS, R_SUCH = 2.0, 2.0, 6.0, 2.0
KOMPAKT_FAMILIE = 1.3                              # Familientest nur fuer runde Tropfen (zwei beruehrende: 1,41)
KONTRAST_GRENZE = 0.05
FAM_TOL, Q_SCHWANK, MIN_ENTSCHEIDBAR = 0.10, 0.20, 5
ZEITGRENZE_S = 560.0
ARME = {
    "s03": {"S0": 0.3, "frei": False, "seed": 31},
    "s01": {"S0": 0.1, "frei": False, "seed": 31},
    "s08": {"S0": 0.8, "frei": False, "seed": 31},
    "frei": {"S0": 0.3, "frei": True, "seed": 31},
    "s03b": {"S0": 0.3, "frei": False, "seed": 73},
    "s01b": {"S0": 0.1, "frei": False, "seed": 73},
}
FAMILIE_DATEI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "familie_2d_m0.json")


# ---------------------------------------------------------------- Hilfen

def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "cpu"


def wrap_d(d, box):
    """Periodische Differenz in [-Box/2, Box/2]."""
    return d - box * torch.round(d / box)


def wrap_x(x, box):
    """Ort zurueck in [-Box/2, Box/2)."""
    return x - box * torch.floor((x + 0.5 * box) / box)


def z7(v):
    """Zahl fuer JSON: 7 signifikante Stellen; nicht endlich oder None -> None."""
    if v is None:
        return None
    v = float(v)
    return float(f"{v:.7g}") if math.isfinite(v) else None


def liste(t):
    return [z7(v) for v in t.tolist()]


def fz(v, fmt=".4g"):
    return "-" if v is None else format(v, fmt)


def median(werte):
    w = sorted(v for v in werte if v is not None)
    if not w:
        return None
    m = len(w) // 2
    return w[m] if len(w) % 2 else 0.5 * (w[m - 1] + w[m])


def quartile(werte):
    w = sorted(v for v in werte if v is not None)
    if not w:
        return None
    return [w[len(w) // 4], median(w), w[(3 * len(w)) // 4]]


# ---------------------------------------------------------------- Theorie des Kondensats [S]

def theorie(S0, frei, box):
    """Homogenes Kondensat psi = sqrt(S0) exp(-i omega0 t). Linearisiert (Betrag R0 + r, Phase omega0 t + phi):
    (k^2 - W^2)(k^2 - W^2 + 2 S0 U'') = 4 omega0^2 W^2; instabil fuer k^2 < -2 S0 U''(S0), also fuer S0 < 2/3.
    Staerkste Mode k*^2 = -b (2c + b)/(4c) mit b = 2 S0 U'', c = 4 omega0^2; Rate gamma_max = S0 |U''| / (2 omega0)."""
    if frei:
        return {"omega0": 1.0, "instabil": False, "q": 2.0 * S0, "E_zu_Q_kondensat": 1.0}
    up = 1.0 - 2.0 * S0 + 1.5 * S0 * S0
    upp = -2.0 + 3.0 * S0
    w0 = math.sqrt(up)
    q = 2.0 * w0 * S0
    aus = {"omega0": w0, "U2": upp, "instabil": upp < 0.0, "q": q,
           "E_zu_Q_kondensat": (up * S0 + S0 - S0 * S0 + 0.5 * S0 ** 3) / q}
    if upp < 0.0:
        b = 2.0 * S0 * upp
        c = 4.0 * up
        k2 = -b * (2.0 * c + b) / (4.0 * c)
        lam = 2.0 * math.pi / math.sqrt(k2)
        aus.update({"k_c": math.sqrt(-b), "k_max": math.sqrt(k2), "lambda_max": lam, "gamma_max": -S0 * upp / (2.0 * w0),
                    "q_lambda2": q * lam * lam, "zellen": (box / lam) ** 2})
    return aus


# ---------------------------------------------------------------- Stationaere 2D-Familie m = 0

class Familie:
    """Tabelle omega^2, Q, E aus familie_2d_m0.json; ln Q und E/Q quadratisch (drei naechste Punkte) in omega^2."""

    def __init__(self, pfad=FAMILIE_DATEI):
        with open(pfad) as fh:
            daten = json.load(fh)
        z = sorted((r for r in daten["zeilen"] if r["gueltig"]), key=lambda r: r["omega2"])
        self.quelle = daten["quelle"]
        self.w2 = [r["omega2"] for r in z]
        self.lnq = [math.log(r["Q"]) for r in z]
        self.eq = [r["E"] / r["Q"] for r in z]

    def _quad(self, werte, w2):
        if w2 < self.w2[0] - 1e-12 or w2 > self.w2[-1] + 1e-12:
            return None
        i = min(range(len(self.w2)), key=lambda j: abs(self.w2[j] - w2))
        i = min(max(i, 1), len(self.w2) - 2)
        x0, x1, x2 = self.w2[i - 1], self.w2[i], self.w2[i + 1]
        y0, y1, y2 = werte[i - 1], werte[i], werte[i + 1]
        return (y0 * (w2 - x1) * (w2 - x2) / ((x0 - x1) * (x0 - x2))
                + y1 * (w2 - x0) * (w2 - x2) / ((x1 - x0) * (x1 - x2))
                + y2 * (w2 - x0) * (w2 - x1) / ((x2 - x0) * (x2 - x1)))

    def q(self, omega):
        if omega is None or not math.isfinite(omega) or omega <= 0.0:
            return None
        v = self._quad(self.lnq, omega * omega)
        return None if v is None else math.exp(v)

    def omega2_bei_q(self, q):
        if q is None or not math.isfinite(q) or q <= 0.0:
            return None
        lq = math.log(q)
        if not (self.lnq[-1] <= lq <= self.lnq[0]):
            return None
        lo, hi = self.w2[0], self.w2[-1]
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if self._quad(self.lnq, mid) > lq:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    def eq_bei_q(self, q):
        w2 = self.omega2_bei_q(q)
        return None if w2 is None else self._quad(self.eq, w2)


def familien_klasse(fam, q, omega, u):
    """delta = Q / Q_fam(omega) - 1 mit Band aus omega -+ u (Q_fam faellt mit omega, also d_lo <= delta <= d_hi).
    auf: ganzes Band in +-FAM_TOL; neben: ganzes Band ausserhalb; sonst unentschieden; omega ausserhalb der Tabelle."""
    if q is None or q <= 0.0:
        return "ausserhalb", None, None, None
    qf = fam.q(omega)
    if qf is None:
        return "ausserhalb", None, None, None
    d = q / qf - 1.0
    q_lo, q_hi = fam.q(omega - u), fam.q(omega + u)
    if q_lo is None or q_hi is None:
        return "unentschieden", d, None, None
    d_lo, d_hi = q / q_lo - 1.0, q / q_hi - 1.0
    if d_lo >= -FAM_TOL and d_hi <= FAM_TOL:
        return "auf", d, d_lo, d_hi
    if d_hi < -FAM_TOL or d_lo > FAM_TOL:
        return "neben", d, d_lo, d_hi
    return "unentschieden", d, d_lo, d_hi


def familien_urteil(klassen):
    n_auf, n_neben = klassen.count("auf"), klassen.count("neben")
    n_ent = n_auf + n_neben
    if n_ent >= MIN_ENTSCHEIDBAR and n_auf >= 0.8 * n_ent:
        return "auf der Familie"
    if n_ent >= MIN_ENTSCHEIDBAR and n_neben >= 0.5 * n_ent:
        return "neben der Familie"
    return "nicht entscheidbar"


# ---------------------------------------------------------------- Gitter, Start, Zeitentwicklung

class Gitter:
    """Periodische Box [-Box/2, Box/2)^2, Felder als [y, x]. Das grobe Gitter ist Teilgitter des feinen."""

    def __init__(self, box, dx):
        n = int(round(box / dx))
        if abs(n * dx - box) > 1e-9 * box:
            raise SystemExit(f"Box {box} ist kein ganzzahliges Vielfaches von dx {dx}")
        self.box, self.dx, self.n, self.dA = box, dx, n, dx * dx
        self.x1 = -0.5 * box + dx * torch.arange(n, dtype=F64, device=DEV)
        self.X = self.x1.view(1, n).expand(n, n)
        self.Y = self.x1.view(n, 1).expand(n, n)
        k = 2.0 * math.pi * torch.fft.fftfreq(n, d=dx, dtype=F64, device=DEV)
        self.kx = k.view(1, n)
        self.ky = k.view(n, 1)
        self.mk2 = -(self.kx ** 2 + self.ky ** 2)


def rauschen(g, seed):
    """eta(x, y) = Re sum c_ab exp(i k1 (a y + b x)), 0 < a^2 + b^2 <= nc^2, k1 = 2 pi / Box, c komplex gaussisch mit
    festem Seed (CPU-Generator), RMS 1. Unabhaengig von dx; nc waechst mit der Box (gleicher k-Bereich)."""
    nc = int(round(N_CUT * g.box / BOX0))
    gen = torch.Generator().manual_seed(seed)
    m = 2 * nc + 1
    re = torch.randn(m, m, generator=gen, dtype=F64)
    im = torch.randn(m, m, generator=gen, dtype=F64)
    j = torch.arange(-nc, nc + 1, dtype=F64)
    jy, jx = j.view(-1, 1), j.view(1, -1)
    auswahl = ((jy * jy + jx * jx <= nc * nc) & ((jy != 0) | (jx != 0))).to(F64)
    c = (torch.complex(re, im) * auswahl).to(DEV)                       # [Mode y, Mode x]
    welle = torch.exp(1j * (2.0 * math.pi / g.box) * (j.to(DEV).view(-1, 1) * g.x1.view(1, -1)))   # (m, n)
    eta = (welle.T @ c @ welle).real                                     # (n, n) = [y, x]
    eta = eta - eta.mean()
    return eta / torch.sqrt((eta * eta).mean())


def startfeld(g, arm):
    th = theorie(arm["S0"], arm["frei"], g.box)
    psi = (math.sqrt(arm["S0"]) * (1.0 + EPS * rauschen(g, arm["seed"]))).to(C128)
    return psi, -1j * th["omega0"] * psi


def kraft_fn(g, nl):
    """psi_tt = Lap psi - U'(S) psi; nl = 0 (frei, U' = 1) oder 1 je Arm, Form (B, 1, 1)."""
    def kraft(p):
        lap = torch.fft.ifft2(torch.fft.fft2(p) * g.mk2)
        s = p.real * p.real + p.imag * p.imag
        return lap - (1.0 + nl * s * (1.5 * s - 2.0)) * p
    return kraft


def dichten(g, psi, vel, nl):
    """S, Ladungsdichte, Energiedichte fuer den Stapel (B, n, n)."""
    s = psi.real ** 2 + psi.imag ** 2
    rho = 2.0 * (psi * vel.conj()).imag
    ph = torch.fft.fft2(psi)
    gx = torch.fft.ifft2(ph * (1j * g.kx))
    gy = torch.fft.ifft2(ph * (1j * g.ky))
    e = (vel.real ** 2 + vel.imag ** 2 + gx.real ** 2 + gx.imag ** 2 + gy.real ** 2 + gy.imag ** 2
         + s + nl * (0.5 * s - 1.0) * s * s)
    return s, rho, e


# ---------------------------------------------------------------- Komponenten und Tropfen

def komponenten(maske):
    """Periodische 4-Nachbar-Zusammenhangskomponenten einer (n, n)-Maske: Minimum-Etikett-Ausbreitung mit Zeigersprung.
    Etikett = kleinster Pixelindex der Komponente. Rueckgabe: Etiketten 0..K-1 (ausserhalb -1), K, Iterationen."""
    n0, n1 = maske.shape
    gross = n0 * n1
    idx = torch.arange(gross, device=maske.device).view(n0, n1)
    lab = torch.where(maske, idx, torch.full_like(idx, gross))
    it = 0
    while True:
        it += 1
        nb = torch.minimum(torch.minimum(torch.roll(lab, 1, 0), torch.roll(lab, -1, 0)),
                           torch.minimum(torch.roll(lab, 1, 1), torch.roll(lab, -1, 1)))
        neu = torch.where(maske, torch.minimum(lab, nb), lab)
        neu = torch.where(maske, neu.flatten()[neu.clamp(max=gross - 1)], neu)
        if torch.equal(neu, lab):
            break
        lab = neu
        if it > gross:
            raise RuntimeError("Komponentensuche konvergiert nicht")
    werte, inv = torch.unique(lab[maske], return_inverse=True)
    etik = torch.full_like(idx, -1)
    etik[maske] = inv
    return etik, int(werte.numel()), it


def eigenschaften(g, etik, K, s, rho):
    """Je Komponente: Flaeche, R_A, S_max, Schwerpunkt (Gewicht S, periodisch ueber die Spitze), groesster Abstand vom
    Schwerpunkt, Umspannen (Projektion deckt alle Zeilen oder alle Spalten), Ladung in der Maske, omega."""
    n = g.n
    m = etik >= 0
    e = etik[m]
    flach = torch.arange(n * n, device=DEV).view(n, n)[m]
    zeile, spalte = flach // n, flach % n
    sm, rm = s[m], rho[m]
    flaeche = torch.bincount(e, minlength=K).to(F64) * g.dA
    smax = torch.zeros(K, dtype=F64, device=DEV).scatter_reduce(0, e, sm, reduce="amax", include_self=False)
    kand = torch.where(sm == smax[e], flach.to(F64), torch.full_like(sm, float(n * n)))
    spitze = torch.full((K,), float(n * n), dtype=F64, device=DEV).scatter_reduce(
        0, e, kand, reduce="amin", include_self=True).long()
    xp, yp = g.x1[spitze % n], g.x1[spitze // n]
    ddx = wrap_d(g.x1[spalte] - xp[e], g.box)
    ddy = wrap_d(g.x1[zeile] - yp[e], g.box)
    ws = torch.bincount(e, weights=sm, minlength=K)
    ox = torch.bincount(e, weights=sm * ddx, minlength=K) / ws
    oy = torch.bincount(e, weights=sm * ddy, minlength=K) / ws
    rx = wrap_d(ddx - ox[e], g.box)
    ry = wrap_d(ddy - oy[e], g.box)
    rmax = torch.zeros(K, dtype=F64, device=DEV).scatter_reduce(
        0, e, torch.sqrt(rx * rx + ry * ry), reduce="amax", include_self=False)
    zeilen_je = torch.bincount(torch.unique(e * n + zeile) // n, minlength=K)
    spalten_je = torch.bincount(torch.unique(e * n + spalte) // n, minlength=K)
    omega = (torch.bincount(e, weights=rm * sm, minlength=K)
             / (2.0 * torch.bincount(e, weights=sm * sm, minlength=K)))
    return {"flaeche": flaeche, "ra": torch.sqrt(flaeche / math.pi), "smax": smax,
            "x": wrap_x(xp + ox, g.box), "y": wrap_x(yp + oy, g.box), "rmax": rmax,
            "umspannt": (zeilen_je == n) | (spalten_je == n),
            "q_maske": torch.bincount(e, weights=rm, minlength=K) * g.dA, "omega": omega}


def scheiben(g, s, rho, e, psi, xs, ys, ra):
    """Je Tropfen k (Zentrum xs, ys): Pixel gehoert zum naechsten Zentrum (periodisch). Scheibe: Abstand <= ra_k + R_PLUS,
    Kern: Abstand <= ra_k. Q, E in der Scheibe roh und netto (Hintergrund = Median ausserhalb aller Scheiben mal
    Scheibenflaeche); im Kern: neuer Schwerpunkt (Gewicht S^2), Phase arg(sum S psi), omega = sum(rho S)/(2 sum S^2), S_max."""
    K = xs.numel()
    dmin = torch.full_like(s, float("inf"))
    eig = torch.full(s.shape, -1, dtype=torch.long, device=DEV)
    bx = torch.zeros_like(s)
    by = torch.zeros_like(s)
    for k in range(K):
        ddx = wrap_d(g.X - xs[k], g.box)
        ddy = wrap_d(g.Y - ys[k], g.box)
        d2 = ddx * ddx + ddy * ddy
        nah = d2 < dmin
        dmin = torch.where(nah, d2, dmin)
        eig = torch.where(nah, torch.full_like(eig, k), eig)
        bx = torch.where(nah, ddx, bx)
        by = torch.where(nah, ddy, by)
    drin = eig >= 0
    rk = ra[eig.clamp(min=0)]
    scheibe = drin & (dmin <= (rk + R_PLUS) ** 2)
    kern = drin & (dmin <= rk * rk)
    aussen = ~scheibe
    if bool(aussen.any()):
        rho_bg, e_bg = rho[aussen].median(), e[aussen].median()
    else:
        rho_bg = e_bg = torch.zeros((), dtype=F64, device=DEV)
    o, ok = eig[scheibe], eig[kern]
    fl = torch.bincount(o, minlength=K).to(F64) * g.dA
    q_roh = torch.bincount(o, weights=rho[scheibe], minlength=K) * g.dA
    e_roh = torch.bincount(o, weights=e[scheibe], minlength=K) * g.dA
    s2 = (s * s)[kern]
    w = torch.bincount(ok, weights=s2, minlength=K)
    wn = w.clamp(min=1e-300)
    cx = torch.bincount(ok, weights=s2 * bx[kern], minlength=K) / wn
    cy = torch.bincount(ok, weights=s2 * by[kern], minlength=K) / wn
    zr = torch.bincount(ok, weights=(s * psi.real)[kern], minlength=K)
    zi = torch.bincount(ok, weights=(s * psi.imag)[kern], minlength=K)
    om = torch.bincount(ok, weights=(rho * s)[kern], minlength=K) / (2.0 * wn)
    smax = torch.zeros(K, dtype=F64, device=DEV).scatter_reduce(0, ok, s[kern], reduce="amax", include_self=False)
    return {"q_roh": q_roh, "e_roh": e_roh, "q_net": q_roh - rho_bg * fl, "e_net": e_roh - e_bg * fl, "flaeche": fl,
            "x": wrap_x(xs + cx, g.box), "y": wrap_x(ys + cy, g.box), "phase": torch.atan2(zi, zr), "omega": om,
            "smax": smax, "leer": w <= 0.0, "rho_bg": rho_bg, "e_bg": e_bg}


def verknuepfung(alt, neu):
    """Verschmelzungen (neue Komponente ueberlappt >= 2 alte) und Teilungen (alte ueberlappt >= 2 neue)."""
    if alt is None or neu is None:
        return 0, 0
    beide = (alt >= 0) & (neu >= 0)
    if not bool(beide.any()):
        return 0, 0
    a, b = alt[beide], neu[beide]
    ka, kb = int(a.max()) + 1, int(b.max()) + 1
    u = torch.unique(a * kb + b)
    eltern = torch.bincount(u % kb, minlength=kb)
    kinder = torch.bincount(u // kb, minlength=ka)
    return int((eltern >= 2).sum()), int((kinder >= 2).sum())


def analyse_arm(g, s, rho, e, psi, S0, fam, alt):
    """Auswertung eines Arms (Felder (n, n)) zu einem Zeitpunkt. alt: Etiketten der vorigen Auswertung (untere Schwelle,
    nur Komponenten >= A_MIN). Rueckgabe: Zeile (JSON), neue Etiketten, Tropfen der unteren Schwelle (oder None)."""
    zeile = {"schwellen": {}}
    neu_etik, tropfen = None, None
    for f in FAKTOREN:
        maske = s >= f * S0
        etik, K, it = komponenten(maske)
        z = {"schwelle": f * S0, "iterationen": it, "masken_anteil": z7(maske.to(F64).mean()), "N_komp": 0,
             "N_klein": 0, "N_tropfen": 0, "N_netz": 0, "umspannt": False, "anteil_groesste": None,
             "anteil_tropfen": None}
        if K > 0:
            ei = eigenschaften(g, etik, K, s, rho)
            gg = ei["flaeche"] >= A_MIN
            tr = gg & ~ei["umspannt"] & (ei["rmax"] <= KOMPAKT * ei["ra"])
            z.update({"N_komp": int(gg.sum()), "N_klein": int((~gg).sum()), "N_tropfen": int(tr.sum()),
                      "N_netz": int((gg & ~tr).sum()), "umspannt": bool((gg & ei["umspannt"]).any())})
            if bool(gg.any()):
                fl_gg = (ei["flaeche"] * gg).sum()
                z["anteil_groesste"] = z7((ei["flaeche"] * gg).max() / fl_gg)
                z["anteil_tropfen"] = z7((ei["flaeche"] * tr).sum() / fl_gg)
            if f == FAKTOREN[0]:
                neu_etik = torch.where((etik >= 0) & gg[etik.clamp(min=0)], etik, torch.full_like(etik, -1))
                ids = tr.nonzero().flatten()
                if ids.numel() > 0:
                    xs, ys, ra = ei["x"][ids], ei["y"][ids], ei["ra"][ids]
                    sch = scheiben(g, s, rho, e, psi, xs, ys, ra)
                    om = ei["omega"][ids]
                    rund = ei["rmax"][ids] / ra
                    tropfen = {"x": xs, "y": ys, "ra": ra, "rund": rund <= KOMPAKT_FAMILIE}
                    dq = []
                    for qn, w in zip(sch["q_net"].tolist(), om.tolist()):
                        qf = fam.q(w)
                        dq.append(z7(qn / qf - 1.0) if qf else None)
                    zeile["tropfen"] = {"x": liste(xs), "y": liste(ys), "A": liste(ei["flaeche"][ids]),
                                        "S_max": liste(ei["smax"][ids]), "Q_maske": liste(ei["q_maske"][ids]),
                                        "Q_roh": liste(sch["q_roh"]), "Q_net": liste(sch["q_net"]),
                                        "E_net": liste(sch["e_net"]), "omega": liste(om), "dQ_familie": dq,
                                        "rmax_zu_ra": liste(rund)}
                    zeile["hintergrund"] = {"rho": z7(sch["rho_bg"]), "e": z7(sch["e_bg"])}
        zeile["schwellen"][str(f)] = z
    zeile["verschmelzungen"], zeile["teilungen"] = verknuepfung(alt, neu_etik)
    return zeile, neu_etik, tropfen


# ---------------------------------------------------------------- Messfenster am Ende

def fenster_start(tropfen):
    if tropfen is None:
        return None
    return {"x": tropfen["x"].clone(), "y": tropfen["y"].clone(), "ra": tropfen["ra"].clone(),
            "rund": tropfen["rund"].clone(), "proben": []}


def fenster_probe(g, fzs, s, rho, e, psi):
    sch = scheiben(g, s, rho, e, psi, fzs["x"], fzs["y"], fzs["ra"])
    sprung = torch.sqrt(wrap_d(sch["x"] - fzs["x"], g.box) ** 2 + wrap_d(sch["y"] - fzs["y"], g.box) ** 2)
    verloren = sch["leer"] | (sprung > R_SUCH)
    K = fzs["x"].numel()
    ddx = wrap_d(sch["x"].view(-1, 1) - sch["x"].view(1, -1), g.box)
    ddy = wrap_d(sch["y"].view(-1, 1) - sch["y"].view(1, -1), g.box)
    eng = ((torch.sqrt(ddx * ddx + ddy * ddy) < fzs["ra"].view(-1, 1) + fzs["ra"].view(1, -1))
           & ~torch.eye(K, dtype=torch.bool, device=DEV))
    fzs["proben"].append(torch.stack([sch["phase"], sch["omega"], sch["smax"], sch["q_roh"], sch["q_net"],
                                      sch["e_net"], sch["x"], sch["y"], verloren.to(F64), eng.any(1).to(F64)]))
    fzs["x"], fzs["y"] = sch["x"], sch["y"]


def steigung(t, y):
    tm, ym = t.mean(), y.mean()
    return (((t - tm) * (y - ym)).sum() / ((t - tm) ** 2).sum()).item()


def fenster_auswerten(fzs, t0, dtf, fam, box):
    """Je verfolgtem Tropfen: omega aus der Phasendrehung am bewegten Schwerpunkt. Ein Ball mit Geschwindigkeit v dreht
    dort mit omega/gamma (psi = f(gamma(x - v t)) exp(i omega gamma (v x - t))); daher omega_ruhe = omega_rot * gamma,
    v aus dem Geradenfit der Schwerpunktbahn. Gegenprobe: omega_inst (rho/2S) misst omega * gamma, also ist
    sqrt(omega_rot * omega_inst) ebenfalls omega_ruhe. Q ist invariant, E_ruhe = E / gamma."""
    leer = {"tropfen": [], "zaehlung": {}, "urteil": "keine Tropfen im Fenster", "urteil_roh": "keine Tropfen im Fenster"}
    if fzs is None or len(fzs["proben"]) < 4:
        return leer
    d = torch.stack(fzs["proben"]).cpu()                   # (M, 10, K)
    rund = fzs["rund"].cpu().tolist()
    M, K = d.shape[0], d.shape[2]
    t = t0 + dtf * torch.arange(M, dtype=F64)
    h = M // 2
    aus = []
    for k in range(K):
        ph, wi = d[:, 0, k], d[:, 1, k]
        pred = -wi[:-1] * dtf                                  # erwartete Phasenaenderung (psi ~ exp(-i omega t))
        korr = torch.remainder(ph[1:] - ph[:-1] - pred + math.pi, 2.0 * math.pi) - math.pi
        pu = torch.cat([ph[:1], ph[:1] + torch.cumsum(pred + korr, 0)])
        om = -steigung(t, pu)
        u = abs(steigung(t[:h + 1], pu[:h + 1]) - steigung(t[h:], pu[h:]))
        xk, yk = d[:, 6, k], d[:, 7, k]
        xu = torch.cat([xk[:1], xk[:1] + torch.cumsum(wrap_d(xk[1:] - xk[:-1], box), 0)])
        yu = torch.cat([yk[:1], yk[:1] + torch.cumsum(wrap_d(yk[1:] - yk[:-1], box), 0)])
        v = math.hypot(steigung(t, xu), steigung(t, yu))
        gam = 1.0 / math.sqrt(1.0 - v * v) if v < 0.99 else float("inf")
        om_r, u_r = om * gam, u * gam
        qn, qr, en = d[:, 4, k], d[:, 3, k], d[:, 5, k]
        q, q_roh, e_r = qn.mean().item(), qr.mean().item(), en.mean().item() / gam
        schwank = ((qn.max() - qn.min()).item() / abs(q)) if q != 0.0 else float("inf")
        verl, stoss = bool(d[:, 8, k].max() > 0.5), bool(d[:, 9, k].max() > 0.5)
        ungestoert = (not verl) and (not stoss) and schwank <= Q_SCHWANK and q > 0.0 and math.isfinite(gam)
        if not rund[k]:
            kl, dq, dlo, dhi, kl_roh = "nicht rund", None, None, None, "nicht rund"
        elif ungestoert:
            kl, dq, dlo, dhi = familien_klasse(fam, q, om_r, u_r)
            kl_roh = familien_klasse(fam, q_roh, om_r, u_r)[0]
        else:
            kl, dq, dlo, dhi, kl_roh = "gestoert", None, None, None, "gestoert"
        w2f = fam.omega2_bei_q(q)
        wim = wi.mean().item()
        aus.append({"k": k, "x0": z7(d[0, 6, k]), "y0": z7(d[0, 7, k]), "v": z7(v), "Q_net": z7(q), "Q_roh": z7(q_roh),
                    "E_ruhe_net": z7(e_r), "E_zu_Q": z7(e_r / q) if q > 0.0 else None,
                    "E_zu_Q_familie": z7(fam.eq_bei_q(q)), "omega_rot": z7(om), "omega_ruhe": z7(om_r),
                    "u_omega": z7(u_r), "omega_inst_mittel": z7(wim),
                    "omega_geo": z7(math.sqrt(om * wim)) if om * wim > 0.0 else None,
                    "omega_familie_bei_Q": z7(math.sqrt(w2f)) if w2f is not None else None,
                    "S_max_mittel": z7(d[:, 2, k].mean()), "Q_schwankung": z7(schwank), "verloren": verl,
                    "stoss": stoss, "rund": bool(rund[k]), "klasse": kl, "klasse_roh": kl_roh, "dQ": z7(dq),
                    "dQ_band": [z7(dlo), z7(dhi)]})
    klassen = [a["klasse"] for a in aus]
    klassen_roh = [a["klasse_roh"] for a in aus]
    zaehlung = {kl: klassen.count(kl) for kl in ("auf", "neben", "unentschieden", "ausserhalb", "gestoert", "nicht rund")}
    return {"tropfen": aus, "zaehlung": zaehlung, "urteil": familien_urteil(klassen),
            "urteil_roh": familien_urteil(klassen_roh)}


# ---------------------------------------------------------------- Kennzahlen, Bericht

def urteil_netz(z):
    if z["umspannt"]:
        return "Netz"
    if z["N_komp"] == 0:
        return "keine Verdichtung"
    if z["N_tropfen"] > 0 and (z["anteil_tropfen"] or 0.0) >= 0.8:
        return "getrennte Tropfen"
    return "gemischt"


def kennzahlen(th, kon_t, kon, aus, fen):
    k = {}
    k0 = kon[0]
    t_sat = None                                           # linear interpoliert zwischen den Abtastpunkten (L3)
    for i in range(1, len(kon)):
        if kon[i] >= 0.5 > kon[i - 1]:
            t_sat = kon_t[i - 1] + (0.5 - kon[i - 1]) / (kon[i] - kon[i - 1]) * (kon_t[i] - kon_t[i - 1])
            break
    pkt = [(t, math.log(v)) for t, v in zip(kon_t, kon) if 3.0 * k0 <= v <= 0.3 and (t_sat is None or t <= t_sat)]
    gam = None
    if len(pkt) >= 5:
        tm = sum(p[0] for p in pkt) / len(pkt)
        ym = sum(p[1] for p in pkt) / len(pkt)
        gam = sum((p[0] - tm) * (p[1] - ym) for p in pkt) / sum((p[0] - tm) ** 2 for p in pkt)
    k.update({"kontrast_start": z7(k0), "kontrast_max": z7(max(kon)), "T_sat": t_sat, "gamma_mess": z7(gam),
              "n_fitpunkte": len(pkt),
              "gamma_verhaeltnis": z7(gam / th["gamma_max"]) if (gam is not None and th.get("gamma_max")) else None})
    ts = [z["t"] for z in aus]
    unten = [z["schwellen"]["2"] for z in aus]
    oben = [z["schwellen"]["3"] for z in aus]
    span = [t for t, z in zip(ts, unten) if z["umspannt"]]
    k["t_erst_umspannt"] = span[0] if span else None
    k["t_letzt_umspannt"] = span[-1] if span else None
    n_tr = [z["N_tropfen"] for z in unten]
    k["N_tropfen_max"] = max(n_tr)
    i_max = n_tr.index(k["N_tropfen_max"])
    k["t_N_max"] = ts[i_max]
    k["N_tropfen_verlauf"] = {f"{t:g}": n for t, n in zip(ts, n_tr) if t in (30.0, 50.0, 100.0, 200.0, 400.0, 600.0, 800.0)}

    def q_liste(i):
        return aus[i].get("tropfen", {}).get("Q_net", [])

    def e_liste(i):
        return aus[i].get("tropfen", {}).get("E_net", [])

    k["erste_generation"] = {"t": ts[i_max], "N": n_tr[i_max], "Q_quartile": quartile(q_liste(i_max)),
                             "vorhersage_q_lambda2": z7(th.get("q_lambda2"))}
    ende = unten[-1]
    k["urteil_netz"] = urteil_netz(ende)
    k["urteil_netz_oben"] = urteil_netz(oben[-1])
    k["ende"] = {"t": ts[-1], "N_tropfen": ende["N_tropfen"], "N_komp": ende["N_komp"], "N_netz": ende["N_netz"],
                 "N_tropfen_oben": oben[-1]["N_tropfen"], "anteil_groesste": ende["anteil_groesste"],
                 "Q_quartile": quartile(q_liste(-1)),
                 "Q_in_tropfen_anteil": z7(sum(v for v in q_liste(-1) if v is not None) / aus[-1]["Q_box"]),
                 "E_in_tropfen_anteil": z7(sum(v for v in e_liste(-1) if v is not None) / aus[-1]["E_box"])}
    k["verschmelzungen"] = sum(z["verschmelzungen"] for z in aus)
    k["teilungen"] = sum(z["teilungen"] for z in aus)
    q0, e0 = aus[0]["Q_box"], aus[0]["E_box"]
    k["drift_Q"] = z7(max(abs(z["Q_box"] / q0 - 1.0) for z in aus))
    k["drift_E"] = z7(max(abs(z["E_box"] / e0 - 1.0) for z in aus))
    kontrast_ok = max(kon) < KONTRAST_GRENZE
    keine = all(z["N_komp"] == 0 for z in unten + oben)
    k["kontrolle"] = {"kontrast_unter_0_05": kontrast_ok, "keine_komponenten": keine, "bestanden": kontrast_ok and keine}
    k["familie"] = {"urteil": fen["urteil"], "urteil_roh": fen["urteil_roh"], "zaehlung": fen["zaehlung"]}
    return k


def ergebnis_bauen(meta, namen, arme, theo, kon_t, kon_k, kon_m, aus, fen_erg, fertig):
    kk = torch.stack(kon_k).cpu()
    km = torch.stack(kon_m).cpu()
    arme_out = {}
    for b, nm in enumerate(namen):
        eintrag = {"arm": arme[b], "theorie": {x: (z7(v) if isinstance(v, float) else v) for x, v in theo[b].items()},
                   "reihe_kontrast": {"t": kon_t, "kontrast": liste(kk[:, b]), "S_max": liste(km[:, b])},
                   "reihe_auswertung": aus[nm]}
        if fertig:
            eintrag["fenster"] = fen_erg[b]
            eintrag["kennzahlen"] = kennzahlen(theo[b], kon_t, kk[:, b].tolist(), aus[nm], fen_erg[b])
        arme_out[nm] = eintrag
    return {**meta, "fertig": fertig, "arme": arme_out}


def schreiben_json(out, name, erg):
    pfad = os.path.join(out, name + "_ergebnis.json")
    with open(pfad + ".tmp", "w") as fh:
        json.dump(erg, fh)
    os.replace(pfad + ".tmp", pfad)


def bericht_text(erg):
    L = [f"KF-5 Geburt in 2D, Aufruf {erg['name']}. Start {erg['start']}, Ende {erg['ende']}, {erg['geraet']}, "
         f"torch {erg['torch']}" + (" RAUCHTEST: Zahlen ungueltig" if erg["rauch"] else "")]
    L.append(f"Gitter: Box {erg['box']}, dx {erg['dx']}, dt {erg['dt']}, n {erg['n']}, T_Ende {erg['t_ende']}, "
             f"Fenster {erg['fenster']}; GPU-Speicher max {fz(erg.get('gpu_speicher_mb'), '.0f')} MB")
    L.append("Dauer [s]: " + ", ".join(f"{x} {v:.1f}" for x, v in erg["dauer_s"].items()))
    if erg.get("prognose_voll_s") is not None:
        L.append(f"Hochrechnung fuer denselben Aufruf mit T_Ende {T_ENDE:g}: {erg['prognose_voll_s']:.0f} s "
                 "(Auswertung x 2 gerechnet); ueber 540 s: Aufruf teilen (--arme einzeln).")
    for nm, a in erg["arme"].items():
        th, k = a["theorie"], a.get("kennzahlen")
        L.append(f"Arm {nm}: S0 {a['arm']['S0']}, frei {a['arm']['frei']}, Seed {a['arm']['seed']}. Theorie: omega0 "
                 f"{fz(th.get('omega0'))}, gamma_max {fz(th.get('gamma_max'))}, lambda_max {fz(th.get('lambda_max'))}, "
                 f"q lambda^2 {fz(th.get('q_lambda2'))}, Zellen {fz(th.get('zellen'))}, E/Q Kondensat "
                 f"{fz(th.get('E_zu_Q_kondensat'))}")
        if not k:
            continue
        L.append(f"  Wachstum: Kontrast Start {fz(k['kontrast_start'])}, max {fz(k['kontrast_max'])}; T_sat (Kontrast >= 0,5) "
                 f"{fz(k['T_sat'])}; gamma_mess {fz(k['gamma_mess'])} ({k['n_fitpunkte']} Punkte), "
                 f"gamma_mess/gamma_max {fz(k['gamma_verhaeltnis'])}")
        L.append(f"  Netz: umspannend zuerst {fz(k['t_erst_umspannt'])}, zuletzt {fz(k['t_letzt_umspannt'])}; N_Tropfen max "
                 f"{k['N_tropfen_max']} bei t {fz(k['t_N_max'])}; Verlauf {json.dumps(k['N_tropfen_verlauf'])}")
        eg, en = k["erste_generation"], k["ende"]
        L.append(f"  Erste Generation (t {fz(eg['t'])}, N {eg['N']}): Q-Quartile {json.dumps(eg['Q_quartile'])}, "
                 f"Vorhersage q lambda^2 {fz(eg['vorhersage_q_lambda2'])}")
        L.append(f"  Ende t {fz(en['t'])}: Urteil {k['urteil_netz']} (obere Schwelle: {k['urteil_netz_oben']}); "
                 f"N_Tropfen {en['N_tropfen']} (oben {en['N_tropfen_oben']}), N_Netz {en['N_netz']}, groesste "
                 f"{fz(en['anteil_groesste'])}; Q-Quartile {json.dumps(en['Q_quartile'])}; Ladung in Tropfen "
                 f"{fz(en['Q_in_tropfen_anteil'])}, Energie in Tropfen {fz(en['E_in_tropfen_anteil'])}")
        L.append(f"  Verschmelzungen {k['verschmelzungen']}, Teilungen {k['teilungen']} (Maskendiagnose); Drift Q "
                 f"{fz(k['drift_Q'], '.1e')}, E {fz(k['drift_E'], '.1e')}; Kontrolle (Kontrast < 0,05, keine Komponente): "
                 f"{'bestanden' if k['kontrolle']['bestanden'] else 'nicht bestanden'}")
        fa = k["familie"]
        L.append(f"  Familie (Fenster): {json.dumps(fa['zaehlung'])}; Urteil {fa['urteil']} (mit Q_roh: {fa['urteil_roh']})")
        for tr in a["fenster"]["tropfen"][:40]:
            L.append(f"    k {tr['k']:3d} | Q {fz(tr['Q_net'])} | v {fz(tr['v'], '.3f')} | omega_ruhe "
                     f"{fz(tr['omega_ruhe'], '.5f')} +- {fz(tr['u_omega'], '.1e')} (geo {fz(tr['omega_geo'], '.5f')}) | "
                     f"omega_fam(Q) {fz(tr['omega_familie_bei_Q'], '.5f')} | dQ {fz(tr['dQ'], '+.3f')} | E/Q "
                     f"{fz(tr['E_zu_Q'], '.4f')} fam {fz(tr['E_zu_Q_familie'], '.4f')} | {tr['klasse']}")
    return "\n".join(L)


# ---------------------------------------------------------------- Unterbefehl lauf

def lauf(args):
    fam = Familie()
    dx, dt = STUFEN[args.stufe]
    box = float(args.box)
    t_ende = args.t_ende if args.t_ende is not None else (RAUCH_T_ENDE if args.rauch else T_ENDE)
    fenster = args.fenster if args.fenster is not None else (RAUCH_FENSTER if args.rauch else FENSTER)
    namen = [a for a in args.arme.split(",") if a]
    for nm in namen:
        if nm not in ARME:
            raise SystemExit(f"unbekannter Arm {nm}; erlaubt: {', '.join(ARME)}")
    q_fen = (t_ende - fenster) / T_AUS
    if fenster < 4.0 * DT_FENSTER or fenster >= t_ende or abs(q_fen - round(q_fen)) > 1e-9:
        raise SystemExit("Fensterbeginn T_Ende - Fenster muss ein Vielfaches von T_AUS sein (Fenster >= 4)")
    start = jetzt()
    t_start = uhr()
    g = Gitter(box, dx)
    arme = [ARME[nm] for nm in namen]
    B = len(namen)
    theo = [theorie(a["S0"], a["frei"], box) for a in arme]
    felder = [startfeld(g, a) for a in arme]
    psi = torch.stack([f[0] for f in felder]).contiguous()
    vel = torch.stack([f[1] for f in felder]).contiguous()
    del felder
    nl = torch.tensor([0.0 if a["frei"] else 1.0 for a in arme], dtype=F64, device=DEV).view(-1, 1, 1)
    kraft = kraft_fn(g, nl)
    n_schritte = int(round(t_ende / dt))
    je_kon, je_aus, je_fen, je_bild, je_zw = (int(round(x / dt)) for x in (T_KON, T_AUS, DT_FENSTER, T_BILD, T_ZWISCHEN))
    s_fen = int(round((t_ende - fenster) / dt))
    st_bild = max(1, int(round(0.5 / dx)))
    name = f"{args.stufe}_box{int(round(box))}_{'-'.join(namen)}" + ("_rauch" if args.rauch else "")
    out = args.out
    os.makedirs(out, exist_ok=True)
    meta = {"karte": "KF-5", "name": name, "start": start, "ende": None, "rauch": args.rauch, "geraet": geraet_name(),
            "torch": torch.__version__, "stufe": args.stufe, "dx": dx, "dt": dt, "box": box, "n": g.n,
            "t_ende": t_ende, "fenster": fenster, "familie_quelle": fam.quelle,
            "parameter": {"EPS": EPS, "N_CUT_bei_Box96": N_CUT, "FAKTOREN": list(FAKTOREN), "A_MIN": A_MIN,
                          "KOMPAKT": KOMPAKT, "KOMPAKT_FAMILIE": KOMPAKT_FAMILIE, "R_PLUS": R_PLUS, "R_SUCH": R_SUCH, "T_KON": T_KON, "T_AUS": T_AUS,
                          "DT_FENSTER": DT_FENSTER, "FAM_TOL": FAM_TOL, "Q_SCHWANK": Q_SCHWANK,
                          "MIN_ENTSCHEIDBAR": MIN_ENTSCHEIDBAR, "KONTRAST_GRENZE": KONTRAST_GRENZE}}
    print(f"KF-5 lauf {name}: Start {start} auf {geraet_name()}, torch {torch.__version__}, n {g.n}, B {B}, "
          f"{n_schritte} Schritte bis T {t_ende:g}, Fenster ab {t_ende - fenster:g}", flush=True)
    for nm, th in zip(namen, theo):
        print(f"  Theorie {nm}: " + json.dumps({x: (z7(v) if isinstance(v, float) else v) for x, v in th.items()}),
              flush=True)

    kon_t, kon_k, kon_m = [], [], []
    aus = {nm: [] for nm in namen}
    alt = [None] * B
    fzs = [None] * B
    bild_t, bilder = [], []
    dauer = {"auswertung": 0.0, "fenster": 0.0}
    n_aus = n_fen = 0
    t_lauf = uhr()
    F = kraft(psi)
    for schritt in range(n_schritte + 1):
        if schritt > 0:
            vel.add_(F, alpha=0.5 * dt)
            psi.add_(vel, alpha=dt)
            F = kraft(psi)
            vel.add_(F, alpha=0.5 * dt)
        t = round(schritt * dt, 6)
        if schritt % je_kon == 0:
            s = psi.real ** 2 + psi.imag ** 2
            mw = s.mean((1, 2))
            kon_t.append(t)
            kon_k.append(torch.sqrt(((s - mw.view(-1, 1, 1)) ** 2).mean((1, 2))) / mw)
            kon_m.append(s.amax((1, 2)))
        a_jetzt = schritt % je_aus == 0
        f_jetzt = schritt >= s_fen and (schritt - s_fen) % je_fen == 0
        b_jetzt = schritt % je_bild == 0 or schritt == n_schritte
        if not (a_jetzt or f_jetzt or b_jetzt):
            continue
        s, rho, e = dichten(g, psi, vel, nl)
        if b_jetzt:
            bild_t.append(t)
            bilder.append(s[:, ::st_bild, ::st_bild].to(torch.float32).cpu())
        if a_jetzt:
            ta = uhr()
            q_box = (rho.sum((1, 2)) * g.dA).tolist()
            e_box = (e.sum((1, 2)) * g.dA).tolist()
            for b in range(B):
                zeile, alt[b], tropfen = analyse_arm(g, s[b], rho[b], e[b], psi[b], arme[b]["S0"], fam, alt[b])
                zeile["t"] = t
                zeile["Q_box"] = q_box[b]
                zeile["E_box"] = e_box[b]
                aus[namen[b]].append(zeile)
                if schritt == s_fen:
                    fzs[b] = fenster_start(tropfen)
            n_aus += 1
            dauer["auswertung"] += uhr() - ta
            print(f"  t {t:6.0f} ({uhr() - t_start:5.0f} s): " + "; ".join(
                f"{nm} Tr {aus[nm][-1]['schwellen']['2']['N_tropfen']}/K {aus[nm][-1]['schwellen']['2']['N_komp']}"
                + (" U" if aus[nm][-1]['schwellen']['2']['umspannt'] else "") for nm in namen), flush=True)
        if f_jetzt:
            tf = uhr()
            for b in range(B):
                if fzs[b] is not None:
                    fenster_probe(g, fzs[b], s[b], rho[b], e[b], psi[b])
            n_fen += 1
            dauer["fenster"] += uhr() - tf
        if a_jetzt and 0 < schritt < n_schritte and schritt % je_zw == 0:
            meta["ende"] = jetzt()
            schreiben_json(out, name, ergebnis_bauen(meta, namen, arme, theo, kon_t, kon_k, kon_m, aus, None, False))
        if (not args.rauch) and (not args.ohne_zeitgrenze) and schritt == 4 * je_aus and schritt < n_schritte:
            vergangen = uhr() - t_lauf
            entw = vergangen - dauer["auswertung"] - dauer["fenster"]
            prognose = ((t_lauf - t_start) + entw / schritt * n_schritte
                        + 2.0 * dauer["auswertung"] / n_aus * (n_schritte // je_aus + 1))
            print(f"  Prognose Gesamtdauer {prognose:.0f} s", flush=True)
            if prognose > ZEITGRENZE_S:
                meta["ende"] = jetzt()
                meta["abbruch"] = f"Prognose {prognose:.0f} s ueber {ZEITGRENZE_S:.0f} s"
                schreiben_json(out, name, ergebnis_bauen(meta, namen, arme, theo, kon_t, kon_k, kon_m, aus, None, False))
                raise SystemExit(f"Abbruch vor der Zeitgrenze: Prognose {prognose:.0f} s > {ZEITGRENZE_S:.0f} s. "
                                 "Aufruf teilen (--arme einzeln) oder --ohne-zeitgrenze.")
    t_ende_lauf = uhr()
    dauer["entwicklung"] = t_ende_lauf - t_lauf - dauer["auswertung"] - dauer["fenster"]
    fen_erg = [fenster_auswerten(fzs[b], t_ende - fenster, DT_FENSTER, fam, box) for b in range(B)]
    dauer["gesamt"] = uhr() - t_start
    meta["ende"] = jetzt()
    meta["dauer_s"] = dauer
    meta["gpu_speicher_mb"] = (torch.cuda.max_memory_allocated() / 2 ** 20) if DEV.type == "cuda" else None
    if args.rauch:
        n_voll = int(round(T_ENDE / dt))
        rest = dauer["gesamt"] - dauer["entwicklung"] - dauer["auswertung"] - dauer["fenster"]
        meta["prognose_voll_s"] = (rest + dauer["entwicklung"] / max(n_schritte, 1) * n_voll
                                   + 2.0 * dauer["auswertung"] / max(n_aus, 1) * (int(round(T_ENDE / T_AUS)) + 1)
                                   + dauer["fenster"] / max(n_fen, 1) * (int(round(FENSTER / DT_FENSTER)) + 1))
    erg = ergebnis_bauen(meta, namen, arme, theo, kon_t, kon_k, kon_m, aus, fen_erg, True)
    schreiben_json(out, name, erg)
    torch.save({"t": t_ende, "arme": namen, "stufe": args.stufe, "box": box, "dx": dx, "psi": psi.cpu(),
                "vel": vel.cpu(), "bild_t": bild_t, "bilder_S_dx0_5": torch.stack(bilder)},
               os.path.join(out, name + "_felder.pt"))
    text = bericht_text(erg)
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


# ---------------------------------------------------------------- Unterbefehl vergleich (L3, Saat, Box, Karte)

def vergleich(args):
    ordner = args.ordner or args.out
    tab = {}
    for pfad in sorted(glob.glob(os.path.join(ordner, "*_ergebnis.json"))):
        with open(pfad) as fh:
            d = json.load(fh)
        if d.get("rauch") or not d.get("fertig"):
            continue
        for nm, a in d["arme"].items():
            tab[(d["stufe"], float(d["box"]), nm)] = a["kennzahlen"]
    L = [f"KF-5 Vergleich ({jetzt()}), Ordner {ordner}: {len(tab)} fertige Arme"]
    erg = {"zeit": jetzt(), "ordner": ordner, "arme": sorted(f"{s}/{b:g}/{n}" for s, b, n in tab), "L3": {},
           "kontrollen": {}, "karte": {}, "box": {}}

    def rel(a, b):
        return None if (a is None or b is None or b == 0) else abs(a / b - 1.0)

    boxen = sorted({b for _, b, _ in tab})
    for box in boxen:
        for nm in ("s03", "s01"):
            kg, kf = tab.get(("grob", box, nm)), tab.get(("fein", box, nm))
            if not (kg and kf):
                continue
            ks = tab.get(("grob", box, nm + "b"))
            saat = abs(kg["ende"]["N_tropfen"] - ks["ende"]["N_tropfen"]) if ks else 0
            tol_n = max(2.0, 0.25 * kg["ende"]["N_tropfen"], saat)
            r_sat, r_gam = rel(kf["T_sat"], kg["T_sat"]), rel(kf["gamma_mess"], kg["gamma_mess"])
            pr = {"T_sat_5_prozent": r_sat is not None and r_sat <= 0.05,
                  "gamma_5_prozent": r_gam is not None and r_gam <= 0.05,
                  "urteil_netz_gleich": kf["urteil_netz"] == kg["urteil_netz"],
                  "N_tropfen_ende": abs(kf["ende"]["N_tropfen"] - kg["ende"]["N_tropfen"]) <= tol_n,
                  "familienurteil_gleich": kf["familie"]["urteil"] == kg["familie"]["urteil"]}
            erg["L3"][f"{nm}/{box:g}"] = {"pruefungen": pr, "bestanden": all(pr.values()), "toleranz_N": tol_n,
                                          "saatstreuung_N": saat, "T_sat": [kg["T_sat"], kf["T_sat"]],
                                          "gamma": [kg["gamma_mess"], kf["gamma_mess"]],
                                          "N_ende": [kg["ende"]["N_tropfen"], kf["ende"]["N_tropfen"]],
                                          "urteil_netz": [kg["urteil_netz"], kf["urteil_netz"]],
                                          "familie": [kg["familie"]["urteil"], kf["familie"]["urteil"]]}
            L.append(f"L3 {nm} Box {box:g} (grob | fein): T_sat {kg['T_sat']} | {kf['T_sat']}; gamma {kg['gamma_mess']} | "
                     f"{kf['gamma_mess']}; N_Tropfen Ende {kg['ende']['N_tropfen']} | {kf['ende']['N_tropfen']} (Toleranz "
                     f"{tol_n:g}, Saatstreuung {saat}); Netz-Urteil {kg['urteil_netz']} | {kf['urteil_netz']}; Familie "
                     f"{kg['familie']['urteil']} | {kf['familie']['urteil']} -> "
                     f"{'bestanden' if all(pr.values()) else 'nicht bestanden: ' + ', '.join(x for x, ok in pr.items() if not ok)}")
        for nm in ("s08", "frei"):
            for st in ("grob", "fein"):
                k = tab.get((st, box, nm))
                if k:
                    erg["kontrollen"][f"{nm}/{st}/{box:g}"] = k["kontrolle"]
                    L.append(f"Kontrolle {nm} {st} Box {box:g}: Kontrast max {k['kontrast_max']}, "
                             f"{'bestanden' if k['kontrolle']['bestanden'] else 'NICHT bestanden'}")
    kontrollen_ok = bool(erg["kontrollen"]) and all(v["bestanden"] for v in erg["kontrollen"].values())
    for nm in ("s03", "s01"):
        ks = [tab.get((st, BOX0, nm)) for st in ("grob", "fein")]
        if not all(ks):
            erg["karte"][nm] = "unvollstaendig"
            continue
        l3 = erg["L3"].get(f"{nm}/{BOX0:g}", {}).get("bestanden", False)
        if all(k["urteil_netz"] == "Netz" for k in ks):
            u = "H scheitert: umspannende Komponente bei T_Ende auf beiden Gittern (Netz)"
        elif all(k["familie"]["urteil"] == "neben der Familie" for k in ks):
            u = "H scheitert: Tropfen neben der Familie auf beiden Gittern"
        elif (all(k["urteil_netz"] == "getrennte Tropfen" for k in ks)
              and all(k["familie"]["urteil"] == "auf der Familie" for k in ks) and l3 and kontrollen_ok):
            u = "H getragen (explorativ): getrennte Tropfen auf der Familie, L3 und Kontrollen bestanden (Stufe 5)"
        else:
            u = "nicht entscheidbar oder gemischt (Einzelpruefungen oben)"
        erg["karte"][nm] = u
        L.append(f"Karte KF-5, Arm {nm}: {u}")
    for nm in ("s03", "s01"):
        k96, k192 = tab.get(("grob", BOX0, nm)), tab.get(("grob", 2.0 * BOX0, nm))
        if k96 and k192:
            d96 = k96["ende"]["N_tropfen"] / BOX0 ** 2
            d192 = k192["ende"]["N_tropfen"] / (2.0 * BOX0) ** 2
            erg["box"][nm] = {"tropfen_je_flaeche": [d96, d192], "Q_quartile_ende": [k96["ende"]["Q_quartile"],
                                                                                   k192["ende"]["Q_quartile"]]}
            L.append(f"Zusatz Boxgroesse {nm} (Box 96 | 192, grob, beschreibend): Tropfen je Flaeche {d96:.2e} | "
                     f"{d192:.2e}; Q-Quartile Ende {json.dumps(k96['ende']['Q_quartile'])} | "
                     f"{json.dumps(k192['ende']['Q_quartile'])}")
    os.makedirs(ordner, exist_ok=True)
    with open(os.path.join(ordner, "vergleich.json"), "w") as fh:
        json.dump(erg, fh, indent=1)
    with open(os.path.join(ordner, "vergleich_bericht.txt"), "w") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


# ---------------------------------------------------------------- Unterbefehl familie (Tabelle pruefen)

def familie_befehl(args):
    fam = Familie()
    print(f"Familie 2D m = 0: {len(fam.w2)} gueltige Zeilen, omega^2 {fam.w2[0]} bis {fam.w2[-1]}; Quelle {fam.quelle}")
    print(f"ln Q streng fallend in omega^2: {all(a > b for a, b in zip(fam.lnq[:-1], fam.lnq[1:]))}")
    knoten = [fam.q(math.sqrt(w2)) / math.exp(lq) - 1.0 for w2, lq in zip(fam.w2, fam.lnq)]
    print(f"Interpolation an den Knoten: max. rel. Abweichung {max(abs(v) for v in knoten):.1e} (soll < 1e-12)")
    rueck = [fam.omega2_bei_q(math.exp(lq)) - w2 for w2, lq in zip(fam.w2[1:-1], fam.lnq[1:-1])]
    print(f"omega^2 aus Q an den Knoten: max. Abweichung {max(abs(v) for v in rueck):.1e} (soll < 1e-9)")
    for w2, q in ((0.52, 1421.4529), (0.55, 238.4322), (0.60, 66.6160), (0.70, 23.9958), (0.80, 16.2315)):
        qt = fam.q(math.sqrt(w2))
        print(f"  R3-Gegenprobe omega^2 {w2}: Tabelle {qt:.4f}, R3 {q:.4f}, rel. {qt / q - 1.0:+.1e}")
    for w2a in (0.515, 0.535, 0.605, 0.745, 0.945):
        print(f"  Zwischenwert omega^2 {w2a}: Q {fam.q(math.sqrt(w2a)):.4f}")
    for S0 in (0.1, 0.3, 0.8):
        th = theorie(S0, False, BOX0)
        text = (f"Kondensat S0 {S0}: omega0 {th['omega0']:.5f}, U'' {th['U2']:+.3f}, E/Q {th['E_zu_Q_kondensat']:.4f}, "
                f"instabil {th['instabil']}")
        if th.get("q_lambda2"):
            w2 = fam.omega2_bei_q(th["q_lambda2"])
            text += (f"; gamma_max {th['gamma_max']:.4f}, lambda_max {th['lambda_max']:.3f}, Zellen {th['zellen']:.1f}, "
                     f"q lambda^2 {th['q_lambda2']:.2f} -> Familie omega^2 {fz(w2, '.4f')}, E/Q "
                     f"{fz(fam.eq_bei_q(th['q_lambda2']), '.4f')}")
        print(text)


def main():
    global DEV
    ap = argparse.ArgumentParser(description="KF-5 Geburt in 2D (Runde 6, v3)")
    ap.add_argument("befehl", choices=["lauf", "vergleich", "familie"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--stufe", choices=list(STUFEN), default="grob")
    ap.add_argument("--arme", default="s03,s01,s08,frei,s03b,s01b")
    ap.add_argument("--box", type=float, default=BOX0)
    ap.add_argument("--rauch", action="store_true", help="T_Ende 40, Fenster 10: nur Durchlauf und Hochrechnung")
    ap.add_argument("--t-ende", type=float, default=None, help="nur fuer kleine Probelaeufe")
    ap.add_argument("--fenster", type=float, default=None, help="nur fuer kleine Probelaeufe")
    ap.add_argument("--ohne-zeitgrenze", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--ordner", default=None)
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        DEV = torch.device("cuda")
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
    if args.out is None:
        args.out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rauchtest" if args.rauch else "ausgabe")
    if args.befehl == "lauf":
        lauf(args)
    elif args.befehl == "vergleich":
        vergleich(args)
    else:
        familie_befehl(args)


if __name__ == "__main__":
    main()
