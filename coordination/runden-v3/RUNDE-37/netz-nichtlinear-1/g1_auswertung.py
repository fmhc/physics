import json, sys, glob, os
import numpy as np

def main():
    files = glob.glob('lauf/g1-*.json') + glob.glob('lauf/gm-*.json')
    files.sort()
    
    print("Netz | Arm | Variante | Zuege (2-3/3-2) | Ausn alt | Ausn neu | M_neg max | dH nach 10 T | Summe dH reg")
    print("|---|---|---|---|---|---|---|---|---|")
    
    for f in files:
        with open(f) as fh:
            d = json.load(fh)
        
        erg = d.get('ergebnis', {})
        if not erg.get('fertig'):
            print(f"{f} nicht fertig")
            continue
            
        netz = erg.get('netz', '').split('-')[-1]
        arm = erg.get('arm', '')
        lesart = erg.get('lesart', '')
        # Variante ist g1 oder gm
        variante = os.path.basename(f).split('-')[0]
        
        ereig = erg.get('ereignisse', [])
        zuege = [e for e in ereig if e.get('ausgefuehrt')]
        
        n_23 = sum(1 for e in zuege if e['typ'] == 23)
        n_32 = sum(1 for e in zuege if e['typ'] == 32)
        
        ausn_alt = sum(1 for e in zuege if e['typ'] == 23 and e.get('mu_hg', 0) > 0)
        ausn_neu = sum(1 for e in zuege if not e['nach']['A_pd'])
        
        m_neg_max = max([e['nach']['M_n_neg'] for e in zuege]) if zuege else 128
        
        proben = erg.get('proben', [])
        dh_10T = 0
        if proben:
            h0 = erg.get('H0', 1)
            dh_10T = (proben[-1][1] - h0) / h0
            
        sum_dh_reg = 0
        for e in zuege:
            if e['nach']['A_pd']:
                sum_dh_reg += e.get('dH_rel', 0)
                
        print(f"| {netz} | {arm}-{lesart} | {variante} | {len(zuege)} ({n_23}/{n_32}) | {ausn_alt} | {ausn_neu} | {m_neg_max} | {dh_10T:.2e} | {sum_dh_reg:.2e} |")

if __name__ == '__main__':
    main()
