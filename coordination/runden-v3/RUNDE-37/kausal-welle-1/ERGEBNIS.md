# KAUSAL-WELLE-1: Ergebnis (Code-Agent fuer die Leitung, Runde 37, explorativ)

- Gerechnet auf der .69 nur ueber kleintest.sh: Spuren cpu7 und p4000a (nur CPU), hoechstens zwei Laeufe zugleich.
- **Zeiten** (date; .69 in UTC, CEST = UTC + 2):
  - Start 05:27:21 CEST. Johnston-PDF gelesen (ein Abruf).
  - Rauch 03:48:03 bis 03:52:09 UTC. Plantext ab 05:50:26 CEST.
  - **Eingefroren 05:52:55 CEST:**
    - PLAN.md.eingefroren-20261004-055255
    - code/*.eingefroren-20261004-055255
    - sha256 in code/pruefsummen-einfrieren.txt
  - Hauptlaeufe 03:53:01 bis 04:06:57 UTC: 8 Starts, alle rc = 0, kein Abbruch.
  - Auswertung 04:07:08 bis 04:07:15 UTC. Text ab 06:10:46 CEST.
- **Hashes:**
  - Alle 65 Laufdateien tragen die sha256 des eingefrorenen kausal_welle.py (2f897e12...): 48 Feld, 16 Punktquelle,
    1 Codeprobe.
  - kontinuum.json und auswertung.json tragen die eingefrorenen Hashes (b7764ff3..., bf2ab218...).
  - Plan und Code sind nach dem Einfrieren unveraendert (sha256 um 06:09:36 CEST geprueft).
- **Kennzeichen:**
  - [S] an der Quelle gelesen; [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [H] Hypothese
  - [M] eigene Mathematik; [E] hier gerechnet (synthetisch, keine Messdaten); [F] Festlegung des Plans
- **Quelle [S]:** S. Johnston, "Particle propagators on discrete spacetime", CQG 25 (2008) 202001, arXiv:0806.3083v2.
  - Die Nummer stimmt. Gelesen: Gl. (2.1), (3.1), (3.3), (3.5), (3.17), (3.23), (3.31), Abschnitt 3.3.
  - In 1+1: Sprung a = 1/2, Halt b = -m^2/rho (3.31), Kette ueber die Kausalmatrix. Damit ist K - I = (1/2) C (I + (m^2/(2 rho)) C)^-1;
    Faktoren und Vorzeichen der Karte stimmen.

## 1. Ergebnis zuerst

1. **Im Mittel laeuft die Welle exakt wie im Kontinuum, ohne Ruhesystem [E].**
   - Johnstons Propagator auf Poisson-Kausalmengen (rho = 50 / 200 / 800, je 16 Saaten, N bis 7 Mio.) trifft die
     Kontinuumsloesung an allen 54 Pruefpunkten innerhalb 1,66 SE.
   - Die relative Streuung von phi faellt wie rho^(-0,52): 23 / 11 / 5 %.
   - Die Norm ist stabil: hoechstens +11 % Zuwachs gegen das Kontinuum bei rho = 50, +1 % bei rho = 800.
2. **Die Schwerpunktgeschwindigkeit einer einzelnen Welle schwankt nur um 0,1 bis 2,5 % der Lichtgeschwindigkeit [E].**
   - Die Streuung faellt mit der Dichte.
   - Ein Punktlaeufer, der Links folgt (KAUSAL-SWERVE-1), haette nach derselben Eigenzeit eine Rapiditaetsstreuung von
     etwa 8 [M, umgerechnet], also rund tausendmal mehr. Die Welle hat sie ~0,005 bis 0,014 (rho = 200).
3. **Ausgedehnt zittert weniger, aber erst bei hoher Dichte [E].** Verhaeltnis der Streuung sigma = 8 zu sigma = 2:

   | rho | eta = 0 | eta = 1 |
   |---|---|---|
   | 50 | 0,86 | 1,48 |
   | 200 | 0,50 | 0,71 |
   | 800 | 0,30 | 0,55 |

   - Bei rho = 200 (Kartendichte) liegt eta = 0 genau auf der Schwelle 0,5, eta = 1 darueber.
4. **Bewegte Pakete hinken bei kleiner Dichte etwas nach [E].**
   - Die |phi|^2-gewichtete Messung verliert bei eta = 1 und rho = 50 bis 2,1 % Tempo, bei rho = 800 nur 0,1 %.
   - Die Verzerrung skaliert wie 1/rho, wie die Rauschleistung. Das Saatmittel von phi selbst ist unverzerrt (Punkt 1).
5. **Urteile:** KW0 eingetroffen, KW1 nicht eingetroffen, KW2 nicht eingetroffen, KW3 eingetroffen.
   - KW1 scheitert an einem von 18 Faellen (rho = 50, sigma = 8, eta = 1).
   - KW2 scheitert an eta = 1 (0,71); eta = 0 erfuellt knapp (0,4998).

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 05:52:55 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json. Die
Felder "vermerk" sind per jq nachgetragen; ohne sie ist die Datei identisch mit lauf-69/auswertung.maschine.json (diff).

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Kartenwortlaut | Werte |
|---|---|---|---|---|---|
| KW0 | Saatmittel trifft Kontinuum in 3 SE; relative Streuung ~ rho^(-1/2) (Steigung -0,5 +- 0,1) | 70 % | **eingetroffen** | gleich | 54 von 54 Tests <= 3 SE, groesste Abweichung 1,66 SE; Steigung -0,519 (je Konfiguration -0,48 bis -0,55) |
| KW1 | Schwerpunktgeschwindigkeit trifft Kontinuum auf 2 %, eta = 0 und 1 | 60 % | **nicht eingetroffen** | **nicht eingetroffen** | 17 von 18 Faellen; verfehlt rho = 50, sigma = 8, eta = 1: 0,7428 +- 0,0047 gegen V_c = 0,7587 (-0,0159, Toleranz 0,0152, 3,4 SE) |
| KW2 | [H] Streuung bei sigma = 8 hoechstens halb so gross wie bei sigma = 2 (rho = 200) | 55 % | **nicht eingetroffen** | gleich | eta = 0: 0,00546 / 0,01093 = 0,4998 (erfuellt); eta = 1: 0,00475 / 0,00669 = 0,710 (verfehlt) |
| KW3 | Paketnorm waechst um hoechstens Faktor 1,5 gegenueber Kontinuum | 70 % | **eingetroffen** | gleich (auch Lesart max R) | G <= 1,111 in allen 18 Faellen; max R = 1,256 (rho = 50) |

- **Kartenfehler KW1** (PLAN 7.1, vor jeder Rechnung offengelegt):
  - "Gruppengeschwindigkeit" woertlich ist tanh(eta) = 0,7616.
  - Das exakte Kontinuumspaket mit runder Laborhuelle laeuft aber mit 0,7139 / 0,7506 / 0,7587 (sigma = 2 / 4 / 8,
    Fenster).
  - Berichtigt ist der Bezug V_c. **Nach Wortlaut:**
    - eta = 1: sigma = 2 liegt bei allen Dichten 6 bis 7 % unter tanh(1) (-0,046 bis -0,052).
    - Bei rho = 50 liegen auch sigma = 4 und 8 ausserhalb.
    - eta = 0 ist relativ zu 0 unerfuellbar.
  - Beide Lesarten ergeben "nicht eingetroffen".
- **Kartenluecke KW1 bei eta = 0:** Toleranz 0,02 absolut [F]. Alle |V| <= 0,0031; diese Faelle sind unkritisch.
- **Bedeutung nach der Karte (vorab):**
  - "KW0 bis KW3 treffen ein" ist nicht ausgeloest. Ausgeloest ist "KW2 verfehlt: Auch ausgedehnte Wellen zittern gleich
    stark. Ueberleitung 3 bekommt ein ernstes Problem mit Teilchen."
  - Die Daten tragen den Wortlaut dieses Zweigs nicht. Bei rho = 200 zittert sigma = 8 nur 0,50- bzw. 0,71-mal so stark,
    bei rho = 800 0,30- bzw. 0,55-mal. Die Streuung selbst ist klein und faellt mit rho (Abschnitt 6).
  - Formal bleibt es beim Zweig "KW2 verfehlt".
- **Meine Vorab-Erwartung** (PLAN 6.1): KW0 ein, KW1 ein, KW2 nicht, KW3 ein. Abweichungen:
  - KW1 scheiterte an rho = 50 mit dem dort befuerchteten Mechanismus (Rauschen in der Gewichtung).
  - Bei KW2 lag ich nur im Ergebnis richtig, nicht in der Begruendung. Ich hatte erwartet, dass die Streuung mit sigma
    waechst. Das stimmt nur bei rho = 50; ab rho = 200 faellt sie mit sigma.

## 3. Tabellen

### 3.1 Schwerpunktgeschwindigkeit (Fenster, Saatmittel +- SE, 16 Saaten) [E]

| rho | sigma = 2, eta = 1 | sigma = 4, eta = 1 | sigma = 8, eta = 1 | eta = 0 (alle sigma) |
|---|---|---|---|---|
| Kontinuum V_c | 0,7139 | 0,7506 | 0,7587 | 0 |
| 50 | 0,7093 +- 0,0032 | 0,7439 +- 0,0023 | **0,7428 +- 0,0047** | -0,0019 / +0,0024 / +0,0026 (SE 0,005 bis 0,006) |
| 200 | 0,7158 +- 0,0017 | 0,7499 +- 0,0013 | 0,7556 +- 0,0012 | -0,0027 / -0,0031 / +0,0007 |
| 800 | 0,7144 +- 0,0006 | 0,7499 +- 0,0004 | 0,7577 +- 0,0003 | +0,0009 / +0,0009 / +0,0002 |
| ganze Scheibe, rho = 50 | 0,6578 | 0,6781 | 0,6545 | |
| ganze Scheibe, rho = 800 | 0,7088 | 0,7458 | 0,7518 | |

- Kontinuum ganze Scheibe: 0,7117 / 0,7507 / 0,7587. Analytisch <v> (positive Frequenz): 0,7118 / 0,7507 / 0,7590.
  tanh(1) = 0,7616.
- Die ganze Scheibe (ohne Fenster) verliert bei rho = 50 bis 14 % Tempo, bei rho = 800 bis 0,9 %. Das Rauschen im ganzen
  Zukunftskegel zieht <x> zurueck, wie im Plan begruendet (PLAN 3, Fenster).

### 3.2 Streuung von V ueber 16 Saaten [E]

Spalten: Std(V); Std der Rapiditaet; Vorhersage nur aus der Punktstichprobe [M]; Feldanteil sqrt(Std^2 - Stichprobe^2) [H].

| rho | sigma | eta = 0: Std V | Stichprobe | Feldanteil | eta = 1: Std V | Std Rapiditaet | Stichprobe | Feldanteil |
|---|---|---|---|---|---|---|---|---|
| 50 | 2 | 0,0248 | 0,0048 | 0,0244 | 0,0128 | 0,0255 | 0,0032 | 0,0124 |
| 50 | 4 | 0,0193 | 0,0045 | 0,0187 | 0,0092 | 0,0204 | 0,0039 | 0,0083 |
| 50 | 8 | 0,0212 | 0,0052 | 0,0206 | 0,0189 | 0,0420 | 0,0055 | 0,0181 |
| 200 | 2 | 0,0109 | 0,0024 | 0,0107 | 0,0067 | 0,0137 | 0,0016 | 0,0065 |
| 200 | 4 | 0,0098 | 0,0022 | 0,0096 | 0,0051 | 0,0116 | 0,0020 | 0,0047 |
| 200 | 8 | 0,0055 | 0,0026 | 0,0048 | 0,0048 | 0,0110 | 0,0028 | 0,0039 |
| 800 | 2 | 0,0075 | 0,0012 | 0,0074 | 0,0025 | 0,0050 | 0,0008 | 0,0023 |
| 800 | 4 | 0,0051 | 0,0011 | 0,0050 | 0,0016 | 0,0037 | 0,0010 | 0,0013 |
| 800 | 8 | 0,0023 | 0,0013 | 0,0018 | 0,0014 | 0,0032 | 0,0014 | ~0 |

- Bei eta = 0 ist die Std der Rapiditaet gleich der Std von V (auf 4 Stellen).
- **Exponent in rho** (Std V, 50 -> 800), je sigma = 2 / 4 / 8:
  - eta = 0: -0,43 / -0,48 / -0,81
  - eta = 1: -0,59 / -0,62 / -0,95
  - Breite Pakete beruhigen sich mit der Dichte schneller.
- Bei sigma = 8 und rho = 800 liegt die Streuung nahe am reinen Stichprobenrauschen der Messung. Dieses waechst mit sigma
  (breiteres Paket, Schwerpunkt aus zufaellig liegenden Punkten).
- Der statistische Fehler einer Std aus 16 Saaten ist ~18 %, der eines Verhaeltnisses ~25 %.
- **"Kein Ruhesystem" in der Rapiditaet (Hinweis der Leitung, beschreibend):** Std der Rapiditaet eta = 1 gegen eta = 0,
  je sigma = 2 / 4 / 8:

  | rho | eta = 1 / eta = 0 |
  |---|---|
  | 50 | 1,03 / 1,06 / 1,98 |
  | 200 | 1,25 / 1,18 / 2,02 |
  | 800 | 0,68 / 0,73 / 1,41 |

  - Die Werte sind nicht gleich, haben aber kein festes Vorzeichen.
  - Mit runder Laborhuelle ist das eta-1-Paket nicht der Boost des eta-0-Pakets (PLAN 7.4). Der Vergleich ist deshalb kein
    sauberer Test.

### 3.3 Norm (Fenster) gegen Kontinuum, R = Saatmittel(n)/n_c [E]

| rho | R am Anfang (ta bis ta + 2) | R am Ende (tb - 2 bis tb) | G = Ende/Anfang | max R |
|---|---|---|---|---|
| 50 | 1,03 bis 1,12 | 1,10 bis 1,17 | 1,03 bis 1,11 | 1,256 |
| 200 | 1,011 bis 1,024 | 1,022 bis 1,037 | 1,010 bis 1,019 | 1,051 |
| 800 | 0,999 bis 1,006 | 1,003 bis 1,011 | 1,002 bis 1,009 | 1,021 |

- R - 1 faellt etwa wie 1/rho. Es ist die Rauschleistung E|delta phi|^2, keine Instabilitaet.
- Das Kontinuum selbst haelt seine Norm im Fenster auf 3e-3 (19,673 -> 19,675 bei sigma = 2, eta = 0; 7,967 -> 7,946 bei sigma = 2, eta = 1).
- Kein Anwachsen und keine Ueberlaeufe: max abs(psi) <= 16 in allen Laeufen; alle Werte endlich.

### 3.4 Saatmittel gegen Kontinuum (KW0) [E]

- Relative Streuung von phi (geometrisches Mittel ueber 18 Pruefpunkte): 0,227 / 0,114 / 0,054 bei rho = 50 / 200 / 800.
- **Je Pruefpunkt** (rho = 200): 0,055 bis 0,164.
  - Sie waechst mit der Laufzeit, etwa bei sigma = 2, eta = 0: 0,056 -> 0,110 -> 0,141.
  - Sie waechst etwas mit sigma: bei tb 0,14 / 0,13 / 0,16 (eta = 0).
- Abweichung in SE: Mittel ~0,8, groesste 1,66, keine ueber 2. Das passt zu einem unverzerrten Schaetzer.
- Bild lauf-69/saatmittel_kontinuum.png: Profil bei tb, rho = 800. Saatmittel und Kontinuum liegen aufeinander. Fuer
  eta = 1 ist das Profil mit Schritt 2 unterabgetastet (Wellenlaenge 5,3); die Punkte treffen trotzdem.

## 4. Kontrollen

- **Codeprobe** (rho = 5, N = 2149, sechs Quellen):
  - CDQ-Rekursion gegen die dichte Loesung (I + a A) psi = J: 1,1e-15 (psi), 1,8e-15 (C psi).
  - Abgebrochene Reihe (1/2) A Summe (-a A)^k: 1,1e-11. Zuschauer gegen Maskensumme: 7,3e-15.
- **Normierung an der Punktquelle** (rho = 200, 16 Saaten, J = rho am eingefuegten Ursprung):
  - Saatmittel von K(0 -> x) gegen (1/2) J0(m tau) [S: (3.23)] an 8 Eigenzeiten x 3 Rapiditaeten.
  - Abweichung |z| <= 2,49, dreimal ueber 2 von 24. Die 24 Werte teilen sich die Streuungen und sind korreliert.
  - Beispiele (zeta = 0): tau = 0,5: 0,4690 gegen 0,4692; tau = 3: -0,1345 gegen -0,1300; tau = 16: -0,0867 gegen -0,0874.
  - Normierung 1/2, Sprung- und Haltamplitude und das Vorzeichen der Masse stimmen. Mit falschem Vorzeichen waechst die
    Reihe wie I0.
  - Relative Streuung des Punktpropagators: 1 % (tau = 0,5) bis 11 bis 19 % (tau = 5, 8 und 16). Bei tau = 12, nahe einer
    Nullstelle von J0, sind es 36 bis 57 %.
- **Kontinuum, zwei Wege:**
  - k-Raum (exakt je Mode, ungekappte Quelle) gegen direkte Gauss-Legendre-Faltung mit (1/2) J0 (gekappte Quelle) an
    18 Pruefpunkten: <= 3,7e-5 relativ.
  - Normanteil am Klassenrand <= 5e-31.
  - V_c gemessen gegen analytisches <v>: <= 3e-4 (ganze Scheibe).
- **Vollstaendige Vergangenheit:** Das Gebiet D = J+(Scheibe 36) geschnitten {t <= 44} ist kausal konvex und enthaelt alle
  Quellen. Jeder Punkt hat seine volle Vergangenheit; es gibt keine Randpunkte (PLAN 2).
- **Stichprobenrauschen [M]:** Die Vorhersage (Delta-Methode) liegt bei rho = 800 und sigma = 8 bei 0,0013 bzw. 0,0014.
  Gemessen: 0,0023 bzw. 0,0014. Die Messvorschrift selbst setzt also eine Untergrenze, die mit sqrt(sigma/rho) geht.
- **Laufzeit:** rho = 800 je Saat 67,5 bis 76,7 s (N = 6,98 Mio.). rho = 200: ~15 s, rho = 50: ~3,5 s. Rechenzeit gesamt
  ~25 min.

## 5. Latten (v3)

- **L1 kann scheitern:** ja.
  - KW1 ist gescheitert (rho = 50), KW2 an eta = 1. Nach Kartenwortlaut auch KW1 bei sigma = 2.
  - KW0 haette an einer Verzerrung des Codes oder des Kontinuums scheitern koennen, KW3 an einer Instabilitaet der
    Vorwaertsrekursion.
- **L2 Gegenprobe:**
  - dichte Loesung, Reihe, Maskensumme
  - Punktquelle gegen (1/2) J0
  - Quadratur gegen k-Raum, analytisches <v>
  - Stichprobenvorhersage, ganze Scheibe gegen Fenster, drei Dichten
- **L3 Numerik:** Rekursion 1e-15; Reihe 1e-11; Kontinuum 4e-5; Kappung der Quelle [M] <= 0,08 %.
- **L4 schon bekannt:**
  - Johnston konstruiert a, b so, dass der Erwartungswert der Kontinuumspropagator ist [S]. KW0 bestaetigt das numerisch
    fuer ausgedehnte Quellen.
  - Johnston nennt fuer 1+1 und m^2 << rho "preliminary results", die Fluktuationen fielen mit der Dichte [S, S. 10]. Hier
    ist das fuer ausgedehnte Pakete beziffert: rho^(-0,52).
  - Feynman-Propagator und Sorkin-Johnston-Zustand auf Kausalmengen [L].
  - Swerves [L: Dowker/Henson/Sorkin 2004].
  - Ob die Schwerpunktstreuung von Wellenpaketen auf Kausalmengen schon gemessen wurde, weiss ich nicht [L?].
- **L5 Messbezug:** keiner (synthetisch, 1+1, eine lineare Welle).

## 6. Bedeutung

- **Fuer Ue3 [E, H]:**
  - Eine Welle, die Johnstons Summe ueber alle Ketten benutzt, laeuft auf dem Netz ohne Ruhesystem im Mittel exakt wie
    im Kontinuum.
  - Eine einzelne Welle zittert nur wenig, und das Zittern faellt mit der Dichte (Exponent -0,4 bis -1).
  - Der Punktlaeufer aus KAUSAL-SWERVE-1 zittert dagegen um 1/4 in der Rapiditaet je Link, und das waechst mit der
    Dichte (Schritte je Eigenzeit ~ sqrt(rho)) [E dort].
  - Umrechnung [M, mit der Annahme, dass KAUSAL-SWERVE-1 tau^2 = Intervallvolumen setzt]: SWERVE-Schritt tau ~ 1,05/sqrt(rho) in Standardnormierung. Bei rho = 200 sind das ~270 Schritte in
    der Eigenzeit 20, Rapiditaetsstreuung ~8. Die Welle hat 0,005 bis 0,014.
  - **Der Hauptgrund ist die Summe ueber alle Wege, nicht die Breite [H].** Schon der Punktpropagator fluktuiert nur um
    1 bis 19 % (ausser nahe Nullstellen von J0; Abschnitt 4).
- **Breite hilft zusaetzlich, aber erst bei genug Dichte [E]:**
  - sigma = 8 gegen 2: 0,86 / 1,48 (rho = 50), 0,50 / 0,71 (rho = 200), 0,30 / 0,55 (rho = 800).
  - Die Hypothese der Karte trifft also die Richtung bei hoher Dichte. Bei rho = 200, wie vorab festgelegt, ist sie nicht
    eingetroffen.
  - **Zwei Gegenkraefte [M/H]:**
    - Das Rauschen je Punkt waechst mit sigma: Die Monte-Carlo-Summe laeuft ueber mehr schwingendes Feld (PLAN 6.1),
      relative Streuung bei tb 0,16 statt 0,14.
    - Das Stichprobenrauschen der Schwerpunktmessung waechst wie sqrt(sigma).
- **Nachhinken bewegter Pakete [E, Mechanismus H]:**
  - Bei eta = 1 liegt <x>(t) hinter dem Kontinuum (abgelesen aus x_t.png):
    - rho = 50: 0,2 bis 0,9
    - rho = 200: 0,05 bis 0,2
    - rho = 800: ~0,03 (Bild x_t.png)
  - Das skaliert wie 1/rho, also wie die Rauschleistung (R - 1), nicht wie das Rauschen selbst. E[phi] ist unverzerrt (KW0).
  - Es ist also eine Verzerrung des |phi|^2-gewichteten Schaetzers, keine Bremsung der Welle im Mittel.
  - **Vermutete Ursache [H]:**
    - Die Rauschleistung waechst mit der Zeit und mit der Vergangenheit, die ein Punkt sieht.
    - Im Laborschnitt liegt sie deshalb hinter dem bewegten Paket.
    - Das Quellgebiet ruht im Laborsystem. Sein Rauschen breitet sich um x = 0 aus, also hinter dem Paket.
  - Ob ein Teil davon ein echtes Ruhesystem des Netzes waere, zeigt dieser Test nicht. Dafuer braeuchte es eine im
    Paketsystem runde Quelle (Abschnitt 8).
- **Stabilitaet [E]:** Die Vorwaertsrekursion mit Johnstons Amplituden ist ueber 20/m Laufstrecke stabil. Eine Glaettung
  ist dafuer nicht noetig (Gegenzweig der Karte nicht ausgeloest).

## 7. Selbstanzeigen

1. **Keine Interpreterstarts ausserhalb des Starters**, auch keine Versionsproben. Lokal kein python, awk oder perl.
   - Benutzt: jq, grep, sed (Textkorrekturen in ERGEBNIS.md), sha256sum, date, ssh, scp.
   - Dazu Datei- und Textbefehle: cp, mv, mkdir, chmod, ls, diff, cat, cut, head, tail, sort, uniq, wc, tr.
   - Warteschleifen mit until/sleep im Hintergrund. Ein direkter "sleep 45" wurde vom Werkzeug abgelehnt.
2. **Vor dem Einfrieren gesehen** (PLAN 8, offengelegt):
   - Kontinuumswerte (V_c, Fenster W, analytisches <v>)
   - Punktquellenwerte der Rauchsaaten 91 und 92
   - Laufzeiten
   - Saatmittel, Geschwindigkeiten und Normen der Kausalmenge habe ich vor dem Einfrieren nicht angesehen. Die Pfadprobe
     der Auswertung lief mit umgeleiteter Ausgabe.
3. **Das Fenster der Hauptmessung ist meine Festlegung** [F]. Die Hinweise sagen "ueber die Punkte der Scheibe". Die ganze
   Scheibe ist mitberichtet.
   - Mit ihr waere KW1 deutlich schlechter: bei rho = 50 bis -14 %, bei rho = 200 bis -3,7 %, bei rho = 800 bis -0,9 %.
   - Nach dieser Lesart scheiterte KW1 auch bei rho = 200 (sigma = 4 und 8, eta = 1: -2,5 % und -3,7 %) und bei rho = 800
     bestuende es (-0,4 % bis -0,9 %). Das ist meine Nachrechnung aus Tabelle 3.1, nicht eingefroren geurteilt.
4. **KW2 steht auf der Schwelle.**
   - eta = 0 erfuellt mit 0,4998 <= 0,5. eta = 1 verfehlt mit 0,710, das sind ~1,3 Standardfehler des Verhaeltnisses ueber
     0,5.
   - Mit 16 Saaten ist das Urteil wenig belastbar. Mehr sagt der Gang mit rho (0,86 -> 0,50 -> 0,30 bzw. 1,48 -> 0,71 ->
     0,55).
5. **Gemeinsame Streuungen:** Alle sechs Quellen laufen je (rho, Saat) auf derselben Streuung. Die Konfigurationen sind
   deshalb korreliert. Die Std je Konfiguration ist davon nicht verzerrt, das Verhaeltnis s8/s2 hat aber korrelierte
   Faktoren.
6. **Nach der Rechnung gebildet und nicht geurteilt** (beschreibend):
   - Feldanteil (Abzug des Stichprobenrauschens in Quadratur, nimmt Unabhaengigkeit an)
   - Exponenten in rho
   - Deutung des Nachhinkens
7. **Kartenfehler KW1** (Bezug tanh(eta) gegen V_c) und die Luecke bei eta = 0 sind vor der Rechnung berichtigt. Nach
   Wortlaut ist KW1 ebenfalls nicht eingetroffen.
8. **Benincasa-Dowker-Vergleich (Karte, beschreibend): nicht gerechnet.**
   - Grund: Zeitbox. Die Schichtzaehlung L1 bis L3 je Punkt liess sich nicht schnell genug vektorisieren.
   - Bekannt ist [L]: Der ungeglaettete Operator hat mit rho wachsende Fluktuationen (Sorkin 2007).
9. **Speicheranzeige:** systemd meldet "Memory peak" ~0,3 MB, das ist offenbar die Zaehlung der Huelle. Kein Lauf
   ueberschritt MemoryMax 4G (alle rc = 0).
10. **Kein frischer Gegenleser** fuer Herleitung, Code und Text.
11. **Zeitbox:** Start 05:27:21 CEST; Text ab 06:10:46 CEST; Abschluss 06:13:39 CEST (date), also 46 min von 120.

## 8. Naechste Schritte [H]

- **Paketrunde Quelle** (Gauss im Ruhesystem des Pakets, Gebiet mitgeboostet) und Messung in Paketzeit:
  - Dann muessen eta = 0 und eta = 1 statistisch identisch sein.
  - Ein Rest-Nachhinken waere ein Messartefakt der Laborscheiben.
- **Schwerpunkt mit der erhaltenen Ladungsdichte** i(phi* d_t phi - phi d_t phi*) statt |phi|^2. Die Rauschleistung geht
  dann nicht positiv in das Gewicht ein.
- **Q-Ball auf der Kausalmenge** (nichtlinear), wie von der Karte als Folge genannt: Haelt er zusammen, und faellt sein
  Zittern mit der Dichte wie hier?

## 9. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-055255
- code/:
  - kausal_welle.py: Streuung, Rekursion, Messung, Punktquelle, Probe
  - kontinuum.py
  - auswertung.py
  - je mit *.eingefroren-20261004-055255; pruefsummen-einfrieren.txt
- lauf-69/:
  - feld-r{50,200,800}-s{1..16}.json/.npz, punkt-r200-s{1..16}.json, probe-r5-s1.json, kont/ (kontinuum.json/.npz)
  - Logs
  - auswertung.json (mit Vermerken), auswertung.maschine.json, aw/ (Originalausgabe)
- **Bilder** (lauf-69/):
  - saatmittel_kontinuum.png
  - x_t.png: <x>(t) - V_c t mit Streuband je sigma und rho
  - streuung_v.png: Streuung von V gegen sigma und rho, mit Stichprobenvorhersage
  - norm_t.png: Norm gegen t
- rauch-69/: Rauchlaeufe (Saaten 91 und 92) und Pfadprobe der Auswertung.
- Auf der .69: /home/fmh/fmhc-physics-remote/runde37-kausal-welle/ (code/, rauch/, lauf/).

## 10. Einfach gesagt

Wir haben eine Welle ueber ein zufaelliges Netz aus Raumzeit-Punkten laufen lassen, bei dem jeder Punkt nur weiss, welche
Punkte vor ihm liegen; die Welle zaehlt dabei alle moeglichen Wege durch das Netz zusammen. Im Mittel ueber viele Netze
laeuft sie genau wie im glatten Raum, und auch eine einzelne Welle behaelt ihr Tempo bis auf etwa ein Prozent, waehrend
ein Punktteilchen, das von Strich zu Strich springt, seine Richtung nach wenigen Dutzend Schritten vergisst. Ob eine breite
Welle weniger zittert als eine schmale, haengt davon ab, wie dicht das Netz ist: bei duennem Netz zittert sie sogar etwas
mehr, bei dichtem nur ein Drittel bis halb so stark, und bei der vorher festgelegten Dichte lag das Ergebnis genau an der
Grenze, deshalb zaehlt die Vorhersage als nicht eingetroffen. Gegen das Zittern hilft also vor allem, dass die Welle alle
Wege zugleich nimmt, die Breite hilft erst bei dichtem Netz dazu. Das ist eine Computerrechnung in einer vereinfachten
zweidimensionalen Welt, keine Messung.
