#!/usr/bin/env python3
# QB-BS-2D (Runde 37): Auswertung der radialen Aeste, Bindung D(q), Urteile QB0-QB4, SVG-Bilder.
# Aufruf: python code/auswertung.py <laufordner> <ausgabe.json>
import sys, os, json
import numpy as np
from scipy.interpolate import CubicHermiteSpline

LAUF = sys.argv[1]
OUT = sys.argv[2]
KAPS = {'1': 1.0, '025': 0.25}
TWO_PI = 2.0 * np.pi


def load(name):
    p = os.path.join(LAUF, name)
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def branch_ok(res, M, key='q'):
    b = res['branches'].get(str(M))
    if b is None:
        return None
    pts = [p for p in b['points'] if p.get('status') == 'ok']
    pts.sort(key=lambda p: p['q'])
    if len(pts) < 2:
        return None
    q = np.array([p['q'] for p in pts])
    E = np.array([p['E'] for p in pts])
    Om = np.array([p['Om'] for p in pts])
    return {'q': q, 'E': E, 'Om': Om, 'pts': pts, 'stop': b.get('stop'), 'spl': CubicHermiteSpline(q, E, Om)}


def dEdq_check(br):
    if br is None or len(br['q']) < 3:
        return None
    q, E, Om = br['q'], br['E'], br['Om']
    fd = (E[2:] - E[:-2]) / (q[2:] - q[:-2])
    om = Om[1:-1]
    rel = np.abs(fd - om) / np.maximum(np.abs(om), 1e-3)
    return float(rel.max())


class Ref:
    def __init__(self, H, Q0, Q1):
        self.H, self.Q = H, [b for b in (Q0, Q1) if b is not None]
        self.umax = float(H['q'][-1])
        self.EH0 = float(H['E'][0])
        self.OmHmax = float(H['Om'][-1])
        self.EHmax = float(H['E'][-1])

    def EQstar(self, qq):
        qq = np.atleast_1d(np.asarray(qq, float))
        val = qq.copy()  # freie phi-Ladung (Strahlungskanal), Grenzkosten m_phi = 1 je Ladung
        chan = np.zeros(qq.shape, int)  # 0 = frei/Vakuum, 1 = Q l=0, 2 = Q l=1
        for k, b in enumerate(self.Q):
            lo, hi = b['q'][0], b['q'][-1]
            m = (qq >= lo) & (qq <= hi)
            if m.any():
                v = b['spl'](qq[m])
                better = v < val[m]
                idx = np.nonzero(m)[0][better]
                val[idx] = v[better]
                chan[idx] = k + 1
        val[qq <= 0] = 0.0
        return val, chan

    def EH(self, u, lin=False):
        u = np.asarray(u, float)
        v = np.where(u <= self.umax, self.H['spl'](np.minimum(u, self.umax)), np.inf)
        if lin:
            v = np.where(u > self.umax, self.EHmax + self.OmHmax * (u - self.umax), v)
        return v

    def Esep(self, q, kons):
        top = min(q, self.umax)
        cand = [np.linspace(0.0, top, 4001)]
        extra = [0.0, top]
        for b in self.Q:
            for qq in (b['q'][0], b['q'][-1]):
                u = q - qq
                if 0.0 <= u <= top:
                    extra.append(u)
        cand.append(np.array(extra))
        if kons and q > self.umax:
            cand.append(np.linspace(self.umax, q, 4001))
            ex2 = [q]
            for b in self.Q:
                u = q - b['q'][0]
                if self.umax < u <= q:
                    ex2.append(u)
            cand.append(np.array(ex2))
        u = np.concatenate(cand)
        EQ, ch = self.EQstar(q - u)
        tot = self.EH(u, lin=kons) + EQ
        k = int(np.argmin(tot))
        return float(tot[k]), float(u[k]), int(ch[k])

    def EsepA(self, q):
        EQ, ch = self.EQstar(q)
        return float(self.EH0 + EQ[0]), int(ch[0])


def mix_points(res, M):
    b = res['branches'].get(str(M)) if res else None
    if b is None:
        return {}
    return {round(p['q'], 6): p for p in b['points']}


def runs_of(flags):
    best, cur, runs, start = 0, 0, [], None
    for i, f in enumerate(flags):
        if f:
            if cur == 0:
                start = i
            cur += 1
        else:
            if cur:
                runs.append((start, i - 1))
            cur = 0
    if cur:
        runs.append((start, len(flags) - 1))
    return runs


# ------------------------------------------------------------------ SVG
COL = ['#1f5fa8', '#c0392b', '#2e8b57', '#7d3c98', '#d68910', '#6e2c00', '#148f77', '#555555']


def svg_plot(path, title, xlabel, ylabel, series, hlines=(), W=760, Hh=440):
    xs = [v for s in series for v in s[1] if np.isfinite(v)]
    ys = [v for s in series for v in s[2] if np.isfinite(v)] + [h[0] for h in hlines]
    if not xs or not ys:
        return
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)
    if x1 == x0:
        x1 = x0 + 1
    if y1 == y0:
        y1 = y0 + 1
    pad = 0.05 * (y1 - y0)
    y0 -= pad
    y1 += pad
    L, R, T, B = 80, 200, 40, 60
    pw, ph = W - L - R, Hh - T - B
    X = lambda v: L + (v - x0) / (x1 - x0) * pw
    Y = lambda v: T + (1 - (v - y0) / (y1 - y0)) * ph
    o = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" font-family="sans-serif" font-size="12">' % (W, Hh),
         '<rect width="100%" height="100%" fill="white"/>',
         '<text x="%d" y="22" font-size="14">%s</text>' % (L, title),
         '<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="#333"/>' % (L, T, pw, ph)]
    for k in range(6):
        xv = x0 + k * (x1 - x0) / 5
        yv = y0 + k * (y1 - y0) / 5
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#ddd"/>' % (X(xv), T, X(xv), T + ph))
        o.append('<text x="%.1f" y="%d" text-anchor="middle">%.4g</text>' % (X(xv), T + ph + 16, xv))
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#ddd"/>' % (L, Y(yv), L + pw, Y(yv)))
        o.append('<text x="%d" y="%.1f" text-anchor="end">%.4g</text>' % (L - 6, Y(yv) + 4, yv))
    o.append('<text x="%d" y="%d" text-anchor="middle">%s</text>' % (L + pw // 2, Hh - 14, xlabel))
    o.append('<text x="18" y="%d" transform="rotate(-90 18 %d)" text-anchor="middle">%s</text>' % (T + ph // 2, T + ph // 2, ylabel))
    for (yv, lab) in hlines:
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#999" stroke-dasharray="6,4"/>' % (L, Y(yv), L + pw, Y(yv)))
        o.append('<text x="%d" y="%.1f" fill="#666">%s</text>' % (L + pw - 4, Y(yv) - 4, lab))
    for k, s in enumerate(series):
        lab, sx, sy = s[0], s[1], s[2]
        dash = s[3] if len(s) > 3 else ''
        col = COL[k % len(COL)]
        ptsxy = [(X(a), Y(b)) for a, b in zip(sx, sy) if np.isfinite(a) and np.isfinite(b)]
        if not ptsxy:
            continue
        d = ' '.join('%.1f,%.1f' % p for p in ptsxy)
        o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8" %s/>' % (
            d, col, ('stroke-dasharray="%s"' % dash) if dash else ''))
        if len(ptsxy) < 60:
            for p in ptsxy:
                o.append('<circle cx="%.1f" cy="%.1f" r="2.2" fill="%s"/>' % (p[0], p[1], col))
        yy = T + 14 + 18 * k
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" %s/>' % (
            L + pw + 10, yy - 4, L + pw + 34, yy - 4, col, ('stroke-dasharray="%s"' % dash) if dash else ''))
        o.append('<text x="%d" y="%d">%s</text>' % (L + pw + 40, yy, lab))
    o.append('</svg>')
    with open(path, 'w') as fh:
        fh.write('\n'.join(o))


# ------------------------------------------------------------------ Hauptteil
erg = {'urteile': {}, 'tabellen': {}, 'kontrollen': {}, 'fehler': []}
refQ0 = load('refQ_l0.json')
refQ1 = load('refQ_l1.json')
Ms = None
for nm in ('refH_k1.json', 'refQ_l0.json'):
    r = load(nm)
    if r:
        Ms = r['Ms']
        break
Mc, Mf = Ms[0], Ms[-1]

refs = {}
for kk in KAPS:
    rH = load('refH_k%s.json' % kk)
    for M in Ms:
        try:
            H = branch_ok(rH, M)
            Q0 = branch_ok(refQ0, M) if refQ0 else None
            Q1 = branch_ok(refQ1, M) if refQ1 else None
            refs[(kk, M)] = Ref(H, Q0, Q1)
        except Exception as ex:
            erg['fehler'].append('Referenz kappa=%s M=%s: %r' % (kk, M, ex))

# ---- S0 / QB0
s0 = {'textur': {}, 'qball': []}
ok0 = True
auswertbar0 = True
for kk in KAPS:
    rH = load('refH_k%s.json' % kk)
    try:
        pc = [p for p in rH['branches'][str(Mc)]['points'] if p['q'] == 0.0][0]
        pf = [p for p in rH['branches'][str(Mf)]['points'] if p['q'] == 0.0][0]
        rel = abs(pf['E'] - pc['E']) / abs(pf['E'])
        above = pf['E'] > TWO_PI and pf['E_sig_over_2pi'] >= 1.0
        s0['textur'][kk] = {'E_grob': pc['E'], 'E_fein': pf['E'], 'rel_aend': rel, 'E_ueber_2pi': pf['E'] / TWO_PI,
                            'E_sig_ueber_2pi': pf['E_sig_over_2pi'], 'virial_rel_fein': pf['virial_rel'],
                            'E_fad': pf['E_fad'], 'E_pot': pf['E_U'] + pf['E_mass'], 'r_ring': pf.get('r_ring'),
                            'konv': bool(pc['conv'] and pf['conv'])}
        ok0 = ok0 and rel <= 1e-6 and above and pc['conv'] and pf['conv']
    except Exception as ex:
        auswertbar0 = False
        erg['fehler'].append('S0 Textur kappa=%s: %r' % (kk, ex))
try:
    bc = {round(p['q'], 6): p for p in refQ0['branches'][str(Mc)]['points'] if p.get('status') == 'ok'}
    bf = {round(p['q'], 6): p for p in refQ0['branches'][str(Mf)]['points'] if p.get('status') == 'ok'}
    common = sorted(set(bc) & set(bf))
    for target in (0.75, 0.85, 0.95):
        qk = min(common, key=lambda k: abs(bf[k]['Om'] - target))
        rel = abs(bf[qk]['E'] - bc[qk]['E']) / abs(bf[qk]['E'])
        s0['qball'].append({'omega_ziel': target, 'q': qk, 'omega_fein': bf[qk]['Om'], 'omega_grob': bc[qk]['Om'],
                            'E_grob': bc[qk]['E'], 'E_fein': bf[qk]['E'], 'rel_aend': rel,
                            'virial_rel_fein': bf[qk]['virial_rel']})
        ok0 = ok0 and rel <= 1e-6 and (1 / np.sqrt(2) < bf[qk]['Om'] < 1)
except Exception as ex:
    auswertbar0 = False
    erg['fehler'].append('S0 Q-Ball: %r' % (ex,))
erg['tabellen']['S0'] = s0
erg['urteile']['QB0'] = {'urteil': ('eingetroffen' if ok0 else 'nicht eingetroffen') if auswertbar0 else 'nicht auswertbar',
                         'werte': s0}

# ---- Referenzaeste
reftab = {}
for kk in KAPS:
    for M in Ms:
        rf = refs.get((kk, M))
        if rf is None:
            continue
        rH = load('refH_k%s.json' % kk)
        reftab['H_kappa%s_M%d' % (kk, M)] = {
            'u_max': rf.umax, 'Om2_bei_u_max': rf.OmHmax ** 2, 'E_H0': rf.EH0, 'stop': rf.H['stop'],
            'chi_max_ast': max(p['chi_max'] for p in rf.H['pts']), 'dEdq_rel_max': dEdq_check(rf.H),
            'virial_rel_max': max(p['virial_rel'] for p in rf.H['pts']),
            'punkte': [{'u': p['q'], 'E': p['E'], 'Om2': p['Om2'], 'chi_max': p['chi_max'], 'J': p['J'],
                        'r_ring': p.get('r_ring')} for p in rf.H['pts']]}
for l, rQ in ((0, refQ0), (1, refQ1)):
    for M in Ms:
        b = branch_ok(rQ, M) if rQ else None
        if b is None:
            continue
        reftab['Q_l%d_M%d' % (l, M)] = {'q_lo': float(b['q'][0]), 'q_hi': float(b['q'][-1]), 'stop': b['stop'],
                                        'Om_bei_q_lo': float(b['Om'][0]), 'dEdq_rel_max': dEdq_check(b),
                                        'virial_rel_max': max(p['virial_rel'] for p in b['pts']),
                                        'E_minus_q_max': float(np.max(b['E'] - b['q']))}
erg['tabellen']['referenzen'] = reftab

# ---- Mischaeste und Bindung
bind = {}
verd = {}
for kk in KAPS:
    for G in (1, 0):
        rM = load('mix_k%s_G%d.json' % (kk, G))
        if rM is None:
            erg['fehler'].append('mix_k%s_G%d fehlt' % (kk, G))
            continue
        qs = [round(v, 6) for v in rM['qs']]
        rows = []
        for q in qs:
            row = {'q': q}
            for M in Ms:
                p = mix_points(rM, M).get(q)
                rf = refs.get((kk, M))
                tag = 'f' if M == Mf else 'g'
                if p is None or rf is None or not p.get('conv'):
                    row['qual_' + tag] = False
                    continue
                row['qual_' + tag] = bool(p.get('qualifiziert'))
                Em = p['E']
                EsK, uK, chK = rf.Esep(q, kons=False)
                EsC, uC, chC = rf.Esep(q, kons=True)
                EsA, chA = rf.EsepA(q)
                row['E_mix_' + tag] = Em
                row['E_sepK_' + tag] = EsK
                row['E_sepC_' + tag] = EsC
                row['E_sepA_' + tag] = EsA
                row['u_opt_' + tag] = uC
                row['kanal_' + tag] = chC
                row['D_K_' + tag] = (EsK - Em) / EsK
                row['D_C_' + tag] = (EsC - Em) / EsC
                row['D_A_' + tag] = (EsA - Em) / EsA
                row['Om2_' + tag] = p['Om2']
                row['chi_max_' + tag] = p['chi_max']
                row['J_' + tag] = p['J']
                row['q_p_anteil_' + tag] = p['q_p'] / q
                row['virial_rel_' + tag] = p['virial_rel']
                row['start_' + tag] = p.get('start')
                row['h_max_' + tag] = p.get('h_max')
                row['r_ring_' + tag] = p.get('r_ring')
                row['E_H_von_q_' + tag] = float(rf.EH(np.array([q]))[0]) if q <= rf.umax else None
            rows.append(row)

        def robust(row, key):
            if not (row.get('qual_f') and row.get('qual_g')):
                return False
            if (key + '_f') not in row or (key + '_g') not in row:
                return False
            Df, Dg = row[key + '_f'], row[key + '_g']
            return Df > 0 and abs(Df - Dg) < Df / 3.0

        for key in ('D_K', 'D_C', 'D_A'):
            flags = [robust(r, key) for r in rows]
            for r, fl in zip(rows, flags):
                r[key + '_robust_pos'] = fl
        bind['kappa%s_G%d' % (kk, G)] = rows
        # dE/dq laengs des Mischastes (feines Gitter, nur benachbarte qualifizierte Punkte)
        try:
            qq = [r['q'] for r in rows if r.get('qual_f')]
            pts = mix_points(rM, Mf)
            if len(qq) >= 3:
                E = np.array([pts[q]['E'] for q in qq])
                Om = np.array([pts[q]['Om'] for q in qq])
                qa = np.array(qq)
                fd = (E[2:] - E[:-2]) / (qa[2:] - qa[:-2])
                rel = np.abs(fd - Om[1:-1]) / np.maximum(Om[1:-1], 1e-3)
                erg['kontrollen']['dEdq_mix_kappa%s_G%d' % (kk, G)] = {'rel_max': float(rel.max()),
                                                                        'rel_median': float(np.median(rel))}
        except Exception as ex:
            erg['fehler'].append('dEdq mix %s %d: %r' % (kk, G, ex))
erg['tabellen']['bindung'] = bind


def verdict_bind(rows, key, need=3):
    if rows is None or not rows:
        return 'nicht auswertbar', []
    if not any(r.get('qual_f') for r in rows):
        return 'nicht auswertbar', []
    flags = [r[key + '_robust_pos'] for r in rows]
    runs = [(a, b) for (a, b) in runs_of(flags) if b - a + 1 >= need]
    return ('eingetroffen' if runs else 'nicht eingetroffen'), runs


for nm, kk in (('QB1', '1'), ('QB3', '025')):
    rows = bind.get('kappa%s_G1' % kk)
    u, runs = verdict_bind(rows, 'D_C')
    uK, runsK = verdict_bind(rows, 'D_K')
    w = {}
    if rows:
        w['max_D_C_fein'] = max((r.get('D_C_f', -np.inf) for r in rows if r.get('qual_f')), default=None)
        w['laeufe_q'] = [[rows[a]['q'], rows[b]['q']] for a, b in runs]
        w['laeufe_q_kartenwortlaut'] = [[rows[a]['q'], rows[b]['q']] for a, b in runsK]
        w['anzahl_robust_pos_C'] = int(sum(r['D_C_robust_pos'] for r in rows))
        w['anzahl_qualifiziert_fein'] = int(sum(bool(r.get('qual_f')) for r in rows))
    erg['urteile'][nm] = {'urteil': u, 'vermerk': 'Hauptregel D mit E_sep,kons (lineare Fortsetzung von E_H ueber u_max); '
                                                  'Kartenwortlaut (E_H abgeschnitten): %s' % uK, 'werte': w}
    if nm == 'QB1':
        rows1, runs1, u1 = rows, runs, u

# QB2
if erg['urteile']['QB1']['urteil'] == 'nicht auswertbar':
    erg['urteile']['QB2'] = {'urteil': 'nicht auswertbar', 'vermerk': 'QB1 nicht auswertbar', 'werte': {}}
elif erg['urteile']['QB1']['urteil'] == 'nicht eingetroffen':
    mn = min((r['Om2_f'] for r in rows1 if r.get('qual_f') and 'Om2_f' in r), default=None)
    erg['urteile']['QB2'] = {'urteil': 'nicht eingetroffen', 'vermerk': 'kein gebundener Ast (QB1 nicht eingetroffen); '
                             'min Om^2 auf qualifizierten Mischpunkten zur Information: %s' % mn, 'werte': {'min_Om2_qualifiziert': mn}}
else:
    hit = []
    allom = []
    for a, b in runs1:
        for r in rows1[a:b + 1]:
            allom.append((r['q'], r['Om2_f'], r['Om2_g']))
            if r['Om2_f'] < 0.5 and r['Om2_g'] < 0.5:
                hit.append(r['q'])
    erg['urteile']['QB2'] = {'urteil': 'eingetroffen' if hit else 'nicht eingetroffen',
                             'werte': {'q_mit_Om2_unter_halb': hit,
                                       'min_Om2_gebunden': min(v[1] for v in allom) if allom else None,
                                       'Om2_gebunden': allom}}

# QB4 (G = 0, beide kappa): Hauptregel D_A (Referenz u = 0), Kartenwortlaut D_K
anyA, anyK, ausw = [], [], True
for kk in KAPS:
    rows = bind.get('kappa%s_G0' % kk)
    if not rows or not any(r.get('qual_f') for r in rows):
        ausw = False
        continue
    anyA += [(kk, r['q'], r['D_A_f']) for r in rows if r['D_A_robust_pos']]
    anyK += [(kk, r['q'], r['D_K_f']) for r in rows if r['D_K_robust_pos']]
if not ausw:
    erg['urteile']['QB4'] = {'urteil': 'nicht auswertbar', 'werte': {}}
else:
    erg['urteile']['QB4'] = {'urteil': 'nicht eingetroffen' if anyA else 'eingetroffen',
                             'vermerk': 'Hauptregel D_A (Referenz E_H(0)+E_Q*(q), getrennte Ladungserhaltung bei G=0); '
                                        'Kartenwortlaut (min_u): %s' % ('nicht eingetroffen' if anyK else 'eingetroffen'),
                             'werte': {'punkte_D_A_pos': anyA[:60], 'punkte_D_K_pos': anyK[:60],
                                       'max_D_A': {kk: max((r.get('D_A_f', -np.inf) for r in bind.get('kappa%s_G0' % kk, [])
                                                            if r.get('qual_f')), default=None) for kk in KAPS},
                                       'max_D_K': {kk: max((r.get('D_K_f', -np.inf) for r in bind.get('kappa%s_G0' % kk, [])
                                                            if r.get('qual_f')), default=None) for kk in KAPS}}}

# ---- Nullprobe K4
try:
    rM = load('mix_k1_G0.json')
    nul = []
    for M in Ms:
        rf = refs[('1', M)]
        bq = {round(p['q'], 6): p for p in refQ0['branches'][str(M)]['points'] if p.get('status') == 'ok'}
        for p in rM['null'].get(str(M), []):
            q = round(p['q'], 6)
            if q in bq:
                Eref = rf.EH0 + bq[q]['E']
                nul.append({'M': M, 'q': q, 'E_null': p['E'], 'E_H0_plus_E_Q': Eref, 'D_null': (Eref - p['E']) / Eref,
                            'conv': p['conv']})
    erg['kontrollen']['K4_nullprobe'] = nul
except Exception as ex:
    erg['fehler'].append('K4: %r' % (ex,))

# ---- weitere Kontrollen
kon = erg['kontrollen']
kon['K3_J_gleich_q_G1'] = {}
for kk in KAPS:
    rows = bind.get('kappa%s_G1' % kk) or []
    devs = [abs(r['J_f'] - r['q']) / r['q'] for r in rows if 'J_f' in r]
    kon['K3_J_gleich_q_G1'][kk] = max(devs) if devs else None
kon['virial_mix_max'] = {}
for key, rows in bind.items():
    v = [r['virial_rel_f'] for r in rows if r.get('qual_f') and 'virial_rel_f' in r]
    kon['virial_mix_max'][key] = max(v) if v else None
kon['chi_max_mix'] = {}
for key, rows in bind.items():
    v = [(r['q'], r['chi_max_f']) for r in rows if 'chi_max_f' in r]
    kon['chi_max_mix'][key] = max(v, key=lambda t: t[1]) if v else None

# ---- Bilder
os.makedirs(os.path.join(LAUF, 'bilder'), exist_ok=True)
try:
    for kk in KAPS:
        rf = refs.get((kk, Mf))
        if rf is None:
            continue
        for G in (1, 0):
            rows = bind.get('kappa%s_G%d' % (kk, G)) or []
            ser = [('E_H(u)', list(rf.H['q']), list(rf.H['E']))]
            for l, b in enumerate(rf.Q):
                ser.append(('E_Q l=%d' % l, list(b['q']), list(b['E'])))
            qg = [r['q'] for r in rows]
            if G == 1:
                ser.append(('E_sep (kons)', qg, [r.get('E_sepC_f', np.nan) for r in rows], '6,3'))
                ser.append(('E_sep (Karte)', qg, [r.get('E_sepK_f', np.nan) for r in rows], '2,3'))
            else:
                ser.append(('E_sep A (u=0)', qg, [r.get('E_sepA_f', np.nan) for r in rows], '6,3'))
                ser.append(('E_sep (Karte)', qg, [r.get('E_sepK_f', np.nan) for r in rows], '2,3'))
            ser.append(('E_mix', qg, [r.get('E_mix_f', np.nan) if r.get('qual_f') else np.nan for r in rows]))
            svg_plot(os.path.join(LAUF, 'bilder', 'energie_kappa%s_G%d.svg' % (kk, G)),
                     'Energien, kappa=%s, G=%d (M=%d)' % (KAPS[kk], G, Mf), 'Ladung q (bzw. u)', 'E', ser)
            k1, k2 = ('D_C', 'D_K') if G == 1 else ('D_A', 'D_K')
            ser = [('%s fein' % k1, qg, [r.get(k1 + '_f', np.nan) if r.get('qual_f') else np.nan for r in rows]),
                   ('%s grob' % k1, qg, [r.get(k1 + '_g', np.nan) if r.get('qual_g') else np.nan for r in rows], '2,3'),
                   ('%s fein' % k2, qg, [r.get(k2 + '_f', np.nan) if r.get('qual_f') else np.nan for r in rows], '6,3')]
            svg_plot(os.path.join(LAUF, 'bilder', 'bindung_kappa%s_G%d.svg' % (kk, G)),
                     'Bindung D(q), kappa=%s, G=%d' % (KAPS[kk], G), 'q', 'D = (E_sep - E_mix)/E_sep', ser,
                     hlines=[(0.0, 'D=0')])
    ser = []
    for kk in KAPS:
        rf = refs.get((kk, Mf))
        if rf is not None:
            ser.append(('H kappa=%s' % KAPS[kk], list(rf.H['q']), [p['Om2'] for p in rf.H['pts']], '2,3'))
        for G in (1, 0):
            rows = bind.get('kappa%s_G%d' % (kk, G)) or []
            ser.append(('mix kappa=%s G=%d' % (KAPS[kk], G), [r['q'] for r in rows],
                        [r.get('Om2_f', np.nan) if r.get('qual_f') else np.nan for r in rows]))
    svg_plot(os.path.join(LAUF, 'bilder', 'omega2.svg'), 'Omega^2(q) (G=0: phi-Frequenz, Textur ruht)', 'q', 'Omega^2', ser,
             hlines=[(0.5, '1/2'), (1.0, '1')])
    ser = []
    for kk in KAPS:
        rf = refs.get((kk, Mf))
        if rf is not None:
            ser.append(('H kappa=%s' % KAPS[kk], list(rf.H['q']), [p['chi_max'] for p in rf.H['pts']], '2,3'))
        rows = bind.get('kappa%s_G1' % kk) or []
        ser.append(('mix kappa=%s G=1' % KAPS[kk], [r['q'] for r in rows],
                    [r.get('chi_max_f', np.nan) if r.get('qual_f') else np.nan for r in rows]))
    svg_plot(os.path.join(LAUF, 'bilder', 'chi_max.svg'), 'chi_max(q)', 'q', 'chi_max', ser, hlines=[(1.0, 'chi=1')])
except Exception as ex:
    erg['fehler'].append('Bilder: %r' % (ex,))


def clean(o):
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating,)):
        o = float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, float) and not np.isfinite(o):
        return None
    return o


with open(OUT + '.tmp', 'w') as fh:
    json.dump(clean(erg), fh, indent=1)
os.replace(OUT + '.tmp', OUT)
print('urteile', {k: v['urteil'] for k, v in erg['urteile'].items()})
print('fehler', erg['fehler'])
