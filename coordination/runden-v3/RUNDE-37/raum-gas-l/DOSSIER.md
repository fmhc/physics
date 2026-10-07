# RAUM-GAS-L: Dossier (feldforscher fuer die Leitung claude-primary; Runde 48, Finn-Auftrag "Was ist mit Gasen?")

- Karte KARTE.md bindend, RG1 bis RG5 unveraendert. Zusatz der Leitung (Navier-Stokes, NS1 bis NS3) woertlich in
  ARBEITSFELD.md, Abschnitt 3a; hier Abschnitt 6a.
- Literatur, keine Rechnung. Eigene Rechnungen sind Schreibtisch-Mathematik [M] oder eigene Schluesse [ES].
- **Kennzeichen:** [E] Messung/Rechnung, [M] Mathematik, [S] Fachquelle (Messdaten aus Fachquellen sind [S]),
  [L] Lehrbuch/Gedaechtnis, [H] Hypothese, [P] Projektbefund mit Fundstelle, [ES] eigener Schluss.
  "[S Abstract]" = nur Abstract gelesen; "[S Volltext]" = Stelle im Volltext gelesen (quellen/*.txt, Zeilennummern
  der pdftotext-Fassung).
- Arbeitsfeld: ARBEITSFELD.md (alle Erwartungen mit Zeit vor jedem Abruf). Abrufe: ABRUFE.md. Rohdaten: quellen/.

## 1. Zeiten und Abrufzahl

- Start 2026-10-05 09:42:40 CEST (date). Lokal gelesen bis 09:49:12 (date).
- Abrufe 09:50:04 bis 10:06:43 (date). Zusatz der Leitung aufgenommen 10:02:18 (date).
- Dossier ab 10:17:23 (date) geschrieben. Ende siehe letzte Zeile.
- **20 von 20 Abrufen** (15 + 5 aus dem Zusatz). 17 davon mit Inhalt. Ohne Inhalt blieben drei: F4
  (Syntaxfehler, 0 Treffer), F15 (openai.com, HTTP 403) und F18 (Werkzeug sperrt web.archive.org).
- Zeitbox 60 + 20 min, also bis 11:02:40.

## 2. Ergebnis zuerst

1. **"Scherung oder Kruemmung" ist fuer das ruhende Netz schon entschieden: Kruemmung [P, M].**
   - TT-GLAS-2 fand bei Gamma in jedem Netz genau 6 Nullmoden, die homogenen Verzerrungen des Torus
     (tt-glas-2/ERGEBNIS.md, Abschn. 2.1). Das Netz hat damit keinen statischen Schermodul, genau wie eine
     Fluessigkeit.
   - Trotzdem traegt es masselose TT-Wellen. Flache 2-3-Zuege lassen die Regge-Energie unveraendert
     (umklapp-1/ERGEBNIS.md, Abschn. 2.1). Die Maxwell-k-Luecke greift deshalb nicht direkt.
   - Ein Gas-Netz kann Schwerewellen tragen, wenn die Zuege die Wellenenergie nicht anfassen.
   - Vorbilder in der Literatur:
     - Weltkristall, der durch Versetzungskondensation nematisch wird; die Gravitation wirkt dann zwischen
       Kruemmungsquellen (Kleinert/Zaanen 2004 [S Abstract]).
     - "Dynamisch trianguliert" heisst bei Zufallsflaechen schlicht fluid (Baillie/Johnston 1993 [S Abstract]).
2. **Waeren die Wellen scherartig, muesste die Umordnungszeit tau mindestens etwa eine Milliarde Jahre betragen
   [S + ES].**
   - Maxwell-Querwellen klingen mit exp(-t/(2 tau)) ab [M].
   - LVK GWTC-4.0 misst Xi_0 = 1,4 +1,0/-0,4 [S]. Grob folgt daraus tau >~ 2 bis 4 Gyr, also omega tau >~ 1e19 bei
     100 Hz [ES].
   - Ein Gas aus Netzpunkten auf der Planck-Skala haette tau ~ 1e-43 s [H].
   - Dispersion und Geschwindigkeit geben nur tau >~ 6 h bis ~1 Jahr.
   - Ausgeschlossen ist also das schnelle, scherartige Gas. Ein kruemmungsgetragenes Gas schliessen die Daten nicht
     aus.
3. **Energie am Zug: Die Hydrodynamik kennt das Problem aus TAKT-DYNAMIK-1 seit 2010 und hat eine Loesung [S].**
   - Gewichte an Delaunay-Zellen springen beim Zug. Gewichte an Voronoi-Zellen bleiben stetig, weil die betroffene
     Voronoi-Flaeche genau im Zugmoment Flaeche null hat (Springel 2010; Hess/Springel 2010 [S Volltext]).
   - Woher die Erhaltung kommt:
     - AREPO: aus der Flussform. Dann wird Bewegung in Waerme umgewandelt; Wellen wuerden gedaempft.
     - Hess/Springel: aus einer Lagrange-Funktion mit Voronoi-Volumen.
   - Korn 2026: Eine Massematrix ohne Dichte erzeugt ein Energieresiduum unbestimmten Vorzeichens [S Abstract]. Das
     passt zu Lesart R gegen P in TAKT-DYNAMIK-1.
   - RG4 trifft nur teilweise ein.
4. **Der Raum als Quantenfluessigkeit ist ein bekanntes Forschungsbild, gezeigt ist aber wenig [S].**
   - He-3-A: Quasiteilchen sehen eine wirksame Metrik und Eichfelder. Die Gravitation ist dort bimetrisch mit
     Gravitonmassen, keine Einstein-Dynamik (RG1 trifft ein).
   - GFT-Kondensate: Sie liefern Friedmann-Gleichungen mit Rueckprall. Erste skalare Stoerungen (2025) folgen im
     einfachen Fall nicht der ART. Arbeiten zu Schwerewellen wurden nicht gefunden (RG2 trifft ein).
   - Neu: Volovik deutet 2026 einen masselosen "zweiten Schall" in einem de-Sitter-Zwei-Fluessigkeitsbild als
     Graviton; welcher Typ, ist offen.
   - DT, CDT und Kausalmengen haben keine Gasphase mit flachem Grenzfall und Wellen (RG5 trifft ein).
5. **Navier-Stokes (Zusatz der Leitung) [S, M]:**
   - OpenAI-Manuskript vom 08.09.2026 (166 S.): erzwungener Blow-up aus der Ruhe, mit glatter Kraft.
   - Folgearbeiten ordnen es den Clay-Faellen (C) und (D) zu und behandeln die Kraft als kompakt in Raum und Zeit.
     Damit ist NS1 Teil 2 nach den gelesenen Quellen verfehlt.
   - Den Wortlaut der Organisation konnte ich nicht lesen (HTTP 403).
   - Fuer Finns Netz: Auf einem endlichen Netz mit Energieungleichung gibt es keinen Blow-up (NS2 trifft ein).
   - Eine veroeffentlichte Verbindung dieser Blow-up-Klasse zu emergenter Raumzeit fehlt (NS3 trifft ein). Es gibt
     nur die allgemeine Abbildung zwischen Navier-Stokes und Einstein (2011).

## 3. Erwartungsverstoesse (das Wichtigste zuerst; Protokoll in ARBEITSFELD.md Abschn. 3 und 4)

1. **"Fluessig" ist in DT keine Phase, sondern die Definition (V-F12a).**
   - Bei Baillie/Johnston 1993 stehen "dynamically triangulated (ie fluid)" und kristalline Zufallsflaechen
     nebeneinander. Ein Term mit innerer Kruemmung friert die Zuege ein und fuehrt zum Kristall.
   - Auch Membranmodelle mit Kanten-Zuegen sind fluessige Flaechen mit Biegesteifigkeit (Koibuchi/Shobukhov 2014).
   - Erwartung korrigiert: Finns "Gas" entspricht dem DT-Ensemble selbst; Kristall heisst feste Verknuepfung.
   - [ES] Es gibt zwei Regime:
     - In der gleichseitigen DT aendert jeder Zug die Fehlwinkel, also kann Kruemmung die Zuege bremsen.
     - Im eingebetteten Delaunay-Netz sind flache Zuege kruemmungsfrei (UMKLAPP-1 [P]); dort bremst die
       Regge-Energie nichts.
2. **Erhaltung im Moving Mesh kommt nicht von den Nullflaechen (V-F3a, V-F3b, F10, V-F19a).**
   - AREPO erhaelt Masse, Impuls und Gesamtenergie, weil die Fluesse antisymmetrisch sind. Die Nullflaechen sorgen
     nur fuer Stetigkeit.
   - Die erhaltene Groesse ist Waerme plus Bewegung; kleinskalige Bewegung wird falsch weggedaempft (Springel 2010,
     Z. 1310-1340).
   - Hess/Springel 2010 beschreiben fuer Delaunay-Zellen dieselbe Unstetigkeit wie TAKT-DYNAMIK-1 [ES: Parallele].
     Ihre Abhilfe sind Voronoi-Volumina in einer Lagrange-Funktion.
   - Korn 2026: Ohne Dichte in der Massematrix bleibt ein Residuum unbestimmten Vorzeichens.
3. **Volovik geht seit 2020 ueber die Quasiteilchen-Metrik hinaus (V-F6a, V-F6b, V-F6c).**
   - 2020: superplastischer Vakuumkristall; die Gravitation sind seine elastischen Verformungen.
   - 2021: Higgs-Moden der Tetrade als zwei masselose Wellen.
   - 2026: masseloser "zweiter Schall" als Graviton.
   - Alles Modell oder Deutung.
4. **Die Navier-Stokes-Kraft liegt nach den Folgearbeiten in der Clay-Klasse (V-F17a, V-F20a).**
   - Petrillo/Glimm 2026 ordnen das Ergebnis (C) und (D) zu. Cao/Chi 2026 nennen raumzeit-kompakte Kraefte und die
     Clay-Datenklasse.
   - Das widerspricht NS1 Teil 2.
   - Lei/Ren nennen keinen Clay-Fall und erwaehnen Lean nicht.
5. **Kruemmungsschwankungen zeigen sich als Phasendiffusion, nicht als Daempfung (V-F12b; Cang/Wang 2025).**
   - Daraus folgen zwei Datenspuren: Ein dissipatives Raum-Gas verliert Amplitude, ein energieerhaltendes zeigt
     Phasenrauschen, das mit der Strecke waechst.
6. **GFT-Inhomogenitaeten folgen im einfachen Fall nicht der ART (V-F5a; Gielen/Mickel 2025).**
7. **Simplex-Netze und Wellen (V-F12c).** Ein bestimmter diskreter lorentzscher Simplex-Komplex kann Minkowski nicht
   von einem bestimmten Schwerewellen-Ausbruch unterscheiden (Dowker/Butterfield 2021). Die Autoren werten das als
   Argument fuer Kausalmengen.
8. **Jedes Netz waehlt ein Bezugssystem (V-F1a).**
   - Bombelli/Henson/Sorkin: Ein Graph endlicher Valenz auf einer Punktstreuung ist nie Lorentz-vertraeglich.
   - Ein Gas-Netz hat ausserdem ein Ruhesystem, wirkt also wie ein Aether [ES]. Die Aether-Kopplung ist durch
     GW170817 beschraenkt: |c13| <= 1e-15.
9. **Zwei weitere Manuskripte (V-F20b, V-F16a).**
   - OpenAI hat am selben Tag ein Manuskript zum ungezwungenen Euler-Blow-up veroeffentlicht (57 S.).
   - Alpoege/Buckmaster haben vorher einen erzwungenen Euler-Blow-up auf R^3 gezeigt.
10. **Kleinere Verstoesse:**
    - Hess/Springel-Abstract nennt kuenstliche Viskositaet und Ordnungskraefte (V-F9a).
    - Eine Maxwell-gedaempfte Schwerewellen-Theorie existiert, im Abstract ohne Daten (Carcione/Ba 2024, V-F11a).
    - Kleinerts Weltkristall mit zweiter Gradientenelastizitaet ist nicht auf arXiv (V-F14a).
    - Zwei Abstract-Details (V-F1b, V-F1c).

## 4. Je Frage der Karte: Stand mit Belegen

### 4.1 Raum als Quantenfluessigkeit bzw. Kondensat

| Ansatz | Gezeigt (im Modell) | Nur gedeutet bzw. Programm | Beleg |
|---|---|---|---|
| He-3-A (Volovik) | Weyl-Fermionen, Eichfelder, wirksame Metrik fuer Quasiteilchen; Fermionen und Eichbosonen sehen dieselbe Metrik; Gravitation bimetrisch mit Gravitonmassen; lambda planckgross, Vakuumterm im Gleichgewicht null | Standardmodell als effektive Theorie; Gleichgewichtsvakuum gravitiert nicht | Volovik 2001 [S Abstract]; Jannes/Volovik 2012 [S Abstract] |
| Neuere Volovik-Bilder | - | Vakuum als superplastischer Kristall (2020); Tetrade als Ordnungsparameter, ihre Higgs-Moden in der ART als zwei masselose Wellen, in He-3-B massiv (2021); masseloses Graviton als "zweiter Schall" in de Sitter, Typ offen (2026) | Volovik 2020, 2021, 2026 [S Abstract]; Zubkov 2019 [S Abstract] |
| GFT-Kondensate | Friedmann-Gleichungen mit Rueckprall als Hydrodynamik einfacher Kondensate (Gross-Pitaevskii-Regime); anisotrope Kondensate werden spaet isotrop | Universum als Kondensat von Quanten-Simplizes, "Hydrodynamik auf dem Superraum" | Oriti/Sindoni/Wilson-Ewing 2016; Oriti/Wang 2023; Oriti 2024 [S Abstract] |
| GFT-Stoerungen | skalare Stoerungen mit rekonstruierter Metrik: im einfachen Fall nicht ART-artig (eine Modenart euklidisch, die andere mit anderen Gleichungen) | - | Gielen/Mickel 2025 [S Abstract] |
| GFT gegen Daten | GFT-Dunkelenergie gegen DESI DR2 + Pantheon+: mit Stoerungs-Priors nahe Lambda-CDM | - | Tsedrik u. a. 2026 [S Abstract] |
| ART als Hydrodynamik | - | Raumzeit als Kondensat; Quantisierung der ART gaebe nur Phononen-Physik | Hu 2005 [S Abstract] |
| Thermodynamik der Raumzeit | Einstein-Gleichung aus delta Q = T dS an lokalen Horizonten (unter Annahmen); mit Nichtgleichgewicht: Horizont-Scherviskositaet als Entropieproduktion | Einstein-Gleichung als Zustandsgleichung, wie Schall in Luft | Jacobson 1995; Eling/Guedens/Jacobson 2006 [S Abstract] |
| Weltkristall / Quanten-Nematik | Modell: Kondensation von Versetzungen -> nematische Phase, keine Torsion, Gravitation zwischen Kruemmungsquellen; Beziehung Quanten-Nematik zu linearisierter Gravitation | Raum als Fluessigkristall | Kleinert/Zaanen 2004; Zaanen/Beekman 2012 [S Abstract] |
| BEC-Analogmodell | Gravitation als modifizierte Poisson-Gleichung, Reichweite = Heilungslaenge; nicht Einstein | Lehren fuer emergente Gravitation | Girelli/Liberati/Sindoni 2008 [S Abstract] |
| Grenzen | Dissipation, die aus einem Kondensat-Raum folgt, ist fuer Materie astrophysikalisch stark beschraenkt; Hindernisse fuer emergente Gravitation | - | Liberati/Maccione 2014; Carlip 2014 [S Abstract] |

- **Gegensweep im 24-Monats-Fenster (F13):** keine gezielte neue Gegenarbeit zu Volovik- oder Kondensatbildern
  gefunden. Methodisch einschlaegig ist nur Tuveri 2026: Wer die ART zurueckgewinnen will, braucht neben Metrik und
  Dynamik auch Messbarkeitsbedingungen. Urteil "nach Recherchestand keine neue Gegenarbeit", nicht "unbestritten".

### 4.2 Querwellen in Fluessigkeiten und Schwerewellen

- **Maxwell-Viskoelastik [M]** (ARBEITSFELD K1):
  - Aus sigma_t + sigma/tau = G v_x und rho v_t = sigma_x folgt omega^2 + i omega/tau = c^2 k^2 mit c^2 = G/rho.
    Also omega = -i/(2 tau) +- sqrt(c^2 k^2 - 1/(4 tau^2)).
  - Querwellen laufen nur fuer k > k_g = 1/(2 c tau). Sie klingen mit exp(-t/(2 tau)) ab, unabhaengig von k.
  - v_Phase < c, v_Gruppe > c. Fuer k < k_g bleibt Scherdiffusion mit nu = c^2 tau = eta/rho.
  - In der Literatur heisst das k-Luecke, aus dem Maxwell-Frenkel-Ansatz und an Dissipation gebunden
    (Baggioli/Brazhkin/Trachenko/Vasin 2020 [S Abstract]).
- **Gilt das fuer Schwerewellen in einem fluessigen Netz? Kette aus Bausteinen [P, M, ES]:**
  1. Ein Festkoerper speichert Energie ~ mu eps^2 (Dehnung ohne Ableitung). Die Welle der ART speichert ~ (d h)^2,
     also eine Ableitung der Dehnung. Homogene Scherung kostet in der ART nichts: flach bleibt flach (K3).
  2. Finns Netz verhaelt sich so: 6 Nullmoden = homogene Verzerrungen, kein statischer Schermodul
     (TT-GLAS-2 [P]). Die TT-Zweige sind trotzdem masselos.
  3. Flache 2-3-Zuege aendern die Regge-Energie nicht (UMKLAPP-1 [P]). Eckverschiebungen im Flachen sind
     Eichrichtungen. Mit Kruemmung gibt es auf dem Gitter keine exakte Eichsymmetrie mehr
     (Bahr/Dittrich 2009 [S Abstract]).
  4. Folge [ES]: Maxwells Mechanismus (Umordnung loescht das Gedaechtnis der Scherspannung) findet in der
     potentiellen Energie nichts zu loeschen.
     - Kopplung bleibt nur ueber die Bewegungsenergie am Zug (TAKT-DYNAMIK-1: Sprung 0,2 bis 0,46 % je Zug [P]).
     - Dazu kommt der 3-2-Zug an gekruemmten Kanten (Rest von der Ordnung des Fehlwinkels [P]).
- **Antwort auf Frage 2:**
  - Die Kruemmungs-Rueckstellkraft entkoppelt von der k-Luecke, soweit die Zuege flach sind und die Traegheit am Zug
    stetig ist.
  - Wo das nicht gilt, wirkt jeder Zug wie ein Stoss, der Wellenenergie umverteilt.
  - Ob daraus Daempfung oder Phasenrauschen wird, haengt an der Energieregel am Zug. In TAKT-DYNAMIK-1 daempft
    Lesart R, Lesart P verstaerkt [P].
- **Gegenlinie [S Abstract]:**
  - Carcione/Ba 2024 formulieren Schwerewellen als viskoelastische SH-Wellen mit Maxwell-Daempfung.
  - Gamble/Flurchick 2017 fassen die Raumzeit als viskoelastisches Kontinuum.
  - Datenvergleiche stehen in keinem der beiden Abstracts.

### 4.3 Daten

- Zahlen und Stellen: Datentabelle in Abschnitt 5.
- **Kern [S]:**
  - Geschwindigkeit: GW170817 + GRB 170817A ergeben -3e-15 <= Delta v/c <= +7e-16.
  - Amplitude gegen Entfernung (modifizierte Ausbreitung): Xi_0 = 1,4 +1,0/-0,4 (GWTC-4.0).
  - Dispersion: m_g <= 1,92e-23 eV/c^2 (GWTC-4.0). PTA: NANOGrav 15 Jahre <~ 8,6e-24 eV, MeerKAT 2,10e-23 eV.
  - Aether: |c13| <= 1e-15.
- **Ausdrueckliche Schranken auf "Viskositaet der Raumzeit" fuer Schwerewellen** gibt es nach Recherchestand nicht.
  - Es gibt Schranken auf die Viskositaet kosmischer Medien (Regime "Medium im Raum"). Die Daempfungsrate ist dort
    proportional zu G eta (Goswami u. a. 2017 [S Abstract]; die Zahl der Schranke ist nicht gelesen).
  - Keine Arbeit verbindet die k-Luecke mit LIGO- oder PTA-Daten (F11). Die tau-Folgerungen unten sind deshalb
    meine [ES].
- **Folge fuer tau** (nur wenn die Wellen scherartig waeren):
  - Die Amplitude verlangt tau >~ Gyr.
  - Dispersion und Geschwindigkeit verlangen nur tau >~ 1e4 bis 4e7 s.
  - Die Daempfung ist also die schaerfste Spur, um 9 (gegen m_g) bis 13 (gegen die Geschwindigkeit) Zehnerpotenzen.
- **Gegensweep-Befund:**
  - Der Mittelwert Xi_0 = 1,4 liegt auf der Seite einer Daempfung. Die ART liegt genau am unteren Rand des
    68-%-Intervalls.
  - Das ist kein Signal, denn der Wert haengt vom Populationsmodell ab. Er gehoert aber hierher, nicht in eine
    Fussnote.

### 4.4 Verfahren: Moving Mesh

- **AREPO (Springel 2010, [S Volltext]):**
  - Voronoi-Gitter aus frei bewegten Punkten. Die Delaunay-Zerlegung aendert sich sprunghaft, die
    Voronoi-Zerlegung stetig. Beim Nachbarwechsel schrumpft die Voronoi-Flaeche auf null (Z. 608-620; Z. 209).
  - Erhaltung kommt aus F_ij = -F_ji (Gl. 13, Z. 861-875). Ohne Gravitation bleibt Waerme plus Bewegung auf
    Maschinengenauigkeit erhalten (Z. 1957-1962).
  - Mit Eigengravitation erhaelt das Standardschema Masse und Impuls, die Gesamtenergie aber nicht ausdruecklich
    (Z. 2106-2107).
  - Falsche Dissipation in kaltem Gas (Z. 1310-1340).
- **Voronoi-Teilchen (Hess/Springel 2010, [S Volltext]):**
  - Bewegungsgleichungen aus einer diskreten Lagrange-Funktion, Massen je Teilchen fest (Z. 90-93).
  - Delaunay-Zellvolumina koennen bei unendlich kleiner Bewegung endlich springen. Dann ist die Energie unstetig,
    das Verfahren ungeeignet (Z. 183-197).
  - Voronoi-Volumina sind stetig, weil Zuege genau bei Flaeche null passieren (Z. 195-200).
  - Mit Formkraeften in der Lagrange-Funktion bleiben Energie, Impuls und Entropie genau erhalten (Z. 606-609).
  - Kuenstliche Viskositaet braucht man nur fuer Stoesse (Abstract).
- **DEC-Fluide:**
  - Mohamed/Hirani/Samtaney 2016: NS auf Simplizial-Flaechen; Masse und Wirbelstaerke auf Maschinengenauigkeit;
    kinetische Energie mit Fehler zweiter Ordnung [S Abstract].
  - Korn 2026a: inkompressibles NS/Euler auf Delaunay-Voronoi-Netzen. Energie- und Kelvin-Erhaltung; diskret ist
    Energieerhaltung Stabilitaet [S Abstract].
  - Korn 2026b: kompressibel. Ohne Dichte in der Massematrix bleibt ein O(h^2)-Residuum unbestimmten Vorzeichens.
    Die dichtegewichtete Massematrix stellt die exakte Energie her [S Abstract].
- **Was Finns Netz uebernehmen kann [ES]:**
  1. Zuege genau im Moment der Ko-Sphaerizitaet ausfuehren. TAKT-DYNAMIK-1 tut das schon (Bisektion [P]).
  2. Traegheit auf duale Masse legen (umkreisbasierte *1-, *2-Gewichte bzw. Voronoi-Volumina), nicht auf
     Tetraeder.
     - Dann ist die Bewegungsenergie am 2-3-Zug stetig (vorab ableitbar, Abschn. 8).
     - Das ist schaerfer als A2 in HODGE-MASSE-1 (Volumen je Tetraeder). Tetraedervolumina springen am Zug, ausser
       bei gleichmaessiger Verzerrung.
  3. Die Bewegungsgleichungen aus einer Lagrange-Funktion ableiten, kein Godunov- oder Fluss-Verfahren. Ein
     Flussverfahren erhaelt nur die Gesamtenergie samt Waerme und wuerde Wellen daempfen.
  4. Ordnungsregel beibehalten: Delaunay als Auswahlregel (TAKT-DYNAMIK-1 [P]); Voronoi-Teilchen brauchen
     Formkraefte.

### 4.5 Phasen in DT, CDT und Kausalmengen

- **DT:**
  - Dynamisch trianguliert heisst in der Flaechenliteratur fluid; ein Term mit innerer Kruemmung friert die Zuege
    ein (Baillie/Johnston 1993 [S Abstract]).
  - Phasen der 4D-DT: Knaeuel bei kleinem kappa0, verzweigte Polymere (d_H = 2) bei grossem
    (WELTKRISTALL-L, BABY-UNIVERSUM-L 4.6 [P]). Beide sind nicht flach.
  - 3D: Budd/Nemeth 2025, dritte "triple-tree"-Phase [P].
- **CDT:**
  - 3D-Starkkopplungsphase "foam of baby universes" [P].
  - 4D de-Sitter-Phase: ausgedehnt, aber nicht flach.
  - Kruemmung-Kruemmung-Korrelatoren passen zu einem massiven Zustand (Geon-Hinweis; Maas/Plaetzer/Pressler 2025
    [S Abstract]). Masselose Wellen sind nicht gezeigt.
- **Kausalmengen:**
  - 2D: Kontinuumsphase gegen Kristallphase (Surya 2012 [S Abstract]).
  - Poisson-Streuung waehlt kein Bezugssystem, ein Graph endlicher Valenz darauf schon (Bombelli/Henson/Sorkin
    [S Abstract]).
  - Dowker/Butterfield 2021: Ein bestimmter Simplex-Komplex unterscheidet Minkowski nicht von einem bestimmten
    Wellenausbruch [S Abstract].
- **24-Monats-Suche (F12):** keine Phase "Gas" mit flachem, isotropem Grenzfall und Schwerewellen.

### 4.6 Regime und Moderatoren

| Regime | Was ist das Medium? | Rueckstellkraft der Welle | Daempfung | Beleg |
|---|---|---|---|---|
| I Medium im Raum | Stoff fuellt die Raumzeit, Einstein-Dynamik bleibt | Kruemmung (ART) | ideale Fluessigkeit keine, Scherviskositaet ~ G eta; Festkoerper gibt Gravitonmasse | Goswami u. a. 2017; Dubovsky 2004 [S Abstract] |
| II Medium = Raum, Welle scherartig | Netz/Kristall, dessen Verschiebungen die Welle sind | Scherung (mu eps^2) | Maxwell: exp(-t/(2 tau)), k-Luecke | Carcione/Ba 2024 [S Abstract]; K1 [M] |
| III Medium = Raum, Welle kruemmungsartig | Finns Netz (Regge) | Kruemmung ((d h)^2), kein statischer Schermodul | nur ueber Kopplung am Zug | TT-GLAS-2, UMKLAPP-1 [P]; Kleinert/Zaanen 2004 [S Abstract] |
| IV Analogmodell | Quasiteilchen in He-3/BEC | wirksame Metrik, Dynamik nicht Einstein | Dissipation an Planck-Skala | Volovik; GLS 2008; Liberati/Maccione 2014 [S Abstract] |
| V Holographie (fluid/gravity) | Fluessigkeit am Rand, Gravitation im Inneren | - | Scherviskositaet am Horizont | Bredberg u. a. 2011; Eling/Guedens/Jacobson 2006 [S Abstract] |

- **Moderatoren:**
  - omega tau: Bei > 1 laufen Scherwellen gedaempft, bei < 1 laufen keine.
  - Ob Zuege flach sind: In der eingebetteten Delaunay-Variante ja, in der gleichseitigen DT nein.
  - Gewicht der Traegheit: Tetraeder springt, dual ist stetig.
  - Energieregel am Zug: R oder P.
  - Dissipativ oder konservativ: Das entscheidet, ob man Daempfung oder Phasendiffusion sieht.

### 4.7 Unterscheidungspunkte

| Erklaerungspaar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| Scherartig (II) gegen kruemmungsartig (III) | statisch: Energie homogener Verzerrung bei k -> 0 (II > 0, III = 0); dynamisch: k-Luecke bei k_g = 1/(2 c tau) und Daempfung 1/(2 tau) nur in II | statisch schon gemessen (TT-GLAS-2: III); in Daten fuer tau >~ Gyr nicht unterscheidbar |
| Dissipatives gegen konservatives Raum-Gas | Amplitudenverlust exp(-T/(2 tau)) gegen Phasenvarianz linear in der Strecke | Amplitude: Standardsirenen (heute grob); Phase: fuer Planck-Skala weit unter Empfindlichkeit (Cang/Wang 2025) |
| Gas-Netz mit Ruhesystem gegen Lorentz-neutrales Netz | Richtungs- bzw. Bezugssystem-Abhaengigkeit der Spin-2-Geschwindigkeit | |c13| <= 1e-15 (Oost u. a. 2018); Doppelpulsare (Gupta u. a. 2021) |
| Kleine Gravitonmasse gegen k-Luecke | Vorzeichen von A_0 (Gravitonmasse: v_Gruppe < c; k-Luecke: v_Gruppe > c) | nur mit Schranken fuer beide Vorzeichen; im GWTC-4.0-Abstract nur m_g |
| Tetraeder- gegen duales Traegheitsgewicht | Energiesprung am 2-3-Zug; Lesart R gegen P | im Netz rechenbar (GAS-NETZ-1), nicht in Daten |

## 5. Datentabelle

Folge fuer tau: nur unter der Annahme "Welle scherartig, Maxwell" [ES]. Fuer kruemmungsartige Wellen folgt aus keiner
Zeile ein tau.

| Groesse | Schranke | Quelle mit Stelle | Folge fuer tau [ES] |
|---|---|---|---|
| Geschwindigkeit (GW170817, ~100 Hz, ~40 Mpc [L]) | -3e-15 <= Delta v/c <= +7e-16 | Abbott u. a. 2017, ApJL 848, L13, Abstract (1710.05834) | v_Gruppe - c ~ c/(8 (omega tau)^2) <= 7e-16 c -> omega tau >= 1,3e7, tau >= 2,1e4 s (~6 h) |
| Amplitude gegen Entfernung, Xi_0 (dunkle Sirenen, bis z ~ 1) | 1,4 +1,0/-0,4 (68,3 %); 1,4 +2,8/-0,6 (90 %); ART = 1 | LVK 2025/26, GWTC-4.0 Kosmologie, Abstract (2509.04348; ApJL 1007) | d_GW/d_EM = exp(T/(2 tau)); bei z ~ 0,5 (T ~ 5 Gyr [L]) Verhaeltnis <= ~1,8 (68 %) -> tau >~ 4 Gyr; 90 %: tau >~ 2,4 Gyr. Xi_0-Form passt nicht genau zu konstanter Daempfung: nur Groessenordnung |
| Gravitonmasse (LVK) | m_g <= 1,92e-23 eV/c^2 (90 %) | LVK 2026, GWTC-4.0 Tests II, Abstract (2603.19020) | wenn k-Luecke wie |m|: tau >= hbar/(2 m_g c^2) = 1,7e7 s; Vorzeichen verschieden, nur Groessenordnung |
| Gravitonmasse (NANOGrav 15 J.) | m_g <~ 8,6e-24 eV (90 %) | Wang/Zhao 2024, PRD 109, L061502, Abstract (2307.04680) | tau >~ 3,8e7 s (~1,2 J.), gleiche Einschraenkung |
| Gravitonmasse (MeerKAT-PTA 4,5 J.) | m_g < 2,10e-23 eV/c^2 (90 %) | Zhao/Wang 2026, Abstract (2607.14790) | tau >~ 1,6e7 s, gleiche Einschraenkung |
| Dispersion, Doppelbrechung (LVK) | keine Abweichung | 2603.19020, Abstract | - |
| Aether-Kopplung | |c13| <= 1e-15 | Oost/Mukohyama/Wang 2018, PRD 97, 124023, Abstract (1802.04303) | kein tau; das Ruhesystem eines Gas-Netzes darf die Spin-2-Geschwindigkeit nicht sichtbar aendern |
| Viskositaet kosmischer Medien (Regime I) | Daempfungsrate ~ G eta; Zahl nicht gelesen | Goswami u. a. 2017, PRD 95, 103509, Abstract (1603.02635) | nur Regime I |
| Phasendiffusion durch Kruemmungsschwankungen | Planck-Skala weit unter heutiger Empfindlichkeit | Cang/Wang 2025, Abstract (2512.02782) | konservatives Gas: noch keine Schranke |
| Planck-Dissipation der Materie (Regime IV) | "strong constraints" (Zahl nicht gelesen) | Liberati/Maccione 2014, PRL 112, 151301, Abstract (1309.7296) | betrifft Materie, nicht Wellen |

## 6. Urteile RG1 bis RG5 (nach Kartenwortlaut)

| Nr | Urteil | Beleg |
|---|---|---|
| RG1 | **eingetroffen** (Teil 2 nur indirekt) | Teil 1: Volovik 2001; Jannes/Volovik 2012 (Fermionen und Eichbosonen am Weyl-Punkt sehen dieselbe Metrik) [S Abstract]. Teil 2: in He-3-A bimetrische Gravitation mit Gravitonmassen, lambda planckgross (Jannes/Volovik 2012) -> keine Einstein-Dynamik von selbst. Regel 7: Volovik-Arbeiten bis 2026 durchgesehen (F6); keine behauptet Einstein-Dynamik in He-3-A. Neuere Bilder ausserhalb He-3-A deuten masselose Wellen (2021, 2026) |
| RG2 | **eingetroffen** | Teil 1: Oriti/Sindoni/Wilson-Ewing 2016 (Friedmann + Rueckprall). Teil 2: F5 (35 Treffer, 7 im 24-Monats-Fenster): keine Arbeit zu Tensorstoerungen bzw. Schwerewellen; Stoerungen in Anfaengen und im einfachen Fall nicht ART-artig (Gielen/Mickel 2025); Rueckwirkung bzw. Materiekopplung erst in Anfaengen (2508.16194, 2608.12003, nur Titel/Abstract) |
| RG3 | **teilweise eingetroffen** | Teil 1 (Schranken aus beobachteten Signalen): ja, als Amplitude gegen Entfernung (Xi_0), Geschwindigkeit, Dispersion (m_g, auch PTA); als "Viskositaet" nur fuer Medien im Raum (Goswami u. a. 2017). Teil 2 (stark genug): Fuer scherartige Wellen schliessen sie tau zwischen einer Schwingungsdauer und ~1 Gyr aus (meine Uebersetzung [ES], keine Literaturschranke; F11). Ein Gas mit tau >~ Gyr ist nicht ausgeschlossen. Liest man "Umordnungszeit ueber einer Schwingungsdauer" als "alle tau > T", trifft Teil 2 nur fuer den Bereich bis ~Gyr zu |
| RG4 | **teilweise eingetroffen** | "exakt": AREPO erhaelt Masse, Impuls und Gesamtenergie (Waerme + Bewegung) auf Maschinengenauigkeit ohne Gravitation; mit Eigengravitation die Energie nicht ausdruecklich. Voronoi-Teilchen (Lagrange): Energie, Impuls, Entropie genau erhalten. "weil die Flaechen durch null gehen": falsch fuer AREPO (Grund: F_ij = -F_ji); richtig fuer die Stetigkeit des Gitters und, ueber die Lagrange-Form, fuer die Stetigkeit der Energie bei Hess/Springel. Wellen- bzw. Bewegungsenergie wird in AREPO teils in Waerme gewandelt (Springel 2010, Z. 1310-1340, 1957-1962, 2106-2107; Hess/Springel 2010, Z. 195-200, 606-609 [S Volltext]) |
| RG5 | **eingetroffen** (nach Recherchestand, 24 Monate) | F12 und Projektbefunde: DT-Phasen Knaeuel/Polymer nicht flach [P]; CDT de Sitter nicht flach, Wellen-Korrelatoren eher massiv (Maas u. a. 2025); Kausalmengen 2D Kontinuum gegen Kristall, ohne Wellen (Surya 2012). Einschraenkung: In DT ist "fluid" das ganze Ensemble, nicht eine Phase (Baillie/Johnston 1993) |

## 6a. Navier-Stokes (Zusatz der Leitung; RG6 = NS1 bis NS3)

**Was behauptet bzw. gezeigt ist (an gelesenen Quellen):**

- **Manuskript:** OpenAI, "Finite Time Blowup for Navier-Stokes", veroeffentlicht am 8. September 2026, 166 Seiten.
  Belegt nur ueber die Literaturangabe [21] bei Lei/Ren 2026 [S Volltext]; keine Adresse dort, nicht auf arXiv
  gefunden.
  - Am selben Tag erschien ein zweites OpenAI-Manuskript, "Finite Time Blowup for the Euler Equation" (57 S.). Nach
    Lei/Ren zeigt es einen ungezwungenen Euler-Blow-up aus glatten, kompakt getragenen Daten.
  - Vorher (Preprint 2026) zeigten Alpoege/Buckmaster einen erzwungenen Euler-Blow-up auf R^3 (ebd., Ref. [2]).
- **Inhalt, soweit aus Folgearbeiten belegbar:**
  - 3D, inkompressibel, mit axialsymmetrischem Wirbelkern (Lei/Ren, Z. 228 [S Volltext]).
  - Start aus der Ruhe auf R^3 mit raumzeit-kompakten, glatten Kraeften (Cao/Chi 2026 [S Abstract]).
  - In der Weiterkonstruktion aus der OpenAI-Loesung bleibt die Kraft durch die Blow-up-Zeit glatt; solche Kraefte
    sind auf T^3 und R^3 dicht in relativem L^1_t H^s_x genau fuer s < 1/2 (Cao/Chi/Nie 2026 [S Abstract]).
  - Kraft C-unendlich, aber am Singularpunkt weder verschwindend noch reell-analytisch (Constantin/Ignatova/Vicol 2026
    [S Abstract]).
  - Beschraenkte Energie: nur aus Presse-Suchtext und aus einer anderen Rahmenarbeit (Liu 2026), nicht am Manuskript
    belegt.
- **Fefferman-Fall:**
  - Petrillo/Glimm 2026 ordnen die Ergebnisse vom 7. und 8. September den Faellen (C) und (D) zu; (A) und (B) seien
    offen [S Abstract].
  - Lei/Ren nennen das Werk einen grossen Fortschritt beim Millennium-Problem, ordnen es aber keinem Fall zu.
  - Dass OpenAI selbst "nicht genau das Preisproblem" sagt, stammt aus der Leitungs-Suche. Hier ist es ungelesen
    (403), der Grund bleibt unbekannt.
  - Moegliche Gruende [H]: die Preisregeln (Veroeffentlichung, Frist), oder der "Geist" des Problems (ohne Kraft).
    Keiner ist belegt.
- **Lean:**
  - Nur der Presse-Suchtext nennt eine Lean-Formalisierung. Lei/Ren erwaehnen Lean nicht (0 Treffer im Volltext).
  - Petrillo/Glimm haben eigene Lean-4-Saetze, ohne ein NS-Objekt in der Bibliothek.
  - Lean-Code selbst: nicht gefunden.
- **Pruefung und Kritik:**
  - Lei/Ren bauen den Profilteil unabhaengig und lesbar nach (Teil I). Teil II (Restkorrektur) ist angekuendigt.
  - Constantin/Ignatova/Vicol zeigen eine Grenze des Mechanismus (analytische Kraft -> regulaer). Das ist keine
    Widerlegung.
  - Duraiswami 2026 prueft physikalisch [S Abstract]:
    - Die Kegelbedingung verlangt Radien der Ordnung 10^20.
    - Echte Fluessigkeiten kavitieren bzw. bilden vorher Stoesse.
  - Cao/Chi und Cao/Chi/Nie behandeln die Konstruktion als gesichert.
  - Die Presse berichtet von einem Streit um Urheberschaft. Das ist nur ein Hinweis, nicht gelesen.

**Passt es zu Finns Modell? [H, ES]**

- **(a) Endliches Netz:**
  - Vorab ableitbar [M]: Ein endliches ODE-System mit lokal Lipschitz-stetiger rechter Seite und Energieungleichung
    explodiert nicht in endlicher Zeit. Voraussetzung: energieneutrale Advektion.
  - Literatur:
    - Korn 2026b beweist globale Wohlgestelltheit fuer das dichtegewichtete DEC-Verfahren (d = 2, 3) und zeigt, dass
      naive Massematrizen ein Energieresiduum unbestimmten Vorzeichens tragen [S Abstract].
    - Abgeschnittenes Euler thermalisiert: Energie staut sich zwischen einer Uebergangs- und der Hoechst-Wellenzahl
      und wirkt als Dissipation auf grosse Skalen (Cichowlas u. a. 2005; Murugan/Ray 2023 [S Abstract]).
    - Petrillo/Glimm: Keine endliche Rechnung bezeugt eine Galerkin-gleichmaessige Obergrenze. In ihrem Test bricht
      die Kaskade an der Kolmogorov-Wellenzahl.
  - Also: Eine Kontinuums-Singularitaet erscheint auf dem Netz als Kaskade bzw. Thermalisierung an der Netzweite.
    Pruefung bestaetigt, mit Literatur.
- **(b) DEC-Navier-Stokes:**
  - Es gibt sie auf Simplizialnetzen: Mohamed/Hirani/Samtaney 2016 fuer Flaechen; Korn 2026a/b auf
    Delaunay-Voronoi-Netzen, auch 3D; hybrid 3D bei Abukhwejah u. a. 2024 [S Abstract].
  - Der zaehe Term wirkt dort auf die Geschwindigkeit als 1-Form, ueber den Hodge-Laplace auf 1-Formen [L].
  - Folge fuer ein Gas-Netz [ES]:
    - Waere Finns Netz selbst ein zaehes Fluid, braeuchte es eine Geschwindigkeits-1-Form auf den Kanten und den
      1-Formen-Laplace mit denselben umkreisbasierten Hodge-Sternen *1 und *2. Das sind genau die Gewichte, die am
      Delaunay-Zug stetig sind (Abschn. 4.4).
    - Finns Takt (8 mal Hodge-Laplace auf 0-Formen, TAKT-UMKLAPP-1 laut Leitung [P]) ist ein anderer Operator.
    - Fuer die Schwerewellen selbst ist kein zaeher Term noetig. Die Daten verlangen, dass er praktisch fehlt
      (Abschn. 5).
- **(c) Verbindungen:**
  - Zu Turbulenz-Kaskaden ja: Cheskidov/Dai/Palasek 2026 (Kaskaden-Mechanismen, Vergleich mit OpenAI);
    Schorlepp/Rosenhaus/Falkovich 2026 (Wirbel-Instanton aehnlich zum OpenAI-Mechanismus); Petrillo/Glimm
    (Onsager-Fluss).
  - Zu emergenter Raumzeit, akustischer Metrik oder Quantengravitation: fuer diese Blow-up-Klasse nichts gefunden
    (F17, F19).
  - Allgemein gilt: Jede Loesung des inkompressiblen NS in p+1 Dimensionen hat eine duale Vakuum-Einstein-Loesung in
    p+2 Dimensionen (Bredberg/Keeler/Lysov/Strominger 2011 [S Abstract]). Auf den Blow-up angewandt hat das niemand.
  - SOC: nicht gesucht.
- **Physikalische Einordnung [ES]:**
  - Der Blow-up ist eine Aussage ueber das Geschwindigkeitsfeld einer Fluessigkeit im Kontinuum, mit starker
    nichtlinearer Wirbelstreckung.
  - Schwerewellen mit h ~ 1e-21 sind linear. In Finns Netz waere das "Gas" der Raum selbst, nicht eine Fluessigkeit
    darin.
  - Ein direkter Bezug ist nicht belegt.

| Nr | Vorhersage (Leitung) | Urteil | Beleg |
|---|---|---|---|
| NS1 | Bewiesen ist ein Blow-up mit Kraft fuer inkompressibles 3D-NS; die Kraft erfuellt die Abklingbedingungen des Preisproblems nicht (55 %) | **teilweise eingetroffen** | Teil 1: behauptet im OpenAI-Manuskript; Profilteil unabhaengig nachgebaut, Teil II offen; Folgearbeiten behandeln es als gesichert (Lei/Ren; Cao/Chi). "Bewiesen" im strengen Sinn (vollstaendige unabhaengige Pruefung) ist noch nicht belegt. Teil 2 nach gelesenen Quellen **verfehlt**: raumzeit-kompakte, glatte Kraefte, Clay-Datenklasse, Faelle (C) und (D) (Cao/Chi; Cao/Chi/Nie; Petrillo/Glimm). OpenAI-Wortlaut ungelesen |
| NS2 | Auf einem endlichen Netz gibt es keine Singularitaet; vorab ableitbar (85 %) | **eingetroffen**, mit Bedingung | [M] mit Energieungleichung bzw. energieneutraler Advektion; Korn 2026b: globale Wohlgestelltheit fuer das dichtegewichtete Verfahren, Residuum unbestimmten Vorzeichens sonst |
| NS3 | Eine veroeffentlichte Verbindung zu emergenter Raumzeit bzw. Quantengravitation gibt es nicht (70 %) | **eingetroffen** (fuer diese Blow-up-Klasse, nach Recherchestand) | F17 (>= 10 Folgearbeiten, alle Mathematik bzw. Fluid) und F19: keine. Allgemeine NS-Einstein-Abbildung existiert (Bredberg u. a. 2011), nicht auf die Klasse angewandt |

## 7. Bedeutung fuer Finns Netz [H]

**Was muesste ein Gas-Netz koennen?**

1. Punkte bewegen sich frei; Zuege nur genau im Delaunay-Moment (Ko-Sphaerizitaet), nur flache Zuege. Dann ist die
   Regge-Energie blind fuer das Fliessen (UMKLAPP-1 [P]).
2. Traegheit auf dualen Massen (Voronoi bzw. umkreisbasiert), aus einer Lagrange-Funktion. Dann ist die Energie am
   2-3-Zug stetig, und Lesart R und P fallen zusammen (Abschn. 8).
3. Keine Flussform mit Waermespeicher. Sonst wird Wellenenergie zu Netz-Waerme (AREPO-Lehre).
4. Eine Ordnungsregel (Delaunay) gegen schlechte Zellen. Ohne sie wachsen Moden (TAKT-DYNAMIK-1 [P]).
5. Den Rest am 3-2-Zug an gekruemmten Kanten klein halten. Dort wirkt der Fehlwinkel der Welle (TAKT-DYNAMIK-1 TD0
   [P]); seine Wirkung auf lange Strecken muss unter den Datenschranken bleiben, als Daempfung (Xi_0) wie als
   Phasenrauschen.
6. Das Ruhesystem des Gases darf die TT-Geschwindigkeit nicht aendern (|c13| <= 1e-15).

**Ist "Scherung oder Kruemmung" entscheidbar?** Ja, an drei Stellen.

- **Statisch, bei k -> 0:** Kostet homogene Verzerrung Energie? Gemessen: nein, also Kruemmung (TT-GLAS-2 [P]).
- **Dynamisch, am Zug:** Verschwindet der Energiesprung mit dualer Traegheit?
  - Wenn ja, ist das Gas-Netz kruemmungsgetragen und dynamisch vertraeglich.
  - Wenn ein systematischer Sprung bleibt, wirkt jeder Zug wie Maxwell-Relaxation, und die Daten verlangen
    tau >~ Gyr.
  - Rechenbar mit GAS-NETZ-1.
- **In Daten:**
  - Dissipativ: Amplitudenverlust. Konservativ: Phasendiffusion.
  - Ein langsames Gas (tau >~ Gyr) ist von einem festen Netz empirisch nicht unterscheidbar. Das sage ich so,
    statt eine Seite zu bevorzugen.

**Zur Lesart:** Die Literatur kennt das Gas aus Tetraedern in zwei anderen Formen [S Abstract].

- Als Kondensat von Quanten-Simplizes ohne Einbettung (GFT, Oriti 2024).
- Als fluessiges DT-Ensemble (Baillie/Johnston 1993).
- Finns Variante, eingebettet und Delaunay-gesteuert, mit flachen Zuegen, habe ich in keiner Quelle gefunden.
  Neu waere die Netzform mit Umklappen. Das passt zur Vorab-Bedeutung von RG1 und RG2.

## 8. Kartenvorschlag GAS-NETZ-1 (folgt erst nach HODGE-MASSE-1)

**GAS-NETZ-1: Duale Traegheit am Delaunay-Zug und ein fliessendes flaches Netz.**

- **Aufbau:**
  - Wie TAKT-DYNAMIK-1: Glas N = 128, A = 1e-3 und 1e-2, Arm b, Lesarten R und P, Code kopiert.
  - Neue Bewegungsenergie aus dualen Massen: umkreisbasierte *1-Gewichte auf Kanten bzw. Voronoi-Volumina an Ecken,
    in einer Lagrange-Funktion. A0 und A2 laufen als Vergleich.
  - Zweiter Arm "Gas": Die Ecken bewegen sich zufaellig in Eichrichtungen eines flachen Netzes, mit Delaunay-Zuegen,
    ohne Welle. Danach dieselbe Bewegung mit Welle.
- **Messgroessen:**
  - Energiesprung je 2-3- und je 3-2-Zug.
  - Unterschied Lesart R gegen P.
  - Drift ueber 10 Perioden.
  - TT-Amplitude und Phase gegen Arm a (wie TD3).
  - TT-Energie, die im reinen Gas-Arm entsteht.
- **Ableitbarkeitsprobe:**
  - **Vorab ableitbar [M]:**
    1. Am 2-3-Zug bei exakter Ko-Sphaerizitaet fallen die Umkugelmittelpunkte zusammen. Die duale Flaeche der neuen
       Kante ist null, die duale Kante der wegfallenden Flaeche hat Laenge null. Jede *1- bzw. *2-gewichtete Summe
       ist also stetig.
       - Literatur: Springel 2010, Z. 608-620; Hess/Springel 2010, Z. 195-200.
       - Projekt: duales Mass am 2-3-Zug <= 2e-13 (TAKT-DYNAMIK-1 [P]).
    2. Ist die Massematrix am Zug stetig, ergeben stetige Raten (R) und stetige Impulse (P) denselben Zustand, weil
       p = M v. Der R-P-Unterschied in TAKT-DYNAMIK-1 misst also die Unstetigkeit der Masse. Das ist eine
       Kontrolle, kein Ergebnis.
    3. Flache Eckbewegung aendert die Regge-Energie nicht (UMKLAPP-1 [P]); das gilt exakt nur im Flachen
       (Bahr/Dittrich 2009).
  - **Nicht ableitbar:**
    - der Rest am 3-2-Zug im gedehnten Netz (TD0: Median 1e-6 bis 2e-5, Ausreisser bis 6e3 [P]);
    - Stabilitaet und Isotropie der TT-Zweige mit dualer Masse;
    - Langzeitdrift, Streuung (TD3) und Energiefluss aus dem Gas-Arm in TT-Moden.
  - **Projekt-grep** (10:09:53, runden-v3, *.md, Ausschluesse gesetzt):
    - AREPO, Springel, Moving Mesh, Korn und Navier-Stokes kommen nur in dieser Karte und in den RUNDE-48-Notizen vor.
    - DEC-Grundlagen (Hirani u. a.) stehen in HODGE-L [P]; Dittrich/Hoehn steht in PACHNER-TAKT-1 [P].
  - **Abgrenzung:** HODGE-MASSE-1 prueft A2 (Volumen je Tetraeder). A2 ist am Zug nur bei gleichmaessiger Verzerrung
    stetig (Hess/Springel Z. 183-197 sinngemaess). GAS-NETZ-1 prueft die duale Form und den Gas-Arm.
- **Vorschlag fuer Vorhersagen** (Wahrscheinlichkeiten setzt die Leitung):
  - GN0 (Kontrolle, vorab): 2-3-Sprung <= 1e-10 H0; R und P gleich bis auf Rundung.
  - GN1 [H]: 3-2-Sprung von der Ordnung des Fehlwinkels (1e-6 bis 1e-5 H0); Drift ueber 10 Perioden < 0,1 %.
  - GN2 [H]: Der reine Gas-Arm erzeugt keine TT-Energie ueber 1e-10 H0.

## 9. Negativliste (nicht sagen)

1. "Volovik hat Einstein-Gravitation aus He-3 abgeleitet." In He-3-A ist sie bimetrisch mit Gravitonmassen.
2. "GFT-Kondensate liefern Schwerewellen." Nicht gefunden; erste Stoerungen sind nicht ART-artig.
3. "Die Daten schliessen ein Raum-Gas aus." Nur das scherartige Gas mit tau <~ Gyr, und auch das nur nach meiner
   Uebersetzung [ES].
4. "Xi_0 = 1,4 zeigt eine Daempfung." Die ART liegt im 68-%-Intervall, der Wert haengt vom Modell ab.
5. "Moving-Mesh-Verfahren erhalten die Wellenenergie exakt." AREPO erhaelt Waerme plus Bewegung und daempft Bewegung.
6. "In AREPO folgt die Erhaltung aus den Nullflaechen." Sie folgt aus F_ij = -F_ji.
7. "A2 macht den Zug stetig." Nicht ableitbar; Tetraedervolumina springen.
8. "DT hat eine Gasphase." DT ist als Ganzes fluid; seine Phasen sind nicht flach.
9. "OpenAI hat das Millennium-Problem geloest." Behauptet; Teilpruefung laeuft; Wortlaut ungelesen.
10. "Die OpenAI-Kraft verletzt die Clay-Abklingbedingungen." Die Folgearbeiten sagen das Gegenteil.
11. "Der NS-Blow-up hat Folgen fuer Finns Netz." Endliche Netze explodieren nicht; eine Verbindung ist nicht
    veroeffentlicht.
12. "Die k-Luecke gilt fuer Schwerewellen." Nur fuer scherartige Wellen.
13. "m_g-Schranken begrenzen die k-Luecke direkt." Das Vorzeichen ist verschieden.
14. "Zufallsnetze sind Lorentz-invariant." Das gilt fuer die Punktmenge, nicht fuer den Graphen.
15. "Carcione/Ba haben Daten verglichen." Im Abstract steht nichts davon.
16. "Lean-Beweis geprueft." Kein Lean-Code gelesen.

## 10. Selbstanzeigen

1. Drei Abrufe ohne Inhalt:
   - F4: eigener Syntaxfehler.
   - F15: HTTP 403.
   - F18: Werkzeugsperre. Eine Umgehung per curl oder mit Browser-Kennung habe ich bewusst nicht versucht.
2. Den Wortlaut der Organisation zu NS (openai.com) habe ich nicht gelesen. Der Satz ist nur ueber Folgearbeiten
   belegt; drei davon im Volltext bzw. Abstract.
3. Die tau-Folgerungen (Abschn. 5) sind meine Uebersetzung, mit offenen Annahmen:
   - Xi_0-Form gegen konstante Daempfung;
   - z ~ 0,5 als typische Rotverschiebung;
   - Rueckblickzeit ~5 Gyr aus dem Gedaechtnis [L].
4. Berichtigt im Arbeitsfeld:
   - GW170817-Schranke zuerst mit der falschen Seite (-3e-15) gerechnet; richtig ist +7e-16 (v_Gruppe > c).
   - Die Groessenordnung blieb gleich.
5. Hawkings Faktor 16 pi G eta ist nur aus dem Gedaechtnis [L]; das Goswami-Abstract sagt nur "proportional zu G eta".
6. Die meisten Belege sind nur Abstracts. Volltext gelesen habe ich nur Springel 2010, Hess/Springel 2010 und
   Lei/Ren 2026.
7. Zeitstempel:
   - Vier Zeiten waren zuerst geschaetzt (F2, F15/F16/F18, Abschnittskoepfe "10:11", "10:14 bis 10:16"). Alle sind
     gestrichen und mit gemessenen Grenzen berichtigt.
   - In ABRUFE.md sind F15, F16 und F18 nur als "nach <gemessene Zeit>" angegeben.
8. Im Arbeitsfeld standen zuerst mehrere Zitate je Quelle, eines ueber 15 Woerter. Ich habe sie auf Paraphrase
   umgestellt; der Vorgang ist in ARBEITSFELD.md Abschn. 6 vermerkt.
9. Der Projekt-grep nach Dittrich/Hoehn brach nach 60 s ab; die Liste ist unvollstaendig.
10. "RG6" hat in der Leitungs-Nachricht keinen eigenen Wortlaut. Ich urteile ueber NS1 bis NS3 (Rueckfrage Q3).
11. **Kalibrierung:**
    - (a) Gemessen: Datenschranken, Projektzahlen, Volltextstellen.
    - (b) Nuetzlich verdichtet: Kette Scherung gegen Kruemmung, tau-Uebersetzung, Regime-Tabelle, GAS-NETZ-1.
    - (c) Gewachsene Gewissheit ohne neue Evidenz: "Kruemmung entkoppelt vom Maxwell-Mechanismus" fuehlte sich im
      Lauf sicherer an. Neue Evidenz dafuer sind aber nur Analogien (Weltkristall, DT = fluid, Membranen); an Finns
      Netz mit Gasbewegung ist nichts gerechnet.
    - Warnzeichen: Die Frage zerfiel in drei Teilfragen (statisch, Energie am Zug, Rest am 3-2-Zug), und dabei stieg
      meine Sicherheit.
12. **Gegensweep** (ARBEITSFELD 4a): "Was war selbstverstaendlich?"
    - Geprueft: Daten = ART (G1: nur knapp, Xi_0); m_g gegen k-Luecke (G2: Vorzeichen); Seite der GW170817-Schranke
      (G3: berichtigt); Lesart "Gas" (G4: weitere Lesarten gefunden); NS-Satz (G7: teilweise).
    - Nicht geprueft: Planck-Gas mit tau ~ Planck-Zeit (G5); duale Stetigkeit am 3-2-Zug im gekruemmten Netz (G6).

## 11. Einfach gesagt

Finn fragt, ob der Raum statt eines festen Netzes auch ein Gas sein kann: Die Punkte flitzen herum, und die kleinen
Pyramiden setzen sich staendig neu zusammen. In einer Fluessigkeit leben Querwellen nur kurz, weil die Teilchen ihre
Lage "vergessen"; waeren Schwerewellen solche Querwellen, muesste ein Raum-Gas Milliarden Jahre stillhalten, sonst
kaemen die Wellen ferner Schwarzer Loecher viel zu leise bei uns an. Finns Netz traegt seine Wellen aber ueber
Kruemmung, nicht ueber Scherung, und ein flaches Umklappen aendert die Kruemmung nicht. Deshalb darf es im Prinzip
fliessen, wenn die Traegheit an den Voronoi-Zellen haengt, deren Flaechen beim Umklappen genau durch null gehen, so
wie es Astrophysiker seit 2010 mit bewegten Gittern machen. Der neue Navier-Stokes-Beweis betrifft echte
Fluessigkeiten im Kontinuum; auf einem endlichen Netz kann so eine Unendlichkeit nicht entstehen, und eine
Verbindung zur Raumzeit ist nicht veroeffentlicht.

## Anhang A: Offene Fragen

- Q1: Gilt "kein statischer Schermodul" auch fuer Glas-Netze nach vielen Zuegen?
- Q2: GAS-NETZ-1, insbesondere der Rest am 3-2-Zug.
- Q3: Wortlaut fuer RG6? Bisher als Sammelname fuer NS1 bis NS3 gefuehrt.
- Q4: OpenAI-Wortlaut zu Preisfrage, Kraftklasse und Lean (Zugriff noetig).
- Q5: Saubere tau-Schranke aus der Standardsirene GW170817 (Abbott u. a. 2017, Nature); nicht gelesen.
- Q6: Gibt es Schranken auf A_0 < 0 (tachyonartig), also auf die k-Luecke selbst, im GWTC-4.0-Volltext?
- Q7: Was genau ist bei Volovik/Zubkov "superplastisch"? Haengen Wellen und Umordnung zusammen? Nur Abstracts
  gelesen.

## Anhang B: Quellenliste (Autor, Jahr, Titel, Adresse; Lesetiefe)

Projekt [P]:
- tt-glas-2/ERGEBNIS.md (Berichtigung, Abschn. 2); umklapp-1/ERGEBNIS.md (Abschn. 2); takt-dynamik-1/ERGEBNIS.md
  (Abschn. 2, 5); weltkristall-l/DOSSIER.md; baby-universum-l/DOSSIER.md (4.6, 4.7); hodge-masse-1/KARTE.md;
  hodge-l/DOSSIER.md (DEC-Grundlagen); RUNDE-37/pachner-takt-1/KARTE.md (nur per grep gefunden).

Fachquellen [S]:
- Abbott, B. P. u. a. (LVK, Fermi-GBM, INTEGRAL) (2017): Gravitational Waves and Gamma-rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A. ApJL 848, L13. https://arxiv.org/abs/1710.05834 (Abstract)
- Abukhwejah, A.; Jagad, P.; Samtaney, R.; Schmid, P. (2024): A Hybrid DEC Discretization and Fourier Transform of the Incompressible NS Equations in 3D. https://arxiv.org/abs/2409.04731 (Abstract)
- Baggioli, M.; Brazhkin, V.; Trachenko, K.; Vasin, M. (2020): Gapped momentum states. Phys. Rep. https://arxiv.org/abs/1904.01419 (Abstract)
- Bahr, B.; Dittrich, B. (2009): (Broken) Gauge Symmetries and Constraints in Regge Calculus. CQG 26, 225011. https://arxiv.org/abs/0905.1670 (Abstract)
- Baillie, C. F.; Johnston, D. A. (1993): Freezing a Fluid Random Surface. PRD 48, 5025. https://arxiv.org/abs/hep-lat/9305012 (Abstract)
- Bombelli, L.; Henson, J.; Sorkin, R. D. (2006/2009): Discreteness without symmetry breaking: a theorem. MPLA 24, 2579. https://arxiv.org/abs/gr-qc/0605006 (Abstract)
- Bredberg, I.; Keeler, C.; Lysov, V.; Strominger, A. (2011): From Navier-Stokes To Einstein. https://arxiv.org/abs/1101.2451 (Abstract)
- Cang, H.; Wang, Y. (2025): Universality and Falsifiability of Quantum Spacetime Decoherence ... GW Phase Diffusion. https://arxiv.org/abs/2512.02782 (Abstract)
- Cao, S.; Chi, Z. (2026): Singular Forces on the Whole Space: Sobolev Density Thresholds and Energy Approximation. https://arxiv.org/abs/2609.10269 (Abstract)
- Cao, S.; Chi, Z.; Nie, P. (2026): Density of Forces Producing Navier-Stokes Blowup. https://arxiv.org/abs/2609.10262 (Abstract)
- Carcione, J. M.; Ba, J. (2024): On the viscoelastic-electromagnetic-gravitational analogy. https://arxiv.org/abs/2405.20920 (Abstract)
- Carlip, S. (2012/2014): Challenges for Emergent Gravity. https://arxiv.org/abs/1207.2504 (Abstract)
- Cheskidov, A.; Dai, M.; Palasek, S. (2026): Cascade mechanisms for Navier-Stokes blow-up. https://arxiv.org/abs/2609.26790 (Abstract)
- Cichowlas, C.; Bonaiti, P.; Debbasch, F.; Brachet, M. (2005): Effective Dissipation and Turbulence in Spectrally Truncated Euler Flows. https://arxiv.org/abs/nlin/0410064 (Abstract)
- Constantin, P.; Ignatova, M.; Vicol, V. (2026): Regularity of asymptotically axisymmetric solutions to the 3D NS equations with analytic forcing. https://arxiv.org/abs/2609.20803 (Abstract)
- Diamantini, M. C.; Kleinert, H.; Trugenberger, C. A. (1999): Floppy Membranes. https://arxiv.org/abs/cond-mat/9903021 (Abstract)
- Dong, Y.-Q.; Mukohyama, S.; Liu, Y.-X. (2026): Propagation and polarization of GWs on curved backgrounds in Einstein-Aether theory. https://arxiv.org/abs/2601.13061 (Abstract)
- Dowker, F.; Butterfield, J. (2021): Recovering General Relativity from a Planck scale discrete theory of quantum gravity. https://arxiv.org/abs/2106.01297 (Abstract)
- Dubovsky, S. L. (2004): Phases of massive gravity. JHEP 0410:076. https://arxiv.org/abs/hep-th/0409124 (Abstract)
- Duraiswami, R. (2026): Self-similar swirl between contracting porous walls ... OpenAI 2026 forced blow-up construction. https://arxiv.org/abs/2609.17642 (Abstract)
- Eling, C.; Guedens, R.; Jacobson, T. (2006): Non-equilibrium Thermodynamics of Spacetime. PRL 96, 121301. https://arxiv.org/abs/gr-qc/0602001 (Abstract)
- Gamble, R.; Flurchick, K. M. (2017): Viscoelastic Theory Representation Of Gravitational Strain Fields In The +Lambda-CDM Vacuum. https://arxiv.org/abs/1801.00350 (Abstract)
- Gielen, S.; Mickel, L. (2025): Cosmological scalar perturbations for a metric reconstructed from GFT. CQG 42, 225015. https://arxiv.org/abs/2505.07951 (Abstract)
- Girelli, F.; Liberati, S.; Sindoni, L. (2008): Gravitational dynamics in Bose Einstein condensates. PRD 78, 084013. https://arxiv.org/abs/0807.4910 (Abstract)
- Goswami, G.; Chakravarty, G. K.; Mohanty, S.; Prasanna, A. R. (2017): Constraints on cosmological viscosity and self interacting dark matter from GW observations. PRD 95, 103509. https://arxiv.org/abs/1603.02635 (Abstract)
- Gupta, T. u. a. (2021): New binary pulsar constraints on Einstein-aether theory after GW170817. CQG 38, 195003. https://arxiv.org/abs/2104.04596 (Abstract)
- Hess, S.; Springel, V. (2010): Particle hydrodynamics with tessellation techniques. https://arxiv.org/abs/0912.0629 (Volltext, quellen/F10-*.txt)
- Hu, B. L. (2005): Can Spacetime be a Condensate? IJTP 44, 1785. https://arxiv.org/abs/gr-qc/0503067 (Abstract)
- Jacobson, T. (1995): Thermodynamics of Spacetime: The Einstein Equation of State. PRL 75, 1260. https://arxiv.org/abs/gr-qc/9504004 (Abstract)
- Jannes, G.; Volovik, G. E. (2012): The cosmological constant: A lesson from the effective gravity of topological Weyl media. JETP Lett. 96, 215. https://arxiv.org/abs/1108.5086 (Abstract)
- Kleinert, H.; Zaanen, J. (2004): World Nematic Crystal Model of Gravity Explaining the Absence of Torsion. PLA 324, 361. https://arxiv.org/abs/gr-qc/0307033 (Abstract)
- Koibuchi, H.; Shobukhov, A. (2014): Branched-polymer to inflated transition of self-avoiding fluid surfaces. Physica A 410, 54. https://arxiv.org/abs/1405.1496 (Abstract)
- Korn, P. (2026a): Exact conservation as selection principle: DEC for the incompressible NS and Euler equations. https://arxiv.org/abs/2605.13048 (Abstract)
- Korn, P. (2026b): A no-go theorem and its resolution for the discrete compressible barotropic NS equations. https://arxiv.org/abs/2605.16554 (Abstract)
- Lei, Z.; Ren, X. (2026): Finite-Time Blowup for Navier-Stokes with Smooth Forcing, Part I. https://arxiv.org/abs/2609.35406 (Volltext v2, quellen/F20-*.txt)
- Liberati, S.; Maccione, L. (2014): Astrophysical constraints on Planck scale dissipative phenomena. PRL 112, 151301. https://arxiv.org/abs/1309.7296 (Abstract)
- LIGO/Virgo/KAGRA (2025/2026): GWTC-4.0: Constraints on the Cosmic Expansion Rate and Modified GW Propagation. ApJL 1007. https://arxiv.org/abs/2509.04348 (Abstract)
- LIGO/Virgo/KAGRA (2026): GWTC-4.0: Tests of General Relativity. II. Parameterized Tests. https://arxiv.org/abs/2603.19020 (Abstract)
- Liu, W. (2026): A compatibility-realization framework for singular NS flows. https://arxiv.org/abs/2609.14292 (Abstract)
- Maas, A.; Plaetzer, S.; Pressler, F. (2025/2026): Hints for a Geon from Causal Dynamic Triangulations. PLB 879, 140600. https://arxiv.org/abs/2504.11047 (Abstract)
- Mohamed, M. S.; Hirani, A. N.; Samtaney, R. (2016): DEC discretization of incompressible NS equations over surface simplicial meshes. J. Comput. Phys. 312, 175. https://arxiv.org/abs/1508.01166 (Abstract)
- Murugan, S. D.; Ray, S. S. (2023): On the thermalization of the 3D incompressible Galerkin-truncated Euler equation. Phys. Rev. Fluids 8, 084605. https://arxiv.org/abs/2209.05046 (Abstract)
- Oost, J.; Mukohyama, S.; Wang, A. (2018): Constraints on Einstein-aether theory after GW170817. PRD 97, 124023. https://arxiv.org/abs/1802.04303 (Abstract)
- Oriti, D. (2024): Hydrodynamics on (mini)superspace, or a non-linear extension of quantum cosmology. https://arxiv.org/abs/2403.10741 (Abstract)
- Oriti, D.; Sindoni, L.; Wilson-Ewing, E. (2016): Emergent Friedmann dynamics with a quantum bounce from quantum gravity condensates. CQG 33, 224001. https://arxiv.org/abs/1602.05881 (Abstract)
- Oriti, D.; Wang, Y.-L. (2023): Effective anisotropic dynamics in GFT cosmology. https://arxiv.org/abs/2311.14377 (Abstract)
- Petrillo, J.; Glimm, J. (2026): The Positive Defect Problem ... Unforced Navier-Stokes Blowup. https://arxiv.org/abs/2609.23868 (Abstract)
- Schorlepp, T.; Rosenhaus, V.; Falkovich, G. (2026): How turbulent flows grow vorticity at a point. https://arxiv.org/abs/2609.13056 (Abstract)
- Springel, V. (2010): E pur si muove: Galilean-invariant cosmological hydrodynamical simulations on a moving mesh. https://arxiv.org/abs/0901.4107 (Volltext, quellen/F3-*.txt)
- Surya, S. (2012): Evidence for a Phase Transition in 2D Causal Set Quantum Gravity. https://arxiv.org/abs/1110.6244 (Abstract)
- Tsedrik, M.; Bose, B.; Marchetti, L.; Ferreira, E. (2026): Constraining quantum-gravity predictions for evolving dark energy. https://arxiv.org/abs/2609.15969 (Abstract)
- Tuveri, M. (2026): Beyond the Metric: Geometrical Measurability as a Constraint on Quantum Gravity. https://arxiv.org/abs/2606.13522 (Abstract)
- Volovik, G. E. (2001): Superfluid analogies of cosmological phenomena. Phys. Rep. 351, 195. https://arxiv.org/abs/gr-qc/0005091 (Abstract)
- Volovik, G. E. (2020): Dimensionless physics. https://arxiv.org/abs/2006.16821 (Abstract)
- Volovik, G. E. (2021): Gravity from symmetry breaking phase transition. https://arxiv.org/abs/2111.07817 (Abstract)
- Volovik, G. E. (2026): Massless graviton in de Sitter as second sound in two-fluid hydrodynamics. https://arxiv.org/abs/2601.00639 (Abstract)
- Wang, S.; Zhao, Z.-C. (2024): Unveiling the Graviton Mass Bounds through Analysis of 2023 PTA Data Releases. PRD 109, L061502. https://arxiv.org/abs/2307.04680 (Abstract)
- Zaanen, J.; Beekman, A. J. (2012): The emergence of gauge invariance: the stay-at-home gauge versus local-global duality. Ann. Phys. 327, 1146. https://arxiv.org/abs/1108.2791 (Abstract)
- Zhao, Z.-C.; Wang, S. (2026): Probing Graviton Mass with MeerKAT PTA and SKA-PTA Forecasts. https://arxiv.org/abs/2607.14790 (Abstract)
- Zubkov, M. A. (2019): Emergent gravity in superplastic crystals. https://arxiv.org/abs/1909.08412 (Abstract)
- OpenAI (2026): Finite Time Blowup for Navier-Stokes (166 S.) und Finite Time Blowup for the Euler Equation (57 S.), Manuskripte vom 08.09.2026. Nur ueber Lei/Ren Ref. [21], [22]; https://openai.com/index/navier-stokes-solution/ ergab HTTP 403.
- Alpoege, L.; Buckmaster, T. (2026): Blowup for the Euler equations with smooth forcing. Preprint, nur ueber Lei/Ren Ref. [2].

Presse, nur Hinweis (Suchtreffer F16, nicht gelesen, keine Quelle fuer Sachaussagen):
- https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/
- https://theneuron.ai/news/inside-openais-navierstokes-claim-the-proof-the-ai-effort-and-the-credit-fight/
- https://lilting.ch/en/articles/navier-stokes-openai-blowup-dispute
- https://interestingengineering.com/ai-robotics/openai-navier-stokes-mystery-solved

Ende: siehe naechste Zeile.

Abschluss Dossier: 2026-10-05 10:22:36 CEST (date).
