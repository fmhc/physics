#!/usr/bin/env python3
"""V-1-WEITER: Bilder als SVG (ohne matplotlib), aus lauf/*.json. Aufruf: python bilder.py <laufordner> <zielordner>"""
import glob
import json
import math
import os
import sys

RHO_WB = 1.7734530718064692
FARBEN = ["#1f6feb", "#d1242f", "#1a7f37", "#9a6700", "#8250df", "#bf3989", "#0a7d87", "#57606a", "#cf222e", "#116329"]


class Bild:
    def __init__(self, titel, xlab, ylab, xr, yr, b=760, h=470):
        self.b, self.h, self.xr, self.yr = b, h, xr, yr
        self.l, self.r, self.o, self.u = 80, 200, 40, 60
        self.teile = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{b}" height="{h}" font-family="sans-serif" '
                      f'font-size="12"><rect width="{b}" height="{h}" fill="white"/>',
                      f'<text x="{self.l}" y="22" font-size="14" font-weight="bold">{titel}</text>',
                      f'<text x="{(self.l + b - self.r) / 2}" y="{h - 15}" text-anchor="middle">{xlab}</text>',
                      f'<text x="18" y="{(self.o + h - self.u) / 2}" text-anchor="middle" '
                      f'transform="rotate(-90 18 {(self.o + h - self.u) / 2})">{ylab}</text>']
        self.legende = 0

    def px(self, x):
        return self.l + (x - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.b - self.l - self.r)

    def py(self, y):
        return self.h - self.u - (y - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.h - self.o - self.u)

    def achsen(self, xt, yt, xfmt=str, yfmt=str):
        x0, x1, y0, y1 = self.px(self.xr[0]), self.px(self.xr[1]), self.py(self.yr[0]), self.py(self.yr[1])
        self.teile.append(f'<rect x="{x0}" y="{y1}" width="{x1 - x0}" height="{y0 - y1}" fill="none" stroke="#333"/>')
        for t in xt:
            X = self.px(t)
            self.teile.append(f'<line x1="{X}" y1="{y0}" x2="{X}" y2="{y1}" stroke="#ddd"/>')
            self.teile.append(f'<text x="{X}" y="{y0 + 16}" text-anchor="middle">{xfmt(t)}</text>')
        for t in yt:
            Y = self.py(t)
            self.teile.append(f'<line x1="{x0}" y1="{Y}" x2="{x1}" y2="{Y}" stroke="#ddd"/>')
            self.teile.append(f'<text x="{x0 - 6}" y="{Y + 4}" text-anchor="end">{yfmt(t)}</text>')

    def linie(self, pts, farbe, name=None, offen=False, strich=True):
        pts = [(x, y) for x, y in pts if y is not None and math.isfinite(y)]
        if strich and len(pts) > 1:
            d = " ".join(f"{self.px(x):.1f},{self.py(y):.1f}" for x, y in pts)
            self.teile.append(f'<polyline points="{d}" fill="none" stroke="{farbe}" stroke-width="1.6"/>')
        for x, y in pts:
            fill = "white" if offen else farbe
            self.teile.append(f'<circle cx="{self.px(x):.1f}" cy="{self.py(y):.1f}" r="4" fill="{fill}" '
                              f'stroke="{farbe}" stroke-width="1.6"/>')
        if name:
            Y = self.o + 14 + 18 * self.legende
            X = self.b - self.r + 14
            fill = "white" if offen else farbe
            self.teile.append(f'<circle cx="{X}" cy="{Y - 4}" r="4" fill="{fill}" stroke="{farbe}" stroke-width="1.6"/>')
            self.teile.append(f'<text x="{X + 10}" y="{Y}">{name}</text>')
            self.legende += 1

    def text(self, x, y, s):
        self.teile.append(f'<text x="{x}" y="{y}" fill="#444">{s}</text>')

    def speichern(self, pfad):
        with open(pfad, "w") as fh:
            fh.write("\n".join(self.teile + ["</svg>"]))


def lade(ordner):
    out = {}
    for p in sorted(glob.glob(os.path.join(ordner, "*.json"))):
        name = os.path.basename(p)[:-5]
        if name in ("auswertung",):
            continue
        try:
            with open(p) as fh:
                d = json.load(fh)
        except Exception:
            continue
        if "nullstellen" not in d or not d["nullstellen"]:
            continue
        z = min(d["nullstellen"], key=lambda e: abs(e["rho_z"] - RHO_WB))
        out[name] = (d, z)
    return out


def main():
    ordner, ziel = sys.argv[1], sys.argv[2]
    daten = lade(ordner)
    # Bild 1: Restgroesse T_aus gegen rho - rho_z, Variante A
    offs = {"+0e+00": 0.0, "-1e-06": -1, "+1e-06": 1, "-1e-05": -2, "+1e-05": 2, "-1e-03": -4, "+1e-03": 4}
    b1 = Bild("Restgroesse T_aus um die stille Stelle (Variante A)", "rho - rho_z (Lage -1e-3 ... +1e-3, gestaucht)",
              "log10 T_aus", (-4.5, 4.5), (-28, 1))
    b1.achsen([-4, -2, -1, 0, 1, 2, 4], list(range(-28, 2, 4)),
              xfmt=lambda t: {-4: "-1e-3", -2: "-1e-5", -1: "-1e-6", 0: "0", 1: "1e-6", 2: "1e-5", 4: "1e-3"}[t])
    HAUPT = {"A_e0", "A_p1e-3", "A_p3e-3", "A_p1e-2", "A_m1e-3x", "A_m3e-3x", "A_m1e-2x", "B_e0", "B_p1e-3", "B_p3e-3",
             "B_p1e-2", "B_m1e-3x", "B_m3e-3x", "B_m1e-2x"}
    namen = [n for n in daten if n.startswith("A_") and n in HAUPT]
    namen.sort(key=lambda n: daten[n][0]["eps"])
    for i, n in enumerate(namen):
        d, z = daten[n]
        pts = sorted((offs[k], math.log10(max(v["T_aus"], 1e-300))) for k, v in z["streuung"].items() if k in offs)
        b1.linie(pts, FARBEN[i % len(FARBEN)], f"eps = {d['eps']:+g}")
    b1.text(90, 455 - 50, "Punkt bei 0: T_aus an der Nullstelle von E (Rechengrenze); V1-Schwelle 1e-10")
    b1.speichern(os.path.join(ziel, "bild1_restgroesse.svg"))
    # Bild 2: rho_z(eps)
    pts = {"A": [], "B": []}
    for n, (d, z) in daten.items():
        v = n[0] if n in HAUPT else "-"
        if v in pts:
            pts[v].append((d["eps"] * 1e3, (z["rho_z"] - RHO_WB) * 1e6))
    alle = [p for v in pts.values() for p in v] or [(0, 0)]
    ymin, ymax = min(p[1] for p in alle), max(p[1] for p in alle)
    pad = 0.1 * max(1e-3, ymax - ymin)
    b2 = Bild("Lage der stillen Stelle rho_z(eps)", "eps in 1e-3", "(rho_z - rho_z,WB) in 1e-6", (-11, 11),
              (ymin - pad, ymax + pad))
    st = (ymax - ymin + 2 * pad) / 6
    b2.achsen([-10, -5, -3, -1, 0, 1, 3, 5, 10], [ymin - pad + st * k for k in range(7)], yfmt=lambda t: f"{t:.1f}")
    b2.linie(sorted(pts["A"]), FARBEN[0], "Variante A")
    b2.linie(sorted(pts["B"]), FARBEN[1], "Variante B", offen=True, strich=False)
    b2.speichern(os.path.join(ziel, "bild2_rho_z.svg"))
    # Bild 3: Restkopplung gegen 1/sqrt|eps|
    b3 = Bild("Restkopplung in die neuen Aussenkanaele (eps < 0, Variante A und Zusatz)", "1/sqrt|eps|",
              "log10 P_neu (Fluss)", (5, 33), (-32, -4))
    b3.achsen([6, 10, 15, 20, 25, 31.6], list(range(-32, -3, 4)), xfmt=lambda t: f"{t:g}")
    auf, unauf = [], []
    for n, (d, z) in daten.items():
        if d["eps"] >= 0 or not ((n in HAUPT and n[0] == "A") or n.startswith("Z_")):
            continue
        amp = z["amp_neu_aus_max"]
        amp_l = z["lose_10rtol"]["amp_neu_aus_max"]
        ok = amp > 0 and abs(amp_l - amp) <= 0.2 * amp
        nb = "B" + n[1:]
        if n[0] == "A" and nb in daten:
            ampb = daten[nb][1]["amp_neu_aus_max"]
            ok = ok and abs(ampb - amp) <= 0.3 * amp
        p = (1.0 / math.sqrt(abs(d["eps"])), math.log10(max(z["P_neu_aus"], 1e-300)))
        (auf if ok else unauf).append(p)
    b3.linie(sorted(auf), FARBEN[2], "aufgeloest")
    b3.linie(sorted(unauf), FARBEN[1], "unter der Grenze (obere Schranke)", offen=True, strich=False)
    dpts, dun = [], []
    for n, (d, z) in daten.items():
        if n.startswith("D_"):
            amp, ampl = z["amp_neu_aus_max"], z["lose_10rtol"]["amp_neu_aus_max"]
            p = (1.0 / math.sqrt(abs(d["eps"])), math.log10(max(z["P_neu_aus"], 1e-300)))
            (dpts if (amp > 0 and abs(ampl - amp) <= 0.2 * amp) else dun).append(p)
    b3.linie(sorted(dpts), FARBEN[4], "Diagnose f0-Hintergrund")
    b3.linie(sorted(dun), FARBEN[4], "Diagnose f0, Rauschen", offen=True, strich=False)
    b3.speichern(os.path.join(ziel, "bild3_restkopplung.svg"))
    print("Bilder geschrieben:", sorted(os.listdir(ziel)))


if __name__ == "__main__":
    main()
