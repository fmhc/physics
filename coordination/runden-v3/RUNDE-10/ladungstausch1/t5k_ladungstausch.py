"""LADUNGSTAUSCH-1 (Runde 10): Ladungstausch-Ball aus eng gestarteten Q/Anti-Q-Paaren, 1D.

Abgeleitet aus RUNDE-09/zusammenhaenge/pruefung/t5k_zus7.py (reparierte Fassung, ZUS-10 Idee 7), die aus
RUNDE-08/chem14/t5k.py stammt. Dieselben Funktionen, Gitter, Stufen (grob dx = 0,1 / fein 0,05) und die
Zeitentwicklung aus tests1d_r3.py (unveraendert importiert aus runde3-tests1d). Neu gegenueber t5k_zus7.py:
- omega^2 waehlbar (--w2, nur die vorgerechneten Profile 0,60 / 0,70 / 0,80 / 0,85 von tests1d_r3).
- Stapel: Q/Anti-Q-Paare fuer jedes d aus --d (theta = 0), ein gleichphasiges Q/Q-Paar bei --d-gleich (Kontrolle),
  optional ein Q/Anti-Q-Paar mit theta = pi/2 bei --d-theta, ein Einzelball (Kontrolle, --kein-einzel schaltet ab).
- Stufenwahl (--stufen grob,fein), Laufzeit --T.
- Auswertung je Lauf: E15(t)/E15(0) bei 500, 1000, 2000, 3000, T; Hauptfrequenz von psi(0, t) (Fenster t >= T/3,
  Hann); Tauschfrequenz Omega_swap aus dem Spektrum von Q_links(t) im selben Fenster (reelles Signal, ohne Gleichanteil);
  Vorzeichenwechsel von Q_links; spaete Verlustrate Gamma_E aus ln E15 ueber das letzte Drittel (lineare Anpassung);
  t_halb (E15 unter die Haelfte); Ladungssumme links + rechts am Ende.
Aufruf: kleintest.sh p4000a <name> t5k_ladungstausch.py --w2 0.7 --d 3,4,5,6 --d-gleich 4 --T 3000 --out <ordner>
"""
import argparse
import json
import math
import os
import sys
import time

sys.path.insert(0, "/home/fmh/fmhc-physics-remote/runde3-tests1d")
import torch  # noqa: E402
import tests1d_r3 as m  # noqa: E402

X_E15 = 15.0


def uhr():
    """CUDA nur synchronisieren, wenn auf CUDA gerechnet wird (m.uhr() synchronisiert bedingungslos)."""
    if m.DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def laufliste(a):
    laeufe = []
    for d in a.ds:
        laeufe.append({"d": d, "art": "Q/anti", "teile": [(-0.5 * d, False, 0.0), (0.5 * d, True, 0.0)]})
    if a.d_gleich > 0.0:
        d = a.d_gleich
        laeufe.append({"d": d, "art": "Q/Q gleichphasig", "teile": [(-0.5 * d, False, 0.0), (0.5 * d, False, 0.0)]})
    if a.d_theta > 0.0:
        d = a.d_theta
        laeufe.append({"d": d, "art": "Q/anti theta=pi/2",
                       "teile": [(-0.5 * d, False, 0.0), (0.5 * d, True, 0.5 * math.pi)]})
    if not a.kein_einzel:
        d = a.ds[0]
        laeufe.append({"d": d, "art": "ball allein", "teile": [(-0.5 * d, False, 0.0)]})
    return laeufe


def spektrum_komplex(z, t_mess, n_spitzen=3):
    n = z.shape[0]
    fenster = torch.hann_window(n, periodic=False, dtype=torch.float64, device=z.device)
    Z = torch.fft.fft(z * fenster)
    om = 2.0 * math.pi * torch.fft.fftfreq(n, d=t_mess).to(z.device)
    P = Z.abs() ** 2
    idx = torch.argsort(P, descending=True)
    spitzen = []
    for k in idx.tolist():
        if all(abs(om[k].item() - s["omega"]) > 0.05 for s in spitzen):
            spitzen.append({"omega": om[k].item(), "leistung": P[k].item()})
        if len(spitzen) >= n_spitzen:
            break
    haupt = spitzen[0]["omega"]
    kp = int(torch.argmin((om - abs(haupt)).abs()))
    km = int(torch.argmin((om + abs(haupt)).abs()))
    return {"haupt_omega": haupt, "haupt_abs": abs(haupt), "spitzen": spitzen,
            "P_plus_durch_P_minus": (P[kp] / P[km]).item() if P[km] > 0 else float("inf"),
            "aufloesung": 2.0 * math.pi / (n * t_mess)}


def spektrum_reell(q, t_mess, n_spitzen=3):
    """Spektrum eines reellen Signals ohne Gleichanteil (Tauschfrequenz)."""
    n = q.shape[0]
    fenster = torch.hann_window(n, periodic=False, dtype=torch.float64, device=q.device)
    Q = torch.fft.rfft((q - q.mean()) * fenster)
    om = 2.0 * math.pi * torch.fft.rfftfreq(n, d=t_mess).to(q.device)
    P = Q.abs() ** 2
    P[0] = 0.0
    idx = torch.argsort(P, descending=True)
    spitzen = []
    for k in idx.tolist():
        if all(abs(om[k].item() - s["omega"]) > 0.02 for s in spitzen):
            spitzen.append({"omega": om[k].item(), "leistung": P[k].item()})
        if len(spitzen) >= n_spitzen:
            break
    return {"haupt_omega": spitzen[0]["omega"], "spitzen": spitzen, "aufloesung": 2.0 * math.pi / (n * t_mess)}


def vorzeichenwechsel(q):
    s = torch.sign(q)
    s = s[s != 0]
    return int((s[1:] * s[:-1] < 0).sum()) if s.numel() > 1 else 0


def rate_spaet(t, e):
    """Lineare Anpassung von ln e ueber das letzte Drittel; Rueckgabe -Steigung (Energierate) oder nan."""
    i0 = int(round(t.shape[0] * 2 / 3))
    tt, ee = t[i0:], e[i0:]
    if ee.min() <= 0.0:
        return float("nan")
    y = torch.log(ee)
    tm, ym = tt.mean(), y.mean()
    steig = float(((tt - tm) * (y - ym)).sum() / ((tt - tm) ** 2).sum())
    return -steig


def kontrolle(p, a):
    w2 = a.w2
    iw = m.iw_von(w2)
    T, t_mess = a.T, 0.5
    laeufe = laufliste(a)
    stufen_liste = [s for s in m.STUFEN if s[0] in a.stufen]
    stufen = {}
    for stufe, dx, dt in stufen_liste:
        x = m.gitter(dx)
        q1 = m.energien(m.profil_werte(p, iw, x)[0].unsqueeze(0), [w2], dx)[3].item()
        psi, vel = m.stapel(len(laeufe), x)
        for n, r in enumerate(laeufe):
            for x0, anti, th in r["teile"]:
                b1, b2 = m.ball(p, iw, x, x0, theta=th, anti=anti)
                psi[n] = psi[n] + b1
                vel[n] = vel[n] + b2
        i0 = int(torch.nonzero(x.abs() < 0.5 * dx)[0, 0])
        innen_f = (x.abs() < m.X_INNEN).to(m.F64)
        e15_f = (x.abs() < X_E15).to(m.F64)
        links_f = (x < 0.0).to(m.F64)
        rechts_f = (x > 0.0).to(m.F64)

        def messen(psi, vel):
            s = m.s_von(psi)
            rho = m.rho_von(psi, vel)
            e = m.e_dichte(psi, vel, dx)
            return torch.stack([(rho.abs() * innen_f).sum(1) * dx, (rho * innen_f).sum(1) * dx,
                                (e * innen_f).sum(1) * dx, (e * e15_f).sum(1) * dx,
                                (rho * links_f).sum(1) * dx, (rho * rechts_f).sum(1) * dx,
                                psi[:, i0].real, psi[:, i0].imag, s.max(1).values], dim=1)

        t0 = uhr()
        t, daten = m.entwickeln(psi, vel, x, dx, dt, T, messen, t_mess=t_mess)
        sek = uhr() - t0
        tc = t.cpu()
        q_abs, q_ges, e_in, e15, q_l, q_r, re0, im0, s_max = [y.cpu() for y in daten.unbind(dim=2)]

        def bei(reihe, tz):
            k = min(int(round(tz / t_mess)), reihe.shape[0] - 1)
            return reihe[k].item()

        i_f = int(round((T / 3.0) / t_mess))
        zeilen = []
        for n, r in enumerate(laeufe):
            e150 = e15[0, n].item()
            ein0 = e_in[0, n].item()
            z0 = torch.complex(re0[:, n], im0[:, n])
            sp = spektrum_komplex(z0[i_f:], t_mess)
            ql, qr = q_l[i_f:, n], q_r[i_f:, n]
            sw = spektrum_reell(ql, t_mess) if ql.std() > 0 else {"haupt_omega": float("nan"), "spitzen": [], "aufloesung": float("nan")}
            korr = float(torch.corrcoef(torch.stack([ql, -qr]))[0, 1]) if ql.std() > 0 and qr.std() > 0 else float("nan")
            unter = torch.nonzero(e15[:, n] < 0.5 * e150).squeeze(1)
            z = {"d": r["d"], "art": r["art"], "E15_0": e150, "E_in_0": ein0,
                 "E15_rel": {str(int(tz)): bei(e15[:, n], tz) / e150 for tz in (500.0, 1000.0, 2000.0, 3000.0, T) if tz <= T},
                 "E_in_rel_T": e_in[-1, n].item() / ein0,
                 "t_halb_E15": tc[int(unter[0])].item() if unter.numel() > 0 else None,
                 "Gamma_E_spaet": rate_spaet(tc, e15[:, n]),
                 "spektrum_psi0": sp, "tausch": sw, "fenster_ab_t": i_f * t_mess,
                 "q_links_wechsel": vorzeichenwechsel(ql), "q_links_max_abs": ql.abs().max().item(),
                 "q_rechts_max_abs": qr.abs().max().item(), "korr_q_links_gegen_minus_q_rechts": korr,
                 "q_ges_0": q_ges[0, n].item(), "q_ges_ende": q_ges[-1, n].item(),
                 "q_links_ende": q_l[-1, n].item(), "q_rechts_ende": q_r[-1, n].item(),
                 "s_max_ende": s_max[-1, n].item(), "q_ball": 0.5 * q1}
            zeilen.append(z)
        stufen[stufe] = {"sekunden": sek, "q1": q1, "dx": dx, "dt": dt, "laeufe": zeilen,
                         "reihen": {"t": tc.tolist(), "E15": e15.T.tolist(), "q_links": q_l.T.tolist(),
                                    "q_rechts": q_r.T.tolist()}}
        text = [f"[{stufe}] omega^2 = {w2}, dx = {dx}, dt = {dt}, T = {T}, {sek:.1f} s, q1 (Ballladung) = {q1:.4f}",
                "d | Art | E15/E15(0) bei 500/1000/2000/3000/T | t_halb | Gamma_E spaet | |Omega| psi(0) (Vorz.) | "
                "P+/P- | Omega_swap (Aufl.) | Q_links Wechsel | max|Q_l| | korr(Q_l,-Q_r) | Q_l, Q_r Ende | S_max Ende"]
        for z in zeilen:
            sp, sw, er = z["spektrum_psi0"], z["tausch"], z["E15_rel"]
            text.append(f"  {z['d']:4.1f} | {z['art']:17s} | "
                        + "/".join(f"{er.get(k, float('nan')):.4f}" for k in ("500", "1000", "2000", "3000", str(int(T))))
                        + f" | {m.zahl(z['t_halb_E15'])} | {m.zahl(z['Gamma_E_spaet'], 3)} | {sp['haupt_abs']:.4f} ({sp['haupt_omega']:+.4f}) | "
                        f"{m.zahl(sp['P_plus_durch_P_minus'], 2)} | {m.zahl(sw['haupt_omega'])} ({m.zahl(sw['aufloesung'], 2)}) | "
                        f"{z['q_links_wechsel']} | {z['q_links_max_abs']:.4f} | {m.zahl(z['korr_q_links_gegen_minus_q_rechts'], 3)} | "
                        f"{z['q_links_ende']:+.4f}, {z['q_rechts_ende']:+.4f} | {m.zahl(z['s_max_ende'])}")
            text.append("        psi(0)-Spitzen: " + ", ".join(f"{s['omega']:+.4f} ({s['leistung']:.3e})" for s in sp["spitzen"])
                        + "; Q_links-Spitzen: " + ", ".join(f"{s['omega']:.4f} ({s['leistung']:.3e})" for s in sw["spitzen"]))
        print("\n".join(text), flush=True)
        stufen[stufe]["text"] = text
        with open(os.path.join(a.out, "zwischen.json"), "w") as fh:
            json.dump({k: {kk: vv for kk, vv in v.items() if kk != "reihen"} for k, v in stufen.items()}, fh, indent=1)
    return stufen


def main():
    ap = argparse.ArgumentParser(description="LADUNGSTAUSCH-1: Q/Anti-Q-Paare eng gestartet, 1D")
    ap.add_argument("--out", default="/home/fmh/fmhc-physics-remote/runde10-ladungstausch1/aus")
    ap.add_argument("--profil", default="/home/fmh/fmhc-physics-remote/runde3-tests1d/ausgabe/profile_r3.pt")
    ap.add_argument("--w2", type=float, default=0.7, help="omega^2 des Balls (0.60, 0.70, 0.80, 0.85)")
    ap.add_argument("--d", default="3,4,5,6", help="Abstaende der Q/Anti-Q-Paare (theta = 0)")
    ap.add_argument("--d-gleich", dest="d_gleich", type=float, default=4.0, help="Abstand des Q/Q-Kontrollpaars (0 = keins)")
    ap.add_argument("--d-theta", dest="d_theta", type=float, default=0.0, help="Abstand fuer Paar mit theta = pi/2 (0 = keins)")
    ap.add_argument("--kein-einzel", dest="kein_einzel", action="store_true")
    ap.add_argument("--stufen", default="grob,fein")
    ap.add_argument("--T", type=float, default=3000.0)
    ap.add_argument("--kurz", action="store_true", help="Rauchtest: T = 60, nur grob")
    ap.add_argument("--geraet", default="cuda", choices=["cuda", "cpu"])
    a = ap.parse_args()
    a.ds = [float(v) for v in a.d.split(",")]
    a.stufen = [s.strip() for s in a.stufen.split(",")]
    if a.kurz:
        a.T, a.stufen = 60.0, ["grob"]
    if a.w2 not in m.OMEGA2_ALLE:
        raise SystemExit(f"--w2 {a.w2} nicht vorgerechnet; erlaubt {m.OMEGA2_ALLE}")
    if a.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("Kein CUDA-Geraet: Abbruch (Hauptlauf nur auf der GPU).")
        geraet = torch.cuda.get_device_name(0)
    else:
        m.DEV = torch.device("cpu")
        torch.set_num_threads(1)
        geraet = "CPU, 1 Faden (nur Rauchtest)"
    os.makedirs(a.out, exist_ok=True)
    p = m.profile_holen(a.profil)
    start = m.jetzt()
    print(f"ladungstausch: Start {start}, {geraet}, omega^2 = {a.w2}, T = {a.T}, d = {a.ds}, d_gleich = {a.d_gleich}, "
          f"d_theta = {a.d_theta}, einzel = {not a.kein_einzel}, Stufen {a.stufen}, kurz = {a.kurz}", flush=True)
    stufen = kontrolle(p, a)
    ende = m.jetzt()
    kopf = (f"ladungstausch: Start {start}, Ende {ende}, {geraet}, omega^2 = {a.w2}, T = {a.T}, d = {a.ds}, "
            f"d_gleich = {a.d_gleich}, d_theta = {a.d_theta}, einzel = {not a.kein_einzel}, Stufen {a.stufen}, kurz = {a.kurz}")
    name = "ladungstausch" + ("_kurz" if a.kurz else "")
    with open(os.path.join(a.out, name + "_ergebnis.json"), "w") as fh:
        json.dump({"test": "ladungstausch", "w2": a.w2, "T": a.T, "d": a.ds, "d_gleich": a.d_gleich, "d_theta": a.d_theta,
                   "start": start, "ende": ende,
                   "stufen": {k: {kk: vv for kk, vv in v.items() if kk != "text"} for k, v in stufen.items()}}, fh, indent=1)
    text = [kopf]
    for k, v in stufen.items():
        text += v["text"]
    with open(os.path.join(a.out, name + "_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    print(kopf, flush=True)


if __name__ == "__main__":
    main()
