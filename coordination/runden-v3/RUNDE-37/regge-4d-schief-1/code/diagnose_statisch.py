#!/usr/bin/env python3
"""REGGE-4D-SCHIEF-1, nachtraegliche Diagnose (nach dem Einfrieren, nicht geurteilt): Spektrum von H(k) auf dem
statischen Gitter L = 32 (k_tau = 0) fuer s = 0,2. Wo liegt der kleinste Nicht-Null-Eigenwert, welche Mode ist es,
wie viele negative Eigenwerte gibt es wo? Importiert regge_schief.py unveraendert.
Aufruf: python diagnose_statisch.py <aus.json>
"""
import json
import sys

import numpy as np

import regge_schief as RS
import regge4d as R4


def main():
    s = 0.2
    L = 32
    git = RS.GitterSchief(RS.matrix_A(s))
    eT, _ = RS.ableitungen(git, [], "diag")
    f = np.fft.fftfreq(L) * 2.0 * np.pi
    g = np.meshgrid(f, f, f, indexing="ij")
    ksp = np.stack([x.ravel() for x in g], 1)
    ks = np.column_stack([np.zeros(len(ksp)), ksp])[1:]
    B = git.B0()
    Qb, _ = np.linalg.qr(B)
    out = {"s": s, "L": L}
    lam_all, nneg, kl, info = [], [], [], []
    for a in range(0, len(ks), 4096):
        kk = ks[a:a + 4096]
        _, Em, M = git.matrizen(kk, eT)
        H = R4.h_von_M(M)[0]
        lam, V = np.linalg.eigh(H)
        al = np.abs(lam)
        mit = al.mean(axis=1)
        order = np.argsort(al, axis=1)
        fuenf = np.take_along_axis(al, order[:, 4:5], 1)[:, 0] / mit
        nneg.extend(list(np.sum(lam <= -RS.NULL_REL * mit[:, None], axis=1)))
        kl.extend(list(fuenf))
        for i in np.argsort(fuenf)[:5]:
            v = V[i][:, order[i, 4]]
            info.append({"k_lat": kk[i].tolist(), "k_phys": (np.linalg.inv(git.A).T @ kk[i]).tolist(),
                         "betrag_k_lat": float(np.linalg.norm(kk[i])), "fuenfter_rel_mittel": float(fuenf[i]),
                         "eigenwert": float(lam[i][order[i, 4]]), "top_anteil": float(abs(v[git.top])),
                         "h_anteil": float(np.linalg.norm(Qb.T @ v) ** 2),
                         "eps_norm": float(np.linalg.norm(Em[i] @ v)),
                         "quelle_ueberlapp": float(abs(v[git.tau_index]))})
    kl = np.array(kl)
    nneg = np.array(nneg)
    info.sort(key=lambda x: x["fuenfter_rel_mittel"])
    out["kleinste_fuenfte"] = info[:10]
    out["n_neg_zaehlung"] = {str(int(k)): int(np.sum(nneg == k)) for k in np.unique(nneg)}
    out["fuenfter_quantile"] = [float(np.quantile(kl, q)) for q in (0.0, 0.001, 0.01, 0.1, 0.5)]
    out["punkte_unter_1e-4"] = int(np.sum(kl < 1e-4))
    out["punkte_unter_1e-3"] = int(np.sum(kl < 1e-3))
    print(json.dumps({k: out[k] for k in ("n_neg_zaehlung", "fuenfter_quantile", "punkte_unter_1e-4",
                                          "punkte_unter_1e-3")}))
    print(json.dumps(out["kleinste_fuenfte"][:3]))
    with open(sys.argv[1], "w") as f_:
        json.dump(out, f_, indent=1)


if __name__ == "__main__":
    main()
