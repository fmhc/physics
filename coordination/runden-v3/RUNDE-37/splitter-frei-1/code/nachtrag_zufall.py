#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SPLITTER-FREI-1, Nachtrag nach Sicht (beschreibend, kein Urteil): Zufallsstoerung ohne Formziel als Gegenprobe.
Alle Punkte des Originalglases (Saat s) werden isotrop gaussisch verschoben, mittlerer Betrag = amp (wie die mittlere
Verschiebung des splitterarmen Baus), ohne Rueckweisung. Ausgabe im Format der Baudatei, damit das eingefrorene
sf.py hm --art sf --bau <datei> sie lesen kann (Feld qs = None: keine Formschranke).
Aufruf: nachtrag_zufall.py <saat> <amp> <zufallssaat> <out>
"""
import sys, os, json, hashlib, math
import numpy as np

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/splitter-frei-1/code')
import sf  # noqa: E402  (eingefroren, d4e03bf6...)
import tg  # noqa: E402


def main():
    saat, amp, rs, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    L, pos0 = sf.punkte_original(sf.N_GLAS, saat)
    rng = np.random.default_rng([7771, saat, rs])
    sigma = amp / (2.0 * math.sqrt(2.0 / math.pi))       # Mittel von |N(0, sigma^2 I_3)| = 2 sigma sqrt(2/pi)
    pos = np.mod(pos0 + sigma * rng.normal(size=pos0.shape), L)
    LV, p, G, O, pr = sf.triang(pos, L)
    mod = tg.modell(LV, p, G, O, pr)
    q, V, R = sf.form(sf.tet_X(LV, p, G, O))
    dl = np.linalg.norm(sf.minbild(pos - pos0, L), axis=1)
    bau = {'saat': saat, 'L': L, 'qs': None, 'amp_soll': amp, 'zufallssaat': rs, 'pos': pos.tolist(),
           'pos_sha256': hashlib.sha256(np.ascontiguousarray(pos).tobytes()).hexdigest(),
           'verschiebung': {'mittel_alle': float(dl.mean()), 'max': float(dl.max())}, 'zerlegung': pr}
    res = {'ergebnis': {'saaten': {str(saat): {'bau': bau, 'form': sf.form_statistik(q, V), 'pruefung': mod['pruefung'],
                                               'kristall': sf.kristall(p, L, mod['n'] * mod['l'][:, None])}}}}
    sf.schreibe(out, res)
    print('fertig zufall', saat, amp, rs, flush=True)


if __name__ == '__main__':
    main()
