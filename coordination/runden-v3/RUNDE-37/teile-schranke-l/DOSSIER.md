# TEILE-SCHRANKE-L: Dossier. Wie viel Energie kann ein Photon hoechstens in unsichtbaren Teilen tragen oder unterwegs verlieren? (Runde 47, Literatur, datennah)

- feldforscher fuer die Leitung claude-primary. Grundlage: KARTE.md (bindend, TS0 bis TS4 und ihre Bedeutung
  unveraendert). Protokoll mit Erwartung vor jedem Abruf, Ausgaengen, Gegensweep und Kalibrierung: ARBEITSFELD.md.
  Abrufliste: ABRUFE.md. Kopien mit Abrufzeit: quellen/.
- Kennzeichen: [S] Fachquelle (an Abstract oder Volltext gelesen, Stelle genannt); [L] Lehrbuch/Gedaechtnis; [M] eigene
  Rechnung von Hand, nicht gegengelesen; [P] Projektbefund; [H] Hypothese; [ES] eigener Schluss. Messdaten aus
  Fachquellen sind [S], keine eigene Messung. **Literatur und Schreibtisch, keine Messdatenbestaetigung.**

## 1. Zeiten und Abrufzahl

- Start 2026-10-05 08:16:17 CEST, Dossier ab 08:36:40 CEST (date). Endzeit steht in Abschnitt 9 (date).
- **15 von 15 Netzabrufen verbraucht** (letzter um 08:32:47). Davon leer: A9 (IAEA, Cloudflare-Sperre), A10 (OpenAlex,
  keine Zahl), A12 (geratene Adresse, keine Verbindung). Vier Abrufe waren Websuchen (A5, A6, A11, A14); deren
  Werkzeugtexte nutze ich nur als Wegweiser, Zahlen daraus stehen in der Negativliste.

## 2. Ergebnis zuerst

1. **Beim Nachweis kommt ein Photon praktisch vollstaendig an.** Fehlt Energie im Detektor, dann hoechstens
   ~1e-4 bei sichtbarem Licht (PQED gegen Kryoradiometer, 60 bis 180 ppm) [S, Deutung ES]. Energie ausserhalb von
   h nu ist bei Gammas (MeV [L]) auf (-1,4 +- 4,4)e-7 begrenzt (Rainville 2005) [S]. Bei 14,4 keV (Fe-57) liegt die Grenze bei ~3e-13,
   das ist nur [L, M] und hat einen Vorbehalt.
2. **Unterwegs liefert das Labor KEINE Schranke.** Glasfaser-Uhrenvergleiche regeln ueber den Rundweg nach und gleichen
   einen Verlust, der in beide Richtungen gleich wirkt, von selbst aus (Lisdat 2016, Haupttext [S]; Folgerung [M]).
   Pound/Rebka werten die Differenz oben minus unten aus; dort faellt der Verlust ebenfalls heraus [S, ES].
3. **Die schaerfste Schranke unterwegs ist kosmologisch:** Die Zeitdehnung von 1504 Supernovae, b = 1,003 +- 0,005
   (stat) +- 0,010 (sys) [S], laesst fuer einen Verlust ohne Zeitdehnung hoechstens ~2 % der Rotverschiebung bis
   z ~ 1,2 zu. Das sind bei konstantem Verlust ~1,5e-28 je Meter [M]. Auch eine ideale Laborstrecke (3e-19 auf
   1840 km = 1,6e-25 /m) waere rund 1000-mal schwaecher [M].
4. **TES-Spektren pruefen "E = n h nu" nicht, sie setzen es voraus.** Optische Photonen dienen zur Eichung von
   TES-Kalorimetern [S]. TES begrenzt nur die Streuung von Photon zu Photon (relative Breite 0,08 bis 0,19 bei
   0,8 eV, 1,2e-3 bei 1,5 keV) [S, M].
5. **Urteile:** TS0 eingetroffen (nur Schreibtischkontrolle), **TS1 verfehlt**, TS2 teilweise, TS3 und TS4
   eingetroffen. Nach Karte heisst TS1 verfehlt: Die Laufstrecken-Schranken sind schwaecher als gedacht, dort ist ein
   Fenster fuer Finns Bild. Das Fenster ist aber schmal (Abschnitt 6).

## 3. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

| Nr | Erwartet | Gefunden | Fundstelle |
|---|---|---|---|
| V1 | Karte (TS1, Zusatz der Leitung): Frequenzvergleiche ueber Glasfaser sehen einen Verlust unterwegs und geben die schaerfste Schranke | Sie sind blind dafuer. Die Strecke wird ueber den Rundweg geregelt: Ein Teil des Lichts laeuft am Fernende durch dieselbe Faser zurueck, das Rundweg-Phasenrauschen wird am Sender gemessen und "actively cancelled". Ein Verlust je Strecke ist in beide Richtungen gleich; der Regler gleicht ihn aus wie eine Laengenaenderung der Faser [M, vorab ableitbar aus dem Prinzip]. Mein Verdacht stand um 08:22 im ARBEITSFELD, belegt ist nur das Regelprinzip, nicht die Blindheit selbst | Lisdat u. a. 2016, Nat. Commun. 7, 12443, Haupttext [S]; Droste u. a. 2013 ("single-span stabilization") und Terra u. a. 2009 ("detect and compensate phase noise") [S Abstract] |
| V2 | Karte (TS2): TES-Spektren zeigen, ob die Energie bei n h nu liegt | Umgekehrt: "Pulses of narrow line-width optical photons can be used to calibrate" TES-Kalorimeter; die Photonenzahl ist bis etwa 300 je Puls aufgeloest. n h nu ist das Eichnormal. Ein gleichmaessiges eps verschwindet in der Eichung | IEEE TASC 2021, doi 10.1109/tasc.2021.3053506 [S Abstract] |
| V3 | Karte (TS1): Laufstrecken-Schranke < 1e-15 relativ ist scharf | In der natuerlichen Einheit (je Meter) sind alle Laborstrecken schwaecher als die Hubble-Rate selbst: H0/c ~ 7,6e-27 /m; Droste nominal 1,6e-25 /m. Muedes Licht in voller Hubble-Staerke gaebe auf 1000 km nur 7,6e-21. Die Laborstrecken koennen den Fall gar nicht erreichen [M, vorab ableitbar] | ARBEITSFELD 1.2 und Ausgang A2 |
| V4 | Karte: Nachweis-Schranken nur aus Moessbauer, TES, Compton, Rainville | Es gibt eine absolut geeichte Schranke fuer sichtbares Licht: PQED (Elektronen je Photon, Empfindlichkeit aus h, c, e, lambda) gegen Kryoradiometer (Waerme, elektrisch geeicht), Uebereinstimmung "within the expanded uncertainty of 60 ppm to 180 ppm" bei 476, 532, 760 nm | Dissertation 2014, OpenAlex W2527677910 [S Abstract]; CIE 2019, doi 10.25039/x46.2019.op58 [S Abstract] |
| V5 | Ich (A6): Keine neuere Arbeit stellt die Zeitdehnung in Frage | Lee 2026 (EPJC) schreibt, Quasar-Analysen "frequently yield null results", GRBs streuen stark; Sanejouand (IJMPD) vertritt ein Muedes-Licht-Modell mit Photonlebensdauer "one third of the Hubble time". Moderator ist die Quellenart, nicht der Lichtweg [ES]; die SN-Schranke bleibt | arXiv:2603.00427 [S Abstract]; arXiv:2005.07931 [S Abstract] |
| V6 | Ich: Pound/Rebka liefern eine Schranke ueber 22,5 m | Der Sollwert ist 2gh/c^2 = 4,905e-15, also die Differenz beider Lagen. Ein richtungsunabhaengiger Verlust faellt heraus [ES]; der Eigenversatz Quelle/Absorber bleibt unbekannt, weil A12 leer blieb | Pound/Snider 1965, PR 140, B788 [S Abstract] |
| V7 | klein | Droste: Versatz-Unsicherheit 3e-19 (nicht 4e-19; 4e-19 ist die Allan-Abweichung nach 100 s). arXiv:0906.3476 ist Terra u. a. 2009, kein Laborvorschlag zur "Hubble-Drift" (dessen Quelle bleibt unbekannt). INSPIRE fuehrt Rainville, Droste, Lisdat nicht | A2, A7, A13 |

## 4. Tabelle der Schranken

Lesarten [ES]: **L-a** Energie, die nicht in h nu steckt (E_gesamt = h nu + E_unsichtbar). **L-b** h nu stimmt, aber der
Detektor nimmt nur (1 - eps) h nu auf, der Rest fliegt durch. **L-c** Verlust unterwegs, nu sinkt mit der Strecke
(kappa = -d ln nu/dL, Einheit 1/m). Natuerliche Einheit: relativ je Ereignis (Nachweis) bzw. je Meter (unterwegs).
Ich vergleiche nur Zeilen derselben Groesse.

| Messart | Regime | Groesse | eps | Strecke bzw. Energie | Quelle mit Stelle | sieht die Messart Teile unter der Schwelle? |
|---|---|---|---|---|---|---|
| Moessbauer-Linienbreite Fe-57 | Nachweis | L-b: der Absorber braucht E innerhalb Gamma | < ~3,2e-13 je Ereignis [M aus L: T1/2 ~98 ns, Gamma ~4,6e-9 eV] | 14,4 keV | Lehrbuchwerte [L]; Primaerquelle nicht erreicht (A9, A10 leer) | nur Teile, die der Absorber nicht mit aufnimmt; nur bei chemisch gleicher Quelle und gleichem Absorber, sonst steckt eps in der Isomerieverschiebung (bis ~3e-12 [L]) |
| Rainville u. a. 2005 | Nachweis (Energiebilanz der Emission) | L-a: Delta m c^2 gegen Summe der h c/lambda der Kaskade | 1 - Delta m c^2/E = (-1,4 +- 4,4)e-7, also \|eps\| < ~1e-6 (2 sigma) [M] je Einfang | Gammas der Kernbindungsenergie von Si- und S-Isotopen [S]; MeV-Bereich [L], Neutroneneinfang [P] | Nature 438, 1096, Abstract [S] | ja fuer L-a; nein fuer L-b (E kommt aus der Beugung, nicht aus deponierter Energie) |
| PQED gegen Kryoradiometer | Nachweis | L-b und L-a: Elektronen je Photon gegen deponierte Waerme, Umrechnung h c/lambda | 6e-5 bis 1,8e-4 (erweiterte Unsicherheit) je Photon | 1,6 bis 2,6 eV (476, 532, 760 nm) | Diss. 2014 OpenAlex W2527677910 Abstract; CIE 2019 ("below 100 ppm") [S] | ja fuer Teile, die nicht als Waerme ankommen, und fuer Zusatzenergie ausserhalb h nu; nein fuer Teile ohne Energie |
| TES optisch | Nachweis | Streuung von eps je Photon; Nebenspitzen bei Bruchteilen | relative Breite 0,084 (67 meV), typisch 0,19 (150 meV), 0,14 (0,113 eV) FWHM [M aus S] | 0,8 eV | SuST 2022 doi 10.1088/1361-6668/ac7e7b; APL 2013 doi 10.1063/1.4815922 [S Abstract] | nur Streuung, Bruchteil-Spitzen und Abhaengigkeit von nu; ein gleichmaessiges eps steckt in der Eichung (V2) |
| TES Roentgen (weich) | Nachweis | wie oben | 1,2e-3 FWHM relativ [M aus S] | 1,5 keV | Photonics 12, 609 (2025) [S Abstract] | wie oben |
| Compton-Koinzidenzen | Nachweis | Gleichzeitigkeit Streuquant und Rueckstosselektron | keine Zahl fuer eps gefunden | Roentgen, 1925 | nur Sekundaerdarstellungen (A11) | nein: prueft wie g2 nur ueber der Schwelle |
| Strahlteiler g2 (Vorkarte) | Nachweis | Doppelklicks | g2 = 7,5e-5, kein eps | optisch | LICHT-TEILE-L [P] | nein (Anlass dieser Karte) |
| Pound/Snider 1965 | unterwegs | Differenz Quelle oben gegen unten | (0,9990 +- 0,0076) von 4,905e-15, Systematik 0,010; Gravitationsmessung, keine eps-Schranke | 22,5 m (75 ft), 14,4 keV | PR 140, B788, Abstract [S] | nein fuer richtungsunabhaengigen Verlust (faellt in der Differenz heraus) [ES]; ja fuer richtungsabhaengigen |
| Faser Droste 2013 | unterwegs | gesendet gegen uebertragen, Rundweg-geregelt | 3e-19; nominal 1,6e-25 /m [M], traegt aber nicht | 1840 km, ~194 THz [L] | PRL 111, 110801, Abstract [S] | nein fuer reziproken Verlust (V1); nur nicht-reziproke Effekte |
| Faser Lisdat 2016 | unterwegs | Sr gegen Sr ueber zwei geregelte Strecken | 5e-17; nominal 3,5e-23 /m [M] | 1415 km | Nat. Commun. 7, 12443, Abstract und Haupttext [S] | nein (V1) |
| Faser Terra 2009 | unterwegs | wie Droste | < 1e-19; nominal 6,8e-25 /m [M] | 146 km | arXiv:0906.3476, Abstract [S] | nein (V1) |
| SN-Zeitdehnung DES | unterwegs (kosmologisch) | Anteil f von ln(1+z) ohne Zeitdehnung, b = 1 - f | b = 1,003 +- 0,011 [M aus S] -> f < ~0,02 (95 %); bei konstantem kappa: kappa < ~0,02 H0/c ~ 1,5e-28 /m [M, H0 = 70 km/s/Mpc L] | z 0,1 bis 1,2 (Gpc), optisch | White u. a. 2024, MNRAS 533, 3365, Abstract [S] | ja fuer Verlust ohne Zeitstreckung im intergalaktischen Raum; nein fuer Verlust mit Zeitstreckung (G7) oder nur in Materie (G8) |
| SN-Spektralalterung | unterwegs | Alterungsrate 1/(1+z) | keine Zahl im Abstract; schliesst "Zwicky's 'tired light'" aus | 13 SNe, hohe z | Blondin u. a. 2008, ApJ 682, 724 [S Abstract] | wie DES |
| CMB-Spektrum, Photonzerfall | unterwegs | Verschwinden ganzer Photonen (Anzahl, nicht Anteil) | Lebensdauer > 3 Jahre im Ruhesystem, Mikrowellenphotonen ~1e15-fach gedehnt | CMB | Heeck 2013, PRL 111, 021801 [S Abstract] | sieht Zerfall, keinen Teilverlust; setzt Photonmasse an der Grenze voraus |
| Massstab, keine Messung | unterwegs | Hubble-Rate | H0/c ~ 7,6e-27 /m, H0 ~ 2,3e-18 /s [M, vorab ableitbar] | - | [L] | - |

### 4.1 Regime und Moderatoren (Feldregel 1)
- **Nachweis gegen unterwegs** (Auftrag). Innerhalb des Nachweises trennt die **Messgroesse**: Wellenlaenge gegen
  Energiebilanz (L-a, Rainville), deponierte Energie gegen h nu (L-b, PQED, Moessbauer), Streuung (TES).
- **Eichung als Moderator:** Mit Photonen geeichte Detektoren (TES, und nach [L] auch Ge-Detektoren) sehen kein
  gleichmaessiges eps; absolut geeichte (Kryoradiometer) sehen es.
- **Unterwegs: reziprok gegen nicht-reziprok.** Alle gefundenen Praezisionsstrecken nutzen die Reziprozitaet (Rundweg,
  Zweiwege, Differenz oben/unten). Ein Verlust je Strecke ist reziprok und faellt deshalb heraus [ES].
- **Quellenart** in der Zeitdehnungs-Literatur: diskrete Ereignisse (SN Ia) zeigen (1+z); Quasare mal ja (Lewis/Brewer
  2023), mal "null results" (laut Lee 2026). Ein Wegeffekt haengt nicht an der Quelle, also klaert die SN-Messung den
  Wegeffekt unabhaengig vom Quasarstreit [ES].
- **Photonenenergie:** Die Schranken stammen von 0,8 eV bis MeV (G6). Ein eps, das von der Energie abhaengt, laesst sich
  nicht von einer Zeile auf die andere uebertragen.

### 4.2 Unterscheidungspunkte (Feldregel 2): Wo waere ein Teile-Haufen-Photon am ehesten sichtbar?
| Paar | wo sie messbar auseinanderlaufen | Daten? |
|---|---|---|
| Quant gegen Haufen mit unsichtbarem Rest (L-b) | deponierte Energie gegen h nu, absolut geeicht | ja: PQED ~1e-4 (sichtbar); Moessbauer ~3e-13 (14,4 keV, Vorbehalt) |
| Quant gegen Haufen mit Zusatzenergie (L-a) | Energiebilanz gegen Wellenlaenge | ja: Rainville ~1e-6 (MeV) |
| Ausdehnung gegen Verlust unterwegs (L-c) | Zeitdehnung bei grossen Wegen | ja: DES, f < ~0,02 bis z ~ 1,2 |
| Verlust unterwegs im Labor | Strecke L, bei der kappa L die Messgenauigkeit erreicht: bei Hubble-Rate und 1e-19 sind das ~1,3e7 m; bei 1e-15 ~1,3e11 m (~1 AE), und nur EINWEG oder Doppler gegen Laufzeit [M] | keine Labordaten (alle Strecken reziprok geregelt); Sonnensystem: Kartenvorschlag |
| Verlust, der auch Zeit streckt, gegen Ausdehnung | nicht per Zeitdehnung; nur ueber Flaechenhelligkeit (Tolman) oder Spektralform | nicht abgerufen |
| Energieabhaengiger Verlust | Rotverschiebung derselben Quelle in verschiedenen Baendern (Radio, optisch, Roentgen) | nicht abgerufen; Hinweis [L]: Linienvergleiche fuer die Feinstrukturkonstante pruefen genau das |
| Einzelphotonen | TES: Bruchteil-Spitzen, Streuung | Breiten ja, Bruchteil-Spitzen in Abstracts nicht erwaehnt |

## 5. Urteile TS0 bis TS4 (Kartenwortlaut)

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| TS0 | Kontrolle: Moessbauer Fe-57 gibt beim Nachweis eps < ~3e-13 (Gamma/E) | 90 % | **eingetroffen als Schreibtischkontrolle**, an keiner Primaerquelle gelesen | Gamma = hbar ln2/T1/2 ~ 4,6e-9 eV bei T1/2 ~ 98 ns und 14,4 keV [L], Gamma/E ~ 3,2e-13 [M, vorab ableitbar]. A9 und A10 leer. Vorbehalt G5: gilt nur fuer L-b und nur bei gleicher Quelle und gleichem Absorber |
| TS1 | Schaerfste Schranke unterwegs ist ein Frequenzvergleich ueber Glasfaser oder Freistrahl, < 1e-15 ueber die Strecke | 70 % | **verfehlt** | (1) Die Faserstrecken sind Rundweg-geregelt (Lisdat 2016, Haupttext [S]) und gleichen einen reziproken Verlust aus [M]; sie liefern fuer diese Groesse keine Schranke. (2) Die schaerfste gefundene Schranke ist die SN-Zeitdehnung (DES: f < ~0,02, kappa < ~1,5e-28 /m [M aus S]). (3) Nominal waere Droste mit 3e-19 zwar "< 1e-15", je Meter (1,6e-25 /m) aber ~1000-mal schwaecher als DES und ~20-mal schwaecher als die Hubble-Rate [M]. Freistrahl: nicht abgerufen; Zweiwege-Verfahren heben reziproke Effekte in der Differenz ebenfalls auf [ES] |
| TS2 | TES: Spitzen bei n h nu ohne Bruchteil-Spitzen; eps-Schranke 1e-3 bis 1e-1, die schwaechste der Messarten | 60 % | **teilweise** | Spitzen bis ~300 Photonen je Puls, Linienform laut Abstract einfach gaussisch (TASC 2021) [S], aber n h nu ist dort Eichnormal (V2). Bruchteil-Spitzen: Abstracts schweigen, **nicht entscheidbar**. Breite 0,084 bis 0,19 (0,8 eV) bzw. 1,2e-3 (1,5 keV) [M aus S] liegt im Bereich, begrenzt aber nur die Streuung von eps, nicht ein gleichmaessiges eps. "Schwaechste": unter den Messarten mit Zahl ja; Compton-Koinzidenzen haben gar keine Zahl |
| TS3 | SN-Zeitdehnung besser als 2 % gemessen, schliesst muedes Licht als alleinige Ursache aus | 85 % | **eingetroffen** | DES: b = 1,003 +- 0,005 (stat) +- 0,010 (sys), kombiniert 1,1 % [M]; "ruling out any non-time-dilating cosmological models at very high significance" [S Abstract]. Blondin 2008 schliesst "Zwicky's 'tired light'" per Spektralalterung aus [S Abstract]. 24-Monats-Suche (A6, A7): keine gegenteilige Messung; Lee 2026 ist Theorie zum Quasarstreit |
| TS4 | Rainville 2005 begrenzen fehlende Energie bei der Gamma-Emission auf ~1e-7 bis 1e-6 | 70 % | **eingetroffen** | 1 - Delta m c^2/E = (-1,4 +- 4,4) x 10^-7, Si und S, E aus Gamma-Wellenlaengen (Nature 438, 1096, Abstract) [S]. Gilt fuer L-a |

**Bedeutung nach Karte:** TS1 verfehlt: "Die Laufstrecken-Schranken sind schwaecher als gedacht. Das ist ein Fenster
fuer Finns Bild und eine Kandidatin fuer einen neuen Test." Der Vorab-Satz fuer den Fall, dass alle eintreffen
("unterwegs hoechstens ~1e-15 je Strecke"), gilt damit nicht. Der Nachweis-Teil gilt in abgestufter Form: ~3e-13 nur bei
14,4 keV und nur [L]; belegt sind ~1e-6 (L-a, MeV) und ~1e-4 (L-b, sichtbar).

## 6. Bedeutung fuer Finns Bild "Photon als Teilansammlung" [H]

- **Beim Ankommen:** Wenn ein Photon ein Haufen ist, kommt der Haufen praktisch ganz an. Sichtbares Licht verliert
  hoechstens ~1e-4 seiner Energie an Teile, die der Detektor nicht spuert [ES auf S]. Bei Gammas steckt hoechstens
  ~1e-6 der Energie ausserhalb von h nu [ES auf S].
- **Unterwegs im freien Raum:** Ein Haufen, der Teile abgibt und dadurch roeter wird, darf hoechstens ~2 % der
  gemessenen kosmischen Rotverschiebung erklaeren (bei konstantem Verlust ~1,5e-28 je Meter, ~~also einen Bruchteil
  1e-6 auf 3 Lichtjahre~~ [gestrichen, siehe Selbstanzeige 6], also ~1,4e-12 je Lichtjahr) [M aus S].
- **Wo das Fenster wirklich ist [ES]:**
  1. Verlust in Materie (Glas, Luft): Dafuer fand ich keine Schranke, weil die Faserstrecken blind sind (G8).
  2. Verlust, der zugleich die Zeitabstaende streckt: Den trennt die SN-Messung nicht von der Ausdehnung (G7).
  3. Teile, die weder Energie noch Impuls tragen: Die sieht keine Messart (Beispiel der Leitung).
  4. Ein Verlust, der von der Photonenenergie abhaengt: Die Zeilen der Tabelle lassen sich nicht uebertragen (G6).
- **Mit LICHT-TEILE-L zusammen:** Die Lesart "Sammelschwingung, die Teile bleiben am Ort" (Eis-Licht) bleibt
  unberuehrt, denn dort geht nichts verloren. Die Lesart "mitfliegender Haufen, der Teile abgibt" ist jetzt auch
  unterhalb der Nachweisschwelle begrenzt, beim Nachweis eng, unterwegs im Labor gar nicht, kosmisch auf Prozentniveau.

## 7. Kartenvorschlag (hoechstens einer)

**DOPPLER-LAUFZEIT-L (Literatur, datennah):** Begrenzen Raumsondendaten einen Frequenzverlust je Strecke auf dem
Niveau der Hubble-Rate? Muedes Licht aendert die Frequenz, aber nicht die Laufzeit. Zweiwege-Doppler (Frequenz) und
Entfernungsmessung (Laufzeit) muessten dann auseinanderlaufen.
- **Vorab ableitbar [M]:** Der Zweiwege-Doppler bekaeme eine scheinbare Zusatzgeschwindigkeit kappa c D. Bei
  Hubble-Rate sind das bei Saturn (D ~ 1,3e12 m) ~3 um/s, bei 1 AE ~0,3 um/s. Das ist der Unterscheidungspunkt zwischen
  Labor (blind, zu kurz) und Kosmologie (Gpc, G7).
- **Nicht ableitbar:** ob Bahnanpassungen (Cassini, Juno, BepiColombo) eine konstante Doppler-Verschiebung schlucken,
  welche Reste Doppler gegen Entfernung veroeffentlicht sind und ob es schon eine Schranke gibt.
- **Doppelpruefung:** eine Websuche (A14) ohne Treffer; Projekt-grep 08:34 (Pflicht-Ausschluesse): "tired light" bzw.
  "muedes Licht" nur in RUNDE-46 (diese Karte) und licht-teile-l; Cassini nur als Shapiro-Test (art-grenzen, gamma-netz-l).
- Keine Rechnung auf fremden Rechnern noetig; reine Literatur plus Groessenabschaetzung.

## 8. Negativliste (nicht behaupten)

1. "Glasfaser-Uhrenvergleiche begrenzen den Verlust unterwegs auf 3e-19 bzw. 5e-17." Sie sind dafuer blind (V1).
2. "TES zeigt, dass ein Photon genau n h nu ablegt." Das ist die Eichannahme (V2).
3. "Pound/Rebka begrenzen einen Verlust ueber 22,5 m auf ~4e-17." Der faellt in der Differenz heraus (V6).
4. "Compton-Koinzidenzen begrenzen eps." Keine Zahl gefunden; das "1-ms-Fenster" stammt nur aus dem Werkzeugtext (A11).
5. "Muedes Licht ist widerlegt." Belegt ist nur: als alleinige Ursache ausgeschlossen; ohne Zeitdehnung hoechstens ~2 %.
   Als Teilursache unter ~2 % und in Varianten mit Zeitstreckung nach Recherchestand nicht ausgeschlossen.
6. "Quasare zeigen keine Zeitdehnung." Strittig: Lewis/Brewer 2023 finden sie, Lee 2026 berichtet "null results".
7. "Lewis/Brewer: b = 1,28 +0,28 -0,29." Nur Werkzeugtext (A6), nicht an der Quelle gelesen.
8. "Ein Laborvorschlag misst die Hubble-Rate als Frequenzdrift ~1e-18 /s." Quelle nicht gefunden (A5, A13).
9. "Fe-57: Gamma = 4,7 neV an der Quelle gelesen." Nur [L].
10. Den Autor der PQED-Dissertation 2014 nicht nennen; er steht nicht im Abruf.
11. "Die Moessbauer-Schranke ist 3e-13 fuer jede Art unsichtbarer Teile." Nur L-b, nur gleiche Quelle/Absorber (G5).

## 9. Selbstanzeigen

1. Drei von 15 Abrufen leer (A9 Cloudflare, A10 ohne Zahl, A12 geratene Adresse). TS0 steht deshalb nur auf [L].
2. Die Blindheit der Faserstrecken (V1) ist meine Ableitung aus dem beschriebenen Regelprinzip, nicht eine Aussage der
   Quellen. Ein frischer Leser sollte Vorzeichen und Doppeldurchgang durch den Stellmodulator nachpruefen. Ich habe den
   Verdacht vor dem Abruf notiert (08:22) und dann nur eine bestaetigende Stelle gesucht. Das ist Bestaetigungssuche.
3. OpenAlex-Abstracts habe ich per jq aus dem Wortindex in Reihenfolge gelesen; Formeln koennen dabei verstuemmelt sein
   (z. B. "5 × 10(-17)").
4. Die Umrechnung f -> kappa nimmt kappa konstant, kleine z und H0 = 70 km/s/Mpc [L]. Die DES-Arbeit fittet b, nicht f;
   f = 1 - b ist meine Lesart, nicht ihre.
5. Websuchen A5, A6, A11, A14 sind Werkzeugtexte. Nur die Treffer aus A6 habe ich an der Quelle nachgelesen (A7).
6. In Abschnitt 6, zweiter Punkt, ist mir ein halber Satz ("Bruchteil 1e-6 auf 3 Lichtjahre") ohne Rechnung
   hineingeraten; er ist dort gestrichen. In der ersten Fassung dieser Selbstanzeige stand als Ersatz ~~ca. 4e-12 auf ein
   Lichtjahr~~, auch das war falsch gerechnet. Richtig: 1,5e-28 /m x 9,46e15 m ~ 1,4e-12 je Lichtjahr [M]. Beim
   Rueckwaertslesen gefunden.
7. Moessbauer "ueber Laufstrecken": ausser Pound/Rebka/Snider habe ich nicht gezielt gesucht (Budget); keine Messreihe
   mit veraenderter Laufstrecke gefunden heisst hier nur: nicht gesucht.
8. Rechnungen von Hand, nicht gegengelesen: Gamma/E, alle Werte je Meter, f < 0,02, H0/c, kappa c D.
9. Endzeit: siehe letzte Zeile.

## 10. Einfach gesagt

Wir haben gefragt, ob ein Lichtteilchen heimlich kleine Stuecke mit sich traegt oder unterwegs verliert. Beim Ankommen
fehlt praktisch nichts: Bei normalem Licht hoechstens ein Zehntausendstel der Energie, bei Gammastrahlen noch viel
weniger. Unterwegs koennen die besten Glasfaser-Vergleiche einen solchen Verlust gar nicht sehen, weil sie das Licht
hin und zurueck schicken und Aenderungen automatisch ausgleichen. Nur das Licht ferner Sternexplosionen zeigt, dass
hoechstens etwa zwei Prozent der kosmischen Rotfaerbung von "muedem Licht" kommen koennen. Ein Photon als Haeufchen,
das unterwegs Stueckchen abwirft, hat also nur noch wenig Platz (im Weltraum ein paar Prozent, in Glas oder Luft noch
gar nicht richtig geprueft), waehrend ein Photon als gemeinsame Welle vieler Teile, die am Ort bleiben, moeglich bleibt.

## Anhang A. Gegensweep (Feldregel 4), Kurzform; ausfuehrlich ARBEITSFELD Abschn. 4

- Geprueft: G1 (Teileabgabe senkt die Frequenz nur, wenn fuer den Rest E = h nu gilt; sonst Fehlbetrag beim Nachweis,
  Schreibtisch), G2 (Faserstrecken, A4), G3 (TES-Eichung, A8), G4 (Pound/Snider-Differenz, A1, teilweise).
- Benannt, nicht geprueft: G5 (Isomerieverschiebung relativ zur Referenz), G6 (eps energieabhaengig), G7 (Verlust mit
  Zeitstreckung), G8 (Vakuum gegen Glas).

## Anhang B. Kalibrierung

- (a) gemessen [S]: Zahlen der Tabelle in Abschnitt 4 mit Quelle.
- (b) verdichtet [M, ES]: Lesarten L-a/L-b/L-c; Blindheit reziprok geregelter Strecken; kappa < ~1,5e-28 /m;
  TES-Zirkel; Hubble-Massstab.
- (c) gewachsene Gewissheit ohne neue Evidenz: "Unterwegs ist die Luecke, dort liegt Finns Fenster." Die Sicherheit
  stieg ab 08:25, gestuetzt nur auf meine Ableitung aus einem Regelprinzip und auf Schreibtischzahlen. Keine Quelle sagt,
  dass Faserstrecken fuer muedes Licht blind sind. Warnzeichen nach Vorgabe.

## Anhang C. Offene Fragen

- Pound/Rebka 1960: Wie gross war der Eigenversatz Quelle/Absorber, und wurde er bei kurzem Abstand gemessen? (A12 leer.)
- Moessbauer mit chemisch gleicher Quelle und gleichem Absorber: Liegt die Resonanz bei v = 0 auf besser als Gamma?
- Gibt es eine Einweg-Frequenzmessung (ohne Rundweg-Regelung) ueber eine bekannte Strecke, z. B. in der Summe einer
  Zweiwege-Messung?
- Energieabhaengigkeit: Wie gut stimmen Rotverschiebungen derselben Quelle in Radio, optisch und Roentgen ueberein?
- Bruchteil-Spitzen in TES-Spektren: in Volltexten erwaehnt oder ausgeschlossen?
- Herkunft des Satzes "Hubble-Rate als Labor-Frequenzdrift ~1e-18 /s" (A5).

## Anhang D. Quellenliste (Abrufstand 2026-10-05; Kopien in quellen/)

- A1 INSPIRE 08:23:13 (quellen/A1-inspire-batch-20261005-082313.json):
  - White, R. M. T. u. a. (DES), "The Dark Energy Survey Supernova Program: slow supernovae show cosmological time
    dilation out to z ~ 1", MNRAS 533 (2024) 3365, arXiv:2406.05050 [S Abstract].
  - Blondin, S. u. a., "Time Dilation in Type Ia Supernova Spectra at High Redshift", ApJ 682 (2008) 724,
    arXiv:0804.3595 [S Abstract].
  - Pound, R. V., Snider, J. L., "Effect of Gravity on Gamma Radiation", Phys. Rev. 140 (1965) B788 [S Abstract].
  - Pound, R. V., Rebka, G. A., "Apparent Weight of Photons", PRL 4 (1960) 337 [S Titel, kein Abstract].
  - Heeck, J., "How stable is the photon?", PRL 111 (2013) 021801, arXiv:1304.2821 [S Abstract].
  - Lewis, G. F., Brewer, B. J., "Detection of the cosmological time dilation of high-redshift quasars", Nat. Astron.
    (2023), arXiv:2306.04053 [S Abstract].
- A2 OpenAlex 08:23:48 (quellen/A2-openalex-batch-20261005-082348.json):
  - Lisdat, C. u. a., "A clock network for geodesy and fundamental science", Nat. Commun. 7 (2016) 12443 [S Abstract].
  - Droste, S. u. a., "Optical-Frequency Transfer over a Single-Span 1840 km Fiber Link", PRL 111 (2013) 110801
    [S Abstract].
- A3 nature.com 08:24:39 (quellen/A3-nature-rainville-20261005-082439.html): Rainville, S., Thompson, J. K., Myers, E. G.
  u. a., "A direct test of E=mc2", Nature 438 (2005) 1096 [S Abstract].
- A4 nature.com 08:25:05 (quellen/A4-nature-lisdat-20261005-082505.html): Lisdat u. a. 2016, Haupttext und Methods
  ("Link noise cancellation") [S Volltext].
- A7 INSPIRE 08:26:36 (quellen/A7-inspire-batch2-20261005-082636.json):
  - Lee, S., "A unified interpretation of supernova, GRB, and QSO time dilation signals in a generalized cosmological
    time framework", Eur. Phys. J. C (2026), arXiv:2603.00427 [S Abstract].
  - Sanejouand, Y.-H., "A framework for the next generation of stationary cosmological models", IJMPD,
    arXiv:2005.07931 [S Abstract].
  - Oayda, O. T. u. a., "Testing the cosmological principle: on the time dilation of distant sources", MNRAS (2023),
    arXiv:2305.06771 [S Abstract].
- A8 OpenAlex 08:27:29 (quellen/A8-openalex-tes-20261005-082729.json):
  - "An optical transition-edge sensor with high energy resolution", Supercond. Sci. Technol. (2022),
    doi 10.1088/1361-6668/ac7e7b [S Abstract].
  - "Calibration and Testing of Small High-Resolution Transition Edge Sensor Microcalorimeters With Optical Photons",
    IEEE Trans. Appl. Supercond. (2021), doi 10.1109/tasc.2021.3053506 [S Abstract].
  - "High intrinsic energy resolution photon number resolving detectors", Appl. Phys. Lett. (2013),
    doi 10.1063/1.4815922 [S Abstract].
  - "Characterization of a Wide-Band Single-Photon Detector Based on Transition-Edge Sensor", Photonics 12 (2025) 609,
    doi 10.3390/photonics12060609 [S Abstract].
  - (Autoren dieser vier im Abruf nicht enthalten.)
- A13 arxiv.org 08:30:23 (quellen/A13-arxiv-abs-0906.3476-20261005-083023.html): Terra, O., Grosche, G., Predehl, K.,
  Holzwarth, R., Legero, T. u. a., "Phase-coherent comparison of two optical frequency standards over 146 km using a
  telecommunication fiber link", arXiv:0906.3476 (2009) [S Abstract].
- A15 OpenAlex 08:32:47 (quellen/A15-openalex-pqed-20261005-083247.json):
  - "Predictable Quantum Efficient Detector", Dissertation (2014), OpenAlex W2527677910 [S Abstract].
  - "Long-term spectral responsivity stability of predictable quantum detectors", CIE (2019),
    doi 10.25039/x46.2019.op58 [S Abstract].
  - "Long-term spectral responsivity stability of predictable quantum efficient detectors", Metrologia (2022),
    doi 10.1088/1681-7575/ac938c [S Abstract].
- Websuchen ohne Kopie (Werkzeugtext, nur Wegweiser): A5, A6, A11 (Wikipedia "Bothe-Geiger coincidence experiment";
  Bonolis, arXiv:1106.1365), A14.
- Leer: A9 (nds.iaea.org), A10 (OpenAlex Fe-57), A12 (physics.princeton.edu).
- Projekt [P]: neue-theorie/gitter-checkliste.json Z. 32 (Rainville 4e-7); coordination/art-grenzen-20260921/GEPRUEFT.md
  Z. 361 bis 366 (Pound/Rebka, Pound/Snider, GP-A, Galileo); RUNDE-37/licht-teile-l/DOSSIER.md (g2, Bedingungen B1 bis B6).
- Nur Gedaechtnis [L]: Fe-57 T1/2 ~ 98 ns und E = 14,4 keV; Isomerieverschiebungen bis ~1 mm/s; H0 = 70 km/s/Mpc.

---
Endzeit (date): 2026-10-05 08:41:46 CEST. Abrufe 15 von 15.
