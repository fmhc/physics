# Runde 12 (v3): Antiferromagnet-Kanaltest, 2D-Leiter praezise, Paper-Entwurf gegen die Beweise, getriebener Ball

Leitung: claude-primary. Angelegt: 2026-09-30 20:08:02 CEST (date). Explorativ, keine formale Bestaetigung. Runde 11 ist
abgeschlossen (RUNDE-11.md: Abschaetzung, Einfach gesagt; Journal claude-runde-v3-11-20260930, Index nr 547; Sicherung
.69 -> TS440 seit 20:06:21).

## Rahmen

- Rechenorte: .69 ueber kleintest.sh (Spuren p4000a, p4000b, cpu bis cpu6).
- Hoechstens drei Agenten zugleich.
- Offene Entscheidungen Finns (unveraendert): Ollama-Stopp (WM-1-MB, B28, CX-1 warten), restic-Aufraeumen auf dem TS440,
  APS-Datenzugang (ST-1), Budget fuer groessere 3D-Laeufe.

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| AFM-KANAL-1 | R11 MESS-3A | Hat ein Antiferromagnet-Ball (Anisotropie vierter Ordnung, Haematit-artig) einen eingebetteten Wandzustand im geschlossenen Kanal? Regel in RUNDE-12/afm-kanal1/KARTE.md (20:08:02) | Code-Agent |
| LEITER-2D-PRAEZ | R11 LEITER-2D | Bricht die 2D-Leiter nach n = 6 ab (Quasi-BIC), oder verliert der Code an der Duennwandgrenze Genauigkeit? | Code-Agent |
| PAPER-LESUNG v0.9 | Codex-Manuskript (Finn beauftragt; v0.1 am 30.09., v0.9 am 1.10. 07:00 UTC) | Behauptet der Entwurf "Radiative cancellations and localized linear modes ..." mehr, als die Beweise und Lesungen tragen? | pruefer-opus (Neustart 1.10.) |
| **Bio 45, Zufallskarte** | R2, gezogen 20:07:32 mit `shuf -n 1` aus den Gen-0-Eintraegen "parken" (erster Zug 20:07:22 ergab Chem 8, in R11 verworfen; Pool nachgetragen, neu gezogen) | Getriebener, gedaempfter Q-Ball als dissipative Struktur. R2: kein stabiler getriebener Ball. Neu: Bezug zu spinstromgetriebenen AFM-Solitonen (Ovcharov 2023) | Leitung, Schreibtisch zuerst |
| SPIN-D | R11 Vormerkung | Diracfeld an Q-Ball koppeln: gebundene Fermionzustaende (Scout-Treffer arXiv:2606.30964) | wartet auf einen freien Platz |
| CEMZ-EBENE | R11 CEMZ-MESS | Schreibtischkarte (l_eff, \|alpha\|) mit Tabellenwerten | feldforscher (seit 01.10. 18:09) |

- Bei Codex laufen (nicht doppeln):
  - nichtlineare Folge: gekoppeltes L0/L2-Problem bei nu = 2 rho fuer T2
  - Hopf-3D-Stationaritaet bei Viertelladung
  - BIC-Paper v0.1 (model-lab/papers/qball-bic-ladder-20260930/; Autor Finn Malte Hinrichsen, keine Veroeffentlichung)

## Tests: Ergebnisse
### Bio 45 Zufallskarte, Schreibtisch der Leitung (eingetragen 2026-09-30 20:10:35 CEST)

- Bestand R2: Im 1D-NLS mit Pumpe und Daempfung entstand kein stabiler getriebener Ball; mit Treiber zerfiel er schneller.
- L4 [L?, nur aus dem Gedaechtnis, nicht an der Quelle]:
  - Angetriebene, gedaempfte NLS-Solitonen sind Literatur, etwa Barashenkov/Smirnov, Phys. Rev. E 54, 5707 (1996),
    mit Existenz- und Stabilitaetskarte.
  - Dissipative Solitonen allgemein: Akhmediev.
  - Eine eigene Pruefung der arXiv-Nummer ging fehl: Die geratene Nummer patt-sol/9603002 ist eine andere Arbeit.
    Keine Nummer raten.
- **Neuer Bezug [H]: angetriebener AFM-Ball.** Ovcharov u. a. 2023 (in RUNDE-11/mess3a/quellen/) treiben AFM-Solitonen
  per Spinstrom gegen die Gilbert-Daempfung.
  - Gibt es dort eine stille Stelle, dann hat die Atmungsmode an ihr nur die innere Daempfung als Breite. Die Abstrahlung
    faellt dort ja weg.
  - Neben den stillen Stellen dominiert die Abstrahlung (Guete 1 bis 10 wie im NLS-Mittelbereich, R10).
  - Messsignatur waere eine sehr schmale Atmungsresonanz im Spektrum des angetriebenen Balls, deren Breite an der Leiter
    gegen die Daempfungsgrenze faellt.
  - Guete an der stillen Stelle etwa 1/alpha. Haematit alpha ~ 1e-5 ist nur ein Zitat in Ovcharov (MESS-3A G4, nicht
    an der Quelle gelesen).
- **Folge:** Die Karte haengt an AFM-KANAL-1. Nur wenn dort ein eingebetteter Wandzustand existiert, lohnt eine
  Rechenkarte "getriebener AFM-Ball, Atmungsspektrum". Bis dahin parken mit diesem Vermerk.


## Abschaetzung

(am Rundenende)

## Einfach gesagt

(am Rundenende)

## Unterbrechung und Neustart (Leitung, eingetragen 2026-10-01 17:12:47 CEST)

- Am 30.09. gegen 20:10 brachen alle drei Agenten (AFM-KANAL-1, LEITER-2D-PRAEZ, PAPER-LESUNG v0.1) an einem
  API-Wochenlimit ab. Uebrig blieb nur eine Teildatei der Paper-Lesung, umbenannt in
  LESUNG-PAPER-V01.abgebrochen-2010.md.
- Neustart am 01.10. nach 17:11:36 (Finn: "mach weiter", "weiter"), nach einem Kontowechsel.
  - Die Paper-Lesung zielt jetzt auf die kanonische Fassung v0.9 (paper.pdf sha256 6119315eb55dc697...).
  - Dazu kommt das Dipolpuls-Ergebnis vom 01.10. als Quelle.
- Sicherung der Runde 11 nach TS440: rc = 0 (Log r11, 30.09. 20:06:25).

### Codex vom 30.09. abends bis 01.10. (Peerbus; nur zusammengefasst, nicht nachgerechnet)

- **Funktionsrunde (Finn direkt an Codex):** 6 Funktionen x 3 Runden x 10 = 180 Ideen mit Reviews
  (function-ideation-3rounds/).
  - Daraus die Kontrollsuite function-controls in model-lab/claim-gauntlet/: 107 Gates bestanden auf der .69, CUDA.
  - Ausdruecklich kein Q-Ball- oder SU(3)-Beweis.
- **3D-Fruehwachstum und nichtlineare Verdichtung (Pilot, .69 P4000 CUDA):**
  - Ein fast homogener geladener Hintergrund entwickelt unter der vollen NLKG von selbst starke raeumliche
    Verdichtungen.
  - Codex nennt das ausdruecklich keinen Bildungs- oder Stabilitaetsnachweis.
- **Paper v0.9** (01.10. 07:00 UTC, 17 Seiten): neu eine modellinterne Quellprojektion.
  - Ein orthogonales homogenes Wellenpaket belaedt die BIC-Mode nicht.
  - Eine lokale Quelle kann es.
  - Keine Veroeffentlichung, keine Einreichung.
- **Dipolpuls-Anregung der T2-Mode (01.10. 15:01/15:04 UTC):** In Kugelarithmetik mit geerbten Huellen ist streng
  gezeigt, dass ein vorab festgelegter lokaler Dipolpuls die zertifizierte l = 1-Mode im linearen Modell anregt.
  - |L| > 0 eingeschlossen.
  - Fuer eine Traegerverstimmung |delta| <= 1/2 gilt |L(delta)| > 7/8000.
  - Zwei Nichtautor-Pruefungen. Keine Lebensdauer, keine Linienbreite, keine Bildung von Q-Baellen.
- Weitere Codex-Arbeiten am 01.10.: L2-Randbudget, Residual- und Operator-Piloten, Bildungs-Reviews; je mit eigenen
  Grenzen, hier nicht einzeln gewertet.

## Finn: "wie finden wir eine ueberleitung zu quarks?" (01.10., eingetragen 2026-10-01 17:14:36 CEST)

- Wortlaut: "ich will weiter gehen mit dem paper bzw mit dem betrachtungsobjekt da. wie finden wir eine ueberleitung zu
  quarks?"
- **Antwort der Leitung (Chat):** Die Bruecke laeuft ueber den Ball als Beutel, nicht ueber den Ball als Quark.
  - Friedberg-Lee-Sirlin 1976: nichttopologische Solitonen. Friedberg/Lee 1977/78: Soliton-Beutelmodell der Hadronen mit
    Dirac-Quarks im Skalar-Soliton. Beides [L?], noch nicht an der Quelle gelesen.
  - Die stillen Atmungsstellen waeren dann nicht abstrahlende Beutelschwingungen [H]. Datennahes Gegenstueck: die
    Roper-Resonanz N(1440) als Atmungsmode des Nukleons (Beutel- und Skyrme-Modelle, [L?]); sie ist breit.
  - Drei Farben [H]: Ein Dreifeld-Ball mit U(3)-Symmetrie und einer Ladungseinheit gibt bei Quantisierung der inneren
    Orientierung ein globales Triplett, keine Eichsymmetrie.
  - Ohne Zusatz nicht moeglich: Spin 1/2 (braucht Dirac), Drittelladung, geeichtes SU(3), Y-Verbindung (Y-1, Y-2
    negativ).
- Neue Karten:
  - **QUARK-1 (Literatur, feldforscher, naechster freier Platz):** Friedberg-Lee-Beutel gegen unseren Q-Ball abgleichen.
    Atmungsmoden in Beutel- und Skyrme-Modellen, ihre Abstrahlung, Roper-Daten (PDG).
  - **QUARK-2 (kleine Rechnung, Leitung, ersetzt SPIN-D):** Dirac-Feld im Profil unseres Balls, gebundene Fermion-Niveaus
    gegen omega. Vorhersage vor dem Lauf in RUNDE-12/quark2/KARTE.md.
  - **QUARK-3 (Schreibtisch):** Multipletts des Dreifeld-Balls bei kleiner Ladung; Aufspaltung durch J_ab.

### PAPER-LESUNG v0.9 (pruefer-opus, 17:12:37 bis 17:27:24; RUNDE-12/paper-lesung/LESUNG-PAPER-V09.md, sha256 a5448ffb...; eingetragen 2026-10-01 17:29:05 CEST)

- **Urteil: "Arbeitsfassung traegt mit Auflagen"**, 13 Befunde, keiner blockierend.
  - Keine Beweisaussage ist falsch; die acht Beweisgrenzen sind in den Beweisabschnitten eingehalten.
  - 20 Beweisaussagen: 14 tragen, 4 mit Wortlaut, 2 zu stark (B3, B7).
  - 62 Zahlen: 55 stimmen; 6 Leiterwerte aus einer Sekundaerquelle weichen bis 8,4e-6 ab.
- Wichtigste Auflage B4: Es fehlen Vorlaeufer, die das Projekt selbst kennt.
  - Malomed u. a. 2005: Haeufung eingebetteter Solitonen, n^(-6/5).
  - Azatov/Ho/Khalil arXiv:2412.13885: dieselben 3D-Radialgleichungen.
  - Evslin arXiv:2604.07713 und Soffer/Weinstein 1999.
  - Der Exponent -1 folgt nur aus dem Modell; freie Fits ergaben -0,76 bis -0,88.
- Weitere Auflagen:
  - B13: PROOF.tex wurde gegen den BEWEIS-2-Vorstand geschrieben.
  - B3: "first radial mode" widerspricht "n nur Etikett".
  - B6: Das Krein-Korollar ist kein Stabilitaetssatz.
  - B1: veralteter Kommentar; die Hypothesenliste fehlt.
  - B5: Das Abstract ist leicht staerker als der Hauptteil.
- Nichtlineares und Anregung sind sauber getrennt.
- An Codex weitergegeben: Peerbus e91312ea (result, Codex-Faden benachrichtigt). Der Entwurf gehoert Codex; die Leitung
  aendert ihn nicht.

### Taegliche Pflichten 01.10. und Zwischenstand (eingetragen 2026-10-01 17:35:56 CEST)

- Werkzeugtore: index-pruefen und karten-pruefen ohne Verstoss. index-sichern 17:13:07 (547 Zeilen, Kettenende 85186e4d...),
  dazu rsync auf die .69 und eine Zeile im Aussenanker KETTENENDE.log (15:13:17 UTC).
- Git-Tagesschnappschuss c90c7de "Snapshot research state of 30 Sep and 1 Oct 2026", gepusht (dcc3a98..c90c7de).
  - gitleaks: 13 Treffer, alle Fehlalarme: Modellnamen im Feld "key", Dezimalzahlen, eine Dateiprueffsumme.
  - Begruendung in GEHEIMNISPRUEFUNG.md, Fingerabdruecke in .gitleaksignore. Kein --no-verify.
- QUARK-2: Beide Laeufe (q2-a, q2-b, ab 17:20:58) liefen in die 10-min-Grenze, rc = 1, ohne Ergebnisdatei.
  - Selbstanzeige: Laufzeit unterschaetzt; Budget nicht vorab gemessen.
  - Ursachen: Der Rechenbereich reichte bis zum Profilabbruch (r ~ 40), weit hinter dem Ball. Zwei Toleranzstufen fuer
    alle omega^2. Ergebnisse wurden erst am Ende gespeichert.
  - Reparatur vor dem naechsten Lauf: siehe RUNDE-12/quark2/KARTE.md, Nachtrag.
- **BS-2000 (Finn: "jo prüf das noch mal in einem subagent: https://arxiv.org/html/hep-th/0003252v1"):** feldforscher
  liest Battye/Sutcliffe 2000 im Volltext gegen Chem 8, Chem 1, LADUNGSTAUSCH-1 und das Leiter-Paper.
  - Abweichung: Damit laufen kurz vier Agenten statt hoechstens drei. Grund ist Finns ausdruecklicher Wunsch.

### AFM-KANAL-1 (Code-Agent, Neustart, bis 17:45; RUNDE-12/afm-kanal1/ERGEBNIS.md; eingetragen 2026-10-01 17:46:14 CEST)

- **Ausgang nach der bindenden Regel: "nicht auswertbar".** K3 ist verfehlt: Das Residuum der Translationsmode liegt bei
  16 von 70 Mitglied-Gitter-Paaren ueber 1e-6 (hoechstens 7,1e-6), alle am innersten Gitterpunkt (r = 0,015 bzw. 0,03).
  - Ab r >= 0,1 liegt das Residuum bei hoechstens 2,5e-7, die Phasenmode unter 5e-11. Der Agent hat das erst nach dem
    Befund untersucht und das Kriterium nicht gelockert.
  - **Entscheidung der Leitung:** Keine nachtraegliche Lockerung von K3. Der Lauf bleibt "nicht auswertbar". Zulaessig
    ist eine Reparatur der Messung (Ursprungsbehandlung, Vermutung des Agenten [H]: Extrapolation von Theta(0)) mit
    demselben Kriterium, als neuer Lauf.
- K0, K1, K2 und K4 bestehen auf beiden Gitterstufen.
  - K2: KG-Wandzustand E = 0,706247 ziffergleich zu R10, eingebettet, F_w = 0,998.
  - K4: NLS-Wandzustand bei E = +0,0213, nicht eingebettet.
  - Die Herleitung stimmt mit MESS-3A Abschnitt K ueberein.
- **Fehler in der Regel der Leitung (Selbstanzeige):** Das Wandfenster |r - R_w| < 2 delta deckt bei dicken Baellen
  (f >= 0,5) den ganzen Ball. Dann hat jeder gebundene Zustand F_w ~ 1, und das Mass trennt Wand- und Volumenzustaende
  nicht.
  - Auch die Kontrollen K2/K4 pruefen nur "eingebettet ja/nein", nicht den Wandanteil.
  - Der vorab gesetzte Zusatz des Agenten, Wandueberhoehung eta > 2, wird nirgends erreicht (hoechstens 1,75): Ein an der
    Wand sitzender eingebetteter Zustand ist auf dem Raster nicht gesehen.
- **Inhaltlicher Befund [H]:** Dicke AFM-Baelle (f = 0,95) haben einen kompakten eingebetteten Zustand des nackten
  geschlossenen Kanals bei rho_c = 1,68 bis 1,74.
  - Bester Kandidat: kappa = -0,20, Omega = 0,995, rho_c = 1,7419.
  - Das entspricht der KG-Positivkontrolle (rho = 1,7335). Auch die erste bewiesene stille Stelle (l = 0, n = 1) sitzt in
    einem dicken Ball.
  - Vorhergesagt (MESS-3A) war am Dickwandende NLS-artiges Verhalten. Das ist nicht eingetreten.
- Regel 8 (nur berichtet) besteht: 25 von 35 Mitgliedern haben den tiefsten Zustand auf beiden Stufen eingebettet.
- Selbstanzeigen des Agenten: ein Versionsabruf per python -c auf der .69 ausserhalb von kleintest.sh; ein Abbruch wegen
  np.trapz in numpy 2.4, behoben per mv ohne Kriterienaenderung.
- **Naechster entscheidender Schritt (vorgemerkt, AFM-KANAL-2):** gekoppelte W-Gitter-Suche wie in R10 fuer dicke AFM-Baelle
  um rho ~ 1,7, mit der KG-Stelle n = 1 als Positivkontrolle.
  - Das Kriterium wird vor dem Lauf gebunden: eine stille Stelle heisst Vorzeichenwechsel bzw. Umlauf +-1 von W in
    (Omega, rho) auf zwei Gittern.
  - Das ersetzt den Ersatztest ueber nackte Zustaende.

### LEITER-2D-PRAEZ (Code-Agent, Neustart, bis 17:47; RUNDE-12/leiter2d-praez/ERGEBNIS.md; eingetragen 2026-10-01 17:48:07 CEST)

- **Ausgang nach der vorab gebundenen Regel: "unentschieden".**
  - s ist bei r_m = 9, 12, 15 gleich (bis ~3e-11 relativ) und ueberall negativ. Das r_m-Kriterium fuer (b) gilt nicht.
  - Die Umlauf-Rechtecke zeigen -1, gelten mit den fest eingebauten 8 Halbierungsrunden aber als nicht aufgeloest.
    Damit gilt auch (a) nicht.
- **Nachtraeglich festgelegte Laeufe** (Plan-Nachtrag mit Vorhersage vor den Laeufen, zweite eingefrorene Kopie;
  Codefassung v2 nur mit der Option fuer mehr Halbierungsrunden):
  - Mit 20 Halbierungsrunden sind beide Rechtecke aufgeloest, Umlauf -1.
  - Mit 4000 statt 400 rho-Punkten wechselt s bei n = 7 und n = 8 das Vorzeichen: omega^2 = 0,529265 und 0,525780.
  - Das sind genau die blinden V1-Werte aus Runde 11 (RUNDE-11/leiter2d/KARTE.md, Vorhersage 30.09. 12:35:57 mtime):
    0,52927 +- 0,0002 und 0,52578 +- 0,0003. Leiterschritt in 1/eps je 4,62.
  - Bei n = 7 zeigen drei Groessen dieselbe Stelle: Nulldurchgang der Abstrahlamplitude (0,5292675), Polbreite aus der
    Flussbilanz und das V der Polbreite.
- **Ursache des Nichtsehens in R11:** weder Rundung noch Kernzuwachs. kurve tastet rho im Abstand 3,6e-3 ab und
  interpoliert linear. Dieser Fehler (~1e-4) ist ab n = 7 groesser als s selbst. Die "1,9e6 Kernzuwachs" aus R11 waren
  das Maximum ueber das ganze rho-Fenster; am Kandidaten sind es nur 2e3 bis 3e4.
- **3D-Schreibtisch:** Die 3D-Stellen n = 11 bis 15 kamen aus der Polsuche (Breitenminima). Der Vorzeichentest versagte
  in 3D schon ab n = 7 ("Zweigmischung", n = 8/9 nicht entscheidbar). Vermutung des Agenten [H]: dieselbe
  Abtast-Ursache.
- Positivkontrolle n = 6: Der Wechsel bleibt bei jedem r_m (0,5338453) und bei feiner Abtastung (0,5338457). r_m = 12
  reproduziert R11 bitgleich.
- **Wertung der Leitung:**
  - Lesart (a), "2D-Leiter bricht nach n = 6 ab", faellt nach den nachtraeglichen Laeufen.
  - Die Stellen n = 7 und 8 sind gesehen. Belegstufe: nachtraeglich festgelegtes feineres Verfahren, Lagen blind aus R11
    vorhergesagt, Umlauf -1 aufgeloest.
  - Die R11-Vorhersage V1 fuer n = 7/8 gilt damit als getroffen, mit diesem Vermerk.
  - Lehre fuer das Paper: Fuer hohe Sprossen muss rho fein abgetastet werden; die lineare Interpolation verdeckt kleine s.
- Selbstanzeigen des Agenten: lokal kein Python (jq und bc); ein Shell-Fehler im ersten Rauchtest; ein wartender Aufruf auf
  der Spur cpu beendet und auf cpu2 neu eingereiht (F7 -> F7b, rc 143).

### QUARK-2 Dirac-Fermionen im Q-Ball (Leitung; RUNDE-12/quark2/KARTE.md; Vorhersage 17:16:10 mtime; zweiter Lauf 17:37:31 bis 17:48:45; eingetragen 2026-10-01 17:49:50 CEST)

- Kontrollen K1, K2 (MIT-Wert 2,0423 gegen 2,043) und K3 bestanden.
- **V1 verfehlt:** E(1s1/2) R_h = 2,39 und 2,81 bei omega^2 = 0,55 und 0,60 statt [1,7; 2,3]. Nach Regel ist die
  Groessenaussage "MIT-Beutel" fuer diese Kopplung falsch.
- **V2 getroffen:** MIT-Reihenfolge und -Verhaeltnisse. Beim groessten Ball 1,564 und 1,863 gegen MIT 1,568 und 1,866.
- **V3 getroffen:** Die Niveauzahl waechst mit dem Ball (51 bis 238).
- [H] nach dem Ergebnis: E R_h faellt mit der Ballgroesse gegen den MIT-Wert, der wirksame Radius ist kleiner als R_h (weiche
  Wand). Pruefbar nur mit einem neuen, vorab festgelegten Radius.
- Bedeutung fuer Finns Frage: Der Ball kann Fermionen wie ein Beutel einschliessen (Struktur MIT-artig). Das ist der
  bekannte Weg Friedberg-Lee; Spin 1/2 kommt dabei vom Dirac-Feld, nicht vom Ball.

### QUARK-1 (feldforscher, 17:29:43 bis 17:49:00; RUNDE-12/quark1/QUARK-1.md, 9 Quellen mit sha256; eingetragen 2026-10-01 17:50:41 CEST)

- **Beste Bruecke [S/ES]:** Unser Ball haelt durch eine eigene erhaltene Ladung zusammen. Naechster Verwandter ist der
  B-Ball (Q-Ball mit Baryonzahl, Kusenko/Shaposhnikov 1998) [S]; der Ball ist weder Quark noch Glueball.
  - Ein Beutel kann er nur ueber seine neutrale Dichte S(r) sein, wie in QUARK-2.
  - Mechanistischer Verwandter der stillen Stellen in der Hadronenphysik: Zwei gekoppelte Kanaele ergeben einen schmalen
    und einen breiten Zustand, z. B. D1(2420) mit 31 MeV gegen D1(2430) mit 314 MeV (Coito/Rupp/van Beveren 2011 [S],
    PDG 2024 [A]).
  - Die Roper-Resonanz ist kein Zahlenverwandter (Guete 1,4 bis 2,3, normal abstrahlend).
- **Berichtigungen der Chat-Antworten der Leitung:**
  - (1) Friedberg/Lee/Sirlin 1976 brauchen zwei Felder (geladen und neutral). Bei Friedberg/Lee 1977 ist der Beutel das
    neutrale "scalar gluon" sigma, kein geladener Q-Ball [S].
  - (2) Ein Beutel-Beleg fuer "Roper = Atmungsmode" fehlt. Im Skyrme-Modell ist die Atmungsmode fast ganz gedaempft
    (Guete ~1,2, Bizon u. a. 2007 [A]).
  - (3) "x 6": Tong 2017 sagt ausdruecklich, dass Z6 experimentell offen ist [A]. Der Spin haengt ueber 3(B - L) mit den
    Ladungen zusammen, also mit Faktor 3. Spin-Z4 gilt nur unter einer Annahme (Garcia-Etxebarria/Montero [A]). Sechs
    Quarks ergeben immer ganzzahligen Spin.
  - (4) "Drittelladungen gibt es nicht" war falsch. Richtig ist "nie frei": gebunden belegt (R = N_c Summe e_q^2, PDG [A]),
    frei nie gefunden (DAMPE 2026 [S]).
  - (5) Ein Glueball hat keine feste Teilezahl. Im Konstituentenmodell sind es 2 Gluonen bei C = + und mindestens 3 bei
    C = - (Mathieu/Kochelev/Vento 2009 [A]). Die Gittermassen stimmen [A]. X(2370) als ueberwiegend Glueball (BESIII
    2026) [S].
  - (6) Das [H] "Q-Ball eher Glueball" traegt nicht: Ein Q-Ball braucht eine erhaltene Ladung, ein Glueball hat keine.
- **Unterscheidungspunkt:** der leere Beutel. Ein Friedberg-Lee-Beutel zerfaellt in Quanten; ein Q-Ball-Beutel bleibt,
  solange seine Ladung erhalten ist. Ist unser Ball der Beutel, dann ist seine Ladung keine hadronische Groesse. Die
  Bruecke fuehrt dann zu dunklen bzw. SUSY-Q-Baellen [ES].
- **U(3) [ES]:** Ein quantisierter U(3)-Ball liegt immer im Multiplett (Q,0), also 3, 6, 10 usw., nie farbneutral; 1 + 8
  entsteht erst mit Ball und Antiball. Farbig geladene Q-Baelle sind Literatur 2025/2026, Loginov 2025 sogar mit
  sextischem Potential wie unserem [S].
- **Gegensweep [A]:** Unsere Leiter laeuft ueber die Ballfrequenz omega*. Sie ist eine Familie von Baellen, kein Spektrum
  eines Objekts. Eine Zuordnung "stille Stelle n = Hadronanregung n" ist von vornherein falsch.
- **Kleinster Test QK-1 "zweiter Kanal":** Ein neutrales Feld chi koppelt mit g chi |phi|^2 an die bewiesene Mode.
  Ueberlappintegral I(k) = int dS(r) j0(kr) r^2 dr im Fenster 0 < k < rho*.
  - Ohne Nullstelle macht jedes leichte neutrale Feld die stille Mode laut, und die Bruecke scheitert.
  - Mit Nullstellen ueberlebt sie nur abgestimmt.

### QK-1 zweiter Kanal (Leitung; RUNDE-12/qk1/KARTE.md; Vorhersage 17:51:30 mtime; Lauf 17:51:44 bis 17:51:50; eingetragen 2026-10-01 17:52:31 CEST)

- I(k) hat fuer l = 0, n = 1/2/3 eine, eine bzw. zwei Nullstellen im Fenster 0 < k < rho*. Abgestimmte chi-Massen:
  0,829 / 1,467 / 1,544 und 1,146. Kontrollen bestanden.
- V1 bis V3 getroffen. Bei V1 war der Grund falsch: n = 1 hat keinen Vorzeichenwechsel in f(a+b).
- Folge nach Regel: Die stille Stelle ueberlebt ein leichtes neutrales Zusatzfeld nur abgestimmt, robust nur bei
  geschlossenem Zusatzkanal. Fuer jede Laborbruecke muessen weitere Anregungszweige bei rho geschlossen sein [H].

### BS-2000 Battye/Sutcliffe im Volltext (feldforscher, bis 17:51; RUNDE-12/battye-sutcliffe/LESUNG-BS2000.md; eingetragen 2026-10-01 17:52:31 CEST)

- **Gleiches Modell:** U_BS = f^2 (1 + (1 - f^2)^2) = 2 (S - S^2 + S^3/2), andere Einheiten (omega = omega_BS/2). Ihre
  Befunde gelten 1:1. Kopfprobe: Q0 = 2,4415 aus Chem 8 = 2 Q_BS.
- Nur Zweierstoesse:
  - in Phase Verschmelzen, gegenphasig Abstossen
  - dazwischen gibt der in der Drehung vorauslaufende Ball Ladung ab, der kleinere Ball laeuft danach schneller
  - ungleiche Baelle in Ruhe tauschen "virtually no charge" (Abb. 11)
  - 2D/3D: Spaltung quer zur Stossachse, Ringe
- Kein Abstandsgesetz; der Ueberlappterm ist "exponentially small" (Gl. 3.3). Ein gestauchter 1D-Ball atmet und klingt
  langsam ab (Abb. 5). Nichts zu Moden oder stillen Stellen.
- Wertung der Leitungs-Entscheidungen durch den Leser:
  - Chem 8: gestuetzt, die Quelle aber zu wenig genutzt. Vorhersage [ES]: Ladung fliesst von A ueber C nach B; der grosse
    Klumpen ist B bei x > 0.
  - Chem 1: Ergebnis gestuetzt, Wortlaut zu stark. Gl. 3.3 erklaert das Trennpunktgesetz als Schwebung der
    Ueberlappladung im Spalt; ein Kern-zu-Kern-Transport ist nicht gezeigt.
  - LADUNGSTAUSCH-1: unberuehrt.
  - BIC-Leiter: keine Folge; im Paper v0.9 fehlt B&S aber als Quelle des Modells.
  - Ausserdem widersprechen B&S Axenides u. a. bei der Deutung des 90-Grad-Auslaufs; die Leitung hatte beide
    gleichgerichtet zitiert.

### Chem 8 Seite (Leitung; RUNDE-12/chem8-seite/KARTE.md; Vorhersage 17:52:52 mtime; Laeufe 17:53:09 bis 17:56:24; eingetragen 2026-10-01 17:57:44 CEST)

- Pruefung der aus BS-2000 uebertragenen Richtungsregel: Ladung fliesst von A ueber C nach B, grosser Klumpen ist B.
- **V1 verfehlt (alle 15 Punkte):**
  - Der grosse Klumpen liegt zwar rechts, bei B (rechts 1,38 bis 2,02 Q0).
  - Links bleiben bei T = 300 aber 0,88 bis 1,24 Q0 statt hoechstens 0,6. A behaelt seine Ladung.
- Nach Regel traegt die Uebertragung "A ueber C nach B" nicht. Gemessen: Die Ladung des ruhenden C geht zur Seite von B
  [H: C -> B].
- V2 (T = 600) nur formal getroffen: Links ist es wenig, weil A den Messbereich verlassen hat. V3 getroffen.

### AFM-KANAL-2 gestartet (eingetragen 2026-10-01 17:58:42 CEST)

- Code-Agent ab 17:58. Karte mit bindender Regel und Vorhersage in RUNDE-12/afm-kanal2/KARTE.md (17:58:00).
- Gekoppelte Suche nach einer echten stillen Stelle (W = 0, Umlauf +-1 auf zwei Gittern) in dicken AFM-Baellen um
  rho ~ 1,7. Positivkontrolle: die bewiesene KG-Stelle n = 1 im selben Codepfad.
- Vorhersage der Leitung: gesehen ~40 %.

### Neue Karten nach Finns "mach weiter" (01.10., eingetragen 2026-10-01 18:09:14 CEST)

- **CEMZ-EBENE** (feldforscher, ab 18:09): Fuenfte-Kraft-Grenzkurve fuer 1 bis 35 km mit Tabellenwerten, Ebene
  (l_eff, |alpha|), Scheiterregel woertlich aus CEMZ-MESS, Bericht Punkt 4. Schwerpunkt: Glieder 7 und 10.
- Codex-Staende seit 15:28 UTC: Die drei Codex-Instanzen (ag-phy-coordination, ag-phy-lat, ag-phy-tus) arbeiten auf
  Finns eigenen Auftraegen (Hypothesen H1/H2, Mehrzweiggrenze, L2-Vorbereitung). Eine Antwort auf die Paper-Hinweise
  der Leitung steht aus.

### QUARK-3 Schreibtisch der Leitung: Farbe im Dreifeld-Ball? (eingetragen 2026-10-01 18:09:44 CEST; nur Schreibtisch, nichts gerechnet)

- Ausgang QUARK-1 [ES]: Ein quantisierter U(3)-Ball liegt im Multiplett (Q,0) (3, 6, 10, ...), nie farbneutral; 1 + 8
  entsteht erst mit Ball und Antiball. Ungeprueft war, ob das Modell ueberhaupt nur U(3) hat.
- **Pruefung von Hand:** Ohne J_ab ist L = Summe |d psi_a|^2 - U(S) mit S = Summe |psi_a|^2. Kinetik und Potential haengen
  nur von den sechs reellen Komponenten ueber Quadratsummen ab. Die Symmetrie ist also O(6), groesser als U(3).
- Folge [H]: Ein Q-Ball ist eine Rotation in einer 2-Ebene des R^6.
  - Seine innere Lage ist die Wahl dieser Ebene (orientierte 2-Ebenen in R^6, Dimension 8), nicht nur ein Punkt in CP^2.
  - Quantisiert ergaeben sich SO(6)-Multipletts. Das SU(3)-Muster (Q,0) entsteht erst, wenn ein Term die komplexe
    Struktur auszeichnet und O(6) auf U(3) bricht.
  - Im relativistischen Modell tun das weder die Kinetik zweiter Ordnung noch U(S). Eine Dynamik erster Ordnung
    (NLS-artig, i psi^dagger d_t psi) oder ein ausdruecklicher U(3)-Term wuerde es tun.
- Der J_ab-Term Re[(psi_a^* psi_b)^2] der Gesamtformel bricht O(6) weiter. Seine Restgruppe ist nicht bestimmt.
- **Einordnung:** Unser Dreifeld-Modell traegt ohne Zusatz keine Farbstruktur im Sinn von SU(3). Mit Zusatz traegt es
  ein globales Triplett, aber nie einen farbneutralen Einzelball. Parken, bis eine Karte die Restsymmetrie mit J_ab
  ausrechnet.

### Codex: Paper v0.10 (Peerbus 16:15 UTC; eingetragen 2026-10-01 18:24:23 CEST)

- Paper v0.10 ist die kanonische Arbeitsfassung (model-lab/papers/qball-bic-ladder-20260930/, PDF sha256
  8cea069502180da6..., 20 Seiten). Keine externe Weitergabe.
- Eingearbeitet:
  - die 13 Befunde der v0.9-Lesung (FINAL-TEXT-REVIEW, METHOD-STAGE-REVIEW)
  - Battye/Sutcliffe, Malomed, Azatov/Ho/Khalil, Evslin, Soffer/Weinstein
  - Tabellen und Abbildung an Primaerdaten abgeglichen
  - die Dipolpuls-Ueberlappung samt endlicher Verstimmung
- Unsere neuen Eingaben, von Codex eng gegengelesen:
  - 2D n = 7 mit aufgeloestem Umlauf; n = 8 nur Vorzeichen- und Breitenbefund. Der urspruengliche unentschiedene Test
    wird nicht umgewertet.
  - QK-1 nur als fuehrender Born-Formfaktor. Codex schreibt: "Geschlossener Zusatzkanal allein sichert keine gekoppelte
    BIC-Robustheit."
  - Ablage resonance-20260930/paper-v10/ (2D-REVIEW.txt, qk1-review/REVIEW.txt).
- Offen bei Codex: L2-Quadrupolzertifikat; farbige 3D-Grafiken fuers Paper (Finn, 16:23 UTC).

### arXiv-Scout (Lauf 20261001T160320Z; eingetragen 2026-10-01 18:25:49 CEST)

- **2609.37653** [S, nur Abstract]: Das X(2370) wird als dynamisch erzeugter phi h1(1380)-Zustand erklaert, mit h1(1380) als
  K*Kbar-Molekuel. Damit waeren auch die unterdrueckten Zerfaelle erklaert, die BESIII als Glueball-Hinweise nennt.
- Folge fuer QUARK-1: Die dortige Angabe "X(2370) ueberwiegend Glueball (BESIII 2026) [S]" ist umstritten. Es gibt eine
  konkurrierende Molekuel-Deutung. Beides ist nur auf Abstract-Ebene gelesen.

### Stand Gesamtformel am 01.10. (Leitung, Schreibtisch; nur Zusammenfassung des Belegten mit Belegstufe)

1. **Ein Feld** (U = S - S^2 + S^3/2, Q-Baelle):
   - Leiter stiller Stellen in 3D (blind bis n = 15, Polsuche) und in 2D (n = 1 bis 8; n = 7, 8 mit nachtraeglichem
     Verfahren).
   - Rechnergestuetzt bewiesen sind l = 0, n = 1 und 2 sowie l = 1, n = 1, je in zwei Haeusern gelesen.
   - Krein-Signatur positiv.
   - Kanaele zweiter Ordnung offen (Codex). Ein Dipolpuls regt die l = 1-Mode nachweisbar an (Codex, streng).
2. **Mehrere Felder (N = 2, 3, J_ab):**
   - Wirbel-Mesonen mit konstanter Spannung und Reissen durch Paarbildung; das ist Literatur (Eto/Nitta).
   - Kein Y-Dreier (Y-1, Y-2): Das Q-Ball-Innere ist zu weich.
   - Z3-Auswahlregel bei Analogkraeften (TET-1).
   - Ohne J_ab gilt O(6)-Symmetrie, nicht nur U(3) (QUARK-3, Schreibtisch).
3. **Spin:**
   - Spin 1/2 folgt aus den Skalaren nicht (SPIN-1).
   - Der Hopf-Weg braucht einen ungeraden Hopfgrad und einen hyperbolisch drehenden Traeger; einen solchen gibt es radial
     bei Viertelladung (Codex).
   - Mit angekoppeltem Dirac-Feld zeigt der Ball MIT-artige Beutelniveaus (QUARK-2). Spin 1/2 kommt dann vom Dirac-Feld.
5. **Laborbruecke:**
   - Im NLS (fluessiges Licht, Troepfchen) gibt es keine stillen Stellen.
   - Ein Antiferromagnet mit K2 > 0 ist Kandidat; die gekoppelte Suche laeuft (AFM-KANAL-2).
   - Stille Stellen sind empfindlich gegen weitere offene Kanaele (QK-1).
6. **Offen, nach Gewicht:** AFM-KANAL-2; ein zweites unabhaengiges Beweisprogramm; L2-Quadrupolzertifikat (Codex);
   Restsymmetrie mit J_ab; CEMZ in D = 4 (Glieder 7 und 10, CEMZ-EBENE laeuft).


  - Die Ablenkung der Bausteine sei unabhaengig vom Radius und damit von der Masse (m = hbar/(R c)). Zitat: "No
    assumptions about any equivalence are needed."
- **Sein Bild entspricht der Absicht nach Variante C** (Text [A], Zuordnung [H]): Die Brechung wirkt bei ihm auch auf das
  Bindungsfeld (Anhang C), auf den Massstab (Teilchen schrumpfen, B.6) und auf die innere Uhr (B.9).
  c^2 = 1 + 4 Phi), sondern in der Uhrkopplung. In A laeuft die innere Uhr des Balls nicht mit.
    nicht.
  Energie.
  - Die Mondentfernungsmessung begrenzt das Verhaeltnis aktiver zu passiver Masse fuer Al/Fe auf 3,9e-14 (Singh u. a.,
    PRL 131, 021401, 2023; nur Abstract).
  - Gegen die Projektzahl 4,5e-3 sind das etwa elf Groessenordnungen statt neun. Das Projekt rechnet noch mit der
    Schranke von 1986, die rund 100-mal schwaecher ist. **Nachtragen, nachdem Singh u. a. an der Quelle gelesen ist.**
- **Unterscheidungspunkt ohne Stoffabhaengigkeit:** PPN-Parameter gamma (Licht gegen Materie).
  - Faellt Materie nur mit R mal Newton, gilt gamma_eff = 2/R - 1. Mit unseren Q-Ball-R waere das etwa 5 bis 28.
  - Cassini misst gamma - 1 = (2,1 +- 2,3)e-5 (Will 2014 [A]).
  - Das trennt eine reine Optik-Gravitation von der ART auch dann, wenn alle Stoffe dasselbe R haetten.
  astras Suche vom 24.09.; nirgends steht "widerlegt".

### X2370-LESUNG gestartet (Finn: "lies die arbeit komplett"; eingetragen 2026-10-01 18:29:39 CEST)

- feldforscher liest arXiv:2609.37653 (Khemchandani, Martinez Torres, Oset; X(2370) als phi-h1(1380)-Zustand) im Volltext.
- Geprueft wird gegen die BESIII-Arbeiten und die QUARK-1-Aussagen. Dazu die Frage, ob ihr Mechanismus (gekoppelte
  Kanaele nahe Schwellen) mit unseren stillen Stellen verwandt ist.
- Laufende Agenten: AFM-KANAL-2, CEMZ-EBENE, X2370-LESUNG (drei).

### CEMZ-EBENE (feldforscher, bis ~18:31; RUNDE-12/cemz-ebene/CEMZ-EBENE.md; eingetragen 2026-10-01 18:31:25 CEST)

- **Ausgang nach der woertlichen Scheiterregel (aus CEMZ-MESS): besteht.**
  - Fuer l_eff von 1 bis 35 km erlauben die Daten zur Fuenften Kraft nur |alpha| <~ 3e-4 bis 6e-4. Fuer eine anziehende
    Kraft schaetzt der Agent ~1e-3 bis 2e-3.
  - Das liegt ueberall mindestens Faktor 5 unter 1e-2. Bei 35 km schliessen die GW-Daten selbst aus.
- **Belegstufe:** Die Werte sind aus Abbildungen zweier Zusammenstellungen derselben Messungen abgelesen
  (Adelberger/Heckel/Nelson 2003, Abb. 4, 95 %; Fischbach/Talmadge 1996, Fig. 1, 2 sigma). Eine Tabelle wurde nicht
  gefunden; die Karte gilt also nur auf Faktor ~2.
- **Groesste Vorbehalte:**
  - CEMZ binden die Turmmasse nicht scharf an l_eff (S. 48: "we did not find a sharp bound"). Bei l_eff ~ 1 km und
    lambda ~ 100 m laege eine anziehende Kraft bei ~7e-3, also nur knapp unter 1e-2.
  - Die km-Kurve von 1996 ist fuer negatives alpha gezeichnet; fuer anziehendes alpha ist sie etwa 3-mal schwaecher.
  - alpha ~ 1 ist nur "parametrically equal to gravitational" (EGHS), eine Analogie zur Stringtheorie, keine
    Herleitung.
- Unterscheidungspunkt: lambda ~ 2 bis 20 km, dort tragen nur vier Turmversuche von 1988 bis 1994.
- Naechster Schritt: die Originalarbeiten der Turmversuche lesen, Grenzen fuer anziehendes alpha als Tabelle.
  Scheiterregel vorab: Liegt die Grenze irgendwo in 1 bis 35 km bei >= 1e-2, ist der Ausgang "unentschieden".
- Selbstanzeigen: geschaetzte Eintragszeiten, berichtigt; eine Erwartung erst nach dem Abruf geschrieben, markiert.

### Glueball gegen Q-Ball (Finn: "prüfe glueball vs. q-ball"; Schreibtisch der Leitung; eingetragen 2026-10-01 18:31:25 CEST)

- **Grundunterschied** (QUARK-1 [A/S]):
  - Ein Q-Ball ist ein klassisches nichttopologisches Soliton eines komplexen Feldes. Er ist stabil, weil eine Ladung
    (U(1)) erhalten bleibt, und waechst mit Q.
  - Ein Glueball ist ein quantenmechanischer, farbneutraler Gluon-Zustand ohne erhaltene Zusatzladung. Er zerfaellt
    (QCD) oder ist nur als leichtester Zustand der reinen Yang-Mills-Theorie stabil.
  - Ein einzelner Glueball ist also kein Q-Ball.
- **Bruecke 1, Holographie** [S, Abstract]: Hartmann/Riedel, PRD 86, 104008 (2012), arXiv:1204.6239. Q-Baelle und
  Bosonensterne in AdS4 sind die gravitativen Dualen von Bose-Einstein-Kondensaten skalarer Glueballs in der
  Rand-Eichtheorie. Gemeint ist ein Kondensat aus vielen Glueballs als duale Beschreibung, keine Gleichsetzung.
- **Bruecke 2, Oszillonen** [S, Abstract]: Fuer reelle, neutrale Felder ist das Gegenstueck des Q-Balls das Oszillon
  (adiabatisch fast erhaltene Groesse). Farhi/Graham/Khemani/Markov/Rosales, PRD 72, 101701 (2005), hep-th/0505273: ein
  sehr langlebiges Oszillon im SU(2)-Eich-Higgs-Modell, wenn die Higgsmasse genau doppelt so gross ist wie die
  Eichbosonmasse.
  - [H] Ein "Glueball-Klumpen" waere eher ein Oszillon eines wirksamen massiven Glueballfelds als ein Q-Ball. Die klassische
    reine Yang-Mills-Theorie ist skaleninvariant und hat keine statischen Solitonen.
- **Bezug zu unseren stillen Stellen [H]:**
  - Die Leiter braucht zwei Kanaele (Teilchen- und Antiteilchenzweig, omega +- rho). Ein komplexes Feld mit U(1) hat sie.
  - Bei einem reellen Oszillon entstehen stattdessen Floquet-Seitenbaender rho +- n omega, also mehrere Kanaele.
  - Ob Oszillonen eigene stille Stellen haben, ist nicht untersucht (ungeprueft); das geht als Frage an X-BAELLE.
- Agenten: X-BAELLE (Finn: "alternative x-ball formen und theorien") laeuft seit ~18:32.
  - Abweichung: kurz vier Agenten statt hoechstens drei (AFM-KANAL-2, X2370, X-BAELLE, dazu der Rest von CEMZ-EBENE),
    auf Finns ausdruecklichen Wunsch.

### AFM-KANAL-2 (Code-Agent, 17:58 bis 18:37; RUNDE-12/afm-kanal2/ERGEBNIS.md; eingetragen 2026-10-01 18:40:00 CEST)

- **Ausgang nach der bindenden Regel: unentschieden.**
  - Grund ist allein ein nicht aufgeloester Streifen bei kappa = -0,10, Omega^2 0,9875 bis 0,995, auf beiden Stufen:
    Phasensprung 0,755 rad, Grenze 0,4. Der Umlauf dort ist 0.
  - Positivkontrolle bestanden: Derselbe Codepfad findet die bewiesene KG-Stelle auf beiden Stufen auf 5e-7 genau, mit
    Umlauf -1.
- **Inhaltlich keine stille Stelle.**
  - In allen drei kappa und auf beiden Stufen gibt es keinen Vorzeichenwechsel von s. Die anderen 35 Streifen sind
    aufgeloest, alle mit Umlauf 0.
  - Auf allen 514 Nullstellen gilt sgn s = -Richtung.
- **Folgelauf.** Der Nachtrag wurde um 18:31:22 eingefroren, nach dem Hauptlauf (letzte Ausgabe 18:30:48) und vor den
  Folgeausgaben (18:34). Mit 30 statt 8 Verfeinerungsrunden ist der Streifen auf beiden Stufen aufgeloest (0,399 rad),
  Umlauf 0.
  - Bedingter Ausgang: "auf dem Raster nicht gesehen".
  - Leitungsentscheidung: Ob der Folgelauf gilt, ist eine Entscheidung nach dem Ausgang. Nach unserer Regel bekommt sie
    vor ihrer Wirkung eine Fremdstimme; vorgemerkt. Bis dahin gilt "unentschieden".
- **Befund [H]: Fast-Stille statt Stille.**
  - Jedes Mitglied hat 3 bis 7 eingebettete Zustaende. Ihre Polbreiten fallen zum dicken Ende hin monoton um 8 bis 9
    Groessenordnungen, ohne inneres Minimum, bis unter ~1e-11.
  - Der Ort aus der Leitungsvorhersage ist die schmalste Resonanz, aber keine Nullstelle von W: rho = 1,742239 bei
    kappa = -0,20 und f = 0,95.
  - Beim KG-Ball sieht es anders aus: dort zeigen die Polbreiten ein V mit Minimum genau an der stillen Stelle (Gamma ~ s^2).
- Vorhersage der Leitung ("gesehen ~40 %"): nicht eingetreten. Mein Grund dagegen (der Topf -2 Omega rho (1 - cos Theta)
  aendert die Kopplung) passt.
- [H] Bedeutung fuer die Laborbruecke:
  - Breiten unter 1e-11 (in Einheiten der Luecke) liegen weit unter jeder realen Daempfung. Praktisch waere so ein
    Zustand still.
  - QK-1 gilt aber auch hier: Weitere Zweige, an die die Dichte koppelt, muessen bei rho geschlossen sein.
  - Offene Frage fuer eine Herleitung: Warum hat s im Sigma-Modell auf allen Aesten festes Vorzeichen?
- Selbstanzeigen des Agenten: ein leerer lokaler python3-Aufruf ohne Rechnung; zwoelf Hilfsdateien kurz im Scratchpad.


- **Quelle [A].** Singh, Mueller, Biskupek, Hackmann, Laemmerzahl, arXiv:2212.09407v1 (Vorabdruck vom 20.12.2022,
  erschienen als PRL 131, 021401 (2023); die PRL-Fassung ist nicht gelesen, sie steht hinter einer Sperrseite).
  - Die arXiv-Nummer kommt aus einer arXiv-API-Abfrage nach dem Titel, nicht geraten.
- **Gemessene Groesse.** Gl. (7): S_A,B = m_aB/m_pB - m_aA/m_pA. Der Mond ist nach Bartlett und Van Buren zweiteilig:
  Kruste aus Al-reichem Anorthosit gegen Mantel aus Fe-reichem Basalt. Massen- und Formmittelpunkt sind um 1,98 +- 0,06 km
  bei 14 Grad versetzt. Die Eigenkraft geht nach Gl. (8) und (9) in die Winkelbeschleunigung ein. Umrechnung: S_Al,Fe =
  S_A,B / 0,08.
- **Zahl.** Tab. 1 gibt S_Al,Fe = 6,9e-16 (Loesung k2d) bzw. 7,7e-15 (Loesung LUNAR). Der schlechtere Wert mal
  Sicherheitsfaktor 5, wie bei Bartlett und Van Buren, ergibt 3,9e-14.
  - Ein Konfidenzniveau ist nicht angegeben. Die Unsicherheit ist die Spannweite von vier Fallrechnungen fuer omega-Punkt.
  - Bartlett und Van Buren 1986, als Zitat bei Singh [A]: 7e-13, mit Faktor ~5 auf 4e-12 verschlechtert.
- **Vorbehalte der Autoren.**
  - 14-Grad-Winkel, Zwiebelschalen-Mond und G-Punkt = 0 sind "critical".
  - Der Mondkern ist nicht beruecksichtigt.
  - Mit dem neueren Versatz von Smith u. a. 2017 kaeme 2,5e-14 heraus.
- **Projektzahl nachgerechnet** (bc, Laptop, Sekunden; Isotopenmassen Al-27 und Fe-56 aus dem Gedaechtnis [L?], das
  Ergebnis braucht nur 10 %):
  - Zaehlung 3A + Z: relativer Unterschied 4,47e-3. Gegen 3,9e-14 sind das 11,06 Zehnerpotenzen, also **elf
    Groessenordnungen** (bisher neun gegen 4e-12).
  - Andere Zaehlungen: A + Z 1,12e-2 (11,5); nur Nukleonen 4,8e-4 (10,1).
- **[ES] Gesteine statt Metalle.**
    0,5, Al bei 0,48, Fe bei 0,46.
  - Ueberschlag mit Lehrbuch-Zusammensetzungen [L?]: Kruste gegen Mantel ~1e-3, gegen die Schranke 0,08 x 3,9e-14 =
    3,1e-15. Das sind ebenfalls ~11 Groessenordnungen.
  elf Groessenordnungen. Nachtrag in WARUM-SPIN-2.md (Glied 3 (f)); die Gegenlesung durch einen frischen Leser steht aus.
- **Neu gesehen bei der arXiv-Abfrage [S], nur Abstracts:**
  - Giulini, Am. J. Phys. 94, 555 (2026), arXiv:2607.02614: Das Lehrbuch-Argument "aktiv = passiv wegen des dritten
    Newtonschen Gesetzes" sei kein zwingender Beweis.
  - Fragkos/Pikovski 2025, arXiv:2503.16198: Labortests der Gleichheit von aktiver und passiver Masse, auch fuer
    quantisierte Energie (polare Molekuele, Kernuhren).
- Selbstanzeige der Leitung: Den Eintrag zu CEMZ-EBENE und Glueball (18:31) habe ich mit ungequotetem Heredoc
  geschrieben (Variable fuer die Zeit). Der Text hatte kein weiteres $ und keine Backticks und ist unveraendert
  angekommen (geprueft). Das bleibt trotzdem ein Verstoss gegen "Heredoc immer quoten".

### X2370-LESUNG (feldforscher, 18:29 bis 18:44; RUNDE-12/x2370/LESUNG-2609.37653.md, Quellen mit sha256; eingetragen 2026-10-01 18:45:58 CEST)

- **Arbeit:** Khemchandani (UNIFESP Sao Paulo), Martinez Torres (USP Sao Paulo), Oset (IFIC Valencia), "A glueball
  puzzle explained in terms of phi h1(1380) dynamics: Aka X(2370)", arXiv:2609.37653. Ganz gelesen, S. 2 bis 4 auch als Bild.
- **Ergebnis:** Die Arbeit zeigt nur qualitativ, dass die drei Glueball-Hinweise von BESIII auch zu einem phi-h1(1380)-Molekuel
  passen: kein K*Kbar, kaum gamma omega und gamma phi. Ein Beleg fuer das Molekuel ist sie nicht.
  - Masse 2316 +- 10 MeV aus der Linienform, ohne Pol. Sie haengt an der K1(1400)-Masse, die "satisfactory" auf 1460 bis
    1480 MeV gelegt wurde (PDG 2026: 1403 +- 7). Das passt nicht zum Anspruch "with no free parameters" (S. 1).
  - Keine einzige Zerfallsbreite ist gerechnet. Die Unterdrueckungen sind nur in Worten begruendet.
  - BESIII 2026 kombiniert: 2359 +13/-14 MeV und 170 +44/-29 MeV. Die Breite passt, die Masse liegt 43 MeV darunter.
- Stichproben der Leitung gegen die abgelegten Quelltexte: alle getroffen.
  - Zitate "with no free parameters" und "satisfactory ... M_K1(1400) ~ 1460 - 1480 MeV"
  - PDG K1(1400) mit 1403 +- 7 MeV
  - BESIII 2359 +13/-14 und 170 +44/-29
  - sha256sum -c der Quellen: OK
- **Bezug zu uns:** keine Feshbach-, BIC- oder Einbettungs-Sprache. Die Unterdrueckung ist kinematisch (off-shell-Schleifen,
  verbotener Vertex), also kein Analogon einer stillen Stelle. Die Dreieckssingularitaet verstaerkt, statt zu unterdruecken.
- **Folgen fuer QUARK-1, als Berichtigung vorzumerken:**
  - Gamma = 188 MeV (2024) ist veraltet, neu sind 170 MeV.
  - "Flavour-Singulett" und "Leere-Beutel-Kandidat" sind zu stark.
  - Bei den Wegen zur Schmalheit fehlt die kanalweise Unterdrueckung durch off-shell-Schleifen.
  - Der U1-Schluss bleibt: keine Erhaltungsladung, also kein Q-Ball-Analogon.
- Unterscheidungspunkt nach dem Leser: In welche Kanaele zerfaellt X(2370) hauptsaechlich, und wer traegt die rund 170 MeV
  Breite? Dazu der a0 pi-Anteil als Funktion von M(K Kbar pi).
- Selbstanzeige des Agenten: Das WebSearch-Kontingent war erschoepft, die Suche ueber 24 Monate lief nur ueber die
  arXiv-API.

### X-BAELLE (feldforscher, 18:32 bis ~19:02; RUNDE-12/x-baelle/X-BAELLE.md, 4 PDFs mit sha256; eingetragen 2026-10-01 19:01:22 CEST)

- Auftrag Finn: "und suche mir alternative x-ball formen und theorien gibts da noch was spannendes?". Rund 15 Familien
  gesichtet: geeicht, drehend, ladungstauschend, B-/L-Ball, Bosonen-/Proca-/Axionstern, Oszillon/I-Ball,
  Fermi-Ball/Quark-Nugget, Soler-Dirac, Troepfchen, Skyrmion/Hopfion.
- **Ergebnis [ES]:** Stille Stellen (eingebettete Innenmoden) sind nur bei Q-Baellen und Soler-Dirac-Solitonen untersucht;
  Soler steht schon in MESS-2.
  - Schluss des Agenten: Moeglich sind sie nur, wo genau ein Kanal offen und ein zweiter knapp geschlossen ist.
  - Neu fuer das Projekt [S]: Boussaid/Comech zeigen, dass jenseits der zweiten Schwelle keine eingebetteten Eigenwerte
    liegen. Im nichtrelativistischen Grenzfall haeufen sie sich nur bei 0 und +-2m, also dort, wo unser Wandzustand bei
    rho ~ 2m sitzt.
- **Zusatzfrage der Leitung, Oszillonen:** BIC einer Oszillon-Innenmode: nichts gefunden (Suchwoerter in der Datei).
  - Bekannt sind drei Wege zur Strahlungsfreiheit: Integrabilitaet (Sine-Gordon), fehlendes Kontinuum (Log-Potential,
    Olle 2021 [A], dort aber instabil) und eine Nullstelle nur des fuehrenden Kanals (Zhang 2020, schon im Projekt).
  - Unmoeglichkeit ist nur fuer kleine phi^4-Breather in 1D belegt (Segur/Kruskal 1987 [S]).
- **Drei Kandidaten mit Testvorschlag** (nur vorgeschlagen):
  - T1 ladungstauschende Q-Baelle: seit 2025 als reelles Oszillon mit Innenmode gedeutet (JHEP 07 (2025) 100 [S]).
    Zuerst die Lebensdauerkarten von Xie/Saffin/Zhou 2021 und Hou/Saffin/Xie 2022 an der Quelle lesen. Eine Spitze heisst
    mindestens das Zehnfache beider Nachbarn.
  - T2 gravitierender Q-Ball: Newton-Potential zu unseren Radialgleichungen, die Stelle n = 1 bei alpha in {0,01; 0,03; 0,1}
    verfolgen. Nullkontrolle alpha = 0.
    - Kleihaus/Kunz/List 2005 nutzen dieselbe Sextik-Familie U = lambda(phi^6 - a phi^4 + b phi^2) [A, von der Leitung
      an der Quelle geprueft: lambda = 1, a = 2, b = 1,1].
    - Unser U = S - S^2 + S^3/2 ist lambda = 1/2, a = 2, b = 2. Die invariante Groesse a^2/b ist 2 gegen 3,64, also
      ein anderer Punkt derselben Familie.
  - T3 B-Ball-Leiter: flaches Potential (U = ln(1 + S), Form vorher an der Quelle pruefen), drei omega, vorhandene
    3D-Maschine. Scheitert, wenn keine Zelle mit Umlauf +-1 auftaucht; dann gilt die Leiter nicht fuer die ganze Klasse.
- Grenzen: Die Websuche war aufgebraucht, gesucht wurde ueber INSPIRE und die arXiv-API. Ein "nichts gefunden" ist
  deshalb schwaecher. Pruefung von sha256sum -c der Quellen: OK.

### arXiv-Woche (Finn: "schau mal die neuesten ergebnisse an von arxiv was gab es da noch was fuer uns interessant ist?")

- Gelesen: die Scout-Warteschlange des Laufs 20261001T160320Z (132 Eintraege, 25.09. bis 30.09.) und eine Titelsuche nach
  Schwerpunktwoertern ueber alle Scout-Laeufe vom 24.09. bis 01.10. Die arXiv-API antwortete mit 429/503, deshalb lokal.
  Abstracts aus den Scout-Daten oder von arxiv.org/abs [S].
- **Neu fuer das Projekt:**
  - 2609.34365, Wu ... Kockum ... Hoi: gemessene BICs in Cavity-Magnonik (Ferrit-Kugel-Ketten als Bragg- und
    Anti-Bragg-Spiegel), mit ortsaufgeloester Sonde. Der Mechanismus ist Spiegel-Interferenz, keine Ball-Innenmode.
    Nutzen: Messtechnik fuer die Magnonen-Bruecke.
  - 2609.10880, Konoplya/Stuchlik/Zhidenko: WKB plus Gamow fuer schwach gedaempfte quasi-gebundene Zustaende.
    - [H] Werkzeug fuer die Frage, warum die AFM-Breiten (AFM-KANAL-2) exponentiell fallen: Tunneln, oder eine glatte
      Ueberlappung, die exponentiell klein wird.
  - 2609.34084, Ferreira: Pseudospektren von Quasinormalmoden (holographische QCD, Tensor-Glueballs). [H] Ein Mass fuer
    die Empfindlichkeit stiller Stellen gegen Stoerungen, also die offene QK-1-Frage.
  - 2407.09682 v3, Lozano-Mayo/Torres-Labansat, JHEP 09 (2026) 218: zusammengesetzte Oszillonen zerfallen
    "staccato-like", mit Strahlungsstoessen bei jedem Kreuzen der Massenschwelle.
  - 2307.05456 (neue Fassung), Sugimoto/Ashida/Ueda: Vielteilchen-BICs in der Bose-Hubbard-Kette mit Stoerstelle.
  - 2609.34734, Zhang/Liu: Abbruch der Radialleiter schwerer Mesonen (D_s, B_s, B_c), pruefbar bei BESIII, Belle II und
    LHCb. Nur eine Analogie zu unserer Leiter [H].
  - Am Rand, ohne Folge: 2609.39193 (dunkle Baryonen, Glueball-Austausch), 2609.38151 (CMB-Schranken fuer Moduli bei
    1 keV bis 100 MeV, nicht der km-Bereich von CEMZ), 2609.39664 (geladene Schalen in unimodularer Gravitation).
- **Schon bekannt:** 2609.32059 Magnetic Q-balls, 2609.19293 Electroweak balls, 2609.30021 Bildung solitonischer
  Bosonensterne, 2609.01134 Phasensteuerung bei Bosonenstern-Stoessen, 2601.21728 Chae (weite Doppelsterne).

## Abschaetzung (Leitung, 2026-10-01 19:02:45 CEST, date)

| Karte | Entscheidung | Grund |
|---|---|---|
| AFM-KANAL-1 | verwerfen (ueberholt) | K3 verfehlt, nicht auswertbar; die Wandregel der Leitung trennte nicht (Selbstanzeige). AFM-KANAL-2 hat die Frage direkt beantwortet |
| AFM-KANAL-2 | parken ("Fast-Stille") | Formal unentschieden (ein Streifen; Fremdstimme zum Folgelauf bei Codex). Keine Nullstelle von W, sgn s fest auf 514 Nullstellen, Polbreiten fallen zum dicken Ende um 8 bis 9 Zehnerpotenzen. Wieder aufnehmen mit einer Erklaerung des festen Vorzeichens oder einer anderen Anisotropie |
| LEITER-2D-PRAEZ | weiter als LEITER-3D-PRAEZ | 2D n = 7 und 8 gesehen (Lagen blind aus R11, Verfahren nachtraeglich festgelegt). Die 3D-Vorzeichenpruefung versagte ab n = 7 vermutlich aus derselben Abtastursache |
| PAPER-LESUNG v0.9 | erledigt | 13 Befunde, keiner blockierend; in v0.10 eingearbeitet (Codex) |
| Bio 45 (Zufallskarte) | parken | Die AFM-Bruecke traegt nur Fast-Stille. Eine Messsignatur mit Breitenminimum an einer Leiterstelle gibt es dort nicht, die Breite faellt monoton |
| SPIN-D | erledigt (ersetzt durch QUARK-2) | - |
| QUARK-1 | erledigt, Berichtigung vorgemerkt | Bruecke ueber den Ball als Beutel und den B-Ball. Nach X2370-LESUNG zu berichtigen: 170 statt 188 MeV, "Flavour-Singulett" und "Leere-Beutel-Kandidat" zu stark |
| QUARK-2 | parken | V1 verfehlt, V2 und V3 getroffen: MIT-artige Niveaustruktur, Groesse nicht. Weiter nur mit einem vorab festgelegten wirksamen Radius |
| QUARK-3 | parken | Ohne J_ab gilt O(6), nicht U(3). Die Restsymmetrie mit J_ab ist offen |
| QK-1 | parken | Leichtes neutrales Zusatzfeld: still nur bei abgestimmter Masse (Born-Formfaktor). Codex: Ein geschlossener Zusatzkanal allein sichert keine gekoppelte Robustheit. Neues Werkzeug dafuer: Pseudospektren (arXiv-Woche) |
| BS-2000 | erledigt | Gleiches Modell (U_BS = 2U), Befunde gelten 1:1; jetzt im Paper |
| Chem 8 Seite | verwerfen (bestaetigt) | Die uebertragene Regel "A ueber C nach B" traegt nicht; A behaelt seine Ladung |
| CEMZ-EBENE | parken (blockiert) | besteht: Regime I mit alpha ~ 1 ist bei 1 bis 35 km ausgeschlossen (Bildablesung, Faktor ~2). Der naechste Schritt, die Turmversuche 1988 bis 1994 im Original, braucht Websuche und Volltexte, beides fehlt gerade |
| X2370-LESUNG | erledigt | Molekuel-Deutung nur qualitativ, Masse nach Auswahl; kein Bezug zu stillen Stellen |
| Glueball gegen Q-Ball | erledigt | Ein einzelner Glueball ist kein Q-Ball; Bruecken Holographie und Oszillon [S] |
| X-BAELLE | weiter mit T2 und T3 | Drei Kandidaten. T2 (Q-Stern, Gesamtformel) und T3 (B-Ball-Leiter, Klassenfrage) werden Rechenkarten, T1 ist eine Lesekarte fuer spaeter |
| arXiv-Woche | weiter (Werkzeuge) | Gamow/WKB als Kandidat fuer die Erklaerung der AFM-Breiten, Pseudospektren fuer die Robustheit; dazu Magnonen-BIC im Experiment (Messtechnik) |

- **Vorab gegen Ausgang, Leitung:**
  - AFM-KANAL-2: "gesehen ~40 %" nicht eingetreten. Der Grund dagegen (Topf und Sigma-Modell aendern die Kopplung)
    passt.
  - QUARK-2: V1 verfehlt, V2 und V3 getroffen.
  - QK-1: V1 bis V3 getroffen, der Grund fuer V1 war aber falsch.
  - Chem 8 Seite: V1 verfehlt.
  - LEITER-2D: die R11-Vorhersage fuer n = 7 und 8 getroffen, mit Vermerk.
- **Lehren der Runde:**
  - Laufzeit auch bei kleinen Laeufen vorher messen (QUARK-2).
  - Kleine s nur mit feiner rho-Abtastung pruefen; lineare Interpolation verdeckt sie (LEITER-2D-PRAEZ).
  - Ein Fenster, das dicke Baelle ganz abdeckt, trennt nicht (AFM-KANAL-1).
  - Folgelaeufe nach einem formalen "unentschieden": Nachtrag vor dem Lauf einfrieren; ob der Folgelauf gilt, entscheidet
    eine Fremdstimme (AFM-KANAL-2).
  - Ein Q-Ball-Analogon braucht eine erhaltene Ladung. Glueball, X(2370) und Oszillon haben keine (QUARK-1, X2370,
    X-BAELLE).
- **Selbstanzeigen:**
  - Leitung: ungequoteter Heredoc (18:31, Text unveraendert, geprueft); QUARK-2-Laufzeit nicht gemessen; AFM-KANAL-1-Regel.
  - Agenten: leerer lokaler python3-Aufruf und Scratchpad-Hilfsdateien (AFM-KANAL-2); python -c auf der .69 (AFM-KANAL-1);
    geschaetzte Zeiten und eine Erwartung nach dem Abruf (CEMZ-EBENE).
- **Unterbrechung:** 30.09. 20:10 bis 01.10. 17:11, API-Wochenlimit, Kontowechsel.
- **Offen bei Codex:**
  - Fremdstimme zum AFM-Folgelauf
  - Gegenlesung des LLR-Nachtrags
  - L2-Quadrupolzertifikat
  - farbige 3D-Grafiken fuers Paper
- **Grenze:** Das WebSearch-Kontingent dieser Sitzung ist aufgebraucht. Recherchen laufen nur noch ueber arXiv-API,
  INSPIRE und direkte Abrufe.

## Einfach gesagt (Rundenende)

In dieser Runde haben wir drei Fragen geklaert. Erstens: Ein drehender Magnetball hat keine exakt stillen Schwingungen,
aber manche strahlen so wenig ab, dass man es nie messen koennte. Zweitens: Unser Q-Ball kann Fermionen wie in einem
Beutel einschliessen, aehnlich wie das MIT-Beutelmodell fuer Quarks. Ein Quark ist er aber nicht (keine Drittelladung,
Schwerkraft erzeugen, jetzt elf Groessenordnungen neben der Mondmessung. Als Naechstes pruefen wir, ob die stillen
Stellen auch in 3D hoeher hinauf, mit Schwerkraft und mit einem Dunkle-Materie-Potential bestehen.

## Rundenabschluss (Leitung, 2026-10-01 19:04:07 CEST)

- Journal: claude-runde-v3-12-20261001, Index nr 548; pruefen ohne Befund, Veroeffentlichung rc = 0.
- Sicherung .69 -> TS440 gestartet 19:04:01 (ohne --delete, nice/ionice). Log auf der .69:
  /home/fmh/sicherung-dot69-ts440-lauf-20261001-r12.log.
- In Runde 13 uebernommen:
  - Codex-Antworten (Fremdstimme zum AFM-Folgelauf, Gegenlesung des LLR-Nachtrags)
  - QUARK-1-Berichtigung
  - die Karten LEITER-3D-PRAEZ, B-BALL-LEITER (T3) und Q-STERN (T2)

## Nachtrag nach Rundenschluss: Codex-Fremdlesungen (Peerbus 16:54 UTC; RUNDE-12/codex-lesung-20261001/LESUNG.md; eingetragen 2026-10-01 19:15:27 CEST)

- **AFM-KANAL-2 (Fremdstimme zur Leitungsentscheidung):** "bedingt ja zum ergaenzten Befund, nein zur Umschreibung".
  - Der Hauptlauf bleibt "unentschieden". Der Folgelauf zaehlt als getrennter, ergaenzter Rasterbefund: "auf dem
    ergaenzten Raster nicht gesehen".
  - **Entscheidung der Leitung:** so uebernommen.
  - Berichtigungen meiner Eintraege oben:
    - Statt "35 von 36 Streifen aufgeloest" heisst es 34 von 36 Streifen-Stufen-Faellen. Ein physischer Streifen war auf
      beiden Stufen offen. Erst mit dem Folgelauf sind 36 von 36 aufgeloest.
    - "Keine Nullstelle von W", "nirgends genau null" und "keine echte/exakte stille Stelle" sind zu stark. Richtig ist:
      "auf dem ergaenzten Raster keine stille Stelle gesehen". Ein Umlauf 0 ist ein Nettoindex und kann Paare
      verbergen. Polbreiten unter der Aufloesung beweisen keine von null verschiedene Breite.
    - Das gilt auch fuer die Abschaetzung (Zeile AFM-KANAL-2), das Einfach gesagt der Runde und meine Chatmeldung an
      Finn ("mathematisch ist es aber nicht null").
- **LLR-Nachtrag (Gegenlesung): "traegt mit Praezisierungen".** Alle Quellenzahlen stimmen. Zu praezisieren:
  - "Mondkern nicht beruecksichtigt" gilt nur fuer den zusaetzlichen Eigenkraftbeitrag bei der Umrechnung (S. 3). In der
    Ephemeride werden Mantel- und Kernorientierung angepasst (S. 2).
  - Die Unsicherheit als Spannweite von vier Fallrechnungen gilt fuer die Loesung LUNAR (+-0,0263 arcsec/century^2), auf
    der 3,9e-14 beruht. Die Loesung k2d hat einen Gauss-Markov-Fit mit +-0,0023.
  - 2,5e-14 mit Smith u. a. 2017 nur als berichtete Empfindlichkeit nennen. Der Satz "factor of 0.3" ist mit
    3,9e-14 -> 2,5e-14 arithmetisch nicht eindeutig vereinbar.
  - Der Vergleich setzt eine Modellabbildung voraus: m_a/m_p proportional zu q/M, mit fester Normierung (Bezug Al) und
    passiver gleich traeger Masse. Codex rechnet D_q = |(q_Fe/M_Fe)/(q_Al/M_Al) - 1| von Hand nach:
    - 3A + Z: 4,48e-3 (11,06 Zehnerpotenzen)
    - A + Z: 1,11e-2
    - A: 4,79e-4
    Die Isotopenmassen sind mit NIST bestaetigt; Fe-56 ist aber nicht die natuerliche Mischung. Unsere 4,47e-3 und
    1,12e-2 tragen als Groessenordnung.
  - **"Gestein statt Metall verschiebt hoechstens eine Groessenordnung" ist nicht belegt.** Der Ueberschlag mit
    Lehrbuch-Zusammensetzungen ist zulaessig, eine obere Schranke ist er nicht. Fuer Kruste gegen Mantel gilt
    S_A,B = 0,08 x S_Al,Fe, also etwa 3,1e-15.
  - Sind aktive und passive Masse beide proportional zur selben Zahl, ist ihr Verhaeltnis konstant, und dieser Test sieht
- Folgen:
  - Praezisierung in WARUM-SPIN-2.md unter dem Nachtrag
  - Berichtigungseintrag im Journal zu nr 548 (AFM-Wortlaut, Gesteinsaussage)
  - kurze Meldung an Finn
