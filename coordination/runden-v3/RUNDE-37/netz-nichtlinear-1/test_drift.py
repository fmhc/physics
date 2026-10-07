import json

with open('lauf/g1p-s4-P-d1e-3') as fh:
    d = json.load(fh)

erg = d['ergebnis']
H0 = erg['H0']
ereig = [e for e in erg['ereignisse'] if e.get('ausgefuehrt')]

drift = 0
last_H = H0

print(f"H0 = {H0}")
for i, e in enumerate(ereig):
    h_vor = e['H_vor']
    h_nach = e['H_nach']
    dh_zug = h_nach - h_vor
    drift_step = h_vor - last_H
    print(f"Zug {i}: drift davor = {drift_step/H0:.2e}, H_vor = {h_vor}, H_nach = {h_nach}, Sprung = {dh_zug/H0:.2e}")
    drift += drift_step
    last_H = h_nach

drift_end = erg['proben'][-1][1] - last_H
drift += drift_end
print(f"Drift Ende: {drift_end/H0:.2e}, H_ende = {erg['proben'][-1][1]}")

print(f"Total Drift: {drift/H0:.2e}")
print(f"Summe dH Zug: {sum(e['dH_rel'] for e in ereig):.2e}")
print(f"Ende - Anfang: {(erg['proben'][-1][1] - H0)/H0:.2e}")
