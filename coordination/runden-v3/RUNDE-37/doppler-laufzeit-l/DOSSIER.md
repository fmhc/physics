# DOPPLER-LAUFZEIT-L: Dossier. Begrenzen Raumsondendaten einen Frequenzverlust des Lichts unterwegs auf dem Niveau der Hubble-Rate? (Runde 47, Literatur, datennah)

- feldforscher fuer die Leitung claude-primary. Grundlage: KARTE.md (bindend, DL0 bis DL3 und ihre Bedeutung
  unveraendert). Protokoll mit Erwartung vor jedem Abruf, Ausgaengen, Gegensweep und Kalibrierung: ARBEITSFELD.md.
  Abrufliste: ABRUFE.md. Kopien mit Abrufzeit: quellen/.
- Kennzeichen: [S] Fachquelle (an Abstract oder Volltext gelesen, Stelle genannt); [L] Lehrbuch/Gedaechtnis; [M] eigene
  Rechnung von Hand, nicht gegengelesen; [P] Projektbefund; [H] Hypothese; [ES] eigener Schluss. Messdaten aus
  Fachquellen sind [S], keine eigene Messung. **Literatur und Schreibtisch, keine Messdatenbestaetigung.**
- Begriffe: kappa = relativer Frequenzverlust je Meter; H0/c = 7,57e-27 /m bei H0 = 70 km/s/Mpc [M, L].
  y = Delta f/f im Zweiwege-Doppler. DRVID = "Differenced Range Versus Integrated Doppler", also Entfernungsaenderung aus
  der Laufzeit minus Entfernungsaenderung aus dem aufsummierten Doppler.

## 1. Zeiten und Abrufzahl

- Start 2026-10-05 08:44:24 CEST, Dossier ab 09:11:52 CEST (date). Endzeit steht in der letzten Zeile (date).
- **15 von 15 Netzabrufen verbraucht** (letzter um 09:05:24). Davon leer: A13 (arXiv-API, Zeitueberschreitung) und A14
  (atmos.nmsu.edu, Verbindung zurueckgesetzt). Sechs Abrufe waren Websuchen (A1 bis A3, A10 bis A12). Deren Werkzeugtexte
  nutze ich nur als Wegweiser; Zahlen daraus stehen in keiner Tabelle.

## 2. Ergebnis zuerst

1. **Keine veroeffentlichte Schranke gefunden.** Keine Analyse begrenzt mit Sondendaten einen Frequenzverlust je
   Strecke (muedes Licht), auch nicht in den letzten 24 Monaten (A3, A10). **DL2 verfehlt** (nach Recherchestand nicht
   belegt), **DL3 eingetroffen**.
2. **Warum das niemand sieht: Das Standardmodell setzt voraus, was muedes Licht bricht.** DE440 liest Doppler als
   Aenderung der Laufzeit [S]. Die Planetenbahnen stammen aus Laufzeiten: ein Range-Punkt je Pass plus VLBA. Doppler dient nur
   der Sondenbahn relativ zum Planeten (Park u. a. 2021, Abschn. 5) [S]. Die Ephemeride ist fuer einen reinen
   Frequenzverlust deshalb praktisch blind [ES]. Bahnfits schieben unmodellierte Effekte in schwach bestimmte Parameter
   (Thornton/Border 2000, Abschn. 3.6) [S]; fuer muedes Licht ist das meine Uebertragung [ES].
3. **Die Hubble-Signatur im Sonden-Doppler ist ein bekannter Theoriestrang, aber ohne Messschranke.**
   - Allgemeine Relativitaet mit Expansion: Im Zweiwege-Doppler steht ein Term H c beta = H v. Er zeigt nach aussen, also
     Pioneer entgegen, und ist im Sonnensystem vernachlaessigbar (Carrera/Giulini 2006) [S].
   - Das ist genau die Form, die muedes Licht bei Hubble-Rate an einer fliegenden Sonde erzeugt [M].
   - Die einzige "Messung" (A. J. Anderson 2010, H0 = 2,59e-18 /s) ist die Pioneer-Anomalie, geteilt durch c [S, M].
     Sie verwechselt einen Versatz proportional zur Entfernung mit einer Drift proportional zur Zeit, und Pioneer ist
     thermisch erklaert.
4. **Messbar waere es, und die Daten liegen frei.**
   - Bei Hubble-Rate: 3 um/s bei Saturn, 0,34 um/s bei 1 AE. Je 8-h-Pass weicht die Laufzeit-Entfernung um 8,5 cm bzw.
     1 cm vom aufsummierten Doppler ab [M].
   - Die Mars-Odyssey-Rohdaten 2002 bis 2019 im PDS enthalten Range, Doppler-Zaehlphase und sogar ein eigenes DRVID-Feld
     [S, A15].
   - Eine Probe je Pass mit X-Band erreicht grob die Hubble-Rate, nicht weniger [M].
5. **Gegensweep: "unter der Hubble-Rate" ist fuer ein universelles kappa die falsche Latte.**
   - Die DES-Zeitdehnung liegt schon bei ~0,02 H0/c (TEILE-SCHRANKE-L) [P].
   - Ein Sondentest bringt nur dann Neues, wenn der Verlust von Medium, Dichte oder Frequenz abhaengt. Dann ist er um
     Groessenordnungen empfindlicher als DES [M, ES].

## 3. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

| Nr | Erwartet | Gefunden | Fundstelle |
|---|---|---|---|
| V1 | Karte und ich: Die relevante Schwelle fuer einen Sonnensystem-Test ist kappa = H0/c | Fuer einen universellen Verlust ohne Zeitstreckung hat die Vorkarte schon kappa < ~1,5e-28 /m ~ 0,02 H0/c (DES). Ein Sondentest auf Hubble-Niveau aendert daran nichts. Er zaehlt nur fuer ein kappa, das von Medium, Dichte oder Frequenz abhaengt [M, ES]. Gegensweep GS1, nicht durch einen Abruf | TEILE-SCHRANKE-L DOSSIER Abschn. 2 Punkt 3 [P]; ARBEITSFELD Abschn. 3 |
| V2 | A3: zur lokalen Expansion nur Ephemeriden- und LLR-Arbeiten, nichts zur Hubble-Signatur im Sonden-Doppler | Eigener Literaturstrang genau dazu: Carrera/Giulini 2006 (Zweiwege-Doppler in FLRW/McVittie), Kopeikin 2012 (H-Terme in der Lichtlaufzeit fehlen in Navigationsprogrammen), Spengler u. a. 2022 (lokale Beobachter), A. J. Anderson 2010 (behauptete Messung) | A4 Abstracts [S] |
| V3 | A4: A. J. Anderson 2010 behauptet einen Effekt, misst aber nichts | Er gibt eine "Messung" an: H0 = (2,59 +- 0,05)e-18 /s. Das ist a_P = 7,77e-8 cm/s^2 aus Pioneer 10 (laut A. J. Anderson Daten 1987 bis 1999), geteilt durch c [M]. Seine Formel -Delta f/f = t H0 (t = Rundlaufzeit) ist muedes Licht im engen Sinn, R1. Den Schritt zur Pioneer-Drift (R3) behauptet er in einem Gedankenexperiment, gerechnet ist er nicht | arXiv:1011.1944v1, S. 3 (Equ. 2), S. 6 bis 7, S. 8 (Zitat aus Anderson u. a. 2002) [S] |
| V4 | A4: kosmologischer Effekt auf Sonden-Doppler nur in zweiter Ordnung in H | Es gibt einen in H linearen Term H c beta, um den Faktor beta unterdrueckt, also H v. Er zeigt "in outer direction and hence opposite to the Pioneer anomalous acceleration" und ist ~1e-7 der speziell-relativistischen Korrektur | Carrera/Giulini 2006, CQG 23, 7483, Gl. (27) S. 7, S. 8, Gl. (36) S. 9 [S] |
| V5 | DL1: ~1e-14 bei 1000 s, ~3 um/s | Die besten Experimente erreichen ~3e-15 bei 1000 s, "better than 1 micron per second" (Asmar u. a. 2005). Im Zweiwege-Doppler gilt 2 Delta v/c = Delta nu/nu0 (Armstrong 2006). 1e-14 sind also 1,5 um/s, nicht 3 um/s. Bertotti 2003 hat bei OpenAlex kein Abstract und ist nicht gelesen | A7 [S Abstract] |
| V6 | A15: Odyssey-Archiv mit Doppler und Range | Zusaetzlich ein eigenes Feld "Differential Range vs Integrated Doppler (DRVID)" (ATDF, 2002 bis 2003) und die Zweiwege-Zaehlphase (ODF). Die modellfreie Probe ist mit Archivdaten machbar | dataset.cat, Zeilen 128 bis 171 [S] |
| V7 | A10: keine neue Sondenschranke, hoechstens Kosmologie | Eine zweite Randstimme liest Pioneer unter "tiring photon hypothesis" als Hubble-Gesetz im Sonnensystem. Die Quelle ist ungeprueft, weil A13 leer blieb | Werkzeugtext A10, nur Wegweiser |

Bestaetigt mit neuem Detail (keine Verstoesse, eine Zeile je Abruf):
- A2 DRVID existiert seit 1961 als Plasmaverfahren (Werkzeugtext).
- A8 Tab. 3-3: Range-Instrumentbias 2 m, Instrumentstabilitaet ueber 8 h 1e-14, Uhrrate zwischen Stationen 5e-14.
- A9: "only one range point per tracking pass was used"; die Steigung innerhalb des Passes geht nicht in DE440 ein.

## 4. Tabelle: Was misst welche Analyse, und schluckt sie einen konstanten Doppler-Versatz?

Regime [M, ES]:
- **R1** muedes Licht im engen Sinn: Die Traegerfrequenz sinkt, die Laufzeit bleibt.
- **R2** zeitdehnender Verlust: Die ganze Signalform wird gestaucht, die gemessene Laufzeit waechst mit.
- **R3** zeitliche Frequenzdrift (Uhrbeschleunigung, Pioneer).

Signal von R1 im Zweiwege-Doppler: y = 2 kappa D, scheinbare Zusatzgeschwindigkeit v_app = kappa c D. Ich vergleiche nur
Zeilen derselben Groesse.

| Mission bzw. Analyse | Regime, Groesse | Empfindlichkeit | kappa-Grenze (falls ableitbar) | Quelle mit Stelle | schluckt konstanten Doppler-Versatz? |
|---|---|---|---|---|---|
| Pioneer 10/11, Doppler allein (Pioneer 10: 1987 bis 1998) | R3: Frequenzdrift, gelesen als Beschleunigung a_P | a_P = (8,74 +- 1,33)e-10 m/s^2; nach thermischem Modell "no anomalous acceleration remains", ohne Restzahl im Abstract | nur ueber die Drift kappa c v (R1 an fliegender Sonde): kappa < a_lim/(c v) ~ 3e-23 bis 4e-23 /m, also ~4e3 bis 5e3 H0/c [M; a_lim 1e-10 bis 1,33e-10 m/s^2 angenommen, v = 12 km/s] | Anderson u. a. 2002, Abstract; Turyshev u. a. 2012, Abstract [S] | ja: der Versatz kappa c D0 verschwindet in der Anfangsgeschwindigkeit [M]; Pioneer ohne Ranging [L; Sekundaerzitat A5 S. 9] |
| Carrera/Giulini 2006 (Theorie, ART in FLRW und McVittie) | Zweiwege-Doppler-Formel | kosmologischer Term H c beta = H v, nach aussen; ~1e-7 der speziell-relativistischen Korrektur | keine (Theorie). Zeigt: Muedes Licht bei Hubble-Rate und "Expansion im Lichtweg" haben im Doppler dieselbe Drift-Form [ES] | CQG 23, 7483, Gl. (27) S. 7, S. 8, Gl. (36) S. 9 [S] | entfaellt |
| A. J. Anderson 2010 (arXiv, ohne Journal-Angabe) | formuliert R1 (-Delta f/f = t H0), wertet R3 aus (a_P/c) | seine Angabe: H0 = (2,59 +- 0,05)e-18 /s | keine Schranke; ein behaupteter Nachweis, der auf Pioneer beruht | arXiv:1011.1944v1, S. 3, S. 6 bis 7, S. 10 [S] | er selbst: das Bahnprogramm koenne den Effekt ueber Strahlungsdruck u. a. "easily absorb" (S. 3) [S, unbegutachtet] |
| Kopeikin 2012 (Theorie) | R2-artig: H-Terme in der Lichtlaufzeit | keine Zahl im Abstract | keine Messung; schlaegt vor, H lokal zu messen | PRD 86, 064004, Abstract [S] | entfaellt |
| Beste Doppler-Experimente 2005 (Asmar u. a.) | Kurzzeit-Rauschen des Zweiwege-Dopplers | ~3e-15 bei 1000 s, < 1 um/s | keine: Rauschen ist kein Versatz. Zum Massstab: y_R1 bei Hubble-Rate 2e-14 (Saturn), 2,3e-15 (1 AE) [M] | Radio Sci. 40, RS2001, Abstract [S] | entfaellt (keine Bahnanpassung) |
| DSN-Fehlerbudget X-Band 2000 (Thornton/Border) | Stabilitaet und Biases | "Instrument stability @ 8 h" 1e-14; Range-Instrumentbias 2 m; Range-Rauschen 60 cm (60 s); Uhrrate 5e-14 | Nennwert je Pass, kein Ergebnis: kappa ~ 1e-14/(2D) = 3,8e-27 /m (0,5 H0/c) bei Saturn, 3,3e-26 /m (4 H0/c) bei 1 AE [M] | JPL Publ. 00-11, Tab. 3-3 (S. 33 f.); Abschn. 3.6 (S. 35 f.) [S] | Abschn. 3.6: unmodellierte Effekte wandern in schwach bestimmte Parameter (5 m Range -> 1000 km Querlage) [S]; fuer R1 uebertragen [ES] |
| DE440 Saturn (Cassini 2004 bis 2018) | Planetenbahn aus Range (147 Normalpunkte) und VLBA; Doppler nur fuer Sonde gegen Saturn | Range-Reste rms ~3 m | R1: keine, die Ephemeride sieht R1 nicht. R2 bei Hubble-Rate: ~93 m je Jahr, ~1,3 km in 14 Jahren [M]; wie viel davon Bahnelemente schlucken, ist ohne Fit nicht ableitbar | AJ 161, 105, Abschn. 5 (S. 10 f.), Tab. 4 (S. 10), Abb. 11 (S. 13) [S] | Ephemeride: R1 kommt gar nicht hinein (Laufzeit). Sonde-Planet-Fit: offen |
| DE440 Jupiter (Juno 2016 bis 2020) | wie Saturn | 15 Range-Punkte, rms ~13 m | R1 keine; R2 bei Hubble-Rate ~56 m je Jahr [M] | AJ 161, 105, Tab. 4, Abb. 9 (S. 12) [S] | wie Saturn |
| DE440 MESSENGER, Mars-Umlaeufer | wie Saturn | rms ~0,7 m (MESSENGER; MGS, ODY, MRO), MEX ~2 m | R1 keine; R2 bei Hubble-Rate ~10,7 m je Jahr bei 1 AE [M] | AJ 161, 105, Abb. 5 und 7 [S] | wie Saturn |
| DRVID (DSN-Verfahren, Plasmakalibrierung) | R1-Beobachtungsgroesse: Laufzeit minus aufsummierter Doppler, nicht-dispersiver Anteil | Fehler je 8-h-Pass (X-Band) ~1e-5 m/s aus dem Range-Rauschen, Plasma ~5e-6 m/s [M aus Tab. 3-3] | keine veroeffentlicht. Signal bei Hubble-Rate: 8,5 cm (Saturn) bzw. 1 cm (1 AE) je Pass [M] | A2 (Werkzeugtext); MacDoran 1970 (nur Titel, Thornton/Border Lit. [19]); Odyssey-Feld (A15) [S] | nein: modellfrei; echte Bewegung wirkt auf Laufzeit und Doppler gleich und faellt heraus [M] |
| BepiColombo, New Horizons, MESSENGER-Gesamtfit (Genova 2018), INPOP | nicht abgerufen (Budget) | – | – | – | – |
| Zum Vergleich: DES-Zeitdehnung | R1 im intergalaktischen Raum | b = 1,003 +- 0,011 | kappa < ~1,5e-28 /m ~ 0,02 H0/c fuer universelles kappa | TEILE-SCHRANKE-L [P] | entfaellt |

## 5. Urteile DL0 bis DL3 (Kartenwortlaut)

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| DL0 | Kontrolle, vorab ableitbar: v_app ~3 um/s bei Saturn und ~0,3 um/s bei 1 AE fuer kappa = H0/c; Pioneer begrenzt eine andere Groesse | 90 % | **eingetroffen** (Schreibtisch und [S]) | v_app = kappa c D = H0 D: 2,95 um/s bei 1,3e12 m, 0,34 um/s bei 1 AE [M]. Pioneer misst eine Drift (R3), a_P/c = 2,92e-18 /s [M aus S]. Carrera/Giulini 2006: Der H-lineare Term ist um den Faktor beta unterdrueckt, zeigt nach aussen und damit Pioneer entgegen [S]. Zusatz: "andere Groesse" heisst nicht "keine". Ueber die Drift kappa c v begrenzt Pioneer kappa schwach, auf ~4e3 bis 5e3 H0/c [M] |
| DL1 | [L?] Cassinis Zweiwege-Doppler erreicht ~1e-14 relativ (~3 um/s) bei ~1000 s (Bertotti u. a. 2003) | 80 % | **teilweise** | Die Groessenordnung haelt und ist vorsichtig: Die besten Experimente erreichen ~3e-15 bei 1000 s, unter 1 um/s (Asmar u. a. 2005, Abstract) [S]; die X-Band-Stabilitaet ueber 8 h ist 1e-14 (Thornton/Border Tab. 3-3) [S]. **Nicht belegt:** Cassini namentlich und Bertotti 2003 als Quelle (kein Abstract bei OpenAlex, Volltext nicht abgerufen). **Umrechnung falsch:** Im Zweiwege-Doppler entsprechen 1e-14 1,5 um/s, nicht 3 um/s (2 Delta v/c = Delta nu/nu0, Armstrong 2006) [S, M] |
| DL2 | [H] Eine veroeffentlichte Doppler-gegen-Laufzeit- oder Ephemeriden-Analyse begrenzt einen streckenproportionalen Frequenzverlust unter die Hubble-Rate | 35 % | **verfehlt** (nach Recherchestand nicht belegt; Existenz einer nicht gefundenen Arbeit nicht ausgeschlossen) | Sechs Suchen ohne Treffer, darunter zwei im 24-Monats-Fenster (A3, A10). DE440 nutzt Doppler nicht fuer Planetenbahnen [S]. Der Theoriestrang (Carrera/Giulini, Kopeikin, Spengler u. a.) hat keine Messschranke [S]. Die einzige "Messung" ist ein behaupteter Nachweis ueber Pioneer (A. J. Anderson 2010) [S]. Zwei Abrufe blieben leer (A13, A14) |
| DL3 | [H] Keine direkte Schranke; das Fenster "Verlust unterwegs" bleibt im Sonnensystem auf Hubble-Niveau offen | 55 % | **eingetroffen**, mit Einschraenkung | Keine direkte Schranke (Beleg wie DL2). Fuer R1 bleibt das Fenster im Sonnensystem offen: Die Ephemeride sieht R1 nicht (DE440 Abschn. 5) [S], Bahnfits verschieben Unmodelliertes (Thornton/Border 3.6) [S, Uebertragung ES]. **Einschraenkung:** Offen ist es nur, was Sonnensystem-Daten angeht. Ein universelles kappa ohne Zeitstreckung ist kosmologisch schon auf ~0,02 H0/c begrenzt (DES) [P]. Fuer R2 legen die Range-Reste nahe, dass die Hubble-Rate auffiele (Saturn ~1,3 km in 14 Jahren gegen 3 m rms) [ES, ohne Fit keine Zahl] |

**Bedeutung nach Karte:** DL3 ist eingetroffen: "Das Fenster bleibt. Ein gezielter Test mit vorhandenen Daten waere eine
echte Vorhersage fuer Finns Bild [H]; dann folgt ein Kartenvorschlag mit Datensatz." Der Vorschlag steht in Abschnitt 7.
Die Bedeutung "DL2 trifft ein" (Verlust auch im Sonnensystem unter H0/c begrenzt) gilt nicht.

## 6. Bedeutung fuer Finns Bild "Photon gibt unterwegs Teile ab" [H]

- **Was das Bild im Funkverkehr vorhersagt [H, M]:**
  - Gibt ein Photon unterwegs Teile ab und wird roeter, ohne spaeter anzukommen (R1), traegt jede Sondenverbindung
    ein Zeichen davon. Der Doppler sagt "die Sonde entfernt sich ein wenig schneller", die Laufzeit sagt das nicht.
  - Das Vorzeichen ist fest (Rotverschiebung). Bei frequenzunabhaengigem kappa haengt es auch nicht vom Funkband ab
    (GS2, ungeprueft). Plasma dagegen haengt vom Band ab.
  - Bei Hubble-Rate fehlen im X-Band-Traeger bei Saturn rund 14 Schwingungen pro Tag gegenueber der Laufzeit
    (2 kappa D f = 1,7e-4 /s bei 8,4 GHz [M, f aus L]).
- **Was das ueber das Bild sagt [ES]:** Eine klassische Welle in einem zeitlich festen Raum kann ihre Frequenz unterwegs
  nicht senken, ohne Schwingungen zu verlieren. R1 ist deshalb eine Teilchen-Lesart: Jedes Photon gibt Energie ab.
  Der Sondentest prueft genau diese Lesart an einem kohaerenten Signal.
- **Was belegt ist:** Im Sonnensystem hat das niemand gemessen oder begrenzt (nach Recherchestand). Die Standardauswertung
  kann es nicht sehen, weil sie Doppler als Laufzeitaenderung rechnet (DE440) [S].
- **Was es fuer das Bild heisst, je nach Art der Teileabgabe:**
  1. **Spontan und ueberall gleich:** DES begrenzt das schon auf <= 2 % der Hubble-Rate [P]. Ein Sondentest aendert daran
     nur etwas, wenn er unter ~1,5e-28 /m kommt (lange Bahnboegen, Ka-Band-Ranging) [M].
  2. **Durch Stoesse mit Materie (dichteabhaengig):** Die DES-Schranke je Meter im fast leeren Raum laesst sich nur schwach
     uebertragen [M, Werte L]. Die Dichte des Sonnenwinds ist ~2e7-mal hoeher als die mittlere Baryonendichte, also
     erlaubt DES dort nur kappa < ~1e5 bis 4e5 H0/c. Dann waere der Sondentest die schaerfste verfuegbare Probe.
     Allerdings fiele ein dichteabhaengiger Verlust zuerst in Luft auf. Dort sind die Praezisionsstrecken
     rundweg-geregelt und blind (TEILE-SCHRANKE-L V1) [P].
  3. **Teileabgabe, die die Signalform mit streckt (R2):** Doppler gegen Laufzeit sieht sie nicht. Die Planetenephemeride
     saehe eine wachsende Laufzeit [ES].
- **Pioneer ist kein Beleg fuer das Bild:** Muedes Licht bei Hubble-Rate gaebe an Pioneer eine scheinbare Beschleunigung
  H0 v ~ 2,7e-14 m/s^2 nach aussen [M]. Gemessen war a_P ~ 8,7e-10 m/s^2 zur Sonne hin. Das Vorzeichen ist falsch und die
  Groesse liegt 3e4-mal daneben; die Richtung bestaetigen Carrera/Giulini 2006 [S].

## 7. Kartenvorschlag (hoechstens einer)

**DRVID-KAPPA-1 (datennah, Kleintest-tauglich):** Zeigt die nicht-dispersive Differenz "Laufzeit-Entfernung minus
aufsummierter Doppler" je Pass eine Steigung, die mit der Erde-Sonde-Entfernung D waechst?

- **Datensatz (frei, an der Quelle geprueft):** 2001 Mars Odyssey Radio Science Raw Data, ODY-M-RSS-1-RAW-V1.0, PDS
  Geosciences Node, 2002-01-01 bis 2019-01-31 [S, A15].
  - ATDF (2002 bis Anfang 2003): mit DRVID-Feld.
  - ODF (bis April 2017): Zweiwege-Doppler, Zweiwege-Zaehlphase, Range (Feldliste dataset.cat Z. 154 bis 171).
  - TNF: ab 2003.
  - Erde-Mars-Entfernung 0,37 bis 2,67 AE [L]; das gibt einen Hebel in D.
- **Vorgehen:**
  - Je Pass Range-Punkte gegen die aufsummierte Zaehlphase legen und die Steigung schaetzen.
  - Nach D und Sonne-Erde-Sonde-Winkel sortieren; nur Zweiwege-Daten (Dreiwege hat Uhrraten 5e-14).
  - Steigung gegen D auftragen. R1 sagt eine Gerade durch null mit Steigung kappa c voraus, mit festem Vorzeichen: Der
    Doppler zeigt mehr Entfernen als die Laufzeit (in der Konvention "Range minus Doppler" also negativ) [M].
- **Ableitbarkeitsprobe:**
  - *Vorab ableitbar [M]:*
    - Signal bei Hubble-Rate 0,13 bis 0,9 um/s ueber den D-Bereich, ~1 cm je 8-h-Pass bei 1 AE.
    - Fehler je Pass ~1e-5 m/s (Range-Rauschen 60 cm, ein Punkt je 10 min) plus ~5e-6 m/s Plasma (X allein).
    - Mit ~3000 brauchbaren Paessen ~2e-7 m/s, also eine Reichweite von grob 0,5 bis 1 H0/c.
  - *Nicht ableitbar:* die tatsaechliche nicht-dispersive DRVID-Steigung (Drift der Stationslaufzeit im Pass, Plasmareste,
    Transponder). Keine Veroeffentlichung gefunden (A1 bis A3, A10); Projekt-grep 09:07:39 ohne DRVID-Treffer.
  - *Kann scheitern und bestehen:* ja. Eine mit D wachsende Abweichung mit dem R1-Vorzeichen ist moeglich; Steigung
    null innerhalb der Fehler ebenso; eine Abweichung mit falschem Vorzeichen spraeche gegen R1 und fuer Systematik.
- **Ehrliche Reichweite:**
  - Fuer ein universelles kappa bleibt DES (0,02 H0/c) staerker. Die Karte prueft kappa im interplanetaren Raum, also die
    dichte- bzw. umgebungsabhaengige Lesart.
  - Unter H0/c kaeme man mit Juno oder Cassini (D 5 bis 10 AE, X/Ka) oder mit Ka-Band-Ranging (BepiColombo). Deren Zugang
    ist ungeprueft (A14 leer).
- Keine Rechnung auf fremden Rechnern noetig fuer die Vorpruefung. Der Lauf selbst gehoert nach Projektregel auf die .69.

## 8. Negativliste (nicht behaupten)

1. "Raumsondendaten schliessen muedes Licht im Sonnensystem aus." Nicht belegt; keine Analyse gefunden.
2. "Die Ephemeriden (DE440) begrenzen kappa." Sie nehmen Planetenbahnen aus Laufzeiten; R1 sehen sie nicht.
3. "A. J. Anderson hat H0 im Sonnensystem gemessen." Er hat a_P/c aus Pioneer 10 als H0 gelesen; Pioneer ist thermisch
   erklaert (Turyshev 2012).
4. Allen Joel Anderson (2010) nicht mit John D. Anderson (Pioneer-Analyse 2002) verwechseln.
5. "Pioneer zeigt muedes Licht oder das Hubble-Gesetz im Sonnensystem." Vorzeichen und Groesse passen nicht (Abschn. 6).
6. "Cassini erreicht 1e-14 bei 1000 s laut Bertotti 2003." Bertotti nicht gelesen. Belegt ist nur Asmar 2005: die besten
   Experimente ~3e-15 bei 1000 s, ohne Missionsnamen im Abstract.
7. "1e-14 entspricht 3 um/s." Im Zweiwege-Doppler sind es 1,5 um/s.
8. "Die Expansion wirkt auf den Sonden-Doppler nur in zweiter Ordnung." Carrera/Giulini: Es gibt einen in H linearen
   Term, er ist um beta unterdrueckt.
9. "Kopeikin 2012 hat einen H-Effekt gemessen." Das ist Theorie und ein Messvorschlag.
10. Die A10-Aussage (Pioneer als Hubble-Gesetz im Sonnensystem unter muedem Licht) keiner Quelle zuschreiben. Sie
    ist ungeprueft.
11. "Juno- oder Cassini-Rohdaten mit Range liegen frei im PDS." Nur Suchtreffer, nicht geprueft. Geprueft ist nur
    Mars Odyssey.
12. "Range-Biases werden je Pass frei geschaetzt." Nicht belegt. Belegt ist nur DE440: Der Kalibrierfehler ist allen
    Punkten eines Passes gemeinsam, ein Range-Punkt je Pass wird verwendet.
13. Die Reichweiten (0,5 bis 1 H0/c, 0,02 H0/c, 1e5 bis 4e5 H0/c) sind Schreibtischzahlen [M], keine Messungen.

## 9. Selbstanzeigen

1. **Zwei Abrufe leer:** A13 (arXiv-API, Zeitueberschreitung) und A14 (atmos.nmsu.edu, Verbindungsabbruch). Dadurch
   blieben ungeprueft: G3 (wird bei drehenden Sonden ein freier Doppler-Bias geschaetzt?), die Quelle der A10-Aussage und
   der Juno-Datensatz.
2. **Geschaetzte Zeit:** In ABRUFE.md stand bei A10 zuerst "09:03". Die Zeit war geschaetzt; ich habe sie gestrichen und
   daneben die gemessene 09:02:36 eingetragen. Ein zweiter Fall stand in der Abschlusszeile des ARBEITSFELD:
   "09:13 bis 09:20", wobei 09:20 sogar nach der Endzeit lag. Auch das ist gestrichen und durch die gemessenen Grenzen
   09:11:52 bis 09:17:12 ersetzt (Nachtrag nach der Endzeit, date 09:17:20).
3. **Erwartungen ohne eigene Zeitzeile:** Bei A13, A14 und A15 stehen die Erwartungen ohne eigene Zeitzeile. Ich habe sie
   im selben Befehl vor dem Abruf geschrieben; die date-Ausgaben dieser Befehle sind 09:02:55, 09:04:20 und 09:05:24.
4. **Pioneer-Grenze geschaetzt:** a_lim ist angenommen (1e-10 bzw. 1,33e-10 m/s^2). Turyshev 2012 nennt im Abstract
   keine Restschranke. Deshalb stehen im ARBEITSFELD zwei Werte (4e3 und 5e3 H0/c), beide nur als Groessenordnung.
5. **"Pioneer ohne Ranging":** nur [L] und ein Sekundaerzitat bei A. J. Anderson (S. 9), nicht an Anderson 2002 gelesen.
6. **"Fits schlucken R1":** Das ist eine Uebertragung [ES] des allgemeinen Beispiels in Thornton/Border 3.6 (unmodellierte
   Kraefte) und einer unbegutachteten Aussage (A. J. Anderson). Einen Fit mit eingebautem kappa habe ich nicht gesehen.
7. **Rechnungen von Hand, nicht gegengelesen:** v_app, y, DRVID je Pass, Fehler je Pass, Pioneer-Grenze,
   Dichteuebertragung (Omega_b, rho_crit, Sonnenwind als [L]), R2-Laufzeiten.
8. **Zahlenformat:** OpenAlex-Abstracts habe ich per jq aus dem Wortindex rekonstruiert. Zahlen wie "10 −15" koennen dabei
   verstuemmelt sein. Seitenzahlen stammen aus den Seitenumbruechen der pdftotext-Dateien, bei Thornton/Border aus den
   Kopfzeilen.
9. **Nicht gelesen (Budget):** BepiColombo MORE, New Horizons, Genova 2018 (MESSENGER-Gesamtfit), INPOP und Spengler
   u. a. 2022 im Volltext. Die Ephemeriden-Aussage stuetzt sich nur auf DE440.
10. **Bestaetigungssuche:** Den Verdacht "Ephemeride ist fuer R1 blind" habe ich vor A9 notiert und A9 gezielt danach
    gelesen.
11. **24-Monats-Suche (Regel 7):** nur ueber die Jahreszahlen 2025/2026 im Suchtext (A3, A10). Das Werkzeug hat keinen
    Datumsfilter. Der einzige Treffer im Fenster (arXiv:2602.09141) war nicht einschlaegig.
12. Endzeit: siehe letzte Zeile.

## 10. Einfach gesagt

Wir haben gefragt, ob Raumsonden schon zeigen, dass Licht unterwegs keine Energie verliert. Wuerde es Energie
verlieren, kaeme das Funksignal einer Sonde ein bisschen tiefer an, als ihre Bewegung erklaert, waehrend die Laufzeit des
Signals gleich bliebe. Diese beiden Messungen hat bisher niemand gezielt gegeneinander gehalten. Die Auswerteprogramme
gehen sogar davon aus, dass sie immer zusammenpassen. Die Daten dafuer liegen frei im Netz, etwa von der Mars-Sonde
Odyssey, sogar mit einer fertigen Vergleichsspalte; spannend ist das vor allem, falls das Licht nur dort ermuedet, wo
Materie ist, denn fuer ein ueberall gleiches Ermueden sind ferne Sternexplosionen schon die strengere Probe.

## Anhang A. Regime und Moderatoren (Feldregel 1)

- **R1 gegen R2 gegen R3:** siehe Abschnitt 4. Moderator R1/R2: Wird die Modulation (Entfernungscode, Lichtkurve)
  mitgestaucht? Das ist derselbe Moderator wie G7 in TEILE-SCHRANKE-L (Zeitstreckung).
  - R1 bricht die Identitaet "Doppler = Laufzeitaenderung" [M].
  - R2 haelt sie, verschiebt aber beide gegen die Bahndynamik.
  - R3 waechst mit t, nicht mit D.
- **Medium bzw. Dichte:** intergalaktisch ~2,7e-7 /cm^3, Sonnenwind ~5 /cm^3, Luft ~2,5e19 /cm^3 [L].
  - Bei universellem kappa gilt DES.
  - Bei dichteabhaengigem kappa zaehlen Sondenstrecken und vor allem bodennahe Strecken [M, ES].
- **Frequenz:** Radio (8 bis 32 GHz) gegen optisch (DES). Fuer achromatisches z muss kappa gleich sein; nicht geprueft (GS2).
- **Messart:**
  - Zweiweg nutzt eine Uhr; Dreiweg hat Uhrraten 5e-14 [S, Tab. 3-3], in der Groesse des Hubble-Signals bei Saturn.
  - Drehende Sonden haben einen Spin-Beitrag zum Doppler (Juno 2 U/min, Werkzeugtext A12).
- **Auswertung:** kurze Boegen (Perijove, Vorbeiflug) gegen lange Boegen gegen modellfreie Probe je Pass (DRVID).
  Nur die Probe je Pass ist frei von Bahnparametern [M].
- **Kosmologischer Doppler-Term:** Carrera/Giulini zeigen im Doppler allein dieselbe Drift-Form wie R1 bei Hubble-Rate
  [S, ES]. Nur die Laufzeit trennt beides.

## Anhang B. Unterscheidungspunkte (Feldregel 2)

| Paar | wo sie messbar auseinanderlaufen | Daten? |
|---|---|---|
| R1 gegen keine neue Physik | nicht-dispersive DRVID-Steigung ~ D; am staerksten bei grossem D (Saturn 8,5 cm je Pass, New Horizons ~0,6 m je Pass bei ~60 AE [L]) und vielen Paessen | Odyssey geprueft (D <= 2,67 AE); Juno/Cassini/NH ungeprueft |
| R1 gegen R3 | Planetenumlaeufer mit wechselndem D: R1 folgt D(t) ueber die synodische Periode, R3 waechst linear in t | Mars-Umlaeufer (Odyssey), MESSENGER |
| R1 gegen R2 | Laufzeit: R1 unveraendert, R2 waechst mit; der Doppler ist in beiden gleich | DRVID (R1) gegen Ephemeriden-Range-Reste (R2) |
| R1 gegen Plasma | Plasma ~1/f^2 und wechselnd im Vorzeichen; R1 achromatisch mit festem Vorzeichen | Zweiband X/Ka (Cassini, Juno); Odyssey nur X [L] |
| R1 gegen Uhrrate | Zweiweg (eine Uhr) gegen Dreiweg (Uhrrate 5e-14) | nur Zweiweg verwenden |
| universelles gegen dichteabhaengiges kappa | DES (fast leerer Raum) gegen Sondenstrecke (Sonnenwind) gegen bodennahe Luftstrecke | DES [P]; Sondentest (Abschn. 7); Luftstrecken blind (TEILE-SCHRANKE-L) |
| Expansion im Lichtweg (Carrera/Giulini-Term) gegen R1 | nur ueber die Laufzeit; im Doppler gleiche Drift H v | Range noetig |

## Anhang C. Gegensweep-Befunde (Feldregel 4; ausfuehrlich ARBEITSFELD Abschn. 3)

- **GS1 (geprueft am Schreibtisch, [P, M]):** "Unter H0/c" ist fuer ein universelles kappa nicht die richtige Latte; DES
  liegt bei 0,02 H0/c. Wichtigster Befund des Gegensweeps.
- **GS2 (nicht geprueft):** Haengt kappa von der Frequenz ab? Radio gegen optisch.
- **GS3 (teilweise):** Zweiwege-Doppler ohne freien Bias. DE440 und Thornton/Border nennen keinen. Spin-Bias bei Juno
  ungeklaert. Dreiweg-Uhrrate 5e-14 [S].
- **GS4 (geprueft, [M]):** "Laufzeit unberuehrt" gilt nur in R1. Die Kopplung ueber Rate-Aiding liegt bei ~mm.
- **GS5 (geprueft an der Quelle, [S]):** DE440 rechnet Doppler als Laufzeitaenderung. Das ist die von R1 gebrochene
  Identitaet.
- **GS6 (geprueft, [S] und [M]):** Der H-lineare Term zeigt nach aussen, Pioneer nach innen (Carrera/Giulini S. 8) [S].
  R1 bei Hubble-Rate hat an einer fliegenden Sonde dieselbe Richtung [M].
- **Auftragsfragen:**
  - Schluckt die Bahnanpassung den Versatz? Bei Doppler allein ja (Pioneer [M]; A. J. Anderson S. 3). Bei Ephemeriden
    kommt er gar nicht hinein (DE440). In Sonde-Planet-Fits ist es offen; Thornton/Border 3.6 macht "schlucken"
    wahrscheinlich [ES].
  - Pruefen Analysen die Konsistenz? Ja, als DRVID, aber nur fuer Plasma. Eine nicht-dispersive Auswertung fand ich
    nicht.

## Anhang D. Kalibrierung

- **(a) gemessen [S]:**
  - Asmar 2005 (3e-15 bei 1000 s); Thornton/Border Tab. 3-3.
  - DE440: Datentypen und Reste.
  - Pioneer: a_P (Anderson 2002).
  - Odyssey-Archivfelder.
- **(b) verdichtet [M, ES]:**
  - Regime R1/R2/R3; DRVID als R1-Groesse; Ephemeride R1-blind.
  - Reichweiten der Probe je Pass; Pioneer-Grenze; Dichteuebertragung.
- **(c) gewachsene Gewissheit ohne neue Evidenz:**
  - "Niemand hat R1 im Sonnensystem begrenzt." Die Sicherheit stieg ab A3/A10. Sie stuetzt sich auf Werkzeugtexte von
    Suchmaschinen und auf zwei leere Abrufe. Warnzeichen nach Vorgabe.
  - "Bahnfits schlucken den Versatz" beruht auf einem allgemeinen Beispiel, nicht auf einem Fit mit kappa.

## Anhang E. Offene Fragen

1. Schluckt eine Bahnbestimmung mit eingebautem kappa-Parameter den Versatz? Gemeint sind Planetenumlaeufer mit langen
   Boegen; der mittlere Doppler-Rest wird gegen die laufzeitbasierte Planetenbahn gelegt. Nach Nennwert waere das bis
   ~0,05 H0/c empfindlich [M], aber nur mit Bahnbestimmungssoftware testbar.
2. Schaetzen Juno, New Horizons und Pioneer einen freien Doppler-Bias fuer den Spin?
3. Gibt es DSN-Berichte mit gemittelter DRVID ueber viele Paesse, also mit einem nicht-dispersiven Rest? MacDoran 1970 und
   die TDA-Berichte habe ich nicht gelesen.
4. Wie gut stimmen Radio- und optische Rotverschiebungen derselben Quellen ueberein (GS2)?
5. LLR als R2-Test: Bei Hubble-Rate waechst die scheinbare Entfernung um 2,7 cm je Jahr (H0 x 3,84e8 m) [M]. Gemessen
   werden 3,8 cm je Jahr Gezeitenentfernung [L]. Schluckt das Gezeitenmodell den Unterschied?
6. Was "klaeren" Spengler u. a. 2022 an Kopeikins Behauptungen?
7. Welche Quelle steht hinter der A10-Aussage?

## Anhang F. Quellenliste (Abrufstand 2026-10-05; Kopien in quellen/)

- **A4** export.arxiv.org 08:54:10 (quellen/A4-arxiv-batch-20261005-085410.xml), je Abstract [S]:
  - Anderson, J. D., Laing, P. A., Lau, E. L., Liu, A. S., Nieto, M. M., Turyshev, S. G., "Study of the anomalous
    acceleration of Pioneer 10 and 11", Phys. Rev. D 65 (2002) 082004, https://arxiv.org/abs/gr-qc/0104064
  - Turyshev, S. G., Toth, V. T., Kinsella, G., Lee, S.-C., Lok, S. M., Ellis, J., "Support for the thermal origin of the
    Pioneer anomaly", Phys. Rev. Lett. 108 (2012) 241101, https://arxiv.org/abs/1204.2507
  - Kopeikin, S., "Celestial Ephemerides in an Expanding Universe", Phys. Rev. D 86 (2012) 064004,
    https://arxiv.org/abs/1207.3873
  - Spengler, F., Belenchia, A., Raetzel, D., Braun, D., "Influence of cosmological expansion in local experiments",
    Class. Quantum Grav. 39 (2022) 055005, https://arxiv.org/abs/2109.03280
  - McQuinn, M. u. a., "NIAC project report: Solar system-scale VLBI to dramatically improve cosmological distance
    measurements" (2026), https://arxiv.org/abs/2602.09141
- **A5** arxiv.org 08:55:43 (quellen/A5-arxiv-1011.1944-20261005-085543.pdf, .txt) [S Volltext]: Anderson, Allen Joel,
  "The Measurement of the Hubble Constant H_0 in the Solar System", arXiv:1011.1944v1 (2010, ohne Journal-Angabe,
  physics.space-ph), https://arxiv.org/abs/1011.1944
- **A6** arxiv.org 08:55:45 (quellen/A6-arxiv-gr-qc-0605078-20261005-085545.pdf, .txt) [S Volltext]: Carrera, M.,
  Giulini, D., "On Doppler tracking in cosmological spacetimes", Class. Quantum Grav. 23 (2006) 7483,
  https://arxiv.org/abs/gr-qc/0605078
- **A7** api.openalex.org 08:57:59 (quellen/A7-openalex-doppler-noise-20261005-085759.json):
  - Asmar, S. W., Armstrong, J. W., Iess, L., Tortora, P., "Spacecraft Doppler tracking: Noise budget and accuracy
    achievable in precision radio science observations", Radio Sci. 40 (2005) RS2001,
    https://doi.org/10.1029/2004RS003101 [S Abstract]
  - Armstrong, J. W., "Low-Frequency Gravitational Wave Searches Using Spacecraft Doppler Tracking", Living Rev.
    Relativ. 9 (2006) 1, https://doi.org/10.12942/lrr-2006-1 [S Abstract]
  - Bertotti, B., Iess, L., Tortora, P., "A test of general relativity using radio links with the Cassini spacecraft",
    Nature 425 (2003) 374, https://doi.org/10.1038/nature01997 [nur Titel und Autoren; kein Abstract im Abruf]
- **A8** descanso.jpl.nasa.gov 08:59:19 (quellen/A8-descanso1-thornton-border-20261005-085919.pdf, .txt) [S Volltext]:
  Thornton, C. L., Border, J. S., "Radiometric Tracking Techniques for Deep-Space Navigation", DESCANSO Monograph 1,
  JPL Publication 00-11 (Oktober 2000), https://descanso.jpl.nasa.gov/monograph/series1/Descanso1_all.pdf
- **A9** ssd.jpl.nasa.gov 09:00:29 (quellen/A9-jpl-de440-20261005-090029.pdf, .txt) [S Volltext]: Park, R. S., Folkner,
  W. M., Williams, J. G., Boggs, D. H., "The JPL Planetary and Lunar Ephemerides DE440 and DE441", Astron. J. 161
  (2021) 105, https://ssd.jpl.nasa.gov/doc/Park.2021.AJ.DE440.pdf
- **A15** pds-geosciences.wustl.edu 09:05:24 (quellen/A15-pds-ody-rss-raw-dataset-20261005-090524.cat) [S]:
  "2001 Mars Odyssey Radio Science Raw Data", ODY-M-RSS-1-RAW-V1.0, Katalogdatei,
  https://pds-geosciences.wustl.edu/ody/ody-m-rss-1-raw-v1/odrs_0275/catalog/dataset.cat
- **Websuchen ohne Kopie** (Werkzeugtext, nur Wegweiser): A1, A2 (u. a. https://ipnpr.jpl.nasa.gov/progress_report/42-106/106A.html,
  https://ntrs.nasa.gov/citations/19950021345), A3, A10 (u. a. https://arxiv.org/abs/astro-ph/0701132v3,
  https://arxiv.org/pdf/0707.3351), A11 (u. a. https://atmos.nmsu.edu/data_and_services/atmospheres_data/JUNO/gravity.html,
  https://pds-geosciences.wustl.edu/MESSENGER/mess-v_h-rss-1-edr-rawdata-v1/messrs_0xxx/document/mess_rs_edr_sis.pdf),
  A12 (u. a. https://arxiv.org/pdf/1411.1613).
- **Leer:** A13 (export.arxiv.org, Zeitueberschreitung), A14 (atmos.nmsu.edu, Verbindungsabbruch).
- **Projekt [P]:**
  - RUNDE-37/teile-schranke-l/DOSSIER.md: DES-Schranke, Faser-Blindheit V1, Lesarten.
  - coordination/art-grenzen-20260921/UNGEPRUEFT.md Abschn. 1.1 bis 1.3: Pioneer erledigt, Voyager ohne Ranging,
    Cassini-Ephemeride.
- **Nur Gedaechtnis [L]:**
  - H0 = 70 km/s/Mpc; Omega_b = 0,049; Sonnenwind ~5 /cm^3; Luftdichte und Skalenhoehe.
  - Erde-Mars 0,37 bis 2,67 AE; New Horizons ~60 AE; X-Band 8,4 GHz.
  - Pioneer ohne Ranging; LLR-Gezeitenentfernung 3,8 cm je Jahr.

---
Endzeit (date): 2026-10-05 09:17:12 CEST. Abrufe 15 von 15 (2 leer).
