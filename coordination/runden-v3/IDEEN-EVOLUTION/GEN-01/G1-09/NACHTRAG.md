# G1-09 Nachtrag (Test-Agent T-2)

- 2026-09-30 08:10:20 CEST (date). KARTE.md geprueft, nicht geaendert; nur die Zeile "Vorhersage geschrieben:
  2026-09-30 07:58:24 CEST" angehaengt. Vorhersage, "scheitert, wenn", Gegenprobe R0 = 0 und Plausibilitaetsschranke
  waren vollstaendig.
- **Geparkt wegen der Zeitbox (45 min fuer fuenf Karten), nicht wegen der 1-h-Grenze.** Kein Code, keine Formprobe, kein
  LAUF.txt. Der neue Teil braucht nach meiner Schaetzung 30 bis 45 min und passte nicht mehr in die Restzeit.
- Fuer einen Folgeauftrag (Kopie von RUNDE-05/r5a/r5a.py, torch, --geraet cpu erlaubt; Spur cpu oder p4000a):
  - vorhanden:
    - familie / schiessen_radial (omega^2 = 0,52 steht dort schon in M_DREI)
    - profil_radial, ball_radial (chi = r f, chi_t = -i omega chi)
    - entwickeln_radial und stufen_radial (grob dr 0,1 / dt 0,05, fein halb; Box 150, Daempfung ab 110)
    - messer (Q_tot, E_tot, S im Zentrum)
    - Zeitbudget 540 s
  - neu:
    - Startzustand f(r) w(r) mit w(r) = f(R_d - (r - R0)) / f(0), Argument unter 0 wie f(0)
    - Messung R_v(t) und R_d(t) (S = S_c/2, linear interpoliert), dazu die radiale Stroemung innen
    - T_E(R0) per Quadratur der Energiebilanz aus KARTE.md mit R = R0 - u^2 (Wurzel-Singularitaet am Start), sigma =
      Int 2 f'^2 dr, rho = 2 omega^2 S_c und R_d0 aus dem gerechneten Profil. T_E wird vor der Zeitentwicklung
      ausgegeben.
    - V1 bis V3, Gegenprobe R0 = 0 und die Schranken als Pruefungen mit "bestanden"
  - Laufzeit laut Karte unter 2 min: 4 Laeufe (R0 = 0 / 8 / 12 / 18) x T = 120, radial 1500 bzw. 3000 Punkte

## Nachtrag 2 (Test-Agent T-2, 2026-09-30 08:14:16 CEST, date)

- Die Parkung von 08:10 ist aufgehoben: Die Restzeit der Zeitbox reichte doch fuer den Code. blase.py (Kopie von r5a.py
  plus Unterbefehl "blase"), Formprobe 08:13 rc 0 fuer beide Teile, LAUF.txt liegt vor.
- Umsetzung der Karte:
  - T_E per Quadratur mit sigma = Int 2 f'^2 dr (plus Schwanz), rho = 2 omega^2 S_c und R_d0 = R_halb aus profil_kenn
    des gerechneten Profils. Das Schiessen schafft 0,52 (Profil gueltig), resonanz3d.py wird nicht gebraucht.
  - R_v und R_d: Radien mit S = S_c/2, linear interpoliert.
  - t70: erste Zeit mit R_v <= 0,7 R0, linear zwischen Messpunkten (Abstand 0,5).
  - V3 "monoton": R_v steigt vor t70 nie um mehr als 0,05 ueber sein bisheriges Minimum; dazu wird t70 bis T erreicht.
  - Erhaltung von Q und E auf 1e-4 bis t_chk = 110 - R_d0 - 5. Frueher kann keine Strahlung (v < 1) vom Ballrand die
    Daempfungsschicht ab r = 110 erreichen.
  - Wandgeschwindigkeit: Schranke c_Q = 0,71 aus der Karte (Papierwert, nicht gerechnet).
  - Gegenprobe: radiale Stroemung max |2 Im(conj(chi) chi')/r^2| fuer r < 0,8 R_d.
- Die Formprobe laeuft nur bis T = 3. Ihre Zahlen gelten nicht und werden nicht geerntet. T_E ist die vorab berechnete
  Vorhersage, kein Laufergebnis.
