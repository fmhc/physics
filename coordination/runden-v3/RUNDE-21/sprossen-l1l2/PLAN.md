# PLAN SPROSSEN-L1L2 (Runde 21)

- Code-Agent. Start 2026-10-02 17:57:17 CEST (date). Plan geschrieben ab 18:09:20 CEST (date), vor jedem L4-Lauf. Bis
  dahin auf der .69 nur py_compile (direkt, 16:09 UTC), Zeilenliste (16:09:10 UTC) und der Start der Hintergrundprofile.
- Gelesen: KARTE.md (mit Berichtigung 17:56:55); RUNDE-20/sprossen-vorab: KARTE, KARTE-NACHTRAG-1, PLAN, ERGEBNIS,
  code/; RUNDE-19/huellen-dipol: PLAN, ERGEBNIS, code/, aus/ (stellen.json, umlauf-*.json, zeilen.json);
  RUNDE-20/huellen-quadrupol: PLAN, ERGEBNIS, code/, aus/ (stellen.json, umlauf-alle-*.json, zeilen.json,
  prof-st1/profile-info.json). Selbstanzeige (ausserhalb der Freigabe, gelesen vor diesem Plan): sprossen-vorab/hilfs/
  (l4.sh, test.sh, laufzeiten.sh, tab.jq, fort-zeilen.jq, Anfang von bekannte.json, nur l = 0), die KARTE.md von
  HUELLEN-DIPOL und HUELLEN-QUADRUPOL und die Dateiliste von huellen-quadrupol/hilfs/. Nichts aus Sperrbereichen.
- Verbindlich (Karte): Annahmekriterium (Kurve nur ueber Stetigkeit von rho und Rang), Pflichtpruefung L4 vor dem
  Einfrieren, Vorhersagetabellen (Satz A formal, Satz B nur berichtet), W0 bis W4, Bedeutung. Nichts davon wird nach dem
  Ergebnis geaendert. **[Lesart]**-Stellen sind markiert.
- Code (code/): unveraendert kopiert und per sha256 mit den Vorlaeuferberichten verglichen: dipol.py 0094476d...
  (HUELLEN-DIPOL, Endfassung), quadrupol.py de6b6a08... (HUELLEN-QUADRUPOL), huellen_leiter.py 68c0a1fb...,
  stille3.py 1d15a38c..., beutel.py f831e818.... Neu: code/sprossen_l1l2.py (Entwurf sha256 544f75a2...; Befehle
  liste, profile, test, ausw, fortfehler). Es importiert fuer l = 1 dipol.py, fuer l = 2 quadrupol.py (je eigener
  Prozess, Argument ell=1 bzw. ell=2) und benutzt deren unveraenderte Kette.
- Hilfsdateien: hilfs/bekannte-l1.json (19 Stellen, R19 stellen.json, Stufe 1, dazu Newton-Lagen und Rechteck-Umlauf
  beider Stufen aus umlauf-A/P-st1/2.json), hilfs/bekannte-l2.json (15 Stellen, R20 entsprechend aus umlauf-alle-st*),
  gebaut mit hilfs/bekannte.jq.

## 1 Verfahren (Code wie HUELLEN-DIPOL und HUELLEN-QUADRUPOL, nur andere Startpunkte)

- **Hintergruende:** HL.cmd_profile (Saat BEUTEL Q = 200, Fortsetzung), Stufe 1 hp 0,01, Stufe 2 hp 0,005. Zeilen nach
  der Runde-18-Regel wie HUELLEN-DIPOL, nur mit Untergrenze 0,78 statt 0,80 (HL.W2_UNTEN = 0,78): 87 Zeilen; Zeilen 0
  bis 70 gleich der Dipol-/Quadrupol-Liste (sha256 der jq-Auszuege gleich), dann 16 Zeilen 0,8008 bis 0,78 (R bis etwa
  26). Die dortige Zeile 71 (erzwungene Untergrenze 0,80) entfaellt. Profilvergleich Zeilen 0 bis 70 gegen
  HUELLEN-QUADRUPOL (profile-info.json, Erwartung bitgleich).
- **Newton auf W = m_ac + i m_bc:** S3.newton_E1 wie in HL.cmd_umlauf der Vorlaeufer (hoechstens 12 Schritte, Schritt
  auf 0,01 gedaempft, konvergiert bei Schritt < 1e-10), Anker = naechste Zeile mit omega^2 <= Start (HL.cmd_umlauf).
  Kanalfunktionen der l-Fassung (dipol.py bzw. quadrupol.py).
- **Start:** omega^2 = lineare Interpolation in der Tabelle (Rchi, omega^2) der eigenen Profile Stufe 1 beim Start-R
  (beide Stufen gleich); rho = rho_fort(Start-R) (Abschnitt 3). Nachstarts bei R_ziel - 0,25, dann + 0,25 (Karte);
  Abbruch beim ersten lokal angenommenen Versuch.
- **R einer Wurzel** = Rchi (chi = 1/2) des Profils bei omega^2 der Wurzel (auf dem Ankergitter).
- **Rechteck-Umlauf von W:** S3.umlauf_mit_rueckfall (16 Punkte je Kante, Verfeinerung bis Sprung < 0,4 rad, Rueckfall
  auf Halbbreite 1e-4), Halbbreite min(1e-3; 0,4 Abstand zum E1-Rand; 0,25 Luecke; 0,5 Zeilenabstand) wie
  HL.cmd_umlauf. Luecke = HL.luecke in der Zeile an der Wurzel, Zeilenabstand = Abstand der Zeilen um omega^2 der Wurzel.

## 2 Annahme einer Stelle (Testcode, derselbe fuer L4 und Test)

Je Ziel (l, k, R_ziel) und Stufe, an der Newton-Wurzel (alle Pflicht):

1. **konv:** Newton konvergiert und |W| <= 1e-9 (Karte). |W| < 1e-10 wird berichtet.
2. **Rangabfall:** sigma2/sigma1 von G <= 1e-6 und Bereich E1.
3. **Rang:** In der Zeile bei omega^2 der Wurzel (HL.zeile_k, l-Fassung) hat die naechste Nullstelle von m_bc den Rang k
   von unten und liegt auf <= 1e-6 bei rho der Wurzel.
4. **Stetigkeit:** |rho_Wurzel - rho_fort(R_Wurzel)| < 0,1 d_nb (Abschnitt 3).
5. **Fenster:** |R_Wurzel - R_ziel| <= 0,5 (Karte: gefunden heisst innerhalb +-0,5).
6. Fuer lokal angenommene Versuche: Rechteck-Umlauf (Abschnitt 1).

Ueber beide Stufen **angenommen**, wenn 1 bis 5 auf beiden Stufen erfuellt sind, der Rechteck-Umlauf auf beiden Stufen
aufgeloest und +-1 ist und die Wurzeln beider Stufen in omega^2 und rho auf <= 1e-6 uebereinstimmen. Gefunden =
angenommen (das Fenster ist Teil der Annahme). R_gefunden = R_Wurzel Stufe 1. **Keine Knotenzahl**; sie wird nur
berichtet. Im Test ist R_ziel = P_lin (Auftrag: Start bei P_lin); die gefundene Stelle wird einmal gesucht und gegen
P_lin und P2 gemessen.

## 3 Fortsetzung, Nachbarabstand, Schwelle (vorab festgelegt)

- **Fortsetzungsformel:** rho_fort(R) = Polynom in x = 1/R (Lagrange) durch die Stuetzstellen, ausgewertet bei 1/R;
  drei Stuetzstellen: quadratisch, zwei: Gerade. Stuetzstellen sind bekannte Stellen der Kurve (l, k) (Stufe-1-Lagen
  R, rho aus stellen.json der Vorlaeufer).
- **Stuetzstellen "vor":** die letzten drei bekannten Stellen der Kurve mit R < R_ziel - 1; sind es nur zwei, die Gerade
  durch beide. Neu gefundene Stellen werden **nicht** verwendet (keine Verkettung); die zweite Sprosse ist also zwei
  Sprossen weit fortgesetzt.
- **Ersatz "formal" [Lesart]:** Liegen vor dem Ziel weniger als zwei bekannte Stellen, gilt die Fortsetzung des Tests
  fuer diese Kurve (die letzten drei bzw. zwei bekannten Stellen). Das kommt nur in L4 vor, an drei Zielen: l = 1, k = 3
  bei 15,584 und 18,1 (die Kurve hat nur diese zwei Stellen) und l = 2, k = 2 bei 15,268 (davor nur 12,715). Dort ist
  die Zielstelle selbst Stuetzstelle und die Stetigkeitspruefung nur formal; das wird je Ziel markiert. Grund: Ohne
  Ersatz waere L4 an diesen drei Zielen vorab zum Scheitern bestimmt, denn aus frueheren Stellen gibt es dort keine
  Fortsetzung.
- **Im Test gilt immer "vor"** (alle Ziele >= 20,09, alle bekannten Stellen <= 19,38):
  - l = 1: k = 0 aus 14,161 / 16,593 / 19,02; k = 1 aus 13,622 / 15,839 / 18,024; k = 2 aus 14,745 / 17,094 / 19,378;
    k = 3 Gerade durch 15,584 / 18,1.
  - l = 2: k = 0 aus 12,694 / 15,172 / 17,63; k = 1 aus 14,301 / 16,565 / 18,787; k = 2 aus 12,715 / 15,268 / 17,68.
- **Abstand zur Nachbarkurve d_nb:** In der Zeile bei omega^2 der Wurzel der kleinere Abstand der Nullstelle mit Rang j
  (naechste zur Wurzel) zu den Nullstellen mit Rang j - 1 und j + 1; fuer j = 0 nur j + 1, fuer die oberste nur j - 1.
  Die Raender von E1 zaehlen nicht.
- **Schwelle:** Fortsetzungsfehler < 0,1 d_nb (Karte).
- **Berichtet:** Fehler, d_nb und Verhaeltnis je Ziel und Stufe; dazu (Befehl fortfehler, reine Datenrechnung) die
  Fortsetzungsfehler an **allen** bekannten Stellen aller Kurven (l = 1: 19, l = 2: 15), fuer einen und zwei
  Sprossenschritte, nur mit Stuetzstellen "vor", im Verhaeltnis zur Luecke gap der Vorlaeufer (stellen.json; diese
  zaehlt auch den Abstand zum E1-Rand).

## 4 Pflichtpruefung L4 (vor dem Einfrieren)

- **Ziele (letzte zwei bekannte Stellen jeder Kurve beider Saetze, R wie Karte bzw. Vorlaeuferbericht):**
  - l = 1: k = 0: 16,593 / 19,02; k = 1: 15,839 / 18,024; k = 2: 17,094 / 19,378; k = 3: 15,584 / 18,1.
  - l = 2: k = 0: 15,172 / 17,63; k = 1: 16,565 / 18,787; k = 2: 15,268 / 17,68.
  - 14 Ziele, beide Stufen, genau der Testcode (Befehl test, Modus l4), danach ausw l4. Stuetzstellen "vor" an 11,
    "formal" an 3 Zielen (Abschnitt 3).
- **Bestanden, wenn alle 14 angenommen sind.** Berichtet: Abstand der Wurzel zur bekannten Newton-Lage der Vorlaeufer
  (je Stufe) und zur Halbierungslage, Umlauf gegen den bekannten Rechteck-Umlauf, Fortsetzungsfehler, d_nb.
- Nicht bestanden: nur das Kriterium berichtigen (nicht Ziele, Vorhersagen oder Wertung), erneut pruefen, jeden
  Durchgang in 4a dokumentieren. Erst nach einem bestandenen Durchgang einfrieren.
- **[Lesart] W0** wird am ersten Durchgang mit dem unveraenderten Entwurf gewertet; spaetere Durchgaenge werden berichtet.
- Vor dem Einfrieren: fortfehler rechnen und an allen bekannten Stellen ansehen (Lehre aus Runde 20).
- Die Umlaeufe aus L4 an der letzten bekannten Stelle jeder Kurve sind die Anfangsglieder fuer W3.

### 4a Durchgaenge (eingetragen ab 18:15:04 CEST, date, vor dem Einfrieren)

- **Durchgang 1 (Entwurf unveraendert, code/sprossen_l1l2.py sha256 544f75a2...): bestanden, 14 von 14 angenommen.**
  Sechs Teillaeufe 16:11:57 bis 16:14:16 UTC (rc 0, 68 bis 97 s), formale Auswertung ausw l4 16:14:27 UTC
  (aus/l4-d1/l4-auswertung.json). Alle 14 im ersten Start (Versuch 0), beide Stufen, Newton in 3 bis 4 Schritten.

| l | k | R Karte | R gefunden | Wurzel - Newton-Lage Vorlaeufer St1 / St2 (max omega^2, rho) | Umlauf St1/St2 (bekannt) | Stufenabstand | Fortsetzungsfehler / d_nb (Art) |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 16,593 | 16,59339 | 8e-15 / 2e-14 | +1/+1 (+1) | 1,6e-10 | 8,2e-6 / 0,190 = 4,3e-5 (vor) |
| 1 | 0 | 19,02 | 19,01986 | 8e-14 / 4e-14 | -1/-1 (-1) | 2,0e-10 | 2,6e-6 / 0,183 = 1,4e-5 (vor) |
| 1 | 1 | 15,839 | 15,83855 | 8e-14 / 4e-14 | +1/+1 (+1) | 5,9e-11 | 8,5e-4 / 0,0625 = 0,0136 (vor) |
| 1 | 1 | 18,024 | 18,02420 | 5e-14 / 3e-14 | -1/-1 (-1) | 4,3e-11 | 2,3e-4 / 0,0502 = 0,0046 (vor) |
| 1 | 2 | 17,094 | 17,09391 | 1e-13 / 2e-14 | +1/+1 (+1) | 3,0e-10 | 3,2e-4 / 0,0550 = 0,0058 (vor, Gerade) |
| 1 | 2 | 19,378 | 19,37795 | 5e-14 / 9e-15 | -1/-1 (-1) | 3,3e-10 | 1,18e-3 / 0,0441 = 0,0267 (vor) |
| 1 | 3 | 15,584 | 15,58439 | 7e-14 / 3e-15 | -1/-1 (-1) | 1,1e-9 | 5,3e-8 / 0,0766 = 6,9e-7 (formal) |
| 1 | 3 | 18,1 | 18,09989 | 2e-14 / 5e-14 | +1/+1 (+1) | 1,1e-9 | 5,6e-8 / 0,0639 = 8,8e-7 (formal) |
| 2 | 0 | 15,172 | 15,17158 | 2e-15 / 7e-15 | -1/-1 (-1) | 5,4e-10 | 1,0e-4 / 0,210 = 4,9e-4 (vor) |
| 2 | 0 | 17,63 | 17,62967 | 3e-14 / 6e-14 | +1/+1 (+1) | 4,7e-10 | 1,3e-5 / 0,198 = 6,7e-5 (vor) |
| 2 | 1 | 16,565 | 16,56505 | 1e-14 / 8e-14 | +1/+1 (+1) | 1,2e-9 | 1,50e-3 / 0,0685 = 0,0219 (vor) |
| 2 | 1 | 18,787 | 18,78695 | 4e-14 / 6e-14 | -1/-1 (-1) | 9,5e-10 | 4,0e-4 / 0,0559 = 0,0071 (vor) |
| 2 | 2 | 15,268 | 15,26846 | 9e-14 / 5e-14 | -1/-1 (-1) | 3,4e-9 | 8,2e-10 / 0,0770 = 1,1e-8 (formal) |
| 2 | 2 | 17,68 | 17,67979 | 8e-16 / 3e-14 | +1/+1 (+1) | 2,5e-9 | 2,88e-3 / 0,0618 = 0,0465 (vor, Gerade) |

  - Rang = k an allen 14 auf beiden Stufen; |W| <= 2,1e-11, sigma2/sigma1 <= 2,1e-11; Rechteck im ersten Versuch
    aufgeloest (groesster Sprung 0,33 bis 0,40 rad, 68 bis 80 Randpunkte, Halbbreite 1e-3, nur l = 1, k = 2 / 19,378:
    9,6e-4). Die Wurzeln liegen auf <= 1e-13 an den Newton-Lagen der Vorlaeufer (gleicher Code); Umlauf = bekannter
    Rechteck-Umlauf an allen 14.
  - Stetigkeit "vor" (11 Ziele): hoechstens 0,0465 (l = 2, k = 2 / 17,68, Gerade; Erwartung Abschnitt 7: ~0,05).
    "formal" (3 Ziele): <= 1e-6, ohne Trennschaerfe (Zielstelle ist Stuetzstelle).
- **Fortsetzungsfehler an allen bekannten Stellen** (Befehl fortfehler 16:14:27 UTC, aus/fortfehler.json, Verhaeltnis zur
  Luecke der Vorlaeufer; nur Stuetzstellen "vor"):
  - Ein Schritt, Maximum je Kurve: l = 1: k = 0: 0,0049 (Nr 4, Gerade); k = 1: 0,014 (Nr 12); k = 2: 0,027 (Nr 19).
    l = 2: k = 0: 0,016 (Nr 4, Gerade); k = 1: 0,022 (Nr 11); k = 2: 0,049 (Nr 13, Gerade).
  - Zwei Schritte, Maximum je Kurve: l = 1: k = 0: 0,012 (Nr 6, Gerade); k = 1: 0,045 (Nr 12, Gerade) und 0,044
    (Nr 15, quadratisch); k = 2: 0,010 (Nr 19, Gerade). l = 2: k = 0: 0,038 (Nr 6, Gerade); **k = 1: 0,072 (Nr 15,
    quadratisch aus Nr 3, 5, 8)**; k = 2: nicht berechenbar.
  - Befund: Alle Werte liegen unter der Schwelle 0,1. Zwei Schritte weit ist der Abstand zur Schwelle aber klein (0,072
    auf l = 2, k = 1). Auf jungen Kurven ist das quadratische Polynom zwei Schritte weit nicht besser als die Gerade
    (l = 2, k = 1: Gerade 0,010 an Nr 11, Parabel 0,072 an Nr 15; l = 1, k = 2: Parabel 0,027 einen Schritt weit an
    Nr 19, Gerade 0,010 zwei Schritte weit). Fuer die zweiten Sprossen im Test (zwei Schritte) ist deshalb eine
    Ablehnung echter Stellen am Stetigkeitskriterium moeglich, am ehesten auf l = 2, k = 1 und l = 1, k = 1. Das Kriterium
    bleibt unveraendert (Karte; L4 bestanden); ein solcher Fall wird im Bericht als Grenze des Kriteriums ausgewiesen.
- **W0 (erster Durchgang): eingetroffen.** Kein zweiter Durchgang.

## 5 Test (nach dem Einfrieren)

- Ziele = P_lin (Karte, woertlich), beide Stufen, Befehl test (Modus test), danach ausw test:
  - Satz A: l = 1: k = 0: 21,447 / 23,874; k = 1: 20,209 / 22,394; k = 2: 21,662 / 23,946; l = 2: k = 0: 20,088 /
    22,546; k = 1: 21,009 / 23,231.
  - Satz B: l = 1, k = 3: 20,616 / 23,132; l = 2, k = 2: 20,092 / 22,504.
- P2 (Karte, mit Berichtigung der Leitung): l = 1: 21,443 / 23,862; 20,182 / 22,316; 21,607 / 23,789; k = 3 keine.
  l = 2: 20,071 / 22,498; 20,973 / 23,129; Satz B 19,972 / 22,162.

## 6 Wertung (vorab operationalisiert)

- **W0:** L4 bestanden (erster Durchgang, Abschnitt 4).
- **W1:** eingetroffen, wenn alle 5 ersten Sprossen von Satz A angenommen sind und je |R_gefunden - P_lin| <= 0,06.
  Sonst nicht.
- **W2:** eingetroffen, wenn mindestens 4 der 5 zweiten Sprossen von Satz A angenommen sind mit
  |R_gefunden - P_lin| <= 0,15. Sonst nicht.
- **W3 [Lesart wie SPROSSEN-VORAB V3]:** Folge je Satz-A-Kurve: letzte bekannte Stelle (Umlauf aus L4), erste neue,
  zweite neue. Gewertet werden Schritte zwischen direkt aufeinander folgenden angenommenen Gliedern (ein nicht
  angenommenes Glied unterbricht). Ein Schritt ist erfuellt, wenn der Rechteck-Umlauf beider Glieder auf beiden Stufen
  gleich ist und das Vorzeichen wechselt. Eingetroffen, wenn alle gewerteten Schritte erfuellt sind und jede der 5
  Satz-A-Kurven mindestens einen gewerteten Schritt hat; nicht eingetroffen, wenn ein Schritt nicht erfuellt ist; sonst
  offen.
- **W4 [Lesart]:** Mittlere Abweichung = Mittel von |R_gefunden - P| ueber die angenommenen Satz-A-Sprossen (dieselbe
  Menge fuer beide Regeln). Eingetroffen, wenn das Mittel fuer P2 kleiner ist als fuer P_lin; nicht eingetroffen sonst;
  offen, wenn keine Satz-A-Sprosse angenommen ist. Berichtet: Zahl n, beide Mittel, vorzeichenbehaftete Mittel.
- **Bedeutung (Karte woertlich; Vorrang [Lesart] wie SPROSSEN-VORAB):**
  - W1 bis W3 eingetroffen (L4 bestanden) -> "Die Sprossenregel sagt auch l = 1- und l = 2-Stellen vorab voraus [H, im
    Modell gestuetzt]."
  - Sonst, wenn bei Satz A eine Sprosse nicht gefunden ist oder angenommen mit |R_gefunden - P_lin| > 0,3 -> "Die Regel
    traegt fuer l > 0 nicht."
  - Sonst Zwischenausgang ohne diese Aussagen.
  - Unabhaengig davon: W4 eingetroffen -> "Der schrumpfende Abstand verbessert die Vorhersage; das stuetzt das Bild
    Delta R ~ pi/k_innen(R) [H]."
  - Der Ausloeser der Abweichungsaussage (welche Sprosse, angenommen oder nicht) wird immer berichtet, auch wenn der
    Vorrang ihn ueberdeckt.
- **Satz B:** nur berichtet (gleiche Rechnung, Abweichung zu P_lin und P2, Umlauffolge), keine Wertung.

## 7 Erwartung vorab (Schreibtisch, [H], nicht gerechnet)

- Fortsetzungsfehler (Handrechnung aus den Berichtstabellen): l = 1, k = 2 bei 17,094 aus der Geraden durch 12,281 /
  14,745: ~3e-4 (Luecke 0,055, also ~0,006 der Luecke); zwei Schritte bis 19,378: ~5e-4. l = 2, k = 2 bei 17,68 aus der
  Geraden durch 12,715 / 15,268: ~2,9e-3 bei Luecke 0,059, also ~0,05 der Luecke: der knappste L4-Fall (Schwelle 0,1).
- Satz B im Test: l = 2, k = 2 quadratisch, das quadratische Glied traegt bei 20,09 ~1,6e-3; l = 1, k = 3 als Gerade
  (die Steigung in 1/R ist auf der jungen Kurve l = 1, k = 2 fast fest: 3,40 / 3,43 / 3,29). Erwartung: Stetigkeit im
  Test unter ~0,05 der Nachbarabstaende.
- Abweichungen von P_lin: negativ (Abstand schrumpft). Knapp: l = 1, k = 2 (Abstaende 2,349 -> 2,284): erste Sprosse
  nach P2-Logik ~ -0,055 (Toleranz 0,06), zweite ~ -0,16 (Toleranz 0,15).
- Risiko: Die neuen Zeilen jenseits R = 19,4 sind mit diesem Code noch nie gerechnet; chi(0) faellt bis R ~ 24 auf
  etwa 1e-11 (Runde-18-Grenze fuer Rundung erst bei R ~ 39).

## 8 Laeufe (.69, kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4, cpu6, je <= 600 s)

- Ordner /home/fmh/fmhc-physics-remote/runde21-sprossen-l1l2/ (code/, hilfs/, aus/, prof-st1/, prof-st2/), Pfade absolut.
- V0: py_compile, Zeilenliste, Profile beider Stufen (Vergleich mit HUELLEN-QUADRUPOL). V1: L4 in Teilen je l und Stufe,
  ausw l4, fortfehler. Einfrieren. V2: Test in Teilen je l und Stufe, ausw test.
- Programmfehler werden behoben und mit sha256 dokumentiert; das Verfahren bleibt. Nachtraege nur eingefroren
  (PLAN-NACHTRAG-n.md.eingefroren-*), als nachtraeglich markiert.
