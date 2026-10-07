# TEILE-SCHRANKE-L: Arbeitsfeld (feldforscher fuer claude-primary)

- Start 2026-10-05 08:16:17 CEST (date). Zeitbox 60 min, hoechstens 15 Netzabrufe.
- Bindend: KARTE.md (TS0 bis TS4 unveraendert). Gelesen: KARTE.md ganz, licht-teile-l/DOSSIER.md ganz (08:17 bis 08:20).
- Feld-Regeln: eine Datei (diese), Erwartung mit date vor jedem Abruf, Gestrichenes bleibt stehen (~~...~~).
- Kennzeichen: [E] [M] [S] [L] [H] [P]; [ES] eigener Schluss.

## 0. Lokale Funde (kein Netzabruf)

- [P] neue-theorie/gitter-checkliste.json Z. 32: "Rainville et al. 2005 (Nature 438, 1096): Δmc² gegen
  γ-Energie bei Neutroneneinfang, Übereinstimmung 4e-7." Projektzahl, keine Primaerquelle.
- [P] coordination/art-grenzen-20260921/GEPRUEFT.md Z. 361 bis 366 (Kennung [A*] = Rechercheagent hat am
  Abstract/Volltext geprueft, claude-primary nicht selbst):
  - Pound & Rebka 1960, PRL 4, 337: (Delta nu)_exp/(Delta nu)_theor = 1,05 +- 0,10.
  - Pound & Snider 1965, PR 140, B788: 0,9990 +- 0,0076.
  - Gravity Probe A 1980, PRL 45, 2081: Uebereinstimmung auf 70e-6.
  - Galileo (Delva) 2018: alpha = (+0,19 +- 2,48)e-5; Tokyo Skytree 2020: 450 m, alpha 9,1e-5.
- [P] RUNDE-36/SAGNAC.md Z. 60: Moessbauer-Rotor (Kuendig 1963 [L]) nur als Zeitdehnungsmessung. Keine Zahl fuer
  diese Karte.

## 1. Vorab-Ueberlegungen (Schreibtisch, vor jedem Abruf, 08:22)

### 1.1 Was heisst "unsichtbarer Teil"? Drei Lesarten, drei verschiedene Groessen [ES]
- L-a: Teile tragen Energie, die NICHT in der Frequenz steckt: E_gesamt = h nu + E_unsichtbar.
  Sichtbar ueber Energiebilanz gegen Wellenlaenge (Rainville: Delta m c^2 gegen h c/lambda).
- L-b: h nu = E_gesamt, aber der Detektor nimmt nur (1 - eps) h nu auf, der Rest fliegt durch.
  Sichtbar ueber deponierte Energie gegen h nu (Kalorimeter, TES, Ge, Radiometer) und ueber Resonanzabsorption
  (Moessbauer: Absorber braucht E innerhalb Gamma).
- L-c: Teile werden unterwegs abgegeben: nu sinkt mit der Strecke ("muedes Licht"). Natuerliche Einheit:
  relativ je Strecke, kappa = -d ln nu / dL [1/m].
- Ein Teil, der weder Energie noch Impuls traegt, ist fuer alle drei unsichtbar (Gegensweep-Beispiel der Leitung).

### 1.2 Vorab ableitbare Schreibtisch-Punkte [M], vor jedem Abruf notiert
- Hubble-Rate als Massstab fuer L-c: H0/c = 70 km/s/Mpc / c ~ 2,3e-4 /Mpc ~ 7,6e-27 /m [M, H0 aus L].
  Muedes Licht als alleinige Ursache der Rotverschiebung braeuchte kappa ~ 7,6e-27 /m.
- Laborfrequenzvergleich ueber ~1000 bis 2000 km mit ~1e-19 relativ ergaebe hoechstens ~1e-25 /m [M], also
  SCHWAECHER als die Hubble-Rate. Erwartung: Laborstrecken koennen muedes Licht auf Hubble-Niveau gar nicht sehen.
- Verdacht (Gegensweep vorgezogen) [ES]: Glasfaserstrecken mit Doppler-Rauschunterdrueckung (Hin- und
  Rueckweg, Servo auf die Rundreisephase) kompensieren jeden reziproken Phasen- bzw. Frequenzgang. Ein
  Frequenzverlust je Strecke ist reziprok (gleich in beide Richtungen). Dann wuerde der Servo ihn
  ausregeln, und der Uhrenvergleich am Ende waere blind dafuer. Dasselbe gilt fuer Zweiwege-Verfahren und
  fuer die Doppler-Kompensation von Gravity Probe A. Pound/Rebka bilden die Differenz oben minus unten; ein
  richtungsunabhaengiger Verlust ueber dieselben 22,5 m faellt dort ebenfalls heraus.
  -> Zu pruefen an der Quelle: Beschreibt die Faserarbeit die Kompensation ueber den Rundweg?
- TES-Kalibrierung [ES]: Wird die Energieskala mit den Photonenspitzen selbst geeicht, faellt ein
  gleichmaessiger Anteil eps heraus. Dann sieht TES nur Nebenspitzen (Bruchteile) oder ein eps, das von nu
  abhaengt, nicht ein festes eps.

### 1.3 Abrufplan (15 hoechstens)
1. INSPIRE-Sammelabruf per DOI/arXiv: Rainville 2005, Pound/Rebka 1960, Pound/Snider 1965, Droste 2013,
   Lisdat 2016, DES-Zeitdehnung 2024, Blondin 2008, Lewis/Brewer 2023, Heeck 2013.
2. TES-Einzelphotonenspektren (Lita/Miller/Nam 2008 o. ae.).
3. Fe-57-Lebensdauer an Datenquelle (TS0, nur Kontrolle).
4. Websuche 24 Monate: muedes Licht / Zeitdehnung (Feldregel 7).
5. Websuche: Compton-Koinzidenzen, Energieerhaltung je Ereignis.
6. Websuche: Labortest muedes Licht / Frequenzverlust je Strecke.
7. bis 15. Reserve fuer Erwartungsverstoesse.

## 2. Abrufprotokoll mit Erwartung (Erwartung VOR dem Abruf, Zeit per date)

### A1 (INSPIRE-Sammelabruf)
- Erwartung notiert 2026-10-05 08:23:08 CEST: Rainville-Abstract nennt Uebereinstimmung Delta m c^2 gegen Gammaenergie auf ~4e-7 (1 sigma, (-1,4 +- 4,4)e-7). Pound/Rebka-Abstract nennt 1,05 +- 0,10 bzw. Pound/Snider 0,9990 +- 0,0076, gemessen als Differenz oben/unten. Droste 2013: Unsicherheit ~4e-19 ueber 1840 km mit Rauschunterdrueckung ueber den Rundweg. Lisdat 2016: Sr-Uhren Paris-Braunschweig, Uebereinstimmung ~5e-17. DES 2024: b = 1,003 +- 0,005 (stat) +- 0,010 (sys), muedes Licht weit ausgeschlossen. Blondin 2008: 1/(1+z) bestaetigt. Lewis/Brewer 2023: Quasar-Zeitdehnung bis z ~ 4. Heeck 2013: Photonlebensdauer > ~3 Jahre im Ruhesystem. Einige alte APS-Abstracts fehlen in INSPIRE.
- Ausgang A1 (08:23:13, quellen/A1-inspire-batch-20261005-082313.json):
  - bestaetigt, eine Zeile je Quelle:
    - DES (White u. a. 2024, MNRAS 533, 3365, arXiv:2406.05050): 1504 SNe Ia, 0,1 < z < 1,2, b = 1,003 +- 0,005
      (stat) +- 0,010 (sys), "ruling out any non-time-dilating cosmological models at very high significance" [S Abstract].
    - Blondin u. a. 2008 (ApJ 682, 724, arXiv:0804.3595): 13 SNe, Alterungsrate passt zu 1/(1+z), schliesst
      "Zwicky's 'tired light'" aus; keine Zahl im Abstract [S Abstract].
    - Pound/Snider 1965 (PR 140, B788): (0,9990 +- 0,0076) x 4,905e-15 = 2gh/c^2, Systematik-Grenze 0,010, 75 ft [S Abstract].
    - Heeck 2013 (PRL 111, 021801): Photonlebensdauer > 3 Jahre im Ruhesystem bei Photonmasse an der Grenze,
      Mikrowellenphotonen um ~1e15 zeitgedehnt [S Abstract]. Misst Zerfall (Anzahl), nicht Energieanteil.
    - Lewis/Brewer 2023 (Nat. Astron., arXiv:2306.04053): Quasar-Zeitdehnung an 190 Quasaren nachgewiesen; keine
      Praezisionszahl im Abstract [S Abstract].
  - kleiner Verstoss: Rainville 2005, Droste 2013, Lisdat 2016 stehen nicht in INSPIRE (Metrologie/Nature-Kurzbeitrag).
    Pound/Rebka 1960 ohne Abstract. -> Ersatz ueber OpenAlex.
  - Beobachtung zu Pound/Snider [ES]: Sollwert ist 2gh/c^2, also die Differenz Quelle oben gegen Quelle unten.
    Ein richtungsunabhaengiger Verlust ueber dieselbe Strecke faellt in dieser Differenz heraus. Noch nicht an
    einer Textstelle gesehen, nur aus dem Faktor 2 erschlossen.
### A2 (OpenAlex-Sammelabruf)
- Erwartung notiert 2026-10-05 08:23:42 CEST: Rainville-Abstract: Uebereinstimmung auf ~4e-7 (E = mc^2 'to within 0,00004 %'); Lisdat 2016: Sr-Uhren PTB-SYRTE ueber 1415 km Faser, Unsicherheit ~5e-17, Faser mit Rauschunterdrueckung; Droste 2013: 1840 km, Unsicherheit ~4e-19; APS-Abstract (Droste) fehlt evtl. in OpenAlex.
- Ausgang A2 (08:23:48, quellen/A2-openalex-batch-20261005-082348.json, Abstract aus OpenAlex-Wortindex per jq in
  Reihenfolge gelesen):
  - bestaetigt: Lisdat u. a. 2016 (Nat. Commun. 7, 12443): zwei Sr-Uhren Paris-Braunschweig, 1415 km Faser,
    Uebereinstimmung bei Unsicherheit 5e-17, Faseruebertragung vernachlaessigbar [S Abstract].
  - leicht abweichend: Droste u. a. 2013 (PRL 111, 110801): 1840 km, "single-span stabilization"; kein
    systematischer Versatz zwischen gesendeter und uebertragener Frequenz innerhalb der statistischen Unsicherheit von
    etwa 3e-19 (erwartet 4e-19; 4e-19 ist dort die Allan-Abweichung nach 100 s) [S Abstract].
    [Nachtrag 08:41: Zitat auf unter 15 Woerter gekuerzt (Urheberrecht), Inhalt unveraendert.]
  - Rainville: kein Abstract in OpenAlex -> Verlagsseite.
  - [ES] Wichtig fuer den Gegensweep: "stabilization" heisst Regelung ueber den Rueckweg. Ob der Text die
    Reziprozitaet als Voraussetzung nennt, steht nicht im Abstract. -> A4 (Lisdat-Volltext, frei).
  - [M] Umrechnung in die natuerliche Einheit, FALLS die Strecke den Verlust saehe: 3e-19 / 1,84e6 m ~ 1,6e-25 /m;
    5e-17 / 1,415e6 m ~ 3,5e-23 /m. Beide schwaecher als die Hubble-Rate 7,6e-27 /m (Abschn. 1.2).
### A3 (nature.com, Rainville 2005)
- Erwartung notiert 2026-10-05 08:24:35 CEST: Kurzbeitrag mit Einleitungsabsatz; Zahl: Delta m c^2 und h c/lambda stimmen auf ~4e-7 ueberein ('0,00004 %'), Isotope 29Si und 33S (Neutroneneinfang), GAMS4 am ILL und Penning-Falle am MIT. Die Zahl steht evtl. nur im Volltext hinter der Bezahlschranke.
- Ausgang A3 (08:24:39): bestaetigt. Rainville u. a. 2005 (Nature 438, 1096): E = Kernbindungsenergie aus
  Gamma-Wellenlaengen, Delta m aus Massendifferenz; "1-Δmc^2/E =(-1.4±4.4)×10^-7", Isotope von Si und S
  [S Abstract]. Eine Zeile, weiter.
  - [ES] Was das misst: Lesart L-a (Energie, die nicht in h nu steckt), summiert ueber die Kaskade. L-b (Detektor
    nimmt weniger auf) sieht es NICHT, denn E kommt aus der Beugung (Welle), nicht aus deponierter Energie.
### A4 (nature.com, Lisdat 2016 Volltext)
- Erwartung notiert 2026-10-05 08:25:01 CEST: Methodenteil beschreibt Faserrauschunterdrueckung: Teil des Lichts wird am Fernende zurueckgeschickt, Rundweg-Phase wird am Anfang gemessen und per AOM korrigiert; Voraussetzung Reziprozitaet von Hin- und Rueckweg; Restfehler aus nicht-reziproken Effekten. Damit waere ein reziproker Frequenzverlust je Strecke ausgeregelt (Gegensweep-Verdacht).
- Ausgang A4 (08:25:05): bestaetigt (Prinzip), eine Zeile: Lisdat u. a. 2016, Haupttext: Ein Teil des Lichts wird am
  Fernende durch dieselbe Faser zurueckgeschickt, das Rundweg-Phasenrauschen am Sender gemessen und "actively
  cancelled"; Methods (Abschnitt "Link noise cancellation"): Das Rundweg-Rauschen wird an einem Ende gemessen und
  korrigiert [S Volltext]. Reziprozitaet wird nicht ausgesprochen, ist aber die stille Voraussetzung.
  [Nachtrag 08:41: lange Zitate durch Umschreibung ersetzt (Urheberrecht, hoechstens ein kurzes Zitat je Quelle).]
  - [M, ableitbar] Folge: Verlust kappa je Meter gibt auf dem Hinweg den Frequenzversatz -nu kappa L, auf dem Rundweg
    -2 nu kappa L. Der Regler schiebt den Eingang um +nu kappa L. Am Fernende kommt nu an, genau wie ohne Verlust.
    Der Vergleich "gesendet gegen uebertragen" (Droste: 3e-19) und der Uhrenvergleich (Lisdat: 5e-17) sind damit
    BLIND fuer einen reziproken Verlust je Strecke. Sichtbar waere er nur im Mittelwert des Stellsignals
    (nu kappa L; bei Hubble-Rate fuer Droste: 1,94e14 Hz x 7,6e-27 /m x 1,84e6 m ~ 2,7e-6 Hz), der von
    temperaturbedingten Laengenaenderungen der Faser ueberdeckt wird [ES].
  - Damit wackelt TS1 im Kern: Der Frequenzvergleich ueber Glasfaser liefert gar keine Schranke fuer diese Groesse.
### A5 (WebSearch: Labortest muedes Licht / Frequenzverlust je Strecke)
- Erwartung notiert 2026-10-05 08:26:01 CEST: Kein eigener Labortest, der eine Frequenzabnahme je Strecke misst. Hoechstens Vorschlaege oder Randliteratur; dazu Treffer zu Zwicky und zur kosmologischen Widerlegung.
### A6 (WebSearch 24 Monate: muedes Licht und Zeitdehnung 2025/2026)
- Erwartung notiert 2026-10-05 08:26:01 CEST: DES 2024 als Bestwert; evtl. neue Zeitdehnungsmessungen an GRBs oder Quasaren 2025; einzelne Arbeiten, die muedes Licht als Teilursache vertreten (Gupta CCC+TL); keine Messung, die die Zeitdehnung in Frage stellt.
- Ausgang A5 (Suche 08:26, keine Kopie, Werkzeugtext): wie erwartet kein Labortest. Der Werkzeugtext spricht von einem
  Vorschlag, die Hubble-Rate im Labor als Frequenzdrift proportional zur Flugzeit zu messen (~1e-18 /s). Das passt zu
  meiner Schreibtischzahl H0 ~ 2,3e-18 /s [M], ist aber keine Quelle. Herkunft unklar (0906.3476 oder 2005.07931).
- Ausgang A6 (Suche 08:26, Werkzeugtext): bestaetigt DES 2024. Werkzeugtext (umschrieben): Hybrid- und statische
  Modelle wie muedes Licht werden weiter diskutiert. Im 24-Monats-Fenster nur ein Treffer arXiv:2603.00427 mit unbekanntem
  Inhalt. Lewis/Brewer b = 1,28 +0,28/-0,29 nur aus dem Werkzeugtext, nicht zitierfaehig.
### A7 (INSPIRE-Sammelabruf 2: 2603.00427, 0906.3476, 2005.07931, 2305.06771)
- Erwartung notiert 2026-10-05 08:26:32 CEST: 2603.00427 ist eine neue Zeitdehnungsarbeit (GRB, Quasar oder SN) ohne Widerspruch zu b = 1; 0906.3476 oder 2005.07931 enthalten den Laborvorschlag 'Hubble-Drift ~1e-18 /s' als Theorie ohne Messung; 2305.06771 ist eine Zeitdehnungsuebersicht (Lewis 2023) mit Quasar-b.
- Ausgang A7 (08:26:36): ERWARTUNGSVERSTOSS (mittel). Erwartet: keine Arbeit stellt die Zeitdehnung in Frage.
  Gefunden: Lee 2026 (EPJC, arXiv:2603.00427) schreibt, Quasar-Analysen "frequently yield null results", GRBs zeigen
  grosse Streuung; er erklaert das theoretisch (Quellenart, Auswahleffekt) [S Abstract]. Sanejouand (IJMPD,
  arXiv:2005.07931) vertritt ein Muedes-Licht-Modell mit Photonlebensdauer "one third of the Hubble time" und nennt
  als Falsifikation eine allgemein beobachtete Zeitdehnung, also auch bei anderen Ereignissen als SN-Ia-Lichtkurven
  [S Abstract]. [Nachtrag 08:41: zweites Zitat umschrieben (Urheberrecht).]
  - Korrigierte Erwartung: Die Literatur hat zwei Lager nach QUELLENART (Feldregel 1): diskrete Ereignisse (SN Ia,
    teils GRB) zeigen (1+z); stochastische Variabilitaet (Quasare) mal ja (Lewis/Brewer 2023), mal nein.
  - [ES] Moderator ist die Quelle bzw. die Auswertung, nicht der Lichtweg: Ein Energieverlust unterwegs haengt nur am
    Weg, und SN-Licht und Quasarlicht laufen bei gleichem z aehnliche Wege. Die SN-Messung begrenzt deshalb den
    Wegeffekt fuer optische Photonen bis z ~ 1,2 unabhaengig vom Quasarstreit. Sanejouands Falsifikationskriterium
    ist mit Blondin 2008 (Spektralalterung, keine Lichtkurve, A1) und Lewis/Brewer 2023 (Quasare, A1) nach
    Abstractlage erfuellt; seine Antwort darauf habe ich nicht gesucht.
  - [M] Schranke aus DES: b = 1,003 +- 0,011 (stat und sys quadratisch). Anteil f von ln(1+z) ohne Zeitdehnung:
    b = 1 - f. 95 %: b > 1,003 - 1,96 x 0,0112 = 0,981, also f < ~0,02. Mit kappa konstant: kappa < ~0,02 H0/c
    ~ 1,5e-28 /m (H0 = 70 km/s/Mpc [L]). Bis z = 1,2: Delta ln E (ohne Zeitdehnung) < 0,02 x ln 2,2 ~ 0,016.
### A8 (OpenAlex-Suche: TES-Einzelphotonenspektren)
- Erwartung notiert 2026-10-05 08:27:25 CEST: Optische TES (W oder Ti) bei 1550 nm (0,8 eV): Aufloesung 0,1 bis 0,3 eV FWHM, Spitzen bei n h nu fuer n = 1 bis ~10, Nachweiswahrscheinlichkeit 95 bis 98 %. Relative Breite je Photon 0,1 bis 0,4. Abstracts nennen keine Nebenspitzen bei Bruchteilen. Die Energieskala wird meist an den Spitzen selbst geeicht.
- Ausgang A8 (08:27:29, Abstracts aus OpenAlex-Wortindex):
  - bestaetigt (Zahlen): optische TES bei 0,8 eV: 67 meV FWHM (Au/Ti, Tc 115 mK), "typical energy resolution of
    optical TESs was 150 meV" (SuST 2022, doi 10.1088/1361-6668/ac7e7b) [S Abstract]; 0,113 eV intrinsisch (APL 2013,
    doi 10.1063/1.4815922) [S Abstract]; Weitband-TES 1,8 eV bei 1,5 keV (Photonics 2025, doi
    10.3390/photonics12060609) [S Abstract]. Relativ je Photon (FWHM/E): 0,08 bis 0,19 optisch, 1,2e-3 bei 1,5 keV [M].
  - ERWARTUNGSVERSTOSS (stark, bestaetigt meinen Kalibrierverdacht aus 1.2): Die Logik laeuft umgekehrt. IEEE TASC 2021
    (doi 10.1109/tasc.2021.3053506): "Pulses of narrow line-width optical photons can be used to calibrate"
    TES-Mikrokalorimeter; Photonenzahl von 3-eV-Photonen bis etwa 300 je Puls aufgeloest; Linienform laut Abstract
    einfach gaussisch [S Abstract]. Die Annahme E = n h nu ist also das EICHNORMAL, nicht der Befund.
    [Nachtrag 08:41: auf ein kurzes Zitat je Quelle gekuerzt (Urheberrecht).]
  - Korrigierte Erwartung: TES sieht kein gleichmaessiges eps (es steckt in der Eichung). TES sieht (i) eine
    Streuung von eps von Photon zu Photon (verbreitert die n-Spitzen mit Wurzel n), (ii) Nebenspitzen bei Bruchteilen,
    (iii) ein eps, das von nu abhaengt (Vergleich verschiedener Wellenlaengen). Abstracts nennen keine Nebenspitzen;
    das ist kein Beleg fuer ihr Fehlen.
### A9 (IAEA LiveChart-API: Fe-57-Niveaus)
- Erwartung notiert 2026-10-05 08:28:14 CEST: Niveau 14,4129 keV, Halbwertszeit ~98 ns (98,3 oder 98,0 ns). Daraus Gamma = hbar ln2/T_1/2 ~ 4,7e-9 eV, Gamma/E ~ 3,2e-13 [M]. TS0 trifft ein.
- Ausgang A9 (08:28:19): leer, Cloudflare-Sperre. Zaehlt mit. Ersatz ueber OpenAlex-Abstracts (Kernresonanzstreuung
  nennt Linienbreite und Lebensdauer oft im Abstract).
### A10 (OpenAlex-Suche: Fe-57 Linienbreite)
- Erwartung notiert 2026-10-05 08:28:33 CEST: Mindestens ein Abstract nennt fuer das 14,4-keV-Niveau eine natuerliche Breite ~4,7 neV und/oder Lebensdauer ~141 ns (Halbwertszeit ~98 ns). Damit Gamma/E ~ 3,2e-13 [M].
- Ausgang A10 (08:28:40): leer fuer die Frage (4 Treffer ohne Zahl). TS0 bleibt bei Lehrbuchwerten [L]. Kein weiterer
  Abruf nur fuer die Kontrolle; falls der Pound/Rebka-Text (A12) die Linienbreite nennt, nehme ich sie von dort.
### A11 (WebSearch: Compton-Koinzidenzen, Energieerhaltung je Ereignis)
- Erwartung notiert 2026-10-05 08:29:02 CEST: Nur historische Versuche (Bothe/Geiger 1925, Compton/Simon 1925, Hofstadter/McIntyre 1950) mit Zeit- bzw. Richtungskoinzidenz, ohne Zahl fuer einen Energieanteil. Die moderne 'Compton coincidence technique' setzt die Energieerhaltung zur Eichung voraus und prueft sie nicht.
- Ausgang A11 (Suche 08:29, Werkzeugtext, keine Kopie): bestaetigt. Nur historische Darstellungen (Wikipedia, Bonolis
  2011 arXiv:1106.1365, Nobelvortrag Bothe). Werkzeugtext: Koinzidenz "within a time interval of 1 ms"; nicht an der
  Primaerquelle gelesen, daher nur als Hinweis. Eine Zahl fuer einen Energieanteil gibt es nach Recherchestand nicht.
  - [ES] Was Compton-Koinzidenzen sehen: dass zu jedem gestreuten Quant ein Rueckstosselektron gehoert (Gleichzeitigkeit,
    Richtung). Das ist wie g2 eine Pruefung ueber der Schwelle; einen unsichtbaren Energieanteil sehen sie nicht.
### A12 (Pound/Rebka 1960 Volltext, Sammlung K. McDonald, Princeton)
- Erwartung notiert 2026-10-05 08:29:49 CEST: Datei existiert unter physics.princeton.edu/~mcdonald/examples/GR/pound_prl_4_337_60.pdf (geraten, kann 404 sein). Inhalt: Verschiebung je Lage (Quelle unten / oben) mit grossem Eigenversatz Quelle-Absorber (~1e-14, Temperatur), gewertet wird die Differenz; Linienbreite im Versuch ~1e-12 relativ. Ein richtungsunabhaengiger Verlust ueber 22,5 m faellt in der Differenz heraus.
- Ausgang A12 (08:29:53): leer (HTTP 000, geratene Adresse). Zaehlt mit. Kein zweiter Versuch: Die Differenzmessung
  steht indirekt im Pound/Snider-Abstract (Sollwert 2gh/c^2 = Summe der Betraege beider Lagen = Differenz oben minus
  unten) [S Abstract, ES]. Eigenversatz und Linienbreite bleiben [L].
### A13 (arxiv.org/abs/0906.3476)
- Erwartung notiert 2026-10-05 08:30:18 CEST: Das ist die Arbeit mit dem Laborvorschlag 'Hubble-Rate als Frequenzdrift proportional zur Flugzeit, ~1e-18 /s', Theorie, keine Messung.
- Ausgang A13 (08:30:23): Erwartung verletzt (klein). 0906.3476 ist kein Laborvorschlag fuer die Hubble-Drift, sondern
  Terra, Grosche, Predehl, Holzwarth, Legero u. a. 2009: 146 km Faser, "relative frequency uncertainty below 1E-19",
  Faser-Interferometer "to detect and compensate phase noise" [S Abstract]. Also wieder eine kompensierte Strecke
  (blind fuer reziproken Verlust [ES]); falls sie es saehe: 1e-19 / 1,46e5 m ~ 6,8e-25 /m [M].
  - Korrektur: Der Satz "Hubble-Rate im Labor als Frequenzdrift ~1e-18 /s" aus A5 hat keine gefundene Quelle. Er kommt
    in die Negativliste. Meine Schreibtischzahl H0 ~ 2,3e-18 /s bleibt [M].
### A14 (WebSearch: Raumsonden-Doppler gegen Laufzeit als Test fuer Frequenzverlust je Strecke)
- Erwartung notiert 2026-10-05 08:32:11 CEST: Keine Arbeit begrenzt einen Frequenzverlust je Strecke direkt mit Raumsonden. Treffer zu Pioneer-Anomalie ('clock acceleration' ~ H0) und zu kosmologischer Expansion im Sonnensystem (Carrera/Giulini). Die Pioneer-Deutung als muedes Licht passt in der Groessenordnung nicht (Schreibtisch: Hubble-Rate gibt H0 v ~ 3e-14 m/s^2, Pioneer 8,7e-10 m/s^2).
- Ausgang A14 (Suche 08:32, Werkzeugtext): bestaetigt. Keine Arbeit, die einen Frequenzverlust je Strecke mit
  Raumsonden begrenzt. Treffer: NASA/JPL-Lehrseiten, Living Review lrr-2006-1 (Doppler-Verfolgung als GW-Detektor),
  Randtexte. Nach diesem (einen) Suchlauf kein Doppel fuer den Kartenvorschlag.
### A15 (OpenAlex-Suche: PQED gegen Kryoradiometer)
- Erwartung notiert 2026-10-05 08:32:43 CEST: Gegensweep-Abruf. Vorhersagbare-Quanteneffizienz-Detektoren (PQED) zaehlen Elektronen je Photon, das Kryoradiometer misst deponierte Leistung elektrisch. Abstracts nennen Uebereinstimmung von vorhergesagter und gemessener Empfindlichkeit auf ~1e-4 (100 ppm) oder etwas besser. Das waere eine absolut geeichte Nachweis-Schranke fuer Lesart L-b bei sichtbarem Licht, |eps| < ~1e-4.
- Ausgang A15 (08:32:47): ERWARTUNGSVERSTOSS (mittel, positiv): Es gibt eine absolut geeichte Nachweis-Schranke, die in
  der Karte nicht vorkam. PQED: Empfindlichkeit laut Abstract nur durch h, c, e und die Vakuumwellenlaenge bestimmt
  [Nachtrag 08:41: Zitat umschrieben (Urheberrecht)]; Vergleich mit dem Kryoradiometer bei 476, 532 und 760 nm: vorhergesagte und gemessene externe
  Quantendefizienz stimmen "within the expanded uncertainty of 60 ppm to 180 ppm" (Dissertation 2014, OpenAlex
  W2527677910, Autor nicht im Abruf) [S Abstract]. CIE 2019 (doi 10.25039/x46.2019.op58): Validierung gegen das
  Kryoradiometer "with standard uncertainty below 100 ppm" [S Abstract]. Metrologia 2022 (doi 10.1088/1681-7575/ac938c):
  Langzeitstabilitaet innerhalb 150 ppm ueber 10 Jahre [S Abstract].
  - [ES] Was das misst: Elektronen je Photon (PQED) gegen elektrisch geeichte Waerme (Radiometer), umgerechnet mit
    h c/lambda. Ein Anteil eps, der im Radiometer nicht ankommt (Lesart L-b), oder ein Zusatz, der ankommt, aber nicht in
    h nu steckt (L-a), verschoebe das Verhaeltnis um eps. Also |eps| < ~1e-4 fuer sichtbare Photonen (1,6 bis 2,6 eV).
    Teile, die im Radiometer UND in der Diode gar nichts abgeben und auch nicht in h nu stecken, sieht es nicht.
  - Damit ist TES nicht die einzige Nachweis-Messart fuer sichtbares Licht; die absolute Eichung liegt beim Radiometer.

## 3. Budget erschoepft (15 von 15) um 08:32:47. Ab hier nur noch lokale Arbeit.

## 4. Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- G1 [geprueft, Schreibtisch]: "Ein Photon, das unterwegs Teile abgibt, verliert Frequenz" (Zusatz der Leitung). Gilt
  nur, wenn fuer den Rest weiter E = h nu gilt. Legt der Sender die Frequenz fest und tragen die Teile nur Energie, dann
  zeigt sich der Verlust als Fehlbetrag beim Nachweis (L-b), nicht als Rotverschiebung. Dann sind PQED und Moessbauer
  die Laufstrecken-Schranken fuer m-Strecken, und SN sieht nichts. Folge: beide Lesarten getrennt fuehren.
- G2 [geprueft, A4]: "Faserstrecken liefern die Frequenz am Fernende unabhaengig." Nein: Rundweg-Regelung. Blind fuer
  reziproken Verlust [S Volltext + M].
- G3 [geprueft, A8]: "TES-Spitzen bei n h nu sind ein Befund." Nein: Eichnormal fuer TES-Kalorimeter [S Abstract].
- G4 [teilweise geprueft, A1]: "Pound/Rebka misst den Verlust ueber 22,5 m." Sollwert 2gh/c^2 = Differenz beider Lagen,
  ein richtungsunabhaengiger Verlust faellt heraus [S Abstract + ES]. Text 1960 nicht gelesen (A12 leer).
- G5 [benannt]: "Gamma/E ist die Moessbauer-Schranke." Isomerieverschiebungen (bis ~1 mm/s, ~3e-12 [L]) werden relativ
  zu einer Referenz angegeben. Eine fuer alle Quellen gleiche Verschiebung verschwaende in der Referenz. Die Schranke
  Gamma/E gilt nur fuer chemisch gleiche Quelle und Absorber bei gleicher Temperatur. Nicht an Quelle geprueft.
- G6 [benannt]: "eps ist fuer alle Photonenenergien gleich." Die Schranken stammen von 0,8 eV bis MeV und lassen sich
  nur unter dieser Annahme zusammenlegen.
- G7 [benannt]: "SN-Zeitdehnung sieht jeden Verlust unterwegs." Nur einen Verlust OHNE Zeitstreckung. Ein Mechanismus,
  der Frequenz senkt UND Abstaende streckt, ist von Ausdehnung per SN nicht zu trennen.
- G8 [benannt]: "Vakuum und Glas verhalten sich gleich." SN gilt fuer intergalaktischen Raum; fuer Glas (Faser) fand ich
  keine Schranke, weil die Faserstrecken blind sind.

## 5. Kalibrierung
- (a) gemessen [S]: Rainville (-1,4 +- 4,4)e-7; DES b = 1,003 +- 0,005 +- 0,010; Pound/Snider 0,9990 +- 0,0076 von
  4,905e-15; Droste 3e-19 (1840 km), Lisdat 5e-17 (1415 km), Terra < 1e-19 (146 km); TES 67 meV bei 0,8 eV, 1,8 eV bei
  1,5 keV; PQED 60 bis 180 ppm (k=2); Heeck > 3 Jahre.
- (b) verdichtet [M, ES]: Lesarten L-a, L-b, L-c; Blindheit kompensierter Strecken; kappa < ~1,5e-28 /m aus DES;
  TES-Zirkel; Hubble-Massstab 7,6e-27 /m.
- (c) gewachsene Gewissheit ohne neue Evidenz: "Unterwegs ist die Luecke, dort liegt Finns Fenster." Gestuetzt nur durch
  meine Ableitung aus dem beschriebenen Regelprinzip (A4) und Schreibtischzahlen. Keine Quelle sagt "Faserstrecken sind
  blind fuer muedes Licht". Warnzeichen: Meine Sicherheit stieg ab 08:25, waehrend die Frage in L-a/L-b/L-c zerfiel.
- Abschnitt 4/5 geschrieben 2026-10-05 08:35:53 CEST. Dossier ab jetzt.

## 6. Rueckwaertslesen des Dossiers (Gegenlesen in beide Richtungen)
- Gefunden und berichtigt: (1) halber Satz "Bruchteil 1e-6 auf 3 Lichtjahre" ohne Rechnung (gestrichen, Selbstanzeige 6);
  (2) Ersatzwert "4e-12 je Lichtjahr" falsch, richtig 1,4e-12 [M]; (3) Rainville-Zeile: "Neutroneneinfang" und "MeV"
  stehen nicht im Abstract -> als [P] bzw. [L] markiert; (4) "194 THz" bei Droste nicht im Abstract -> [L];
  (5) Zitate ueber 15 Woerter bzw. mehrere je Quelle (Lisdat, TASC 2021, PQED, Sanejouand, Droste) umschrieben;
  (6) "Einfach gesagt" letzter Satz war zu stark ("fast ausgeschlossen") gegen das Fenster aus TS1 -> abgeschwaecht.
- Rueckwaertslesen abgeschlossen 2026-10-05 08:41:46 CEST.
