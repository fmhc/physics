#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-0, Runde 35: Auswertung nach den eingefrorenen Urteilsregeln (PLAN.md, Abschnitt 5).

Erst hier werden die Kontinuumsformeln der Karte benutzt (Vergleich), nie in der Rechnung selbst.
Aufruf: te0_auswertung.py --lauf <ordner>   (liest explizit.json, kern-a.json, kern-b.json, pinch.json, pinch.npz)
"""
import argparse, json, os, time
import numpy as np

XI = -2.837297479   # Ewald-Konstante einfach kubisch (Literatur [L]); nur fuer die Agenten-Vorhersage A1/A2
PI4 = 4 * np.pi


def U_par_kont(v):
    v = np.asarray(v, float); r = np.linalg.norm(v); c = v[2] / r
    return 2.0 / (PI4 * r) * (7.0 / 8.0 + c * c / 8.0)


def U_senk_kont(s):
    s = np.asarray(s, float); r = np.linalg.norm(s); n = s / r
    return 2.0 / (PI4 * r) * (n[2] * n[0] / 8.0)


def norm(v):
    return float(np.linalg.norm(np.asarray(v, float)))


def fs_fit(Ls, vals):
    A = np.array([[1.0, 1.0 / L, 1.0 / L ** 3] for L in Ls])
    return np.linalg.solve(A, np.asarray(vals, float))


def ls_steigung(rs, us):
    return float(np.polyfit(np.asarray(rs, float), np.asarray(us, float), 1)[0])


RICHT_SKAL = {'100': lambda m: (m, 0, 0), '110': lambda m: (m, m, 0), '111': lambda m: (m, m, m)}


def skal_reihen(Ufun):
    """Ufun(v) -> U ungleicher Skalarladungen; liefert je Richtung (r, D=U-U(4,0,0))."""
    U4 = Ufun((4, 0, 0))
    out = {}
    for name, f in RICHT_SKAL.items():
        rows = []
        for m in range(1, 17):
            v = f(m)
            if norm(v) > 16.5:
                break
            u = Ufun(v)
            if u is None:
                continue
            rows.append((norm(v), u - U4, v))
        out[name] = rows
    return out


def t3_bewertung(reihen):
    res = {}; ok = True
    for name, rows in reihen.items():
        a = [(r, d) for r, d, v in rows if 8.0 <= r <= 12.0 + 1e-9]
        b = [(r, d) for r, d, v in rows if 12.0 - 1e-9 <= r <= 16.5]
        sa = ls_steigung(*zip(*a)); sb = ls_steigung(*zip(*b))
        ab4 = [d for r, d, v in rows if r >= 4.0 - 1e-9]
        steigt = all(y > x for x, y in zip(ab4, ab4[1:]))   # streng steigend laengs der Richtung ab r >= 4
        ratio = sb / sa
        okr = abs(ratio - 1.0) < 0.10 and steigt
        ok = ok and okr
        res[name] = {'s_8_12': sa, 's_12_16': sb, 'verhaeltnis': ratio, 'aenderung': ratio - 1.0, 'steigt': steigt,
                     'n_a': len(a), 'n_b': len(b), 'erfuellt': okr}
    return ok, res


def zaehle(C, max_frac=0.5, null_frac=0.01):
    C = np.asarray(C); n = len(C); cm = C.max()
    nmax = nnull = 0
    for i in range(n):
        a, b, c = C[i - 1], C[i], C[(i + 1) % n]
        if b >= a and b >= c and (b > a or b > c) and b >= max_frac * cm:
            nmax += 1
        if b <= a and b <= c and (b < a or b < c) and b <= null_frac * cm:
            nnull += 1
    return nmax, nnull


def eq17_xy(qh):
    qx, qy, qz = qh
    return 0.5 - 0.5 * (qx ** 2 + qy ** 2) + 0.5 * qx ** 2 * qy ** 2


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--lauf', required=True)
    ap.add_argument('--Lroh', type=int, default=64); ap.add_argument('--Lklein', type=int, default=32)
    ap.add_argument('--Lfs', default='128,192,256'); ap.add_argument('--Lchk', default='64,128,256')
    a = ap.parse_args(); LR = a.Lroh; LK = a.Lklein
    Lfs = [int(x) for x in a.Lfs.split(',')]; Lchk = [int(x) for x in a.Lchk.split(',')]
    d = a.lauf
    ex = json.load(open(os.path.join(d, 'explizit.json')))
    kl = json.load(open(os.path.join(d, 'kern-a.json')))['laeufe'] + json.load(open(os.path.join(d, 'kern-b.json')))['laeufe']
    pi = json.load(open(os.path.join(d, 'pinch.json')))
    E = {x['L']: x for x in ex['laeufe']}
    K = {x['L']: x for x in kl}
    A = {'erzeugt_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'urteile': {}, 'zusatz': {}, 'agent_vorhersagen': {},
         'kontrollen': {}}

    # ------------------------------------------------------------ Kontrollen und T0a
    gmax = 0.0; spur6 = 0.0; spur5 = 0.0; imag = 0.0; pars = 0.0; dE56 = 0.0; dF56 = 0.0
    for L, x in E.items():
        recs = [(r['typ'], r) for r in x['records']] + [('einzel_' + n, r) for n, r in x['einzel'].items()]
        for typ, r in recs:
            gmax = max(gmax, r['gauss_res']); imag = max(imag, r['imag_max'])
            pars = max(pars, abs(r['F'] - r['F_parseval']) / max(abs(r['F']), 1e-12))   # Nenner >= 1e-12 (L=16-Probe: Paar faellt zusammen, F ~ 1e-31)
            if typ == 'vek_par_6dof_spurzeile':
                spur6 = max(spur6, r['spur_res'] / r['E_max']); dE56 = max(dE56, r['max_abs_E5_minus_E6'])
                dF56 = max(dF56, abs(r['F'] - r['F5']) / r['F'])
            elif typ.startswith('vek') or typ in ('skal_ungleich_5dof', 'einzel_vz', 'einzel_vx', 'einzel_s5'):
                spur5 = max(spur5, r['spur_res'] / r['E_max'])   # spurfrei per Konstruktion (5er-Basis)
            # skal_* mit 6 Freiheitsgraden und einzel_s6: bewusst ohne Spurbedingung, nicht geprueft
    A['kontrollen'] = {'gauss_res_max': gmax, 'spur_rel_6dof_spurzeile': spur6, 'spur_rel_5dof_konstruktion': spur5,
                       'imag_max': imag, 'parseval_rel_max': pars, 'max_abs_E5_minus_E6': dE56, 'F5_vs_F6_rel_max': dF56,
                       'kern_vs_explizit_max_abs': {str(L): x['max_abs_U_minus_Ukern'] for L, x in E.items()},
                       'pinv_q0_max': {str(L): x['pinv_q0_max'] for L, x in E.items()},
                       'gram5': E[LR]['gram5'], 'gram6': E[LR]['gram6']}
    t0a = gmax <= 1e-10 and spur6 <= 1e-10 and spur5 <= 1e-10

    def tab(L, typ):
        return [r for r in E[L]['records'] if r['typ'] == typ]
    par64 = {tuple(r['v']): r['U'] for r in tab(LR, 'vek_par')}
    par32 = {tuple(r['v']): r['U'] for r in tab(LK, 'vek_par')}

    # ------------------------------------------------------------ T0b (woertlich, L = 64)
    dev = {str(v): u / U_par_kont(v) - 1.0 for v, u in par64.items() if norm(v) >= 4.0 - 1e-9}
    t0b_max = max(abs(x) for x in dev.values())
    t0b = t0b_max <= 0.03
    A['urteile']['T0'] = {'urteil': 'eingetroffen' if (t0a and t0b) else 'nicht eingetroffen',
                          'vermerk': 'woertlich: L = 64, q = 0 ausgelassen (Neutralisierungshintergrund), Punktladungen; '
                                     'Endlichkeitskorrektur siehe zusatz.Z0',
                          'werte': {'T0a_gauss_spur_ok': t0a, 'gauss_res_max': gmax, 'spur_rel_6dof': spur6,
                                    'T0b_max_rel_abw_r_ab_4': t0b_max, 'T0b_ok': t0b,
                                    'T0b_abw_beispiele': {k: dev[k] for k in ['(0, 0, 4)', '(4, 0, 0)', '(0, 0, 8)', '(8, 0, 0)',
                                                                             '(0, 0, 16)', '(16, 0, 0)'] if k in dev}}}

    # ------------------------------------------------------------ T1 (L = 64)
    t1v = {v: u for v, u in par64.items() if 2.0 - 1e-9 <= norm(v) <= 16.5}
    vmin = min(t1v, key=t1v.get)
    A['urteile']['T1'] = {'urteil': 'eingetroffen' if t1v[vmin] > 0 else 'nicht eingetroffen',
                          'vermerk': 'L = 64, %d Abstandsvektoren 2 <= r <= 16, 15 Richtungen' % len(t1v),
                          'werte': {'U_min': t1v[vmin], 'v_min': list(vmin), 'r_min': norm(vmin),
                                    'U_min_kontinuum': U_par_kont(vmin), 'anzahl': len(t1v)}}

    # ------------------------------------------------------------ T2 (L = 64)
    R64 = par64[(0, 0, 8)] / par64[(8, 0, 0)]
    A['urteile']['T2'] = {'urteil': 'eingetroffen' if abs(R64 / (8 / 7) - 1) <= 0.03 else 'nicht eingetroffen',
                          'vermerk': 'woertlich L = 64, v = (0,0,8) gegen (8,0,0), p = z; Endlichkeitskorrektur siehe zusatz.Z2',
                          'werte': {'U_theta0': par64[(0, 0, 8)], 'U_theta90': par64[(8, 0, 0)], 'verhaeltnis': R64,
                                    'soll': 8 / 7, 'rel_abw': R64 / (8 / 7) - 1}}

    # ------------------------------------------------------------ T3 (L = 64, ungleiche Skalarladungen, 6 Freiheitsgrade)
    sk64 = {tuple(r['v']): r['U'] for r in tab(LR, 'skal_ungleich')}
    ok3, r3 = t3_bewertung(skal_reihen(lambda v: sk64.get(tuple(v))))
    A['urteile']['T3'] = {'urteil': 'eingetroffen' if ok3 else 'nicht eingetroffen',
                          'vermerk': 'woertlich L = 64; Steigungen per Ausgleichsgerade auf [8,12] und [12,16] je Richtung; '
                                     'Kontinuumssteigung 1/(8 pi) = %.6f; Endlichkeitskorrektur siehe zusatz.Z3' % (1 / (8 * np.pi)),
                          'werte': r3}

    # ------------------------------------------------------------ T4 (Pinch-Punkte)
    t4 = {}; ok4 = True
    for ebene, soll in (('hk0', (4, 4)), ('0kl', (2, 2))):
        P = pi['ebenen'][ebene]; phi = np.asarray(P['phi'])
        z = {}
        for eps, C in P['profile'].items():
            z[eps] = zaehle(C)
        C1 = np.asarray(P['profile']['0.02']); C3 = np.asarray(P['profile']['0.1'])
        epsunab = float(np.abs(C1 - C3).max() / C1.max())
        qh = (np.cos(phi), np.sin(phi), 0 * phi) if ebene == 'hk0' else (0 * phi, np.cos(phi), np.sin(phi))
        d17 = float(np.abs(C1 - eq17_xy(qh)).max())
        okz = all(tuple(v) == soll for v in z.values()) and epsunab <= 0.05
        ok4 = ok4 and okz
        t4[ebene] = {'zaehlung_max_null_je_eps': {k: list(v) for k, v in z.items()}, 'soll': list(soll),
                     'eps_abhaengigkeit_rel': epsunab, 'max_abw_Gl17_eps0.02': d17, 'C_max': float(C1.max()),
                     'C_min': float(C1.min()), 'erfuellt': okz}
    A['urteile']['T4'] = {'urteil': 'eingetroffen' if ok4 else 'nicht eingetroffen',
                          'vermerk': 'objektive Zaehlung (Keulen >= 0,5 max, Nullstellen <= 0,01 max) auf Kreisen eps = 0,02/0,05/0,1; '
                                     'Bildvergleich mit Fig. 1b/c in ERGEBNIS.md',
                          'werte': t4}

    # ------------------------------------------------------------ Endlichkeitskorrektur (Zusatz, vorab festgelegt)
    pass  # Lfs, Lchk aus den Argumenten
    fs = {}; fs_chk = {}; bco = {}
    for v in par64:
        key = str(tuple(v))
        f = fs_fit(Lfs, [K[L]['zz'][key] for L in Lfs]); g = fs_fit(Lchk, [K[L]['zz'][key] for L in Lchk])
        fs[v] = f[0]; fs_chk[v] = g[0]; bco[v] = f[1]
    devfs = {v: fs[v] / U_par_kont(v) - 1 for v in fs if norm(v) >= 4 - 1e-9}
    unsich = max(abs(fs[v] - fs_chk[v]) / abs(fs[v]) for v in fs)
    z0 = max(abs(x) for x in devfs.values())
    A['zusatz']['Z0'] = {'urteil': 'eingetroffen' if (t0a and z0 <= 0.03) else 'nicht eingetroffen',
                         'vermerk': 'wie T0, aber U_FS aus L = 128, 192, 256 (U_L = a + b/L + c/L^3); Unsicherheit = Abstand zur Anpassung 64/128/256',
                         'werte': {'max_rel_abw_r_ab_4': z0, 'fs_unsicherheit_rel_max': unsich,
                                   'abw_nach_r': {str(v): devfs[v] for v in sorted(devfs, key=norm)}}}
    z1v = {v: fs[v] for v in fs if 2 - 1e-9 <= norm(v) <= 16.5}
    vm = min(z1v, key=z1v.get)
    A['zusatz']['Z1'] = {'urteil': 'eingetroffen' if z1v[vm] > 0 else 'nicht eingetroffen',
                         'werte': {'U_FS_min': z1v[vm], 'v_min': list(vm)}}
    RFS = fs[(0, 0, 8)] / fs[(8, 0, 0)]
    A['zusatz']['Z2'] = {'urteil': 'eingetroffen' if abs(RFS / (8 / 7) - 1) <= 0.03 else 'nicht eingetroffen',
                         'werte': {'verhaeltnis_FS': RFS, 'rel_abw': RFS / (8 / 7) - 1}}
    skf = {}
    for v in [tuple(x) for x in [RICHT_SKAL[n](m) for n in RICHT_SKAL for m in range(1, 17)] if norm(x) <= 16.5]:
        key = str(tuple(v))
        if key in K[Lfs[0]]['s6']:
            skf[v] = fs_fit(Lfs, [-(K[L]['s6'][key] - K[L]['s6']['(4, 0, 0)']) for L in Lfs])[0]
    ok3f, r3f = t3_bewertung(skal_reihen(lambda v: skf.get(tuple(v), None) if tuple(v) != (4, 0, 0) else 0.0))
    A['zusatz']['Z3'] = {'urteil': 'eingetroffen' if ok3f else 'nicht eingetroffen',
                         'vermerk': 'wie T3, D = U - U(4,0,0) je L endlichkeitskorrigiert (128/192/256)',
                         'werte': r3f}
    # 5- gegen 6-Freiheitsgrade (Skalar) und gleiche gegen ungleiche
    q56 = [r['U'] / sk64[tuple(r['v'])] for r in tab(LR, 'skal_ungleich_5dof')]
    gl64 = {tuple(r['v']): r['U'] for r in tab(LR, 'skal_gleich')}
    A['zusatz']['skalar_identitaeten'] = {'U5_durch_U6': [min(q56), max(q56)],
                                          'max_abs_gleich_plus_ungleich': max(abs(gl64[v] + sk64[v]) for v in sk64)}
    an64 = {tuple(r['v']): r['U'] for r in tab(LR, 'vek_anti')}
    A['zusatz']['antiparallel'] = {'max_abs_anti_plus_par': max(abs(an64[v] + par64[v]) for v in an64),
                                   'alle_negativ': all(u < 0 for u in an64.values())}
    se = []
    for r in tab(LR, 'vek_senk'):
        uc = U_senk_kont(r['s']); se.append({'s': r['s'], 'U': r['U'], 'U_kont': uc, 'abw_in_Einheiten_Upar': (r['U'] - uc) / U_par_kont([0, 0, norm(r['s'])])})
    A['zusatz']['senkrecht'] = {'max_abs_abw_rel_zu_Upar': max(abs(x['abw_in_Einheiten_Upar']) for x in se), 'liste': se}

    # ------------------------------------------------------------ Agenten-Vorhersagen A1 bis A4 (vorab im PLAN)
    off_soll = 2 / PI4 * (11 / 12) * XI / LR
    off = {v: par64[v] - fs[v] for v in par64 if 4 - 1e-9 <= norm(v) <= 16.5}
    A['agent_vorhersagen']['A1'] = {'urteil': 'eingetroffen' if all(1.15 * off_soll <= o <= 0.85 * off_soll for o in off.values()) else 'nicht eingetroffen',
                                    'werte': {'soll': off_soll, 'min': min(off.values()), 'max': max(off.values())}}
    b_soll = 2 / PI4 * (11 / 12) * XI
    bs = [bco[v] for v in bco if norm(v) >= 4 - 1e-9]
    A['agent_vorhersagen']['A2'] = {'urteil': 'eingetroffen' if all(abs(b / b_soll - 1) <= 0.10 for b in bs) else 'nicht eingetroffen',
                                    'werte': {'soll': b_soll, 'min': min(bs), 'max': max(bs)}}
    ra = r3['100']['verhaeltnis']
    A['agent_vorhersagen']['A3'] = {'urteil': 'eingetroffen' if 0.75 <= ra <= 0.92 else 'nicht eingetroffen',
                                    'werte': {'verhaeltnis_100_L64': ra, 'schaetzung': 0.84}}
    A['agent_vorhersagen']['A4'] = {'urteil': 'eingetroffen' if par32[(16, 0, 0)] < 0 else 'nicht eingetroffen',
                                    'werte': {'U_L32_(16,0,0)': par32[(16, 0, 0)], 'U_L32_min': min(par32.values()),
                                              'negativ_bei_L32': [list(v) for v, u in par32.items() if u < 0]}}

    with open(os.path.join(d, 'auswertung.json.tmp'), 'w') as f:
        json.dump(A, f, indent=1, ensure_ascii=False, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(os.path.join(d, 'auswertung.json.tmp'), os.path.join(d, 'auswertung.json'))

    # ------------------------------------------------------------ Bilder
    try:
        import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    except Exception as exc:
        print('keine Bilder:', exc); return
    th = np.linspace(0, 90, 200)
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    ax.plot(th, 7 / 8 + np.cos(np.radians(th)) ** 2 / 8, 'k-', lw=1.5, label='Kontinuum (Karte): 7/8 + cos²θ/8')
    for vals, mk, lab in ((par64, 'o', 'Gitter L = 64, roh'), (fs, 's', 'Gitter, endlichkeitskorrigiert')):
        vs = [v for v in vals if norm(v) >= 4 - 1e-9]
        thv = [np.degrees(np.arccos(v[2] / norm(v))) for v in vs]
        y = [vals[v] * PI4 * norm(v) / 2 for v in vs]
        sc = ax.scatter(thv, y, c=[norm(v) for v in vs], cmap='viridis', marker=mk, s=22, label=lab, vmin=4, vmax=16)
    plt.colorbar(sc, ax=ax, label='Abstand r')
    ax.set_xlabel('Winkel θ zwischen p und r (Grad)'); ax.set_ylabel('U · 4π r / (2 K p²)')
    ax.set_title('Parallele Vektorladungen: Formfaktor, r ≥ 4'); ax.legend(fontsize=8); ax.grid(alpha=.3)
    fig.tight_layout(); fig.savefig(os.path.join(d, 'bild-U-theta.png'), dpi=130); plt.close(fig)

    fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
    for ax, (name, f) in zip(axs, (('θ = 0 (r längs p)', lambda m: (0, 0, m)), ('θ = 90° (r quer zu p)', lambda m: (m, 0, 0)))):
        ms = np.arange(2, 17)
        ax.plot(ms, [U_par_kont(f(m)) for m in ms], 'k-', label='Kontinuum (Karte)')
        ax.plot(ms, [par32[f(m)] for m in ms], 'v--', label='L = 32 roh')
        ax.plot(ms, [par64[f(m)] for m in ms], 'o--', label='L = 64 roh')
        ax.plot(ms, [fs[f(m)] for m in ms], 's-', ms=4, label='endlichkeitskorrigiert')
        ax.axhline(0, color='grey', lw=.8); ax.set_title(name); ax.set_xlabel('r'); ax.grid(alpha=.3)
    axs[0].set_ylabel('U (K = p = 1)'); axs[0].legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(d, 'bild-U-r.png'), dpi=130); plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.4))
    rr = np.linspace(1, 16.5, 100)
    ax.plot(rr, (rr - 4) / (8 * np.pi), 'k-', label='Kontinuum: (r - 4)/(8π)')
    raw = skal_reihen(lambda v: sk64.get(tuple(v))); kor = skal_reihen(lambda v: skf.get(tuple(v), None) if tuple(v) != (4, 0, 0) else 0.0)
    for n, mk in (('100', 'o'), ('110', '^'), ('111', 'd')):
        ax.plot([x[0] for x in raw[n]], [x[1] for x in raw[n]], mk + '--', ms=4, label='L = 64 roh [%s]' % n)
        ax.plot([x[0] for x in kor[n]], [x[1] for x in kor[n]], mk + '-', ms=4, label='korrigiert [%s]' % n)
    ax.set_xlabel('r'); ax.set_ylabel('U(r) - U(4)'); ax.set_title('Ungleiche Skalarladungen (6 Freiheitsgrade)')
    ax.legend(fontsize=7, ncol=2); ax.grid(alpha=.3)
    fig.tight_layout(); fig.savefig(os.path.join(d, 'bild-skalar.png'), dpi=130); plt.close(fig)

    z = np.load(os.path.join(d, 'pinch.npz'))
    fig, axs = plt.subplots(2, 2, figsize=(9, 8.2))
    for j, (key, ebene, lab) in enumerate((('hk0', 'hk0', ('h', 'k')), ('okl', '0kl', ('k', 'l')))):
        ax = axs[0, j]
        im = ax.imshow(z[key].T / z[key].max(), origin='lower', extent=[-1, 1, -1, 1], cmap='inferno', vmin=0, vmax=1)
        ax.set_title('<E_xy E_xy> in [%s] (normiert)' % ebene); ax.set_xlabel('q_%s / 2π' % lab[0]); ax.set_ylabel('q_%s / 2π' % lab[1])
        plt.colorbar(im, ax=ax, fraction=.046)
        ax = axs[1, j]
        P = pi['ebenen'][ebene]; phi = np.asarray(P['phi'])
        for eps in ('0.02', '0.1'):
            ax.plot(np.degrees(phi), P['profile'][eps], label='Gitter, eps = %s' % eps)
        qh = (np.cos(phi), np.sin(phi), 0 * phi) if ebene == 'hk0' else (0 * phi, np.cos(phi), np.sin(phi))
        ax.plot(np.degrees(phi), eq17_xy(qh), 'k:', label='Gl. 17 (Yan u. a.)')
        ax.set_xlabel('Winkel in der Ebene (Grad, ab %s-Achse)' % lab[0]); ax.set_ylabel('<E_xy E_xy>'); ax.legend(fontsize=7); ax.grid(alpha=.3)
    fig.tight_layout(); fig.savefig(os.path.join(d, 'bild-pinch.png'), dpi=130); plt.close(fig)
    print('auswertung fertig')


if __name__ == '__main__':
    main()
