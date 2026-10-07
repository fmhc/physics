#!/usr/bin/env python3
"""ZELLE600-1 (Runde 46). Finn: "Welche 600 Zelle? Bau die".

Baut die 600-Zelle {3,3,5} aus den 120 Einheitsquaternionen der binaeren Ikosaedergruppe 2I
(Rezept der Karte), prueft Gruppe, Zahlen und Regularitaet (Z0), rechnet die Regge-Kruemmung (Z3),
das Spektrum von Adjazenz- und Graph-Laplace-Matrix (Z1, Z2, Z4) mit Identitaetsprobe gegen die
Kugelfunktionen auf S^3, die Schalen um einen Pol und den 30er-Ring (Boerdijk-Coxeter-Helix).

Nur CPU, ein Thread, numpy. Aufruf: python zelle600.py <ausgabeordner>
Alles ist Geometrie und Darstellungstheorie, keine Messdaten.
"""
import itertools
import json
import math
import os
import platform
import socket
import sys
import time
from collections import defaultdict, deque
from datetime import datetime, timezone

import numpy as np

T0 = time.time()
START_UTC = datetime.now(timezone.utc).isoformat(timespec='seconds')
OUT = sys.argv[1] if len(sys.argv) > 1 else 'lauf-69'
os.makedirs(OUT, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
EPS = 1e-9
ZEIT = {}


def dump(name, obj, compact=False):
    path = os.path.join(OUT, name)
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        if compact:
            json.dump(obj, f, separators=(',', ':'), ensure_ascii=False)
        else:
            json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write('\n')
    os.replace(tmp, path)


def fl(x, nd=12):
    return float(round(float(x), nd))


def mark(name):
    ZEIT[name] = round(time.time() - T0, 3)


# ------------------------------------------------------------------ 1. Ecken (Rezept der Karte)
def parity(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2


verts, herkunft = [], []
for i in range(4):
    for s in (1.0, -1.0):
        v = [0.0] * 4
        v[i] = s
        verts.append(v)
        herkunft.append(8)
for signs in itertools.product((0.5, -0.5), repeat=4):
    verts.append(list(signs))
    herkunft.append(16)
BASE = [PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0]
for perm in itertools.permutations(range(4)):
    if parity(perm):
        continue
    for s in itertools.product((1.0, -1.0), repeat=3):
        vals = [s[0] * BASE[0], s[1] * BASE[1], s[2] * BASE[2], 0.0]
        v = [0.0] * 4
        for k in range(4):
            v[perm[k]] = vals[k]
        verts.append(v)
        herkunft.append(96)
V = np.array(verts, dtype=float)
N = V.shape[0]
norms = np.linalg.norm(V, axis=1)
G = V @ V.T
D2 = np.clip(2.0 - 2.0 * G, 0.0, None)
np.fill_diagonal(D2, np.inf)
min_abstand = float(np.sqrt(D2.min()))
np.fill_diagonal(D2, 0.0)
mark('ecken')


# ------------------------------------------------------------------ 2. Gruppe 2I (Quaternionen a + b i + c j + d k)
def qmul(p, q):
    a1, b1, c1, d1 = p[..., 0], p[..., 1], p[..., 2], p[..., 3]
    a2, b2, c2, d2 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    return np.stack([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                     a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                     a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2], axis=-1)


PROD = qmul(V[:, None, :], V[None, :, :]).reshape(-1, 4)
MUL = (PROD @ V.T).argmax(axis=1).reshape(N, N)
abgeschlossen_fehler = float(np.abs(PROD - V[MUL.reshape(-1)]).max())
E = int(np.argmin(np.linalg.norm(V - np.array([1.0, 0.0, 0.0, 0.0]), axis=1)))
latein = bool(all(len(set(MUL[i].tolist())) == N and len(set(MUL[:, i].tolist())) == N for i in range(N)))
INV = np.array([int(np.nonzero(MUL[i] == E)[0][0]) for i in range(N)])
inverse_ok = bool(all(MUL[INV[i], i] == E for i in range(N)))
assoz = bool(all(MUL[MUL[a, b], c] == MUL[a, MUL[b, c]] for a in range(N) for b in range(N) for c in range(0, N, 7)))
konj = set()
for x in range(N):
    konj.add(frozenset(int(MUL[MUL[g, x], INV[g]]) for g in range(N)))
konj_tab = []
for c in konj:
    re = float(V[next(iter(c)), 0])
    konj_tab.append({'realteil': fl(re), 'winkel_grad_quaternion': fl(math.degrees(math.acos(max(-1.0, min(1.0, re)))), 6),
                     'anzahl': len(c),
                     'realteil_einheitlich': bool(all(abs(V[i, 0] - re) < EPS for i in c))})
konj_tab.sort(key=lambda r: -r['realteil'])
ordnungen = defaultdict(int)
for i in range(N):
    x, o = i, 1
    while x != E:
        x = int(MUL[x, i])
        o += 1
    ordnungen[o] += 1
gruppe = {
    'abgeschlossen_max_fehler': abgeschlossen_fehler,
    'abgeschlossen': abgeschlossen_fehler < 1e-12,
    'einselement_index': E,
    'gruppentafel_lateinisches_quadrat': latein,
    'inverse_vorhanden': inverse_ok,
    'assoziativ_auf_tafel_stichprobe_jedes_7_c': assoz,
    'konjugationsklassen': konj_tab,
    'anzahl_konjugationsklassen': len(konj_tab),
    'elementordnungen': {str(k): v for k, v in sorted(ordnungen.items())},
}
mark('gruppe')

# ------------------------------------------------------------------ 3. Kanten, Dreiecke, Tetraeder
COS36 = PHI / 2.0
A = (np.abs(G - COS36) < EPS).astype(np.int64)
np.fill_diagonal(A, 0)
kanten = [(i, j) for i in range(N) for j in range(i + 1, N) if A[i, j]]
kanten_laengen = np.array([math.sqrt(max(0.0, 2.0 - 2.0 * G[i, j])) for i, j in kanten])
nb = [set(np.nonzero(A[i])[0].tolist()) for i in range(N)]
dreiecke = sorted((i, j, k) for i, j in kanten for k in (nb[i] & nb[j]) if k > j)
tetraeder = sorted((i, j, k, l) for i, j, k in dreiecke for l in (nb[i] & nb[j] & nb[k]) if l > k)
mark('komplex')

tet_je_kante, tet_je_ecke, tet_je_dreieck = defaultdict(int), defaultdict(int), defaultdict(int)
for t in tetraeder:
    for a in t:
        tet_je_ecke[a] += 1
    for e in itertools.combinations(t, 2):
        tet_je_kante[e] += 1
    for f in itertools.combinations(t, 3):
        tet_je_dreieck[f] += 1
kanten_set = set(kanten)
link_info, link_ok = None, True
for v in range(N):
    le = sorted(nb[v])
    lk = [e for e in itertools.combinations(le, 2) if A[e[0], e[1]]]
    ld = [f for f in itertools.combinations(le, 3) if A[f[0], f[1]] and A[f[0], f[2]] and A[f[1], f[2]]]
    gr = [sum(1 for e in lk if u in e) for u in le]
    info = (len(le), len(lk), len(ld), min(gr), max(gr))
    if v == E:
        link_info = info
    if info != (12, 30, 20, 5, 5):
        link_ok = False

L0 = 1.0 / PHI
tet_kante_abw, vols = 0.0, []
for t in tetraeder:
    P4 = V[list(t)]
    for a, b in itertools.combinations(range(4), 2):
        tet_kante_abw = max(tet_kante_abw, abs(float(np.linalg.norm(P4[a] - P4[b])) - L0))
    M = P4[1:] - P4[0]
    vols.append(math.sqrt(max(0.0, float(np.linalg.det(M @ M.T)))) / 6.0)
vols = np.array(vols)
V_SOLL = L0 ** 3 / (6.0 * math.sqrt(2.0))
nE, nK, nD, nT = N, len(kanten), len(dreiecke), len(tetraeder)
z0 = {
    'ecken': nE, 'kanten': nK, 'dreiecke': nD, 'tetraeder': nT,
    'euler_charakteristik': nE - nK + nD - nT,
    'ecken_alle_auf_einheitssphaere_max_abw': fl(np.abs(norms - 1.0).max(), 16),
    'kleinster_eckenabstand': fl(min_abstand, 15),
    'nachbarn_je_ecke_min_max': [int(A.sum(1).min()), int(A.sum(1).max())],
    'tetraeder_je_kante_min_max': [min(tet_je_kante.values()), max(tet_je_kante.values())],
    'jede_kante_in_einem_tetraeder': set(tet_je_kante) == kanten_set,
    'tetraeder_je_ecke_min_max': [min(tet_je_ecke.values()), max(tet_je_ecke.values())],
    'tetraeder_je_dreieck_min_max': [min(tet_je_dreieck.values()), max(tet_je_dreieck.values())],
    'dreiecke_je_kante_min_max': [None, None],
    'eckfigur_pol_ecken_kanten_dreiecke_grad': list(link_info),
    'eckfigur_ueberall_ikosaeder': link_ok,
    'kantenlaenge_soll_1_durch_phi': fl(L0, 15),
    'kantenlaenge_min_max': [fl(kanten_laengen.min(), 15), fl(kanten_laengen.max(), 15)],
    'tetraeder_kanten_max_abw': fl(tet_kante_abw, 16),
    'tetraedervolumen_soll': fl(V_SOLL, 15),
    'tetraedervolumen_min_max': [fl(vols.min(), 15), fl(vols.max(), 15)],
}
dr_je_kante = defaultdict(int)
for f in dreiecke:
    for e in itertools.combinations(f, 2):
        dr_je_kante[e] += 1
z0['dreiecke_je_kante_min_max'] = [min(dr_je_kante.values()), max(dr_je_kante.values())]
z0['erfuellt'] = bool(
    (nE, nK, nD, nT) == (120, 720, 1200, 600) and z0['euler_charakteristik'] == 0
    and z0['nachbarn_je_ecke_min_max'] == [12, 12] and z0['tetraeder_je_kante_min_max'] == [5, 5]
    and z0['tetraeder_je_ecke_min_max'] == [20, 20] and z0['tetraeder_je_dreieck_min_max'] == [2, 2]
    and z0['jede_kante_in_einem_tetraeder'] and link_ok
    and abs(kanten_laengen.max() - L0) < 1e-12 and abs(kanten_laengen.min() - L0) < 1e-12
    and tet_kante_abw < 1e-12 and abs(vols.max() - V_SOLL) < 1e-12 and abs(vols.min() - V_SOLL) < 1e-12)
mark('z0')

# ------------------------------------------------------------------ 4. Regge-Kruemmung (Z3)
dieder_summe = defaultdict(float)
dieder_alle = []
for t in tetraeder:
    for a, b in itertools.combinations(t, 2):
        c, d = [x for x in t if x not in (a, b)]
        e = V[b] - V[a]
        e = e / np.linalg.norm(e)
        u = V[c] - V[a]
        u = u - (u @ e) * e
        w = V[d] - V[a]
        w = w - (w @ e) * e
        ang = math.acos(max(-1.0, min(1.0, float(u @ w) / (np.linalg.norm(u) * np.linalg.norm(w)))))
        dieder_summe[(a, b)] += ang
        dieder_alle.append(ang)
dieder_alle = np.array(dieder_alle)
delta = np.array([2.0 * math.pi - dieder_summe[e] for e in kanten])
summe_l_delta = float((kanten_laengen * delta).sum())
kontinuum = 6.0 * math.pi ** 2
V_flach = float(vols.sum())
R_eff = (V_flach / (2.0 * math.pi ** 2)) ** (1.0 / 3.0)
delta_analytisch = 2.0 * math.pi - 5.0 * math.acos(1.0 / 3.0)
regge = {
    'radius_R': 1.0,
    'diederwinkel_grad_min_max': [fl(math.degrees(dieder_alle.min()), 10), fl(math.degrees(dieder_alle.max()), 10)],
    'diederwinkel_soll_arccos_1_3_grad': fl(math.degrees(math.acos(1.0 / 3.0)), 10),
    'fehlwinkel_je_kante_grad_min_max': [fl(math.degrees(delta.min()), 10), fl(math.degrees(delta.max()), 10)],
    'fehlwinkel_analytisch_grad': fl(math.degrees(delta_analytisch), 10),
    'fehlwinkel_analytisch_rad': fl(delta_analytisch, 12),
    'summe_l_delta': fl(summe_l_delta, 10),
    'kontinuum_6_pi2_R': fl(kontinuum, 10),
    'verhaeltnis_umkreis': fl(summe_l_delta / kontinuum, 10),
    'abweichung_prozent_umkreis': fl(100.0 * (summe_l_delta / kontinuum - 1.0), 6),
    'volumen_flach_600_tetraeder': fl(V_flach, 10),
    'volumen_S3_2_pi2': fl(2.0 * math.pi ** 2, 10),
    'R_eff_gleiches_volumen': fl(R_eff, 10),
    'kontinuum_6_pi2_R_eff': fl(kontinuum * R_eff, 10),
    'verhaeltnis_gleiches_volumen': fl(summe_l_delta / (kontinuum * R_eff), 10),
    'abweichung_prozent_gleiches_volumen': fl(100.0 * (summe_l_delta / (kontinuum * R_eff) - 1.0), 6),
}
regge['z3_erfuellt_5_prozent'] = bool(abs(regge['abweichung_prozent_umkreis']) <= 5.0)
mark('regge')

# ------------------------------------------------------------------ 5. Schalen um den Pol
ip = G[E]
keys = np.round(ip, 9).tolist()
werte = sorted(set(keys), reverse=True)
schale_w = [werte.index(k) for k in keys]
dist = [-1] * N
dist[E] = 0
dq = deque([E])
while dq:
    x = dq.popleft()
    for y in sorted(nb[x]):
        if dist[y] < 0:
            dist[y] = dist[x] + 1
            dq.append(y)
nW, nG = len(werte), max(dist) + 1
kreuz = [[0] * nG for _ in range(nW)]
for i in range(N):
    kreuz[schale_w[i]][dist[i]] += 1
gemeinsam = defaultdict(set)
for i in range(N):
    if dist[i] == 2:
        gemeinsam[schale_w[i]].add(len(nb[i] & nb[E]))
schalen = {
    'pol_index': E,
    'pol_koordinaten': V[E].tolist(),
    'nach_winkel': [{'schale': s, 'skalarprodukt': fl(werte[s]), 'winkel_grad': fl(math.degrees(math.acos(max(-1.0, min(1.0, werte[s])))), 6),
                     'radius_stereographisch_tan_halbe': (fl(math.tan(math.acos(max(-1.0, min(1.0, werte[s]))) / 2.0), 6) if werte[s] > -1 + 1e-9 else None),
                     'anzahl': schale_w.count(s), 'ecken': [i for i in range(N) if schale_w[i] == s]} for s in range(nW)],
    'nach_graphabstand': [{'abstand': d, 'anzahl': dist.count(d), 'ecken': [i for i in range(N) if dist[i] == d]} for d in range(nG)],
    'kreuztabelle_zeile_winkelschale_spalte_graphabstand': kreuz,
    'gemeinsame_nachbarn_mit_pol_bei_abstand_2_je_winkelschale': {str(k): sorted(v) for k, v in sorted(gemeinsam.items())},
}
schalen['graph_abstandsregulaer_bei_abstand_2'] = len(set().union(*gemeinsam.values())) == 1
mark('schalen')

# ------------------------------------------------------------------ 6. Spektrum (Z1, Z2, Z4)
Af = A.astype(float)
evA, vecA = np.linalg.eigh(Af)
Lm = 12.0 * np.eye(N) - Af
evL, vecL = np.linalg.eigh(Lm)


def buendel(ev, tol=1e-6):
    order = np.argsort(ev)
    groups = []
    for idx in order:
        if groups and abs(ev[idx] - ev[groups[-1][-1]]) < tol:
            groups[-1].append(int(idx))
        else:
            groups.append([int(idx)])
    return groups


GESCHLOSSEN = [('12', 12.0, '1 = V_0 (k=0)'), ('6 phi', 6 * PHI, '2 = V_1/2 (k=1)'), ('4 phi', 4 * PHI, '3 = V_1 (k=2)'),
               ('3', 3.0, '4s = V_3/2 (k=3)'), ('0', 0.0, '5 = V_2 (k=4)'), ('-2', -2.0, '6 = V_5/2 (k=5)'),
               ('-4/phi', -4.0 / PHI, "3' Galois-Partner von 3"), ('-3', -3.0, '4 aus A5 (nicht spinoriell)'),
               ('-6/phi', -6.0 / PHI, "2' Galois-Partner von 2")]
gA = buendel(evA)
adj = []
for g in reversed(gA):
    x = float(np.mean(evA[g]))
    name, val, rep = min(GESCHLOSSEN, key=lambda c: abs(c[1] - x))
    adj.append({'eigenwert': fl(x), 'vielfachheit': len(g), 'streuung': fl(float(np.ptp(evA[g])), 16),
                'geschlossen': name, 'geschlossen_wert': fl(val), 'abw': fl(abs(val - x), 16), 'darstellung': rep})
gL = buendel(evL)
lap = []
for m, g in enumerate(gL):
    x = float(np.mean(evL[g]))
    lap.append({'niveau': m, 'eigenwert': fl(x), 'vielfachheit': len(g), 'streuung': fl(float(np.ptp(evL[g])), 16)})


def monome(maxgrad):
    ex = [e for e in itertools.product(range(maxgrad + 1), repeat=4) if sum(e) <= maxgrad]
    ex.sort(key=lambda e: (sum(e), e))
    return ex


EXP = monome(8)
MON = np.stack([np.prod(V ** np.array(e, dtype=float), axis=1) for e in EXP], axis=1)
GRAD = np.array([sum(e) for e in EXP])
raenge, basen = [], {}
for k in range(9):
    U, s, _ = np.linalg.svd(MON[:, GRAD <= k], full_matrices=False)
    r = int((s > 1e-9 * s[0]).sum())
    raenge.append({'grad_bis': k, 'rang': r, 'neu': r - (raenge[-1]['rang'] if raenge else 0),
                   'harmonische_dimension_k_plus_1_quadrat': (k + 1) ** 2,
                   'kleinster_behaltener_sv': fl(s[r - 1], 14), 'groesster_verworfener_sv': (fl(s[r], 18) if r < len(s) else None)})
    basen[k] = U[:, :r]
EL = [vecL[:, g] for g in gL]
identitaet = []
for k in range(6):
    Ek = np.hstack(EL[:k + 1])
    Qk = basen[k]
    rest = float(np.linalg.norm(Qk - Ek @ (Ek.T @ Qk)))
    identitaet.append({'grad_bis': k, 'dim_polynome': int(Qk.shape[1]), 'dim_unterste_niveaus': int(Ek.shape[1]), 'restnorm': fl(rest, 16)})
verteilung = []
for k in range(9):
    Qk = basen[k]
    if k == 0:
        Pn = Qk
    else:
        Qp = basen[k - 1]
        Pn = Qk - Qp @ (Qp.T @ Qk)
    U, s, _ = np.linalg.svd(Pn, full_matrices=False)
    Qn = U[:, s > 1e-6]
    gew = [fl(float(np.linalg.norm(EL[m].T @ Qn) ** 2), 6) for m in range(len(EL))]
    verteilung.append({'grad': k, 'neue_dimension': int(Qn.shape[1]), 'auf_niveaus': gew})
S3 = []
lam1 = lap[1]['eigenwert']
chord2 = L0 ** 2
for k in range(6):
    lk = lap[k]['eigenwert']
    S3.append({'k': k, 'n_fock': k + 1, 'kontinuum_k_k_plus_2': k * (k + 2), 'vielfachheit_kontinuum': (k + 1) ** 2,
               'vielfachheit_graph': lap[k]['vielfachheit'], 'laplace_graph': lk,
               'verhaeltnis_graph_zu_k1': (fl(lk / lam1, 10) if k > 0 else 0.0),
               'verhaeltnis_kontinuum_zu_k1': fl(k * (k + 2) / 3.0, 10),
               'abw_prozent': (fl(100.0 * ((lk / lam1) / (k * (k + 2) / 3.0) - 1.0), 6) if k > 0 else None),
               'kontinuum_skaliert_2_l2_k_k_plus_2': fl(2.0 * chord2 * k * (k + 2), 10)})
mult_A_fallend = [r['vielfachheit'] for r in adj]
mult_L_steigend = [r['vielfachheit'] for r in lap]
z1 = {'verschiedene_eigenwerte': len(adj), 'vielfachheiten_fallend': mult_A_fallend,
      'vorhersage': [1, 4, 9, 16, 25, 36, 9, 16, 4]}
z1['erfuellt'] = bool(len(adj) == 9 and mult_A_fallend == z1['vorhersage'] and max(r['abw'] for r in adj) < 1e-9)
z2 = {'vielfachheiten_steigend': mult_L_steigend, 'erste_sechs': mult_L_steigend[:6], 'danach': mult_L_steigend[6:]}
z2['erfuellt'] = bool(mult_L_steigend[:6] == [1, 4, 9, 16, 25, 36] and len(mult_L_steigend) > 6 and mult_L_steigend[6] != 49)
z4 = {'k': [1, 2, 3], 'graph': [S3[k]['verhaeltnis_graph_zu_k1'] for k in (1, 2, 3)],
      'kontinuum': [S3[k]['verhaeltnis_kontinuum_zu_k1'] for k in (1, 2, 3)],
      'abw_prozent': [0.0, S3[2]['abw_prozent'], S3[3]['abw_prozent']]}
z4['erfuellt_10_prozent'] = bool(all(abs(a) <= 10.0 for a in z4['abw_prozent']))
spur = {'spur_A': fl(float(np.trace(Af)), 12), 'spur_A2': fl(float(np.trace(Af @ Af)), 9),
        'summe_lambda': fl(float(evA.sum()), 9), 'summe_lambda2': fl(float((evA ** 2).sum()), 9)}
mark('spektrum')

# ------------------------------------------------------------------ 7. 30er-Ring (Boerdijk-Coxeter-Helix)
tri2tet = defaultdict(list)
for t in tetraeder:
    for f in itertools.combinations(t, 3):
        tri2tet[f].append(t)


def lauf(start, schritte=64):
    seq = list(start)
    for _ in range(schritte):
        f = tuple(sorted(seq[-3:]))
        neu = [x for t in tri2tet[f] for x in t if x not in f and x != seq[-4]]
        if len(neu) != 1:
            return seq, False
        seq.append(neu[0])
    return seq, True


def periode(seq):
    for p in range(1, len(seq) // 2 + 1):
        if all(seq[i + p] == seq[i] for i in range(len(seq) - p)):
            return p
    return None


def ring_tets(seq, p):
    return frozenset(tuple(sorted(seq[(i + j) % p] for j in range(4))) for i in range(p))


t_start = next(t for t in tetraeder if E in t)
start = [E] + [x for x in t_start if x != E]
seq0, ok0 = lauf(start)
p0 = periode(seq0)
ring_seq = seq0[:p0] if p0 else seq0[:30]
ring_tet_liste = [list(sorted(ring_seq[(i + j) % len(ring_seq)] for j in range(4))) for i in range(len(ring_seq))]
alle_perioden = defaultdict(int)
alle_ringe = set()
for t in tetraeder:
    for o in itertools.permutations(t):
        s_, ok_ = lauf(o, 64)
        p_ = periode(s_) if ok_ else None
        alle_perioden[str(p_)] += 1
        if p_:
            alle_ringe.add(ring_tets(s_, p_))
ring_je_tetraeder = defaultdict(int)
for r in alle_ringe:
    for t in r:
        ring_je_tetraeder[t] += 1
R0 = ring_tets(ring_seq, len(ring_seq))


def bahn(seite):
    fam = {}
    for g in range(N):
        if seite == 'links':
            sq = [int(MUL[g, x]) for x in ring_seq]
        else:
            sq = [int(MUL[x, g]) for x in ring_seq]
        key = ring_tets(sq, len(sq))
        if key not in fam:
            fam[key] = sq
    keys = list(fam)
    alle = set().union(*keys)
    disj = sum(len(r) for r in keys) == len(alle)
    return fam, {'ringe': len(keys), 'paarweise_disjunkt': bool(disj), 'tetraeder_ueberdeckt': len(alle)}


fam_l, info_l = bahn('links')
fam_r, info_r = bahn('rechts')
zerlegung, zerlegung_seite = None, None
for seite, fam, info in (('rechts', fam_r, info_r), ('links', fam_l, info_l)):
    if info['ringe'] == 20 and info['paarweise_disjunkt'] and info['tetraeder_ueberdeckt'] == 600:
        zerlegung = [fam[k] for k in fam]
        zerlegung_seite = seite
        break
if zerlegung:
    # den Ring durch den Pol zuerst
    zerlegung.sort(key=lambda sq: (0 if R0 == ring_tets(sq, len(sq)) else 1, min(sq)))
P = len(ring_seq)
geometrie = []
for st in (1, 2, 3, 5, 6, 10, 15):
    zyklen = math.gcd(st, P)
    rz = []
    for r in range(zyklen):
        cyc = [ring_seq[(r + st * m) % P] for m in range(P // zyklen)]
        rz.append(int(np.linalg.matrix_rank(V[cyc], tol=1e-9)))
    ips = [float(V[ring_seq[i]] @ V[ring_seq[(i + st) % P]]) for i in range(P)]
    geometrie.append({'schritt': st, 'zyklen': zyklen, 'laenge': P // zyklen, 'rang_je_zyklus': rz,
                      'skalarprodukt_v_i_v_i_plus_schritt_min_max': [fl(min(ips)), fl(max(ips))],
                      'winkel_grad': fl(math.degrees(math.acos(max(-1.0, min(1.0, ips[0])))), 6)})
ring = {
    'start_geordnet': start,
    'lauf_ok': ok0,
    'periode': p0,
    'ecken_folge': ring_seq,
    'tetraeder': ring_tet_liste,
    'verschiedene_tetraeder': len(set(map(tuple, ring_tet_liste))),
    'verschiedene_ecken': len(set(ring_seq)),
    'aufeinanderfolgende_teilen_ein_dreieck': bool(all(len(set(ring_tet_liste[i]) & set(ring_tet_liste[(i + 1) % P])) == 3 for i in range(P))),
    'geometrie_schritte': geometrie,
    'alle_14400_geordneten_starts_perioden': dict(alle_perioden),
    'verschiedene_ringe_gesamt': len(alle_ringe),
    'ringe_je_tetraeder_min_max': [min(ring_je_tetraeder.values()), max(ring_je_tetraeder.values())],
    'bahn_linksmultiplikation': info_l,
    'bahn_rechtsmultiplikation': info_r,
    'zerlegung_in_20_ringe_gefunden': zerlegung is not None,
    'zerlegung_seite': zerlegung_seite,
    'zerlegung_ecken_folgen': zerlegung,
    'zerlegung_tetraeder': ([[list(sorted(sq[(i + j) % len(sq)] for j in range(4))) for i in range(len(sq))] for sq in zerlegung] if zerlegung else None),
}
mark('ring')


# ------------------------------------------------------------------ 8. Ausgabe
def code(x):
    for c, val in enumerate((0.0, 1.0 / (2.0 * PHI), 0.5, PHI / 2.0, 1.0)):
        if abs(abs(x) - val) < 1e-12:
            return c if x >= 0 else -c
    raise ValueError(x)


ecken_code = [code(x) for row in V.tolist() for x in row]
assert np.allclose(np.array([[(1 if c >= 0 else -1) * (0.0, 1.0 / (2.0 * PHI), 0.5, PHI / 2.0, 1.0)[abs(c)] for c in ecken_code[4 * i:4 * i + 4]] for i in range(N)]), V, atol=1e-15)

dump('ecken.json', {'reihenfolge': 'Quaternion a + b i + c j + d k, Spalten [a, b, c, d]', 'radius': 1.0,
                    'rezept_block': herkunft, 'koordinaten': V.tolist()})
dump('kanten.json', {'anzahl': nK, 'laenge': fl(L0, 15), 'kanten': [list(e) for e in kanten]})
dump('dreiecke.json', {'anzahl': nD, 'dreiecke': [list(f) for f in dreiecke]})
dump('tetraeder.json', {'anzahl': nT, 'tetraeder': [list(t) for t in tetraeder]})
dump('schalen.json', schalen)
dump('spektrum.json', {
    'adjazenz_fallend': adj, 'laplace_steigend': lap, 'spurprobe': spur,
    'kugelfunktionen_rang_je_grad': raenge,
    'identitaet_polynomgrad_bis_k_gleich_unterste_k_plus_1_niveaus': identitaet,
    'grad_auf_niveaus_verteilung': verteilung,
    'vergleich_S3_wasserstoff': S3,
    'z1': z1, 'z2': z2, 'z4': z4})
dump('regge.json', regge)
dump('pruefungen.json', {'gruppe_2I': gruppe, 'z0': z0})
dump('ring30.json', ring)
ansicht = {
    'quelle': 'lauf-69/ansicht.json aus code/zelle600.py (ZELLE600-1, .69)',
    'code_werte': [0.0, 1.0 / (2.0 * PHI), 0.5, PHI / 2.0, 1.0],
    'ecken_code': ecken_code,
    'kanten': [x for e in kanten for x in e],
    'pol': E,
    'schale_winkel': schale_w,
    'schalen_winkel': [{'winkel': fl(r['winkel_grad'], 4), 'anzahl': r['anzahl']} for r in schalen['nach_winkel']],
    'schale_graph': dist,
    'schalen_graph': [{'abstand': r['abstand'], 'anzahl': r['anzahl']} for r in schalen['nach_graphabstand']],
    'ring': ring_seq,
    'ringe': zerlegung,
    'laplace': [{'wert': fl(r['eigenwert'], 6), 'vielfach': r['vielfachheit']} for r in lap],
    'regge': {'delta_grad': fl(regge['fehlwinkel_analytisch_grad'], 4), 'summe_l_delta': fl(summe_l_delta, 4),
              'kontinuum': fl(kontinuum, 4), 'abw_prozent': fl(regge['abweichung_prozent_umkreis'], 3)},
}
dump('ansicht.json', ansicht, compact=True)
mark('ende')
urteile = {'Z0': z0['erfuellt'], 'Z1': z1['erfuellt'], 'Z2': z2['erfuellt'],
           'Z3': regge['z3_erfuellt_5_prozent'], 'Z4': z4['erfuellt_10_prozent'],
           'gruppe_2I': bool(gruppe['abgeschlossen'] and latein and inverse_ok and assoz)}
dump('lauf.json', {'start_utc': START_UTC, 'ende_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                   'laufzeit_s': round(time.time() - T0, 3), 'zwischenzeiten_s': ZEIT,
                   'host': socket.gethostname(), 'python': platform.python_version(), 'numpy': np.__version__,
                   'threads_env': {k: os.environ.get(k) for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')},
                   'urteile_maschinell': urteile})
print(json.dumps({'urteile': urteile, 'zahlen': [nE, nK, nD, nT], 'regge': [regge['summe_l_delta'], regge['kontinuum_6_pi2_R'], regge['abweichung_prozent_umkreis']],
                  'adj': [(r['eigenwert'], r['vielfachheit']) for r in adj], 'lap': [(r['eigenwert'], r['vielfachheit']) for r in lap],
                  'raenge': [r['rang'] for r in raenge], 'ring_periode': p0, 'ringe_gesamt': len(alle_ringe),
                  'bahn_links': info_l, 'bahn_rechts': info_r, 'laufzeit_s': round(time.time() - T0, 3)}, ensure_ascii=False))
