#!/usr/bin/env python3
# ISO-ATEM-1, Diagnose [D] NACH dem Einfrieren (beschreibend, kein Urteil).
# Importiert den eingefrorenen Code unveraendert. (a) Beruehrtest-Probe, (b) Symmetrie der Teil-C-Loesungen,
# (c) Fortsetzung je eines Vertreters in lambda (Richtung 1 und kleiner).
import sys, json, time, importlib.util, itertools
import numpy as np

spec = importlib.util.spec_from_file_location('ia', sys.argv[1])
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)
zf_pfad, out_pfad = sys.argv[2], sys.argv[3]
I3 = np.eye(3)


def probe_beruehrung():
    out = {}
    V = ia.S * ia.D
    fn, ed = ia.achsen_tetra(V)
    for d in (0.1, 0.3, 0.6, 1.5):
        Q = V + np.array([d, 0, 0])
        fq, eq = ia.achsen_tetra(Q)
        out['verschoben_%g' % d] = ia.sat_gap(V, Q, fn, ed, fq, eq)
    # gemeinsame Ecke v = V[0]; Partner = A-Tetraeder um v gedreht (kleiner Winkel -> Ueberlappung)
    v = V[0]
    for wg in (5, 30, 60, 90, 180):
        Rr = ia.rot_axis([1, -1, 0], np.radians(wg))
        Q = (V - v) @ Rr.T + v
        fq, eq = ia.achsen_tetra(Q)
        t = 0.05
        P1 = np.vstack([v + t * (V[i] - v) for i in (1, 2, 3)] + [V[i] for i in (1, 2, 3)])
        P2 = np.vstack([v + t * (Q[i] - v) for i in (1, 2, 3)] + [Q[i] for i in (1, 2, 3)])
        cosw = ((0 - v) @ (Q.mean(0) - v)) / np.linalg.norm(v) / np.linalg.norm(Q.mean(0) - v)
        out['ecke_gedreht_%d' % wg] = {'g': ia.sat_gap(P1, P2, fn, ed, fq, eq),
                                       'mitte_ecke_mitte_grad': float(np.degrees(np.arccos(np.clip(cosw, -1, 1))))}
    return out


NAMEN = {}
for i, M in enumerate(ia.O24):
    tr = np.trace(M)
    art = {3: 'E', -1: '2', 0: '3', 1: '4'}[int(round(tr))]
    w, U = np.linalg.eig(M)
    ax = np.real(U[:, np.argmin(np.abs(w - 1))]); ax = ax / np.max(np.abs(ax))
    NAMEN[i] = art + str(np.round(ax).astype(int).tolist())


def symdetail(c, R, lam, tol=1e-7):
    a = lam * ia.A0
    V = c[ia.PJ] + np.einsum('pab,pb->pa', R[ia.PJ], ia.T_OFF[ia.PJ, ia.PK])
    res = []
    for qi, Q in enumerate(ia.O24):
        for jp in range(8):
            tau = c[jp] - Q @ c[0]
            mc = c @ Q.T + tau
            ec = np.linalg.norm(ia.wrap(mc[:, None, :] - c[None, :, :], a), axis=2).min(1).max()
            mv = V @ Q.T + tau
            ev = np.linalg.norm(ia.wrap(mv[:, None, :] - V[None, :, :], a), axis=2).min(1).max()
            if max(ec, ev) < tol:
                w, U = np.linalg.eig(Q)
                ax = np.real(U[:, np.argmin(np.abs(w - 1))]); ax /= np.linalg.norm(ax)
                tf = tau / a
                par = float(((tf @ ax) * ax @ ax))
                # Schraubanteil laengs der Achse (Bruchteil der Gitterperiode laengs der Achse)
                per = 1.0 if np.sum(np.abs(np.round(ax * np.sqrt(3)))) != 3 else np.sqrt(3)
                res.append({'op': NAMEN[qi], 'tau_frac': [float(x % 1.0) for x in tf],
                            'laengs': float((tf @ ax) % per)})
                break
    return res


def fortsetzen(c, R, lam0, ziele):
    spur = []
    cc, RR = c.copy(), R.copy()
    for lam in ziele:
        s = lam / lam0 if False else None
        cE, RE, it = ia.lm(cc, RR, lam, 400)
        D = ia.rest(cE, RE, lam * I3)
        geo = ia.geometrie(cE, RE, lam * I3)
        wk = [ia.drehwinkel_achse(RE[j])[0] for j in range(8)]
        J = ia.jac_voll(cE, RE)
        sv = np.linalg.svd(J, compute_uv=False)
        Jl = np.hstack([J, (-ia.A0 * ia.PN).reshape(48, 1)])
        svl = np.linalg.svd(Jl, compute_uv=False)
        st = ia.sym_test(cE, RE, lam)
        spur.append({'lambda': lam, 'r_max': ia.rmax(D), 'iter': int(it), 'g_nb': geo['g_nb'], 'g_adj': geo['g_adj'],
                     'd_OO': geo['d_OO'], 'drehwinkel_grad': [float(np.degrees(x)) for x in wk],
                     'max_dreh_grad': float(np.degrees(max(wk))),
                     'mitten_abw_max': float(np.max(np.linalg.norm(cE - lam * ia.C0 - (cE[0] - lam * ia.C0[0]), axis=1))),
                     'nullitaet_fest': int(np.sum(sv < 1e-8 * sv[0])), 'nullitaet_lam_frei': int(np.sum(svl < 1e-8 * svl[0])),
                     'n_O24': st['n_O24'], 'P213': st['P213']})
        if ia.rmax(D) < 1e-10:
            # naechster Start: Mitten mitskalieren
            cc = cE * 1.0; RR = RE.copy()
        else:
            break
    return spur


t0 = time.time()
out = {'probe_beruehrung': probe_beruehrung()}
zf = json.load(open(zf_pfad))
for L in zf['laeufe']:
    lam = L['lambda']
    lo = [s for s in L['starts'] if s['klasse'] == 'Loesung']
    klassen = {}
    for s in lo:
        c = np.array(s['mitten']); R = np.array(s['R'])
        sd = symdetail(c, R, lam)
        sig = ' '.join(sorted(x['op'] + ('s' if abs(x['laengs'] - 0.5) < 1e-6 else '') for x in sd))
        winkel = np.round(sorted(s['drehwinkel_grad']), 4).tolist()
        uebl = not ((s['g_nb'] is None or s['g_nb'] > 0) and (s['g_adj'] is None or s['g_adj'] > 0))
        key = sig + ' | ' + str(winkel)
        k = klassen.setdefault(key, {'n': 0, 'nah': 0, 'weit': 0, 'P213': s['sym']['P213'], 'ops': sd,
                                     'winkel': winkel, 'ueberlappung': uebl, 'g_nb': s['g_nb'], 'g_adj': s['g_adj'],
                                     'd_OO': s['d_OO'], 'beispiel_i': (s['art'], s['i'])})
        k['n'] += 1; k[s['art']] += 1
    out['lambda_%g' % lam] = {'n_loesungen': len(lo), 'n_klassen': len(klassen),
                              'klassen': sorted(klassen.values(), key=lambda k: -k['n'])}
# Fortsetzung je eines Vertreters (lambda = 0,97): P2_13 und nicht P2_13
L97 = [L for L in zf['laeufe'] if abs(L['lambda'] - 0.97) < 1e-12][0]
fort = {}
for name, bed in (('P213', True), ('nicht_P213', False)):
    kand = [s for s in L97['starts'] if s['klasse'] == 'Loesung' and s['sym']['P213'] == bed and s['art'] == 'nah']
    if not kand:
        continue
    s = kand[0]
    c = np.array(s['mitten']); R = np.array(s['R'])
    hoch = [0.97 + 0.0025 * i for i in range(1, 13)]
    runter = [0.97 - 0.01 * i for i in range(1, 28)]
    fort[name] = {'start': (s['art'], s['i']), 'hoch': fortsetzen(c, R, 0.97, hoch), 'runter': fortsetzen(c, R, 0.97, runter)}
out['fortsetzung'] = fort
out['laufzeit_s'] = time.time() - t0
json.dump(out, open(out_pfad, 'w'), indent=1)
print('fertig diag %.1f s' % out['laufzeit_s'])
