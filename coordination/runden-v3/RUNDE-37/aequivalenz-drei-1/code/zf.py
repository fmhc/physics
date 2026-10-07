# -*- coding: utf-8 -*-
"""AEQUIVALENZ-DREI-1: Zusammenfassung der Lauf-JSON von aq.py (nur Lesen der Zeitreihen und kleine Fits, numpy).

Aufruf (ueber kleintest.sh auf der .69): python zf.py <lauf-ordner> <aus.json>
"""
import glob
import json
import os
import sys
import time

import numpy as np


def lin(t, y, potenzen):
    tm = float(np.max(np.abs(t)))
    X = np.stack([(t / tm) ** p for p in potenzen], 1)
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    return c / tm ** np.array(potenzen, dtype=float), float(np.sqrt(np.mean((y - X @ c) ** 2)))


def fall(p):
    r = np.array(p['reihe_t_zE_zQ_PEz_H'])
    t, v = r[:, 0], r[:, 3] / r[:, 4]
    g = p['g_Q']
    out = {'a0_durch_g': p['a0_durch_g']}
    # stetige Beschleunigung nach dem schnellen Anfangsstueck: v(t) = c0 + a t (+ c3 t^3 fuer Einrasten/1PN)
    for name, (t1, t2), pot in (('lin_5_T', (5.0, 1e9), (0, 1)), ('lin_5_T_t2', (5.0, 1e9), (0, 1, 2)),
                                ('frueh_3_30_t3', (3.0, 30.0), (0, 1, 3)), ('frueh_3_60_t3', (3.0, 60.0), (0, 1, 3))):
        s = (t >= t1) & (t <= t2)
        c, rest = lin(t[s], v[s], pot)
        out[name] = {'a_durch_g': -c[1] / g, 'v0': c[0], 'rest_rel': rest / max(1e-300, float(np.abs(v[s]).max())),
                     'n': int(s.sum())}
    out['fallweg_Q'] = float(r[-1, 1] - r[0, 1])
    out['v_end'] = float(v[-1])
    return out


def main(ordner, aus):
    zeilen = []
    for f in sorted(glob.glob(os.path.join(ordner, '*.json'))):
        if os.path.basename(f).startswith('zf'):
            continue
        d = json.load(open(f))
        if 'zusammenfassung' not in d:
            continue
        b, ak, tr, pa = d['ball'], d['aktiv'], d['traege'], d['passiv']
        E = b['E']
        r = np.array(tr['reihe_t_XE_XQ_PE_H'])
        t, X, P, H = r[:, 0], r[:, 1], r[:, 3], r[:, 4]
        Pint = float(np.trapezoid(P, t))
        dX = float(X[-1] - X[0])
        T = float(t[-1] - t[0])
        vbar = dX / T
        kQ = tr['kQ']
        z = {'lauf': os.path.basename(f)[:-5], 'om': b['om_kont'], 'h': d['parameter']['h'], 'n': d['parameter']['n'],
             'kb': d['parameter']['kb'], 'dtf': d['parameter']['dtf'], 'phimax': d['parameter']['phimax'],
             'E': E, 'Q': b['Q'], 'bindung': b['bindung'], 'S_rel': b['S_rel'],
             'relax_iter': b['relax']['iter'], 'relax_rest': b['relax']['resid_rel'],
             'energie_randschicht_z': b['energie_randschicht_z'],
             'homogen_dH_gamma1_rel': ak['dH_dPhi_durch_E_plus_gS_minus_1_gamma1'],
             'M_aktiv_quelle_durch_E': ak['gamma1']['quelle_durch_E'],
             'M_aktiv_fit_korr_durch_E': ak['gamma1']['M_aktiv_korr_durch_E'],
             'M_aktiv_fit_roh_durch_quelle': ak['gamma1']['M_aktiv_fit_durch_quelle'],
             'aktiv_kontrolle_A_durch_M': ak['gamma1']['kontrolle_A_durch_M'],
             'aktiv_quelle_ausserhalb_r1': ak['gamma1']['quelle_betrag_ausserhalb_r1'],
             'E_tot_boost_durch_E_minus_1': tr['E_tot_durch_E_minus_1'],
             'identitaet_H_dX_durch_intP_minus_1': float(np.mean(H)) * dX / Pint - 1,
             'v_mittel': vbar, 'P_E_spanne_rel': tr['P_E_x_rel_spanne'],
             'kQ_durch_PE0_minus_1': tr['kQ_durch_PE0_minus_1'],
             'PE_mittel_durch_PE0_minus_1': Pint / T / (tr['P_E0_x_Q']) - 1,
             'M_traege_energiestrom_durch_Etot_minus_1': Pint / dX / tr['E_tot'] - 1,
             'M_traege_phase_durch_Etot_minus_1': kQ / vbar / tr['E_tot'] - 1}
        for gam in ('gamma1', 'gamma0'):
            z['fall_' + gam] = fall(pa[gam])
        # Massen in Q-Einheiten, traege Masse auf den ruhenden Ball bezogen (Faktor kQ/(v E_tot) mal E)
        MT = E * (1 + z['M_traege_phase_durch_Etot_minus_1'])
        ag1 = z['fall_gamma1']['frueh_3_30_t3']['a_durch_g'] if z['h'] > 0.7 else z['fall_gamma1']['lin_5_T']['a_durch_g']
        ag0 = z['fall_gamma0']['frueh_3_30_t3']['a_durch_g'] if z['h'] > 0.7 else z['fall_gamma0']['lin_5_T']['a_durch_g']
        MA = E * z['M_aktiv_quelle_durch_E']
        z['massen'] = {'M_aktiv': MA, 'M_traege_phase': MT, 'M_traege_energiestrom': E,
                       'a_durch_g_gamma1': ag1, 'a_durch_g_gamma0': ag0,
                       'M_passiv_gamma1': MT * ag1, 'M_passiv_gamma0': MT * ag0,
                       'Mp_durch_Mt_gamma1': ag1, 'Ma_durch_Mt_phase': MA / MT, 'Ma_durch_Mt_energiestrom': MA / E,
                       'Ma_durch_Mp_gamma1': MA / (MT * ag1), 'Mp_durch_E_gamma1': MT * ag1 / E,
                       'Mp_durch_E_gamma0': MT * ag0 / E}
        zeilen.append(z)
    out = {'zeilen': zeilen, 'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    with open(aus + '.tmp', 'w') as f:
        json.dump(out, f, indent=1)
    os.replace(aus + '.tmp', aus)
    for z in zeilen:
        m = z['massen']
        print('%-14s om %.3f h %.1f B %.4f S/E %.2e | Ma/E %.6f | Mt_ph/E %.5f (kQ/PE0-1 %.4f, PEsp %.3f, ident %.1e) | '
              'a/g g1 %.5f g0 %.5f (a0 %.5f %.5f) | Mp1/E %.5f Mp0/E %.5f | Ma/Mt %.5f Ma/Mp %.5f'
              % (z['lauf'], z['om'], z['h'], z['bindung'], z['S_rel'], z['M_aktiv_quelle_durch_E'],
                 m['M_traege_phase'] / z['E'], z['kQ_durch_PE0_minus_1'], z['P_E_spanne_rel'],
                 z['identitaet_H_dX_durch_intP_minus_1'], m['a_durch_g_gamma1'], m['a_durch_g_gamma0'],
                 z['fall_gamma1']['a0_durch_g'], z['fall_gamma0']['a0_durch_g'], m['Mp_durch_E_gamma1'],
                 m['Mp_durch_E_gamma0'], m['Ma_durch_Mt_phase'], m['Ma_durch_Mp_gamma1']), flush=True)
        for gam in ('gamma1', 'gamma0'):
            fz = z['fall_' + gam]
            print('    %s: lin_5_T %.5f  lin_5_T_t2 %.5f  frueh_3_30_t3 %.5f  frueh_3_60_t3 %.5f  fallweg %.3f'
                  % (gam, fz['lin_5_T']['a_durch_g'], fz['lin_5_T_t2']['a_durch_g'], fz['frueh_3_30_t3']['a_durch_g'],
                     fz['frueh_3_60_t3']['a_durch_g'], fz['fallweg_Q']), flush=True)
    print('->', aus)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
