#!/usr/bin/env python3
"""Runde 5, Paket R5-C (runden-v3): 1D-Tests mit mehreren Baellen oder Hintergrund. Explorativ. Ungetestet abgegeben
(Interpreterverbot auf dem Laptop); Aufrufe, Vorhersagen, Gegenproben und Latten stehen in PLAN.md daneben.

Modell wie RUNDE-02/tests1d/tests1d.py: L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2.
Bewegungsgleichung psi_tt = psi_xx - U'(S) psi. Ladungsdichte rho = 2 Im(psi conj psi_t), Ladungsfluss
j = -2 Im(psi conj psi_x), Energiedichte |psi_t|^2 + |psi_x|^2 + U, Impulsdichte -2 Re(conj psi_t psi_x),
Impulsfluss T_xx = |psi_t|^2 + |psi_x|^2 - U.

Aus tests1d.py unveraendert: Velocity-Verlet mit dx = 0,1 und dt = 0,05 (fein beide halbiert), quadratische
Daempfungsschicht (sigma0 = 1, 40 breit), Lorentz-Boost der Baelle, Anker-Formeln, FFT-Spitzen, L3-Hilfe.
Geaendert (begruendet in PLAN.md):
  - Profil: der geschlossene 1D-Anker f^2 = 2 a0/(1 + b0 cosh(2 sqrt(a0) x)) statt der Schiessbahn. In RUNDE-02 stimmte
    das Schiessen mit ihm auf 1,5e-10 ueberein; das Schiessen kostete 80 s je Aufruf und bringt in 1D nichts Neues.
  - Rand: periodischer Ring; die offene Box ist derselbe Ring mit der Daempfungsschicht am Stoss (|x| > L/2 - 40).
    Ohne Hintergrund entspricht das dem Dirichlet-Rand der Vorlage (Feld dort null).
  - Hintergrund (nur Osmose, Massenwirkung): exakt diskrete Loesung A exp(-i theta n), theta = 2 asin(nu dt/2),
    Startgeschwindigkeit -i sin(theta)/dt A; der Hintergrund allein bleibt dann bis auf Rundung stehen.

Unterbefehle (je Idee einer, dazu Rauchtest):
  osmose         Bio 2       Ball auf dichtem, linear stabilem Kondensat (S = 0,8 / 1,0 / 1,1 / 1,2)
  massenwirkung  Chemie 9    drei Startmischungen (Ball 0,55 / 0,70 / 0,90 auf S = 1,1), Endzustand
  pendeln        Bio 12      Josephson-Pendeln im gegenphasigen Ring; Periode gegen Abstand; freie Paare
  symbiose       Bio 16      freie Paare: verschmelzen, gebunden oder getrennt; Energiebilanz
  quorum         Bio 39      Atem-Phasen im Ring bei drei Dichten
  lawinen        Bio 50      Kette mit zufaelligen kleinen Stoessen; Groessenverteilung der Atem-Ereignisse
  ir             Chemie 4    Abstandsschwingung im gegenphasigen Ring (FFT)
  bragg          W21         Wellenpaket durch gegenphasige Q-Ball-Kette (Ring), Transmission gegen k
  anderson       W22         Wellenpaket durch zufaelliges Q-Ball-Gas (4, 8, 16 Baelle), log T gegen Laenge
  hintergrund    Wellen 6/7/11 und Bio 2/Chemie 9: Papierprobe der Hintergrund-Stabilitaet (keine Zeitentwicklung)
  rauch          alle Zeitentwicklungen mit Laufzeit x 0,05 (nur Durchlaufprobe und Zeitmessung)

Aufruf:  python r5c.py <unterbefehl> [--geraet cuda|cpu] [--out ORDNER] [--nur a,b,...] [--seeds N] [--roh DATEI]
"""
import argparse
import datetime
import json
import math
import os
import time
import traceback

import torch

VERSION = "v2 (2026-09-30 02:44: integral fuer (Zeit, Lauf, Ebene); Rohdaten-Sicherung; --roh)"
DEV = torch.device("cpu")
F64 = torch.float64
C128 = torch.complex128
PI = math.pi

DX, DT, FEIN = 0.1, 0.05, 0.5      # wie tests1d.py; fein = dx/2 und dt/2 (Latte L3)
SIGMA0, SCHWAMM = 1.0, 40.0        # Daempfungsschicht wie tests1d.py
SPEICHER_GB = 1.5                  # Vorgabe der Leitung fuer die GPU
T_MESS = 0.5
W2 = 0.70                          # Standard-Ball wie RUNDE-02
RAUCH_FAKTOR = 0.05


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


# ---------------------------------------------------------------- Anker (aus tests1d.py)

def anker_wgv(w2):
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    integ = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integ
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integ / 4.0
    return w, g, w + g


def anker_q_e(w2):
    w, g, v = anker_wgv(w2)
    return 2.0 * w / math.sqrt(w2), w + g + v


def anker_umkehr(q):
    if not math.isfinite(q) or q <= 0.0:
        return float("nan")
    lo, hi = 0.5 + 1e-12, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if anker_q_e(mid)[0] > q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def domega_dq(w2, h=1e-4):
    return (math.sqrt(w2 + h) - math.sqrt(w2 - h)) / (anker_q_e(w2 + h)[0] - anker_q_e(w2 - h)[0])


def kopplung_j(w2, d):
    """Tail-Kopplung (Josephson-Strom, Wechselwirkungsenergie) J = 4 kappa A^2 exp(-kappa d), A^2 = 4 a0/b0."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    k = math.sqrt(a0)
    return 4.0 * k * (4.0 * a0 / b0) * math.exp(-k * d)


def u_strich(s):
    return 1.0 - 2.0 * s + 1.5 * s * s


# ---------------------------------------------------------------- Gitter, Felder

def box(L, dx, schwamm):
    n = int(round(L / dx))
    x = torch.arange(n, dtype=F64, device=DEV) * dx - 0.5 * L
    if schwamm:
        sig = SIGMA0 * ((x.abs() - (0.5 * L - SCHWAMM)).clamp(min=0.0) / SCHWAMM) ** 2
    else:
        sig = torch.zeros_like(x)
    return {"L": L, "dx": dx, "x": x, "n": n, "sigma": sig}


def pdist(x, xc, L):
    return torch.remainder(x - xc + 0.5 * L, L) - 0.5 * L


def ball(bx, w2, xc, v=0.0, phase=0.0):
    """Q-Ball (geschlossener 1D-Anker) um xc, Geschwindigkeit v (Lorentz-Boost wie tests1d.ball), Phase.
    f'(xi) = -sqrt(2) a0 b0 sinh(z) / D^(3/2), z = 2 sqrt(a0) xi, D = 1 + b0 cosh(z)."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    k, w = math.sqrt(a0), math.sqrt(w2)
    gam = 1.0 / math.sqrt(1.0 - v * v)
    d = pdist(bx["x"], xc, bx["L"])
    xi = gam * d
    z = (2.0 * k * xi).clamp(-300.0, 300.0)
    nen = 1.0 + b0 * torch.cosh(z)
    f = torch.sqrt(2.0 * a0 / nen)
    fp = -math.sqrt(2.0) * a0 * b0 * torch.sinh(z) / nen ** 1.5
    ph = torch.exp(1j * (w * gam * v * d + phase))
    return f * ph, (-gam * v * fp - 1j * w * gam * f) * ph


def paket(bx, k0, x0, sigma, eps):
    """Schwaches Wellenpaket nach rechts (wie tests1d.paket), Traegerwellenzahl k0, nu^2 = k0^2 + 1."""
    nu = math.sqrt(k0 * k0 + 1.0)
    vg = k0 / nu
    d = pdist(bx["x"], x0, bx["L"])
    psi = eps * torch.exp(-d * d / (2.0 * sigma * sigma)) * torch.exp(1j * k0 * d)
    return psi, (-1j * nu + vg * d / sigma ** 2) * psi


def hintergrund(bx, dt, S):
    """Ruhender homogener Hintergrund als exakt diskrete Loesung (Raum und Verlet-Zeitschritt)."""
    nu = math.sqrt(u_strich(S))
    th = 2.0 * math.asin(0.5 * nu * dt)
    a = math.sqrt(S) * torch.ones(bx["n"], dtype=C128, device=DEV)
    return a, (-1j * math.sin(th) / dt) * a


def leer(bx):
    z = torch.zeros(bx["n"], dtype=C128, device=DEV)
    return z, z.clone()


def plus(*teile):
    return sum(p for p, _ in teile), sum(v for _, v in teile)


def stapel(felder):
    return torch.stack([p for p, _ in felder]), torch.stack([v for _, v in felder])


# ---------------------------------------------------------------- Zeitentwicklung

def entwickeln(bx, psi, vel, dt, t_end, t_mess, messen, ereignisse=None):
    """Velocity-Verlet wie tests1d.entwickeln; Laplace periodisch; Daempfung wie dort, falls sigma > 0.
    ereignisse: {Schritt n: (B, N)-Faktor}, wirkt nach Schritt n auf psi und psi_t (Stoesse, nur 'lawinen')."""
    dx, sigma = bx["dx"], bx["sigma"]
    daempfen = bool((sigma > 0).any())

    def kraft(p):
        lap = (torch.roll(p, -1, 1) + torch.roll(p, 1, 1) - 2.0 * p) / (dx * dx)
        s = p.real ** 2 + p.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s) * p

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    for n in range(1, n_schritte + 1):
        if daempfen:
            vel = vel + (0.5 * dt) * (kr - sigma * vel)
        else:
            vel = vel + (0.5 * dt) * kr
        psi = psi + dt * vel
        kr = kraft(psi)
        if daempfen:
            vel = vel + (0.5 * dt) * (kr - sigma * vel)
        else:
            vel = vel + (0.5 * dt) * kr
        if ereignisse is not None and n in ereignisse:
            fak = ereignisse[n]
            psi = psi * fak
            vel = vel * fak
            kr = kraft(psi)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
    daten = torch.stack(reihe)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64) * (alle * dt)
    return t, daten.cpu(), n_schritte


def messer(bx, zentren, breiten, verfolgen, ebenen):
    """Messfunktion. zentren, breiten: (B, K) Listen; verfolgen: K Wahrheitswerte; ebenen: (B, P) Orte.
    Je Zelle k: Ort des Maximums von |psi|^2 (Parabel), S dort, Phase -arg psi dort, und im Fenster |x - Mitte| < W:
    Ladung, Energie, Impuls, Breite (Standardabweichung von |psi|^2). Je Ebene: Ladungsfluss j und T_xx.
    Dazu Gesamtladung, -energie, -impuls. Verfolgte Zellen suchen das Maximum in +-1 um den letzten Ort."""
    x, dx, L, N = bx["x"], bx["dx"], bx["L"], bx["n"]
    zt = torch.tensor(zentren, dtype=F64, device=DEV)
    wt = torch.tensor(breiten, dtype=F64, device=DEV).unsqueeze(-1)
    vt = torch.tensor(verfolgen, dtype=torch.bool, device=DEV).unsqueeze(0)
    et = torch.tensor(ebenen, dtype=F64, device=DEV)
    zustand = {"idx": torch.remainder(torch.round((zt + 0.5 * L) / dx).long(), N)}
    ie = torch.remainder(torch.round((et + 0.5 * L) / dx).long(), N)
    w = max(1, int(round(1.0 / dx)))
    off = torch.arange(-w, w + 1, device=DEV)
    xv = x.view(1, 1, N)

    def messen(psi, vel):
        nb = psi.shape[0]
        s = psi.real ** 2 + psi.imag ** 2
        px = (torch.roll(psi, -1, 1) - torch.roll(psi, 1, 1)) / (2.0 * dx)
        vv = vel.real ** 2 + vel.imag ** 2
        gg = px.real ** 2 + px.imag ** 2
        u = s - s * s + 0.5 * s ** 3
        rho = 2.0 * (psi * vel.conj()).imag
        e = vv + gg + u
        pd = -2.0 * (vel.conj() * px).real
        txx = vv + gg - u
        jj = -2.0 * (psi * px.conj()).imag
        cur = zustand["idx"]
        kand = torch.remainder(cur.unsqueeze(-1) + off, N)
        werte = s.gather(1, kand.reshape(nb, -1)).reshape(kand.shape)
        neu = kand.gather(2, werte.argmax(dim=2, keepdim=True)).squeeze(2)
        cur = torch.where(vt, neu, cur)
        zustand["idx"] = cur
        sm = s.gather(1, torch.remainder(cur - 1, N))
        s0 = s.gather(1, cur)
        sp = s.gather(1, torch.remainder(cur + 1, N))
        nen = sm - 2.0 * s0 + sp
        delta = torch.where(nen < 0.0, 0.5 * (sm - sp) / nen.clamp(max=-1e-300), torch.zeros_like(s0)).clamp(-1.0, 1.0)
        xp = x[cur] + delta * dx
        mitte = torch.where(vt, xp, x[cur])
        th = -torch.angle(psi.gather(1, cur))
        d = torch.remainder(xv - mitte.unsqueeze(-1) + 0.5 * L, L) - 0.5 * L
        m = (d.abs() < wt).to(F64)
        q = torch.einsum("bn,bkn->bk", rho, m) * dx
        en = torch.einsum("bn,bkn->bk", e, m) * dx
        pp = torch.einsum("bn,bkn->bk", pd, m) * dx
        m0 = torch.einsum("bn,bkn->bk", s, m).clamp(min=1e-300)
        md = m * d
        m1 = torch.einsum("bn,bkn->bk", s, md) / m0
        m2 = torch.einsum("bn,bkn->bk", s, md * d) / m0
        br = torch.sqrt((m2 - m1 * m1).clamp(min=0.0))
        glob = torch.stack([rho.sum(1) * dx, e.sum(1) * dx, pd.sum(1) * dx], dim=1)
        return torch.cat([xp, s0, th, q, en, pp, br, jj.gather(1, ie), txx.gather(1, ie), glob], dim=1)
    return messen


def spalten(k, p):
    c = {n: slice(i * k, (i + 1) * k) for i, n in enumerate(["x", "S", "th", "Q", "E", "P", "B"])}
    c["j"] = slice(7 * k, 7 * k + p)
    c["T"] = slice(7 * k + p, 7 * k + 2 * p)
    c["Qg"], c["Eg"], c["Pg"] = 7 * k + 2 * p, 7 * k + 2 * p + 1, 7 * k + 2 * p + 2
    return c


ROH = {}             # v2: Rohdaten je Stufenname des laufenden Unterbefehls; gespeichert auch bei Auswertungsfehlern
VORRAT = {}          # v2: mit --roh geladene Rohdaten; stufen() rechnet dann nicht, es wird nur ausgewertet
ZWISCHEN = [None]    # v2: Datei, in die stufen() nach jeder Stufe die Rohdaten schreibt (Schutz gegen Abbruch)


def stufen(name, bauen, t_end, t_mess=T_MESS):
    """Grob (dx, dt) und fein (dx/2, dt/2). bauen(dx, dt) -> dict(box, psi, vel, messen[, ereignisse])."""
    if name in VORRAT:
        print(f"{name}: Rohdaten aus --roh, keine Zeitentwicklung", flush=True)
        ROH[name] = VORRAT[name]
        return VORRAT[name]
    aus = {}
    for stufe, dx, dt in (("grob", DX, DT), ("fein", DX * FEIN, DT * FEIN)):
        b = bauen(dx, dt)
        t0 = uhr()
        t, daten, n = entwickeln(b["box"], b["psi"], b["vel"], dt, t_end, t_mess, b["messen"], b.get("ereignisse"))
        sek = uhr() - t0
        ms = 1000.0 * sek / max(1, n)
        print(f"{name} {stufe}: {b['psi'].shape[0]} Laeufe x {b['psi'].shape[1]} Punkte, T = {t_end:g}, "
              f"{n} Schritte, {sek:.1f} s ({ms:.2f} ms/Schritt)", flush=True)
        aus[stufe] = {"t": t, "daten": daten, "sek": sek, "ms_schritt": ms}
        del b
        ROH[name] = aus
        if ZWISCHEN[0]:
            torch.save(ROH, ZWISCHEN[0])
    return aus


def roh_laden(pfad):
    """v2: Rohdaten laden, flach je Stufenname. Nimmt r5c_zeitreihen.pt ({Unterbefehl: {Stufenname: Stufen}}) oder
    r5c_roh_zwischen.pt ({Stufenname: Stufen}); nur Eintraege mit grob UND fein."""
    alt = torch.load(pfad, map_location="cpu", weights_only=False)
    vorrat = {}

    def sammeln(dd):
        for k, v in dd.items():
            if not isinstance(v, dict):
                continue
            if isinstance(v.get("grob"), dict) and isinstance(v.get("fein"), dict) and "daten" in v["grob"] \
                    and "daten" in v["fein"]:
                vorrat[k] = v
            else:
                sammeln(v)
    sammeln(alt)
    return vorrat


# ---------------------------------------------------------------- Auswerte-Hilfen

def wrap(a):
    return torch.remainder(a + PI, 2.0 * PI) - PI


def entfalten(th):
    return torch.cat([th[:1], th[:1] + torch.cumsum(wrap(th[1:] - th[:-1]), dim=0)], dim=0)


def integral(t, y):
    """Trapezregel ueber die Zeit (Achse 0). v2: y darf beliebig viele weitere Achsen haben; v1 kannte nur 1D und 2D
    und brach in bragg/anderson an (Zeit, Lauf, Ebene) ab."""
    dt_ = (t[1:] - t[:-1]).reshape([-1] + [1] * (y.dim() - 1))
    return 0.5 * ((y[1:] + y[:-1]) * dt_).sum(0)


def steigung(t, y, t_ab):
    w = t >= t_ab - 1e-9
    ts, ys = t[w], y[w]
    if ts.numel() < 3:
        return float("nan")
    tm, ym = ts.mean(), ys.mean()
    return float(((ts - tm) * (ys - ym)).sum() / ((ts - tm) ** 2).sum())


def mittel(t, y, t_von, t_bis=None):
    w = t >= t_von - 1e-9
    if t_bis is not None:
        w = w & (t <= t_bis + 1e-9)
    return float(y[w].mean()) if bool(w.any()) else float("nan")


def spitzen(t, y, t_ab=0.0, n_spitzen=3, om_min=0.0):
    """Groesste Spitzen der FFT (Trend entfernt, Hann-Fenster) wie tests1d.spektrum, auf der CPU."""
    wahl = t >= t_ab - 1e-9
    ts, ys = t[wahl], y[wahl]
    n = ys.shape[0]
    if n < 16:
        return []
    tau = ts - ts[0]
    a_mat = torch.stack([torch.ones_like(tau), tau], dim=1)
    koef = torch.linalg.lstsq(a_mat, ys.unsqueeze(1)).solution
    rest = ys - (a_mat @ koef).squeeze(1)
    fen = torch.hann_window(n, periodic=False, dtype=F64)
    amp = torch.fft.rfft(rest * fen).abs()
    d_om = 2.0 * PI / (n * (ts[1] - ts[0]).item())
    lok = (amp[1:-1] > amp[:-2]) & (amp[1:-1] >= amp[2:])
    kand = torch.nonzero(lok).squeeze(1) + 1
    kand = kand[kand.to(F64) * d_om > om_min]
    kand = kand[amp[kand].argsort(descending=True)][:n_spitzen]
    aus = []
    for k in kand.tolist():
        a, b, c = amp[k - 1].item(), amp[k].item(), amp[k + 1].item()
        nen = a - 2.0 * b + c
        dl = 0.5 * (a - c) / nen if nen != 0.0 else 0.0
        aus.append({"Omega": (k + dl) * d_om, "amplitude": 2.0 * b / fen.sum().item()})
    return aus


def haupt(t, y, t_ab=0.0, om_min=0.0):
    sp = spitzen(t, y, t_ab, 1, om_min)
    return sp[0]["Omega"] if sp else float("nan")


def l3(g, f, null):
    eff, aend = abs(g - null), abs(f - g)
    return {"effekt": eff, "aenderung": aend, "bestanden": bool(eff >= 5.0 * aend)}


def gf(v):
    return float(v.item()) if torch.is_tensor(v) else float(v)


def fz(v, fmt=".4g"):
    return format(v, fmt) if isinstance(v, (int, float)) and math.isfinite(v) else str(v)


def ring_kette(bx, kz, w2_liste, phasen, versatz):
    """K Baelle gleichmaessig im Ring (Abstand D = L/K), Ball j bei -L/2 + D/2 + j D + versatz[j]."""
    L = bx["L"]
    d = L / kz
    orte = [-0.5 * L + 0.5 * d + j * d + versatz[j] for j in range(kz)]
    teile = [ball(bx, w2_liste[j], orte[j], 0.0, phasen[j]) for j in range(kz)]
    return plus(*teile), orte


def aufgefuellt(liste, k_max):
    return list(liste) + [liste[0]] * (k_max - len(liste))


# ---------------------------------------------------------------- Bio 2 Osmose und Chemie 9 Massenwirkung (dichtes Kondensat)

OS_L, OS_W, OS_T = 200.0, 15.0, 200.0
OS_S = (0.8, 1.0, 1.1, 1.2)
MW_L, MW_W, MW_T, MW_S = 200.0, 15.0, 800.0, 1.1
MW_W2 = (0.55, 0.70, 0.90)


def kondensat_laeufe(bauplan, L, W, T, name):
    """bauplan: Liste von Laeufen {'art': 'ball+hg'|'hg'|'ball', 'S': .., 'w2': ..}. Ball bei 0 mit Phase pi/2 gegen
    den Hintergrund (dann kein Kreuzterm in rho und |psi|^2 zu Beginn). Zelle fest bei 0."""
    def bauen(dx, dt):
        bx = box(L, dx, False)
        felder = []
        for r in bauplan:
            teile = [leer(bx)]
            if r["art"] in ("ball+hg", "hg"):
                teile.append(hintergrund(bx, dt, r["S"]))
            if r["art"] in ("ball+hg", "ball"):
                teile.append(ball(bx, r["w2"], 0.0, 0.0, 0.5 * PI))
            felder.append(plus(*teile))
        psi, vel = stapel(felder)
        nb = len(bauplan)
        return {"box": bx, "psi": psi, "vel": vel,
                "messen": messer(bx, [[0.0]] * nb, [[W]] * nb, [False], [[0.5 * L - 1.0]] * nb)}
    return stufen(name, bauen, T)


def kondensat_zeile(t, d, i_mix, i_hg, i_ball, S, w2, T):
    """Ueberschuss im Fenster: Q(Ball + Kondensat) - Q(Kondensat) und die Buckelhoehe S(0) - S_Kondensat."""
    c = spalten(1, 1)
    ex = d[:, i_mix, c["Q"]][:, 0] - d[:, i_hg, c["Q"]][:, 0]
    hb = d[:, i_mix, c["S"]][:, 0] - d[:, i_hg, c["S"]][:, 0]
    thu = entfalten(d[:, i_mix, c["th"]][:, 0])
    om_bg = math.sqrt(u_strich(S))
    ex0, hb0 = gf(ex[0]), gf(hb[0])
    z = {"S": S, "w2_ball": w2, "omega_ball": math.sqrt(w2), "omega_bg": om_bg,
         "delta_mu": math.sqrt(w2) - om_bg, "Q_ball_allein": gf(d[0, i_ball, c["Q"]][0]),
         "ueberschuss_0": ex0, "buckel_0": hb0,
         "rate_0_30": steigung(t[t <= 30.0 + 1e-9], ex[t <= 30.0 + 1e-9], 0.0),
         "ueberschuss_rel_T4": mittel(t, ex, 0.2 * T, 0.3 * T) / ex0 if ex0 else float("nan"),
         "ueberschuss_rel_ende": mittel(t, ex, 0.75 * T) / ex0 if ex0 else float("nan"),
         "buckel_rel_ende": mittel(t, hb, 0.75 * T) / hb0 if hb0 else float("nan"),
         "omega_mitte_ende": steigung(t, thu, 0.75 * T),
         "Q_box_drift": gf(d[-1, i_mix, c["Qg"]] - d[0, i_mix, c["Qg"]]),
         "E_box_drift": gf(d[-1, i_mix, c["Eg"]] - d[0, i_mix, c["Eg"]])}
    z["wachstum"] = bool(z["ueberschuss_rel_ende"] > 1.0)
    z["aufgeloest"] = bool(abs(z["ueberschuss_rel_ende"]) < 0.3)
    return z


def t_osmose(faktor):
    T = OS_T * faktor
    plan = []
    for S in OS_S:
        plan += [{"art": "ball+hg", "S": S, "w2": W2}, {"art": "hg", "S": S, "w2": W2}]
    plan.append({"art": "ball", "S": 0.0, "w2": W2})
    st = kondensat_laeufe(plan, OS_L, OS_W, T, "osmose")
    erg = {}
    for stufe, s in st.items():
        erg[stufe] = [kondensat_zeile(s["t"], s["daten"], 2 * i, 2 * i + 1, len(plan) - 1, S, W2, T)
                      for i, S in enumerate(OS_S)]
    l3l = [{"S": g["S"], "ueberschuss_rel_ende": l3(g["ueberschuss_rel_ende"], f["ueberschuss_rel_ende"], 1.0)}
           for g, f in zip(erg["grob"], erg["fein"])]
    text = [f"Osmose (Bio 2): Ball omega^2 = {W2} auf Kondensat S = {OS_S}, Ring L = {OS_L}, Fenster +-{OS_W}, T = {T:g}.",
            "  S | omega_bg | omega - omega_bg | Ueberschuss 0 | rel. bei T/4 | rel. Ende | Buckel rel. Ende | "
            "Rate 0-30 | omega Mitte Ende | geloest / gewachsen"]
    for stufe in ("grob", "fein"):
        text.append(f"  [{stufe}]")
        for z in erg[stufe]:
            text.append(f"  {z['S']} | {z['omega_bg']:.4f} | {z['delta_mu']:+.4f} | {z['ueberschuss_0']:.4f} | "
                        f"{fz(z['ueberschuss_rel_T4'])} | {fz(z['ueberschuss_rel_ende'])} | {fz(z['buckel_rel_ende'])} | "
                        f"{fz(z['rate_0_30'])} | {fz(z['omega_mitte_ende'])} | {z['aufgeloest']} / {z['wachstum']}")
    text.append(f"  L3 (rel. Ueberschuss am Ende gegen 1): {sum(e['ueberschuss_rel_ende']['bestanden'] for e in l3l)} "
                f"von {len(l3l)}")
    return {"plan": plan, "ergebnis": erg, "L3": l3l}, text, st


def t_massenwirkung(faktor):
    T = MW_T * faktor
    plan = [{"art": "ball+hg", "S": MW_S, "w2": w2} for w2 in MW_W2]
    plan.append({"art": "hg", "S": MW_S, "w2": 0.0})
    plan += [{"art": "ball", "S": 0.0, "w2": w2} for w2 in MW_W2]
    st = kondensat_laeufe(plan, MW_L, MW_W, T, "massenwirkung")
    n = len(MW_W2)
    erg = {stufe: [kondensat_zeile(s["t"], s["daten"], i, n, n + 1 + i, MW_S, w2, T) for i, w2 in enumerate(MW_W2)]
           for stufe, s in st.items()}
    l3l = [{"w2": g["w2_ball"], "omega_mitte_ende": l3(g["omega_mitte_ende"], f["omega_mitte_ende"], g["omega_ball"])}
           for g, f in zip(erg["grob"], erg["fein"])]
    text = [f"Massenwirkung (Chemie 9): Kondensat S = {MW_S} (omega_bg = {math.sqrt(u_strich(MW_S)):.4f}), Baelle "
            f"omega^2 = {MW_W2}, Ring L = {MW_L}, T = {T:g}.",
            "  omega^2 | omega - omega_bg | Ueberschuss 0 | rel. Ende | Buckel rel. Ende | omega Mitte Ende | geloest"]
    for stufe in ("grob", "fein"):
        text.append(f"  [{stufe}]")
        for z in erg[stufe]:
            text.append(f"  {z['w2_ball']} | {z['delta_mu']:+.4f} | {z['ueberschuss_0']:.4f} | "
                        f"{fz(z['ueberschuss_rel_ende'])} | {fz(z['buckel_rel_ende'])} | {fz(z['omega_mitte_ende'])} | "
                        f"{z['aufgeloest']}")
    text.append(f"  L3 (omega Mitte Ende gegen omega Ball): {sum(e['omega_mitte_ende']['bestanden'] for e in l3l)} "
                f"von {len(l3l)}")
    return {"plan": plan, "ergebnis": erg, "L3": l3l}, text, st


# ---------------------------------------------------------------- Ring-Ketten: Bio 12 Pendeln, Chemie 4 IR, Bio 39 Quorum

RING_L = 120.0
RING_K = (16, 12, 10, 8, 6, 4)             # D = 7,5 / 10 / 12 / 15 / 20 / 30
PD_DELTA, PD_T = 0.004, 600.0
PD_FREI_D = (7.0, 8.0, 10.0)
IR_K, IR_S0, IR_T = (16, 12, 10, 8, 4), 0.3, 600.0
QU_K, QU_ETA, QU_OMB, QU_T, QU_SEED = (8, 12, 16), 0.02, 0.17, 600.0, 1239


def ring_messer(bx, laeufe, k_max):
    L = bx["L"]
    zen, brt = [], []
    for r in laeufe:
        dd = L / r["K"]
        orte = [-0.5 * L + 0.5 * dd + j * dd for j in range(r["K"])]
        zen.append(aufgefuellt(orte, k_max))
        brt.append([0.5 * dd - 0.1] * k_max)
    return messer(bx, zen, brt, [True] * k_max, [[0.0]] * len(laeufe))


def vorhersage_ring(dd):
    """Gegenphasiger Ring, jeder Ball zwei Nachbarn im Abstand dd:
    Ladungsmode Omega_p^2 = 4 |domega/dQ| J(dd); Abstandsmode Omega_vib^2 = 4 kappa^2 J(dd) / E."""
    j = kopplung_j(W2, dd)
    kap = math.sqrt(1.0 - W2)
    return {"J": j, "Omega_p": math.sqrt(4.0 * abs(domega_dq(W2)) * j),
            "Omega_vib": math.sqrt(4.0 * kap * kap * j / anker_q_e(W2)[1])}


def t_pendeln(faktor):
    T = PD_T * faktor
    laeufe = [{"K": kz, "delta": PD_DELTA, "muster": "wechselnd"} for kz in RING_K]
    laeufe += [{"K": 12, "delta": 0.0, "muster": "wechselnd"}, {"K": 12, "delta": PD_DELTA, "muster": "gleich"}]
    km = max(r["K"] for r in laeufe)

    def bauen(dx, dt):
        bx = box(RING_L, dx, False)
        felder = []
        for r in laeufe:
            kz = r["K"]
            w2l = [W2 + (r["delta"] if j % 2 == 0 else -r["delta"]) for j in range(kz)]
            ph = [(PI * j if r["muster"] == "wechselnd" else 0.0) for j in range(kz)]
            f, _ = ring_kette(bx, kz, w2l, ph, [0.0] * kz)
            felder.append(f)
        psi, vel = stapel(felder)
        return {"box": bx, "psi": psi, "vel": vel, "messen": ring_messer(bx, laeufe, km)}
    st = stufen("pendeln Ring", bauen, T)

    frei = [{"D": dd, "dphi": PI, "delta": PD_DELTA} for dd in PD_FREI_D] + [{"D": 8.0, "dphi": 0.5 * PI, "delta": 0.0}]

    def bauen_frei(dx, dt):
        bx = box(300.0, dx, True)
        felder = [plus(ball(bx, W2 + r["delta"], -0.5 * r["D"], 0.0, 0.0),
                       ball(bx, W2 - r["delta"], 0.5 * r["D"], 0.0, r["dphi"])) for r in frei]
        psi, vel = stapel(felder)
        nb = len(frei)
        return {"box": bx, "psi": psi, "vel": vel,
                "messen": messer(bx, [[-0.5 * r["D"], 0.5 * r["D"]] for r in frei],
                                 [[0.5 * r["D"] - 0.1] * 2 for r in frei], [True, True], [[0.0]] * nb)}
    st_frei = stufen("pendeln frei", bauen_frei, T)

    c = spalten(km, 1)

    def auswerten(t, d):
        zz = []
        for b, r in enumerate(laeufe):
            kz = r["K"]
            vz = torch.tensor([(-1.0) ** j for j in range(kz)], dtype=F64)
            q = (d[:, b, c["Q"]][:, :kz] * vz).mean(1)
            xs = d[:, b, c["x"]][:, :kz]
            abst = torch.remainder(torch.roll(xs, -1, 1) - xs, RING_L)
            v = vorhersage_ring(RING_L / kz)
            om = haupt(t, q, 0.0)
            zz.append({"K": kz, "D": RING_L / kz, "delta": r["delta"], "muster": r["muster"],
                       "Omega_p": om, "Omega_p_vorhersage": v["Omega_p"],
                       "verhaeltnis": om / v["Omega_p"] if math.isfinite(om) else float("nan"),
                       "q0": gf(q[0]), "q_spanne": gf(q.max() - q.min()), "q_max_abs": gf(q.abs().max()),
                       "wachstum_q": gf(q.abs()[-max(1, len(t) // 10):].mean() / max(abs(gf(q[0])), 1e-12)),
                       "max_verschiebung": gf((xs - xs[:1]).abs().max()), "min_abstand_ende": gf(abst[-1].min())})
        fit = [(z["D"], math.log(z["Omega_p"])) for z in zz if z["muster"] == "wechselnd" and z["delta"] > 0
               and z["D"] <= 15.0 and math.isfinite(z["Omega_p"]) and z["Omega_p"] > 0]
        steig = float("nan")
        if len(fit) >= 3:
            dm = sum(a for a, _ in fit) / len(fit)
            ym = sum(b for _, b in fit) / len(fit)
            steig = sum((a - dm) * (b - ym) for a, b in fit) / sum((a - dm) ** 2 for a, _ in fit)
        return {"zeilen": zz, "steigung_lnOmega_D": steig, "vorhersage_steigung": -0.5 * math.sqrt(1.0 - W2)}

    def auswerten_frei(t, d):
        c2 = spalten(2, 1)
        zz = []
        for b, r in enumerate(frei):
            q = 0.5 * (d[:, b, c2["Q"]][:, 0] - d[:, b, c2["Q"]][:, 1])
            dd = d[:, b, c2["x"]][:, 1] - d[:, b, c2["x"]][:, 0]
            nulldg = int(((q[1:] - q.mean()) * (q[:-1] - q.mean()) < 0).sum().item())
            zz.append({"D0": r["D"], "dphi": r["dphi"], "delta": r["delta"], "q0": gf(q[0]),
                       "q_spanne": gf(q.max() - q.min()), "nulldurchgaenge_q": nulldg, "D_ende": gf(dd[-1]),
                       "D_min": gf(dd.min()), "D_max": gf(dd.max()), "verschmolzen": bool(gf(dd[-1]) < 1.5)})
        return zz
    erg = {s: auswerten(st[s]["t"], st[s]["daten"]) for s in st}
    erg_frei = {s: auswerten_frei(st_frei[s]["t"], st_frei[s]["daten"]) for s in st_frei}
    l3l = [{"D": g["D"], "Omega_p": l3(g["Omega_p"], f["Omega_p"], 0.0)}
           for g, f in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]) if g["delta"] > 0 and g["muster"] == "wechselnd"]
    text = [f"Ladungspendeln (Bio 12): gegenphasiger Ring L = {RING_L}, Ungleichgewicht omega^2 = {W2} +- {PD_DELTA}, "
            f"T = {T:g}. Vorhersage Omega_p = sqrt(4 |domega/dQ| J(D)), |domega/dQ| = {abs(domega_dq(W2)):.4f}.",
            "  K | D | Muster | delta | Omega_p | Vorhersage | Verhaeltnis | q0 | Spanne q | max|q| | max Verschiebung | "
            "min Abstand Ende"]
    for stufe in ("grob", "fein"):
        e = erg[stufe]
        text.append(f"  [{stufe}] Steigung ln Omega_p gegen D: {fz(e['steigung_lnOmega_D'])} "
                    f"(Vorhersage {e['vorhersage_steigung']:.4f})")
        for z in e["zeilen"]:
            text.append(f"  {z['K']} | {z['D']:.2f} | {z['muster']} | {z['delta']} | {fz(z['Omega_p'])} | "
                        f"{z['Omega_p_vorhersage']:.4f} | {fz(z['verhaeltnis'])} | {z['q0']:+.4f} | {z['q_spanne']:.4f} | "
                        f"{z['q_max_abs']:.4f} | {z['max_verschiebung']:.3f} | {z['min_abstand_ende']:.2f}")
        text.append("  freie Paare: D0 | dphi | q0 | Spanne q | Nulldurchgaenge q | D min, max, Ende | verschmolzen")
        for z in erg_frei[stufe]:
            text.append(f"  {z['D0']} | {z['dphi']:.3f} | {z['q0']:+.4f} | {z['q_spanne']:.4f} | {z['nulldurchgaenge_q']} | "
                        f"{z['D_min']:.2f}, {z['D_max']:.2f}, {z['D_ende']:.2f} | {z['verschmolzen']}")
    text.append(f"  L3 (Omega_p): {sum(e['Omega_p']['bestanden'] for e in l3l)} von {len(l3l)}")
    return ({"laeufe": laeufe, "frei": frei, "ergebnis": erg, "ergebnis_frei": erg_frei, "L3": l3l}, text,
            {"ring": st, "frei": st_frei})


def t_ir(faktor):
    T = IR_T * faktor
    laeufe = [{"K": kz, "s0": IR_S0} for kz in IR_K] + [{"K": 12, "s0": 0.0}]
    km = max(r["K"] for r in laeufe)

    def bauen(dx, dt):
        bx = box(RING_L, dx, False)
        felder = []
        for r in laeufe:
            kz = r["K"]
            f, _ = ring_kette(bx, kz, [W2] * kz, [PI * j for j in range(kz)],
                              [r["s0"] * (1.0 if j % 2 == 0 else -1.0) for j in range(kz)])
            felder.append(f)
        psi, vel = stapel(felder)
        return {"box": bx, "psi": psi, "vel": vel, "messen": ring_messer(bx, laeufe, km)}
    st = stufen("ir", bauen, T)
    c = spalten(km, 1)

    def auswerten(t, d):
        zz = []
        for b, r in enumerate(laeufe):
            kz = r["K"]
            dd = RING_L / kz
            vz = torch.tensor([(-1.0) ** j for j in range(kz)], dtype=F64)
            orte0 = torch.tensor([-0.5 * RING_L + 0.5 * dd + j * dd for j in range(kz)], dtype=F64)
            u = ((d[:, b, c["x"]][:, :kz] - orte0) * vz).mean(1)
            q = (d[:, b, c["Q"]][:, :kz] * vz).mean(1)
            v = vorhersage_ring(dd)
            om = haupt(t, u, 0.0)
            n4 = max(2, len(t) // 4)
            zz.append({"K": kz, "D": dd, "s0": r["s0"], "Omega_vib": om, "Omega_vib_vorhersage": v["Omega_vib"],
                       "verhaeltnis": om / v["Omega_vib"] if math.isfinite(om) else float("nan"),
                       "u0": gf(u[0]), "u_spanne_anfang": gf(u[:n4].max() - u[:n4].min()),
                       "u_spanne_ende": gf(u[-n4:].max() - u[-n4:].min()), "q_max_abs": gf(q.abs().max()),
                       "Omega_p_vorhersage": v["Omega_p"]})
        return zz
    erg = {s: auswerten(st[s]["t"], st[s]["daten"]) for s in st}
    l3l = [{"D": g["D"], "Omega_vib": l3(g["Omega_vib"], f["Omega_vib"], 0.0)}
           for g, f in zip(erg["grob"], erg["fein"]) if g["s0"] > 0]
    text = [f"IR-Schwingung (Chemie 4): gegenphasiger Ring L = {RING_L}, Baelle abwechselnd um +-{IR_S0} verschoben, "
            f"T = {T:g}. Vorhersage Omega_vib = sqrt(4 kappa^2 J(D)/E).",
            "  K | D | s0 | Omega_vib | Vorhersage | Verhaeltnis | u0 | Spanne u Anfang, Ende | max|q| | (Omega_p Vorhersage)"]
    for stufe in ("grob", "fein"):
        text.append(f"  [{stufe}]")
        for z in erg[stufe]:
            text.append(f"  {z['K']} | {z['D']:.2f} | {z['s0']} | {fz(z['Omega_vib'])} | {z['Omega_vib_vorhersage']:.4f} | "
                        f"{fz(z['verhaeltnis'])} | {z['u0']:+.4f} | {z['u_spanne_anfang']:.4f}, {z['u_spanne_ende']:.4f} | "
                        f"{z['q_max_abs']:.2e} | ({z['Omega_p_vorhersage']:.4f})")
    text.append(f"  L3 (Omega_vib): {sum(e['Omega_vib']['bestanden'] for e in l3l)} von {len(l3l)}")
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3l}, text, st


def t_quorum(faktor):
    T = QU_T * faktor
    g = torch.Generator().manual_seed(QU_SEED)
    laeufe = []
    for kz in QU_K:
        laeufe.append({"K": kz, "alpha": (torch.rand(kz, generator=g, dtype=F64) * 2.0 * PI).tolist(), "art": "zufall"})
    laeufe.append({"K": 12, "alpha": [0.0] * 12, "art": "gleich"})
    laeufe.append({"K": 2, "alpha": (torch.rand(2, generator=g, dtype=F64) * 2.0 * PI).tolist(), "art": "entkoppelt"})
    km = max(r["K"] for r in laeufe)

    def bauen(dx, dt):
        bx = box(RING_L, dx, False)
        felder = []
        for r in laeufe:
            kz = r["K"]
            dd = RING_L / kz
            teile = []
            for j in range(kz):
                f, v = ball(bx, W2, -0.5 * RING_L + 0.5 * dd + j * dd, 0.0, PI * j)
                ca, sa = math.cos(r["alpha"][j]), math.sin(r["alpha"][j])
                teile.append((f * (1.0 + QU_ETA * ca), v * (1.0 + QU_ETA * ca) - QU_ETA * QU_OMB * sa * f))
            felder.append(plus(*teile))
        psi, vel = stapel(felder)
        return {"box": bx, "psi": psi, "vel": vel, "messen": ring_messer(bx, laeufe, km)}
    st = stufen("quorum", bauen, T)
    c = spalten(km, 1)

    def auswerten(t, d):
        oms = [haupt(t, d[:, b, c["B"]][:, 0], 0.0, 0.05) for b in range(len(laeufe))]
        oms = [o for o in oms if math.isfinite(o)]
        om_b = sorted(oms)[len(oms) // 2] if oms else QU_OMB
        n_fen = 4
        grenzen = torch.linspace(0.0, float(t[-1]), n_fen + 1).tolist()
        zz = []
        for b, r in enumerate(laeufe):
            kz = r["K"]
            bb = d[:, b, c["B"]][:, :kz]
            bb = bb - bb.mean(0, keepdim=True)
            rr, cc = [], []
            for i in range(n_fen):
                w = (t >= grenzen[i] - 1e-9) & (t <= grenzen[i + 1] + 1e-9)
                z = (bb[w] * torch.exp(-1j * om_b * t[w]).unsqueeze(1)).sum(0)
                a = z.abs().clamp(min=1e-300)
                rr.append(gf((z / a).mean().abs()))
                cc.append(gf(z.sum().abs() ** 2 / (kz * (a ** 2).sum())))
            zz.append({"K": kz, "D": RING_L / kz, "art": r["art"], "r_fenster": rr, "C_fenster": cc,
                       "r_anfang": rr[0], "r_ende": rr[-1], "C_anfang": cc[0], "C_ende": cc[-1],
                       "atem_amplitude_anfang": gf(bb[: len(t) // 4].std()), "atem_amplitude_ende": gf(bb[-len(t) // 4:].std())})
        return {"Omega_atem": om_b, "zeilen": zz}
    erg = {s: auswerten(st[s]["t"], st[s]["daten"]) for s in st}
    l3l = [{"K": g["K"], "art": g["art"], "r_ende": l3(g["r_ende"], f["r_ende"], g["r_anfang"])}
           for g, f in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"])]
    text = [f"Quorum (Bio 39): gegenphasiger Ring L = {RING_L}, K = {QU_K} (D = 15 / 10 / 7,5), Atemstoss eta = {QU_ETA} "
            f"mit Zufallsphasen (Seed {QU_SEED}), T = {T:g}. r = Kuramoto-Ordnung der Atemphasen, C = Kohaerenz, je in "
            "vier Zeitfenstern."]
    for stufe in ("grob", "fein"):
        e = erg[stufe]
        text.append(f"  [{stufe}] Atemfrequenz (Median) {fz(e['Omega_atem'])}")
        for z in e["zeilen"]:
            text.append(f"  K {z['K']} (D {z['D']:.1f}, {z['art']}): r {', '.join(f'{v:.3f}' for v in z['r_fenster'])}; "
                        f"C {', '.join(f'{v:.3f}' for v in z['C_fenster'])}; Atemamplitude {z['atem_amplitude_anfang']:.2e} -> "
                        f"{z['atem_amplitude_ende']:.2e}")
    text.append(f"  L3 (r_Ende gegen r_Anfang): {sum(e['r_ende']['bestanden'] for e in l3l)} von {len(l3l)}")
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3l}, text, st


# ---------------------------------------------------------------- Bio 16 Symbiose (freie Paare)

SY_D0, SY_T = 10.0, 800.0
SY_W2B = (0.70, 0.71, 0.72, 0.74, 0.78)


def t_symbiose(faktor):
    T = SY_T * faktor
    laeufe = [{"w2a": W2, "w2b": w, "dphi": 0.0} for w in SY_W2B] + [{"w2a": W2, "w2b": W2, "dphi": PI}]
    laeufe.append({"w2a": W2, "w2b": None, "dphi": 0.0})

    def bauen(dx, dt):
        bx = box(300.0, dx, True)
        felder = []
        for r in laeufe:
            if r["w2b"] is None:
                felder.append(ball(bx, r["w2a"], 0.0, 0.0, 0.0))
            else:
                felder.append(plus(ball(bx, r["w2a"], -0.5 * SY_D0, 0.0, 0.0),
                                   ball(bx, r["w2b"], 0.5 * SY_D0, 0.0, r["dphi"])))
        psi, vel = stapel(felder)
        zen = [[-0.5 * SY_D0, 0.5 * SY_D0] if r["w2b"] is not None else [0.0, 0.0] for r in laeufe]
        return {"box": bx, "psi": psi, "vel": vel,
                "messen": messer(bx, zen, [[4.0, 4.0]] * len(laeufe), [True, True], [[0.0]] * len(laeufe))}
    st = stufen("symbiose", bauen, T)
    c = spalten(2, 1)

    def auswerten(t, d):
        zz = []
        for b, r in enumerate(laeufe):
            q0, qt = gf(d[0, b, c["Qg"]]), gf(d[-1, b, c["Qg"]])
            e0, et = gf(d[0, b, c["Eg"]]), gf(d[-1, b, c["Eg"]])
            z = {"w2a": r["w2a"], "w2b": r["w2b"], "dphi": r["dphi"], "Q_box_0": q0, "Q_box_T": qt, "E_box_0": e0,
                 "E_box_T": et, "abgestrahlt_E": e0 - et, "abgestrahlt_Q": q0 - qt}
            if r["w2b"] is None:
                z["E_anker"] = anker_q_e(r["w2a"])[1]
                zz.append(z)
                continue
            dd = d[:, b, c["x"]][:, 1] - d[:, b, c["x"]][:, 0]
            e_einzeln = anker_q_e(r["w2a"])[1] + anker_q_e(r["w2b"])[1]
            q_summe = anker_q_e(r["w2a"])[0] + anker_q_e(r["w2b"])[0]
            w2m = anker_umkehr(q_summe)
            e_versch = anker_q_e(w2m)[1] if math.isfinite(w2m) else float("nan")
            w2t = anker_umkehr(qt)
            unter = torch.nonzero(dd < 1.5)
            z.update({"D_ende": gf(dd[-1]), "D_min": gf(dd.min()), "D_max": gf(dd.max()),
                      "t_verschmelzen": gf(t[int(unter[0, 0])]) if unter.numel() else float("nan"),
                      "E_einzeln_summe": e_einzeln, "bindung_start": e0 - e_einzeln,
                      "E_verschmolzen_anker": e_versch, "gewinn_verschmelzen": e_versch - e_einzeln,
                      "E_anker_zu_Q_ende": anker_q_e(w2t)[1] if math.isfinite(w2t) else float("nan")})
            z["anregung_ende"] = et - z["E_anker_zu_Q_ende"]
            if z["D_ende"] < 1.5:
                z["klasse"] = "verschmolzen"
            elif z["D_ende"] > 2.0 * SY_D0:
                z["klasse"] = "getrennt"
            else:
                z["klasse"] = "gebunden"
            zz.append(z)
        return zz
    erg = {s: auswerten(st[s]["t"], st[s]["daten"]) for s in st}
    l3l = [{"w2b": g["w2b"], "dphi": g["dphi"], "D_ende": l3(g["D_ende"], f["D_ende"], SY_D0)}
           for g, f in zip(erg["grob"], erg["fein"]) if g["w2b"] is not None]
    text = [f"Symbiose (Bio 16): freie Paare im Abstand {SY_D0}, links omega^2 = {W2}, rechts {SY_W2B}, gleichphasig; "
            f"dazu gegenphasig gleich und ein Einzelball. T = {T:g}.",
            "  rechts | dphi | Klasse | D min, max, Ende | t verschmelzen | Bindung Start | Gewinn Verschmelzen (Anker) | "
            "abgestrahlt E | Anregung Ende"]
    for stufe in ("grob", "fein"):
        text.append(f"  [{stufe}]")
        for z in erg[stufe]:
            if z["w2b"] is None:
                text.append(f"  Einzelball: E Box {z['E_box_0']:.6f} -> {z['E_box_T']:.6f} (Anker {z['E_anker']:.6f})")
                continue
            text.append(f"  {z['w2b']} | {z['dphi']:.3f} | {z['klasse']} | {z['D_min']:.2f}, {z['D_max']:.2f}, "
                        f"{z['D_ende']:.2f} | {fz(z['t_verschmelzen'])} | {z['bindung_start']:+.5f} | "
                        f"{fz(z['gewinn_verschmelzen'])} | {z['abgestrahlt_E']:.4f} | {fz(z['anregung_ende'])}")
    text.append(f"  L3 (D_Ende gegen D0): {sum(e['D_ende']['bestanden'] for e in l3l)} von {len(l3l)}")
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3l}, text, st


# ---------------------------------------------------------------- Bio 50 Lawinen

LW_L, LW_K, LW_T, LW_DT_STOSS = 240.0, 24, 500.0, 10.0
LW_ETA = (0.01, 0.03)
LW_SEEDS = (11, 12, 13, 14)
LW_SCHWELLE = 0.01


def t_lawinen(faktor):
    T = LW_T * faktor
    laeufe = [{"K": LW_K, "seed": s, "stoesse": True} for s in LW_SEEDS]
    laeufe += [{"K": LW_K, "seed": 0, "stoesse": False}, {"K": 8, "seed": LW_SEEDS[0], "stoesse": True}]
    km = LW_K
    n_st = max(0, int(math.floor(T / LW_DT_STOSS + 1e-9)) - 1)
    plan = []
    for r in laeufe:
        g = torch.Generator().manual_seed(r["seed"])
        balle = torch.randint(0, r["K"], (n_st,), generator=g).tolist()
        etas = (LW_ETA[0] + (LW_ETA[1] - LW_ETA[0]) * torch.rand(n_st, generator=g, dtype=F64)).tolist()
        plan.append(list(zip(balle, etas)) if r["stoesse"] else [])

    def bauen(dx, dt):
        bx = box(LW_L, dx, False)
        felder = []
        for r in laeufe:
            kz = r["K"]
            f, _ = ring_kette(bx, kz, [W2] * kz, [PI * j for j in range(kz)], [0.0] * kz)
            felder.append(f)
        psi, vel = stapel(felder)
        x = bx["x"]
        ereig = {}
        for m in range(n_st):
            fak = torch.ones(len(laeufe), bx["n"], dtype=F64, device=DEV)
            for b, r in enumerate(laeufe):
                if not plan[b]:
                    continue
                j, eta = plan[b][m]
                dd = LW_L / r["K"]
                xc = -0.5 * LW_L + 0.5 * dd + j * dd
                fak[b] = fak[b] + eta * (pdist(x, xc, LW_L).abs() < 0.5 * dd).to(F64)
            ereig[int(round((m + 1) * LW_DT_STOSS / dt))] = fak
        return {"box": bx, "psi": psi, "vel": vel, "messen": ring_messer(bx, laeufe, km), "ereignisse": ereig}
    st = stufen("lawinen", bauen, T)
    c = spalten(km, 1)

    def cluster(akt):
        m, kz = akt.shape
        gesehen = torch.zeros_like(akt)
        a = akt.tolist()
        s = gesehen.tolist()
        groessen, dauern = [], []
        for i in range(m):
            for j in range(kz):
                if not a[i][j] or s[i][j]:
                    continue
                stapel_ = [(i, j)]
                s[i][j] = True
                baelle, zeiten = set(), set()
                while stapel_:
                    p, q = stapel_.pop()
                    baelle.add(q)
                    zeiten.add(p)
                    for pp, qq in ((p + 1, q), (p - 1, q), (p, (q + 1) % kz), (p, (q - 1) % kz)):
                        if 0 <= pp < m and a[pp][qq] and not s[pp][qq]:
                            s[pp][qq] = True
                            stapel_.append((pp, qq))
                groessen.append(len(baelle))
                dauern.append(len(zeiten))
        return groessen, dauern

    def auswerten(t, d):
        zz = []
        for b, r in enumerate(laeufe):
            kz = r["K"]
            sj = d[:, b, c["S"]][:, :kz]
            akt = ((sj / sj[:1] - 1.0).abs() > LW_SCHWELLE)
            gr, du = cluster(akt)
            hist = [sum(1 for v in gr if v == n) for n in range(1, kz + 1)]
            zz.append({"K": kz, "seed": r["seed"], "stoesse": r["stoesse"], "n_stoesse": len(plan[b]),
                       "n_lawinen": len(gr), "groessen_hist": hist, "groesse_mittel": sum(gr) / len(gr) if gr else 0.0,
                       "groesse_max": max(gr) if gr else 0, "anteil_groesse_1": hist[0] / len(gr) if gr else float("nan"),
                       "dauer_max": max(du) * T_MESS if du else 0.0,
                       "aktiv_anteil_ende": gf(akt[-max(1, len(t) // 10):].to(F64).mean())})
        return zz
    erg = {s: auswerten(st[s]["t"], st[s]["daten"]) for s in st}
    l3l = [{"seed": g["seed"], "K": g["K"], "groesse_mittel": l3(g["groesse_mittel"], f["groesse_mittel"], 1.0)}
           for g, f in zip(erg["grob"], erg["fein"]) if g["stoesse"]]
    text = [f"Lawinen (Bio 50): gegenphasiger Ring L = {LW_L}, K = {LW_K} (D = 10), alle {LW_DT_STOSS} ein Stoss "
            f"(Faktor 1 + eta, eta in {LW_ETA}) auf einen zufaelligen Ball; Ereignis: |S_max/S_max(0) - 1| > {LW_SCHWELLE}; "
            f"Lawine = zusammenhaengendes Gebiet in (Zeit, Ball). T = {T:g}."]
    for stufe in ("grob", "fein"):
        text.append(f"  [{stufe}]")
        for z in erg[stufe]:
            text.append(f"  K {z['K']} Seed {z['seed']} Stoesse {z['n_stoesse']}: {z['n_lawinen']} Lawinen, Groesse mittel "
                        f"{z['groesse_mittel']:.2f}, max {z['groesse_max']}, Anteil 1 {fz(z['anteil_groesse_1'])}, "
                        f"Dauer max {z['dauer_max']:.1f}, aktiv Ende {z['aktiv_anteil_ende']:.2f}; Verteilung 1..: "
                        f"{z['groessen_hist'][:8]}")
    text.append(f"  L3 (mittlere Groesse gegen 1): {sum(e['groesse_mittel']['bestanden'] for e in l3l)} von {len(l3l)}")
    return {"laeufe": laeufe, "stossplan": plan, "ergebnis": erg, "L3": l3l}, text, st


# ---------------------------------------------------------------- W21 Bragg-Spiegel und W22 Anderson-Gas

BR_L, BR_T = 480.0, 700.0
BR_D = (10.0, 12.0)
BR_K0 = (0.22, 0.24, 0.25, 0.26, 0.27, 0.28, 0.30, 0.31, 0.32, 0.34, 0.38)
BR_K0_EINZEL = (0.22, 0.26, 0.31, 0.38)
BR_X0, BR_SIG, BR_EPS = -120.0, 25.0, 1e-3
BR_EBENEN = {10.0: (-210.0, -40.0), 12.0: (-216.0, -36.0)}
BR_EINZEL_X = -76.0

AN_L, AN_T, AN_K0 = 1400.0, 2200.0, 0.4189
AN_X0, AN_SIG, AN_EPS = -500.0, 40.0, 1e-3
AN_EBENEN = (-620.0, 230.0)
AN_START, AN_ABST, AN_PER = -400.0, (30.0, 40.0), 35.0
AN_N, AN_SEEDS = (4, 8, 16), (21, 22, 23, 24)
AN_N_SEEDS = [4]                   # --seeds (Notbremse, falls der Rauchtest mehr als 9 min hochrechnet)


def transmission_auswerten(t, d, laeufe, ref_von, basis_von, k_zellen):
    """T = Fluss durch die hintere Ebene / Fluss im leeren Lauf gleicher Welle; R = -Fluss vorn / derselbe Nenner.
    Laeufe mit Kette werden um den Kettenlauf ohne Paket bereinigt (falls vorhanden)."""
    c = spalten(k_zellen, 2)
    flu = integral(t, d[:, :, c["j"]].reshape(len(t), len(laeufe), 2))      # (B, 2)
    zz = []
    for b, r in enumerate(laeufe):
        if r.get("ohne_paket"):
            xs = d[:, b, c["x"]]
            zz.append({**r, "max_verschiebung": gf((xs - xs[:1]).abs().max()), "fluss_vorn": gf(flu[b, 0]),
                       "fluss_hinten": gf(flu[b, 1])})
            continue
        nb = ref_von(b)
        ba = basis_von(b)
        f_h, f_v = gf(flu[b, 1]), gf(flu[b, 0])
        if ba is not None:
            f_h -= gf(flu[ba, 1])
            f_v -= gf(flu[ba, 0])
        nenner = gf(flu[nb, 1]) if nb is not None else float("nan")
        tt = f_h / nenner if nenner else float("nan")
        xs = d[:, b, c["x"]]
        zz.append({**r, "T": tt, "R": -f_v / nenner if nenner else float("nan"), "fluss_hinten": f_h,
                   "nenner": nenner, "lnT": math.log(tt) if tt > 0 else float("nan"),
                   "max_verschiebung": gf((xs - xs[:1]).abs().max())})
    return zz


def t_bragg(faktor):
    T = BR_T * faktor
    laeufe = []
    for dd in BR_D:
        for k0 in BR_K0:
            laeufe.append({"art": "kette", "d": dd, "k0": k0})
    for k0 in BR_K0:
        laeufe.append({"art": "leer", "d": None, "k0": k0})
    for k0 in BR_K0_EINZEL:
        laeufe.append({"art": "einzel", "d": None, "k0": k0})
    for dd in BR_D:
        laeufe.append({"art": "kette", "d": dd, "k0": None, "ohne_paket": True})
    kz = 4

    def zellen(r):
        if r["d"] is None:
            return [BR_EINZEL_X] * kz
        dd = r["d"]
        orte = [-0.5 * BR_L + 0.5 * dd + j * dd for j in range(int(round(BR_L / dd)))]
        nah = sorted(orte, key=lambda o: abs(o - (BR_X0 + 40.0)))[:kz]
        return sorted(nah)

    def bauen(dx, dt):
        bx = box(BR_L, dx, False)
        felder = []
        for r in laeufe:
            teile = [leer(bx)]
            if r["art"] == "kette":
                nk = int(round(BR_L / r["d"]))
                f, _ = ring_kette(bx, nk, [W2] * nk, [PI * j for j in range(nk)], [0.0] * nk)
                teile.append(f)
            elif r["art"] == "einzel":
                teile.append(ball(bx, W2, BR_EINZEL_X, 0.0, 0.0))
            if r["k0"] is not None:
                teile.append(paket(bx, r["k0"], BR_X0, BR_SIG, BR_EPS))
            felder.append(plus(*teile))
        psi, vel = stapel(felder)
        eb = [list(BR_EBENEN[r["d"]]) if r["d"] is not None else list(BR_EBENEN[10.0]) for r in laeufe]
        return {"box": bx, "psi": psi, "vel": vel,
                "messen": messer(bx, [zellen(r) for r in laeufe], [[4.0] * kz] * len(laeufe), [True] * kz, eb)}
    st = stufen("bragg", bauen, T)

    def ref_von(b):
        k0 = laeufe[b]["k0"]
        for i, r in enumerate(laeufe):
            if r["art"] == "leer" and r["k0"] == k0:
                return i
        return None

    def basis_von(b):
        r = laeufe[b]
        if r["art"] != "kette":
            return None
        for i, q in enumerate(laeufe):
            if q.get("ohne_paket") and q["d"] == r["d"]:
                return i
        return None

    def auswerten(t, d):
        zz = transmission_auswerten(t, d, laeufe, ref_von, basis_von, kz)
        zus = {}
        for dd in BR_D:
            reihe = [z for z in zz if z["art"] == "kette" and z["d"] == dd and not z.get("ohne_paket")]
            gut = [z for z in reihe if math.isfinite(z["T"])]
            if gut:
                zmin = min(gut, key=lambda z: z["T"])
                zus[str(dd)] = {"k_bragg": PI / dd, "k0_minimum": zmin["k0"], "T_minimum": zmin["T"],
                                "T_max": max(z["T"] for z in gut)}
        return {"zeilen": zz, "zusammen": zus}
    erg = {s: auswerten(st[s]["t"], st[s]["daten"]) for s in st}
    l3l = [{"d": g["d"], "k0": g["k0"], "T": l3(g["T"], f["T"], 1.0)}
           for g, f in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]) if g["art"] == "kette" and not g.get("ohne_paket")]
    text = [f"Bragg-Kette (W21): gegenphasige Kette (0, pi) im Ring L = {BR_L}, d = {BR_D}, Paket sigma = {BR_SIG}, "
            f"eps = {BR_EPS} bei x = {BR_X0}; T = {T:g}. T und R bezogen auf den leeren Ring; Bragg k = pi/d."]
    for stufe in ("grob", "fein"):
        e = erg[stufe]
        text.append(f"  [{stufe}] " + "; ".join(f"d = {k}: k_Bragg {v['k_bragg']:.4f}, Minimum T = {v['T_minimum']:.4f} bei "
                                               f"k0 = {v['k0_minimum']}, T_max {v['T_max']:.4f}" for k, v in e["zusammen"].items()))
        for z in e["zeilen"]:
            if z.get("ohne_paket"):
                text.append(f"  Kette d = {z['d']} ohne Paket: max Verschiebung {z['max_verschiebung']:.3e}, Restfluss "
                            f"{z['fluss_vorn']:+.2e}, {z['fluss_hinten']:+.2e}")
            elif z["art"] != "leer":
                text.append(f"  {z['art']} d = {z['d']} k0 = {z['k0']}: T = {fz(z['T'], '.5f')}, R = {fz(z['R'], '.5f')}, "
                            f"max Verschiebung {z['max_verschiebung']:.2e}")
    text.append(f"  L3 (T gegen 1): {sum(e['T']['bestanden'] for e in l3l)} von {len(l3l)}")
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3l}, text, st


def t_anderson(faktor):
    T = AN_T * faktor
    laeufe = []
    for n in AN_N:
        for s in AN_SEEDS[:AN_N_SEEDS[0]]:
            g = torch.Generator().manual_seed(s * 100 + n)
            abst = (AN_ABST[0] + (AN_ABST[1] - AN_ABST[0]) * torch.rand(n - 1, generator=g, dtype=F64)).tolist()
            orte = [AN_START]
            for a in abst:
                orte.append(orte[-1] + a)
            ph = (torch.rand(n, generator=g, dtype=F64) * 2.0 * PI).tolist()
            laeufe.append({"art": "zufall", "N": n, "seed": s, "orte": orte, "phasen": ph})
    for n in AN_N:
        laeufe.append({"art": "periodisch", "N": n, "seed": 0, "orte": [AN_START + AN_PER * j for j in range(n)],
                       "phasen": [PI * j for j in range(n)]})
    laeufe.append({"art": "leer", "N": 0, "seed": 0, "orte": [], "phasen": []})
    laeufe.append({"art": "einzel", "N": 1, "seed": 0, "orte": [AN_START], "phasen": [0.0]})
    kz = 4

    def bauen(dx, dt):
        bx = box(AN_L, dx, False)
        felder = []
        for r in laeufe:
            teile = [leer(bx), paket(bx, AN_K0, AN_X0, AN_SIG, AN_EPS)]
            teile += [ball(bx, W2, o, 0.0, p) for o, p in zip(r["orte"], r["phasen"])]
            felder.append(plus(*teile))
        psi, vel = stapel(felder)
        zen = [aufgefuellt(r["orte"][:kz], kz) if r["orte"] else [AN_START] * kz for r in laeufe]
        return {"box": bx, "psi": psi, "vel": vel,
                "messen": messer(bx, zen, [[5.0] * kz] * len(laeufe), [True] * kz, [list(AN_EBENEN)] * len(laeufe))}
    st = stufen("anderson", bauen, T)
    i_leer = [i for i, r in enumerate(laeufe) if r["art"] == "leer"][0]

    def auswerten(t, d):
        zz = transmission_auswerten(t, d, laeufe, lambda b: i_leer, lambda b: None, kz)
        for z in zz:
            if z["art"] == "leer":
                z["max_verschiebung"] = float("nan")
        einzel = [z for z in zz if z["art"] == "einzel"][0]
        r1 = -math.log(einzel["T"]) if einzel["T"] > 0 else float("nan")
        mittel_ln = {}
        for n in AN_N:
            werte = [z["lnT"] for z in zz if z["art"] == "zufall" and z["N"] == n and math.isfinite(z["lnT"])]
            per = [z["lnT"] for z in zz if z["art"] == "periodisch" and z["N"] == n]
            mittel_ln[str(n)] = {"mittel_lnT_zufall": sum(werte) / len(werte) if werte else float("nan"),
                                 "streuung": (sum((v - sum(werte) / len(werte)) ** 2 for v in werte) / len(werte)) ** 0.5
                                 if werte else float("nan"),
                                 "lnT_periodisch": per[0] if per else float("nan"), "vorhersage_N_mal_einzel": -n * r1}
        xs = [(n, v["mittel_lnT_zufall"]) for n, v in ((int(k), v) for k, v in mittel_ln.items())
              if math.isfinite(v["mittel_lnT_zufall"])]
        steig = float("nan")
        if len(xs) >= 2:
            nm = sum(a for a, _ in xs) / len(xs)
            ym = sum(b for _, b in xs) / len(xs)
            steig = sum((a - nm) * (b - ym) for a, b in xs) / sum((a - nm) ** 2 for a, _ in xs)
        d_mittel = 0.5 * (AN_ABST[0] + AN_ABST[1])
        return {"zeilen": zz, "einzel_minus_lnT": r1, "mittel": mittel_ln, "steigung_lnT_je_ball": steig,
                "lokalisierungslaenge": -d_mittel / steig if steig and math.isfinite(steig) and steig < 0 else float("inf"),
                "max_verschiebung": max((z["max_verschiebung"] for z in zz if math.isfinite(z["max_verschiebung"])),
                                        default=float("nan"))}
    erg = {s: auswerten(st[s]["t"], st[s]["daten"]) for s in st}
    l3l = [{"N": n, "mittel_lnT": l3(erg["grob"]["mittel"][str(n)]["mittel_lnT_zufall"],
                                     erg["fein"]["mittel"][str(n)]["mittel_lnT_zufall"], 0.0)} for n in AN_N]
    text = [f"Anderson-Gas (W22): Baelle zufaellig ab x = {AN_START}, Abstaende in {AN_ABST}, Zufallsphasen, N = {AN_N}, "
            f"Seeds {AN_SEEDS[:AN_N_SEEDS[0]]}; periodisch mit Abstand {AN_PER}; Paket k0 = {AN_K0}, sigma = {AN_SIG}; Ring L = {AN_L}, "
            f"T = {T:g}."]
    for stufe in ("grob", "fein"):
        e = erg[stufe]
        text.append(f"  [{stufe}] Einzelball -ln T = {fz(e['einzel_minus_lnT'])}; Steigung <ln T> je Ball "
                    f"{fz(e['steigung_lnT_je_ball'])}; Lokalisierungslaenge {fz(e['lokalisierungslaenge'])}; max Verschiebung "
                    f"{fz(e['max_verschiebung'])}")
        for n, v in e["mittel"].items():
            text.append(f"  N = {n}: <ln T> zufall {fz(v['mittel_lnT_zufall'])} (Streuung {fz(v['streuung'])}), periodisch "
                        f"{fz(v['lnT_periodisch'])}, Vorhersage N x Einzel {fz(v['vorhersage_N_mal_einzel'])}")
    text.append(f"  L3 (<ln T> gegen 0): {sum(e['mittel_lnT']['bestanden'] for e in l3l)} von {len(l3l)}")
    return {"laeufe": [{k: v for k, v in r.items()} for r in laeufe], "ergebnis": erg, "L3": l3l}, text, st


# ---------------------------------------------------------------- Papierprobe Hintergrund (Wellen 6, 7, 11; Bio 2; Chemie 9)

HG_S = (1e-4, 1e-3, 0.01, 0.05, 0.1, 0.3, 0.5, 0.6, 2.0 / 3.0, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3)


def t_hintergrund(faktor):
    """Dispersion des ruhenden Hintergrunds: (k^2 - Om^2)(k^2 + M2 - Om^2) = 4 omega_bg^2 Om^2, M2 = 2 S U''(S)
    = 2 S (3 S - 2). Numerischer k-Scan gegen die Formeln gamma_max = |M2|/(4 omega_bg), Band k^2 < -M2,
    c_s^2 = M2/(M2 + 4 omega_bg^2); Landau v_c = min Om/k; Buckel-Loesungen gibt es nur fuer S = 0 (Vakuum)."""
    kk = torch.linspace(1e-4, 3.0, 30000, dtype=F64)
    zz = []
    for S in HG_S:
        w2 = u_strich(S)
        m2 = 2.0 * S * (3.0 * S - 2.0)
        bq = 2.0 * kk ** 2 + m2 + 4.0 * w2
        cq = kk ** 2 * (kk ** 2 + m2)
        disk = torch.sqrt((bq * bq - 4.0 * cq).clamp(min=0.0))
        om2_unten = 0.5 * (bq - disk)
        gam = torch.sqrt((-om2_unten).clamp(min=0.0))
        z = {"S": S, "omega_bg2": w2, "M2": m2, "gamma_max_formel": (-m2 / (4.0 * math.sqrt(w2))) if m2 < 0 else 0.0,
             "gamma_max_scan": gf(gam.max()), "k_band_formel": math.sqrt(-m2) if m2 < 0 else 0.0,
             "k_band_scan": gf(kk[gam > 0].max()) if bool((gam > 0).any()) else 0.0,
             "ring_stabil_L100": bool(m2 >= 0 or -m2 < (2 * PI / 100.0) ** 2),
             "ring_stabil_L300": bool(m2 >= 0 or -m2 < (2 * PI / 300.0) ** 2),
             "art_stationaer": ("keine" if m2 < 0 else ("Delle (Blase)" if S < 1.0 else "dunkles Soliton (Knick)"))}
        if m2 > 0:
            om = torch.sqrt(om2_unten.clamp(min=0.0))
            z["c_s_formel"] = math.sqrt(m2 / (m2 + 4.0 * w2))
            z["v_c_landau_scan"] = gf((om / kk).min())
        zz.append(z)
    krit = {str(L): (4.0 - math.sqrt(16.0 - 24.0 * (2 * PI / L) ** 2)) / 12.0 for L in (100.0, 200.0, 300.0)}
    text = ["Hintergrund (Papierprobe, keine Zeitentwicklung): S | omega_bg^2 | M2 | gamma_max Formel / Scan | "
            "k_Band Formel / Scan | Ring L=100 / 300 stabil | stationaere Form auf dem Hintergrund | c_s | v_c (Landau)"]
    for z in zz:
        text.append(f"  {z['S']:.4g} | {z['omega_bg2']:.4f} | {z['M2']:+.4e} | {z['gamma_max_formel']:.4e} / "
                    f"{z['gamma_max_scan']:.4e} | {z['k_band_formel']:.4e} / {z['k_band_scan']:.4e} | "
                    f"{z['ring_stabil_L100']} / {z['ring_stabil_L300']} | {z['art_stationaer']} | "
                    f"{fz(z.get('c_s_formel', float('nan')))} | {fz(z.get('v_c_landau_scan', float('nan')))}")
    text.append("  Kritische Dichte im Ring (alle Ringmoden ausserhalb des Bandes): " +
                ", ".join(f"L = {k}: S < {v:.3e}" for k, v in krit.items()))
    return {"zeilen": zz, "ring_kritisch": krit}, text, {}


# ---------------------------------------------------------------- Hauptprogramm

TESTS = {"osmose": t_osmose, "massenwirkung": t_massenwirkung, "pendeln": t_pendeln, "symbiose": t_symbiose,
         "quorum": t_quorum, "lawinen": t_lawinen, "ir": t_ir, "bragg": t_bragg, "anderson": t_anderson,
         "hintergrund": t_hintergrund}


def schreiben(out, ausgabe, text, reihen):
    with open(os.path.join(out, "r5c_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    with open(os.path.join(out, "r5c_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)
    torch.save(reihen, os.path.join(out, "r5c_zeitreihen.pt"))


def main():
    global DEV
    ap = argparse.ArgumentParser(description="Runde 5, R5-C: 1D mehrere Baelle und Hintergrund")
    ap.add_argument("unterbefehl", choices=sorted(TESTS) + ["rauch"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None)
    ap.add_argument("--nur", default=None, help="nur fuer rauch: Komma-Liste der Unterbefehle")
    ap.add_argument("--seeds", type=int, default=4, help="nur anderson: Zahl der Zufalls-Seeds je Laenge (1 bis 4)")
    ap.add_argument("--roh", default=None, help="v2: Rohdaten (r5c_zeitreihen.pt oder r5c_roh_zwischen.pt) eines "
                    "frueheren Laufs nur neu auswerten; gleicher Unterbefehl und gleiche Optionen wie dort")
    args = ap.parse_args()
    AN_N_SEEDS[0] = max(1, min(len(AN_SEEDS), args.seeds))
    if args.roh:
        VORRAT.update(roh_laden(args.roh))
        print(f"--roh: {sorted(VORRAT)} aus {args.roh}", flush=True)
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet sichtbar: Abbruch.")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 2 ** 30 / gesamt))
        name_geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
        name_geraet = "CPU, 1 Thread"
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe-" + args.unterbefehl)
    os.makedirs(out, exist_ok=True)
    if args.unterbefehl == "rauch":
        auswahl = args.nur.split(",") if args.nur else [n for n in TESTS if n != "hintergrund"]
        faktor = RAUCH_FAKTOR
    else:
        auswahl, faktor = [args.unterbefehl], 1.0
    start = jetzt()
    t_start = uhr()
    kopf = (f"R5-C r5c.py {VERSION}, Start {start} auf {name_geraet}, torch {torch.__version__}, Unterbefehl "
            f"{args.unterbefehl}, Laufzeitfaktor {faktor}" + (f", Rohdaten aus {args.roh}" if args.roh else ""))
    print(kopf, flush=True)
    ausgabe = {"version": VERSION, "start": start, "geraet": name_geraet, "torch": torch.__version__,
               "unterbefehl": args.unterbefehl, "faktor": faktor, "roh": args.roh, "ergebnisse": {}, "fehler": {},
               "sek": {}, "hochrechnung_s": {}}
    text, reihen = [kopf, ""], {}
    for name in auswahl:
        t0 = uhr()
        ROH.clear()
        ZWISCHEN[0] = os.path.join(out, "r5c_roh_zwischen.pt")
        try:
            res, zeilen, st = TESTS[name](faktor)
            ausgabe["ergebnisse"][name] = res
            text += zeilen
        except Exception:
            ausgabe["fehler"][name] = traceback.format_exc()
            text += [f"{name} FEHLER:", ausgabe["fehler"][name]]
            if ROH:
                text.append(f"  Rohdaten von {sorted(ROH)} sind in r5c_zeitreihen.pt gesichert; neu auswerten mit --roh")
            print(ausgabe["fehler"][name], flush=True)
        reihen[name] = dict(ROH)          # v2: flach je Stufenname, auch wenn die Auswertung scheitert
        sek = uhr() - t0
        ausgabe["sek"][name] = sek
        if faktor < 1.0:
            ausgabe["hochrechnung_s"][name] = sek / faktor
            text.append(f"  {name}: {sek:.1f} s bei Faktor {faktor}; Hochrechnung volle Laenge etwa {sek / faktor:.0f} s")
        else:
            text.append(f"  {name}: {sek:.1f} s")
        text.append("")
        schreiben(out, ausgabe, text, reihen)
    ausgabe["ende"] = jetzt()
    ausgabe["dauer_s"] = uhr() - t_start
    if DEV.type == "cuda":
        ausgabe["torch_speicher_max_mb"] = torch.cuda.max_memory_allocated() / 2 ** 20
    text.append(f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Torch-Speicher max "
                f"{ausgabe.get('torch_speicher_max_mb', float('nan')):.0f} MB, Fehler in: "
                f"{sorted(ausgabe['fehler']) if ausgabe['fehler'] else 'keine'}")
    schreiben(out, ausgabe, text, reihen)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
