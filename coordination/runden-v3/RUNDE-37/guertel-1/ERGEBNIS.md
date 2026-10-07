# GUERTEL-1: Ergebnis (Runde 41, zusammengelegt mit STRUKTUR-FEDERRING-1)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 14:51:08 CEST; Literaturabrufe ab 15:02:08 CEST.
  - Rauchlauf 1: 13:16:15 bis 13:17:41 UTC. Rauchlauf 2 und Gegenprobe-Codetest: 13:20:04 bis 13:24:36 UTC.
  - Plantext ab 15:21:50 CEST. Plan und Code eingefroren 15:28:38 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe 13:28:57 bis 13:58:46 UTC: 14 Units ueber kleintest.sh, Spur cpu, alle rc = 0, keiner wiederholt.
  - Nachtrag 1 zum Plan 15:45:27 CEST. Berichtigungsfeld in auswertung.json 16:01:30 CEST. Text ab 16:03:08 CEST.
- **Kennzeichen:**
  - [G] hier gerechnet (synthetisch, keine Messdaten); [M] eigene Mathematik
  - [S] an der Quelle gelesen (quellen/); [L] Gedaechtnis; [H] Hypothese; [ES] eigener Schluss
  - [R] im Rauchlauf vor dem Einfrieren gesehen
- **Art des Ergebnisses:** synthetische Modellrechnung an einem Modellknoten, keine Messdatenbestaetigung.

## Ergebnis zuerst

1. **Einfaches Abkuehlen findet den Entwirrungsweg nicht [G].**
   - Bei 720 Grad endet jede der 20 Saaten (zwei Laengen, zwei Achsen) weit ueber dem Grundzustand:
     E_min(720)/E_min(0) = 20,9 (zweizaehlig, L = 1,8), 19,7 (allgemeine Achse), 112 (zweizaehlig, L = 1,3).
   - Damit ist GT1 nicht eingetroffen. Eine Sperre (GT3) liess sich nicht bestimmen, weil kein entwirrter Endzustand
     entstand.
   - Die Topologie erlaubt die Entwirrung. Die Rechnung zeigt nur, dass dieser Abkuehlweg sie nicht erreicht.
2. **Der vorwaerts gewickelte Zustand bleibt ueber 360 Grad hinaus stabil [G], gegen meinen Schreibtisch in fuehrender
   Ordnung.**
   - Das Drehprotokoll springt erst bei 659 Grad (zweizaehlig) bzw. 427 Grad (allgemein, beide L = 1,8) in einen
     tieferen Zustand. Bei L = 1,3: 721 bzw. 375 Grad.
   - Bei diesen Spruengen verlieren einzelne Faeden eine oder zwei Windungen. Das sind Zwischenrasten.
   - Der Kraftverlauf bleibt nach der Startdelle fast ueberall positiv, mit Einbruechen an den Spruengen. Nur die
     allgemeine Achse wird kurz vor ihrem Sprung leicht negativ (bis -6,2).
   - Bei 360 Grad gibt es keinen Vorzeichenwechsel: weder Finns Sinus 0, +, 0, -, 0 noch die Saege des Schreibtischs,
     eher eine Ratsche.
3. **Bei 360 Grad wandert die Verdrillung auf eine andere Achse [G].**
   - Die allgemeine Achse endet nach dem Abkuehlen in allen Saaten bei derselben Energie wie die zweizaehlige Achse:
     - L = 1,8: 49,6515125 gegen 49,6515126 (vorher 177,8);
     - L = 1,3: 255,075535 in beiden Faellen (vorher 497,85).
   - Die Windung um die eigene Achse ist danach 0. Das ist Staleys "2 pi um eine Achse wird 2 pi um eine andere" [S]
     als gemessener Vorgang, mit bevorzugter Endlage.
4. **Die dritte Dimension macht das Verdrillen billig [G].**
   - L = 1,8: 360 Grad kosten im Raum 41,2 Energieeinheiten, in der Ebene 2700, also das 65-Fache. Bei 720 Grad 168
     gegen 25650.
   - In der Ebene bleiben die Windungen erhalten (GT0 nach Plan eingetroffen).
   - Ohne Ausschlussvolumen (Gegenprobe) gehen sie verloren, und die Sonde schlaegt an.
5. **Urteile fuer die Konturlaenge 1,8 d, berichtigt nach Nachtrag 1:**
   - GT0 eingetroffen nach Plan; nach Wortlaut nicht auswertbar.
   - GT1, GT2a, GT2b nicht eingetroffen.
   - GT3 nicht auswertbar. Der Code meldet "eingetroffen"; das beruht auf einem Gleitkomma-Grenzfall der Windungsregel
     (Selbstanzeige 6).

## Urteile (lauf-69/auswertung.json; berichtigt im Feld nachtrag_1)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan (L = 1,8) | nach Wortlaut (L = 1,8) | L = 1,3 (Grenze) | tragende Werte (L = 1,8) |
|---|---|---|---|---|---|---|
| GT0 | Ebene: E_min waechst bei jedem Vielfachen von 360 Grad, keine Rueckkehr | 85 % | **eingetroffen** | nicht auswertbar (1080 und 1440 Grad verletzen in der Ebene die Sonde) | nicht auswertbar (schon 720 Grad verletzt die Sonde) | Stufen 0 -> 360: +2700,1 (SE 0,011); 360 -> 720: +22951 (SE 0,66); E_min(720)/E_min(0) = 3044 |
| GT1 | [H] frei: E_min(720) innerhalb 10 % bei E_min(0), E_min(360) >= 3 SE darueber | 50 % | **nicht eingetroffen** | nicht eingetroffen | nicht eingetroffen (Verhaeltnis 112) | E_min(0) = 8,409; E_min(360) = 49,652; E_min(720) = 176,03 (Verhaeltnis 20,9); 0 von 5 Saaten entwirrt |
| GT2a | [H] zweizaehlig: keine weitere Nullstelle in (0, 360), Kraftspitze 180 +- 45 | 45 % | **nicht eingetroffen** | nicht eingetroffen | nicht eingetroffen (Spitze bei 120 Grad, M(30) < 0) | M_best < 0 bei 30 und 60 Grad (Startdelle); Spitze auf 30..330 bei 300 Grad; E_min nicht monoton (8,41 -> 2,82 bei 90 Grad) |
| GT2b | [H] allgemeine Achse: dasselbe Muster, Nullstelle 360 +- 30 | 35 % | **nicht eingetroffen** | nicht eingetroffen | nicht eingetroffen | einziger Vorzeichenwechsel von - nach + bei etwa 73 Grad (Startdelle); kein Wechsel + -> - bis 690 Grad |
| GT3 | [H] Sperre bei 720 endlich und < Verdrillungsenergie bei 360 | 40 % | **nicht auswertbar** (berichtigt; Code: eingetroffen, S = 0,24) | nicht auswertbar (berichtigt) | nicht auswertbar (berichtigt; Code: eingetroffen, S = 0) | keine Saat entwirrt (alle W = (1, 0, 1, 0)); dE_360 = 41,24 |

- **Allgemeine Achse, nur berichtet:**
  - GT1 nicht eingetroffen (Verhaeltnis 19,7).
  - GT3 nach Plan "eingetroffen" (S := 0, weil das Protokoll bei 720 Grad W = (0, 0, 0, 0) zeigt). **Nicht belastbar**:
    E(720) = 168 bzw. 165,6 nach dem Abkuehlen, gegen E_min(0) = 8,41. Das Windungsmass um die Drehachse sieht die
    Achsenwanderung nicht (Ergebnis 3).
- **SE-Regeln:** Die "3 SE" sind meist leer erfuellt. An 18 von 27 Winkeln (zweizaehlig, L = 1,8) enden alle fuenf
  Saaten energiegleich (SE < 0,001, an 10 davon SE < 1e-6). Jede positive Differenz besteht dann.

## Kennzahlen je Fadenlaenge und Achse

E_min = kleinste Endenergie der gueltigen Saaten; E_quer +- SE ueber 5 Saaten; M = Haltemoment dE/dtheta des besten
Zustands (Energie je rad); W = Windungen des besten Zustands um die Drehachse. Alle 3D-Saaten bestehen die Sonde
(540 von 540).

### L = 1,8 d (Konturlaenge 3,24, 16 Segmente)

| theta | zweizaehlig E_min | E_quer +- SE | M | W | allgemein E_min | E_quer +- SE | M | W |
|---|---|---|---|---|---|---|---|---|
| 0 | 8,41 | 8,41 +- 0 | -0,9 | 0 0 0 0 | 8,41 | 8,41 +- 0 | 0,8 | 0 0 0 0 |
| 90 | 2,82 | 2,82 +- 0 | 0,5 | 0,25 je Faden | 3,89 | 3,89 +- 0 | 3,9 | 0,25 je Faden |
| 180 | 13,13 | 13,13 +- 0 | 3,8 | 0,5 | 44,76 | 44,76 +- 0 | 18,7 | 0,5 |
| 270 | 27,47 | 27,47 +- 0 | 13,0 | 0,75 | 106,79 | 106,79 +- 0 | 58,7 | -0,25 0,75 -0,25 -0,25 |
| 300 | 34,62 | 34,62 +- 0 | 14,1 | 0,83 | 38,75 | 97,48 +- 23,98 | 7,2 | 0,83 -0,17 -0,17 -0,17 |
| 360 | 49,65 | 49,65 +- 0 | 16,1 | 1 1 1 1 | 49,65 | 49,65 +- 0 | 14,0 | 0 0 0 0 |
| 450 | 79,40 | 79,40 +- 0 | 21,6 | 1,25 | 71,96 | 71,96 +- 0 | 15,8 | 0,25 |
| 540 | 117,68 | 118,52 +- 0,23 | 26,6 | 0,5 | 106,38 | 106,48 +- 0,05 | 31,7 | 0,5 |
| 570 | 123,32 | 124,98 +- 1,08 | 3,4 | -0,42 0,58 -0,42 0,58 | 125,75 | 126,05 +- 0,08 | 40,4 | -0,42 0,58 0,58 0,58 |
| 630 | 132,46 | 133,32 +- 0,29 | 14,4 | 0,75 -0,25 -0,25 0,75 | 139,41 | 139,58 +- 0,17 | 14,0 | 0,75 -0,25 -0,25 -0,25 |
| 720 | 176,03 | 176,17 +- 0,14 | 30,0 | 1 0 1 0 | 165,55 | 166,48 +- 0,45 | 21,7 | 0 0 0 0 |
| 1080 | 396,39 | 396,39 +- 0 | 50,1 | 1 1 1 1 | 376,53 | 379,97 +- 0,86 | 35,9 | 1 1 0 0 |
| 1440 | 744,92 | 744,92 +- 0 | 64,1 | 0 1 0 1 | 758,23 | 764,54 +- 2,49 | 34,7 | 0 1 0 0 |

- Alle 27 Winkel je Achse stehen in auswertung.json (tabellen).
- Verdrillungsenergie dE_360 = 41,24 (beide Achsen; allgemein nach Achsenwanderung).
- Moment auf dem Weg kleinster Energie, zweizaehlig, von 90 bis 540 Grad: 0,5, 7,7, 9,6, 3,8, 7,6, 11,3, 13,0, 14,1,
  13,8, 16,1, 17,8, 20,0, 21,6, 24,6, 24,4, 26,6. Bei 570 Grad bricht es auf 3,4 ein (Zweigwechsel), danach steigt es
  wieder bis 30,0 bei 720 Grad.

### L = 1,3 d (Konturlaenge 2,34, 12 Segmente; Grenze)

| theta | zweizaehlig E_min | E_quer +- SE | M | W | allgemein E_min | E_quer +- SE | M | W |
|---|---|---|---|---|---|---|---|---|
| 0 | 5,11 | 5,11 +- 0 | -1,6 | 0 | 5,11 | 5,11 +- 0 | -1,7 | 0 |
| 90 | 21,51 | 21,51 +- 0 | 61,5 | 0,25 | 29,90 | 29,90 +- 0 | 75,3 | 0,25 |
| 180 | 127,27 | 127,27 +- 0 | 21,8 | 0,5 | 204,41 | 204,41 +- 0 | 54,8 | 0,5 |
| 360 | 255,08 | 255,08 +- 0 | 47,2 | 1 1 1 1 | 255,08 | 255,08 +- 0 | 41,2 | 0 0 0 0 |
| 540 | 425,52 | 432,94 +- 4,64 | 44,2 | 1,5 0,5 0,5 0,5 | 429,80 | 429,89 +- 0,05 | 98,8 | -0,5 0,5 0,5 0,5 |
| 720 | 572,57 | 575,38 +- 2,82 | 66,3 | 1 0 1 0 | 568,20 | 568,20 +- 0 | 71,2 | 0 0 0 0 |
| 1080 | 1058,32 | 1058,32 +- 0 | 119,7 | 1 1 1 1 | 1074,68 | 1083,81 +- 7,59 | 122,4 | 0 1 0 0 |
| 1440 | 1784,81 | 1784,81 +- 0 | 115,4 | 1 1 1 1 | 2045,16 | 2101,74 +- 14,14 | 249,1 | 0 0 0 0 |

- dE_360 = 249,97, sechsmal so viel wie bei L = 1,8. Die Schlaffe senkt den Preis der Verdrillung stark.
- Auch hier hat die allgemeine Achse bei 360 Grad nach dem Abkuehlen exakt die Energie der zweizaehligen (255,075535).

### Ebene (Kontrolle GT0)

| theta | L = 1,8 E_min | E_quer +- SE | W | L = 1,3 E_min | E_quer +- SE | W |
|---|---|---|---|---|---|---|
| 0 | 8,43 | 8,43 +- 0 | 0 | 5,11 | 5,11 +- 0 | 0 |
| 180 | 206,81 | 206,81 +- 0 | 0,5 | 649,97 | 649,97 +- 0 | 0,5 |
| 360 | 2708,47 | 2708,51 +- 0,011 | 1 | 5205,61 | 5272,15 +- 28,88 | 1 |
| 540 | 10187,66 | 10191,27 +- 1,97 | 1,5 | 17538,78 | 17539,21 +- 0,20 | 1,5 |
| 720 | 25658,25 | 25659,93 +- 0,66 | 2 | Sonde verletzt (0 von 5) | | |
| 1080, 1440 | Sonde verletzt (0 von 5) | | | Sonde verletzt | | |

- Die gueltigen Ebenen-Zustaende sind stark gespannt. Restkraft nach FIRE bis 1272 (L = 1,8) bzw. 932 (L = 1,3).
  Gegen die Stufen von 2700 und 22951 ist der daraus folgende Energiefehler (Groessenordnung 10) klein.

## Drehprotokoll (quasistatisch, 1-Grad-Schritte, beschreibend)

| L | Achse | erster grosser Sprung | Energie vorher -> nachher | Windungen danach |
|---|---|---|---|---|
| 1,8 | zweizaehlig | 659 bis 661 Grad | 186,8 -> 149,2 | Faeden 1, 3 eine, Faeden 2, 4 zwei Windungen verloren |
| 1,8 | allgemein | 427 bis 431 Grad | 179,5 -> 70,1 | alle eine Windung verloren |
| 1,3 | zweizaehlig | 720 Grad (in der Gitter-Relaxation) bis 722 Grad | 735,6 -> 590,8 | (1, 0, 1, 1) bei 720 Grad |
| 1,3 | allgemein | 375 bis 378 Grad | 504,3 -> 269,9 | alle eine Windung verloren |

- Bis zum ersten Sprung bleiben alle vier Faeden auf dem Vorwaertsast (W_i = theta/360).
- Das Haltemoment ist auf dem Protokollweg der zweizaehligen Achse (L = 1,8) nach der Startdelle (negativ bis 76 Grad)
  bis 1440 Grad ueberall positiv.
- Bei der allgemeinen Achse (L = 1,8) ist es nach der Startdelle (bis 69 Grad) nur von etwa 400 bis 426 Grad leicht
  negativ (bis -6,2), kurz vor dem Sprung.
- Weitere kleinere Spruenge (je 2 bis 21 Energieeinheiten) folgen zwischen 431 und 1397 Grad, gehaeuft bei 1069 bis
  1084 Grad (allgemeine Achse, L = 1,8; zusammen etwa -48).
- **Sonde:** Im Protokoll bestehen beide 3D-Systeme in beiden Laengen bis 1440 Grad (Faden-Faden >= 0,155,
  Kreuzungsrand >= 0,085, Koerperabstand >= 1,078).

### Formmass bei 360 Grad (vorab festgelegt, beschreibend)

- **Zweizaehlig, L = 1,8:** J = 0,52 mit M(330) = 13,8 > 0 und M(390) = 17,8 > 0, also "unklar". Es gibt keinen
  Vorzeichenwechsel. Korrelation mit sin(theta/2): -0,56; mit der Saege: -0,46.
- **Allgemein, L = 1,8:** Die Regel ergibt "glatt" (J = 0,18), aber auch hier wechselt das Vorzeichen nicht.
  - J ist klein, weil das Moment bei 270 Grad am groessten ist.
  - Das Etikett "glatt" beschreibt also keinen Nulldurchgang.
  - Korrelationen 0,13 bzw. 0,17.
- **L = 1,3:** "unklar" (zweizaehlig) bzw. "glatt" ohne Nulldurchgang (allgemein).

## Kontrollen

1. **Ebene (GT0) [G]:**
   - Windungen erhalten: W = k bei k mal 360 Grad in allen gueltigen Saaten.
   - Die Energie steigt viel steiler als im Raum (Faktor 65 bei 360 Grad, etwa 150 bei 720 Grad). Nach Plan
     eingetroffen.
   - 1080 und 1440 Grad (W = 3, 4) brechen die Sonde, wie die Packungsgrenze aus PLAN.md 7.3 vorhersagte.
2. **Durchdringungsprobe:**
   - Abkuehlen 3D: 540 von 540 Saaten gueltig. Kleinster Faden-Faden-Abstand 0,137 (Grenze 0,1), kleinster
     Kreuzungsrand 0,026 (> 0), kleinster Koerperabstand 1,072 (> 1).
   - Ebene: 25 von 35 (L = 1,8) bzw. 20 von 35 (L = 1,3) gueltig.
     - Ungueltig sind 1080 und 1440 Grad (Packungsgrenze).
     - Bei L = 1,3 auch 720 Grad (Dehnung, wie in Rauchlauf 2).
   - Stringlaeufe: Pfadpruefung bestanden. Inhaltlich sind sie aber keine Entwirrungswege (Selbstanzeige 6).
3. **Topologie-Probe (Windungen):**
   - In 3D wechseln Faeden ihre Windung um ganze Zahlen; Kreuzungen gab es nach der Sonde nicht.
   - Bei 720 Grad sind alle W_i bis auf 3,3e-16 ganzzahlig.
   - Grenze des Masses: Wandert die Verdrillung auf eine andere Achse, zeigt W um die Drehachse 0, obwohl der Zustand
     verdrillt ist (allgemeine Achse bei 360 Grad).
4. **Gegenprobe der Sonde (Ausschluss aus, L = 1,8) [G]:**
   - Beim Drehen auf 720 Grad schlaegt die Sonde in beiden Systemen an. Ebene: Mittellinie bis 6,6e-5 an den
     Koerpermittelpunkt, Kreuzungsrand -0,038. Zweizaehlig: Kreuzungsrand -0,021.
   - Die Windungen sind danach in beiden Systemen 0 statt 2. Ohne Ausschluss gehen sie also verloren, und die Sonde
     erkennt das.
5. **Code und Daten:**
   - Eingefrorene Hashes beim Lauf auf der .69 bestaetigt (guertel.py 795f474d..., auswertung.py a61b2bfd...).
   - Alle 36 Laufdateien haben auf beiden Rechnern dieselbe sha256 (lauf-69/PRUEFSUMMEN.txt).
   - Die Auswertung lief vor dem Einfrieren gegen synthetische Eingaben (testdaten-synthetisch/), um Abstuerze nach dem
     Einfrieren auszuschliessen.

## Ableitbarkeit

- **Vorab ableitbar und nur Kontrolle:**
  - GT0 (Windung in der Ebene erhalten, PLAN 1.2 Punkt 7).
  - E_min(theta) = E_min(-theta) und die 720-Periodizitaet von E_min. Die gemessene Kurve erreicht E_min aber nicht
    und prueft das deshalb nicht.
  - Die Existenz des Entwirrungswegs; die Packungsgrenze der Ebene (PLAN 7.3).
- **Schreibtisch-Vorhersagen [M, Naeherung], jetzt geprueft:**
  - "Vorwaerts ueber 360 Grad ist kein lokales Minimum" (konjugierter Punkt in SO(3)): **nicht bestaetigt.** Dicke,
    schlaffe Faeden mit Kontakten halten den Vorwaertsast im Drehprotokoll bis 375 bis 721 Grad, je nach Laenge und
    Achse.
  - "Saege mit Sprung bei 360 Grad statt Sinus": auf dem erreichbaren Weg weder noch. Fuer das wahre E_min
    ungeprueft.
  - "Kraftspitze kurz vor 360 Grad, nicht bei 180 Grad":
    - L = 1,8: teilweise (Spitze bei 300 Grad auf 30..330).
    - L = 1,3: verfehlt (Spitze bei 120 Grad).
- **Nicht ableitbar, hier gemessen:**
  - Abkuehlen findet die Entwirrung nicht.
  - Spruenge (Zwischenrasten) bei 375 bis 721 Grad.
  - Achsenwanderung bei 360 Grad in einen gemeinsamen Endzustand.
  - Faktor 65 zwischen Ebene und Raum.
  - dE_360 faellt von 250 auf 41, wenn die Kontur von 1,3 d auf 1,8 d waechst.

## Grundsaetzlich: was folgt fuer halben Spin im Netz? [H, mit Ableitbarkeitsprobe]

1. **Zweiter Zustand je Knoten aus der Verdrillungsparitaet.**
   - Ein Knoten, der mit mindestens drei Faeden im Raum angebunden ist, hat ueber jeder Lage zwei topologische Klassen
     von Fadenzustaenden. 360 Grad fuehren von der einen in die andere, 720 Grad zurueck.
   - Zusammen sind Lage und Klasse ein Punkt von SU(2) statt SO(3) [M; L Newman 1942, Kugelzopfgruppe].
   - Das ist genau die Zusatzstruktur, die TWIST-SPIN-1 vermisst ("ein Zustand je Knoten erlaubt keine projektive
     Klasse").
   - **Ableitbarkeitsprobe:** Die Existenz des Labels ist Topologie, also ableitbar. Gemessen ist sein Preis
     (dE_360 = 41 bzw. 250 bei E_min(0) = 8,4 bzw. 5,1).
   - **Was die Rechnung hinzufuegt [G]:** Erreichbar sind nicht zwei, sondern viele metastabile Windungszustaende, etwa
     W = (1, 0, 1, 0) bei 720 Grad. Die saubere Z_2 ist eine Aussage ueber das globale Minimum, das Abkuehlen hier
     nicht erreicht.
2. **Quantenrotor auf SU(2) statt SO(3)** [L Peter-Weyl; Schulman 1968]:
   - Ein freier Rotor mit Lageraum SU(2) hat Zustaende mit allen j = 0, 1/2, 1, ...; auf SO(3) nur ganzzahlige. Die
     halbzahligen wechseln unter dem Zentralelement -1 (der 360-Grad-Drehung) das Vorzeichen.
   - **Einschraenkung [M]:** Der angebundene Knoten ist kein freier Rotor. Die Fadenenergie unterscheidet die Klassen
     (dE_360 > 0), das Potential ist also nicht invariant unter -1. Dann ist j keine gute Quantenzahl, und die
     Spinor-Kombination |P0> - |P1> ist kein Energiezustand.
   - Halbzahliger Spin waere nur naeherungsweise sichtbar, wenn dE_360 klein gegen die Rotationsenergie ist. Die
     Rechnung zeigt, dass dE_360 mit der Schlaffe faellt (Faktor 6 von 1,3 d auf 1,8 d); ob es gegen null geht, ist
     offen.
   - Ausserdem brechen feste Anker die Drehsymmetrie; "Spin" verlangt, dass sich das ganze Netz dreht.
3. **Finkelstein-Rubinstein [L]:**
   - Die Topologie erlaubt beide Sektoren. Ob eine 360-Grad-Drehung -1 gibt, ist eine zusaetzliche Eingabe (Phase auf
     der nichttrivialen Schleife; bei Skyrmionen ein Wess-Zumino-Term).
   - Die Statistik ist eine eigene Frage. FR verknuepfen Austausch und Drehung nur, wenn die Austauschschleife zur
     2-pi-Drehung homotop ist; Knoten eines festen Netzes werden nicht ausgetauscht.
   - Im Projekt: Fadenenden sind Fermionen (TWIST-PYRO-1), aber spinlos (TWIST-SPIN-1). Spin und Statistik kommen auf
     Finns Netz bisher aus verschiedenen Quellen.
4. **Bezug zu TWIST-SPIN-1 [H]:**
   - Die Paritaet liefert zwei Zustaende je Knoten, und die 360-Grad-Drehung tauscht sie (wie ein Pauli-X). Das ist die
     Kinematik eines Spinors.
   - Halber Spin entstuende erst, wenn beide Zustaende (fast) entartet waeren und die Dynamik den ungeraden Sektor
     waehlte.
   - Die Anbindung ist eine Zusatzannahme (eingesetzt, nicht entstanden). Dafuer ist sie mechanisch anschaulich und
     prueft sich am Netz selbst.

## Kartenvorschlaege (hoechstens zwei, je Lauf <= 10 min)

1. **GUERTEL-2: Sperre auf dem konstruierten Entwirrungsweg [H].**
   - **Bau:** Den Staley-Weg explizit bauen. Schalendrehungen g_s(r) = Rot(x, 2 pi f_aussen(r)) Rot(n(s), 2 pi
     f_innen(r)), n(s) dreht von x ueber y nach -x. Die Faeden bleiben radial monoton; fuer duenne Faeden ist das
     durchdringungsfrei.
   - **Rechnung:** Daraus den Anfangsstring zwischen der idealen 4-pi-Wicklung und dem Grundzustand bilden, mit der
     vorhandenen Stringmethode samt Sonde relaxieren und S mit dE_360 vergleichen. Zusaetzlich S vom gemessenen
     Zwischenrast-Zustand W = (1, 0, 1, 0) aus.
   - **Ableitbarkeitsprobe:**
     - Existenz des Wegs: ableitbar.
     - S = 0 in fuehrender Ordnung: hier widerlegt, weil der Vorwaertsast metastabil ist. Die Hoehe von S ist damit nicht
       ableitbar.
   - **Kann scheitern:** S >= dE_360, oder die Relaxation laesst den String an einer Kontaktsperre haengen. Laufzeit:
     String etwa 20 bis 30 s, Bau vernachlaessigbar.
2. **GUERTEL-SCHLAFF-1: Wird das Paritaetspaar mit mehr Schlaffe entartet? [H]**
   - **Rechnung:** dE_360 und E_min(720)/E_min(0) fuer Konturlaengen 1,3, 1,8, 2,5 und 3,5 d, nur bei 0, 360 und 720
     Grad, mit Temperaturleiter T0 = 0,5, 1, 2 (Sonde aktiv).
   - **Vorhersage [H]:**
     - dE_360 / E_min(0) faellt unter 1,5, sobald die Kontur die Wickellaenge deckt.
     - Schaetzung [M]: Einmal um die zweizaehlige Achse wickeln braucht 2 pi mal 0,9 = 5,6 quer zur Radialstrecke 1,8,
       zusammen etwa 5,9 Kontur, also ab etwa 3,3 d.
     - Gemessen bisher: 49 (1,3 d) und 4,9 (1,8 d).
     - Mit Temperatur 2 entwirrt bei 720 Grad mindestens eine von 5 Saaten.
   - **Ableitbarkeitsprobe:** Das Verschwinden des Dehnanteils ist geometrisch abschaetzbar, der Boden aus Biegung und
     Kontakten nicht. Ob Waerme die Entwirrung findet, ist nicht ableitbar.
   - **Kann scheitern:** Der Boden bleibt hoch, oder keine Saat entwirrt. Laufzeit je Laenge und Temperatur etwa 1
     bis 3 min (B = 15).

## Selbstanzeigen

1. **Rauchlauf 1 vor dem Plantext:** Er lief 15:16 bis 15:17 CEST, bevor PLAN.md geschrieben war. Ausgegeben wurden
   nur Laufzeit, Sondenwerte und Restkraefte, keine Energien und keine Windungen.
2. **Vor dem Einfrieren gesehen:**
   - Laufzeiten, Sondenwerte, Restkraefte (auch die hohe Spannung der Ebene bei 720 Grad).
   - Der Gegenprobe-Codetest (bis 90 Grad) schrieb Windungen in seine Datei; angesehen habe ich nur rc und Laufzeit.
   - Keine E_min-Werte.
3. **Aenderungen vor dem Einfrieren aufgrund der Rauchlaeufe:**
   - Drehschritt 4 -> 1 Grad; Relaxation je Schritt Vorgabe 200 (Rauchlauf 1: 100) -> 80; Gitter-FIRE 3000 -> 1500;
     nL 8000 -> 6000; nF 3000 -> 2500.
   - Schalter fuer den Ausschluss und Modus gegenprobe; Schutz gegen rho = 0.
   - GT0-Planregel auf 360 und 720 Grad beschraenkt (Packungsgrenze, PLAN 7.3); der Wortlaut verlangt weiter alle
     Vielfachen.
   - Ebene nur auf 7 Winkeln abgekuehlt (Rechenzeit).
4. **Nach dem Einfrieren:** Code und Vorhersagen nicht geaendert. Eine Regelanwendung wurde per Nachtrag 1 berichtigt
   (Punkt 6). Jeder Hauptlauf genau einmal, keine Wiederholung.
5. **Wirkungsloses Abkuehlen:**
   - Mit T0 = 0,5 und 6000 Schritten enden an den meisten Winkeln alle Saaten im Startzustand; die SE sind dann
     praktisch null, und die "3 SE"-Regeln sind leer erfuellt.
   - Auch E_min(0) ist wahrscheinlich nicht das wahre Minimum bei 0 Grad: Bei 60 bis 90 Grad liegt die Energie tiefer
     (2,8 gegen 8,4). Das erzeugt die negative Startdelle des Moments, an der GT2a und GT2b formal scheitern.
   - Unabhaengig davon scheitern GT2a an der Spitzenlage und GT2b am fehlenden Wechsel bei 360 Grad.
6. **Gleitkomma-Grenzfall (Nachtrag 1, PLAN.md Abschnitt 8):**
   - W = (1, 0, 1, 0) hat exakt Mittel |W| = 0,5, also "nicht entwirrt". Der Code zaehlte eine Saat wegen
     0,49999999999999994 als entwirrt und rechnete einen String zwischen zwei gleichartigen Zustaenden (S = 0,24 bzw.
     0).
   - Ich habe das erst beim Ansehen von sperre-L1.8-s0 bemerkt und die Regel auf gerundete W_i angewandt. Ergebnis:
     GT3 nicht auswertbar statt eingetroffen.
   - Beide Urteile stehen in auswertung.json (Code: haupturteile_nach_plan; berichtigt: nachtrag_1). Die Berichtigung
     entfernt ein falsch positives Urteil.
7. **Untaugliches Mass bei der allgemeinen Achse:** "Entwirrt" war ueber W um die Drehachse definiert. Wandert die
   Verdrillung auf eine andere Achse, zeigt W = 0 ohne Entwirrung. GT3 der allgemeinen Achse ist deshalb nur formal
   "eingetroffen" und nicht belastbar. Regel nicht geaendert, nur gekennzeichnet.
8. **Literatur:** 3 von 10 Abrufen (arXiv-PDFs per curl, Text per pdftotext); [S] nur aus diesen. Newman,
   Fadell/Van Buskirk, Finkelstein/Rubinstein, Schulman, Mermin, Braun/Kivshar und Adams sind Gedaechtnis [L].
9. **Werkzeuge:**
   - Lokal ausserhalb der Liste: ls, cat, head, tail, wc, sort, uniq, diff, paste, column, which, curl, pdftotext,
     Shell-Schleifen. Kein lokaler Interpreter.
   - Auf der .69 ausserhalb des Starters: mkdir, ls, cat, tail, grep, sha256sum, cp, mv, uptime.
   - Die Hauptlaeufe liefen als eine verkettete ssh-Befehlszeile nacheinander ueber kleintest.sh; kein Skript, kein
     Dienst.
   - Erste Codefassung per scp direkt nach code/ (neue Datei), spaetere ueber .neu und mv.
10. **Zeitbox:** 180 min ab 14:51:08 CEST. Hauptlaeufe beendet 15:58:46 CEST. Kein Journaleintrag, kein Peerbus, kein
    Commit.

## Dateien

- **Plan:** PLAN.md (mit Nachtrag 1), PLAN.md.eingefroren-20261004-152838, EINGEFROREN-SHA256.txt.
- **Code:** code/guertel.py, code/auswertung.py, je mit .eingefroren-20261004-152838.
- **Rauchlaeufe:** rauch-69/ (rauch.json, rauch.log; r2/ mit rauch.json, rauch2.log, gegen0.log und
  gegenprobe-codetest-tmax90-L1.8.json, dem nicht angesehenen Codetest).
- **Hauptlaeufe:** lauf-69/
  - protokoll-L*.json/npz, abkuehlen-L*-s*.json/npz, sperre-L*-s*.json, gegenprobe-L1.8.json
  - auswertung.json (mit nachtrag_1) und auswertung.maschine.json
  - Logs; PRUEFSUMMEN.txt und PRUEFSUMMEN-69-roh.txt
- **Synthetische Testeingaben** der Auswertung: testdaten-synthetisch/ (keine Ergebnisse).
- **Quellen:** quellen/ (drei arXiv-PDFs mit Text).
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde41-guertel/ (code/, rauch/, lauf/).
- **Federring und Drehungs-Cluster:** RUNDE-37/struktur-federring-1/BERICHT.md.

## Einfach gesagt

Wir haben im Computer einen kleinen Koerper an vier Faeden aufgehaengt, wie einen Knoten in Finns Tetraeder-Netz, und
ihn immer weiter gedreht. Nach der Mathematik des Guerteltricks muesste er sich nach zwei vollen Umdrehungen wieder
ganz entwirren lassen, nach einer aber nicht; genau das ist die Wurzel des halben Spins. In unserer Rechnung bleiben die
Faeden aber auch nach zwei Umdrehungen verheddert: Vorsichtiges Schuetteln und Abkuehlen findet den Entwirrungsweg
nicht, die Faeden rasten in Zwischenstellungen ein und springen nur ab und zu ein Stueck zurueck. Die Kraft beim Drehen
laeuft deshalb nicht wie ein Sinus hin und zurueck, sondern baut sich auf und bricht ruckweise ein, eher wie bei einer
Ratsche. Deutlich zeigt sich dagegen, wie viel die dritte Dimension hilft: Flach in der Ebene kostet eine Umdrehung etwa
65-mal so viel Energie wie im Raum.
