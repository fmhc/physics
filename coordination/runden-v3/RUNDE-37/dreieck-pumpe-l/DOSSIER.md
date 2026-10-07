# DREIECK-PUMPE-L: Dossier (feldforscher fuer die Leitung, Runde 42, Literatur und Schreibtisch)

- Start 2026-10-04 18:12:19 CEST (date). Dossier geschrieben ab 18:38:56 CEST (date), abgeschlossen 2026-10-04
  18:45:59 CEST (date). Arbeitsdatei: ARBEITSFELD.md (alle Erwartungen mit date-Zeit vor jedem Abruf,
  Abrufprotokoll, Verstoesse, Gegensweep).
- Abrufe: 10 von 10 (F1 leer, F2 bis F10), alle ueber curl auf arXiv (API oder PDF), keine Websuche, kein WebFetch.
  Lokale Kopien in quellen/. Keine lokale Rechnung; [M] ist Kopfrechnung bzw. Herleitung.
- Kennzeichen: [S Z. n] an der Quelle gelesen mit Zeile (Zeilen von quellen/F3-rocklin-1510.06389v1.txt), [S Abstract],
  [P] Projektdatei, [L] Gedaechtnis, [L?] unsicher, [M] eigene Mathematik, [ES] eigener Schluss, [H] Hypothese.
- Einheit wie Karte: Kantenlaenge 1 PU.

## 1. Ergebnis zuerst

1. **Der Schreibtisch hat zwei folgenreiche Fehler.**
   - (a) Der Faltwinkel ist kein "eigener Kantenwert" im Sinn von B2. Er ist die relative Drehung zweier starrer
     Dreiecke (O_i^-1 O_j), also reine Eichung; um jede Ecke ist das Ringprodukt 1. Einen echten Umlauf gibt nur das
     Winkeldefizit: bei gleichen Dreiecken in 60-Grad-Stufen (Zahl der Dreiecke je Ecke), stufenlos erst mit
     ungleichen Kantenlaengen (Regge) [M].
   - (b) Geschlossene Schalen aus eckenteilenden Dreiecken sind nicht starr. Das Kuboktaeder aus 8 Dreiecken hat 6 innere
     Freiheitsgrade; seine symmetrische Drehung ist Fullers "Jitterbug" [M; P: Kusner u. a., Z. 1801-1823].
2. **Frage 1: Eckenbindung erzeugt Gelenke, keine neuen Kanten.**
   - 2D: Eine geteilte Ecke ist schon ein Scharnier mit 1 Winkel. Viele Dreiecke mit je 2 Dreiecken pro Ecke bilden die
     Kagome-Familie, genau ausgeglichen (Maxwell).
   - 3D: Eine Ecke ist ein Kugelgelenk mit 3 Winkeln, zwei Ecken ein Scharnier mit stufenlosem Faltwinkel. Viele
     Dreiecke mit 2 je Ecke sind wackelig (1,5 lose Moden je Dreieck); ausgeglichen erst bei 3 Dreiecken je Ecke [M].
   - Experiment: Dreiecksprismen binden an einer Wasseroberflaeche Spitze an Spitze oder Spitze an Kantenmitte und
     bilden offene Netze (Ferrar u. a. 2018) [S Abstract]. Kantenbindung mit Winkelvorgabe baut dagegen Schalen,
     Roehrchen und Toroide (DNA-Origami) [S Abstract].
3. **Frage 2, Atmen: ja, und robust.**
   - Jedes Maxwell-Gitter hat d(d-1)/2 gleichfoermige Verformungen ohne Energie: in 2D eine, in 3D drei [S Z. 272-279;
     M]. Das gilt "even with arbitrarily chosen shapes of triangles" [S Z. 254-258].
   - Bei gleichen Dreiecken in 2D ist es reines Wachsen und Schrumpfen [S Z. 122-127].
   - In Finns 3D-Netz schrumpft jede gleichfoermige Bewegung der primitiven Zelle nur quer zu einer Achse
     (tetragonal) [M]. Ob ein Kippmuster ueber vier Untergitter isotrop atmet, ist offen [L?, H]; dazu die Rechenkarte
     ISO-ATEM-1.
4. **Frage 2, Pumpen: gleichmaessiges Atmen allein pumpt nicht.**
   - Es ist ein Hin und Zurueck mit einem Parameter [M; P: SCHALTER-UND-ATMEN D4]. Die Atem-Mode schaltet die
     Polarisation nur hin und her [S Z. 233-242].
   - Gepumpt wird erst mit einer laufenden Phase: ein Randzustand im Experiment (Xia u. a. 2021) und Kink-Solitonen
     (Juergensen u. a. 2025, nur mit Reibung) [S Abstract].
   - "Pumpen durch einen Zyklus der Atem-Mode" ist nach Recherchestand nicht belegt (alle Jahre und 24 Monate).
   - Als Bauteil ist der Jitterbug eine Verdraengerpumpe: Volumen Faktor 5 bei festen Kanten [M; Endlage Oktaeder
     L]. Er ist als Atem-Roboter gebaut (2025) [S Abstract].
5. **Frage 3, ungleich grosse Dreiecke:**
   - Sie koennen sich keine Kanten mehr teilen, nur Ecken [M].
   - Erst ungleich geformte Dreiecke machen das Atmen topologisch wirksam: Beim Durchdrehen springt die Polarisation
     0 -> (a2 - a1) -> a2 -> 0 [S Z. 233-242]. Zwei Groessen gleichseitiger Dreiecke (Breathing Kagome) bleiben
     C3-symmetrisch und damit vermutlich unpolarisiert [ES].
   - Kruemmung entsteht nur im kantenteilenden Netz [M].
   - Zufall zerstoert das Atmen nicht [M + S]. Breathing-Pyrochlor-Kristalle mit grossen und kleinen Tetraedern gibt es
     [S Abstract].
6. **Kalibrierung und Warnzeichen:**
   - Meine Sicherheit "3D kann nicht isotrop atmen" wuchs am Schreibtisch und musste im Gegensweep auf die primitive
     Zelle eingeschraenkt werden.
   - "Cristobalit schrumpft beim Erwaermen" (Karte [L]) ist nicht belegt: Die gekippte Phase dehnt sich in einer
     Rechnung stark aus (BeF2) [S Abstract]. Das sind zwei Regime, kein Widerspruch.

## 2. Pruefung des Schreibtischs (Fehler zuerst)

**Fehler:**
- **SP1, Abschnitt 1, "eigener Kantenwert" [M]:** Zwei Dreiecke mit Lagen O_i, O_j: Ihr Faltwinkel steckt in O_i^-1 O_j.
  Um eine Ecke gilt (O_1^-1 O_2)(O_2^-1 O_3)...(O_n^-1 O_1) = 1, also die Schliessbedingung starrer Platten.
  - Das ist genau der Fall von GLUONEN-L V2 und B2 ("Ringprodukt 1"), nicht dessen Abhilfe. Passend dazu hat
    KOPPLUNG-TETRA-1 gemessen, dass die Ring-Holonomie nach Relaxation nichts kostet [P].
  - "Folgt nicht aus den Ecken" stimmt nur fuer die zwei geteilten Ecken. Aus den Lagen aller vier Ecken folgt der
    Winkel (Spitzenabstand sqrt(3) sin(theta/2)).
  - Ein Umlauf ungleich 1 ist die innere Holonomie: Drehung um das Winkeldefizit. Bei gleichseitigen Dreiecken kommt sie
    in 60-Grad-Stufen (Disklination), mit ungleichen Kantenlaengen stufenlos. Der Kantenwert mit Umlauf ist also die
    Kantenlaenge (Regge) [M, ES].
- **SP2, Abschnitt 2, "starr erst mit geschlossenen Schalen" [M]:** Bei eckenteilenden Dreiecken (jede Ecke in zwei)
  gilt V = 3F/2 und E = 3F, also 3V - E - 6 = 1,5 F - 6 innere Freiheitsgrade.
  - Kuboktaeder (F = 8): 6. Ikosidodekaeder (F = 20): 24.
  - Der Jitterbug ist "a jointed framework motion" vom Kuboktaeder zum Ikosaeder, mit Abstaenden, die "remain constant
    during the motion" [P: arXiv:1611.10297, lokal RUNDE-17/quellen-frustration/hilfs/p8-1611.10297.txt Z. 1801-1808].
  - Allgemein [M]: Ein starres Dreieck hat in D Dimensionen 3D - 3 Freiheitsgrade. Liegt jede Ecke in n Dreiecken,
    kostet das je Dreieck 3D(n - 1)/n Bedingungen. Ausgeglichen ist das bei n = D: in 2D bei n = 2 (Kagome), in 3D bei
    n = 3, in 4D bei n = 4.
  - Geschlossene Triangulationen, bei denen sich Dreiecke Kanten teilen, sind generisch starr (Gluck 1975 [L?]).
- **SP3, Abschnitt 1, Tetraeder-Schritt [M]:** Hier wechselt das Bindungsmodell.
  - Schritte 1 und 2: Ecken fallen zusammen (Gelenk).
  - Tetraeder-Schritt: Spitzen im Abstand 1 PU "binden", das ist ein neuer Stab.
  - Mit Zusammenfallen allein entsteht aus zwei Dreiecken kein Tetraeder. Es braucht einen Stab oder vier
    kantenteilende Dreiecke (jede Ecke in drei, n = 3: in 3D ausgeglichen und starr).
  - Welches Modell Finn meint, ist offen (Rueckfrage R1).
- **SP4, Abschnitt 5c, "ungleiche Kantenlaengen ... Winkeldefizite" [M]:** Das gilt nur generisch und nur im
  kantenteilenden Netz.
  - Eine ebene Triangulation aus ungleichen Dreiecken ist flach (Defizit 0).
  - Im eckenteilenden Netz bleiben ungleiche Dreiecke flach (Breathing Kagome).
  - Zufaellige Laengen geben in einer freien Haut Kruemmung (Beulen, vgl. KUGELSCHALE-1 [P]) und in der Ebene
    Frustration.
- **SP5, Abschnitt 5d, "das gleichmaessige Atmen zerfaellt vermutlich in Flecken [H]":** Das widerspricht der
  Zaehlung, siehe Verstoss V1 (Abschnitt 3a).
- **SP6, Abschnitt 4, "darum schrumpfen Geruest-Kristalle wie Cristobalit beim Erwaermen [L]":** nicht belegt, siehe
  V7. Ausserdem [M]: Die gleichfoermige Gegendrehung ist in 3D nicht isotrop, siehe SP8.

**Einschraenkungen und Ergaenzungen:**
- **SP7, Abschnitt 3 (richtig, aber anderes Regime):** Die Defizite stimmen: 12 x 60 = 6 x 120 = 4 x 180 = 720 Grad,
  n = 7 gibt -60 Grad [M]. Das gilt aber fuer kantenteilende Netze. Im eckenteilenden Netz (Kagome, Pyrochlor) liegt
  jede Ecke in genau zwei Dreiecken; die Kruemmung sitzt dort in den Loechern [M]:
  - Sechsecke: flach (60 + 60 + 120 + 120 = 360)
  - Fuenfecke: Ikosidodekaeder (30 Ecken x 24 Grad = 720)
  - Vierecke: Kuboktaeder (12 x 60 = 720)
  - Siebenecke: Sattel
- **SP8, Abschnitt 4, Dimension [M]:**
  - Kagome: Die Gegendrehung (oben +alpha, unten -alpha) ist ein exakter endlicher Mechanismus; das Gitter schrumpft
    isotrop um cos alpha. Vom geraden Kagome aus ist das zweite Ordnung, im verdrehten erste Ordnung. Rocklin u. a.
    bestaetigen "a pure dilation" fuer das verdrehte Kagome [S Z. 122-127].
  - 3D (Finns Netz, gerade Bruecke an der geteilten Ecke): Jede gleichfoermige Bewegung der primitiven Zelle ist eine
    Verformung F = (R_A + R_B)/2. Ihr Dehnungsanteil ist cos(phi) (I - n n^T) + n n^T, mit n der Achse und 2 phi dem
    Winkel der relativen Drehung R_A^-1 R_B.
  - Das Netz schrumpft also nur quer zu einer Achse (tetragonal, Volumen cos^2 phi). Das passt zu den drei
    Gamma-Drehungen von KOPPLUNG-TETRA-1 [P].
  - In 2D (sym R = cos alpha I) und in 4D (isokline Drehung) ist isotropes Atmen in der primitiven Zelle moeglich.
  - Grenze (Gegensweep G2): Kippmuster groesserer Zellen sind damit nicht erfasst.
- **SP9, fehlendes 2D-Gegenstueck zu Abschnitt 1 [M]:**
  - 2D, eine geteilte Ecke: 6 - 2 - 3 = 1 innerer Freiheitsgrad (Scharnier).
  - 2D, zwei geteilte Ecken: starr, mit zwei diskreten Lagen (Raute oder aufeinander). Der Faltwinkel ist in 2D
    diskret (0 oder 180 Grad), erst in 3D stufenlos.
- **SP10, Abschnitt 1, Zaehlung (richtig) [M]:** 12 - 3 - 2 = 7, minus 6 = 1.
  - Die zweite Bindung zaehlt nur 2, weil beide Dreiecke dieselbe Kantenlaenge haben.
  - Ungleich grosse Dreiecke koennen deshalb keine Kante teilen.
- **SP11, Wortwahl:** theta in sqrt(3) sin(theta/2) ist der Innen-Diederwinkel. arccos(1/3) = 70,53 Grad ist richtig
  (sin^2(theta/2) = 1/3, cos theta = 1/3). Im Origami-Gebrauch hiesse "Faltwinkel" die Abweichung von flach: 109,47
  Grad.
- **Richtig ohne Einschraenkung:** Abschnitt 2, Zaehlung der D-Simplexe: D(D+1)/2 Freiheitsgrade gegen D(D+1)/2
  Bedingungen [M]. Dreiecke in 3D mit 2 je Ecke: 6 - 4,5 = 1,5 [M].

## 3. Erwartungen E1 bis E6

| Nr | Erwartung (Karte) | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | Jedes periodische Maxwell-Gitter hat mindestens eine Verformung ohne Energie (Guest/Hutchinson 2003) | **eingetroffen, genauer:** d(d-1)/2 solche Verformungen, also 2D mindestens eine, 3D drei | Rocklin u. a. 2017, Z. 272-279: "all lattices with <z> = 2d (Maxwell lattices) must have d(d - 1)/2 homogeneous deformations that are of zero energy"; "These floppy modes have also been called 'Guest modes' [15, 16]" [S]; [15] = Guest/Hutchinson, JMPS 51, 383 (2003), nicht selbst gelesen. Eigene Zaehlung gleich [M] |
| E2 | Kane/Lubensky 2014: Polarisation folgt aus der Geometrie; im verformten Kagome sitzen die weichen Moden exponentiell an einem Rand | **eingetroffen, ueber Sekundaerquellen** | Kane/Lubensky, Abstract: Randmoden "localized at their boundary", "topological origin", Modelle "in one and two dimensions" [S Abstract]; Kagome und Polarisation stehen dort nicht. Rocklin Z. 233-242: R_T "points to an edge that gains extra floppy edge modes", "As first discovered in Ref. [20]" (= Kane/Lubensky) [S]; exponentieller Abfall Z. 108-114 [S]; Charara u. a. 2022: polarisierte Maxwell-Gitter "focus these zero modes to one of their boundaries" [S Abstract]. Volltext Kane/Lubensky nicht gelesen |
| E3 | Rocklin u. a. 2017: Die Guest-Hutchinson-Verformung schaltet die Polarisation um | **eingetroffen, genauer:** nur bei Dreiecken anderer Form als im regulaeren Kagome; Spruenge dort, wo Dreiecksseiten gerade Linien bilden | Abb. 1a, Z. 71-75: "Two types of triangles (red and blue) are connected by free hinges at their corners"; "3 critical angles ... where sides of the triangles form straight lines ... and topological polarization RT ... changes"; Z. 233-242: "0 -> (a2 - a1) -> a2 -> 0"; Kantensteifigkeit aendert sich "by orders of magnitude" (Rechnung, 60 x 60) Z. 216-230 [S] |
| E4 | Mechanische Thouless-Pumpe: langsame zyklische Parameteraenderung traegt einen Randzustand durchs Gitter (etwa Rosa u. a. 2019) | **eingetroffen, andere Quelle** | Xia u. a., PRL 126, 095501 (2021): "a smooth temporal variation of the modulation phase drives the transfer of edge states from one boundary of the waveguide to the other" (Experiment) [S Abstract]; Grinberg u. a.: "the first temporal topological pump ... of mechanical energy" [S Abstract]. Rosa u. a. 2019 nicht gelesen. Dazu Verstoss V2 |
| E5 | Janus-Kugeln -> Kagome (Chen/Bae/Granick 2011); DNA-Origami-Dreiecke mit festem Winkel -> Ikosaederschalen (Sigl u. a. 2021); ohne Winkelvorgabe in 3D wackelige Gele [H] | **teilweise** | Janus-Kagome: Chen/Bae/Granick nicht gefunden, bleibt [L]; in Simulation "elusive" (Mallory/Cacciuto 2019) [S Abstract], Verstoss V6. Origami: T = 3-Kapside aus 60 Dreiecken (Wei u. a. 2024) [S Abstract; P]; Roehrchen ueber programmierte Diederwinkel (Hayakawa u. a. 2022) [S Abstract]; Sigl 2021 nicht geprueft. Gele: begrenzte Valenz gibt "empty liquids and equilibrium gels" im Experiment (Ruzicka u. a. 2011) und eine bis T = 0 stabile ungeordnete Fluessigkeit (Smallenburg/Sciortino 2013) [S Abstract]. "Wackelig" haengt an der Gelenksteifigkeit (Neves u. a. 2025) [S Abstract] |
| E6 | Solitonen in topologischen Maxwell-Ketten (Chen/Upadhyaya/Vitelli 2014): eine Verformungsfront laeuft durch die Kette | **eingetroffen** | "the soft motion, initially localized at the edge, can in fact propagate unobstructed all the way to the opposite end"; "moving domain walls between distinct topological mechanical phases"; "transporting a mechanical state from one location to another" (Prototypen) [S Abstract] |

### 3a. Erwartungsverstoesse (getrennt, wichtigste zuerst)

- **V1: Die globale Atem-Mode ueberlebt beliebige Dreiecksformen und Unordnung.** Das widerspricht Kartenhypothese 5d.
  - Belege: Rocklin Z. 254-258 [S]. Die Zaehlung d(d-1)/2 gilt fuer jede periodische Superzelle, also auch fuer ein
    Zufallsnetz mit periodischem Rand [M]. Jedes Stueck behaelt die Bewegung, denn ein Mechanismus bleibt einer, wenn
    man Bindungen weglaesst [M].
  - Was sich aendert: Die Dreiecke drehen lokal ungleich, und die Mode ist im Allgemeinen keine reine Dilatation mehr.
    Nach dem Vorzeichen von det eps ist sie dilatations- oder scherungsdominiert [S Z. 108-133].
  - Folge fuer das Pumpen [M]: In 2D gibt es generisch genau einen gleichfoermigen Freiheitsgrad, also keine Schleife.
    In 3D gibt es drei, also Schleifen.
- **V2: Die mechanische Thouless-Pumpe, die Finns Bild am naechsten kommt, pumpt Kink-Solitonen.**
  - Juergensen u. a. 2025, gekoppelte Pendel: "quantized non-adiabatic Thouless pumping using topological kink
    solitons"; "dissipation is necessary"; die Quantisierung "cannot be described by the Chern number" (Experiment)
    [S Abstract].
  - Gemeinsame Groesse nach Regel 6 [ES]: Drei verschiedene Bauteile pumpen, naemlich Pendel, Gelenkkette (Chen 2014)
    und Piezo-Balken (Xia 2021). Allen gemeinsam ist eine **raeumlich laufende Phase**, also ein Zyklus mit Flaeche im
    Parameterraum. Gleichphasiges Atmen hat keine.
- **V3: Der Jitterbug ist gebaut.**
  - Roboter MOFU: "Jitterbug geometric transformation mechanism that enables smooth diameter changes from approximately
    210 mm to 280 mm with a single actuator" (Mogi u. a. 2025) [S Abstract].
  - Gold-Nanocluster: Kuboktaeder -> Ikosaeder als "soft-mode-driven jitterbug-type ... motions" (Rechnung,
    Khajehpasha u. a. 2026) [S Abstract].
  - Erwartet hatte ich nur Mathematik.
- **V4: Winkel einer Origami-Kette sind als Pumpparameter vorgeschlagen.** Li, Kevrekidis, Mao, Yang 2024:
  "topological pumping in origami metamaterials with spatial modulation by tuning the rotation angles" [S Abstract].
  Das ist eine Modulation im Raum, kein zeitliches Atmen.
- **V5: Kruemmung durch gezielt gesetzte Disklinationen ist bei DNA-Origami-Dreiecken ein Bauprinzip.** Toroide,
  helikale und schlangenfoermige Roehrchen "via the arrangement of disclination defects" (Price u. a. 2025)
  [S Abstract].
- **V6: Kolloid-Kagome ist schwer zu bauen.** Kagome aus Triblock-Janus-Kolloiden ist "elusive"; Eigenantrieb hilft
  (Mallory/Cacciuto 2019, Simulation) [S Abstract].
- **V7, gegen Karte [L]: Cristobalit-Ausdehnung.**
  - BeF2 in alpha-Cristobalit-Struktur: "we do not find any negative thermal expansion", dafuer "giant" Ausdehnung
    (~175e-6/K) (Rechnung, 2022) [S Abstract].
  - Urteil: "Cristobalit schrumpft beim Erwaermen" ist nach Recherchestand nicht belegt (eine Abfrage).
- **V8, nur meine Zwischenerwartung:** Nach Rocklins Abstract ("classification of all structures that exhibit such soft
  deformations") hatte ich erwartet, dass nicht jedes Maxwell-Gitter eine Guest-Mode hat. Falsch, siehe E1.

## 4. Antworten auf die Fragen 1 bis 4

**Dimensionsregel:** Raeumliche Dimension (2D/3D) ist getrennt von den inneren Freiheitsgraden (Gelenkwinkel,
Faltwinkel, Drehung eines Dreiecks).

### Frage 1: Was bilden zwei und viele Dreiecke, die an den Ecken binden?

**Vorab:** Es gibt drei Bindungsarten (Regime), siehe 4a: Ecke an Ecke, Ecke an Kante, Kante an Kante. Finn fragt
nach Ecke an Ecke. Ob die Ecken zusammenfallen oder sich im Abstand 1 PU beruehren, ist offen (R1). Unten gilt
Zusammenfallen.

| | 2D | 3D |
|---|---|---|
| Zwei Dreiecke, eine Ecke ("Fliege") | Scharnier: 1 Gelenkwinkel (innerer Freiheitsgrad) [M] | Kugelgelenk: 3 Winkel, eine relative Drehung [M] |
| Zwei Dreiecke, zwei Ecken | starr, zwei diskrete Lagen (Raute oder aufeinander) [M] | Scharnier: 1 stufenloser Faltwinkel; bei 70,53 Grad Spitzenabstand 1 PU [M] |
| Drei Ecken | aufeinander | aufeinander; ein Tetraeder nur mit Zusatzstab oder vier kantenteilenden Dreiecken [M] |
| Viele, jede Ecke in 2 | Kagome-Familie, genau ausgeglichen; mindestens eine Atem-Mode [S Z. 254-258] | wackelig, 1,5 lose Moden je Dreieck; auch geschlossene Schalen (Kuboktaeder 6, Ikosidodekaeder 24) [M] |
| Viele, jede Ecke in 3 | ueberbestimmt | ausgeglichen [M] |
| Kantenteilend (Triangulation) | Dreiecksgitter, starr | geschlossene Schalen generisch starr [L?]; Kruemmung = Zahl der Dreiecke je Ecke (Abschnitt 3 der Karte) |
| Experiment | Prismen an der Wasseroberflaeche: Spitze an Spitze oder Spitze an Kantenmitte, "space-spanning open networks" (Ferrar u. a. 2018) [S Abstract]; Kagome aus Janus-Kugeln [L], "elusive" [S Abstract] | DNA-Origami (Kante an Kante, Winkel programmiert): Roehrchen, T = 3-Kapside, Toroide [S Abstract]; ohne Winkelvorgabe: Netzwerke begrenzter Valenz bleiben Fluessigkeit oder Gel [S Abstract] |

**Was das fuer die Kanten heisst [M, ES]:**
- Die Dreieckskanten bleiben starr und gehoeren im eckenteilenden Netz je einem Dreieck.
- Der neue Wert sitzt am Gelenk: in 2D ein Winkel, in 3D eine Drehung (3 Winkel), an einer geteilten Kante ein
  Faltwinkel.
- Im Netz liegt jedes Gelenk auf einer Kante des Mittelpunktnetzes: Honigwabe in 2D, Diamant in 3D [M]. Im
  Cristobalit ist das der Si-O-Si-Winkel am Brueckensauerstoff [L].
- Alle diese Gelenkwerte sind Differenzen der Dreieckslagen und haben deshalb keinen Umlauf (SP1). Einen Kantenwert
  mit Umlauf gibt es erst, wenn die Kantenlaengen variieren duerfen (Frage 3).

### Frage 2: Kann ein solches Netz gleichmaessig atmen und dabei pumpen?

**Atmen:**
- 2D: ja. Jedes Maxwell-Gitter hat mindestens eine gleichfoermige weiche Verformung, bei beliebiger Dreiecksform
  [S Z. 254-258, 272-279]. Bei gleichen Dreiecken ist sie reine Dilatation mit "emergent conformal symmetry"
  [S Z. 122-129].
- 3D, Finns Netz: Es gibt drei gleichfoermige Moden (d(d-1)/2 = 3; die drei Gamma-Drehungen [P]). Jede davon und jede
  Kombination in der primitiven Zelle schrumpft nur quer zu einer Achse [M, SP8]. Isotropes Atmen braucht ein Muster
  ueber mehrere Zellen und ist offen (ISO-ATEM-1).
- Endliches 3D-Teil: der Jitterbug, 8 Dreiecke an 12 Ecken. Er atmet vom Kuboktaeder ueber das Ikosaeder zum
  Oktaeder [P bis Ikosaeder; L bis Oktaeder].
  - Umkugelradius a, 0,951 a, 0,707 a [M].
  - Volumen 2,357 a^3, 2,182 a^3, 0,471 a^3, also Faktor 5 [M].

**Pumpen:**
- Ein gleichmaessiger Atemzyklus ist ein Hin und Zurueck auf einem Weg mit einem Parameter.
  - Er transportiert nichts netto: Purcell [P: SCHALTER-UND-ATMEN D4]; ein Zyklus ohne Flaeche [M].
  - Topologisch schaltet die Atem-Mode die Polarisation vor und zurueck, die weichen Moden wandern von einem Rand zum
    anderen und zurueck [S Z. 216-242].
- Was in der Literatur pumpt, hat eine laufende Phase:
  - Modulationsphase verschiebt Randzustaende von Rand zu Rand (Xia u. a. 2021, Experiment) [S Abstract].
  - Kink-Solitonen werden je Zyklus quantisiert weitergeschoben, nur mit Reibung (Juergensen u. a. 2025, Experiment)
    [S Abstract].
  - Eine wandernde Domaenenwand traegt den Zustand durch die Gelenkkette (Chen u. a. 2014, Prototyp) [S Abstract].
- **Bestes Literaturbild fuer Finns Frage [ES]:** eine laufende Verdrehungswelle (Peristaltik), also eine Domaenenwand
  zwischen zwei Verdrehungszustaenden, die durchs Netz wandert. Gleichtakt allein reicht nicht.
- **Dimension [M]:**
  - 2D: generisch eine gleichfoermige Mode, also keine Schleife moeglich.
  - 3D: drei, also Schleifen mit Flaeche moeglich. Ob eine solche Schleife Randmoden oder Kinks traegt, ist nicht belegt
    (F4 alle Jahre, F5 24 Monate) [H].
- **Als Fluessigkeitspumpe (Lesart R2):** Der Jitterbug verdraengt bis zu 4/5 seines groessten Volumens [M]. Eine
  Richtung braucht Ventile oder eine zweite, phasenversetzte Formaenderung. Er hat 6 innere Freiheitsgrade [M], also
  genug fuer nicht umkehrbare Zyklen [H].

### Frage 3: Was aendern ungleich grosse Dreiecke?

- **Bindung [M]:** Ungleich grosse gleichseitige Dreiecke koennen sich keine Kante teilen, nur Ecken. Damit bleibt nur
  das eckenteilende Regime.
- **Polarisation:**
  - Erst Dreiecke anderer Form machen die Atem-Mode topologisch wirksam (Rocklin: zwei Dreieckstypen, R_T springt an
    drei kritischen Winkeln) [S Z. 71-75, 233-242].
  - Zwei Groessen gleichseitiger Dreiecke (Breathing Kagome) behalten C3-Symmetrie. Ein Gittervektor R_T muesste
    C3-invariant sein, also null [ES, nicht in der Literatur gefunden].
  - Mechanisch ist das Breathing Kagome als Federmassen-Modell untersucht: Higher-Order-Phase mit Eckzustaenden,
    Z3-Berry-Phase 2 pi/3 (Wakao u. a. 2020) [S Abstract]. Das ist ein anderes Regime (endliche Frequenz, keine
    Nullmoden).
- **Kruemmung [M]:**
  - Kantenteilend: Ungleiche Laengen koennen Defizite erzeugen (Regge), muessen aber nicht.
  - Eckenteilend: Ungleiche Dreiecke bleiben flach; Kruemmung entsteht nur ueber die Loecher (SP7).
  - Im Experiment setzt man Disklinationen gezielt (Price u. a. 2025) [S Abstract].
- **Zufall:**
  - Die globale Atem-Mode bleibt (V1) [S, M].
  - Topologische Randmoden gibt es auch in ungeordneten Parallelogramm-Kachelungen, mit Richtungen, die periodisch nicht
    erlaubt sind (Zhou/Zhang/Mao 2019) [S Abstract]. Polarisation ist "protected against disorder" (Charara u. a. 2022)
    [S Abstract].
  - Material: die Silica-Doppelschicht als "two dimensional network of corner sharing triangles" (Wilson u. a. 2013)
    [S Abstract].
- **3D:**
  - Breathing-Pyrochlor-Kristalle mit "size-alternating ... tetrahedra" gibt es: LiGa(1-x)In(x)Cr4O8 [S Abstract],
    Ba3Tm2Zn5O11 mit F-43m-Struktur [S Abstract]. Untersucht wird dort Magnetismus, nicht die Mechanik der Kippmoden.
  - Im Projekt ist der Name schon da (Yan u. a. 2020, Rang-2-U(1) "auf dem atmenden Pyrochlor" [P, TETRAEDER-L]).

### Frage 4: siehe Abschnitt 6 (ISO-ATEM-1)

### 4a. Regime und Moderatoren (Regel 1)

| Regime A | Regime B | Moderator | Beleg |
|---|---|---|---|
| Ecke an Ecke (Gelenk): offene, wackelige oder ausgeglichene Netze (Kagome, Pyrochlor) | Kante an Kante mit Winkelvorgabe: Schalen, Roehrchen, Toroide | Bindungsort und Winkelprogrammierung; Zahl n der Dreiecke je Ecke | [M]; Hayakawa 2022, Wei 2024, Price 2025 [S Abstract]; dritter Modus Ecke an Kantenmitte (Ferrar 2018) |
| Ecken fallen zusammen (Kugelgelenk) | Ecken beruehren sich im Abstand 1 PU (Stab) | Finns Definition von "binden" (R1) | SP3 |
| freie Gelenke: Nullmoden, Mechanismen | winkelsteife Bindungen: weiche, aber nicht freie Moden; Gelsteifigkeit ab Teilchen mit drei Bindungen | Gelenksteifigkeit | Rocklin Z. 271-278 [S]; Neves 2025 [S Abstract] |
| regulaere Dreiecke, gerade Linien: Eigenspannungen, Linien-Nullmoden, R_T = 0 | verformte Dreiecke: Luecke, polarisiert | Dreiecksform und Verdrehwinkel theta | Rocklin Z. 216-242 [S]; EIS-1 [P] |
| gleichphasiges Atmen: kein Netto-Transport | laufende Phase: Pumpe | Flaeche des Zyklus im Parameterraum | Xia 2021, Juergensen 2025 [S Abstract]; [M] |
| gekippte Phase (statisch): Ausdehnung beim Erwaermen | ungekippte Phase (dynamisch): Schrumpfen durch thermische Drehungen | Temperatur relativ zum Kipp-Uebergang | BeF2-Rechnung [S Abstract]; Rocklin Z. 288-293 [S]; Lesart [ES, L] |
| 2D: eine gleichfoermige Mode, isotrop bei gleichen Dreiecken | 3D: drei Moden, in der primitiven Zelle nur tetragonal | Raumdimension (feste Drehachse in ungerader Dimension) | [S Z. 272-279; M] |

### 4b. Unterscheidungspunkte (Regel 2)

- **Faltwinkel "eigener Kantenwert" oder reine Eichung:**
  - Trennende Messung: das Ringprodukt der relativen Drehungen um eine geschlossene Ecke. Reine Eichung gibt immer 1,
    ein eigener Wert koennte davon abweichen.
  - In jedem Modell aus starren Platten ist es 1 [M]. KOPPLUNG-TETRA-1 hat das indirekt gesehen (Holonomie kostet
    nichts) [P].
  - Die Erklaerungen trennen sich nur, wenn die Platten sich verformen duerfen (Kantenlaengen frei).
- **Atmen pumpt oder nicht:**
  - Trennende Region: Zyklen mit Flaeche im Raum der gleichfoermigen Moden. In 2D gibt es sie generisch nicht, dort
    ist die Frage leer: kein Pumpen durch gleichfoermiges Atmen.
  - In 3D: eine Schleife um eine kritische Lage (gerade Linien bzw. Ebenen), gemessen an den Randmoden je Flaeche nach
    einem Umlauf. Nicht gerechnet, nicht in der Literatur gefunden.
- **Isotropes Atmen in 3D moeglich oder nicht:**
  - Die primitive Zelle trennt nicht, dort ist es sicher unmoeglich [M].
  - Trennend ist die kubische Zelle mit 8 Tetraedern: ISO-ATEM-1.
- **Breathing Kagome polarisiert oder nicht:**
  - Trennende Messung: die Kantensteifigkeit gegenueberliegender Raender wie in Rocklin Abb. 3d.
  - Vorhersage [ES]: kein Unterschied, solange C3 bleibt; ein Unterschied erst bei Formbruch.
- **Cristobalit schrumpft oder dehnt sich:** Die Temperatur trennt, unterhalb gegen oberhalb des Kipp-Uebergangs. Die
  Literatur dazu habe ich nicht gelesen (Klassiker nicht auf arXiv).

## 5. Ankertabelle (messnah)

| Anker | Was gemessen oder gebaut | Raum | Bezug | Quelle |
|---|---|---|---|---|
| Dreiecksprismen an Luft-Wasser-Grenzflaeche | Kante 120 um; binden kapillar Spitze an Spitze oder Spitze an Kantenmitte; offene, raumspannende Netze, noch kein Kagome | 2D | Frage 1 woertlich | Ferrar u. a., Soft Matter 14, 3902 (2018), arXiv:1802.02949 [S Abstract] |
| DNA-Origami-Dreiecke, programmierte Diederwinkel | Roehrchen mit vorgegebener Breite, aber Breiten- und Chiralitaetsverteilung | 3D (gekruemmte 2D-Haut) | Kante an Kante, Faltwinkel als Bauvorgabe | Hayakawa u. a., PNAS 119, e2207902119 (2022), arXiv:2203.01421 [S Abstract] |
| DNA-Origami-Dreiecke -> T = 3-Kapsid | 60 Untereinheiten; ungleiche Bindungen geben Dimer- oder Pentamer-Wege, schneller und robuster | 3D-Schale | Ikosaeder aus Dreiecken, Fuenfer-Ecken | Wei u. a., PNAS 121, e2312775121 (2024), arXiv:2310.18790 [S Abstract; P] |
| DNA-Origami: Disklinationen nach Plan | Toroide, helikale und schlangenfoermige Roehrchen | 3D | Kruemmung = Dreiecke je Ecke | Price u. a. (2025), arXiv:2506.16403 [S Abstract] |
| Kolloidaler Ton ("complex colloidal clay"), begrenzte Valenz | "empty liquids and equilibrium gels" | 3D | Netz ohne Winkelvorgabe -> Gel | Ruzicka u. a., Nat. Mater. 10, 56 (2011), arXiv:1007.2111 [S Abstract] |
| Triblock-Janus-Kolloide -> Kagome | Kagome im Experiment [L]; Simulation: "elusive", Aktivitaet hilft | 2D | Eckenbindung ordnet schlecht | Chen/Bae/Granick, Nature 469, 381 (2011) [L]; Mallory/Cacciuto, arXiv:1902.05583 [S Abstract] |
| 3D-gedruckte Kagome-Doppelschicht | topologische Polarisation bei endlicher Frequenz, Laser-Vibrometrie | 2D-Schicht im Raum | polarisierte Raender | Charara u. a. (2022), arXiv:2204.13615 [S Abstract] |
| Gelenkkette (Prototyp) | Kink laeuft vom einen Ende zum anderen | 1D | Verformungsfront als Transport | Chen/Upadhyaya/Vitelli, PNAS 111, 13004 (2014), arXiv:1404.2263 [S Abstract] |
| Piezo-Aluminiumbalken | Randzustand per Modulationsphase von Rand zu Rand | 1D | mechanische Thouless-Pumpe | Xia u. a., PRL 126, 095501 (2021), arXiv:2006.07348 [S Abstract] |
| Gekoppelte Pendel | quantisiertes Pumpen von Kink-Solitonen, Reibung noetig | 1D | Pumpe mit Kinks | Juergensen u. a. (2025), arXiv:2502.14046 [S Abstract] |
| Roboter MOFU | Jitterbug, ein Motor, Durchmesser 210 -> 280 mm | 3D | atmendes Teil aus eckverbundenen Dreiecken | Mogi u. a. (2025), arXiv:2509.09613 [S Abstract] |
| Breathing-Pyrochlor-Kristalle | LiGa(1-x)In(x)Cr4O8, Ba3Tm2Zn5O11 (F-43m), Einkristalle, Neutronenstreuung | 3D | ungleich grosse Tetraeder als echter Kristall | Tanaka u. a., JPSJ 87, 073710; Yadav u. a., PRMaterials 8, 123401 (2024) [S Abstract] |
| Glasartige Silica-Doppelschicht | experimentell hergestellt [S Abstract, "landmark work"]; Modell als eckenteilendes Dreiecksnetz | 2D | ungeordnetes eckenteilendes Netz | Wilson u. a., PRB 87, 214108 (2013), arXiv:1303.5898 [S Abstract] |
| beta-Cristobalit (SiO2) | RUM-Ebenen (Hammonds u. a. 1996); Waermeausdehnung nicht belegt | 3D | Finns Netz als Mineral | [P: KOPPLUNG-TETRA-1, Wegner S]; Karte [L]; BeF2-Rechnung arXiv:2209.10087 [S Abstract] |

## 6. Rechenkartenvorschlag: ISO-ATEM-1 "Kann Finns Netz isotrop atmen?"

**Modell:**
- Regulaere Tetraeder, Kante 1 PU, starr. Eckenteilend in Finns Topologie (Pyrochlor bzw. ideales beta-Cristobalit),
  Kugelgelenke.
- Periodische kubische Zelle mit 8 Tetraedern (16 Ecken).

**Frage:** Gibt es eine endliche Bewegung ohne Verformung der Tetraeder, bei der die Zelle kubisch bleibt und schrumpft
(F = lambda I, lambda < 1)?

**Teile:**
- **A, Kontrolle, vorab ableitbar:** Gegendrehung um [001] mit Dehnungsanteil diag(cos phi, cos phi, 1), Rest der
  Eckbedingungen <= 1e-12.
- **B, symmetrischer Start:** Jedes Tetraeder dreht um seine eigene <111>-Achse (P2_13-artig). Unbekannte: Drehwinkel
  oben und unten, Lage der Mitten auf den Achsen, Zellkante, also 5 Unbekannte gegen 4 Gleichungen. Die Loesungskurve
  wird von phi = 0 aus verfolgt.
- **C, ohne Symmetrieansatz:** Je Zielwert lambda in {0,99; 0,97; 0,95; 0,90} wird der Rest der 16 Eckgleichungen aus
  vielen Zufallsstarts minimiert. Das prueft, ob es weitere isotrope Mechanismen gibt.

**Messgroessen:**
- Rest r(lambda)
- Volumen lambda^3 gegen den Kippwinkel
- Winkel an der geteilten Ecke (Gegenstueck zu Si-O-Si)
- Kippwinkel, bei dem sich Tetraeder beruehren

**Vorhersagen (vorab):**

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IA1 | Kontrolle: Teil A exakt; der Gamma-Ansatz erreicht F = lambda I nie (Rest > 1e-3 bei lambda = 0,97) | 95 % |
| IA2 | [H] Fuer lambda = 0,97 gibt es eine Loesung mit Rest < 1e-10, also isotropes Atmen in der kubischen Zelle | 60 % |
| IA3 | [H] Die Loesung aus IA2 hat P2_13-Symmetrie (je Tetraeder eine eigene <111>-Achse) | 50 % |

**Scheitern und Bestehen:**
- IA2 scheitert, wenn kein Start fuer ein lambda < 1 unter Rest 1e-6 kommt. Dann gilt: Finns Netz atmet in dieser
  Zelle nur flach (tetragonal) oder ungleich.
- IA2 besteht mit Rest < 1e-10 auf einem zusammenhaengenden Ast.

**Ableitbarkeitsprobe:**
- **Vorab ableitbar [M]:**
  - Teil A und der Satz "in der primitiven Zelle nur tetragonal" (SP8).
  - Zweite Ordnung: Das Mittel von (I - n n^T) ueber die vier <111>-Richtungen ist (2/3) I. Das ist nur ein Hinweis,
    kein Beweis.
  - Die Zaehlung 5 - 4 = 1 im Ansatz B ist heuristisch; ob die Gleichungen unabhaengig und loesbar sind, ist offen.
- **Vielleicht in der Literatur, nicht gelesen:** das P2_13-Modell von beta-Cristobalit (Wright/Leadbetter 1975 [L?])
  und RUM-Analysen der Dove-Gruppe [L?].
  - Die Leitung sollte vor der Rechnung pruefen, ob dort "P2_13 = Kippung starrer Tetraeder" steht.
  - Wenn ja, ist IA2 vorab bekannt. Als Messung bleiben dann nur lambda(phi), die Grenze des Asts und Teil C.
- **Nicht ableitbar:** Existenz und Bereich eines exakten endlichen Asts, lambda(phi) und weitere isotrope Mechanismen
  in der Zelle.
- **Kann scheitern und bestehen:** ja (siehe oben). Aufwand: Sekunden (A, B) bis Minuten (C), Kleintest-Spur.

**Anschluss und Dimension:**
- **Anschluss ATEM-NETZ-1:** Laut dortigem Schreibtisch entsteht Gleichtakt ueber die Huelle nicht. Trifft IA2 ein,
  hat Finns Netz einen Gleichtakt-Atemkanal ohne Energie (alle Tetraeder kippen, das Netz atmet isotrop). Dann lohnt
  eine gemeinsame Karte "atmende Ecken + Kippmode" (R5).
- **Dimension:**
  - 2D (Kagome): isotrop bekannt [S Z. 122-127].
  - 3D: Gegenstand der Karte.
  - 4D: schon in der primitiven Zelle moeglich (isokline Drehung) [M].
- **Projekt-grep (18:35):** keine Karte zu isotropem Atmen, P2_13 oder I-42d.

### 6a. Gegensweep (Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

- **G1, "Binden an der Ecke" ist ein Kugelgelenk:** geprueft (F10). Reale Spitzenbindung ist ein Kapillarkontakt; die
  Spitze bindet auch an die Kantenmitte oder an jede Stelle der Kante (Ferrar u. a. 2018). Daraus ergibt sich ein
  dritter Bindungsmodus.
- **G2, "gleichmaessig" heisst gleich in jeder primitiven Zelle:** nicht durch Abruf geprueft (Budget). Folge: SP8 gilt
  nur fuer die primitive Zelle. Daraus entstand ISO-ATEM-1.
- **G3, Cristobalit-Ausdehnung (Karte [L]):** geprueft (F8), nicht belegt (V7). Lesart mit zwei Regimen.
- **G4, freie Gelenke:** geprueft (F3 Z. 271-278: "When this hinge rigidity is small but finite it determines
  properties that would vanish with completely flexible hinges, such as the stiffness of the soft edges and sound
  velocities"). Moderator Gelenksteifigkeit.
- **G5, "pumpen" heisst Thouless:** nicht geprueft. Finn kann eine Fluessigkeitspumpe meinen (R2); Frage 2 beantwortet
  beide Lesarten.
- **G6, die Maxwell-Zaehlung gilt fuer Finns Netz:** geprueft (F3 Z. 219-226; EIS-1 [P]). Finns regulaeres Netz ist
  die besondere Geometrie mit geraden Linien; dort kommen Eigenspannungen und Linien- bzw. Ebenen-Nullmoden dazu. Die
  Untergrenzen bleiben.

### 6b. Offene Fragen und Rueckfragen

- **R1 (Finn):** Ecken fallen zusammen (Gelenk) oder beruehren sich im Abstand 1 PU (Stab)?
- **R2 (Finn):** Was soll gepumpt werden: Fluessigkeit, eine Verformung oder ein Randzustand?
- **R3 (Finn):** "Ungleich gross" heisst zwei Groessen im Wechsel oder zufaellig?
- **R4 (Finn/Leitung):** Darf eine Ecke mehr als zwei Partner haben? Ab n = 3 wird das Netz in 3D ausgeglichen, mit
  Kantenteilung starr.
- **R5 (Leitung):** ISO-ATEM-1 mit ATEM-NETZ-1 abstimmen.
- **R6 (Literatur, offen):** P2_13 mit exakt starren Tetraedern? Thermische Ausdehnung von beta-Cristobalit (Vorzeichen)?
  Guest/Hutchinson 2003, Kane/Lubensky (Volltext), Sun u. a. 2012 und Sigl u. a. 2021 nicht selbst gelesen.

### 6c. Kalibrierung

- **(a) Gemessen:** die Experimente der Ankertabelle (Ferrar, Hayakawa, Wei, Price, Ruzicka, Charara, Chen, Xia,
  Juergensen, MOFU, Kristallsynthesen).
- **(b) Nuetzlich verdichtet:**
  - Zaehlungen: n = D je Ecke; 1,5 F - 6 bei eckenteilenden Schalen; d(d-1)/2 [M, S]
  - Faltwinkel = reine Eichung [M]
  - Gamma-Mode in 3D nur tetragonal [M]
  - Jitterbug-Zahlen [M]
  - Lesart "laufende Phase pumpt" [ES]
- **(c) Gewissheit ohne neue Evidenz:**
  - Die Breathing-Kagome-Aussage R_T = 0 [ES].
  - Die Pump-Schleife in 3D [H].
  - "3D kann nicht isotrop atmen": Meine Sicherheit stieg am Schreibtisch, bis der Gegensweep sie auf die primitive
    Zelle einschraenkte. Dieses Muster ist ein Warnzeichen und hier offen benannt.

## 7. Quellenliste mit lokalen Kopien (alle in quellen/, ausser [P])

Gelesen per curl (arXiv-API oder PDF), Abrufzeiten in ARBEITSFELD.md:
- F1 (leer, 0 Byte): F1-api-kane-rocklin-chen.xml.
- F2: F2-api-kane-rocklin-chen.xml (+ F2-header.txt).
  - Kane, C. L.; Lubensky, T. C. (2014): Topological boundary modes in isostatic lattices. Nat. Phys. 10, 39.
    https://arxiv.org/abs/1308.0554 [S Abstract]
  - Rocklin, D. Z.; Zhou, S.; Sun, K.; Mao, X. (2017): Transformable topological mechanical metamaterials. Nat. Commun.
    8, 14201. https://arxiv.org/abs/1510.06389 [S Abstract]
  - Chen, B. G.; Upadhyaya, N.; Vitelli, V. (2014): Nonlinear conduction via solitons in a topological mechanical
    insulator. PNAS 111, 13004. https://arxiv.org/abs/1404.2263 [S Abstract]
- F3: F3-rocklin-1510.06389v1.pdf und .txt (Volltext Rocklin u. a., v1, 7 S.) [S Z.]
- F4: F4-api-mech-pumping.xml (20 von 61).
  - Li, S.; Kevrekidis, P. G.; Mao, X.; Yang, J. (2024): Topological pumping in origami metamaterials.
    https://arxiv.org/abs/2401.09668
  - Grinberg, I. H.; Lin, M.; Harris, C.; Benalcazar, W. A.; Peterson, C. W.; Hughes, T. L.; Bahl, G. (arXiv 2019):
    Robust temporal pumping in a magneto-mechanical topological insulator. https://arxiv.org/abs/1905.02778
  - Xia, Y.; Riva, E.; Rosa, M. I. N.; Cazzulani, G.; Erturk, A.; Braghin, F.; Ruzzene, M. (2021): Experimental
    observation of temporal pumping in electro-mechanical waveguides. PRL 126, 095501.
    https://arxiv.org/abs/2006.07348
  - Juergensen, M.; ...; Rechtsman, M. C. (2025): Quantized dynamical pumping via dissipation in a mechanical Thouless
    pump. https://arxiv.org/abs/2502.14046 (Autorenliste im Abruf nur teilweise gesehen)
  - Nur Abstract-Abgleich: arXiv:2303.04111, 2005.14066, 2402.09958, 1911.02567.
- F5: F5-api-maxwell-pump-24m.xml (38 Treffer, 2024-10-04 bis 2026-10-04): kein Treffer zum Pumpen mit Nullmoden;
  arXiv:2607.18995 (Maxwell-Zaehlung, granulare Kontinua).
- F6: F6-api-selbstbau.xml.
  - Hayakawa, D. u. a. (2022): Geometrically programmed self-limited assembly of tubules using DNA origami colloids.
    PNAS 119, e2207902119. https://arxiv.org/abs/2203.01421
  - Wei, W.-S. u. a. (2024): Hierarchical assembly is more robust than egalitarian assembly in synthetic capsids. PNAS
    121, e2312775121. https://arxiv.org/abs/2310.18790 (auch [P])
  - Price, M. u. a. (2025): From toroids to helical tubules: Kirigami-inspired programmable assembly of two-periodic
    curved crystals. https://arxiv.org/abs/2506.16403
  - Mallory, S.; Cacciuto, A. (2019): Activity-enhanced self-assembly of a colloidal kagome lattice.
    https://arxiv.org/abs/1902.05583
  - Huang, R. u. a. (2025): Shape-controlled growth of two-dimensional kagome-lattice colloidal crystals through
    nanoparticle capping. https://arxiv.org/abs/2511.06630
- F7: F7-api-breathing-unordnung.xml.
  - Wakao, H.; Yoshida, T.; Araki, H.; Mizoguchi, T.; Hatsugai, Y. (2020): Higher-order topological phases in a
    spring-mass model on a breathing kagome lattice. PRB 101, 094107. https://arxiv.org/abs/1909.02828
  - Charara, M.; McInerney, J.; Sun, K.; Mao, X.; Gonella, S. (2022): Omnimodal topological polarization of bilayer
    networks. https://arxiv.org/abs/2204.13615
  - Zhou, D.; Zhang, L.; Mao, X. (2019): Topological mechanics in quasicrystals. PRX 9, 021054.
    https://arxiv.org/abs/1809.09188
  - Tanaka, Y. u. a.: Inelastic neutron scattering study ... LiGa0.95In0.05Cr4O8. JPSJ 87, 073710.
    https://arxiv.org/abs/2301.05064
  - Yadav, L. u. a. (2024): Synthesis and characterization of the novel breathing pyrochlore compound Ba3Tm2Zn5O11.
    PRMaterials 8, 123401. https://arxiv.org/abs/2407.00222
- F8: F8-api-cristobalit.xml.
  - A first-principles investigation of the linear thermal expansion coefficients of BeF2 (2022), RSC Adv. 12, 26588.
    https://arxiv.org/abs/2209.10087 (Autoren im Abruf nicht notiert)
  - Rickwardt, C.; Nielaba, P.; Mueser, M. H.; Binder, K.: Path integral Monte Carlo simulations of silicates.
    https://arxiv.org/abs/cond-mat/0010315
- F9: F9-api-jitterbug-patchy.xml.
  - Ruzicka, B. u. a. (2011): Observation of empty liquids and equilibrium gels in a colloidal clay. Nat. Mater. 10, 56.
    https://arxiv.org/abs/1007.2111
  - Smallenburg, F.; Sciortino, F. (2013): Liquids more stable than crystals. https://arxiv.org/abs/1307.1842
  - Neves, J. C.; Tavares, J. M.; Araujo, N. A. M.; Dias, C. S. (2025): Rigid m-percolation in limited-valence gels.
    https://arxiv.org/abs/2504.02474
  - Mogi, T. u. a. (2025): MOFU: Development of a MOrphing Fluffy Unit .... https://arxiv.org/abs/2509.09613
  - Khajehpasha, E. R.; Safa, M. I.; Eyvazi, N.; Krummenacher, M.; Goedecker, S. (2026): The transformation mechanisms
    among cuboctahedra, Ino's decahedra and icosahedra structures of magic-size gold nanoclusters.
    https://arxiv.org/abs/2601.10434
  - Sadler, G.; Fang, F.; Kovacs, J.; Irwin, K. (2013): Periodic modification of the Boerdijk-Coxeter helix
    (tetrahelix). https://arxiv.org/abs/1302.1174
- F10: F10-api-ecken-selbstbau.xml.
  - Ferrar, J. A.; Bedi, D. S.; Zhou, S.; Zhu, P.; ... (2018): Capillary-driven binding of thin triangular prisms at
    fluid interfaces. Soft Matter 14, 3902. https://arxiv.org/abs/1802.02949
  - Wilson, M.; Kumar, A.; Sherrington, D.; Thorpe, M. F. (2013): Modeling vitreous silica bilayers. PRB 87, 214108.
    https://arxiv.org/abs/1303.5898

Projektdateien [P] (nur gelesen):
- RUNDE-34/eis-1/ERGEBNIS.md
- RUNDE-37/tetraeder-l/DOSSIER.md Z. 80-125 und quellen/F11-api-regime-packung.xml (Lubensky u. a. 2015,
  arXiv:1503.01324)
- RUNDE-37/kopplung-tetra-1/ERGEBNIS.md (Wegner 2007, cond-mat/0703486; lokale PDF dort per pdftotext auf stdout
  durchsucht)
- RUNDE-23/kugelschale-1/ERGEBNIS.md
- RUNDE-37/atem-netz-1/KARTE.md
- RUNDE-42/SCHALTER-UND-ATMEN.md (B2, D4)
- RUNDE-16/stabil-6-8-12/KARTE.md Z. 44
- parallel-pruefungen-20260910/natur-mechanismen/NATUR-ABGLEICH.md Z. 18-24
- RUNDE-17/quellen-frustration/hilfs/p8-1611.10297.txt Z. 1801-1823 (Kusner, Kusner, Lagarias, Shlosman, arXiv:1611.10297:
  Jitterbug)

Aus dem Gedaechtnis, nicht gelesen [L/L?]:
- Guest/Hutchinson 2003, JMPS 51, 383 (nur als Zitat [15] bei Rocklin)
- Sun/Souslov/Mao/Lubensky 2012, PNAS 109, 12369 (Zitat [18])
- Chen/Bae/Granick 2011
- Sigl u. a. 2021
- Gluck 1975
- Wright/Leadbetter 1975 (P2_13)
- Fuller, Synergetics (Jitterbug bis zum Oktaeder)

## 8. Selbstanzeigen

- **Regelverstoss awk (vor 18:45:23, date):** Fuer eine Zeilenlaengenprobe dieses Dossiers habe ich einmal awk
  aufgerufen, obwohl awk verboten ist. Keine Physikrechnung; Ergebnis nur: lange Zeilen sind Tabellenzeilen, nichts
  geaendert.
- **F1 war leer** (http ohne Weiterleitung) und zaehlt als Abruf. Inhaltlich gab es nur 9 Abrufe.
- **Buendelung:** Mehrere API-Abrufe holten mehrere Arbeiten in einem Aufruf (F2: 3, F4: 20, F5: 38 Eintraege). Je
  Aufruf habe ich einen Abruf gezaehlt; das legt die Grenze 10 weit aus.
- **Geschaetzte Zeiten:** "Notiert ab 18:15" und "berichtigt 18:38" geschaetzt in ARBEITSFELD.md geschrieben, danach
  gestrichen bzw. durch date-Werte ersetzt.
- **Falsche Zeilenangaben:** Rocklin "Z. 244-250", "Z. 268-277" und "Z. 289-295" standen falsch (die letzte auch im
  ersten Dossierstand); gestrichen bzw. berichtigt zu 219-226, 271-278 und 288-293.
- **Nachtraeglich praezisiert (Rueckwaertsdurchgang):** Ergebnis 1a sagte zuerst "also erst ungleich grosse
  Dreiecke"; richtig ist: Defizite gibt es auch bei gleichen Dreiecken in 60-Grad-Stufen, stufenlos erst mit
  ungleichen. Ebenso "Einfach gesagt" (Jitterbug-Faktor 5 ist die Geometrie, nicht der Roboter) und die
  Endlage Oktaeder als [L] markiert.
- **Unvollstaendige Ausschluesse:** Eine Unter-grep in RUNDE-37 (*.md, "isotrop") lief ohne die Ausschluesse T8-SOLL-*
  und *KS-1* fuer Dateien. Die Namenspruefung (find, nur Namen) zeigt: solche Dateien gibt es dort nicht.
- **E2 nur ueber Sekundaerquellen:** E2 habe ich ueber Rocklin (Volltext) und Charara (Abstract) gewertet, nicht am
  Kane/Lubensky-Volltext.
- **Nicht selbst gelesen:** Sigl 2021, Chen/Bae/Granick 2011, Guest/Hutchinson 2003 und Sun 2012.
- **Nur Kopfrechnung:** Alle [M] sind ohne Rechner (keine lokale Rechnung); Rechenfehler sind moeglich. Am staerksten
  belastet ist SP8 (F = (R_A + R_B)/2), ungeprueft durch eine zweite Person.
- **Juergensen u. a.:** Die vollstaendige Autorenliste ist nicht notiert, ebenso die Autoren der BeF2-Arbeit.
- **Wegner-PDF:** Die PDF in kopplung-tetra-1/quellen habe ich per pdftotext auf stdout durchsucht (ohne Datei);
  kein Treffer zu Schrumpfen oder Kippung.
- Die Systemvorgabe meiner Rolle verbietet Berichtsdateien; die Karte verlangt DOSSIER.md und ARBEITSFELD.md. Ich bin
  der Karte gefolgt.

## 9. Einfach gesagt

Wenn Dreiecke nur an ihren Spitzen zusammenkleben, entstehen Gelenke: In der Ebene kann sich jedes Paar noch drehen,
im Raum sogar in drei Richtungen, und ein ganzes Netz daraus bleibt beweglich. Ein solches Netz kann "atmen", also
als Ganzes wachsen und schrumpfen, ohne dass sich ein Dreieck verbiegt, sogar wenn die Dreiecke verschieden geformt
sind; der "Jitterbug" aus acht Dreiecken kann so sein Volumen bis auf ein Fuenftel verkleinern und ist als Roboter
schon gebaut. Gleichmaessiges Ein- und Ausatmen allein pumpt aber nichts in eine Richtung, dafuer braucht man eine
Welle, die durch das Netz laeuft, wie bei einer Schlauchpumpe. Verschieden geformte Dreiecke koennen das Netz
einseitig machen: Dann sammeln sich die weichen Stellen an einem Rand, und das Atmen kann diese Seite umschalten. Ob
Finns Tetraedernetz im Raum gleichmaessig in alle Richtungen atmen kann, ist offen; dafuer schlagen wir eine kurze
Rechnung vor.
