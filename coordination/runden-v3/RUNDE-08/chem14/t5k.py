"""Runde 8, Zufallskarte Chem 14: Kontrolle zu Test 5 aus Runde 3 (Q gegen Anti-Q, 1D, omega^2 = 0,7).

In Runde 3 fehlte die Einzelkontrolle. Dieses Skript rechnet mit denselben Funktionen, Gittern, Stufen, Zeiten und
Messgroessen wie test5 in tests1d_r3.py:
- Ball allein bei -d/2
- Anti-Ball allein bei +d/2
- das Q/Anti-Q-Paar (theta = 0) als Wiederholung
Jeweils fuer d = 8 und 12. Nur Lesen und Rechnen, tests1d_r3.py bleibt unveraendert (Import aus runde3-tests1d).
Aufruf auf der .69: kleintest.sh p4000a <name> t5k.py [--kurz]
"""
import argparse
import json
import math
import os
import sys

sys.path.insert(0, "/home/fmh/fmhc-physics-remote/runde3-tests1d")
import torch  # noqa: E402
import tests1d_r3 as m  # noqa: E402


def laufliste():
    laeufe = []
    for d in (8.0, 12.0):
        laeufe.append({"d": d, "art": "ball allein", "teile": [(-0.5 * d, False)]})
        laeufe.append({"d": d, "art": "anti allein", "teile": [(0.5 * d, True)]})
        laeufe.append({"d": d, "art": "Q/anti", "teile": [(-0.5 * d, False), (0.5 * d, True)]})
    return laeufe


def kontrolle(p, kurz):
    w2 = 0.70
    iw = m.iw_von(w2)
    T, t_mess = 1000.0 * (0.1 if kurz else 1.0), 0.5
    laeufe = laufliste()
    stufen = {}
    for stufe, dx, dt in m.STUFEN:
        x = m.gitter(dx)
        q1 = m.energien(m.profil_werte(p, iw, x)[0].unsqueeze(0), [w2], dx)[3].item()
        psi, vel = m.stapel(len(laeufe), x)
        for n, r in enumerate(laeufe):
            for x0, anti in r["teile"]:
                a, b = m.ball(p, iw, x, x0, anti=anti)
                psi[n] = psi[n] + a
                vel[n] = vel[n] + b
        innen = x.abs() < m.X_INNEN
        innen_f, innen_m = innen.to(m.F64), innen[1:-1]

        def messen(psi, vel):
            s = m.s_von(psi)
            rho = m.rho_von(psi, vel)
            mitte = s[:, 1:-1]
            klumpen = ((mitte > s[:, :-2]) & (mitte >= s[:, 2:]) & (mitte > 0.05) & innen_m).sum(1).to(m.F64)
            return torch.stack([(rho.abs() * innen_f).sum(1) * dx, (rho * innen_f).sum(1) * dx,
                                (m.e_dichte(psi, vel, dx) * innen_f).sum(1) * dx, s.max(1).values, klumpen], dim=1)

        t0 = m.uhr()
        t, daten = m.entwickeln(psi, vel, x, dx, dt, T, messen, t_mess=t_mess)
        sek = m.uhr() - t0
        tc = t.cpu()
        q_abs, q_ges, e_in, s_max, klumpen = [y.cpu() for y in daten.unbind(dim=2)]
        breite = int(round(20.0 / t_mess))
        gm = q_abs.clone()
        for k in range(1, breite + 1):
            gm[k:] = torch.maximum(gm[k:], q_abs[:-k])

        def erste(maske):
            idx = maske.nonzero()
            return tc[idx[0, 0]].item() if idx.shape[0] > 0 else None

        zeilen = []
        for n, r in enumerate(laeufe):
            q0 = q_abs[0, n].item()
            z = {"d": r["d"], "art": r["art"], "q_abs0_zu_q1": q0 / q1,
                 "t50": erste((gm[:, n] <= 0.5 * q0) & (tc >= 20.0)),
                 "rest_q_abs_glatt": gm[-1, n].item() / q0, "rest_e": e_in[-1, n].item() / e_in[0, n].item(),
                 "q_ges_0": q_ges[0, n].item(), "q_ges_ende": q_ges[-1, n].item(),
                 "s_max_ende": s_max[-1, n].item(), "klumpen_ende": int(klumpen[-1, n])}
            zeilen.append(z)
        stufen[stufe] = {"sekunden": sek, "q1": q1, "laeufe": zeilen}
    fz, gz = stufen["fein"]["laeufe"], stufen["grob"]["laeufe"]
    l3 = [m.l3_quote(1.0 - a["rest_q_abs_glatt"], 1.0 - b["rest_q_abs_glatt"]) for a, b in zip(fz, gz)]
    text = ["Chem 14 Kontrolle (Runde 8): omega^2 = 0,7, T = " + m.zahl(T),
            "Laufzeit [s]: " + ", ".join(f"{s} {stufen[s]['sekunden']:.1f}" for s in stufen),
            "d | Art | Q_abs0/q1 | t50 | Rest Q_abs fein (glatt) | grob | Rest E fein | Q ges. 0 -> Ende | S_max Ende | "
            "Klumpen | L3"]
    for z, g, q in zip(fz, gz, l3):
        text.append(f"  {z['d']:4.1f} | {z['art']} | {z['q_abs0_zu_q1']:.4f} | {m.zahl(z['t50'])} | "
                    f"{m.zahl(z['rest_q_abs_glatt'])} | {m.zahl(g['rest_q_abs_glatt'])} | {m.zahl(z['rest_e'])} | "
                    f"{m.zahl(z['q_ges_0'])} -> {m.zahl(z['q_ges_ende'])} | {m.zahl(z['s_max_ende'])} | "
                    f"{z['klumpen_ende']} | {m.zahl(q)}")
    return {"test": "t5k", "T": T, "t_mess": t_mess, "stufen": stufen, "l3": l3}, "\n".join(text)


def main():
    ap = argparse.ArgumentParser(description="Chem 14 Kontrolle: Einzelbaelle und Q/Anti-Q, 1D")
    ap.add_argument("--out", default="/home/fmh/fmhc-physics-remote/runde8-chem14/ausgabe")
    ap.add_argument("--profil", default="/home/fmh/fmhc-physics-remote/runde3-tests1d/ausgabe/profile_r3.pt")
    ap.add_argument("--kurz", action="store_true")
    a = ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    os.makedirs(a.out, exist_ok=True)
    p = m.profile_holen(a.profil)
    start = m.jetzt()
    ausgabe, text = kontrolle(p, a.kurz)
    kopf = f"t5k: Start {start}, Ende {m.jetzt()}, {torch.cuda.get_device_name(0)}, kurz = {a.kurz}"
    name = "t5k" + ("_kurz" if a.kurz else "")
    with open(os.path.join(a.out, name + "_ergebnis.json"), "w") as fh:
        json.dump({**ausgabe, "start": start, "ende": m.jetzt()}, fh, indent=1)
    with open(os.path.join(a.out, name + "_bericht.txt"), "w") as fh:
        fh.write(kopf + "\n" + text + "\n")
    print(kopf + "\n" + text, flush=True)


if __name__ == "__main__":
    main()
