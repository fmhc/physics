#!/usr/bin/env python3
"""diag_umlauf.py - HUELLEN-LEITER-3, PLAN-NACHTRAG-2, Diagnose D2 (keine Wertung).
F-Newton ab der S-Wurzel und Rechteck-Umlauf von W mit F an den nicht angenommenen Sprossen einer Kurve."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import glob
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import huellen_leiter3 as H3   # unveraendert
S3 = H3.S3


def main():
    stufe, pdir, listejson, testmuster, aus, kurve = (int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4],
                                                     sys.argv[5], int(sys.argv[6]))
    mod = S3.modell_von('M2')
    liste = json.load(open(listejson))['w2']
    erg = dict(stufe=stufe, punkte=[])
    for fn in sorted(glob.glob(testmuster)):
        for sp in json.load(open(fn))['sprossen']:
            if sp['k'] != kurve or sp.get('gefunden_versuch') is not None:
                continue
            v = sp['versuche'][0]
            w2, rho = v['S']['w2'], v['S']['rho']
            za, anker = H3.anker_von(pdir, liste, w2)
            U = S3.Umgebung(mod, anker)
            H3.setze_variante('F')
            w2F, rhoF, okF, verlF, fF = H3.newton_W(U, w2, rho)
            e = dict(k=sp['k'], R_vorhergesagt=sp['R_vorhergesagt'], S=[w2, rho], F=[w2F, rhoF], ok=okF,
                     dF=[w2F - w2, rhoF - rho], verl=verlF, fehler=fF)
            if okF:
                e.update(H3.am_punkt(mod, U, w2F, rhoF))
                dwz = H3.dw2_zeile_an(liste, w2F)
                hmax = H3.halbbreite(mod, w2F, rhoF, v['kurve']['gap'], dwz)
                e['umlauf'] = H3.rechteck(U, w2F, rhoF, hmax)
            H3.setze_variante('S')
            erg['punkte'].append(e)
            H3.schreibe(aus, erg)
            u = e.get('umlauf', {})
            H3.log('diag2 k=%d Rp=%.2f stufe=%d ok=%s dF=%s umlauf=%s aufgeloest=%s sprung=%s punkte=%s' % (
                sp['k'], sp['R_vorhergesagt'], stufe, okF, e['dF'], u.get('umlauf'), u.get('aufgeloest'),
                u.get('groesster_sprung'), u.get('punkte')))
    H3.log('fertig')


if __name__ == '__main__':
    main()
