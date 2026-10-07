# KUGELSCHALE-1: Kraefteverhaeltnis einer Kugel aus Dreiecken: wann bleibt sie rund, wann knickt sie zum Ikosaeder? (Runde 23)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 22:07:17 CEST (date), vor jeder Rechnung. Gerechnet von der Leitung.
- Finn ~22:12: "ok dann ueberleg aber mal mit der kugel aus dreiecken, hat die noch eine aussenkraft? wie ist das
  verhaeltnis der kraefte da?"
- Herkunft:
  - WINKELFELD-1 (R22): Winkelspannung und Beulen.
  - Euler: Jede Kugel-Triangulierung hat netto 12 Fuenfer-Ecken.
  - DIM-BEUTEL (R16): Huellenanteil 1/(d+1); gemessen 0,2497 bei freiem Inhalt in 3D (M3), M2-Tropfen 0,1455.
- Literatur aus dem Gedaechtnis [L?]: Lidmar/Mirny/Nelson 2003. Elastische Kugelschalen mit 12 Disklinationen werden
  oberhalb einer Foeppl-von-Karman-Zahl gamma = Y R^2/kappa ~ 154 zu facettierten Ikosaedern (Viruskapside).
- Ableitbarkeitspruefung: Im Projekt nicht gerechnet. Die Lage des Uebergangs in unserem Federmodell ist nicht ablesbar.
- Explorativ (v3), L4 (Literaturwert). Ein Lauf <= 10 min.

## Test

- Geodaetische Kugel: Ikosaeder, Frequenz n unterteilt (n = 8 und 12; 642 bzw. 1442 Ecken), auf die Kugel projiziert.
  Federn k = 1 mit Ruhelaenge = mittlere Kantenlaenge (Dreiecke wollen flach und gleichseitig sein).
  Biegeenergie kappa Sum (1 - n_1 . n_2) ueber Nachbardreiecke (flach bevorzugt).
- Relaxation mit L-BFGS (Code relax2d aus WINKELFELD-1, dim = 3), kleine Zufallsauslenkung, je kappa ein Lauf.
- **gamma** = Y R^2/kappa_c mit Y = 2/sqrt3 (Dreiecksnetz, k = 1, a = 1) und kappa_c = (sqrt3/2) kappa (Seung/Nelson).
  R ist der mittlere Radius nach der Relaxation. Scan ueber gamma von ~10 bis ~3000 (ueber kappa).
- **Messgroessen:**
  - Asphaerizitaet A = <(r - <r>)^2>/<r>^2
  - Anteil Dehnenergie an der Gesamtenergie
  - Verhaeltnis Radius an den 12 Fuenfer-Ecken zu mittlerem Radius (Spitzen)

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K1 | A steigt zwischen gamma = 50 und 500 um mindestens das 10-Fache (Uebergang rund -> facettiert) | 70 % |
| K2 | Der steilste Anstieg von log A gegen log gamma liegt bei gamma zwischen 80 und 300 (Literatur ~154) | 55 % |
| K3 | Oberhalb des Uebergangs liegen die 12 Fuenfer-Ecken als Spitzen aussen (Radius > 1,02 x mittlerer Radius) | 75 % |
| K4 | Der Dehnanteil der Energie faellt oberhalb des Uebergangs unter 50 % (Knicken tauscht Dehnung gegen Biegung) | 60 % |

**Bedeutung (vorab):** Treffen K1 bis K3 ein, entscheidet das Kraefteverhaeltnis Dehnen gegen Biegen (gamma), ob die
Dreieckskugel rund bleibt oder zum Ikosaeder knickt. Die Spannung sammelt sich an den 12 Fuenfer-Ecken [L, nachgerechnet].

## Plan der echten Laeufe (Leitung, 2026-10-02 22:11:30 CEST; vor den Laeufen eingefroren)

- **Rauchlauf** (n = 4, N = 162, gesehen):
  - Euler V - E + F = 2; 12 Fuenfer- und 150 Sechser-Ecken.
  - gamma = 20: A = 9,2e-6, Spitzen 0,9905, Dehnanteil 0,103.
  - gamma = 2000: A = 2,2e-3, Spitzen 1,138, Dehnanteil 0,041.
  - Selbstanzeige: K1 und K3 sind fuer n = 4 damit schon angedeutet; gewertet wird mit n = 8 und 12.
- **Echte Laeufe:** n = 8 (N = 642) und n = 12 (N = 1442); gamma = 10, 20, 40, 70, 100, 150, 200, 300, 500, 1000, 2000, 4000
  (Soll; berichtet wird gamma_eff mit dem relaxierten R).
- **Auswertung:**
  - K1: A(gamma_eff ~ 500)/A(gamma_eff ~ 50) >= 10, je n (Interpolation in log-log).
  - K2: groesste lokale Steigung von log A gegen log gamma_eff zwischen benachbarten Punkten; deren Mitte liegt zwischen 80
    und 300.
  - K3: Spitzen_rel > 1,02 bei gamma_eff oberhalb der K2-Stelle.
  - K4: Dehnanteil < 0,5 oberhalb der K2-Stelle.
- Hinweis zu K4: Schon im Rauchlauf ist der Dehnanteil auch unterhalb klein (0,10). K4 ist damit wenig trennscharf;
  berichtet wird zusaetzlich der Verlauf.
