import json, sys

def bilanziere(datei):
    with open(datei) as fh:
        d = json.load(fh)

    erg = d['ergebnis']
    H0 = erg['H0']
    H_ende = erg['proben'][-1][1]
    ereig = [e for e in erg['ereignisse'] if e.get('ausgefuehrt')]

    drift_zwischen = 0
    sum_dh_zug = 0
    sum_dh_neu = 0
    
    last_H = H0
    for e in ereig:
        h_vor = e['H_vor']
        h_nach = e['H_nach']
        # e['dH_zug_rel'] = (H_nach - H1g) / H0
        # e['dH_neu_rel'] = (H1g - H_vor) / H0
        dh_zug = e.get('dH_zug_rel', 0) * H0
        dh_neu = e.get('dH_neu_rel', 0) * H0
        
        drift_step = h_vor - last_H
        drift_zwischen += drift_step
        
        sum_dh_zug += dh_zug
        sum_dh_neu += dh_neu
        last_H = h_nach

    drift_end = H_ende - last_H
    drift_zwischen += drift_end
    
    ende_anfang = H_ende - H0
    summe_spruenge = sum_dh_zug + sum_dh_neu
    
    print(f"Bilanz für {datei}:")
    print(f"  Ende - Anfang:          {ende_anfang/H0: .8e}")
    print(f"  Summe dH_zug_rel:       {sum_dh_zug/H0: .8e}")
    print(f"  Summe dH_neu_rel:       {sum_dh_neu/H0: .8e}")
    print(f"  Drift zwischen Zuegen:  {drift_zwischen/H0: .8e}")
    
    rest = ende_anfang - (summe_spruenge + drift_zwischen)
    print(f"  Rest (sollte ~0 sein):  {rest/H0: .8e}\n")

bilanziere('lauf/g1p-s4-P-d1e-3')
try:
    bilanziere('lauf/g1p-s4-R-d1e-3')
except:
    pass
