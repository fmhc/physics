## 3 Kontrollen

### Absorber-Reflexion (Vorab-Kontrolle, Plan 7; grobes Gitter, Vakuum, Pakete r0 = 30, Breite 6, Amplitude 1e-3)

| Paket | E(0) | E(r < 55, T_end = 500) / E(0) (Planmass) | max ueber t >= 400 (Zusatz) | Gesamtbilanz inkl. Absorption |
|---|---|---|---|---|
| psi, k0 = 1,41 | 1,07e-3 | 5,5e-11 | 6,7e-11 | 1,6e-8 |
| psi, k0 = 0,7 | 6,67e-4 | 3,6e-7 | 1,1e-6 | 5,5e-9 |
| chi, k0 = 1,6 | 3,05e-4 | 1,1e-10 | 1,3e-10 | 2,3e-8 |
| chi, k0 = 0,7 | 1,67e-4 | 3,6e-7 | 1,3e-6 | 5,5e-9 |

- Planmass < 1e-6 in allen vier Faellen: Schwamm angenommen (vor den Hauptlaeufen).
- Bei den langsamen Paketen (k0 = 0,7) liegt der spaete Hoechstwert knapp ueber 1e-6. Ob das Reflexion ist oder der
  langsame Spektralrest (k < 0,15, Gruppengeschwindigkeit < 0,1), trennt der Test nicht. Die Strahlung der Arme (i)
  und (ii) liegt bei k = 1,4 bis 3,3 (Reflexion ~1e-10).

### Hintergrund (eigener Newton auf dem Zeitgitter, D2 4. Ordnung, R = 120)

| Stelle | Gitter | omega^2 | Q (eigen) | dQ rel. zu stille3 (hp 0,05) | r_half | chi(0) | Restresiduum |
|---|---|---|---|---|---|---|---|
| S-a (i) | h = 0,05 | 0,86085981 | 11073,6629 | 5,0e-8 | 10,9025 | 3,63e-5 | 2,8e-12 |
| S-a (i) | h = 0,025 | 0,86085981 | 11073,6637 | 2,5e-8 | 10,9025 | 3,63e-5 | 1,4e-11 |
| S-a (ii) | 0,05 / 0,025 | 0,87085981 | 9026,4279 / 9026,4286 | 5,1e-8 / 2,5e-8 | 10,177 | 7,97e-5 | <= 1,1e-11 |
| S-b (i) | h = 0,05 | 0,84743426 | 14971,3726 | 5,0e-8 | 12,0670 | 1,02e-5 | 4,2e-12 |
| S-b (i) | h = 0,025 | 0,84743426 | 14971,3737 | 2,5e-8 | 12,0670 | 1,02e-5 | 1,4e-11 |
| S-b (ii) | 0,05 / 0,025 | 0,85743426 | 11921,6401 / 11921,6410 | 5,0e-8 / 2,5e-8 | 11,177 | 2,70e-5 | <= 9,8e-12 |

- chi(0) stimmt mit der STILLE-ZWEIFELD-Tabelle (S-a 3,6e-5, S-b 1,0e-5) ueberein: volle Huelle.

### Lokalisierung der Mode (Kastenmode R_box = 50, Plan 3)

| Stelle, Mode | Gitter | rho (eigen) | rho Karte | lambda bei rho Karte | a-Schwanz | c-Schwanz | Anteil a aussen | Lokalisierung | c max / eps |
|---|---|---|---|---|---|---|---|---|---|
| S-a (i) | 0,05 | 1,0697634705 | 1,06976351 | -9,0e-8 | 1,0e-6 | 1,9e-6 | 1,8e-11 | 1 - 5e-9 | 0,376 |
| S-a (i) | 0,025 | 1,0697634990 | 1,06976351 | -2,5e-8 | 2,1e-7 | 1,9e-6 | 1,6e-11 | 1 - 5e-9 | 0,376 |
| S-a (ii) | 0,05 / 0,025 | 1,0953666 / 1,0953667 | - | - | 0,258 | 3,1e-6 | 0,215 | 0,813 | 0,412 |
| S-b (i) | 0,05 | 1,3395604865 | 1,33956049 | -9,5e-9 | 1,9e-6 | 1,5e-3 | 7,5e-10 | 0,99996 | 3,70 |
| S-b (i) | 0,025 | 1,3395604958 | 1,33956049 | 1,6e-8 | 1,1e-7 | 1,6e-3 | 7,5e-10 | 0,99996 | 3,70 |
| S-b (ii) | 0,05 / 0,025 | 1,3583658 / 1,3583658 | - | - | 0,168 | 3,6e-3 | 0,067 | 0,943 | 37,8 |

- Schwanz = Betrag der u-Komponente (r a, r b, r c/2) in [r_half + 15, 45] relativ zum Maximum der Mode. Anteil a
  aussen = Normanteil der a-Komponente bei r > r_half + 5.
- Lineare Ladung der Mode (muss fuer eine Eigenmode verschwinden): |q1_rel| <= 7e-15 (i) und <= 7e-13 (ii).
