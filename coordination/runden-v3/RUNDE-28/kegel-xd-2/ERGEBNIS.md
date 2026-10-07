# KEGEL-XD-2: Ergebnis (Code-Agent fuer claude-primary, Runde 28, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6), 34 Aufrufe nach Plan, alle rc = 0:
  - ziel (2D-Radialprofil, Zielwerte) 04:45:40 bis 04:47:14 UTC, danach versiegelt
  - 32 Kegel-Laeufe 04:47:18 bis 05:04:01 UTC; der laengste dauerte 4 min 58 s (Grenze 600 s), kein Punkt abgebrochen
  - auswertung 05:04:22 UTC
  - dazu eine nachtraegliche Diagnose (diag_rest.py, nicht im Plan) 04:53 bis 04:54:38 UTC, siehe Kontrollen
- **Eingefroren** um 06:45:32 CEST, vor der ersten echten Rechnung:
  - PLAN.md.eingefroren-20261003-064532 (sha256 1817e3ba...)
  - code/kegel_xd2.py.eingefroren-20261003-064532 (sha256 f841bf15..., auf der .69 identisch und schreibgeschuetzt)
  - code/laufplan.20261003-064532.tar (Spurskripte, sha256 e701eba6...)
- **Zielwerte versiegelt:** lauf-69/ziel-2d.json (r--r--r--, sha256 5e6f8b91...), geschrieben 04:47:14 UTC, vier Sekunden
  vor dem ersten Kegel-Lauf. Die Auswertung liest die Datei; auf keiner Befehlszeile stand ein Zielwert.
- **Rohdaten:** lauf-69/ (32 Kegel-JSON, 34 Logs, ziel-2d.json). Urteile in lauf-69/urteile.json, Tabellen in
  lauf-69/auswertung.json. Rauchlaeufe: rauch-69/. Diagnose: diag-69/.
- Begonnen 06:31:36 CEST, geschrieben ab 07:07:31 CEST (date).
- **Einheiten:** Modell M1 (beta = 1/2), Masse 1. 2D-Ball Q = 200: R_halb(S = 1/2) = 6,32, kappa = 0,667, omega = 0,7449,
  E = 157,301, E - omega Q = 8,326.
- **Abkuerzungen:**
  - O(d; delta) = [E(+delta) - E(-delta)]/2, ungerader Teil
  - Delta E_1(d; delta) = erste Ordnung der Karte aus dem ebenen Profil
  - r(d; delta) = [O - Delta E_1]/|Delta E_1(0; delta)|, relative Abweichung
  - fein/grob: Polargitter dr = 0,1 / 0,16 mit dphi = pi/384 / pi/240; Rich. = Richardson (Ansatz h^2)

## Ergebnis zuerst

1. **Die 2D-Abweichung schrumpft wie delta^2.**
   - max_d |r| = 4,12 % (pi/3), 1,22 % (pi/6), 0,33 % (pi/12), jedes Mal bei d = 6,0, wo die Ballwand ueber der Spitze
     liegt.
   - Halbiert man delta, faellt das Maximum um den Faktor 3,37 bzw. 3,68 (Richardson 3,38 bzw. 3,75); reines delta^2
     gaebe 4.
   - Auch an jedem anderen Abstand bis 14,4 liegen die Faktoren nach Richardson zwischen 3,8 und 5,5, im Schwanz bei 4,3
     und 4,1.
2. **K2-0, K2-1 und K2-2 sind eingetroffen;** nach der Karte gilt Lesart (A).
   - Die erste Ordnung ist richtig.
   - Die 2D-Abweichung bei delta = pi/3 kommt aus hoeheren Ordnungen [H, numerisch gestuetzt].
3. **Die 4 % bei pi/3 sind kein Netzeffekt.** Der neue Kontinuumscode (Polarkoordinaten) trifft den ungeraden Teil der
   KEGEL-Q-Dreiecksnetze an allen 17 Abstaenden auf 0,029 % von |Delta E_1(0)|. Erlaubt waren 0,3 %.
4. **Gitter und Numerik tragen das Urteil.**
   - Der Gitterfehler von r ist fuer alle drei delta gleich (fein gegen grob 0,0215 %). Er sitzt also im Term erster
     Ordnung.
   - Richardson trifft die exakten Werte r(0) aus der Radialfamilie auf 1,5e-6 (in Einheiten von |Delta E_1(0)|).
   - Nach Richardson bleiben K2-1 und K2-2 im Bereich (1,219 % und 0,325 %, Verhaeltnis 3,75).
5. **Nachtrag ohne Urteil [nachtraeglich]:** Eine Extrapolation durch die drei delta (r = r0 + a delta^2 + b delta^4,
   Richardson-Werte) gibt fuer delta -> 0 an jedem d bis 9,6: |r0| = 0,012 % bei d = 6,0, sonst <= 0,0011 %. Dahinter
   ist schon |r(pi/3)| < 0,006 %.
   - In der Wandzone sind die Terme der naechsten Ordnung bei pi/3 gross: Bei d = 6,0 bzw. 7,2 sind sie 19 bzw. 49 % des
     delta^3-Terms.
   - Daher weichen dort die Faktoren von 4 ab.

## Vorab gegen Ausgang

Mechanisch nach PLAN.md Abschnitt 4 (lauf-69/urteile.json); alle Urteile auf dem feinen Gitter.

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| K2-0 | delta = pi/3: Kontinuumscode trifft den ungeraden Teil der KEGEL-Q-Gitterwerte (h = 0,2) an allen 17 d auf 0,3 % von \|Delta E_1(0)\| | 80 % | **eingetroffen**: Schranke 4,16e-3; groesste Abweichung 4,0e-4 bei d = 2,4 (0,029 %) |
| K2-1 | delta = pi/6: max_d \|r\| zwischen 0,6 % und 1,6 % | 65 % | **eingetroffen**: max \|r\| = 1,225 % bei d = 6,0 |
| K2-2 | delta = pi/12: max_d \|r\| zwischen 0,15 % und 0,45 %, Verhaeltnis max\|r(pi/6)\|/max\|r(pi/12)\| zwischen 3 und 5,5 | 60 % | **eingetroffen**: max \|r\| = 0,333 % bei d = 6,0; Verhaeltnis 3,68 |

- **Mechanischer Fall:** "A: K2-1 und K2-2 eingetroffen".
- **Ableitbarkeit:**
  - r(0; delta) folgt exakt aus der Radialfamilie (-0,318 / -0,079 / -0,020 %). Dieser Wert stand im ziel, bevor die Laeufe
    endeten. Er ist aber nicht das Maximum.
  - Das Maximum in der Wandzone war bei pi/6 und pi/12 nirgends gerechnet und konnte scheitern.
  - K2-0 vergleicht zwei unabhaengige Codes (Dreiecksnetz gegen Polargitter). Er haette bei einem Fehler im neuen Code oder
    einer anderen Lagedefinition scheitern koennen.

**Bedeutung (nach Karte, Fall "K2-1 und K2-2 treffen ein"):**
- Lesart (A): Die erste Ordnung ist richtig, die 2D-Abweichung bei delta = pi/3 sind hoehere Ordnungen
  [H, numerisch gestuetzt].
- **Beschreibung:**
  - Das Kopplungsgesetz Delta E_1(d) = -delta Int_0^inf r g(d + r) dr gilt damit in 2D wie in 3D (KEGEL-XD) als erste
    Ordnung im Defizit [H, numerisch gestuetzt].
  - Die Abweichung bei endlichem delta sitzt dort, wo die Ballwand ueber die Spitze laeuft (d = 4,8 bis 8,4). Dort reagiert
    der Ball vermutlich stark nichtlinear, weil die Wand zur Fuenfer-Spitze hin ausbeult (KEGEL-Q) [H].
  - Im Schwanz ist es ein fester Faktor: O/Delta E_1 = 1,10 / 1,023 / 1,005 bei d = 12 (pi/3, pi/6, pi/12). Auch der
    Ueberschuss faellt wie delta^2 (Faktoren 4,3).
  - Die 3-%-Schranke von KX1 (KEGEL-XD) war fuer delta = pi/3 zu eng; ein Fehler der Herleitung liegt nicht vor
    [H, numerisch gestuetzt].
- Nur als grobe Einordnung ueber die Dimension hinweg [H]: Die 2D-Skalierung, auf delta = 0,1284 (Fuenfer-Kante im
  Tetraederraum) uebertragen, gaebe 4,1 % x (0,1284/1,047)^2 = 0,06 %. KEGEL-XD mass in 3D <= 0,081 % (fein) bzw.
  <= 0,044 % (Richardson), bei anderer Dimension und Ballgroesse.

## Tabelle r(d; delta) fuer alle drei delta

- r in Prozent von \|Delta E_1(0; delta)\|.
- Delta E_1(0) = -1,387728 / -0,693864 / -0,346932 (pi/3, pi/6, pi/12). Das sind -delta/(2pi) (E - omega Q) fuer
  dr = 0,01; dr = 0,005 aendert Delta E_1 um <= 1,4e-6.
- "KQ" = r aus den KEGEL-Q-Daten (h = 0,2), wie in KEGEL-XD Teil A.
- Verhaeltnisse aus den Richardson-Werten: 3:6 = r(pi/3)/r(pi/6), 6:12 = r(pi/6)/r(pi/12). Unter reinem delta^2 ist
  beides 4.

| d | Delta E_1(pi/3) | r(pi/3) fein | r(pi/3) KQ | r(pi/6) fein | r(pi/12) fein | r(pi/3) Rich. | r(pi/6) Rich. | r(pi/12) Rich. | 3:6 | 6:12 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | -1,387728 | -0,3047 | -0,2771 | -0,0652 | -0,0061 | -0,3185 | -0,0790 | -0,0198 | 4,03 | 3,99 |
| 1,2 | -1,345305 | -0,1351 | -0,1064 | -0,0251 | +0,0023 | -0,1467 | -0,0367 | -0,0093 | 4,00 | 3,96 |
| 2,4 | -1,218036 | -0,2906 | -0,2617 | -0,0696 | -0,0113 | -0,2991 | -0,0781 | -0,0198 | 3,83 | 3,94 |
| 3,6 | -1,005987 | -0,3897 | -0,3643 | -0,0964 | -0,0202 | -0,3951 | -0,1019 | -0,0258 | 3,88 | 3,95 |
| 4,8 | -0,710835 | -0,8669 | -0,8616 | -0,1584 | -0,0346 | -0,8690 | -0,1592 | -0,0354 | 5,46 | 4,49 |
| 6,0 | -0,361965 | **-4,1243** | -4,1389 | **-1,2246** | **-0,3325** | -4,1245 | -1,2193 | -0,3248 | 3,38 | 3,75 |
| 7,2 | -0,107227 | -3,7622 | -3,7777 | -0,7018 | -0,1539 | -3,7656 | -0,7095 | -0,1622 | 5,31 | 4,37 |
| 8,4 | -0,021837 | -0,2667 | -0,2754 | -0,0557 | -0,0115 | -0,2699 | -0,0584 | -0,0141 | 4,62 | 4,13 |
| 9,6 | -4,017e-3 | -0,0315 | -0,0333 | -0,0070 | -0,0014 | -0,0319 | -0,0074 | -0,0018 | 4,30 | 4,06 |
| 10,8 | -7,31e-4 | -5,3e-3 | -5,7e-3 | -1,2e-3 | -2,7e-4 | -5,4e-3 | -1,3e-3 | -3,1e-4 | 4,27 | 4,06 |
| 12,0 | -1,34e-4 | -9,8e-4 | -1,05e-3 | -2,3e-4 | -5,2e-5 | -9,9e-4 | -2,3e-4 | -5,7e-5 | 4,27 | 4,07 |
| 13,2 | -2,47e-5 | -1,8e-4 | -2,0e-4 | -4,3e-5 | -1,1e-5 | -1,8e-4 | -4,3e-5 | -1,1e-5 | 4,27 | 4,07 |
| 14,4 | -4,6e-6 | -3,5e-5 | -3,7e-5 | -8e-6 | -2e-6 | -3,4e-5 | -8e-6 | -2e-6 | 4,25 | 3,98 |
| 15,6 | -8,6e-7 | -6e-6 | -7e-6 | -2e-6 | < 1e-6 | -7e-6 | -2e-6 | -1e-6 | (n. a.) | (n. a.) |
| 16,8 | -1,6e-7 | -1e-6 | -1e-6 | < 1e-6 | < 1e-6 | -2e-6 | -1e-6 | < 1e-6 | (n. a.) | (n. a.) |
| 18,0 | -3,1e-8 | < 1e-6 | < 1e-6 | < 1e-6 | < 1e-6 | -1e-6 | < 1e-6 | < 1e-6 | (n. a.) | (n. a.) |
| 19,2 | -5,8e-9 | < 1e-6 | < 1e-6 | < 1e-6 | < 1e-6 | -1e-6 | -1e-6 | -1e-6 | (n. a.) | (n. a.) |

- Ab d = 15,6 ist O kleiner als 1e-6 und r kleiner als 1e-5 %. Dort ist O - Delta E_1 nicht groesser als der
  Gitterfehler (fein gegen Richardson ~1e-8 von \|Delta E_1(0)\|); die Verhaeltnisse (1,0 bis 4,0) sind nicht
  aussagekraeftig (n. a.).
- r(pi/3) fein und KQ unterscheiden sich um hoechstens 0,029 % (K2-0). Bei d = 6,0 und 7,2 liegen beide bei 4,1 und
  3,8 %, wie in KEGEL-XD.

**Kraefte (beschreibend).** Ungerader Teil der Multiplikator-Kraft gegen d(Delta E_1)/dd, relative Abweichung:

| d | pi/3 | pi/6 | pi/12 |
|---|---|---|---|
| 1,2 / 2,4 / 3,6 | -0,5 / -1,6 / +0,07 % | -0,2 / -0,45 / +0,07 % | -0,10 / -0,13 / +0,01 % |
| 4,8 | -7,0 % | -1,5 % | -0,35 % |
| 6,0 | -14,5 % | -4,9 % | -1,25 % |
| 7,2 | +43,8 % | +13,7 % | +3,4 % |
| 8,4 | +26,5 % | +5,4 % | +1,4 % |

- Auch die Kraftabweichung faellt etwa wie delta^2 (Faktoren 3 bis 5 je Halbierung, ab d = 4,8).

## Gerader Teil P(d; delta) = [E(+delta) + E(-delta)]/2 - E_flach(d) (nur berichtet)

- E_flach(d) aus dem flachen Lauf (k = 0) am selben d auf demselben Gitter (fein).

| d | P(pi/3) | P(pi/6) | P(pi/12) | P3/P6 | P6/P12 |
|---|---|---|---|---|---|
| 0 | -0,054352 | -0,013501 | -0,003370 | 4,03 | 4,01 |
| 1,2 | -0,078657 | -0,019666 | -0,004917 | 4,00 | 4,00 |
| 2,4 | -0,117818 | -0,029419 | -0,007352 | 4,00 | 4,00 |
| 3,6 | -0,161739 | -0,040074 | -0,009995 | 4,04 | 4,01 |
| 4,8 | -0,202736 | -0,051452 | -0,012902 | 3,94 | 3,99 |
| 6,0 | -0,188759 | -0,048411 | -0,012202 | 3,90 | 3,97 |
| 7,2 | -0,088427 | -0,015957 | -0,003674 | 5,54 | 4,34 |
| 8,4 | -9,70e-3 | -2,13e-3 | -5,17e-4 | 4,56 | 4,12 |
| 9,6 | -1,445e-3 | -3,36e-4 | -8,25e-5 | 4,31 | 4,07 |
| 10,8 | -2,54e-4 | -5,9e-5 | -1,46e-5 | 4,28 | 4,07 |
| 12,0 bis 19,2 | <= 4,7e-5 | <= 1,1e-5 | <= 2,7e-6 | 4,28 bis 4,36 | 4,06 bis 4,07 |

- P ist O(delta^2), wie es sein muss.
- Bei pi/3 erreicht P 14,6 % von \|Delta E_1(0)\| (d = 4,8), gleich wie die KEGEL-Q-Daten in KEGEL-XD (-0,2024).
- P ist an allen d und fuer alle delta negativ: Der Ball spart am Fuenfer-Kegel mehr, als er am Siebener-Kegel zahlt.

## Kontrollen

- **d = 0 gegen die exakte Kegelabbildung** E_eben(sQ)/s - E_eben(Q), alle sechs Defizite:
  - fein +0,0134 bis +0,0138 % (\|Delta E\| zu klein), grob +0,035 %. Verhaeltnis 2,58 bei Soll 1,6^2 = 2,56.
  - Auf dem Polargitter ist der zentrierte Ball exakt das Radialgitter mit dr. Die Abweichung ist also der radiale
    Diskretisierungsfehler.
- **Exaktes r(0)** aus der Radialfamilie: -0,3183 / -0,0789 / -0,0197 % (Verhaeltnisse 4,04 und 4,01).
  - Richardson trifft das auf <= 2e-4 % (-0,3185 / -0,0790 / -0,0198 %).
  - Fein allein liegt um +0,014 % daneben, gleich fuer alle delta.
- **Gitterfehler:**
  - max_d \|r_fein - r_grob\| = 2,150e-4 / 2,146e-4 / 2,145e-4 fuer pi/3, pi/6, pi/12, also unabhaengig von delta.
    Der Fehler steckt im Term erster Ordnung (O ~ delta mal Gitterfehler von J_1).
  - max_d \|r_fein - r_Rich\| = 1,38e-4. Das sind 4 % von max\|r(pi/12)\|.
  - Das Urteil K2-2 haelt nach Richardson (0,325 %, Verhaeltnis 3,75).
- **Gitterinterne Probe ohne Delta E_1 [nachtraeglich]:** Q3 = [O(pi/3) - 2 O(pi/6)]/[O(pi/6) - 2 O(pi/12)] ist 8 fuer
  einen reinen delta^3-Term. Der Gitterfehler erster Ordnung hebt sich darin heraus, soweit er linear in delta ist.
  - Gemessen: 8,09 / 8,04 / 7,59 / 7,70 (d = 0 bis 3,6); 11,45 / 6,50 / 11,17 / 9,57 (4,8 bis 8,4); 8,67 bis 8,75 (9,6
    bis 19,2).
  - Fein, grob und Richardson stimmen bis d = 16,8 auf <= 0,5 %.
  - Diese Probe prueft nur die Reihe in ungeraden Potenzen, nicht Delta E_1 selbst.
- **Flache Laeufe (Scheinkraft des Polargitters):**
  - E_flach(d) steigt von 157,29916 (d = 0) auf 157,30026 (d = 7,2) und faellt auf 157,29866 (d = 19,2): Spanne 1,6e-3
    (fein), 4,1e-3 (grob, Verhaeltnis 2,56).
  - Die Scheinkraft betraegt also ~1e-4. Sie ist gerade in delta und faellt aus O heraus; in P ist sie abgezogen.
- **Randprobe** (grob, r_max = 48 statt 40; k = +-4 und +-1; d = 7,2 und 19,2):
  - O aendert sich um <= 5e-12 (<= 4e-12 von \|Delta E_1(0)\|).
  - E selbst aendert sich bei d = 19,2 um -2,2e-8, gleich fuer beide Vorzeichen.
- **Konvergenz** (238 Punkte Haupt und flach, dazu 8 Randpunkte):
  - Nebenbedingungsrest \|c\| <= 1,4e-6, d_W trifft d auf <= 2,4e-6
  - kein Punkt abgebrochen; 94 bis 1468 Funktionsaufrufe; laengster Punkt 88 s
  - Feld am aeusseren Rand <= 7,3e-6
- **Restgradient bis 1,5e-3**, nachtraegliche Diagnose (diag_rest.py, nicht im Plan; importiert den eingefrorenen Code
  unveraendert):
  - Bei k = +4, d = 6,0 und 9,6 sitzt das Maximum in der innersten Zellreihe an der Spitze (r = 0,05, am hinteren Spiegel).
  - Ausserhalb r = 0,5 ist der Rest <= 2,6e-5. Die Energie darin ist nach einem Diagonal-Newton-Schritt <= 2e-14.
  - 400 rot-schwarze Gauss-Seidel-Durchgaenge senken den Rest auf 3e-6 bzw. 1,3e-5. E_korr aendert sich dabei um
    -2,6e-13 bzw. -1,9e-12.
  - Die Diagnose hat beide Punkte neu gerechnet: E_korr ist bitgleich mit dem Hauptlauf.
- **Zielwerte:** dr = 0,005 aendert Delta E_1 um <= 1,4e-6. Impulsfluss-Probe Int g drho = -3,7e-15 relativ.
  Delta E_1(0; pi/3) = -1,387728, wie in KEGEL-XD.
- **Unveraendert seit dem Einfrieren:**
  - PLAN.md = PLAN.md.eingefroren-20261003-064532 (1817e3ba...)
  - kegel_xd2.py = Eingefrorenes = .69-Kopie = Rauchlauf-Code kegel_xd2_rauch1.py (f841bf15...)
  - ziel-2d.json lokal = .69 (5e6f8b91...)
- **Eingaben KEGEL-Q** (sha256 lokal = .69 = KEGEL-XD):
  - kraft-n5-h0.2-Q200-a 9cc1223d..., -b 8357104b...
  - kraft-n7-h0.2-Q200-a bd8acefb..., -b 19db4f8d...

## Latten (v3)

- **L1: ja.**
  - K2-1 und K2-2 konnten scheitern: Unter (B) waere r bei ~4 % geblieben. Gerechnet war die Wandzone bei pi/6 und pi/12
    nirgends.
  - K2-0 konnte an einem Fehler des neuen Codes scheitern.
  - Ableitbar war nur r(0) (exakte Abbildung), nicht das Maximum.
- **L2: ja.**
  - zwei Gitter mit Richardson; d = 0 gegen die exakte Abbildung bei sechs Defiziten
  - zweiter Code (KEGEL-Q-Netz) bei pi/3
  - Randprobe, flache Laeufe an jedem d
  - Multiplikator-Kraft gegen d(Delta E_1)/dd
  - gitterinterne delta^3-Probe; Restgradient-Diagnose mit Nachrechnung
- **L3: ja.**
  - Gitterfehler in r 2,2e-4 (fein gegen grob) bzw. 1,4e-4 (fein gegen Richardson) bei einem Signal von 3,3e-3 (pi/12)
  - Randeinfluss auf O 5e-12; Konvergenz von E 1e-12
- **L4: teilweise.**
  - Dass ein Kegeldefekt in erster Ordnung ueber -1/2 Int T^ij h_ij koppelt und hoehere Ordnungen mit delta^2 relativ
    folgen, ist Standard der Stoerungsrechnung [L?, nicht nachgelesen].
  - Zur kosmischen Saite (Vilenkin 1981; Linet 1986; Smith 1990) gilt weiter [L?, nicht gelesen].
  - Neu ist nur der Befund fuer Q-Baelle an einer 2D-Kegelspitze.
- **L5: nein.** Kein Messbezug. Moegliche Bruecke wie in KEGEL-XD [H]: Kegeldefekte (Fuenfer-Ecken, Disklinationen,
  Saiten) binden Feldklumpen kurzreichweitig nur ueber deren Spannungstensor.

## Selbstanzeigen

1. **Nachtraegliche Diagnose ausserhalb des Plans:**
   - diag_rest.py habe ich nach dem Einfrieren geschrieben, weil der Restgradient bei k = +4 bis 1,5e-3 stieg (im
     Rauchlauf 4,8e-4).
   - Sie lief ueber die Spur cpu und verzoegerte dort f-m2-c um etwa 1,5 min.
   - Am Code, an den Laeufen und an den Urteilen aendert sie nichts.
2. **Rauchlaeufe** (k = +-3, d.h. delta = pi/4, und flach, Q = 150, je <= 52 s) zeigten nur Laufzeit und Konvergenz. Mit
   der Formel habe ich sie nicht verglichen. Beim ersten Start gingen drei von vier Aufrufen wegen eines Shell-Fehlers nicht
   los (Plan, Abschnitt 7).
3. **Zwischenblick:** Um 06:53 CEST habe ich r(pi/3) und K2-0 aus den ersten fertigen Laeufen angesehen, bevor die
   pi/6- und pi/12-Laeufe fertig waren. Die Laeufe standen da schon fest (eingefrorene Spurskripte); geaendert habe ich
   nichts.
4. **Textfilter:** Auf der .69 lief kein Interpreter ausserhalb der Spur (kein python, kein awk).
   - In zwei Befehlen habe ich dort sed als einfachen Zeilenfilter benutzt (Praefix setzen, Zeile kuerzen).
   - Einer davon steckte in der Ueberwachungsschleife und lief alle 30 s, bis die Laeufe fertig waren.
   - Lokal lief kein Interpreter, auch sed nur fuer einfache Ersetzungen; die Tabellen kommen aus jq.
5. **Geteilter Scratchpad:** Dort habe ich eine vorhandene Datei tab.jq ueberschrieben (Herkunft unbekannt) und danach in
   kxd2-tab.jq umbenannt. Ihr alter Inhalt ist verloren.
6. **Deutungen [H] und Nachtraege:** Die Extrapolation r0, die Q3-Probe, die Kraft- und P-Verhaeltnisse und die Aussage
   zum Tetraederraum sind nachtraeglich. Sie sind kein Urteil; eine neue Formel stelle ich nicht auf.

## Einfach gesagt

Die Leitung hatte eine Formel, die sagt, wie stark ein Feldklumpen von der Spitze eines flachen Kegels angezogen oder
weggeschoben wird; sie gilt streng nur fuer kleine Spitzen. Bei einer grossen Spitze (60 Grad Luecke) lag sie genau dort, wo
der Rand des Klumpens ueber die Spitze rutscht, um 4 Prozent daneben. Jetzt haben wir die Luecke auf 30 und 15 Grad
verkleinert: Die Abweichung fiel von 4,1 auf 1,2 und dann auf 0,33 Prozent, also bei jeder Halbierung auf etwa ein Viertel.
So verhaelt sich ein Korrekturglied, das nur bei grossen Luecken zaehlt; die Formel selbst ist also richtig.
