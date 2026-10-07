"""ZUS-10 Idee 7 (Runde 9, Pruefung): Ist der Rest der Q/Anti-Q-Vernichtung ein Oszillon? 1D, omega^2 = 0,7.

Abgeleitet aus RUNDE-08/chem14/t5k.py (Chem 14): dieselben Funktionen, Gitter, Stufen (grob dx = 0,1 / fein 0,05) und
die Zeitentwicklung aus tests1d_r3.py (unveraendert importiert aus runde3-tests1d). Neu gegenueber t5k.py:
- Abstaende (--d) und Laufzeit (--T) als Argumente; Stapel: Paare theta = 0 je d, dazu ein Paar mit relativer Phase
  pi/2 (--d-theta) und ein Einzelball (Kontrolle) bei demselben d.
- Messung alle t_mess = 0,5: Q_abs und Q in |x| < X_INNEN (wie t5k), E in |x| < X_INNEN, E in |x| < 15, Q links (x < 0),
  Q rechts (x > 0), Re/Im psi(0), S_max.
- Auswertung im Skript: E15(t)/E15(0) bei t = 1000, 2000, 3000 (bzw. T); Spektrum von psi(0, t) im Fenster t >= T/3
  (Hann-Fenster, Hauptfrequenz mit Vorzeichen und Betrag, staerkste drei Spitzen); Vorzeichenwechsel von Q_links im
  Fenster t >= T/3, max |Q_links| dort, Korrelation Q_links gegen -Q_rechts; t50 und Rest wie t5k.
- --geraet cpu nur fuer den Rauchtest (m.DEV wird umgestellt); der Hauptlauf braucht CUDA wie t5k.
Aufruf: kleintest.sh p4000a <name> t5k_zus7.py --d 4,6,8 --d-theta 8 --T 3000 --out <ordner>
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
    """Zeitmessung dieser Kopie: CUDA nur synchronisieren, wenn tatsaechlich auf CUDA gerechnet wird (m.uhr()
    synchronisiert bedingungslos und bricht auf der CPU ab; das Fremdmodul bleibt unveraendert)."""
    if m.DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def laufliste(ds, d_theta):
    laeufe = []
    for d in ds:
        laeufe.append({"d": d, "art": "Q/anti", "theta": 0.0,
                       "teile": [(-0.5 * d, False, 0.0), (0.5 * d, True, 0.0)]})
    laeufe.append({"d": d_theta, "art": "Q/anti theta=pi/2", "theta": 0.5 * math.pi,
                   "teile": [(-0.5 * d_theta, False, 0.0), (0.5 * d_theta, True, 0.5 * math.pi)]})
    laeufe.append({"d": d_theta, "art": "ball allein", "theta": 0.0, "teile": [(-0.5 * d_theta, False, 0.0)]})
    return laeufe


def spektrum(z, t_mess, n_spitzen=3):
    """Hann-gefenstertes Spektrum einer komplexen Reihe; Kreisfrequenzen mit Vorzeichen (e^{-i Omega t} -> -Omega)."""
    n = z.shape[0]
    fenster = torch.hann_window(n, periodic=False, dtype=torch.float64, device=z.device)
    Z = torch.fft.fft(z * fenster)
    om = 2.0 * math.pi * torch.fft.fftfreq(n, d=t_mess).to(z.device)
    P = (Z.abs() ** 2)
    idx = torch.argsort(P, descending=True)
    spitzen = []
    for k in idx.tolist():
        if all(abs(om[k].item() - s["omega"]) > 0.05 for s in spitzen):
            spitzen.append({"omega": om[k].item(), "leistung": P[k].item()})
        if len(spitzen) >= n_spitzen:
            break
    haupt = spitzen[0]["omega"]
    # Leistung bei +|haupt| gegen -|haupt| (Ladungsasymmetrie des Rests)
    kp = int(torch.argmin((om - abs(haupt)).abs()))
    km = int(torch.argmin((om + abs(haupt)).abs()))
    return {"haupt_omega": haupt, "haupt_abs": abs(haupt), "spitzen": spitzen,
            "P_plus_durch_P_minus": (P[kp] / P[km]).item() if P[km] > 0 else float("inf")}


def vorzeichenwechsel(q):
    s = torch.sign(q)
    s = s[s != 0]
    return int((s[1:] * s[:-1] < 0).sum()) if s.numel() > 1 else 0


def kontrolle(p, a):
    w2 = 0.70
    iw = m.iw_von(w2)
    T, t_mess = a.T, 0.5
    laeufe = laufliste(a.ds, a.d_theta)
    stufen_liste = list(m.STUFEN)[:1] if a.kurz else list(m.STUFEN)
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
        breite = int(round(20.0 / t_mess))
        gm = q_abs.clone()
        for k in range(1, breite + 1):
            gm[k:] = torch.maximum(gm[k:], q_abs[:-k])

        def erste(maske):
            idx = maske.nonzero()
            return tc[idx[0, 0]].item() if idx.shape[0] > 0 else None

        def bei(reihe, tz):
            k = min(int(round(tz / t_mess)), reihe.shape[0] - 1)
            return reihe[k].item()

        i_f = int(round((T / 3.0) / t_mess))
        zeilen = []
        for n, r in enumerate(laeufe):
            q0 = q_abs[0, n].item()
            e150 = e15[0, n].item()
            ein0 = e_in[0, n].item()
            z0 = torch.complex(re0[:, n], im0[:, n])
            sp = spektrum(z0[i_f:], t_mess)
            ql, qr = q_l[i_f:, n], q_r[i_f:, n]
            korr = float(torch.corrcoef(torch.stack([ql, -qr]))[0, 1]) if ql.std() > 0 and qr.std() > 0 else float("nan")
            z = {"d": r["d"], "art": r["art"], "theta": r["theta"], "q_abs0_zu_q1": q0 / q1,
                 "t50": erste((gm[:, n] <= 0.5 * q0) & (tc >= 20.0)),
                 "rest_q_abs_glatt": gm[-1, n].item() / q0,
                 "E15_0": e150, "E_in_0": ein0, "E15_0_zu_E_in_0": e150 / ein0,
                 "E15_rel": {str(int(tz)): bei(e15[:, n], tz) / e150 for tz in (500.0, 1000.0, 2000.0, 3000.0, T) if tz <= T},
                 "E_in_rel_T": e_in[-1, n].item() / ein0,
                 "spektrum_psi0_fenster": sp, "fenster_ab_t": i_f * t_mess,
                 "q_links_wechsel_fenster": vorzeichenwechsel(ql), "q_links_max_abs_fenster": ql.abs().max().item(),
                 "q_rechts_max_abs_fenster": qr.abs().max().item(), "korr_q_links_gegen_minus_q_rechts": korr,
                 "q_ges_0": q_ges[0, n].item(), "q_ges_ende": q_ges[-1, n].item(),
                 "s_max_ende": s_max[-1, n].item(), "s_max_fenster_max": s_max[i_f:, n].max().item()}
            zeilen.append(z)
        stufen[stufe] = {"sekunden": sek, "q1": q1, "dx": dx, "dt": dt, "laeufe": zeilen,
                         "reihen": {"t": tc.tolist(), "E15": e15.T.tolist(), "q_links": q_l.T.tolist(),
                                    "q_rechts": q_r.T.tolist()}}
        text = [f"[{stufe}] dx = {dx}, dt = {dt}, T = {T}, {sek:.1f} s",
                "d | Art | Q_abs0/q1 | t50 | Rest Q_abs (glatt) | E15/E15(0) bei 500/1000/2000/3000 | E_in/E_in(0) Ende | "
                "Hauptfrequenz psi(0) (Fenster) |Omega| (Vorz.) | P+/P- | Q_links Wechsel | max|Q_l| | max|Q_r| | "
                "korr(Q_l, -Q_r) | S_max Ende"]
        for z in zeilen:
            sp = z["spektrum_psi0_fenster"]
            er = z["E15_rel"]
            text.append(f"  {z['d']:4.1f} | {z['art']:18s} | {z['q_abs0_zu_q1']:.4f} | {m.zahl(z['t50'])} | "
                        f"{m.zahl(z['rest_q_abs_glatt'])} | " + "/".join(f"{er.get(k, float('nan')):.4f}" for k in ("500", "1000", "2000", "3000"))
                        + f" | {z['E_in_rel_T']:.4f} | {sp['haupt_abs']:.4f} ({sp['haupt_omega']:+.4f}) | "
                        f"{m.zahl(sp['P_plus_durch_P_minus'])} | {z['q_links_wechsel_fenster']} | "
                        f"{z['q_links_max_abs_fenster']:.4f} | {z['q_rechts_max_abs_fenster']:.4f} | "
                        f"{m.zahl(z['korr_q_links_gegen_minus_q_rechts'])} | {m.zahl(z['s_max_ende'])}")
            text.append("        Spitzen: " + ", ".join(f"{s['omega']:+.4f} ({s['leistung']:.3e})" for s in sp["spitzen"]))
        print("\n".join(text), flush=True)
        stufen[stufe]["text"] = text
        with open(os.path.join(a.out, "t5k_zus7_zwischen.json"), "w") as fh:
            json.dump({k: {kk: vv for kk, vv in v.items() if kk != "reihen"} for k, v in stufen.items()}, fh, indent=1)
    return stufen


def main():
    ap = argparse.ArgumentParser(description="ZUS-10 Idee 7: Rest der Q/Anti-Q-Vernichtung (1D, omega^2 = 0,7)")
    ap.add_argument("--out", default="/home/fmh/fmhc-physics-remote/runde9-zus10/aus-t5k-zus7")
    ap.add_argument("--profil", default="/home/fmh/fmhc-physics-remote/runde3-tests1d/ausgabe/profile_r3.pt")
    ap.add_argument("--d", default="4,6,8", help="Abstaende der Paare (theta = 0)")
    ap.add_argument("--d-theta", dest="d_theta", type=float, default=8.0, help="Abstand fuer Paar pi/2 und Einzelball")
    ap.add_argument("--T", type=float, default=3000.0)
    ap.add_argument("--kurz", action="store_true", help="Rauchtest: T = 60, nur grobe Stufe")
    ap.add_argument("--geraet", default="cuda", choices=["cuda", "cpu"])
    a = ap.parse_args()
    a.ds = [float(v) for v in a.d.split(",")]
    if a.kurz:
        a.T = 60.0
    if a.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("Kein CUDA-Geraet: Abbruch (Hauptlauf wie t5k nur auf der GPU).")
        geraet = torch.cuda.get_device_name(0)
    else:
        m.DEV = torch.device("cpu")
        torch.set_num_threads(1)
        geraet = "CPU, 1 Faden (nur Rauchtest)"
    os.makedirs(a.out, exist_ok=True)
    p = m.profile_holen(a.profil)
    start = m.jetzt()
    print(f"t5k_zus7: Start {start}, {geraet}, T = {a.T}, d = {a.ds}, d_theta = {a.d_theta}, kurz = {a.kurz}", flush=True)
    stufen = kontrolle(p, a)
    ende = m.jetzt()
    kopf = f"t5k_zus7: Start {start}, Ende {ende}, {geraet}, T = {a.T}, d = {a.ds}, d_theta = {a.d_theta}, kurz = {a.kurz}"
    name = "t5k_zus7" + ("_kurz" if a.kurz else "")
    with open(os.path.join(a.out, name + "_ergebnis.json"), "w") as fh:
        json.dump({"test": "t5k_zus7", "T": a.T, "d": a.ds, "d_theta": a.d_theta, "start": start, "ende": ende,
                   "stufen": {k: {kk: vv for kk, vv in v.items() if kk != "text"} for k, v in stufen.items()}}, fh, indent=1)
    text = [kopf]
    for k, v in stufen.items():
        text += v["text"]
    with open(os.path.join(a.out, name + "_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    print(kopf, flush=True)


if __name__ == "__main__":
    main()
