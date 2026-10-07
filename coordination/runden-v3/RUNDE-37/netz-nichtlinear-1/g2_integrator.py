import sys, os, time, json
import numpy as np
import nn, td, uf
import scipy.linalg as sla

def g2_lauf(args):
    T0w = time.time()
    LV, pos, G0, O0, ninfo = td.netz_bauen(args.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    
    # Initiales Netz
    N0 = nn.NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    mode, xm, w2, Qm = td.tt_mode(N0, args.A, k1)
    om = mode['omega']
    Tper = 2 * np.pi / om
    wmax = np.sqrt(N0.eig['w2_max'])
    NT = int(np.ceil(Tper * wmax / 0.5))
    dt = Tper / NT
    nges = NT * args.perioden
    
    x = np.zeros(N0.m)
    y = sla.lu_solve(N0.lu, om * xm)
    
    H0 = N0.energie(x, y)[0]
    
    N = N0
    proben = []
    
    def probe(N_curr, x_curr, y_curr, t_curr):
        H, V, K = N_curr.energie(x_curr, y_curr)
        proben.append([t_curr, H])
        
    probe(N, x, y, 0.0)
    
    n_update = 200 # Update alle 200 Schritte (ca. 50x pro Lauf -> 50 * 4.5s = ~4 Min)
    
    # Wir brauchen eine Funktion, die N(x) baut
    def bau_Nx(x_vec):
        a_op = N0.S @ x_vec
        f_alt = 1.0 + a_op
        def f_neu_fn(N2, f_alt=f_alt):
            return f_alt
        return nn.NetzG(LV, pos, G0, O0, k1, hp, hx, f_fn=f_neu_fn, rolle='g2_update')
        
    for n in range(1, nges + 1):
        if time.time() - T0w > 550: # Kurz vor 10 Min abbrechen
            break
            
        if n % n_update == 0:
            # Implizite Mitte mit Fixpunktiteration fuer den Update-Schritt
            x_m = x.copy()
            y_m = y.copy()
            for it in range(3):
                N_m = bau_Nx(x_m)
                # Naeherung: dA/dx wird ignoriert, wir iterieren nur A(x_m) und B(x_m)
                B_m = N_m.B.toarray()
                A_m = N_m.A
                
                # Loese implizites System fuer linearen Teil (y_m, x_m sind Midpoints)
                # y_{n+1} = y_n - dt B_m x_m
                # x_{n+1} = x_n + dt A_m y_m
                # Da x_m = (x_n + x_{n+1})/2, y_m = (y_n + y_{n+1})/2:
                # y_m = y_n - dt/2 B_m x_m
                # x_m = x_n + dt/2 A_m y_m
                
                # Setze x_m ein: y_m = y_n - dt/2 B_m (x_n + dt/2 A_m y_m)
                # (I + dt^2/4 B_m A_m) y_m = y_n - dt/2 B_m x_n
                M_sys = np.eye(N0.m) + (dt**2 / 4.0) * (B_m @ A_m)
                rhs = y - (dt / 2.0) * (B_m @ x)
                y_m_neu = np.linalg.solve(M_sys, rhs)
                x_m_neu = x + (dt / 2.0) * (A_m @ y_m_neu)
                
                x_m = x_m_neu
                y_m = y_m_neu
                
            x = 2 * x_m - x
            y = 2 * y_m - y
            N = N_m  # Neues Netz fuer die naechsten Schritte
        else:
            # Normaler Leapfrog mit konstantem N
            B_curr = N.B.toarray()
            y_halb = y - 0.5 * dt * (B_curr @ x)
            x = x + dt * (N.A @ y_halb)
            y = y_halb - 0.5 * dt * (B_curr @ x)
            
        if n % NT == 0:
            probe(N, x, y, n * dt)
            print(f"Periode {n//NT}, dH_rel = {(proben[-1][1] - H0)/H0:.2e}", flush=True)

    with open(args.out, 'w') as fh:
        json.dump({'proben': proben, 'H0': H0}, fh)

if __name__ == '__main__':
    class Args:
        netz = sys.argv[1]
        A = 1e-3
        perioden = 10
        out = sys.argv[2]
    g2_lauf(Args())
