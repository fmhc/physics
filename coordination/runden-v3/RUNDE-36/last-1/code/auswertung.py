#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LAST-1 (Runde 36): mechanische Auswertung nach PLAN.md Abschnitt 5, Kontrollen nach Abschnitt 6, Bilder.

Aufruf (nur ueber kleintest.sh auf der .69):
  auswertung.py <lauf128.json> <lauf3264.json> <kontrolle.json> <kontinuum.json> <ausgabeordner>
Die .npz-Dateien liegen jeweils neben den .json-Dateien.
"""
import sys, os, json, math, hashlib
import numpy as np

S2 = math.sqrt(2.0)
NETZE = ('aniso', 'iso')
QUELLEN = ('a', 'b', 'c')
BENANNT = {'[100]': (1, 0, 0), '[110]': (1, 1, 0), '[111]': (1, 1, 1)}
EPS = 1e-9


def richtungen():
    out = []
    for h in range(-3, 4):
        for k in range(-3, 4):
            for l in range(-3, 4):
                if (h, k, l) == (0, 0, 0):
                    continue
                if math.gcd(math.gcd(abs(h), abs(k)), abs(l)) != 1:
                    continue
                if not ((l > 0) or (l == 0 and k > 0) or (l == 0 and k == 0 and h > 0)):
                    continue
                t = 1 if (h + k + l) % 2 == 0 else 2
                step = np.array([h, k, l]) * t
                sl = float(np.linalg.norm(step) / S2)
                if sl > 16.0 / 3.0 + EPS:
                    continue
                out.append(((h, k, l), step, sl))
    return out


def punkte(step, lut):
    idx, rs = [], []
    t = 1
    while True:
        v = step * t
        r = float(np.linalg.norm(v) / S2)
        if r > 16.0 + EPS:
            break
        if r >= 2.0 - EPS:
            idx.append(lut[tuple(int(x) for x in v)]); rs.append(r)
        t += 1
    return np.array(idx, int), np.array(rs)


def exponent(r, v, lo=4.0, hi=16.0):
    m = (r >= lo - EPS) & (r <= hi + EPS)
    if m.sum() < 2:
        return None, int(m.sum())
    x = np.log(r[m]); y = np.log(np.maximum(np.abs(v[m]), 1e-300))
    A = np.vstack([x, np.ones_like(x)]).T
    sl = np.linalg.lstsq(A, y, rcond=None)[0][0]
    return float(-sl), int(m.sum())


def huellkurve(r, v):
    o = np.argsort(r)
    a = np.abs(v[o])
    E = np.maximum.accumulate(a[::-1])[::-1]
    return r[o], E


def schalen(r, v, ks=range(2, 17)):
    out = {}
    for k in ks:
        m = (r >= k - 0.5) & (r < k + 0.5)
        out[k] = float(np.sqrt(np.mean(v[m] ** 2))) if m.any() else None
    return out


def p_schale(sch, lo=4, hi=16):
    ks = np.array([k for k in range(lo, hi + 1) if sch.get(k)])
    vs = np.array([sch[k] for k in ks])
    return exponent(ks.astype(float), vs, lo, hi)[0]


class Daten:
    def __init__(self, jpfad):
        self.j = json.load(open(jpfad))
        self.z = np.load(jpfad.replace('.json', '.npz'))

    def hat(self, netz, L):
        return ('%s_L%d_n' % (netz, L)) in self.z.files

    def get(self, netz, L, k):
        return self.z['%s_L%d_%s' % (netz, L, k)]


def main():
    p128, p3264, pkontr, pkont, aus = sys.argv[1:6]
    os.makedirs(aus, exist_ok=True)
    quellen_daten = {}
    for p in (p128, p3264):
        if os.path.exists(p):
            quellen_daten[p] = Daten(p)
    kontr = json.load(open(pkontr)) if os.path.exists(pkontr) else None
    kont = Daten(pkont) if os.path.exists(pkont) else None

    def finde(netz, L):
        for d in quellen_daten.values():
            if d.hat(netz, L):
                return d
        return None

    groessen = [L for L in (32, 64, 128) if all(finde(n, L) for n in NETZE)]
    Lh = 128 if 128 in groessen else (64 if 64 in groessen else None)
    E = dict(hauptgroesse=Lh, groessen=groessen, urteile={}, kontrollen={}, tabellen={})
    if Lh is None:
        for k in ('L0', 'L1', 'L2', 'L3', 'L4'):
            E['urteile'][k] = dict(urteil='nicht auswertbar', vermerk='kein Hauptlauf', werte={})
        json.dump(E, open(os.path.join(aus, 'auswertung.json'), 'w'), indent=1)
        return

    # ---------------------------------------------------------------- Konstanten (L0, K7, K8)
    d0 = finde('aniso', Lh)
    C = {n: finde(n, Lh).j['netze'][n]['C'] for n in NETZE}
    C2 = {n: finde(n, Lh).j['netze'][n]['C_eps2'] for n in NETZE}
    ca = C['aniso']; ci = C['iso']
    l0a1 = abs(ca['C11'] / (2 * ca['C44']) - 1); l0a2 = abs(ca['C12'] / ca['C44'] - 1)
    zener_iso = 2 * ci['C44'] / (ci['C11'] - ci['C12'])
    zener_aniso = 2 * ca['C44'] / (ca['C11'] - ca['C12'])
    l0 = (l0a1 <= 1e-6) and (l0a2 <= 1e-6) and (abs(zener_iso - 1) <= 0.01)
    k8 = {}
    for n, kt in (('aniso', 0.0), ('iso', 1 / 18)):
        soll = dict(C11=S2 * (1 + 14 * kt), C12=S2 * (0.5 - 7 * kt), C44=S2 * (0.5 + 6 * kt))
        k8[n] = {k: abs(C[n][k] - soll[k]) / abs(soll[k]) for k in soll}
    E['kontrollen']['K7_C_eps1_gegen_eps2_max_rel'] = max(abs(C[n][k] - C2[n][k]) / abs(C[n][k]) for n in NETZE for k in C[n])
    E['kontrollen']['K8_C_gegen_geschlossene_Form_max_rel'] = max(v for n in k8 for v in k8[n].values())
    mu = ci['C44']; lam = ci['C12']; nu = lam / (2 * (lam + mu))
    E['urteile']['L0'] = dict(urteil='eingetroffen' if l0 else 'nicht eingetroffen', vermerk='vorab ableitbar [M]; prueft den Code',
                              werte=dict(C=C, aniso_C11_durch_2C44_minus_1=l0a1, aniso_C12_durch_C44_minus_1=l0a2,
                                         zener_iso=zener_iso, zener_aniso=zener_aniso, mu_iso=mu, lambda_iso=lam, nu_iso=nu))

    # ---------------------------------------------------------------- Codekontrollen K1-K3
    ok_code = True
    if kontr is not None:
        res_max = 0.0; abw_max = 0.0; fmax = 1.0
        for n, v in kontr['netze'].items():
            for qn, q in v['quellen'].items():
                res_max = max(res_max, q['residuum_einzeln'] / q['f_max'], *[p['residuum_max'] / q['f_max'] for p in q['paare']])
                abw_max = max(abw_max, *[p['abw_rel'] for p in q['paare']])
        E['kontrollen']['K1_residuum_rel_max'] = res_max
        E['kontrollen']['K2_paar_explizit_gegen_korrelation_rel_max'] = abw_max
        E['kontrollen']['K2_tabelle'] = {n: {qn: [dict(R=p['R'], r=p['r'], explizit=p['Pi12_explizit'], korrelation=p['Pi12_korrelation'])
                                                  for p in q['paare']] for qn, q in v['quellen'].items()} for n, v in kontr['netze'].items()}
        ok_code &= (res_max <= 1e-9) and (abw_max <= 1e-9)
    else:
        E['kontrollen']['K1_K2'] = 'fehlt'
        ok_code = False
    ung = 0.0; nullp = set()
    for L in groessen:
        for n in NETZE:
            o = finde(n, L).j['netze'][n]['groessen'][str(L)]
            ung = max(ung, *[o['ungerade_rel_' + q] for q in QUELLEN])
            nullp.add(o['nullpunkte_q'])
    E['kontrollen']['K3_ungerade_rel_max'] = ung
    E['kontrollen']['K3_nullpunkte_je_gitter'] = sorted(nullp)
    ok_code &= (ung <= 1e-12) and (nullp == {2})
    E['kontrollen']['code_ok'] = bool(ok_code)

    # ---------------------------------------------------------------- Daten der Hauptgroesse
    def lade(L):
        X = {}
        for n in NETZE:
            d = finde(n, L)
            X[n] = {k: d.get(n, L, k) for k in ('n', 'r', 'Pi_torus_a', 'Pi_torus_b', 'Pi_torus_c', 'dPi_a', 'dPi_b', 'dPi_c',
                                                 'Pi_korr_a', 'Pi_korr_b', 'Pi_korr_c', 'u_n_a', 'u_r_a', 'u_a', 'u_korr_a',
                                                 'u_n_b', 'u_r_b', 'u_b', 'u_n_c', 'u_r_c', 'u_c')}
        return X

    alle = {L: lade(L) for L in groessen}
    H = alle[Lh]
    nvec = H['aniso']['n']; rr = H['aniso']['r']
    lut = {tuple(int(x) for x in v): i for i, v in enumerate(nvec)}
    dirs = richtungen()
    dpts = {hkl: punkte(step, lut) for hkl, step, sl in dirs}
    E['tabellen']['richtungen'] = [dict(hkl=list(hkl), schritt=sl, punkte=int(len(dpts[hkl][0]))) for hkl, step, sl in dirs]
    if kont is not None:
        assert np.array_equal(kont.z['n'], nvec)

    def urteile_fuer(X, nm=''):
        U = {}
        # L1
        W1 = {}
        ok1 = True; ok2 = True
        for n in NETZE:
            P = X[n]['Pi_korr_a']; r = X[n]['r']
            m = (r >= 3 - EPS) & (r <= 16 + EPS)
            W1['groesster_wert_3_16_' + n] = float(P[m].max())
            W1['anzahl_nicht_negativ_3_16_' + n] = int((P[m] >= 0).sum())
            W1['anzahl_vektoren_3_16'] = int(m.sum())
            ok1 &= bool((P[m] < 0).all())
            ps = []
            for hkl, (ix, rs) in dpts.items():
                p, k = exponent(rs, P[ix])
                ps.append(p)
            ps = np.array(ps)
            W1['p_min_' + n] = float(ps.min()); W1['p_max_' + n] = float(ps.max())
            W1['p_benannt_' + n] = {nm_: exponent(dpts[h][1], P[dpts[h][0]])[0] for nm_, h in BENANNT.items()}
            sch = schalen(r, P)
            W1['p_schale_' + n] = p_schale(sch)
            ok2 &= bool(((ps >= 0.9) & (ps <= 1.1)).all()) and (0.9 <= W1['p_schale_' + n] <= 1.1)
        ok3 = None
        if kont is not None:
            K = kont.z['iso_Pi_kelvin_a']
            P = X['iso']['Pi_korr_a']; r = X['iso']['r']
            m = (r >= 6 - EPS) & (r <= 16 + EPS)
            q = P[m] / K[m] - 1
            W1['kelvin_max_abw'] = float(np.abs(q).max()); W1['kelvin_abw_min'] = float(q.min()); W1['kelvin_abw_max'] = float(q.max())
            ok3 = bool(np.abs(q).max() <= 0.05)
        if ok3 is None:
            U['L1'] = dict(urteil='nicht auswertbar', vermerk='Kelvin-Vergleich fehlt', werte=W1)
        else:
            U['L1'] = dict(urteil='eingetroffen' if (ok1 and ok2 and ok3) else 'nicht eingetroffen',
                           werte=dict(W1, teil_i_vorzeichen=ok1, teil_ii_exponent=ok2, teil_iii_kelvin=ok3))
        # L2
        W2 = {}
        okr = True
        Pa = X['aniso']['Pi_korr_b']; Pi = X['iso']['Pi_korr_b']; r = X['iso']['r']
        for nm_, h in BENANNT.items():
            ix, rs = dpts[h]
            j = int(np.argmin(np.abs(rs - 8.0) + 1e-12 * rs))
            ratio = abs(Pi[ix[j]]) / abs(Pa[ix[j]])
            W2['verhaeltnis_r8_' + nm_] = dict(r=float(rs[j]), iso=float(Pi[ix[j]]), aniso=float(Pa[ix[j]]), verhaeltnis=float(ratio))
            okr &= ratio <= 0.05
        si = schalen(r, Pi); sa = schalen(r, Pa)
        W2['verhaeltnis_schale_8'] = si[8] / sa[8]
        okr &= W2['verhaeltnis_schale_8'] <= 0.05
        allr = []
        for hkl, (ix, rs) in dpts.items():
            j = int(np.argmin(np.abs(rs - 8.0) + 1e-12 * rs))
            allr.append(abs(Pi[ix[j]]) / abs(Pa[ix[j]]))
        W2['verhaeltnis_r8_alle_richtungen_max'] = float(max(allr)); W2['verhaeltnis_r8_alle_richtungen_median'] = float(np.median(allr))
        W2['anteil_richtungen_verhaeltnis_le_005'] = float(np.mean(np.array(allr) <= 0.05))
        W2['p_schale_iso'] = p_schale(si)
        okf = W2['p_schale_iso'] >= 2.6
        for nm_, h in BENANNT.items():
            ix, rs = dpts[h]
            rr_, Ev = huellkurve(rs, Pi[ix])
            W2['p_env_' + nm_] = exponent(rr_, Ev)[0]
            W2['p_' + nm_] = exponent(rs, Pi[ix])[0]
            W2['vorzeichenwechsel_4_16_' + nm_] = bool(len(set(np.sign(Pi[ix][(rs >= 4 - EPS)]))) > 1)
            okf &= W2['p_env_' + nm_] >= 2.6
        U['L2'] = dict(urteil='eingetroffen' if (okr and okf) else 'nicht eingetroffen',
                       werte=dict(W2, teil_i_verhaeltnis=bool(okr), teil_ii_abfall=bool(okf)))
        # L3
        W3 = {}
        r = X['aniso']['r']
        ok_e = True
        for nm_, h in BENANNT.items():
            ix, rs = dpts[h]
            W3['p_' + nm_] = exponent(rs, Pa[ix])[0]
            ok_e &= 2.6 <= W3['p_' + nm_] <= 3.4
        W3['p_schale_aniso'] = p_schale(sa)
        ok_e &= 2.6 <= W3['p_schale_aniso'] <= 3.4
        ps = [exponent(rs, Pa[ix])[0] for hkl, (ix, rs) in dpts.items()]
        W3['p_alle_richtungen_min_max'] = [float(min(ps)), float(max(ps))]
        W3['anteil_richtungen_p_in_26_34'] = float(np.mean([(2.6 <= p <= 3.4) for p in ps]))
        sg = {}
        for nm_ in ('[100]', '[111]'):
            ix, rs = dpts[BENANNT[nm_]]
            m = (rs >= 4 - EPS) & (rs <= 16 + EPS)
            sg[nm_] = sorted(set(int(s) for s in np.sign(Pa[ix][m])))
        W3['vorzeichen'] = sg
        ok_s = (len(sg['[100]']) == 1) and (len(sg['[111]']) == 1) and (sg['[100]'][0] == -sg['[111]'][0]) and sg['[100]'][0] != 0
        ix, rs = dpts[BENANNT['[110]']]
        W3['vorzeichen_[110]'] = sorted(set(int(s) for s in np.sign(Pa[ix][(rs >= 4 - EPS)])))
        U['L3'] = dict(urteil='eingetroffen' if (ok_e and ok_s) else 'nicht eingetroffen',
                       werte=dict(W3, teil_i_exponent=bool(ok_e), teil_ii_vorzeichen=bool(ok_s)))
        # L4
        W4 = {}
        ok4 = True
        for n in NETZE:
            for qn in ('b', 'c'):
                u = np.linalg.norm(X[n]['u_' + qn], axis=1); ru = X[n]['u_r_' + qn]
                sch = schalen(ru, u)
                W4['p_u_%s_%s' % (qn, n)] = p_schale(sch)
                ok4 &= 1.7 <= W4['p_u_%s_%s' % (qn, n)] <= 2.3
            ua = np.linalg.norm(X[n]['u_korr_a'], axis=1); ub = np.linalg.norm(X[n]['u_a'], axis=1)
            W4['kontrast_p_u_a_korr_' + n] = p_schale(schalen(X[n]['u_r_a'], ua))
            W4['kontrast_p_u_a_torus_' + n] = p_schale(schalen(X[n]['u_r_a'], ub))
        U['L4'] = dict(urteil='eingetroffen' if ok4 else 'nicht eingetroffen', werte=W4)
        return U

    U = urteile_fuer(H)
    for k, v in U.items():
        if not ok_code:
            v['vermerk'] = 'Codekontrolle verfehlt'; v['urteil'] = 'nicht auswertbar'
        E['urteile'][k] = v
    # Groessenprobe: Urteile mit L = 64
    if 64 in groessen and Lh != 64:
        U64 = urteile_fuer(alle[64])
        E['kontrollen']['K4_urteile_L64'] = {k: v['urteil'] for k, v in U64.items()}
        E['kontrollen']['K4_werte_L64'] = {k: v['werte'] for k, v in U64.items()}
    # Groessenreihe der korrigierten und unkorrigierten Werte
    k4 = {}
    for n in NETZE:
        for qn in QUELLEN:
            ref = H[n]['Pi_korr_' + qn]; r = H[n]['r']
            m = (r >= 3 - EPS) & (r <= 16 + EPS)
            skala = float(np.abs(ref[m]).max())
            for L in groessen:
                if L == Lh:
                    continue
                X = alle[L][n]
                for art in ('korr', 'torus'):
                    dlt = np.abs(X['Pi_%s_%s' % (art, qn)][m] - ref[m])
                    k4['%s_%s_L%d_%s' % (n, qn, L, art)] = dict(max_abw_rel_zur_skala=float(dlt.max() / skala),
                                                                  max_abw_rel_lokal=float((dlt / np.abs(ref[m])).max()))
            k4['%s_%s_skala_max_abs_3_16' % (n, qn)] = skala
    E['kontrollen']['K4_groessenreihe_gegen_L%d' % Lh] = k4
    # Torus ohne Korrektur: Vorzeichen der Punktlast-Wechselwirkung
    tor = {}
    for L in groessen:
        for n in NETZE:
            P = alle[L][n]['Pi_torus_a']; r = alle[L][n]['r']
            m = (r >= 3 - EPS) & (r <= 16 + EPS)
            tor['%s_L%d_anzahl_nicht_negativ_3_16' % (n, L)] = int((P[m] >= 0).sum())
            Pb = alle[L][n]['Pi_torus_b']
            ix, rs = dpts[(1, 1, 0)]
            tor['%s_L%d_b_torus_110_r8' % (n, L)] = float(Pb[ix[np.argmin(np.abs(rs - 8))]])
            tor['%s_L%d_b_dPi_110_r8' % (n, L)] = float(alle[L][n]['dPi_b'][ix[np.argmin(np.abs(rs - 8))]])
            tor['%s_L%d_a_dPi_110_r8_rel' % (n, L)] = float(alle[L][n]['dPi_a'][ix[np.argmin(np.abs(rs - 8))]] /
                                                            alle[L][n]['Pi_korr_a'][ix[np.argmin(np.abs(rs - 8))]])
    E['kontrollen']['torus_unkorrigiert'] = tor
    # Kontinuum K5
    if kont is not None:
        K = kont.z
        r = H['iso']['r']
        E['kontrollen']['K5_synge_gegen_kelvin_iso_max_rel'] = float(np.abs(K['iso_Pi_kont_a'] / K['iso_Pi_kelvin_a'] - 1).max())
        E['kontrollen']['K5_iso_dilatation_kontinuum_max_abs'] = float(np.abs(K['iso_Pi_kont_b']).max())
        E['kontrollen']['K6_dipol_schritt'] = kont.j.get('dipol_schrittprobe_max_rel')
        E['kontrollen']['K6_dipol_nphi'] = kont.j.get('dipol_nphi_probe_max_rel')
        gk = {}
        for n in NETZE:
            for qn in QUELLEN:
                P = H[n]['Pi_korr_' + qn]; Kk = K['%s_Pi_kont_%s' % (n, qn)]
                for lo, hi in ((6, 10), (12, 16)):
                    m = (r >= lo - EPS) & (r <= hi + EPS)
                    if n == 'iso' and qn == 'b':
                        gk['%s_%s_%d_%d_max_abs_gitter' % (n, qn, lo, hi)] = float(np.abs(P[m]).max())
                        gk['%s_%s_%d_%d_max_abs_gitter_r3' % (n, qn, lo, hi)] = float(np.abs(P[m] * r[m] ** 3).max())
                    else:
                        gk['%s_%s_%d_%d_max_abw_rel' % (n, qn, lo, hi)] = float(np.abs(P[m] / Kk[m] - 1).max())
                        gk['%s_%s_%d_%d_median_abw_rel' % (n, qn, lo, hi)] = float(np.median(np.abs(P[m] / Kk[m] - 1)))
        E['kontrollen']['K5_gitter_gegen_kontinuum'] = gk

    # ---------------------------------------------------------------- Tabellen
    tab = {}
    for n in NETZE:
        for qn in QUELLEN:
            P = H[n]['Pi_korr_' + qn]; T = H[n]['Pi_torus_' + qn]
            rows = []
            for nm_, h in BENANNT.items():
                ix, rs = dpts[h]
                for rz in (2, 4, 8, 16):
                    j = int(np.argmin(np.abs(rs - rz) + 1e-12 * rs))
                    row = dict(richtung=nm_, r=float(rs[j]), Pi_korr=float(P[ix[j]]), Pi_torus=float(T[ix[j]]))
                    if kont is not None:
                        row['Pi_kont'] = float(kont.z['%s_Pi_kont_%s' % (n, qn)][ix[j]])
                        if qn == 'a':
                            row['Pi_kelvin'] = float(kont.z['%s_Pi_kelvin_a' % n][ix[j]])
                    rows.append(row)
            tab['%s_%s' % (n, qn)] = dict(zeilen=rows, p_schale=p_schale(schalen(H[n]['r'], P)),
                                          p_benannt={nm_: exponent(dpts[h][1], P[dpts[h][0]])[0] for nm_, h in BENANNT.items()},
                                          p_benannt_6_16={nm_: exponent(dpts[h][1], P[dpts[h][0]], 6)[0] for nm_, h in BENANNT.items()},
                                          p_benannt_8_16={nm_: exponent(dpts[h][1], P[dpts[h][0]], 8)[0] for nm_, h in BENANNT.items()},
                                          schalen_rms=schalen(H[n]['r'], P))
            # Richtungstabelle bei r nahe 8
            rt = []
            pp = 1.0 if qn == 'a' else 3.0
            for hkl, (ix, rs) in dpts.items():
                j = int(np.argmin(np.abs(rs - 8.0) + 1e-12 * rs))
                rt.append(dict(hkl=list(hkl), r=float(rs[j]), Pi=float(P[ix[j]]), r_hoch_p_Pi=float(P[ix[j]] * rs[j] ** pp),
                               p=exponent(rs, P[ix])[0]))
            tab['%s_%s' % (n, qn)]['richtungen_r8'] = rt
    E['tabellen']['werte'] = tab
    with open(os.path.join(aus, 'auswertung.json'), 'w') as f:
        json.dump(E, f, indent=1, default=lambda x: x.tolist() if isinstance(x, np.ndarray) else (bool(x) if isinstance(x, np.bool_) else float(x)))

    # ---------------------------------------------------------------- Bilder
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    farben = {'[100]': '#1f77b4', '[110]': '#d62728', '[111]': '#2ca02c'}
    namen = {'a': 'Punktlasten (a)', 'b': 'Dilatationszentren (b)', 'c': 'zu lange Staebe (c)'}
    for qn in QUELLEN:
        fig, axs = plt.subplots(1, 2, figsize=(11, 4.6), sharey=True)
        for ax, n in zip(axs, NETZE):
            P = H[n]['Pi_korr_' + qn]; r = H[n]['r']
            for nm_, h in BENANNT.items():
                ix, rs = dpts[h]
                v = P[ix]
                ax.loglog(rs[v < 0], -v[v < 0], 'o', color=farben[nm_], label=nm_ + ' (Pi<0)')
                ax.loglog(rs[v > 0], v[v > 0], 'o', mfc='none', color=farben[nm_], label=nm_ + ' (Pi>0)')
                if kont is not None and not (n == 'iso' and qn == 'b'):
                    Kk = kont.z['%s_Pi_kont_%s' % (n, qn)][ix]
                    ax.loglog(rs, np.abs(Kk), '-', color=farben[nm_], lw=0.8, alpha=0.7)
            sch = schalen(r, P)
            ks = [k for k in sch if sch[k]]
            ax.loglog(ks, [sch[k] for k in ks], 'k--', lw=1.2, label='Schalen-RMS')
            ax.set_title('%s, %s (k_theta = %s), L = %d' % (namen[qn], n, '0' if n == 'aniso' else '1/18', Lh))
            ax.set_xlabel('r (Stablaengen)')
            ax.grid(True, which='both', alpha=0.3)
        axs[0].set_ylabel('|Pi_12| (gefuellt: Anziehung, offen: Abstossung); Linien: Kontinuum')
        axs[1].legend(fontsize=7, loc='lower left')
        fig.tight_layout(); fig.savefig(os.path.join(aus, 'pi12_%s.png' % qn), dpi=110); plt.close(fig)
        # Richtungsabhaengigkeit
        fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
        pp = 1.0 if qn == 'a' else 3.0
        for ax, n in zip(axs, NETZE):
            rt = tab['%s_%s' % (n, qn)]['richtungen_r8']
            hk = np.array([x['hkl'] for x in rt], float)
            hk /= np.linalg.norm(hk, axis=1)[:, None]
            th = np.degrees(np.arccos(np.clip(hk[:, 2], -1, 1))); ph = np.degrees(np.arctan2(hk[:, 1], hk[:, 0]))
            val = np.array([x['r_hoch_p_Pi'] for x in rt])
            vm = np.abs(val).max()
            sc = ax.scatter(ph, th, c=val, cmap='coolwarm', vmin=-vm, vmax=vm, s=70, edgecolors='k', linewidths=0.4)
            for x, p_, t_ in zip(rt, ph, th):
                if tuple(x['hkl']) in BENANNT.values() or tuple(x['hkl']) == (0, 0, 1):
                    ax.annotate(str(x['hkl']), (p_, t_), fontsize=7, xytext=(3, 3), textcoords='offset points')
            plt.colorbar(sc, ax=ax, label='r^%d Pi_12 bei r nahe 8' % pp)
            ax.set_xlabel('phi (Grad)'); ax.set_ylabel('theta zur z-Achse (Grad)')
            ax.set_title('%s, %s: Richtungsabhaengigkeit' % (namen[qn], n))
            ax.invert_yaxis()
        fig.tight_layout(); fig.savefig(os.path.join(aus, 'richtung_%s.png' % qn), dpi=110); plt.close(fig)
    # Kelvin
    if kont is not None:
        fig, ax = plt.subplots(figsize=(7, 4.4))
        for L in groessen:
            P = alle[L]['iso']['Pi_korr_a']; r = alle[L]['iso']['r']
            m = r >= 2
            ax.plot(r[m], P[m] / kont.z['iso_Pi_kelvin_a'][m] - 1, '.', ms=2, label='L = %d, korrigiert' % L, alpha=0.6)
        P = H['iso']['Pi_torus_a']; r = H['iso']['r']
        ax.plot(r, P / kont.z['iso_Pi_kelvin_a'] - 1, '.', ms=1.5, color='grey', alpha=0.4, label='L = %d, unkorrigiert' % Lh)
        ax.axhspan(-0.05, 0.05, color='g', alpha=0.1); ax.axvline(6, color='k', lw=0.6)
        ax.set_ylim(-0.4, 0.2); ax.set_xlabel('r (Stablaengen)'); ax.set_ylabel('Pi_12/Pi_Kelvin - 1')
        ax.set_title('Punktlasten im isotropen Netz gegen Kelvin (alle Gittervektoren)'); ax.legend(fontsize=7)
        fig.tight_layout(); fig.savefig(os.path.join(aus, 'kelvin.png'), dpi=110); plt.close(fig)
    # Torus-Effekt
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
    for ax, qn in zip(axs, ('a', 'b')):
        ix, rs = dpts[(1, 1, 0)]
        for L in groessen:
            ax.plot(rs, alle[L]['iso']['Pi_torus_' + qn][ix] * (rs if qn == 'a' else rs ** 3), 'o--', mfc='none', ms=4, label='L = %d unkorrigiert' % L)
            ax.plot(rs, alle[L]['iso']['Pi_korr_' + qn][ix] * (rs if qn == 'a' else rs ** 3), '-', label='L = %d korrigiert' % L)
        ax.axhline(0, color='k', lw=0.6)
        ax.set_xlabel('r laengs [110] (Stablaengen)')
        ax.set_ylabel('r Pi_12' if qn == 'a' else 'r^3 Pi_12')
        ax.set_title('%s, isotropes Netz: Torus und Korrektur' % namen[qn]); ax.legend(fontsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(aus, 'torus.png'), dpi=110); plt.close(fig)
    # Verschiebung
    fig, ax = plt.subplots(figsize=(7, 4.6))
    for n, ls in (('aniso', '-'), ('iso', '--')):
        for qn, key in (('a', 'u_korr_a'), ('b', 'u_b'), ('c', 'u_c')):
            u = np.linalg.norm(H[n][key], axis=1); ru = H[n]['u_r_' + qn]
            sch = schalen(ru, u); ks = [k for k in sch if sch[k]]
            ax.loglog(ks, [sch[k] for k in ks], ls, marker='o', ms=3, label='%s, %s' % (namen[qn], n))
    rg = np.array([2, 16.0])
    ax.loglog(rg, 0.3 / rg, 'k:', lw=0.8, label='~ 1/r'); ax.loglog(rg, 0.3 / rg ** 2, 'k-.', lw=0.8, label='~ 1/r^2')
    ax.set_xlabel('r (Stablaengen)'); ax.set_ylabel('Schalen-RMS |u|')
    ax.set_title('Verschiebung einer einzelnen Quelle (L = %d)' % Lh); ax.legend(fontsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(aus, 'verschiebung.png'), dpi=110); plt.close(fig)
    print('auswertung fertig:', {k: v['urteil'] for k, v in E['urteile'].items()}, flush=True)


if __name__ == '__main__':
    main()
