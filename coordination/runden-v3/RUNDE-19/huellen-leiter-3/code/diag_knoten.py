#!/usr/bin/env python3
"""diag_knoten.py - HUELLEN-LEITER-3, PLAN-NACHTRAG-1, Diagnose D1 (keine Wertung).
Rang und Knotenzahl der Nullstellen von m_bc an den S-Wurzeln der Testlaeufe, mit Variante F und alt."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import glob
import time
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import huellen_leiter3 as H3   # unveraendert
S3 = H3.S3


def main():
    stufe, pdir, listejson, testmuster, aus = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    varianten = sys.argv[6].split(',') if len(sys.argv) > 6 else ['F', 'alt']
    mod = S3.modell_von('M2')
    liste = json.load(open(listejson))['w2']
    erg = dict(stufe=stufe, punkte=[])
    for fn in sorted(glob.glob(testmuster)):
        for sp in json.load(open(fn))['sprossen']:
            v = sp['versuche'][0]
            w2, rho = v['S']['w2'], v['S']['rho']
            za, anker = H3.anker_von(pdir, liste, w2)
            U = S3.Umgebung(mod, anker)
            e = dict(k=sp['k'], R_vorhergesagt=sp['R_vorhergesagt'], w2=w2, rho=rho,
                     S=dict(rang=v.get('kurve', {}).get('rang'), knoten=v.get('kurve', {}).get('knoten'),
                            knoten_alle=v.get('kurve', {}).get('knoten_alle')))
            for var in varianten:
                t1 = time.time()
                H3.setze_variante(var)
                kv = H3.kurve_an(mod, U, w2, rho)
                e[var] = dict(rang=kv.get('rang'), knoten=kv.get('knoten'), knoten_alle=kv.get('knoten_alle'),
                              d_rho=kv.get('d_rho'), n=kv.get('n'), sekunden=time.time() - t1)
            H3.setze_variante('S')
            erg['punkte'].append(e)
            H3.schreibe(aus, erg)
            H3.log('diag k=%d Rp=%.2f %s' % (sp['k'], sp['R_vorhergesagt'],
                                             json.dumps({x: (e[x]['rang'], e[x]['knoten']) for x in ['S'] + varianten})))
    H3.log('fertig')


if __name__ == '__main__':
    main()
