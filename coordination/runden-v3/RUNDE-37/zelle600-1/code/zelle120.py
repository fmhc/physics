#!/usr/bin/env python3
"""ZELLE600-1, Nachtrag der Leitung (06:39): die 120-Zelle als Dual der 600-Zelle.

Ecken = normierte Mitten der 600 Tetraeder aus lauf-69/tetraeder.json, Kanten = Tetraederpaare mit gemeinsamem
Dreieck. Prueft Zahlen, Grad und Kantenlaengen, rechnet Adjazenz- und Laplace-Spektrum (600 x 600), vergleicht die
Vielfachheiten mit 1, 4, 9, 16, ... und zerlegt die Kugelfunktionen vom Grad k auf die Laplace-Niveaus.
Nur CPU, ein Thread, numpy. Aufruf: python zelle120.py <lauf-69-ordner>
"""
import itertools
import json
import math
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np

T0 = time.time()
START_UTC = datetime.now(timezone.utc).isoformat(timespec='seconds')
D = sys.argv[1] if len(sys.argv) > 1 else 'lauf-69'
PHI = (1.0 + math.sqrt(5.0)) / 2.0


def fl(x, nd=12):
    return float(round(float(x), nd))


def dump(name, obj, compact=False):
    path = os.path.join(D, name)
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        if compact:
            json.dump(obj, f, separators=(',', ':'), ensure_ascii=False)
        else:
            json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write('\n')
    os.replace(tmp, path)


V6 = np.array(json.load(open(os.path.join(D, 'ecken.json')))['koordinaten'])
TET = [tuple(t) for t in json.load(open(os.path.join(D, 'tetraeder.json')))['tetraeder']]
K6 = [tuple(e) for e in json.load(open(os.path.join(D, 'kanten.json')))['kanten']]
NT = len(TET)
C = np.array([V6[list(t)].sum(0) for t in TET])
C = C / np.linalg.norm(C, axis=1)[:, None]

# Kanten: Tetraeder mit gemeinsamem Dreieck
tri = defaultdict(list)
for i, t in enumerate(TET):
    for f in itertools.combinations(sorted(t), 3):
        tri[f].append(i)
je_dreieck = sorted(len(v) for v in tri.values())
kanten = sorted(tuple(sorted(v)) for v in tri.values() if len(v) == 2)
A = np.zeros((NT, NT))
for i, j in kanten:
    A[i, j] = A[j, i] = 1.0
grad = A.sum(1)
ip_k = np.array([C[i] @ C[j] for i, j in kanten])
G = C @ C.T
np.fill_diagonal(G, -2.0)
ip_max = float(G.max())
geo_paare = int((np.abs(G - ip_max) < 1e-9).sum() // 2)
geo_gleich_graph = bool(np.array_equal((np.abs(G - ip_max) < 1e-9).astype(float), A))
# Fuenfecke: die 5 Tetraeder um jede Kante der 600-Zelle bilden einen 5-Kreis im Graphen
tet_je_kante6 = defaultdict(list)
for i, t in enumerate(TET):
    for e in itertools.combinations(sorted(t), 2):
        tet_je_kante6[e].append(i)
fuenfecke_ok = 0
for e, ts in tet_je_kante6.items():
    sub = A[np.ix_(ts, ts)]
    if len(ts) == 5 and np.all(sub.sum(1) == 2):
        fuenfecke_ok += 1
# Dodekaeder: die 20 Tetraeder um jede Ecke der 600-Zelle (20 Ecken, Grad 3 im Teilgraphen)
dodeka_ok = 0
for v in range(V6.shape[0]):
    ts = [i for i, t in enumerate(TET) if v in t]
    sub = A[np.ix_(ts, ts)]
    if len(ts) == 20 and np.all(sub.sum(1) == 3):
        dodeka_ok += 1
theta_soll = math.acos(1.0 - 1.0 / (4.0 * PHI ** 4))
bau = {
    'ecken': NT, 'kanten': len(kanten), 'tetraeder_je_dreieck_min_max': [je_dreieck[0], je_dreieck[-1]],
    'grad_min_max': [int(grad.min()), int(grad.max())],
    'ecken_auf_S3_max_abw': fl(np.abs(np.linalg.norm(C, axis=1) - 1).max(), 16),
    'kantenwinkel_grad_min_max': [fl(math.degrees(math.acos(min(1.0, ip_k.max()))), 10), fl(math.degrees(math.acos(min(1.0, ip_k.min()))), 10)],
    'kantenwinkel_soll_grad': fl(math.degrees(theta_soll), 10),
    'sehne_min_max': [fl(math.sqrt(2 - 2 * ip_k.max()), 12), fl(math.sqrt(2 - 2 * ip_k.min()), 12)],
    'sehne_soll_1_durch_wurzel2_phi2': fl(1 / (math.sqrt(2) * PHI ** 2), 12),
    'naechste_nachbarn_geometrisch_paare': geo_paare,
    'naechste_nachbarn_geometrisch_gleich_graphkanten': geo_gleich_graph,
    'fuenfecke_um_kanten_der_600_zelle': fuenfecke_ok,
    'dodekaeder_um_ecken_der_600_zelle': dodeka_ok,
    'euler_600_minus_1200_plus_720_minus_120': NT - len(kanten) + fuenfecke_ok - dodeka_ok,
}
bau['n1_erfuellt'] = bool(NT == 600 and len(kanten) == 1200 and bau['grad_min_max'] == [4, 4]
                          and abs(ip_k.max() - ip_k.min()) < 1e-12 and abs(ip_k.min() - math.cos(theta_soll)) < 1e-12)

# Spektrum
L = 4.0 * np.eye(NT) - A
evL, vecL = np.linalg.eigh(L)
evA = np.linalg.eigvalsh(A)


def buendel(ev, tol=1e-6):
    order = np.argsort(ev)
    groups = []
    for idx in order:
        if groups and abs(ev[idx] - ev[groups[-1][-1]]) < tol:
            groups[-1].append(int(idx))
        else:
            groups.append([int(idx)])
    return groups


gL = buendel(evL)
niveaus = [{'niveau': m, 'laplace': fl(float(np.mean(evL[g])), 10), 'adjazenz': fl(4.0 - float(np.mean(evL[g])), 10),
            'vielfachheit': len(g), 'streuung': fl(float(np.ptp(evL[g])), 16)} for m, g in enumerate(gL)]
EL = [vecL[:, g] for g in gL]


def monome(maxgrad):
    ex = [e for e in itertools.product(range(maxgrad + 1), repeat=4) if sum(e) <= maxgrad]
    ex.sort(key=lambda e: (sum(e), e))
    return ex


KMAX = 8
EXP = monome(KMAX)
MON = np.stack([np.prod(C ** np.array(e, dtype=float), axis=1) for e in EXP], axis=1)
GR = np.array([sum(e) for e in EXP])
basen, raenge = {}, []
for k in range(KMAX + 1):
    U, s, _ = np.linalg.svd(MON[:, GR <= k], full_matrices=False)
    r = int((s > 1e-9 * s[0]).sum())
    raenge.append({'grad_bis': k, 'rang': r, 'neu': r - (raenge[-1]['rang'] if raenge else 0), 'kontinuum_k_plus_1_quadrat': (k + 1) ** 2,
                   'kleinster_behaltener_sv': fl(s[r - 1], 14), 'groesster_verworfener_sv': (fl(s[r], 18) if r < len(s) else None)})
    basen[k] = U[:, :r]
verteilung = []
for k in range(KMAX + 1):
    Qk = basen[k]
    Pn = Qk if k == 0 else Qk - basen[k - 1] @ (basen[k - 1].T @ Qk)
    U, s, _ = np.linalg.svd(Pn, full_matrices=False)
    Qn = U[:, s > 1e-6]
    gew = {}
    for m in range(len(EL)):
        w = float(np.linalg.norm(EL[m].T @ Qn) ** 2)
        if w > 1e-6:
            gew[str(m)] = fl(w, 6)
    verteilung.append({'grad': k, 'neue_dimension': int(Qn.shape[1]), 'gewicht_je_niveau': gew})

# Vergleich mit Wasserstoff und Kontinuum
mult = [n['vielfachheit'] for n in niveaus]
unterste_sechs = mult[:6]
lam1 = niveaus[1]['laplace']
traeger = []
for k in range(6):
    gew = verteilung[k]['gewicht_je_niveau']
    m_best = min((int(m) for m in gew), key=lambda m: niveaus[m]['laplace']) if gew else None
    # niedrigstes Niveau, das Grad-k-Anteil traegt, und sein Anteil an den (k+1)^2 Funktionen
    anteil = gew.get(str(m_best), 0.0) / max(1, verteilung[k]['neue_dimension']) if m_best is not None else None
    lk = niveaus[m_best]['laplace'] if m_best is not None else None
    traeger.append({'k': k, 'n': k + 1, 'niveau': m_best, 'laplace': lk, 'vielfachheit_niveau': niveaus[m_best]['vielfachheit'] if m_best is not None else None,
                    'anteil_grad_k_in_diesem_niveau': fl(anteil, 6) if anteil is not None else None,
                    'verhaeltnis_zu_k1': (fl(lk / lam1, 8) if (k > 0 and lk) else None), 'kontinuum_k_k_plus_2_durch_3': fl(k * (k + 2) / 3.0, 8),
                    'abw_prozent': (fl(100.0 * ((lk / lam1) / (k * (k + 2) / 3.0) - 1.0), 4) if (k > 0 and lk) else None)})
th = theta_soll
zonal = [fl(4.0 * (1.0 - math.sin((k + 1) * th) / ((k + 1) * math.sin(th))), 10) for k in range(8)]
urteile = {
    'N1': bau['n1_erfuellt'],
    'N2': unterste_sechs == [1, 4, 9, 16, 25, 36],
    'N3': bool(abs(niveaus[1]['laplace'] - PHI ** -4) < 1e-9 and abs(niveaus[2]['laplace'] - PHI ** -2) < 1e-9),
    'N4_kein_49': 49 not in mult,
    'N5_k2_k3_innerhalb_10_prozent': bool(all(t['abw_prozent'] is not None and abs(t['abw_prozent']) <= 10.0 for t in traeger[2:4])),
    'N6_anteil_ueber_90_prozent_k3_bis_k5': bool(all(t['anteil_grad_k_in_diesem_niveau'] is not None and t['anteil_grad_k_in_diesem_niveau'] > 0.9 for t in traeger[3:6])),
}
res = {
    'start_utc': START_UTC, 'quelle': 'lauf-69/ecken.json, tetraeder.json, kanten.json (zelle600.py)',
    'bau': bau,
    'anzahl_verschiedene_laplace_eigenwerte': len(niveaus),
    'laplace_niveaus': niveaus,
    'adjazenz_spur_probe': {'spur_A': fl(float(evA.sum()), 9), 'spur_A2': fl(float((evA ** 2).sum()), 9), 'soll_A2': 2 * len(kanten)},
    'vielfachheiten_unterste_20': mult[:20],
    'kugelfunktionen_rang_je_grad': raenge,
    'grad_auf_niveaus_verteilung': verteilung,
    'traeger_grad_k_unterstes_niveau': traeger,
    'zonale_schaetzung_laplace_k_0_bis_7': zonal,
    'urteile_maschinell': urteile,
    'laufzeit_s': round(time.time() - T0, 3),
    'ende_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
}
dump('zelle120.json', res)
dump('ansicht120.json', {'quelle': 'lauf-69/ansicht120.json aus code/zelle120.py (ZELLE600-1 Nachtrag, .69)',
                         'tetraeder': [x for t in TET for x in t], 'kanten_anzahl': len(kanten),
                         'laplace_unten': [{'wert': fl(n['laplace'], 5), 'vielfach': n['vielfachheit']} for n in niveaus[:12]]}, compact=True)
print(json.dumps({'urteile': urteile, 'bau': [NT, len(kanten), bau['grad_min_max'], bau['kantenwinkel_grad_min_max'], fuenfecke_ok, dodeka_ok],
                  'niveaus_unten': [(n['laplace'], n['vielfachheit']) for n in niveaus[:22]], 'verschiedene': len(niveaus),
                  'raenge': [r['rang'] for r in raenge], 'traeger': [(t['k'], t['niveau'], t['anteil_grad_k_in_diesem_niveau'], t['abw_prozent']) for t in traeger],
                  'laufzeit_s': res['laufzeit_s']}, ensure_ascii=False))
