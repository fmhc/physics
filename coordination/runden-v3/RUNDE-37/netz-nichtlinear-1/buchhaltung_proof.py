import json

with open('lauf/g1p-s4-P-d1e-3') as fh:
    d = json.load(fh)

erg = d['ergebnis']
H0 = erg['H0']
ereig = [e for e in erg['ereignisse'] if e.get('ausgefuehrt')]

print("Zug | stabil_dt | drift_davor (rel) | instabil?")
print("----|-----------|-------------------|----------")
last_H = H0
for i, e in enumerate(ereig):
    h_vor = e['H_vor']
    drift_step = h_vor - last_H
    
    # Der stabil_dt-Wert, der WÄHREND dieses Intervalls (also seit dem *letzten* Zug) wirkte,
    # wurde im *vorherigen* Ereignis (als 'nach' dem Zug) gespeichert.
    # Für Zug 0 wirkte N0 (stabil_dt = 0.5).
    if i == 0:
        s_dt = 0.5
    else:
        s_dt = ereig[i-1]['stabil_dt']
        
    instabil = "JA!" if s_dt > 2.0 else "nein"
    print(f"{i:3d} | {s_dt:9.3f} | {drift_step/H0:17.2e} | {instabil}")
    
    last_H = e['H_nach']
