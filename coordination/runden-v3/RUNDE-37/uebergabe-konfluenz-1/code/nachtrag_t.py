#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERGABE-KONFLUENZ-1, Nachtrag nach Sicht (beschreibend, kein Urteil).

Anlass: Der eingefrorene Plan fand in 4 Saaten nur einen Fall der Art T (gemeinsames Tetraeder; 80 Kandidaten je Saat,
1 von 320 angenommen). Nur dieser eine Fall hatte in XY und YX verschiedene Zugwege.
Hier dieselbe eingefrorene Rechnung (konfluenz.py unveraendert importiert), nur mit mehr Kandidaten:
N_KAND = argv[2], ARTEN = ['T']. Aufruf: nachtrag_t.py <saat> <n_kand> <out.json>
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import konfluenz as kf  # noqa: E402


class A:
    pass


def main():
    s, nk, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    kf.N_KAND = nk
    kf.ARTEN = ['T']
    a = A()
    a.saat, a.rauch, a.faelle = s, False, None
    t0 = time.time()
    erg = kf.lauf(a)
    res = {'info': {'nachtrag': 'T mit mehr Kandidaten, beschreibend', 'N_KAND': nk, 'konfluenz_sha256': kf.sha(kf.__file__),
                    'skript_sha256': kf.sha(os.path.abspath(__file__)), 'argv': sys.argv},
           'ergebnis': erg, 'laufzeit_s': time.time() - t0}
    kf.schreibe(out, res)
    print('fertig nachtrag_t saat %d laufzeit %.1f s' % (s, res['laufzeit_s']), flush=True)


if __name__ == '__main__':
    main()
