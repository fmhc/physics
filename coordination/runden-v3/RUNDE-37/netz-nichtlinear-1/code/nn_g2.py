import sys, os, time, json
import numpy as np
import scipy.sparse as sp
import scipy.linalg as sla
import argparse
import nn, td, uf

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('netz')
    ap.add_argument('out')
    ap.add_argument('--A', type=float, default=1e-3)
    ap.add_argument('--perioden', type=float, default=10.0)
    ap.add_argument('--h', type=float, default=0.5)
    ap.add_argument('--n_update', type=int, default=200)
    args = ap.parse_args()

    T0w = time.time()
    LV, pos, G0, O0, ninfo = td.netz_bauen(args.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    
    N0 = nn.NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    if not N0.A_pd:
        raise RuntimeError('A_red nicht positiv definit')
    
    mode, xm, w2, Qm = td.tt_mode(N0, args.A, k1)
    om = mode['omega']
    Tper = 2 * np.pi / om
    wmax = np.sqrt(N0.eig['w2_max'])
    NT = int(np.ceil(Tper * wmax / args.h))
    dt = Tper / NT
    nges = int(NT * args.perioden)

    x = np.zeros(N0.m)
    y = sla.lu_solve(N0.lu, om * xm)
    
    H0 = N0.energie(x, y)[0]
    N = N0
    
    proben = []
    ereig = []
    
    def probe(N_curr, x_curr, y_curr, t_curr):
        H, V, K = N_curr.energie(x_curr, y_curr)
        mu = N_curr.mu_alle(x_curr)
        proben.append([t_curr, H, V, K, float((mu < 0).sum()), float(mu.min())])

    probe(N, x, y, 0.0)
    
    t_cur = 0.0
    for n in range(1, nges + 1):
        if time.time() - T0w > 540:
            break
            
        # Update des Operators alle n_update Schritte
        if n % args.n_update == 0:
            # Baue neues Netz am gedehnten Zustand x
            a_op = N.S @ x
            f_alt = 1.0 + a_op
            def f_neu_fn(N2, f_alt=f_alt): return f_alt
            N2 = nn.NetzG(LV, pos, N.G, N.O, k1, hp, hx, f_fn=f_neu_fn, rolle='g2_update')
            N = N2

        # Impliziter Midpoint (bzw. verallgemeinerter Leapfrog linearisiert)
        # Fixpunktiteration fuer x_{n+1/2}, y_{n+1/2}
        xm = x.copy()
        ym = y.copy()
        
        A_n = N.Ar
        B_n = N.Br
        
        for it in range(3):
            # y_{n+1/2} = y_n - dt/2 * B * x_{n+1/2}
            # x_{n+1/2} = x_n + dt/2 * A * y_{n+1/2}
            # Da M_eff konstant ist in diesem Schritt, ist das ein lineares System
            M_sys = np.eye(N0.m) + (dt**2 / 4.0) * (A_n @ B_n)
            rhs = x + (dt / 2.0) * (A_n @ y)
            xm = np.linalg.solve(M_sys, rhs)
            ym = y - (dt / 2.0) * (B_n @ xm)
            
        x = 2 * xm - x
        y = 2 * ym - y
        t_cur += dt
        
        # Umklapp-Detektion (vereinfacht, wir prüfen nach dem Schritt)
        mu1 = N.mu_alle(x)
        kand = np.nonzero(mu1 < 0)[0]
        if len(kand) > 0 and 's2' in args.netz:
            # Wenn ein Zug passiert, brechen wir hier für den Test ab,
            # oder wir loggen es zumindest. Ein voller Umklapp mit NetzG
            # erfordert td.abbilden.
            j = kand[0]
            print(f"Zug {j} bei t={t_cur} erkannt!", flush=True)
            # Da g2_integrator.py ein Proof-of-Concept ist, brechen wir ab.
            ereig.append({'t': t_cur, 'j': int(j), 'ausgefuehrt': False})
            break
            
        if n % NT == 0:
            probe(N, x, y, t_cur)
            print(f"Periode {n//NT}, H = {proben[-1][1]:.6e}, dH_rel = {(proben[-1][1] - H0)/H0:.2e}", flush=True)

    with open(args.out, 'w') as fh:
        json.dump({'proben': proben, 'H0': H0, 'ereignisse': ereig}, fh)

if __name__ == '__main__':
    main()
