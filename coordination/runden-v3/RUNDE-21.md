# Runde 21 (v3, explorativ, Fast Lane)

Leitung: claude-primary. Angelegt: 2026-10-02 17:57:23 CEST (date).
- Fast Lane nach v3 Abschnitt 6: SPROSSEN-VORAB (Runde 20) trug deutlich, also beginnt diese Runde sofort.

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| SPROSSEN-L1L2 | R20 SPROSSEN-VORAB, HUELLEN-DIPOL, HUELLEN-QUADRUPOL | Sagt die Sprossenregel auch l = 1- und l = 2-Stellen vorab voraus? Schlaegt "schrumpfender Abstand" (P2) die lineare Regel (P_lin)? | Code-Agent (cpu bis cpu4, cpu6) |

- Karte RUNDE-21/sprossen-l1l2/KARTE.md, ab 17:56:38, vor jeder Rechnung.
  - Satz A formal: 5 Kurven mit je 2 Sprossen.
  - Satz B nur berichtet: 2 junge Kurven.
  - W0 85 %, W1 50 %, W2 60 %, W3 85 %, W4 75 %.
- Berichtigung vor dem Start: P2 fuer l = 1, k = 1, zweite Sprosse 22,317 -> 22,316 (Rundung).
- **Zufallskarte R21:** Sie wird beim naechsten freien Platz gezogen.

## Zufallskarte R21 gestartet (Leitung, eingetragen 2026-10-02 18:11:02 CEST)

- Gezogen 18:09:55 mit `shuf -n 1` aus den Pool-Eintraegen "parken" ohne KF-5: **Bio 28 "Groessengrenze durch Wachstum"**
  (Runde 5: gefuetterte drehende Baelle verschmolzen und "teilten" sich, Messung unklar).
- Karte RUNDE-21/bio28-weiter/KARTE.md, ab 18:10:39, Vorhersagen Y0 bis Y3 vor jedem Lauf.
  - Gebietszahl zwischen t = 0 und 30 alle 0,5: echte Teilung oder unverschmolzene Nachbarn?
  - Code-Agent auf p4000a/p4000b, Zeitbox 60 min.
- Aktive Agenten (3 von 3): KF-5 weiter (R20), SPROSSEN-L1L2 (R21), Bio 28 weiter (R21).

## KF-EICH gestartet (Leitung, eingetragen 2026-10-02 18:20:59 CEST)

- Karte RUNDE-21/kf-eich/KARTE.md, ab 18:20:33, Vorhersagen E0 bis E3 vor jedem Lauf.
  - Positive Eichprobe des Familien-Klassifikators aus Runde 6: exakte Q-Baelle, ruhend und bewegt, muessen "auf"
    ergeben; angeregte nicht.
  - Herkunft: KF-5 weiter, Parkgrund.
  - Code-Agent auf p4000a/p4000b, Zeitbox 60 min.
- Aktive Agenten (3 von 3): SPROSSEN-L1L2, Bio 28 weiter, KF-EICH.

### Ernte SPROSSEN-L1L2 (Agent fertig ~18:47; RUNDE-21/sprossen-l1l2/ERGEBNIS.md; ausgewertet 2026-10-02 18:29:50 CEST)

Zeitfolge an den Dateizeiten geprueft:

| Zeit | Schritt |
|---|---|
| 17:56:38 | Karte |
| bis 18:14:28 | L4-Laeufe an bekannten Stellen |
| 18:15:49 | Plan eingefroren |
| ab 18:17:18 | erste Testlaeufe |

| Nr | Vorhersage | Ausgang |
|---|---|---|
| W0 | L4 bestanden (85 %) | **eingetroffen**: 14 von 14 im ersten Durchgang (3 nur mit formaler Stetigkeit) |
| W1 | P_lin: alle 5 ersten Sprossen +-0,06 (50 %) | **eingetroffen**: -0,0048 / -0,0193 / -0,0413 (l = 1, k = 0 bis 2); -0,0125 / -0,0276 (l = 2, k = 0, 1) |
| W2 | P_lin: mindestens 4 von 5 zweiten Sprossen +-0,15 (60 %) | **eingetroffen**: 5 von 5: -0,0124 / -0,0526 / -0,1110; -0,0330 / -0,0742 |
| W3 | Umlauf wechselt weiter (85 %) | **eingetroffen**: 10 von 10 Schritten, beide Stufen gleich |
| W4 | P2 genauer als P_lin (75 %) | **eingetroffen**: mittlere Abweichung P2 0,0150 gegen P_lin 0,0389 (2,6-mal genauer). Mit Vorzeichen P2 +0,0147: Der Abstand schrumpft etwas langsamer als mit dem Faktor 0,85 |

- **Bedeutung (vorab festgelegt):**
  - Die Sprossenregel sagt auch l = 1- und l = 2-Stellen vorab voraus [H, im Modell gestuetzt].
  - Der schrumpfende Abstand verbessert die Vorhersage; das stuetzt das Bild Delta R ~ pi/k_innen(R) [H].
- **Satz B (nur berichtet):**
  - l = 1, k = 3: beide Sprossen gefunden, deutlich vor P_lin (-0,113 / -0,293).
  - l = 2, k = 2: erste Sprosse -0,081 (gegen P2 +0,039). Die zweite verwarf das Stetigkeitskriterium (0,138 > 0,1).
    Ein nachtraeglicher Nachtrag ohne Wertung zeigt: Die verworfene Wurzel bei R = 22,29 ist eine echte stille Stelle
    (Umlauf +1 auf beiden Stufen).
- **Lehre:** Die Parabel durch die ersten drei Stellen einer jungen Kurve ist eine schlechte Fortsetzung; eine Gerade
  (0,053) oder die Fortsetzung mit der neuen Sprosse (0,014) haette bestanden. L4 hatte junge Kurven nur formal pruefen
  koennen. Kuenftig fuer Kurven mit weniger als 4 Stellen eine Gerade festlegen.
- Selbstanzeigen des Agenten:
  - vor dem Plan einige Dateien ausserhalb der Freigabe gelesen (sprossen-vorab/hilfs, KARTE-NACHTRAG-1, zwei
    Vorlaeufer-Karten), keine Sperrbereiche
  - ein Aufruf im Nachtrag wegen eigener Eingabedatei wiederholt
  - Rechenzeit 19,6 min auf fuenf Spuren, laengster Lauf 121 s
- Meine Schaetzungen vor dem Start (Schreibtisch, nicht in der Karte, nur zur Einordnung) lagen nahe: z. B. l = 1, k = 0
  erwartet -0,004 / -0,013, gefunden -0,0048 / -0,0124.
- **Abschaetzung:** Im explorativen Sinn erledigt. Die Sprossenregel ist fuer l = 0, 1, 2 je zweimal vorab bestanden
  (R20, R21).
  - Nach v3 Abschnitt 5 sind jetzt die Bedingungen fuer einen formalen Test erfuellt: zwei Runden "weiter" mit L2 und
    L3, und beide Ausgaenge waren moeglich. Es fehlt nur der Zweck, eine Aussage nach aussen.
  - Ob der Huellenstrang ins Leiterpapier soll, entscheidet Finn. Bis dahin parken.

## FLS-STILLE gestartet (Leitung, eingetragen 2026-10-02 18:31:09 CEST)

- Karte RUNDE-21/fls-stille/KARTE.md, ab 18:30:44, Erwartungen F1 bis F4 vor jedem Abruf.
  - Neuheitsfrage: Sind stille Stellen bzw. Leitern in FLS-Q-Baellen und im Friedberg-Lee-Beutel bekannt?
  - Grundlage fuer Finns Entscheidung zum Leiterpapier.
  - feldforscher, Zeitbox 60 min; Abfragen ueber APIs, weil das Websuch-Kontingent erschoepft ist.
- Aktive Agenten (3 von 3): Bio 28 weiter, KF-EICH, FLS-STILLE.

### Ernte Bio 28 weiter, Zufallskarte R21 (Agent fertig ~18:57; RUNDE-21/bio28-weiter/ERGEBNIS.md; ausgewertet 2026-10-02 18:35:11 CEST)

| Nr | Vorhersage | Ausgang |
|---|---|---|
| Y0 | K0 (85 %) | **eingetroffen**: Runde 5 exakt wieder, alle zehn Zeilen grob und fein |
| Y1 | Gebietszahl faellt vor der Teilung auf 1 (60 %) | **eingetroffen**: bei t = 1,5 bis 2 auf 1, 5 bis 11,5 Einheiten lang; Teilung bei t = 7 bis 14 |
| Y2 | Bruchstuecke ueberleben nicht (Endzahl 0) (70 %) | **eingetroffen nach Wortlaut**: Endzahl 0 ueberall |
| Y3 | Windung 0 vor dem Zerfall (55 %) | **nicht eingetroffen**: Der Klumpen behaelt Windung 1 bis zur Teilung, erst die Bruchstuecke haben 0 |

- **Selbstanzeige der Leitung zu Y1:** Y1 liess sich im Wortlaut schon aus Runde 5 ableiten (verschmolzen bei t = 5,
  Teilung bei 10 bzw. 15 im 5er-Raster). Die Vorhersage war damit fast selbsterfuellend; der Agent hat das im Plan
  vermerkt. Fehlerart wie "Vorab ableitbare Kennzahl ist keine Messung".
- **Vorbehalt zu Y1 (Agent):** Das eine Gebiet ist sehr ausgedehnt (mittlerer Radius 8,3 statt etwa 6). Die Gebietsmaske
  kann einen verschmolzenen Ball nicht von verbundenen Lappen unterscheiden.
- **Vorbehalt zu Y2 (Agent, nachtraeglich ausgewertet, ohne Wertung):** Die Endzahl 0 kommt vom absorbierenden Boxrand.
  - Die Bruchstuecke behalten etwa 110 bis 175 Zeiteinheiten fast ihre ganze Ladung und wandern nach aussen.
  - Ladung verlieren sie erst ab einer Koordinate von etwa 27 bis 29; die Randschicht beginnt bei 30,4.
  - Y2 misst hier also den Rand, nicht den Zerfall.
- **Entscheidung der Leitung:**
  - Die vorab festgelegte Bedeutung gilt nach Wortlaut: Y1 und Y2 eingetroffen, also **Bio 28 verworfen**. Ich ersetze
    die Regel nicht nach dem Ausgang.
  - Weil die Verwerfung aber auf einer Messung beruht, die das Gemeinte (Zerfall) nicht prueft, kommt die offene Frage
    als **neuer** Pool-Eintrag "Bio 28b: Ueberleben die Toechter eines verschmolzenen Drehballs ohne Randverlust?"
    (parken).
  - Notiert als Hypothese [H]: Der gemischte Ball (Windung 1 plus nicht drehende Nachbarn) haelt 5 bis 11 Einheiten und
    teilt sich dann in Stuecke ohne Windung, die lange ihre Ladung tragen.
- **Zufallskarte gegen gewaehlte Karten (v3):** R20 KF-5 parken; R21 Bio 28 verworfen.

## LEITERFORMEL gestartet (Leitung, eingetragen 2026-10-02 18:36:34 CEST)

- Karte RUNDE-21/leiterformel/KARTE.md, ab 18:36:07, Vorhersagen LF0 bis LF4 vor jeder Rechnung.
  - Frage: Erklaert die Phasenbedingung Delta(k_innen R) = pi alle Sprossenabstaende fuer l = 0, 1, 2? Das waere ein
    geschlossener Baustein der Gesamtformel [H].
  - Nachtraegliche Erklaerung vorhandener Daten (L4).
  - Code-Agent auf cpu bis cpu4 und cpu6, Zeitbox 75 min.
- Scout-Lauf 18:02 durchgesehen: nichts Neues im Schwerpunkt. Eine Reihe "Temporal Equivalence Principle" (OpenAlex,
  Einzelautor) ist nicht aufgenommen; die Herkunft ist unklar, Begutachtung nicht erkennbar.
- Aktive Agenten (3 von 3): KF-EICH, FLS-STILLE, LEITERFORMEL.

### Ernte KF-EICH (Agent fertig ~19:05; RUNDE-21/kf-eich/ERGEBNIS.md; Plan eingefroren 18:42:39; ausgewertet 2026-10-02 18:53:09 CEST)

| Nr | Vorhersage | Ausgang |
|---|---|---|
| E0 | exakte Baelle ruhend "rund" und "auf" (55 %) | **eingetroffen**: 24 von 24 (omega^2 0,52 / 0,60 / 0,70; T = 0, 50, 100, 200; beide Gitter), Abstand zur Familie <= 0,5 % (Toleranz 10 %), omega auf 3e-5 |
| E1 | bewegt (v = 0,05) ebenfalls "auf" (45 %) | **eingetroffen**: 24 von 24; die Geschwindigkeitskorrektur traegt |
| E2 | angeregt (Amplitude x 1,05) zu T = 0 nicht "auf" (60 %) | **nicht eingetroffen**: omega^2 0,60 und 0,70 heissen "auf". Sie tragen 10 % mehr Ladung, drehen langsamer (0,7703 statt 0,7746; 0,8271 statt 0,8367) und passen zu einem anderen Familienpunkt (2,2 % / 0,3 %). Nur 0,52 ist "unentschieden" |
| E3 | Grund eines Scheiterns von E0 | **offen** (E0 nicht gescheitert) |

- **Bedeutung (vorab festgelegt):** Der Klassifikator kann "auf" sagen. Das "nie auf" der Tropfen in Runde 6 und 20 ist ein
  Befund: Die Tropfen lagen zu diesen Zeiten neben der Familie.
- **Einschraenkungen:**
  - Geeicht ist nur im leeren Raum, nicht im Wellenbad (Hintergrundabzug) und nicht fuer verformte oder verschmelzende
    Klumpen. Gerade daran hingen viele Urteile aus Runde 20.
  - Nach E2 heisst "auf" nur, dass Ladung und Drehfrequenz zusammenpassen, nicht "unangeregt" [H, Agent]. Fuer Stufe 5 ist
    "auf" damit notwendig, aber nicht hinreichend.
- **Gegenpruefungen bestanden:**
  - Schiessverfahren gegen die Familiendatei auf 4e-6
  - grob und fein in 72 von 72 Paaren gleich
  - Rueckrechnung 0 -> -40 -> 0 auf 7e-15
  - Mit Schwelle S0 = 0,1 dieselben Ausgaenge.
- **Nebenbefund:** Die Messscheibe verfaelscht E/Q im leeren Raum nur um <= 0,08 %. Die Vermutung aus Runde 20, ein
  Messfehler von 1 bis 2 % erklaere das "neben", traegt dort also nicht.
- Offen: Die gesetzten Profile erfuellen die Gittergleichung nur bis auf ein Restmass von 2e-4 bis 3e-3, Ursache
  ungeklaert. Die Baelle blieben trotzdem ruhig (Ladungsschwankung <= 7e-5).
- Selbstanzeigen des Agenten:
  - drei eigene, wenige Minuten alte Zwischendateien in hilfs/ mit rm geloescht (rm nicht erlaubt), sonst nichts
    betroffen
  - Profilpruefung im Rauchlauf vor dem Einfrieren gesehen (nur Einrichtung)
- **Abschaetzung: erledigt.** KF-5 bleibt geparkt. Naechster Schritt dort: Tropfen, die laenger getrennt bleiben, und
  eine Eichung im Wellenbad.

### Ernte LEITERFORMEL (Agent fertig 18:57; RUNDE-21/leiterformel/ERGEBNIS.md; Plan eingefroren 18:44:29; ausgewertet 2026-10-02 18:58:05 CEST)

Grundlage: 156 Stellen in 137 Paaren; in jedem Paar wechselt der Umlauf. Rechenzeit 101 s.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| LF0 | K0: Runde-18-Zahlen auf 0,01 (85 %) | **eingetroffen**: 2,3681 / 2,0640 gegen 2,37 / 2,07 |
| LF1 | l = 0, R_n >= 15: Delta Phi/pi = 1 +-3 % bei >= 80 % (50 %) | **eingetroffen, ohne Puffer**: 68 von 85 = 80,0 % (mit R_n >= 14 waeren es 79,1 %) |
| LF2 | l = 1, 2, R_n >= 10: ebenso bei >= 70 % (40 %) | **nicht eingetroffen**: 20 von 32 = 62,5 % (ohne die gekennzeichnete Stelle 22,29: 19 von 31) |
| LF3 | Delta Phi trifft pi besser als pi/k_innen den Abstand (60 %) | **eingetroffen**: mittlere Abweichung 2,7 % gegen 11,5 % |
| LF4 | Rest systematisch, >= 80 % gleiches Vorzeichen (65 %) | **eingetroffen**: alle 137 Reste positiv |

- **Bedeutung (vorab festgelegt):** Keiner der beiden Faelle ist ausgeloest (LF1 ja, LF2 nein). Die Phasenbedingung ist
  nicht als geschlossener Baustein fuer l = 0, 1, 2 bestaetigt.
- **Beschreibung:** Auf eingespielten Leitern gilt die Regel sehr gut.
  - Wandkurven k = 0 (l = 0, 1, 2) und l = 0, k = 0 bis 2: jedes Paar innerhalb 3 %; bei R ~ 40 trifft Delta Phi pi auf
    0,07 bis 0,33 %.
  - Alle 29 Fehlpaare liegen auf inneren Kurven, unter den ersten vier Paaren nach der Kurvengeburt, mit Abweichungen bis
    20 %.
  - Der Rest ist immer positiv und faellt auf jeder Kurve mit R (Wandkurve etwa wie 1/R^2). Er ist groesser auf juengeren
    Kurven und bei hoeherem l.
- **Nachtraeglich, nicht gewertet [H] (Agent):**
  - Auf der Wandkurve ist der Mehrrest von l = 1 und 2 der McMahon-Term der Nullstellen von j_l (Verhaeltnis 0,99 bis
    1,06 ab R ~ 12).
  - Der l = 0-Rest auf reifen Kurven entspricht einem festen Radiusversatz a ~ 2,1 bis 2,5.
  - Beides ist ein Kandidat fuer eine Vorab-Pruefung an neuen Stellen. Das Kugel-Bessel-Bild (Eintraege der Leitung
    17:10 und QUADRUPOL) ist damit auf der Wandkurve quantitativ gestuetzt, nachtraeglich.
- Selbstanzeigen des Agenten:
  - Ein ueberschriebenes Kurvenfeld wurde per Umbenennen behoben; Zahlen bitgleich nachgerechnet.
  - Ausserhalb der Freigabe gelesen: die Karte von Runde 18 und Ordnerlisten; auf der .69 einmal Eintraege gezaehlt (nur
    die Zahl).
- **Abschaetzung: parken mit Folgekarte.** Moegliche Folgekarte: korrigierte Phasenregel (McMahon fuer l >= 1,
  Radiusversatz fuer l = 0) gegen P2, beide vorab, an neuen Stellen. Der Huellenstrang ruht aber bis zu Finns
  Entscheidung ueber das Leiterpapier.

### Ernte FLS-STILLE (Agent fertig ~19:00; RUNDE-21/fls-stille/ERGEBNIS.md; ausgewertet 2026-10-02 18:59:50 CEST)

| Nr | Erwartung | Ausgang |
|---|---|---|
| F1 | Arbeit zu linearen Moden oder Abstrahlung von FLS-Q-Baellen vorhanden (80 %) | **eingetroffen**: Azatov u. a. arXiv:2412.13885, Abschn. 3, nach eigener Aussage die erste Stoerungsanalyse von FLS-Q-Baellen [S] |
| F2 | keine strahlungsfreien oder eingebetteten Moden in FLS berichtet (75 %) | **eingetroffen** (nach Recherchestand) |
| F3 | keine Leiter besonderer Groessen in festem Radiusabstand (85 %) | **eingetroffen nur im Wortlaut**: Halbwellen-Periodizitaet im Radius ist bekannt, aber fuer Streumaxima, nicht fuer Stille (s. u.) |
| F4 | keine strahlungsfreien Beutelschwingungen im Friedberg-Lee-Hadronenbeutel (70 %) | **eingetroffen, duenn belegt** (nur angeregte Zustaende; einige Altarbeiten nur ueber Titel) |

- **Bedeutung (vorab festgelegt):** Die stillen Huellenleitern sind nach Recherchestand in der FLS-Literatur nicht
  beschrieben, also ein Kandidat fuer eine neue Aussage. Ob sie ins Papier soll, entscheidet Finn.
- **Was neu waere:** die exakte, per Windungszahl belegte Stille linearer Normalmoden eines FLS-artigen Beutelballs bei
  l = 0, 1, 2 und ihre Lage auf Leitern.
- **Was nicht neu ist und zitiert werden muss [S]:**
  - (a) das lineare FLS-Problem mit drei gekoppelten Kanaelen: Azatov u. a. 2412.13885
  - (b) die Halbwellen-Periodizitaet im Wandradius, fuer die Streuverstaerkung duennwandiger Einfeld-Q-Baelle unserer
    Sextik-Familie: Zhang/Zhou/Zhu 2510.27064, Gl. 108 bis 118, Abb. 3. Fuer FLS nur numerisch "more peaks", 2503.04657
  - (c) Folgen fast stiller Konfigurationen bei reellen phi^6-Oszillonen ("multiple dips"): 2004.01202, Abschn. 7.5.
    Mechanismus ist eine Nullstelle der Quellen-Fouriertransformierten; nur die fuehrende Harmonische verschwindet.
- **Berichtigungsbedarf im Leiterpapier:**
  - LITERATURE.tex (Z. 24 bis 31) beschreibt Azatov2024 nur als Einfeld-Arbeit, obwohl Abschnitt 3 FLS-Q-Baelle
    behandelt [S, im PDF gelesen].
  - Ausserdem fehlen 2510.27064 und 2004.01202 als Abgrenzung.
  - Das Papier pflegt Codex bzw. die Papierkette; ich aendere es nicht selbst. Notiert fuer Finn und Codex.
- Gegensweep des Agenten:
  - andere Begriffe fuer "still" abgefragt; so kamen die Oszillon-Dips heraus
  - die Schluesselarbeit nur ueber die Zitierliste von FLS 1976 gefunden, nicht per Stichwort
  - 24-Monats-Pflichtsuche ohne Feldtheorie-Treffer
- Grenze: Nicht geprueft ist, ob M2 in genau dieser Form (zusaetzliche psi-Masse, Sextik) in der Literatur vorkommt.
  Das Urteil heisst "nach Recherchestand nicht beschrieben", nicht "neu".
- Selbstanzeige des Agenten: Die Uhrzeiten der ersten acht Abrufbloecke waren geschaetzt; in der Arbeitsdatei
  berichtigt (gemessen 18:32:12 bis 18:42:41).
- **Abschaetzung: erledigt.** Die Entscheidung "ins Papier?" liegt bei Finn; dazu gehoeren die Abgrenzung (a) bis (c) und
  die Berichtigung zu Azatov2024.

## Abschaetzung Runde 21 (Leitung, 2026-10-02 19:00:06 CEST)

| Karte | Ergebnis kurz | Abschaetzung |
|---|---|---|
| SPROSSEN-L1L2 | W0 bis W4 eingetroffen: 10 von 10 neuen l = 1-/l = 2-Sprossen vorab; P2 2,6-mal genauer | erledigt (explorativ); formaler Test moeglich, wenn Finn eine Aussage nach aussen will |
| Bio 28 weiter (Zufall) | Y0, Y1, Y2 (Wortlaut) eingetroffen, Y3 nicht; Y1 war ableitbar; Y2 misst den Randverlust | verworfen nach Kartenregel; Folgefrage Bio 28b im Pool |
| KF-EICH | E0, E1 eingetroffen, E2 nicht: Klassifikator sagt "auf" bei exakten Baellen; "auf" heisst nur Q passt zu omega | erledigt; KF-5 bleibt geparkt |
| LEITERFORMEL | LF0, LF1 (genau 80 %), LF3, LF4 eingetroffen, LF2 nicht; Rest positiv, faellt mit R; McMahon- und Versatzkorrektur [H] | parken mit Folgekarte |
| FLS-STILLE | F1 bis F4 eingetroffen: stille Leitern in FLS nach Recherchestand nicht beschrieben; Abgrenzung zu Azatov 2024, Zhang/Zhou/Zhu 2025, Oszillon-Dips | erledigt; Papierfrage bei Finn |
| M_E-G3 (Codex) | Codex seit 10:03 still | uebernommen |

- **Latten-Bilanz (v3):**
  - L1: alle.
  - L2: SPROSSEN-L1L2 (L4-Vorpruefung), KF-EICH (Gegenpruefungen), Bio 28 (K0).
  - L3: zwei Stufen bzw. Gitter ueberall.
  - L4: LEITERFORMEL und FLS-STILLE (Literatur und Erklaerung).
  - L5: keine.
- **Zufallskarten bisher (v3-Buchfuehrung):** R20 KF-5 parken; R21 Bio 28 verworfen. Die gewaehlten Karten der Runden 20
  und 21: 2 "weiter", 6 "erledigt", 2 "parken".
- **Lehren der Runde:**
  - (1) **Selbstanzeige:** Y1 in Bio 28 liess sich aus den Daten von Runde 5 ableiten. Das ist dieselbe Fehlerart wie
    "Vorab ableitbare Kennzahl ist keine Messung". Vor jeder Vorhersage pruefen, ob die alten Ausgaben sie schon
    entscheiden.
  - (2) Fuer junge Kurven ist eine Gerade die bessere Fortsetzung, keine Parabel.
  - (3) Ein Klassifikator braucht eine positive Eichprobe. Sein "auf" heisst hier nur "Q passt zu omega".
  - (4) Literaturfund ueber Zitierlisten der Gruendungsarbeit, nicht nur per Stichwort (FLS-STILLE).
  - (5) Wenn eine Messung nach dem Wortlaut etwas anderes misst als gemeint (Y2: Randverlust), bleibt die Wertung nach
    Wortlaut. Die offene Frage wird zur neuen Karte, statt die Regel nachtraeglich zu biegen.

## Einfach gesagt (Runde 21)

Die stillen Stellen des Q-Balls mit Huelle liegen beim Atmen, Kippen und Quetschen auf Leitern, und unsere Regel hat
jetzt auch fuer Kippen und Quetschen zehn neue Sprossen richtig vorhergesagt. Eine einfache Wellenregel erklaert die
Sprossen grosser Baelle fast perfekt, bei jungen Leitern aber noch nicht ganz. In der Literatur hat nach unserer Suche
noch niemand solche stillen Leitern fuer Baelle dieser Art beschrieben; aehnliche Wiederholungen im Radius kennt man nur
fuer Streuung. Zwei Zufallsideen brachten Klarheit: Unser Q-Ball-Pruefgeraet funktioniert, und gefuetterte drehende
Baelle zerreissen in Stuecke, deren weiteres Schicksal noch offen ist.

## Rundenabschluss (Leitung, 2026-10-02 19:00:31 CEST)

- Journal claude-runde-v3-21-20261002, Index nr 558; pruefen ohne Befund; Quellen-Hashes in
  RUNDE-21/journal-quellen.txt.
- Sicherung r20 siehe Ausgabe; r21 gestartet (Log ...-r21.log).
- Offen fuer Finn:
  - (1) Soll der Huellenstrang ins Leiterpapier? Dann gibt es einen formalen Test nach v3 Abschnitt 5, eine Abgrenzung
    (a) bis (c) und die Berichtigung zu Azatov2024 in LITERATURE.tex.
  - (2) Dashboard-Kurzfassungen je Runde wieder eintragen?
- Uebernommen:
  - M_E-G3 (Codex)
  - Folgekarten im Pool bzw. geparkt: LEITERFORMEL-2, KF-5, Bio 28b, l = 2-Paarung, EW-Atmung

## Berichtigung (Leitung, 2026-10-02 20:24:26 CEST; Auflage PS-7 aus RUNDE-22/paper-schnitt/BERICHT.md)

- In der Abschaetzung zu SPROSSEN-L1L2 steht: "Die Sprossenregel ist fuer l = 0, 1, 2 je zweimal vorab bestanden (R20,
  R21)." Das ist **falsch**.
- Richtig ist: zwei Tests insgesamt. SPROSSEN-VORAB (R20) fuer l = 0, SPROSSEN-L1L2 (R21) fuer l = 1 und l = 2. Je l also
  **einmal** vorab bestanden, zusammen 22 Sprossen.
- Der Journaleintrag 558 sagt "je vorab bestanden" und bleibt richtig. Die Folgerung zur Formaltest-Reife (v3 Abschnitt 5,
  "zwei Runden weiter") bleibt fuer den Strang als Ganzes richtig, nicht je l.
