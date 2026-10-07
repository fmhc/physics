# KOPPLUNG-TETRA-1: Wie koppeln eckenverknuepfte Tetraeder, und traegt die gegenseitige Verdrehung wie ein Eichfeld ("Kleber")? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 16:47:47 CEST (date), vor jeder
  Rechnung.
- **Finn (04.10., Nachricht zwischen 16:45 und 16:47, woertlich):** "rechne einen kommplungsmechanismus zwischen
  tetraedern"
- **Zusammenhang:**
  - Farb-Frage (RUNDE-42.md, 16:39) und RUNDE-42/FARBE-SCHREIBTISCH.md: Eine Ecken-Kopplung spaltet das Biege-Triplett in
    1 + 2. Echte Farbe braeuchte Verbindungsgroessen, deren Energie nur von Schleifen abhaengt (Eichfeld, "Kleber").
- **Idee der Leitung [H]:**
  - In Finns Netz teilen sich Tetraeder Ecken. Ihre Mittelpunkte bilden ein Diamantgitter, die kuerzesten Schleifen sind
    Sechsringe.
  - Das ist die Topologie von beta-Cristobalit (SiO4-Tetraeder mit gemeinsamen Sauerstoff-Ecken; der Sauerstoff bildet
    ein Pyrochlor-Gitter) [L].
  - Solche Geruestgitter haben "starre Einheitsmoden" (rigid unit modes, RUM): gemeinsame Drehungen ganzer Tetraeder ohne
    Verformung, also ohne Energie, auf Flaechen bzw. Ebenen im k-Raum (Dove, Heine, Giddy, Hammonds u. a., 1990er) [L].
    Gemessen als diffuse Streuung.
  - TENSOR-EIS-PYRO-1, Bauweise A (Eichfreiheit an den Ecken), fand Nullmoden auf sechs Ebenenscharen k . a_m = 0
    mod 2 pi [P]. Ob das dieselben Ebenen sind, ist offen.
  - Die relative Verdrehung R_ij in SO(3) benachbarter Tetraeder ist eine natuerliche nichtabelsche Verbindungsgroesse.
    Haengt die Energie entlang der RUM nur von der Verdrehung um Sechsringe ab, verhielte sie sich wie ein Eichfeld; sonst
    wie ein massives ("Higgs") Feld.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Literatur (hoechstens 3 Abrufe, keine Websuche):** RUM in beta-Cristobalit bzw. eckenverknuepften Tetraedergeruesten
   an der Quelle (Dove u. a.; Hammonds u. a. 1996, Am. Mineral.; Giddy u. a. 1993, "split-atom"-Methode): Wo im k-Raum
   liegen die RUM, wie viele je k?
2. **Modell:**
   - Finns Netz als eckenverknuepfte Tetraeder auf dem Diamantgitter der Mittelpunkte.
   - (a) starre Tetraeder, Ecken per Feder verbunden ("split atom"); (b) verformbare Federtetraeder mit gemeinsamen Ecken.
   - Zuerst Altdaten bzw. Code aus TENSOR-EIS-PYRO-1 (Bauweise A) und QBALL-PYRO-1 pruefen; nichts doppelt rechnen.
3. **Messgroessen:**
   - Nullmoden je k im ganzen Brillouin-Gebiet: Lage, Zahl, Dimension der Flaechen.
   - Vergleich mit Literatur und mit den sechs Ebenenscharen von TENSOR-EIS-PYRO-1.
   - Aufspaltung des Biege-Tripletts bei Ecken-Kopplung.
   - **Eichprobe:** Energie einer kleinen Ringverdrehung (sechs Tetraeder um einen Sechsring, gleiche Holonomie)
     gegen eine Verdrehung mit derselben Holonomie, aber anders auf die Tetraeder verteilt. Gleich heisst eichartig.
4. Plan, Rauchlauf, Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KT0 | Kontrollen: Einzel-Federtetraeder omega^2 = (k/m){4; 1,1; 2,2,2}; ein eckenverknuepftes Paar spaltet das Triplett in 1 + 2 (C3v) | 90 % |
| KT1 | [L] Das starre Geruest hat RUM auf Flaechen im k-Raum (nicht nur an Punkten), wie fuer beta-Cristobalit beschrieben | 70 % |
| KT2 | [H] Die RUM-Flaechen fallen mit den sechs Ebenenscharen aus TENSOR-EIS-PYRO-1 (Bauweise A) zusammen | 45 % |
| KT3 | [H] Eichprobe: Die Energie haengt entlang der RUM nur von der Ring-Holonomie ab (Unterschied der Verteilungen < 5 %) | 20 % |

**Bedeutung (vorab):**
- **KT1 und KT2 treffen ein:** Finns Netz ist mechanisch ein bekanntes Geruest. Seine weichen Drehmoden sind dieselben
  Nullmoden wie in der Tensor-Eis-Rechnung; es gibt messbare Gegenstuecke in echten Kristallen.
- **KT3 trifft ein:** Die gegenseitige Verdrehung wirkt wie ein nichtabelscher "Kleber" (Eichfeld) [H]; naechster Schritt
  waeren Farb-Tripletts als Ladungen.
- **KT3 verfehlt:** Die Verdrehung kostet Energie wie ein massives Feld; Kopplung ja, Kleber nein. Fuer Farbe braeuchte es
  dann String-Netz-Regeln.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, auf den Spuren, die die Leitung beim Start eintraegt; je Lauf
  <= 10 min, 1 Thread. Zeitbox 150 min.
