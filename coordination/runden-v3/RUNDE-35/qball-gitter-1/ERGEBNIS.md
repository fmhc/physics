# QBALL-GITTER-1: Ergebnis (Code-Agent fuer die Leitung, Runde 35, explorativ)

- Gerechnet auf der .69 ueber kleintest.sh, nur Spuren cpu3 und cpu4, hoechstens zwei Laeufe zugleich.
- **Ablauf** (Zeiten per date):
  - Start 21:56:48 CEST.
  - Rauch 1 20:10:23 bis 20:10:30 UTC, Rauch 2 20:15:08 bis 20:15:17 UTC, Rauch 3 bis 20:17:35 UTC, Kurzprobe des
    Endcodes 20:20:15 UTC.
  - Plan ab 22:18:09 CEST. Eingefroren 22:20:24 CEST: PLAN.md.eingefroren-20261003-222024,
    code/*.eingefroren-20261003-222024, sha256 in code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe 20:20:24 bis 20:29:59 UTC, alle rc = 0, jeder in einem Abschnitt. Auswertung 20:29:59 bis 20:30:09 UTC.
  - Text ab 22:32:54 CEST.
- Alle Laeufe tragen die sha256 des eingefrorenen qgitter.py (a9eb7f30...). Die Auswertung traegt die von auswertung.py
  (f7126fb9...). Plan und Code wurden nach dem Einfrieren nicht geaendert.
- **Daten:**
  - lauf-69/: je Lauf .json (Kopf), .npz (Zeitreihen, Momentaufnahmen), .log
  - lauf-69/auswertung.json: Urteile
  - Bilder lauf-69/v_t.png, gamma_t.png, ladung_t.png, raumzeit_f1.png
  - lauf-69/beschreibung.json: beschreibende Zusatzzahlen nach dem Einfrieren (Selbstanzeige 6)
  - rauch-69/: Rauchlaeufe
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese,
  [E] hier gerechnet (synthetisch, keine Messdatenbestaetigung).

## 1. Ergebnis

1. **Der Q-Ball wird auf dem Gitter nie lichtschnell. Er wird hoechstens so schnell wie die schnellste Gitterwelle [E].**
   - Hoechste Schnelle 0,7834 / 0,8832 / 0,9392 bei h = 0,5 / 0,25 / 0,125. Die groesste Gruppengeschwindigkeit der
     linearen Gitterwellen ist 0,7808 / 0,8828 / 0,9395 [M].
   - Also gamma_max = 1,609 / 2,133 / 2,913 gegen gamma(v_g,max) = 1,600 / 2,129 / 2,918.
   - Mit doppeltem Feld kommt dasselbe heraus (1,609 / 2,131 / 2,906). Die Grenze haengt also nicht merklich von der
     Kraft ab (zwei Feldstaerken), sondern vom Gitter.
   - Der Kink aus NETZ-C-1 lag mit seinem Energie-gamma ueber gamma(v_g,max), mit der Schnelle bei h = 0,25 und 0,125
     ueber v_g,max. Der Q-Ball liegt auf v_g,max.
2. **Bis gamma = 1,5 ist der Ball relativistisch [E].**
   - Bei h = 0,125 gilt gamma M v = Q E t auf 0,88 % (bei gamma = 1,5), frueher auf 0,2 %.
   - Danach knickt gamma bei rund 90 % von gamma(v_g,max) ab. Dort beginnt der Ladungsverlust.
3. **Der Ball zerstrahlt, statt umzukehren [E].**
   - Ab gamma = 1,43 / 1,92 / 2,63 gibt er Ladung als Wellen nach hinten ab, mit seinem eigenen Vorzeichen.
   - Unter 50 % faellt seine Ladung bei t = 753 / 1091 / 1593, also schon vor dem Schnellemaximum. Bei t_max hat er
     noch 27 / 31 / 34 % seiner Ladung.
   - Danach wird der Rest langsamer und loest sich auf: Q_win < 5 % bei t = 1675 / 2499 / 3822. Die
     Bloch-Perioden waeren 2669 / 5339 / 10678.
   - Eine Umkehr sah ich nur einmal: beim doppelten Feld und h = 0,5 kehrt ein Rest mit 6,6 % der Ladung bei t = 908 um.
4. **Urteile:** eingetroffen G0, G1, G2; nicht eingetroffen G3, G4.
   - Die Proben mit halbem Zeitschritt und mit doppelt langer Kette geben dieselben Urteile.
5. **Uebertragung [H]:** Die Grenze folgt der linearen Gitterdispersion [E, drei h]. Diese gibt gamma(v_g,max) -> h^(-1/2),
   h in Compton-Laengen der Feldquanten [M, Abschnitt 3.4].
   - gamma ~ 1e11 (kosmische Strahlung [L]) verlangte in diesem 1D-Bild h < 1e-22 Compton-Laengen.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 22:20:24 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json.

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| G0 | ohne Feld: Drift < 1e-4 bis t = 500, Ladung 1e-10, Energie 1e-7 | 90 % | **eingetroffen** | Drift <= 1,2e-12, Ladung <= 8,9e-15, Energie <= 7,9e-15 (alle drei h, dt = 0,02) |
| G1 | h = 0,125: gamma M v = Q E t innerhalb 2 % bis gamma = 1,5 | 75 % | **eingetroffen** | max abs. Abweichung 0,88 % bei t = 226 (= t(gamma = 1,5), Kontinuum 223,6); -0,16 % bei t = 50, -0,22 % bei t = 100 |
| G2 | gamma_max(h) existiert, waechst mit 1/h, gamma_max(0,125) >= 1,5 gamma_max(0,5) | 70 % | **eingetroffen** | gamma_max 1,609 / 2,133 / 2,913 (t = 1076 / 1459 / 2008), Faktor 1,81; alle drei danach gefallen (Ende 1,06 / 1,20 / 1,40) |
| G3 | [H] Umkehr vor T_B mit >= 50 % Ladung (Bloch-artig) | 35 % | **nicht eingetroffen** | keine Umkehr; Ball zerfallen (Q_win < 5 %) bei t = 1675 / 2499 / 3822 vor T_B = 2669 / 5339 / 10678; Q_win < 50 % schon bei t = 753 / 1091 / 1593 |
| G4 | [H] gamma_max des Q-Balls >= Kink (1,78 / 2,61 / 3,86) | 50 % | **nicht eingetroffen** | 1,609 / 2,133 / 2,913, je 10 / 18 / 25 % darunter |

- **Bedeutung, wie vorab festgelegt:**
  - **"G1 und G2 treffen ein" ist ausgeloest.** Auf einem Gitter verhalten sich Q-Baelle relativistisch, aber nur bis zu
    einer Hoechstgamma, die von der Maschenweite abhaengt.
    - Im Netzbild heisst das: Teilchen lassen sich nicht beliebig beschleunigen.
    - Die Hoechstgamma ist hier die der schnellsten Gitterwelle, gamma_max ~ h^(-1/2).
    - Teilchen mit gamma ~ 1e11 [L] verlangten im 1D-Bild h < 1e-22 Compton-Laengen [H, Uebertragung von 1D].
  - **"G3 verfehlt, dafuer Ladungsverlust" ist ausgeloest: Der Ball zerstrahlt an der Gittergrenze.** Ablauf:
    1. Relativistische Beschleunigung: gamma liegt bei t = 200 um 0,3 % (h = 0,125) bzw. 5 % (h = 0,5) unter der
       Kontinuumskurve.
    2. Knick bei rund 0,90 gamma(v_g,max). Ab da gibt der Ball Ladung ab; sie bleibt als positiv geladene Welle hinter ihm
       zurueck (raumzeit_f1.png).
    3. Mit sinkender Ladung kriecht er bis an v_g,max heran. Er erreicht sie mit nur noch rund einem Drittel seiner Ladung.
    4. Danach verzoegert der Rest gleichmaessig (dv/dt = -8,7e-4 / -3,5e-4 / -1,4e-4) und verbreitert sich, bis weniger
       als 5 % der Ladung im Fenster +-10 liegen.
  - "G3 trifft ein" (Bloch-Pendeln des Balls) ist nicht ausgeloest.

## 3. Tabellen

### 3.1 Uebersicht (Hauptlaeufe dt = 0,02, Fenster 400)

- E aus Q0 E/M0. T_B = 2 pi/(h E). Q_win = Ladung in |x - X| <= 10.
- "Beginn Verlust" = erster Zeitpunkt mit Q_win < 0,99 Q0 (aus beschreibung.json).

| h | Q0 E/M0 | E | T_B | gamma_max (t_max) | v_max | v_g,max | Beginn Verlust: t, gamma | Q_win/Q0 bei t_max | t(Q_win < 0,5 Q0) | Ende (Q_win < 0,05 Q0) | Umkehr |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0,5 | 0,005 | 0,0047081 | 2669,1 | 1,609 (1076) | 0,7834 | 0,7808 | 282,5; 1,433 | 0,273 | 753 | 1674,5 | nein (v >= 0,334) |
| 0,25 | 0,005 | 0,0047076 | 5338,8 | 2,133 (1459) | 0,8832 | 0,8828 | 458,5; 1,915 | 0,305 | 1090,5 | 2498,5 | nein (v >= 0,556) |
| 0,125 | 0,005 | 0,0047074 | 10677,9 | 2,913 (2008) | 0,9392 | 0,9395 | 709,5; 2,631 | 0,339 | 1592,5 | 3821,5 | nein (v >= 0,701) |
| 0,5 | 0,01 | 0,0094162 | 1334,6 | 1,609 (460) | 0,7833 | 0,7808 | 162,5; 1,459 | 0,401 | 396 | 1016,5 | ja bei t = 907,7 mit Q_win = 0,066 Q0 (v_min -0,226) |
| 0,25 | 0,01 | 0,0094151 | 2669,4 | 2,131 (629) | 0,8830 | 0,8828 | 266; 1,951 | 0,449 | 585 | 1543,5 | nein (v >= 0,136) |
| 0,125 | 0,01 | 0,0094149 | 5339,0 | 2,906 (862,5) | 0,9389 | 0,9395 | 419,5; 2,678 | 0,505 | 869 | 2414,5 | nein (v >= 0,394) |

- Kein Lauf erreichte T_B: Alle endeten mit Status "zerfallen" (Plan Abschnitt 3).
- Bei h = 0,5 lief der Ball ueber T_B/2 hinaus, wie die Karte verlangt (1674,5 > 1334,6); Q_win bei T_B/2 = 0,157 Q0.
- Gitterball:
  - M0 = 2,28763 / 2,29589 / 2,29793 und Q0 = 2,42946 / 2,43852 / 2,44075
  - Kontinuum [M]: 2,2986 und 2,4416
- t_max/T_B = 0,40 / 0,27 / 0,19 (E1). Das Maximum liegt also nicht beim Zonenrand-Zeitpunkt 0,563 T_B des Plans
  (Abschnitt 7) [H verworfen fuer den Ball].
- Die Restladung bei t_max liegt fuer E2 hoeher (40 / 45 / 51 %): Bei staerkerem Feld bleibt weniger Zeit zum
  Abstrahlen.

### 3.2 G1 im Einzelnen (h = 0,125, Q0 E/M0 = 0,005)

| Groesse | Hauptlauf dt = 0,02 | dt = 0,01 | Kette 800 | Feld 0,01 (nur Vergleich) |
|---|---|---|---|---|
| t(gamma = 1,5) (Kontinuum 223,6 bzw. 111,8) | 226,0 | 226,0 | 226,0 | 113,0 |
| A = gamma M0 v/(Q0 E t) - 1 bei t = 50 | -0,157 % | -0,157 % | -0,157 % | -0,40 % |
| A bei t = 100 | -0,224 % | -0,224 % | -0,224 % | -0,76 % |
| max abs. A auf [20, t(1,5)] | 0,881 % (bei t = 226) | 0,881 % | 0,881 % | 0,973 % |
| Kontrolle Energieschwerpunkt | 0,884 % | 0,884 % | 0,884 % | 0,987 % |
| Kontrolle kinetischer Impuls P/(Q0 E t) - 1 | 0,448 % | 0,448 % | 0,448 % | 0,448 % |
| Q_win/Q0 bei t(1,5) | 0,999999 | 0,999999 | 0,999999 | 0,999995 |

- Die Abweichung waechst stetig und ist negativ: Der Gitterball ist bei gleichem Q E t etwas langsamer als der
  Kontinuumsball.
- Der kinetische Impuls bleibt nur halb so weit zurueck (0,45 %). Der Rest ist Geschwindigkeit je Impuls, also ein
  Gittereffekt der Traegheit [H].

### 3.3 gamma(t) gegen das Kontinuum sqrt(1 + (0,005 t)^2), in Klammern Q_win/Q0 (Hauptlaeufe E1)

| t | Kontinuum | h = 0,5 | h = 0,25 | h = 0,125 |
|---|---|---|---|---|
| 50 | 1,031 | 1,030 | 1,031 | 1,031 |
| 100 | 1,118 | 1,112 | 1,116 | 1,118 |
| 200 | 1,414 | 1,343 | 1,396 | 1,410 |
| 300 | 1,803 | 1,436 (0,976) | 1,709 | 1,779 |
| 400 | 2,236 | 1,445 (0,853) | 1,895 (0,9998) | 2,151 |
| 600 | 3,162 | 1,479 (0,637) | 1,930 (0,870) | 2,604 (0,99996) |
| 800 | 4,123 | 1,534 (0,462) | 1,960 (0,700) | 2,646 (0,943) |
| 1000 | 5,099 | 1,596 (0,317) | 2,009 (0,558) | 2,668 (0,809) |
| 1500 | 7,566 | 1,160 (0,082) | 2,129 (0,287) | 2,782 (0,541) |
| 2000 | 10,05 | - | 1,550 (0,130) | 2,912 (0,342) |
| 3000 | 15,03 | - | - | 1,885 (0,124) |

- Ohne Klammer: Q_win > 0,999 Q0.
- Ladungsbreite (rms im Fenster) bei h = 0,125: 1,69 bei t = 50, 0,60 bei t = 600 (Lorentz-Verkuerzung). Mit dem
  Ladungsverlust steigt sie auf 2,3 (t = 1500) und 5,6 (t = 3000).

### 3.4 Gittergrenze [M]

- Lineare Gitterwellen: Omega^2 = 1 + (2/h^2)(1 - cos k h), v_g = sin(k h)/(h Omega).
  - Das Maximum liegt bei cos(k* h) = [(h^2 + 2) - sqrt((h^2 + 2)^2 - 4)]/2.
  - Werte: v_g,max = 0,78078 / 0,88278 / 0,93945, k* = 1,83 / 2,71 / 3,92 (beschreibung.json).
- Fuer kleines h gilt 1 - v_g,max -> h/2 (hier 0,44 h / 0,47 h / 0,48 h), also gamma(v_g,max) -> h^(-1/2).
  - gamma(v_g,max) sqrt(h) = 1,13 / 1,06 / 1,03.
- Der Kink in NETZ-C-1 gab empirisch gamma_max ~ h^(-0,55); seine Endschnelle lag bei h = 0,25 und 0,125 ueber v_g,max,
  bei h = 0,5 knapp darunter.

### 3.5 Energie und Ladung (E1, Laufende bzw. bei t_max)

| h | Feldarbeit W bei t_max / Ende | E_win bei t_max | Energie ausserhalb bei t_max | Ladung Ende: geschluckt / im Fenster ausserhalb / im Ball | negative Ladung im Fenster (letzte Aufnahme) |
|---|---|---|---|---|---|
| 0,5 | 6,17 / 7,41 | 1,52 | 6,93 | 75,1 % / 19,9 % / 5,0 % | -9e-17 Q0 |
| 0,25 | 11,18 / 14,32 | 2,46 | 11,02 | 74,4 % / 20,6 % / 5,0 % | -2e-10 Q0 |
| 0,125 | 18,19 / 25,05 | 3,98 | 16,50 | 73,8 % / 21,2 % / 5,0 % | -2e-10 Q0 |

- Die abgegebene Ladung hat das Vorzeichen des Balls. Es entstehen keine Gegenladungen (Paare) in messbarer Menge.
- Bei t_max (h = 0,125) liegen 16,5 der 20,5 Energieeinheiten (Ruheenergie 2,30 plus Feldarbeit 18,19) ausserhalb des
  Balls, darin auch die Ruheenergie der abgegebenen Ladung.

### 3.6 Konvergenzproben

| Groesse | dt = 0,02 (Haupt) | dt = 0,01 | Kette 800 (dt = 0,02) |
|---|---|---|---|
| gamma_max h = 0,5 / 0,25 / 0,125 | 1,60905 / 2,13260 / 2,91255 | 1,60905 / 2,13262 / 2,91282 | - / - / 2,91255 |
| t_max h = 0,125 | 2008,0 | 2008,5 | 2008,0 |
| Zerfall h = 0,125 | 3821,5 | 3824,5 | 3821,5 |
| t(Q_win < 0,5) h = 0,125 | 1592,5 | 1591,5 | 1592,5 |
| Urteile G1 / G2 / G3 / G4 | e / e / n / n | e / e / n / n | e / e / n / n |

- Die lange Kette gibt fuer den Ball dieselben Zahlen auf 1e-12. Abstrahlung, die der Schwamm schluckt, wirkt also in
  diesen Laeufen nicht auf den Ball zurueck.
- Die Energieposten unterscheiden sich: W = 28,55 statt 25,05, weil das Feld laenger an der noch nicht geschluckten
  Abstrahlung arbeitet.

## 4. Kontrollen

- **G0-Pfad:** wie in der Urteilstabelle. Die Amplitude des ruhenden Balls schwankt um 1,8e-8 (Zeitschritt).
- **Newton:**
  - Rest 4,7e-16 / 3,2e-15 / 1,3e-14
  - phi_0 = 0,60778 / 0,60662 / 0,60635 (Kontinuum 0,60624)
- **Vorzeichen:** Der Ball mit psi ~ exp(+i omega t) (Q > 0) laeuft bei E > 0 nach +x, wie aus P = P_kan + a Q
  abgeleitet (Rauch 1 und 2, alle Hauptlaeufe).
- **Ladungsbilanz** Q_dom + Q_abs + Q_ab - Q0: <= 2,1e-14 relativ in allen Laeufen.
- **Energiebilanz mit der Feldarbeit,** R/M0 (Plan-Kontrolle <= 1e-4):

  | Lauf | h = 0,5 | h = 0,25 | h = 0,125 |
  |---|---|---|---|
  | E1, dt = 0,02 | 6,3e-6 | 9,4e-5 | **1,2e-3** |
  | E1, dt = 0,01 | 3,9e-7 | 5,9e-6 | 7,5e-5 |
  | E2, dt = 0,02 | 8,2e-6 | **2,0e-4** | **3,7e-3** |
  | E1, Kette 800 | - | - | **2,2e-3** |

  - Das Verhaeltnis dt1/dt2 ist 16,0 / 15,9 / 15,8. Es ist also der dt^4-Fehler des Integrators, und zwar auf der
    hochfrequenten Abstrahlung (Omega bis 16 bei h = 0,125).
  - Bezogen auf die Feldarbeit sind es 1e-4 (h = 0,125).
  - Die Kontrolle ist in vier Laeufen verfehlt (Selbstanzeige 4). Zwischen dt1 und dt2 aendert sich gamma_max um
    hoechstens 2,7e-4 und t_max um 0,5.
- **Fensterbuchfuehrung:**
  - Was beim Verschieben herausfiel: Energie <= 4,9e-9, Ladung <= 1,1e-9 (beides E2, h = 0,5). Die Schwaemme haben alles vorher geschluckt.
  - Kein Ball kam naeher als 90 an einen Schwamm (Sollort im Fenster).
- **Zweites Positionsmass (Energieschwerpunkt):** gamma_max 1,612 / 2,136 / 2,919 gegen 1,609 / 2,133 / 2,913;
  t_max 5 bis 14 spaeter.
- **Schnellefenster +-20 statt +-10:** gamma_max 1,609 / 2,132 / 2,912.
- **Fortsetzung bitgleich** (Rauch 2). In den Hauptlaeufen nicht gebraucht, jeder Lauf blieb unter 500 s.
- **Latten (v3):**
  - L1 kann scheitern: ja. G3 und G4 sind gescheitert, G1 und G2 haetten scheitern koennen.
  - L2 Gegenprobe: zweites Positionsmass, kinetischer Impuls, doppeltes Feld, lange Kette.
  - L3 Numerik: dt/2, Ladungsbilanz 2e-14, Energiebilanz mit dt^4-Gang.
  - L4 schon bekannt [L?]: Bloch-Schwingungen diskreter Solitonen in Gittern mit linearem Potential sind fuer die
    diskrete NLS beschrieben (Wellenleiter-Arrays, um 1999). Eine Schnellegrenze von Q-Baellen bei v_g,max kenne ich nicht
    aus der Literatur; nicht nachgeschlagen.
  - L5 Messbezug: keiner, synthetisch und 1D.

## 5. Selbstanzeigen

1. **Vor dem Einfrieren gesehen (Rauch 2, im Plan offengelegt):**
   - G1-Werte bis gamma = 1,1: A = -0,09 % bis -0,21 % bei h = 0,125
   - bei h = 0,5 und doppeltem Feld -3 % bei gamma = 1,11
   - Die Schwelle 2 % blieb.
2. **Messkorrektur vor dem Einfrieren:**
   - Der Schwerpunkt mit hartem Fenster driftete beim ruhenden Ball (5e-4 bis t = 50).
   - Ersetzt durch das glatte cos^2-Gewicht mit Iteration bis zur Konvergenz, R = 10 statt 8. Die G0-Schwelle blieb.
3. **Zeitschritt nach dem Rauch:** 0,02 statt 0,0125, wegen der Laufzeit. Die Probe 0,01 blieb.
   - Nach dem Planschreiben, vor dem Einfrieren:
     - Die Konvergenzschwelle des Schwerpunkts wurde relativ gesetzt (|dX| < 1e-12 max(1, |X|)), Plan Abschnitt 4
       angepasst.
     - Kurzprobe r4 (h = 0,25, t = 30, 20:20:15 UTC) lief fehlerfrei. Sie steht nicht im Plan.
     - Im Plan standen zuerst falsche Fensterzahlen fuer die Ruhe-Ladung ausserhalb (3,6e-4 aus Rauch 1 mit R = 8); vor
       dem Einfrieren berichtigt auf 3,1e-5 / 3,9e-5 (Rauch 2, R = 10).
4. **Energiebilanz-Kontrolle verfehlt** (<= 1e-4 M0, Plan Abschnitt 4): E1 h = 0,125 (1,2e-3), Kette 800 (2,2e-3), E2
   h = 0,125 (3,7e-3) und E2 h = 0,25 (2,0e-4).
   - Ursache ist der dt^4-Fehler (Faktor 16). Mit dt = 0,01 ist sie erfuellt (7,5e-5).
   - Kein Urteil haengt daran. E2 hat keine dt2-Probe.
5. **Zwischenauswertung:** 20:23:36 bis 20:24:03 UTC mit dem eingefrorenen auswertung.py auf die bis dahin fertigen
   Laeufe (rauch-69/zwischen/).
   - Zweck: Fehlersuche und frueher Textbeginn.
   - Danach wurde nichts geaendert. Sie lief auf cpu3 zwischen zwei Hauptlaeufen (Lock), also nie als dritter Lauf.
6. **Nach dem Einfrieren:** code/beschreibung.py (sha256 a3b7fa9a..., 20:31:55 UTC, cpu3) liefert nur beschreibende Zahlen,
   keine Urteile:
   - Beginn des Ladungsverlusts
   - v_g,max, Ladungsvorzeichen
   - Umkehr des Rests bei E2
   - Verzoegerung nach dem Maximum
7. **G3 ueber den Zerfallszweig:**
   - Die Laeufe enden bei Q_win < 0,05 Q0; keiner erreichte T_B. Was die abgegebene Ladung oder ein schwacher Rest danach
     tut (etwa eine spaete Bloch-Rueckkehr), ist nicht gerechnet.
   - Fuer G3 aendert das nichts: Q_win lag in allen drei E1-Laeufen schon vor t_max unter 0,5 Q0 (bei E2, h = 0,125 erst
     6,5 Zeiteinheiten danach).
   - Rueckkehr von Ladung in den Ball wurde nirgends gesehen.
8. **Q_win misst ein festes Fenster +-10.**
   - Ein Rest mit wenig Ladung wird breit; "zerfallen" heisst am Ende auch "zu breit fuer das Fenster".
   - Beim 50-%-Punkt war die rms-Breite 2,3 bis 3,2, der Ball lag also sicher im Fenster.
9. **G4 vergleicht ungleiche Masse:**
   - Kink-gamma aus der Energie bei F = 0,02 (Beschleunigung 2 pi F/8 = 0,016), Ball-gamma aus der Schnelle bei 0,005.
   - Weil gamma_max des Balls bei doppeltem Feld gleich bleibt (0,3 %), haengt das Urteil vermutlich nicht an der
     Kraft [H].
10. **Zahl faellt mit einer ableitbaren zusammen:** gamma_max des Balls ist gamma(v_g,max) der linearen Wellen [M] auf
    0,2 bis 0,5 %.
    - Das war vorab nicht festgelegt; die Karte erwartete ausdruecklich, dass ein nichtlineares Objekt darueber liegen
      kann.
    - Das G2-Urteil folgt aber aus dieser ableitbaren Zahl (Faktor 2,918/1,600 = 1,82). Warum der Ball genau bei v_g,max
      stehen bleibt, ist offen [H].
    - Moegliche Lesart: Der Ball strahlt resonant ab, wenn seine Schnelle die Gruppengeschwindigkeit seiner
      Traegerwellen erreicht. Der kleiner werdende Ball naehert sich dabei einer linearen Welle.
11. **Plan-Hypothese Zonenrand** (0,563 T_B) trifft fuer den Ball nicht zu (t_max = 0,19 bis 0,40 T_B).
12. **Kein Messbezug (L5):** synthetisch, 1D, ein omega. Die Uebertragung auf kosmische Strahlung ist [H].
    - Fuer die h^(-1/2)-Grenze gilt nur [M] fuer die lineare Dispersion; dass Baelle in 3D derselben Grenze folgen, ist
      nicht gerechnet.
13. **Zeitbox:** Start 21:56:48, Text ab 22:32:54 CEST, innerhalb von 120 min.

## 6. Einfach gesagt

Finn fragte, ob eingefangene Baelle auf Lichtgeschwindigkeit kommen: Auf einem Gitter nicht. Ein Q-Ball unter
gleichmaessiger Kraft beschleunigt zuerst genau so, wie es die Relativitaetstheorie sagt, wird aber hoechstens so
schnell wie die schnellste Welle, die das Gitter tragen kann (78, 88 bzw. 94 % der Lichtgeschwindigkeit; je feiner das
Gitter, desto naeher an 100 %). Schon kurz davor gibt er seine Ladung als Wellen nach hinten ab und erreicht die
Hoechstgeschwindigkeit nur noch mit etwa einem Drittel davon. Danach wird der Rest langsamer und loest sich auf, statt
wie ein Elektron im Kristall zurueckzupendeln. Lichtschnell wird er also nie, er zerstrahlt vorher.
