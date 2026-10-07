# Gemeinsames Netz, Fassung 4.3: Was traegt welcher Teil, und was fehlt zur Erklaerung? (Entwurf der Leitung, Runde 48)

- Leitung claude-primary. Fassung 4 geschrieben ab 2026-10-05 09:19:29 CEST (date).
- **Fassung 4.1 ab 2026-10-05 09:43:36 CEST (date):** berichtigt nach dem frischen Leser GEMEINSAMES-NETZ-V4-LESER (RUNDE-37/gemeinsames-netz-v4-leser/GEGENLESEN.md; Urteil: nicht weitergabefaehig vor A1 bis A7).
  - Eingearbeitet: A1 bis A7 inhaltlich, dazu B1 bis B4, B7, B8 und B10 bis B14.
  - Nachgetragen ist der Stand nach 09:19: TAKT-DYNAMIK-1, DANZER-NAEHERUNG-2, ATEM-VOLLZAEHLUNG-L, die neuen Karten und Finns Frage "Was ist mit Gasen?".
  - Die gelesene Fassung liegt als GEMEINSAMES-NETZ-v4.md.wie-gelesen-v4-leser (sha256 87d099c3...).
- **Fassung 4.2 ab 2026-10-05 10:04:13 CEST (date):** berichtigt nach dem zweiten frischen Leser GEMEINSAMES-NETZ-V41-LESER (RUNDE-37/gemeinsames-netz-v41-leser/GEGENLESEN.md; Urteil: weitergabefaehig nach A8 bis A11, ohne neue Rechnungen).
  - Eingearbeitet: A8 bis A11 inhaltlich, dazu B1, B2, B5 bis B9.
  - Die gelesene Fassung 4.1 liegt als GEMEINSAMES-NETZ-v4.md.wie-gelesen-v41-leser (sha256 857a800c...).
  - Die Aenderungen von 4.2 sind kurze Textstellen nach den Sollinhalten des Lesers. Drei Stellen gingen darueber hinaus (Codex C1 und C7, Navier-Stokes); der dritte Leser fand sie quellentreu.
- **Fassung 4.3 ab 2026-10-05 10:21 CEST (date-Klammer 10:20:31 bis 10:22):** berichtigt nach dem dritten Leser GEMEINSAMES-NETZ-V42-LESER (RUNDE-37/gemeinsames-netz-v42-leser/GEGENLESEN.md; weitergabefaehig nach A12 bis A14).
  - Eingearbeitet: A12 bis A14, B10 bis B17.
  - Dazu die v4-Punkte der unabhaengigen Codex-Pruefung CODEX-REVIEW-R48: "erster Klasse" nur linear am flachen Hintergrund; "drei Befunde zeigen auf die Bewegungsenergie" nur fuer die TT-Spanne belegt; L9 mit Parameterbereich und Messabbildung.
  - Die gelesene Fassung 4.2 liegt als GEMEINSAMES-NETZ-v4.md.wie-gelesen-v42-leser (sha256 f5338cf4...).
  - **Die Aenderungen von 4.3 hat kein Leser mehr gesehen.** Sie folgen woertlich bzw. inhaltlich den Sollvorgaben der Leser.
  - **Nicht eingearbeitet (kommt in Fassung 5):** die Ergebnisse nach 10:05, also SKALAR-MISCH-1, REGGE-KINETIK-L und HODGE-MASSE-1.
- **Grundlage:**
  - Fassung 3.1 (RUNDE-44/GEMEINSAMES-NETZ-v3.md; deren Leser-Berichtigungen gelten weiter)
  - Ernten der Runden 45 bis 48
  - Lueckenabgleich 1.1 (RUNDE-46/LUECKEN-ABGLEICH-20261005.md)
  - Frische Leser: GEGENLESEN-R45 (Abschnitt 4), GEGENLESEN-R47, GEMEINSAMES-NETZ-V4-LESER
- **[neu in Fassung 4]** markiert Ergebnisse nach Fassung 3.1. Unveraenderte Teile aus Fassung 3.1 sind gekuerzt; der volle Wortlaut steht dort.
- **Gegenlesestand:**
  - Mit unabhaengigem Leser: IMPULS-NETZ-1, TAKT-UMKLAPP-1, TT-GLAS-2, OKTA-SCHATTEN-1, KAC-DIAMANT-WICK-1; DEFEKT-NETZ-1 und MATERIE-NETZ-1 mit Leser, letzte Textschicht ungesehen.
  - Ohne frischen Leser: SKALAR-SEKTOR-L, TAKT-DYNAMIK-1, DANZER-NAEHERUNG-2, ATEM-VOLLZAEHLUNG-L, WELTKRISTALL-L, BABY-UNIVERSUM-L, TEILE-SCHRANKE-L, DOPPLER-LAUFZEIT-L.
- **Status:** Entwurf, kein Befund. Die Leitidee ist eine Hypothese [H]. Alles sind synthetische Modellrechnungen oder Literatur, keine eigenen Messdaten; Messdaten aus Fachquellen sind [S].
- **Kennzeichen:** [G] im Modell gerechnet, [M] Mathematik, [S] an der Quelle gelesen, [L] Gedaechtnis, [P] Projektdatei, [ES] eigener Schluss, [H] Hypothese.
- **Kleine Legende** (Fassung 3.1, dazu neu):
  - Takt-Operator: Finns Regel, wie die Ecken im Takt aneinander ziehen.
  - Hodge-Laplace: dieselbe Art Regel, gebaut aus den dualen Flaechen.
  - Delaunay: In keiner Umkugel einer Zelle liegt eine fremde Ecke.
  - Glas: Zufallsnetz. Kristall: regelmaessiges Netz.
  - Bewegungsenergie: Wie traege die Zellen sind. J = 1 heisst, jede Zelle gleich traege, egal wie gross.

## 0. Neu seit Fassung 3.1, ganz kurz [neu in Fassung 4]

1. **Finns Takt ist 8-mal der umkreisbasierte Hodge-Laplace des Netzes** [G, vorab ableitbar].
   - Auf V, S und V_D liegt der Rest unter 1e-15 (gewertet auf V und S).
   - Auf Zufalls- und Umklappnetzen liegt er bis 1,9e-10 (je Tetraeder bis 1,5e-7; als Rundung an fast flachen Tetraedern gedeutet [H]).
   - Der Takt ist damit Mathematik und keine freie Setzung.
2. **Umklappen hat einen Mechanismus:** Die Ecken bewegen sich, und Delaunay waehlt die Zelle; dann bleibt der Takt positiv.
   - Nach kleinen Eckverschiebungen waren 26 von 26 Netzen stabil, mit gleich vielen Zufallszuegen 10 von 26 [G].
   - Auch waehrend einer laufenden Welle bleibt das Netz mit Delaunay-Zuegen stabil (22 Laeufe; Zufallszuege in 7 von 7 Faellen instabil) [G].
   - **Die Energie der Welle bleibt dabei aber nicht erhalten:** Ein Zug aendert sie im Mittel um 0,2 bis 0,5 %, hoechstens um 2,2 %. Bei A = 1e-3 verliert die Welle ueber 10 Perioden 2,4 bis 12,7 %, wenn die Raten ueber den Zug stetig gehalten werden, und gewinnt 15 bis 20 %, wenn die Impulse stetig gehalten werden (bei A = 1e-2: 10,5 bis 34,6 % bzw. 32 bis 80 %). Beides sind Festlegungen, keine Physik des Netzes (TAKT-DYNAMIK-1, ohne frischen Leser) [G].
   - Der Sprung sitzt in der Bewegungsenergie mit J = 1; die Regge-Energie bleibt beim 2-3-Zug exakt stetig. HODGE-MASSE-1 prueft eine Abhilfe (laeuft); Codex schlaegt zusaetzlich eine kanonische Zustandsuebertragung beim Zug vor.
3. **Mitfuehrung und Abstrahlung (nur Netz V gerechnet):**
   - Mit Impulskopplung dreht das Netz um eine rotierende Masse wie bei Einstein: Mitfuehrung 1 auf 1,3e-5, aber nur mit abgestimmter Bewegungsenergie (J_iso); mit J = 1 0,975 bis 1,036 [G].
   - Wie Einstein strahlt es nur im reinen TT-Kanal (3e-6, PUMPE-NETZ-1, P1-Gewichte). Mit allen Kanaelen liegt die Abstrahlung der gittergrossen Quelle nicht innerhalb 1e-2 (1,030 / 1,004 / 0,967) [G].
   - Kreisbahnen schwanken je Lage um -0,15 % bis +0,12 %, ohne den Energiekanal V1 gerechnet. Das ist rund 12-mal ueber der Doppelpulsar-Genauigkeit 1,3e-4 [S].
4. **Die skalaren Regeln** sind die Hamilton-Bedingung je Ecke plus maximales Slicing (K = 0) [ES, SKALAR-SEKTOR-L].
   - Im Kontinuum ist das der K = 0-Sonderfall jener Zusatzbedingung, die die einzige datenvertraegliche Horava-Ecke (alpha = beta = 0) erst lebensfaehig macht. Diese Ecke ist mit asymptotisch flachem Rand die ART in maximaler Scheibung [S].
   - **Nicht gezeigt ist, dass das Netz im Kontinuum die ART ist;** das gefuellte Netz ist anisotrop.
   - Ein einziger globaler Takt scheidet nach heutigem Stand aus (Mukohyama u. a. 2026, nur Abstract; eine Rettung ueber die Expansion ist offen).
5. **Glas und Kristall:**
   - Delaunay-Glasnetze sind an den 112 k-Klassen ihres 6^3-Gitters stabil (24 Netze).
   - Jedes einzelne Glasnetz ist anisotrop; die TT-Spanne faellt etwa wie N^(-1/2) (4,66 % bei N = 1024; fuer 1 % braucht es etwa 2e4 Punkte). Dass sich der Rest ueber eine Wellenlaenge herausmittelt, ist [H] und nicht geprueft.
   - Kristallnetze ohne Abstimmung: V 6,34 %, C15 (= Netz S) 2,68 %, A15 0,93 % [G]. GW170817 verlangt ~1e-15 fuer den Tempounterschied zum Licht [S].
6. **Licht mit Takt-Gewichten** [M, G]: Mit den umkreisbasierten Gewichten des Takts ist das langwellige Grundtempo von Skalar- und Maxwell-Wellen auf jedem periodischen Netz exakt isotrop (26 Netze, Spanne <= 5,5e-12). Das folgt fuer den Skalar aus der Identitaet Summe *1 l l^T = Vol I, fuer Maxwell aus Summe L* A n n^T = Vol I, und ist vorab ableitbar (DANZER-NAEHERUNG-2). Beide Identitaeten und die Herleitung von c = 1 sind in der Quelle eigene Mathematik (ungeprueft), numerisch bestaetigt auf 26 Netzen. Kurzwellig bleibt ein vom Netz abhaengiges Muster. Fuer Schwerewellen folgt daraus nichts: Eine Rang-2-Identitaet erzwingt keine Rang-4-Isotropie (Codex, nachgerechnet).

## 1. Leitidee [H]: Das Netz ist der Raum (Finn), jede Groesse sitzt auf einem Teil

| Teil von Finns Netz | traegt | Stand | Herkunft |
|---|---|---|---|
| Knoten (Punkte, 1 PU, atmend) | Takt als Phase; Materiedichte (Q-Ball-Feld); ein Drehfeld (Rahmen) je Knoten | wie Fassung 3.1: Atmen, zwei isotrope Atemformen der 8-Tetraeder-Zelle, Guertel-Trick im SO(3)-Feld. [neu in Fassung 4] Finns Netz ist das Geruest des beta-Cristobalits [P]. Echter Cristobalit waechst am alpha-beta-Uebergang (~533 K) um etwa 5 % [S] und dehnt sich danach zwischen 750 und 2000 K im Mittel nicht aus: \|alpha_V\| <= 1,5e-6/K [E aus S, aus den Volumina berechnet]; das Volumen steigt bis 1300 K und faellt bis 2000 K zurueck (Bourova/Richet 1998). Die Deutung ueber kippende starre Tetraeder ist nur Theorie und Simulation. Die zweite Atemform gehoert vermutlich zur starren P2_12_12_1-Familie von Coh/Vanderbilt 2008 [H, ohne Rechnung; die Zuordnung ist ES]; deren isotroper Ast ist dort nicht beschrieben (ATEM-VOLLZAEHLUNG-L, ohne frischen Leser) | ATEM-NETZ-1, ISO-ATEM-1, GUERTEL-FINN-NETZ-1, EIS-1, ATEM-VOLLZAEHLUNG-L |
| Kanten als Laengen | die Geometrie selbst | wie Fassung 3.1: zwei getrennte Welten ohne Fuellung; eine Welt mit zwei TT-Moden mit Fuellung; Isotropie nur mit abgestimmter Bewegungsenergie (TT-ISO-1: 6,34 % -> 1,1e-5 bzw. 2,2e-7). [neu in Fassung 4] **Glas:** 24 Delaunay-Glasnetze (N = 128 und 256) sind an allen 112 k-Klassen ihres 6^3-Gitters stabil. Jedes Netz ist anisotrop, die Spanne faellt etwa wie N^(-1/2). Die Anisotropie sitzt in der Bewegungsenergie bzw. in der Projektion auf den Eichvertreter, nicht in nichtaffiner Relaxation [G] (TT-GLAS-1, TT-GLAS-2). **Kristalle:** C15 ist Netz S (2,68 %), A15 0,934 %; ikosaedrische Nahordnung sagt die Isotropie nicht voraus [G] (DEFEKT-NETZ-1). **Quasikristall-Naeherungen:** Mit Takt-Gewichten faellt der kubische a2-Rest ohne Abstimmung von Stufe zu Stufe, linear in der Phason-Verzerrung (relativ zu a2 von 3,3 % auf 0,17 % beim Skalar), kein Boden bis 5/3 (nur 2 Saaten) [G] (DANZER-NAEHERUNG-1/-2) | TENSOR-EIS-PYRO-1, EINE-WELT-LOCH-1, TT-ISO-1, TT-GLAS-1/2, DEFEKT-NETZ-1, DANZER-NAEHERUNG-1/2 |
| Kanten als Linkwerte | Licht (U(1)); Kleber (SU(3)) | wie Fassung 3.1: Maxwell langwellig isotrop, kurzwellig kubisches Muster. [neu in Fassung 4] Mit den Takt-Gewichten ist das Grundtempo auf jedem periodischen Netz exakt isotrop (siehe 0.6). Auf den Pyrochlor-Kanten laeuft Licht nur mit den Sechseckflaechen der Loecher: Ohne sie sind alle 8 Baender flach, mit ihnen ist das Licht langwellig isotrop, mit umkreisbasierten Gewichten genau c = 1 [G, vorab ableitbar] (OKTA-SCHATTEN-1). Fuer die volle Lichtablenkung braucht Maxwell Laengen- bzw. Hodge-Gewichte [ES] (MATERIE-NETZ-1) | FLUSS-1, GLUONEN-L, LICHT-FINN-NETZ-1, OKTA-SCHATTEN-1, DANZER-NAEHERUNG-2, MATERIE-NETZ-1 |
| Dreiecke | Umlauf = Feldstaerke | wie Fassung 3.1 | Fassung 1 |
| Tetraeder | Eisregel | wie Fassung 3.1 | FLUSS-1, FARB-EIS-R3-L |
| Schattenformen und duale Zellen [neu in Fassung 4] | Kopplungsgewichte (Hodge-Stern = duales Mass / primales Mass) | Die Rhombendodekaeder der Tetraeder-Oktaeder-Wabe tragen die Takt-Gewichte exakt [G]. Unter den gerechneten Zerlegungen helfen Oktaeder den Schwerewellen nur als starre ganze Zellen (exakt isotrop und stabil, vorab ableitbar); jede gerechnete innere Groesse macht das Netz instabil oder stark anisotrop (95 bis 100 %) [G]. Die Diagonalwahl der Oktaeder kostet im flachen Netz nichts und zeigt sich nur in der Bewegungsenergie [G] (OKTA-SCHATTEN-1). Fuenfeck-Dodekaeder sind die Voronoi-Zellen der Ikosaederplaetze in C15 und A15 (A15 = Weaire-Phelan-Schaum) [L]; auf S^3 bilden sie die 120-Zelle | OKTA-SCHATTEN-1, DEFEKT-NETZ-1, ZELLE600-1 |
| Vierte Richtung (Platte) | eine moegliche Quelle der Haendigkeit | wie Fassung 3.1 | TAKT-RAND-4D-1 |
| Takt (Zeit) | Pachner-Zuege; lokale Zeit-Umbenennung | wie Fassung 3.1: Flip-Flop nur mit mitrueckenden Ecken; die 1/2 als Passbedingung. [neu in Fassung 4] Takt = 8 d0^T *1 d0 mit umkreisbasiertem *1 (siehe 0.1; TAKT-UMKLAPP-1). In 3D ist das nicht der P1-Laplace: Am Ecktetraeder (0, e1, e2, e3) gibt P1 der Kante 0-e1 das Gewicht 1/6, der umkreisbasierte Stern 1/4 [M, zweimal gerechnet]. Ein flacher 2-3-Zug kostet keine Regge-Energie [G, ableitbar] (UMKLAPP-1). Nach zufaelligen Zuegen ist der Takt indefinit; die negativen Richtungen der reduzierten Regge-Matrix kommen ganz aus dem Takt (n_-(B_red) = n_-(P)). Wo die Bewegungsenergie nicht positiv ist, wachsen einige Moden mehr [G]. Die Kette "Delaunay => *1 >= 0 => Takt psd => stabil" (HKV 2013, HT0, HT3) braucht zusaetzlich n_-(B) = V und eine positive Bewegungsenergie [H]. Letztere ist nicht durchweg beobachtet: Im V2-Z-Arm und in UMKLAPP-1 bei f = 0,2 ist sie nicht positiv definit, in TT-GLAS-2 hat sie bei Gamma eine negative Richtung. Waehrend laufender Wellen gilt: stabil, aber nicht energieerhaltend (siehe 0.2) | PACHNER-TAKT-1, TAKT-UMBENENNUNG-L, UMKLAPP-1, HODGE-L, TAKT-UMKLAPP-1, TAKT-DYNAMIK-1 |

**Was Finns Antwort aendert (Fassung 3.1 sinngemaess gekuerzt; voller Wortlaut dort, auch zu weiteren Auswegen und den zu klaerenden Observablen):**
- Fuer Netze mit lokaler Kinematik gilt ein Satz von Marolf (2015): Lineare Schwerewellen bleiben erlaubt, Einstein-Schwerkraft ist ausgeschlossen [S laut Agent].
- Der Satz greift nicht, wenn das Netz selbst die Geometrie ist und Umbauten nur Umbenennungen sind (Eichredundanz, wie bei Regge oder CDT). **Dann ist die Schwerkraft aber eingesetzt, nicht entstanden.**
- "Netz = Geometrie" ist allein weder ein Gegenbeweis noch ein hinreichender Ausweg. Ob Finns Netz diese Eichredundanz traegt, ist offen; Codex' Voraussetzungen des Satzes stehen in Fassung 3.1.
- [neu in Fassung 4] Zum skalaren Teil: siehe 0.4 und L1. Zur ART-Gleichheit der Horava-Ecke gibt es zwei Lager; fuer Doppelsterne sagen beide dasselbe, getrennt sind sie nur kosmologisch [S laut Agent].

## 2. Was fehlt zur Erklaerung (Stand 05.10., 09:43)

In der gelesenen Literatur traegt kein Ansatz zugleich Materie, Licht, Kleber und Schwerkraft (nach Recherchestand nicht belegt, nicht unmoeglich) [S]. Die Luecken folgen dem Lueckenabgleich 1.1 (L1 bis L11 Netz, T1 bis T9 Teilchen).

| Nr | Luecke | Stand | naechster Schritt |
|---|---|---|---|
| L1 | Eine Schrittregel fuer alles, erster Klasse | [neu in Fassung 4] Der Takt ist der Hodge-Laplace (TAKT-UMKLAPP-1) [G]. Die Impulsregel M^H p ist erster Klasse (linear, am flachen Hintergrund), Materie koppelt widerspruchsfrei (IMPULS-NETZ-1) [G, ableitbar]. Die skalare Regel bleibt zweiter Klasse. Erste Klasse mit Finns Takt ist im Prinzip machbar, aber nicht wegen der Takt-Deutung. Entscheidend ist allein eine Passbedingung auf dem Gitter ("A c_v im Bild von M"): Im kovarianten 4D-Regge-Takt ist sie asymptotisch erfuellt (PACHNER-TAKT-1), im gefuellten Hamilton-Netz verletzt (langwellig konstant 0,90) [G, ES] (SKALAR-SEKTOR-L). Khronon- und CMC-Takt waeren offene Wege; der Khronon braucht ein eigenes Feld, CMC liegt naeher, weil K = 0 schon eingebaut ist [S laut Agent]. Ein exakter diskreter Komplex (FEEC/Hodge) ist noch keine erstklassige Zwangsalgebra [Codex] | Gitter-Passbedingung; Bewegungsenergie A (HODGE-MASSE-1) |
| L2 | Ein Tempo fuer alle Felder | wie Fassung 3.1. [neu in Fassung 4] Licht und Skalar haben mit Takt-Gewichten auf jedem periodischen Netz langwellig exakt dasselbe Grundtempo in alle Richtungen [M, G]; kurzwellig bleibt ein netzabhaengiges Muster. GW170817 verlangt fuer Schwerewellen gegen Licht ~1e-15 [S]. Netz V hat ohne Abstimmung 6,34 %, mit J_iso 1,1e-5 [G]; fuer GW170817 waere eine exakte Abstimmung oder ein Grund noetig. Glasnetze werden mit mehr Punkten gleichmaessiger (~N^(-1/2)); jedes einzelne ist anisotrop [G] | SKALAR-MISCH-1, HODGE-MASSE-1, GLAS-STRAHLUNG-1 |
| L3 | Schwerkraft aus demselben Netz | wie Fassung 3.1 (gamma = 2 kappa'/kappa_g; 4D-Regge gamma -> 1). [neu in Fassung 4] **Statik:** Newton-Takt mu = -A/r mit A = 1/(8 Wurzel(2) pi); gamma_S ist eine Identitaet (MATERIE-NETZ-1) [G]. **Abstrahlung (nur Netz V):** Mit Spannungskopplung (P1-Gewichte) wie Einstein im reinen TT-Kanal (3e-6) (PUMPE-NETZ-1). Mit Impulskopplung verschwindet der Laengskanal; G_rad/G_N = 1,030 / 1,004 / 0,967 fuer die gittergrosse Quelle, Kreisbahnen -0,15 % bis +0,12 % je Lage, ohne V1 gerechnet; die frueheren Werte 1,18 / 0,91 / 0,98 hingen an der Eichwahl (IMPULS-NETZ-1) [G]. Ob der Doppelpulsar das Netz ausschliesst, ist offen: Die Lage der Gitterachsen ist unbekannt, die konservativen Bahnparameter fehlen, und vertraeglich ist ein Band (Summe m_i^4 = 0,60 bis 0,67) [G, ES]. **Mitfuehrung:** mit J_iso wie Einstein auf 1,3e-5, mit GP-B und LARES vertraeglich [G, S Abstract]; mit J = 1 0,975 bis 1,036, Vertraeglichkeit nicht gerechnet. Der Rest sitzt vermutlich in einer l = 4-Fehlkopplung ueber die Bewegungsenergie, nicht in einem Zusatzskalar [H] (SKALAR-SEKTOR-L) | SKALAR-MISCH-1, HODGE-MASSE-1, GLAS-STRAHLUNG-1 |
| L4 | Spin 1/2 als Dynamik | wie Fassung 3.1 (Guertel-Trick klassisch; daraus keine fermionische Quantisierung; unveraenderte Formel nur bosonisch) | mit T3 |
| L5 | Masse ohne Verlust | wie Fassung 3.1, praezisiert: Rueckgabequote r = 0,43 bis 0,44 fuer sigma 4 bis 12, feste Takte [G]. [neu in Fassung 4] Die Wick-rotierte Kantenwahl auf Finns Diamantnetz gibt eine Welle mit Nelson-Masse (ohne Ruecksprung m = hbar lambda/c^2), langsam isotrop (aus Symmetrie ableitbar), aber mit tetraedrischem Grenzkegel (c, 0,816 c, c/Wurzel(3)); das i kommt von Hand (KAC-DIAMANT-WICK-1) [G, M] | geparkt |
| L6 | Haendigkeit auf Finns Geometrie | wie Fassung 3.1 | FINN-PLATTE-1 |
| L7 | Kleber-Variablen | wie Fassung 3.1 | geparkt |
| L8 | Verstecktes Ruhesystem | wie Fassung 3.1 (LHAASO-Schranken, bedingt). [neu in Fassung 4] Aus der Mitfuehrung folgt ein wirksames alpha1_eff = 8 (R - 1) ~ 6e-5 bis 1,1e-4. Das gilt nur bei kl = 0,01 (langwellig fallend, ~(kl)^2), mit einer Aufloesung von ~2,4e-5 und unter gamma = 1 und c_Licht = c_TT. Es ist keine Netzeigenschaft "an der Schranke" [H] (SKALAR-SEKTOR-L) | alpha2 nicht untersucht |
| L9 | Eine unterscheidende Vorhersage | offen. Kandidat [H]: das kubische Muster der kurzwelligen Lichtverlangsamung auf regelmaessigen Netzen (Fassung 3.1). Mit Takt-Gewichten ist das Grundtempo zwar exakt isotrop, das kurzwellige Muster bleibt aber netzabhaengig. Eine Vorhersage braucht ausserdem einen festgelegten Parameterbereich und eine Messabbildung, beides vor dem Blick auf Daten (Lueckenabgleich 1.1) | GLAS-STRAHLUNG-1 |
| L10 | Gemeinsame Wirkung bzw. universelle Kopplung [aus Lueckenabgleich 1.1] | [neu in Fassung 4] Erster gemeinsamer Baustein: Spannung und Impuls der Materie koppeln ueber eine Hamilton-Funktion mit einer Regel erster Klasse (linear, am flachen Hintergrund); Kopplung und Rueckwirkung stammen aus demselben Term (Gegenseitigkeit im Vektor-Sektor erfuellt) [G, ES] (IMPULS-NETZ-1). Offen sind der skalare Sektor (Energiekanal V1), die Bindungsenergie (Codex Rang 8) und gleiche Gewichte fuer Takt und Materie (bisher P1 fuer die Materie, umkreisbasiert fuer den Takt; langwellig gleichwertig, gittergrosse Quellen nicht) [G]. Fuer die TT-Anisotropie ist belegt, dass sie in der Bewegungsenergie sitzt (TT-GLAS-2). Die Leckage kann auch an der Quelle haengen, der Energiesprung beim Umklappen auch an der Uebergaberegel [H] | HODGE-MASSE-1, REGGE-KINETIK-L |
| L11 | Grundlagen [aus Lueckenabgleich 1.1] | Energie nach unten beschraenkt, kausales Anfangswertproblem, kontrollierter Kontinuumsbereich, Vertraeglichkeit aller Sektoren [Codex] | vor jedem "vollstaendig" pruefen |

**Teilchen-Luecken (Kurzstand, Lueckenabgleich 1.1 Teil B) [neu in Fassung 4]:**
- **T1 Quantenmechanik:** Unschaerfe aus der Kantenwahl nur als Amplitude; mit Wick-Rotation eine Welle mit Masse, das i von Hand (UNSCHAERFE-KANTE-L, KAC-DIAMANT-WICK-1) [S, M, G].
- **T2 und T6 Q-Baelle:** keine Hadronen, keine Regge-Regel bei festem Q in 2D, 3D und 4D; am Doppelspalt klassisch, ohne Muster [M, G]. Finns rotierendes Paar trifft die Gitter-Tensor-Trajektorie bedingt (am 4++) [G].
- **T7 Licht:**
  - Spaltbar nur in ganze Photonen mit einem Dritten, g2 = 7,5e-5 [S].
  - Unsichtbare Teile tragen beim Nachweis hoechstens ~1e-4 der Energie (Gamma: (-1,4 +- 4,4)e-7) [S].
  - Ein Verlust unterwegs ohne Zeitdehnung ist kosmisch auf ~2 % der Rotverschiebung begrenzt (DES) [S]; ein Verlust mit Zeitdehnung ist ein offenes Fenster.
  - Laborstrecken und die Standardauswertung von Raumsonden sind fuer einen solchen Verlust blind. Ein Test mit Raumsonden-Rohdaten (DRVID) ist ein geparkter Vorschlag; X-Band reicht nach Schreibtischrechnung nur bis etwa zur Hubble-Rate (TEILE-SCHRANKE-L, DOPPLER-LAUFZEIT-L).
  - Paar-Licht nur mit Vorbehalt V-1: Licht aus Paaren zweier Fermionen kann im Breitband hoechstens n = 1/8 je Polarisation tragen (unpolarisiert; 1/4 bei einer Linearpolarisation); gemessene Rayleigh-Jeans-Spektren (n >> 1) passen nicht dazu. Vorbehalt: [M], einmal frisch gegengelesen; gilt fuer den Bau aus zwei Vernichtern mit Verschmierung nach Bisio Gl. (20), auch mit gefuelltem See. Offen sind der Dichtebau c^+ c mit Dirac-See (Jordan, Bosonisierung) und die Verduennung ueber N innere Zustaende (8 n/N). Die Literaturpruefung ist unvollstaendig.
- **T9 Ankopplung an die Schwerkraft:** siehe L3 und L10.

## 3. Dimensionen und 4D-Formen

- wie Fassung 3.1 (Q-Ball D = 1 bis 12, Verschraenkung, Faeden mit Grenze 3, innere Zustaende als Richtung).
- [neu in Fassung 4] **600-Zelle und 120-Zelle** (ZELLE600-1, WELTKRISTALL-L):
  - Die 600-Zelle ist die regulaere Tetraeder-Dichtpackung auf der 3-Sphaere: 12 Nachbarn je Ecke, 5 Tetraeder je Kante; 120 Ecken, 720 Kanten, 1200 Dreiecke, 600 Tetraeder; Fehlwinkel 7,36 Grad.
  - Das Gegenstueck zu Finns Diamant-Netz (4 Nachbarn) ist die 120-Zelle.
  - Beide tragen die Laplace-Pakete 1, 4, 9, 16, 25, 36, wie die Wasserstoff-Schalen n = 1 bis 6. Das ist Symmetrie, keine Vorhersage [G, M].
  - Die Hopf-Faserung der 600-Zelle ist eine diskrete Fock-Kugel, keine Kustaanheimo/Stiefel-Bruecke [M, S].
  - "Flach im Mittel" (q = 5,1043, etwa 10,43 % Sechser-Kanten) ist die Zaehlregel der dynamischen Triangulierung. Eine Zufallsschwankung ~N^(-1/2) als Lambda passt nur in 4D; als 3D-Kruemmung ist sie um rund 32 Groessenordnungen ausgeschlossen [S, M].
- [neu in Fassung 4] **Baby-Universen** (BABY-UNIVERSUM-L):
  - Topologisch abgetrennte Baby-Universen entstehen durch Pachner-Zuege nicht, denn diese aendern die Topologie nie [M].
  - Minimale Haelse koennen 3-2- und 1-4-Zuege erzeugen (Schreibtisch, ungeprueft), und 3D-CDT kennt eine Baby-Universen-Phase [S].
  - Kein anerkannter Beweis fuer oder gegen Baby-Universen; Colemans Lambda -> 0 gilt als gescheitert [S].
  - Fuer Lambda (Glied 10) neu: Bei unimodular freiem Lambda ist der Zustandsraum eines geschlossenen Universums unendlichdimensional (Gielen 2026) [S laut Agent].

## 4. Weichen fuer Finn

1. **R1:** Steckt die Energie einer Masse in der Regel jeder Ecke, und tickt Materie im Takt ihrer Ecke? [neu in Fassung 4] MATERIE-NETZ-1 hat diese Lesart gerechnet (Newton-Takt; gamma_S ist eine Identitaet). Offen bleibt, welches Feld das Licht ist.
2. **Q-Baelle:** [neu in Fassung 4] von Finn beantwortet (05.10.): Q-Baelle nur fuers Teilchenmodell.
3. **Kristall oder Glas:** Finn (05.10.): beide Zweige testen. [neu in Fassung 4] Stand:
   - 24 Delaunay-Glasnetze sind an den gerechneten 112 k-Klassen ihres 6^3-Gitters stabil. Jedes einzelne ist anisotrop; die Reihe wird mit wachsender Punktzahl gleichmaessiger.
   - Kristalle brauchen fuer GW170817 eine exakte Abstimmung oder einen Grund dafuer.
   - Der Quasikristall-Zweig naehert sich mit Takt-Gewichten der Isotropie.
   - Keine Rueckfrage noetig, bis GLAS-STRAHLUNG-1, SKALAR-MISCH-1 und HODGE-MASSE-1 fertig sind.
4. **[neu in Fassung 4] Takt:**
   - Ein einziger globaler Takt scheidet nach heutigem Stand aus; eine Rettung ueber die Expansion ist offen.
   - "Takt je Ort als Maximal-Takt" und "Takt als Eichwahl" sind fuer Doppelsterne nicht unterscheidbar; kosmologisch koennten sie sich trennen.
   - Keine Wahl noetig, solange nur Doppelsterne zaehlen.
5. **[neu in Fassung 4] Photon-Teile:** Ein Verlust unterwegs, der von Dichte, Medium oder Frequenz abhaengt, waere vielleicht mit Raumsonden-Rohdaten pruefbar (geparkter Vorschlag, Empfindlichkeit etwa Hubble-Rate). Frage an Finn, falls gewuenscht: Haengt in deinem Bild das Abgeben von Teilen von der Umgebung ab?
6. **[neu in Fassung 4.1] Gas:** Finn (05.10.): "Was ist mit Gasen?" Lesart der Leitung: der dritte Zustand des Netzes, frei fliegende Punkte mit laufendem Umbau.
   - Ein Gas-Raum klappt staendig um. Mit J = 1 erhaelt das Umklappen die Energie nicht (TAKT-DYNAMIK-1); ein kleiner Verlust oder Gewinn je Zug wuerde Schwerewellen daempfen bzw. verstaerken, wie stark, ist fuer ein Gas nicht gerechnet [ES].
   - Offen ist ausserdem, ob die Rueckstellkraft der Schwerewellen wie Scherung oder wie Kruemmung wirkt; nur im ersten Fall gaelte die Fluessigkeits-Regel "Querwellen erst bei schnellen Schwingungen" [H].
   - RAUM-GAS-L (Literatur, laeuft, mit Zusatz Navier-Stokes) und HODGE-MASSE-1 pruefen das.

## 5. Dimensionsvergleich (AGENTS.md)

- wie Fassung 3.1.
- [neu in Fassung 4]
  - Der Takt als Hodge-Laplace ist dimensionsunabhaengig definiert. Der Faktor 8 und P1 != umkreisbasiert gelten in 3D; in 2D faellt P1 mit dem umkreisbasierten Stern zusammen [L].
  - Die Doppelstern-Gleichheit "Takt je Ort = Eichwahl" gilt fuer 3+1 mit flachem Rand.

## 6. Naechste Karten (Stand 09:43)

- **laufen:**
  - SKALAR-MISCH-1: Gewichte auf V gegen Bahnlagen-Gang und TT-Spanne
  - GLAS-STRAHLUNG-1: Abstrahlung auf Glasnetzen
  - HODGE-MASSE-1: Eich-Reduktion, volumengewichtete Bewegungsenergie, Energie beim Umklappen
  - REGGE-KINETIK-L: Literatur zur Bewegungsenergie im kanonischen Regge-Kalkuel
  - RAUM-GAS-L: Finns Gas-Frage
- **geerntet seit Fassung 4:** TAKT-DYNAMIK-1, DANZER-NAEHERUNG-2, ATEM-VOLLZAEHLUNG-L
- **Warteschlange:**
  - GAS-NETZ-1 (nach HODGE-MASSE-1 und RAUM-GAS-L)
  - Codex-Ideation Rang 7 (lokaler Takt als Phase oder Masse, nach SKALAR-MISCH-1)
  - Codex Rang 4, 5, 6 und 10 erst mit festgelegter Messabbildung bzw. Auswahlregel
  - geparkt: DRVID-KAPPA-1, MINIMALHALS-1, BU-ABSORPTION-1, KAC-DIAMANT-WICK-1
- Alle Karten bekommen vor dem Schreiben eine Ableitbarkeits- und Projektsuche, auch nach Kennzahlen. Bausteine werden verkettet, bevor etwas "nicht ableitbar" heisst.

## 7. Negativliste (darf in dieser Fassung und in Berichten nicht stehen) [neu in Fassung 4, ergaenzt in 4.1 bis 4.3]

- **Aus GEGENLESEN-R45, Abschnitt 4.1, alle A-Befunde (A-1 bis A-9).** Darunter:
  - "Die Bose-Abweichung ist bei Laserdichten unsichtbar (10^90)"
  - "Der 3D-Paarbau ist durch Rayleigh-Jeans widerlegt"
  - "Jordan bzw. Pryce haben gezeigt ..."
- **Aus GEGENLESEN-R47:**
  - "Zufaelliges Umklappen ist die ganze Instabilitaet" bzw. "genau dort wachsen Stoerungen"
  - "Das Glas ist in der ganzen Brillouin-Zone stabil"
  - "Die Kantenwahl ergibt ein Teilchen"
  - "Nur ein positiver Takt ist noetig"
- **Aus GEMEINSAMES-NETZ-V4-LESER:**
  - "Der Rest ist auf allen 78 Netzen <= 1e-15"
  - "Das Netz strahlt wie Einstein" (gilt nur im reinen TT-Kanal)
  - "Das Netz ist im Kontinuum die ART"
  - "Zellen duerfen umklappen" ohne den Energie-Vorbehalt
- **Aus den Runden 44 bis 48:**
  - "Glas ist von selbst isotrop"; "Auf Zufallsnetzen stabil" (nur gerechnete k)
  - "Netz = Geometrie ist ein Ausweg aus Marolf"
  - "Die 600-Zelle ist Finns Netz"
  - "Finns Netz besteht den Doppelpulsar"
  - "Abstrahlung ist richtungsunabhaengig"
  - "Umklappen ist harmlos"
  - "Delaunay ist fuer Stabilitaet noetig"
  - "Der Photoeffekt beweist ganze Photonen"
  - "Das Photon hat gebundene Teile"
  - "Kantenwahl erklaert die Unschaerfe"
  - "Lambda bzw. Flachheit aus der Defektzaehlung ist eine neue Idee"
  - "Die 600-Zelle verbindet Wasserstoff ueber Kustaanheimo/Stiefel"
  - "Die freien Rahmendrehungen sind Versetzungen"
  - "Ikosaedrische Nahordnung macht TT isotroper"
  - "Glasfaser-Uhrenvergleiche begrenzen den Verlust unterwegs"
  - "Muedes Licht ist widerlegt" (nur als alleinige Ursache ausgeschlossen)
  - "Cristobalit schrumpft beim Erwaermen" (richtig: Ueber den alpha-beta-Uebergang waechst er um etwa 5 %; als beta-Cristobalit dehnt er sich zwischen 750 und 2000 K im Mittel nicht aus und schrumpft erst ueber ~1300 K)
  - "Finns Paar beschreibt die Glueballs" ohne den 4++-Vorbehalt
  - "Connor Hill hat eine physikalische Theorie" bzw. "ist am MIT"
- **Ergaenzt in 4.2 (zweiter v4-Leser, B8):**
  - "beta-Cristobalit hat negative Waermeausdehnung"
  - "Die 222-Form ist in der Literatur beschrieben" (ihre Familie vermutlich, die Zuordnung ist ES; der isotrope Ast ist nicht beschrieben)
  - "Echter beta-Cristobalit atmet isotrop wie P2_13"
  - "Der RUM-Anteil der Waermeausdehnung ist gemessen"
  - "widerlegt" fuer Horava, mHG oder das projizierbare Modell
  - "alpha1 des Netzes ist gemessen"
  - "Der Doppelpulsar schliesst das Netz aus"
  - "TES zeigt n h nu"
  - "Pound/Rebka begrenzt den Verlust unterwegs"
  - "Beim Umklappen geht Energie verloren" als Tatsache (richtig: nicht erhalten; Verlust oder Gewinn je nach Festlegung)
  - "Licht laeuft in jedem Netz in alle Richtungen gleich schnell" ohne "langwellig"
  - "Die Licht-Identitaet macht auch die Schwerewellen isotrop"

## Einfach gesagt

Alles hier sind Rechnungen an Modellnetzen und Literatur, keine eigenen Messungen.
- Finns Takt ist eine bekannte Rechenregel der Mathematik. Mit seinen Gewichten laufen lange Lichtwellen in jedem regelmaessig wiederholten Netz in alle Richtungen gleich schnell; bei kurzen Wellen bleibt ein Muster, das vom Netz abhaengt.
- Zellen koennen nach einer einfachen Bauregel umklappen, ohne dass das Netz kippt. Beim Umklappen bleibt die Energie aber noch nicht erhalten: Je nach Rechenvorschrift geht welche verloren oder kommt hinzu. Vermutlich liegt das an der Traegheit der Zellen im Modell oder an der fehlenden Uebergaberegel beim Umklappen.
- Mit abgestimmter Traegheit dreht sich das Netz um eine rotierende Masse wie bei Einstein. Auf dem gerechneten Kristallnetz haengen die Schwerewellen eines Doppelsterns noch ein kleines bisschen von seiner Lage im Netz ab, mehr als die Messgenauigkeit des besten Doppelsterns. Ob das Netz damit ausgeschlossen ist, ist offen: Wie das Netz zum Doppelstern liegt, ist unbekannt, und ein Teil der Rechnung fehlt noch.
- Zufaellig gebaute Netze werden mit mehr Punkten immer gleichmaessiger.
- Offen bleiben vor allem die Quantenmechanik selbst, der halbe Spin und eine Vorhersage, die sich von Einstein unterscheidet.
