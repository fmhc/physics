# RAUM-GAS-L: Arbeitsfeld (feldforscher fuer die Leitung claude-primary)

- Start 2026-10-05 09:42:40 CEST (date). Karte KARTE.md bindend, RG1 bis RG5 unveraendert.
- Diese Datei ist das gemeinsame Feld. Gestrichenes bleibt mit ~~...~~ stehen, offene Rueckfragen wandern mit.
- Kennzeichen: [E] Messung/Rechnung, [M] Mathematik, [S] Fachquelle, [L] Lehrbuch, [H] Hypothese, [P] Projektbefund.
  [ES] = eigener Schluss.

## 0. Lokal gelesen (vor jedem Abruf, 09:42 bis 09:49)

- KARTE.md (ganz).
- takt-dynamik-1/ERGEBNIS.md Abschn. 2 und 5; umklapp-1/ERGEBNIS.md Abschn. 2; tt-glas-2/ERGEBNIS.md Berichtigung und
  Abschn. 2; weltkristall-l/DOSSIER.md (DT-Stellen, Z. 15-21, 89-97, 210-211); baby-universum-l/DOSSIER.md 4.6, 4.7;
  hodge-masse-1/KARTE.md (nur gelesen, nicht nachgerechnet).

## 1. Projektbausteine [P] (fuer die Verkettung)

- B1 UMKLAPP-1 Abschn. 2.1: flache 2-3-Zuege, |Delta S| <= 3,6e-12; die Regge-Energie ist blind fuer Zuege.
- B2 TAKT-DYNAMIK-1 Abschn. 2.2/2.3/5: Delaunay-Zuege stabil, Zufallszuege nicht; Energiesprung 0,2 bis 0,46 % von H0
  je Zug, sitzt in der Bewegungsenergie (gleiches Gewicht A0 je Tetraeder); "duales Mass und P-Sprung beim 2-3-Zug
  <= 2e-13"; beim 3-2-Zug Sprung von der Ordnung des Fehlwinkels der Welle (Median 1e-6 bis 2e-5). Lesart R daempft,
  Lesart P verstaerkt.
- B3 TT-GLAS-2 Abschn. 2.1: Nullmoden nur bei Gamma, je Netz genau 6 = die homogenen Verzerrungen des Torus.
  Abschn. 2.2: Anisotropie sitzt in der Traegheit (Bewegungsenergie), nicht in Relaxation.
- B4 WELTKRISTALL-L Z. 210-211: Kleinert/Zaanen 2004 [S Abstract]: Weltkristall -> nematische Phase durch
  Kondensation von Versetzungen; "Explaining the Absence of Torsion".
- B5 BABY-UNIVERSUM-L 4.6/4.7: DT-Phasen Knaeuel (kappa0 klein) und verzweigte Polymere (d_H = 2); 3D-CDT
  Starkkopplung "foam of baby universes"; Budd/Nemeth 2025 triple-tree-Phase.
- B6 HODGE-MASSE-1 (laeuft): volumengewichtete DeWitt-Bewegungsenergie A2; HM4 = Sprung je 2-3-Zug < 1e-4 H0.

## 2. Schreibtisch-Kette vor dem ersten Abruf (Bausteine verketten)

- K1 [M] Maxwell-Viskoelastik, Querwelle: sigma_t + sigma/tau = G v_x, rho v_t = sigma_x. Ebene Welle ergibt
  omega^2 + i omega/tau = c^2 k^2 mit c^2 = G/rho, also omega = -i/(2 tau) +- sqrt(c^2 k^2 - 1/(4 tau^2)).
  - Laufende Querwelle nur fuer k > k_g = 1/(2 c tau) ("k-Luecke").
  - Jede laufende Querwelle klingt mit exp(-t/(2 tau)) ab, unabhaengig von k.
  - Phasengeschwindigkeit < c, Gruppengeschwindigkeit c^2 k / Re(omega) > c; fuer c k tau >> 1:
    Delta v / c ~ 1/(8 c^2 k^2 tau^2).
  - Fuer k < k_g: Scherdiffusion mit nu = c^2 tau = eta/rho.
- K2 [M] Folge fuer Daten (wenn Schwerewellen scherartig waeren): Amplitude nach Laufzeit T um exp(-T/(2 tau)) kleiner,
  frequenzunabhaengig -> wirkt wie eine zu grosse Entfernung: d_GW/d_EM = exp(T/(2 tau)). Mit erlaubtem Faktor
  (1 + x): tau >= T / (2 ln(1 + x)).
- K3 [M, ES] Scherung gegen Kruemmung als Skalierung: Festkoerper-Energie ~ mu eps^2 (eps = Dehnung, ohne Ableitung);
  ART-Energie der Welle ~ (d h)^2 (Ableitung der Dehnung). Ein homogener Scher-Zustand kostet im Festkoerper
  Energie, in der ART nicht (flach bleibt flach).
- K4 [P + M, ES] TT-GLAS-2 hat bei Gamma genau 6 Nullmoden = homogene Verzerrungen (B3). Das Netz hat also keinen
  statischen Schermodul, wie eine Fluessigkeit. Trotzdem gibt es masselose TT-Wellen (omega^2 ~ k^2). Ihre
  Rueckstellkraft ist Kruemmung (Gradient), nicht Scherung. Vorlaeufige Lesart: Die Karten-Frage
  "Scherung oder Kruemmung" ist fuer das ruhende Netz schon beantwortet: Kruemmung.
- K5 [M] Delaunay-Zug genau bei Ko-Sphaerizitaet (5 Punkte auf einer Kugel): Die drei Umkugelmittelpunkte der neuen
  Tetraeder fallen zusammen. Die duale Flaeche der neuen Kante hat Flaeche null, die duale Kante der wegfallenden
  Flaeche Laenge null. Groessen mit dualem Gewicht (*1, *2) sind am Zug stetig. Das passt zu B2 (duales Mass
  <= 2e-13). Es ist das Prinzip, nach dem RG4 fragt.
- K6 [L, ES] Regge: Eckverschiebungen im Flachen sind Eichrichtungen (diskrete Diffeomorphismen); bei Kruemmung
  nur naeherungsweise. Ein "Gas" aus Ecken ist im flachen Grenzfall reine Umbenennung (wie ein Moving-Mesh-Gitter).
  Physik steckt in Kantenlaengen und Fehlwinkeln. Quelle noch zu pruefen (Bahr/Dittrich).
- K7 [ES] Drei Regime fuer "Raum als Medium":
  - (I) Medium im Raum (Stoff fuellt die Raumzeit, Einstein-Dynamik bleibt): Schwerewellen werden durch Viskositaet
    gedaempft (Hawking 1966, 16 pi G eta [L, Quelle pruefen]); ein Festkoerper gibt dem Graviton Masse (Dubovsky [L]).
  - (II) Medium ist der Raum (Finns Netz): Maxwell nur, wenn die Welle scherartig ist (K3, K4).
  - (III) Analogmodell: Quasiteilchen sehen eine wirksame Metrik, die Metrik hat keine Einstein-Dynamik (RG1).
  - Dazu omega tau > 1 gegen omega tau < 1.

## 3. Erwartungen vor Abrufen (Regel: Zeit per date, dann Abruf)

- **F1, 09:49:49 CEST, arXiv-API id_list (16 IDs aus dem Gedaechtnis, Titel pruefen):**
  - 0901.4107 Springel 2010: erwartet "conserves mass, momentum, energy", Galilei-invariant, Voronoi bewegter Punkte;
    der Satz "Flaechen gehen durch null" steht vermutlich NICHT im Abstract.
  - 1710.05834 GW170817/GRB: erwartet Delta v/c zwischen -3e-15 und +7e-16.
  - gr-qc/0005091 Volovik Phys. Rep. 2001: erwartet wirksame Metrik/Eichfelder fuer Quasiteilchen; Einstein-Dynamik
    nicht von selbst.
  - 1602.05881 Oriti/Sindoni/Wilson-Ewing 2016: erwartet Friedmann-Gleichungen mit Rueckprall aus GFT-Kondensat.
  - gr-qc/9504004 Jacobson 1995: Einstein-Gleichung als Zustandsgleichung; Vergleich mit Schall in Luft.
  - gr-qc/0602001 Eling/Guedens/Jacobson 2006: Nichtgleichgewicht, Scherviskositaet der Horizonte, eta/s = 1/(4 pi).
  - 1207.2504 Carlip: Herausforderungen fuer emergente Gravitation (Weinberg-Witten u. a.).
  - 1904.01419 Baggioli u. a.: "Gapped momentum states", k-Luecke.
  - gr-qc/0605006 Bombelli/Henson/Sorkin: zufaellige Streuung bricht Lorentz nicht.
  - 0807.4910 Girelli/Liberati/Sindoni: BEC liefert nur Poisson-artige (Newton-)Gravitation, keine Einstein-Dynamik.
  - 1309.7296 Liberati/Maccione: sehr starke Schranken auf Planck-unterdrueckte Dissipation.
  - hep-th/0409124 Dubovsky: Phasen massiver Gravitation, Lorentz-brechend (Medium-Bild).
  - 0905.1670 Bahr/Dittrich: Eichsymmetrie (Eckverschiebung) im Flachen exakt, bei Kruemmung gebrochen.
  - 1603.02635 Goswami u. a.: Viskositaetsschranke aus GW150914 ueber Hawking 16 pi G eta (ID unsicher).
  - gr-qc/0503067 B. L. Hu "Can spacetime be a condensate?" (ID unsicher).
  - 1110.6244 Surya 2012: 2D-Kausalmengen, Kontinuumsphase und geschichtete Phase.
  - **F1 Ergebnis (09:50):** 16 von 16 Titeln passen. Je eine Zeile:
    - GW170817: -3e-15 bis +7e-16 bestaetigt (Zeitversatz 1,74 +- 0,05 s).
    - OSW 2016: bestaetigt; woertlich "emerging as the hydrodynamics of simple condensate states" (Kosmologie als
      Hydrodynamik), Gross-Pitaevskii-Regime, Rueckprall.
    - Jacobson 1995: bestaetigt (Schall in Luft). EGJ 2006: bestaetigt, aber eta/s = 1/(4 pi) steht nicht im Abstract;
      dort "shear viscosity of the horizon" fuer reine Einstein-Theorie, Volumenviskositaet fuer f(R).
    - Carlip, Gapped momentum states (Maxwell-Frenkel, k-Luecke ~ Dissipation), Hu 2005 (ART als Hydrodynamik,
      Quantisierung gaebe nur "phonon physics"), GLS 2008 (BEC: modifizierte Poisson-Gleichung, Reichweite =
      Heilungslaenge), Dubovsky, Surya 2012 ("continuum phase" gegen "crystalline phase"): bestaetigt.
    - Bahr/Dittrich 2009: bestaetigt K6: "for a solution with curvature there do not exist exact gauge symmetries".
    - Goswami u. a. 2016/17: bestaetigt Regime I: ideale Fluessigkeit daempft nicht, Scherviskositaet daempft mit
      Rate ~ G eta; 410 Mpc (GW150914). Zahl der Schranke nicht im Abstract.
    - Liberati/Maccione: bestaetigt ("strong constraints"), Zahlen nicht im Abstract.
    - **V-F1a (Verstoss, klein):** Bombelli/Henson/Sorkin: zusaetzlich "no way to associate a finite-valency graph to
      a sprinkling consistently with Lorentz invariance". Fuer Finn: Jedes Netz endlicher Valenz waehlt ein
      Bezugssystem. Ein Gas-Netz hat ausserdem eine mittlere Stroemung = Ruhesystem. Folge: Lorentz-Tests sind ein
      eigener Unterscheidungspunkt (Aether-artig) [ES]. Erwartung korrigiert: "zufaellig = Lorentz-neutral" gilt nur
      fuer die Punktmenge, nicht fuer das Netz darauf.
    - **V-F1b (Verstoss, klein):** Springel-Abstract sagt nicht "erhaelt Masse, Impuls, Energie", sondern nennt ein
      Finite-Volumen-Verfahren (ungeteiltes Godunov-Schema mit exaktem Riemann-Loeser). Erhaltung folgt aus der
      Flussform; ein Godunov-Verfahren hat numerische Dissipation (Riemann-Loeser) [L]. Fuer RG4 im Volltext pruefen.
    - **V-F1c (Verstoss, mittel):** Volovik-Abstract: "equilibrium vacuum is not gravitating" (Vakuumenergie
      im Gleichgewicht exakt null); zur Einstein-Dynamik der Metrik steht dort nichts. RG1-Teil 2 braucht eine
      andere Stelle.

- **F2, ~~09:51 CEST (date 09:50:49 + Schreibzeit)~~ [Berichtigung ~~10:10~~ [nach date 10:10:20]: geschaetzte Zeit gestrichen; gemessen
  sind date 09:50:49 vor dem Schreiben der Erwartung und 09:51:19 beim Abrufbefehl], arXiv-API Suche
  Kleinert/Zaanen Weltkristall:**
  - Erwartet: Kleinert 1987 "Gravity as theory of defects in a crystal with only second gradient elasticity"
    (vermutlich nicht auf arXiv), Kleinert/Zaanen 2004 "World nematic crystal": Versetzungen kondensiert ->
    keine Torsion, Kruemmung bleibt. Zaanen u. a. (Nussinov/Mukhin 2004, Beekman u. a. 2017): Quanten-Nematen,
    Scherwellen ("shear photons") werden massiv, Rotationssteifigkeit bleibt. Ein "floppy world crystal" ohne
    Schersteifigkeit erster Ordnung.
  - Wenn zutreffend: Literatur-Vorbild fuer "Raum = Fluessigkristall, Kruemmung traegt, Scherung nicht".
  - **F2 Ergebnis (09:51:19):** 4 Treffer. Bestaetigt: Kleinert/Zaanen 2004 (Gravitation zwischen Kruemmungsquellen,
    weil der Weltkristall durch Versetzungskondensation nematisch wurde; keine Torsion). Beekman/Zaanen 2012
    (1108.2791): "the relation between the quantum nematic and linearized gravity". Kleinert 1987 (zweite
    Gradientenelastizitaet) und "shear photons massiv" sind auf arXiv nicht gefunden -> nur [L], nicht an der
    Quelle. Kein Verstoss; Erwartung im Kern bestaetigt, Detail (Scherwellen massiv) offen.

- **F3, 09:51:47, arXiv-PDF 0901.4107 (Springel 2010), pdftotext, grep:**
  - Erwartet: Erhaltung von Masse, Impuls, Energie "to machine precision" aus der Flussform; Stetigkeit der
    Gitterbewegung, weil Voronoi-Flaechen beim Topologiewechsel mit Flaeche null erscheinen bzw. verschwinden.
    Erwartet ausserdem: Gesamtenergie erhalten, aber kinetische Energie wird ueber den Riemann-Loeser in Waerme
    gewandelt (numerische Viskositaet); bei Gravitation keine exakte Energieerhaltung.
  - **F3 Ergebnis (09:51:58, Volltext 5104 Zeilen, quellen/F3-*.txt):**
    - Bestaetigt (Volltext Z. 608-620, S. 10, sinngemaess): Die Delaunay-Zerlegung aendert sich sprunghaft, die
      Voronoi-Zerlegung stetig; beim Nachbarwechsel schrumpft die betroffene Voronoi-Flaeche auf
      "a vanishing area". Z. 209: Eine Kante zwischen entarteten Punkten hat duale Voronoi-Flaeche null.
      Zweck dort: kein Verheddern des Gitters (mesh tangling).
    - **V-F3a (Verstoss, gross, RG4):** Die Erhaltung kommt NICHT aus den Nullflaechen, sondern aus der Flussform:
      Gl. (13) mit F_ij = -F_ji, die Diskretisierung ist damit offenkundig erhaltend (Z. 861-875). Ohne Gravitation
      bleibt die Summe aus thermischer und kinetischer Energie auf Maschinengenauigkeit erhalten (Z. 1957-1962). Mit
      Eigengravitation erhaelt das Standardschema Impuls und Masse, die Gesamtenergie aber nicht ausdruecklich
      (Z. 2106-2107); die streng erhaltende Variante hat nach Springel in der Praxis schwere Maengel (Z. 2140-2143).
    - **V-F3b (Verstoss, gross, Kern fuer Finn):** Erhalten wird die Summe aus Waerme und Bewegung, nicht die
      Wellenenergie. Z. 1310-1340 (sinngemaess): Auch der Moving-Mesh-Code erzeugt falsche Dissipation in kaltem Gas;
      kleinskalige Geschwindigkeitsschwankungen werden weggedaempft und heizen das Gas. Uebertragen [ES]: Ein AREPO-artiges Gas-Netz wuerde Schwerewellen-Energie in "Waerme"
      des Netzes wandeln, also daempfen. Wellenerhaltung braucht eine Lagrange-/Hamilton-Form mit stetigem
      dualem Gewicht (K5), nicht ein Godunov-Flussverfahren. Kandidat: Hess/Springel 2010 (Voronoi-Teilchen aus
      einer Lagrange-Funktion), in F-Sammelabruf pruefen.
    - Erwartung korrigiert: "Moving Mesh = exakt erhaltend" gilt nur fuer Masse, Impuls und Gesamtenergie mit
      Waermespeicher; Nullflaechen geben Stetigkeit, nicht Erhaltung.

- **F4, 09:52:35, arXiv-API: GFT-Kondensate und Stoerungen (Tensor, Schwerewellen), neueste zuerst:**
  - Erwartet: skalare Stoerungen (Marchetti/Oriti 2021/22; Jercher/Marchetti/Pithis 2023/24); Tensorstoerungen
    bzw. Schwerewellen hoechstens 1 bis 2 Arbeiten, eher programmatisch; keine Daempfung/Viskositaet berechnet.
  - **F4 Ergebnis (09:52:52):** 0 Treffer, Suchsyntax fehlerhaft (Platzhalter * in Anfuehrungszeichen). Zaehlt als
    Abruf. Wiederholt als F5.
- **F5, 09:53:00, dieselbe Suche mit korrigierter Syntax (Erwartung wie F4):**
  - **F5 Ergebnis:** 35 Treffer, 7 im 24-Monats-Fenster (seit 2024-10-05). Kein Abstract nennt Schwerewellen,
    Tensorstoerungen oder Gravitonen (Treffer fuer "tensor" sind "tensorial GFT").
    - **V-F5a (Verstoss, mittel, RG2):** 2505.07951 (2025, skalare Stoerungen mit rekonstruierter Metrik): fuer einen
      einfachen Zustand "inhomogeneities do not follow the dynamics of general relativity in the semiclassical
      regime"; gequetschte Moden euklidische Signatur, schwingende Moden lorentzisch, aber andere Gleichungen.
      Erwartet war "Anfaenge"; gefunden: Anfaenge mit ausdruecklicher Abweichung von der ART.
    - 2311.14377 (2023): anisotrope Kondensate werden spaet isotrop (Friedmann), Anisotropie nur nahe am Rueckprall.
    - 2403.10741 (Oriti 2024, sinngemaess): Vorschlag einer Hydrodynamik auf dem (Mini-)Superraum; das Universum als
      Quantengravitations-Kondensat; Kosmologie aus der Hydrodynamik von "fundamental quantum simplices in a condensate
      phase" -> das Fluessigkeitsbild ist dort Programm (gedeutet), Grundlage OSW 2016 (gezeigt im
      Gross-Pitaevskii-Regime).
    - 2609.15969 (Sept. 2026): GFT-Dunkelenergie gegen DESI DR2 + Pantheon+; konservative Stoerungs-Priors
      unterdruecken Abweichungen von Lambda-CDM. Erster direkter Datentest (Hintergrund, nicht Wellen).
    - Erwartung korrigiert: GFT-Wellen-Physik ist nicht nur "Anfang", sondern im ersten konkreten Fall nicht ART-artig.

- **F6, 09:53:30, arXiv-API au:Volovik mit Einstein/wirksamer Gravitation/Tetraden, neueste zuerst:**
  - Erwartet: aeltere Arbeiten sagen, in He-3-A ist die wirksame Gravitation durch nicht-kovariante Terme
    verunreinigt, die Einstein-Wirkung ist klein bzw. nicht dominant. Neuere Arbeiten (2022-2026): Tetraden als
    Ordnungsparameter (Akama-Diakonov-Wetterich), Elastizitaets-Tetraden (Nissinen/Volovik), q-Theorie. Moeglicher
    Verstoss: Volovik behauptet in neuen Arbeiten, die Einstein-Wirkung entstehe in der gebrochenen Phase.
  - **F6 Ergebnis (09:53:46):** 40 Treffer; im 24-Monats-Fenster 2605.21047, 2601.00639, 2410.10549.
    - Bestaetigt RG1 Teil 1: 1108.5086 (Jannes/Volovik 2011/12): Fermionen und Eichbosonen am Weyl-Punkt "obey the
      same effective metric". RG1 Teil 2 indirekt (sinngemaess): in He-3-A entsteht eine bimetrische Gravitation mit
      Bezug zu Gravitonmassen, lambda von der Ordnung der Planck-Skala des Systems -> keine reine Einstein-Dynamik.
    - **V-F6a (Verstoss, gross, Finns Bild):** 2006.16821 (2020, sinngemaess): Das Quantenvakuum wird als
      "superplastic crystal" betrachtet; die wirksame Gravitation beschreibt seine dynamischen elastischen
      Verformungen. Ein
      Vakuum-Kristall, der plastisch fliessen kann und dessen Verformungen die Gravitation sind, ist Finns
      Kristall-Gas-Zwitter. Im Projekt nicht gelesen. Quelle des Begriffs pruefen (vermutlich Klinkhamer/Volovik,
      Elastizitaets-Tetraden, 2205.15222 Dzyaloshinskii/Volovik 1980).
    - Nachtrag F7 (09:54:43, 5 Treffer): "superplastic" erscheint bei Zubkov 2019 (1909.08412, "Emergent gravity in
      superplastic crystals": Fermionen an Gravitation gekoppelt, Gravitation Riemann ohne Torsion oder
      teleparallel; integrierte Spannungsanteile topologisch invariant) und in Volovik 2022/23 als "model of
      superplastic vacuum" (Begruendung fuer Metrik-Dimension 1/L^2). Zu Wellen, Scherung, Umordnung: nichts in den
      Abstracts. Bestaetigt die F7-Erwartung im Kern; "Gitterplaetze nicht erhalten" nicht belegt -> [L?] bleibt.
    - **V-F6b (Verstoss, gross, Frage 2):** 2601.00639 (Volovik, Jan. 2026): in Zwei-Fluessigkeits-Hydrodynamik des
      de-Sitter-Zustands eine Mode wie zweiter Schall, "massless and propagates at the speed of light"; gedeutet als
      masseloses Graviton; welcher Graviton-Typ das ist, laesst der Autor ausdruecklich offen. Erwartet war: kein
      Wellenbezug in Volovik-Fluessigkeitsbildern. Gefunden: neueste Arbeit macht das Graviton zu einer
      Schall-artigen (laengs, nicht quer) Fluessigkeitsmode; Tensorcharakter offen.
    - **V-F6c (Verstoss, mittel):** 2111.07817 (Volovik 2021, sinngemaess): Tetrade als Ordnungsparameter (Diakonov);
      die zugehoerigen Higgs-Moden sind in He-3-B massiv, in der ART geben sie "two massless gravitational waves".
      Zwei Regime derselben Struktur: Laborsystem massiv, ART masselos.
    - Erwartung korrigiert: Volovik ist nicht bei "nur Quasiteilchen-Metrik" stehen geblieben; neuere Arbeiten
      (2020-2026) behaupten Gravitationswellen-Moden in Kristall-, Tetraden- und Zwei-Fluessigkeits-Bildern.
      Gezeigt ist das jeweils nur im Modell bzw. per Analogie.

- **F7, 09:54:25, arXiv-API "superplastic" + Vakuum/Gravitation:**
  - Erwartet: Klinkhamer/Volovik ca. 2019 bis 2022, "superplastic vacuum": Zahl der Gitterplaetze nicht erhalten,
    Gitterkonstante frei, daher Gleichgewicht ohne Spannung (Lambda = 0). Ueber Querwellen/Scherung vermutlich
    nichts.
  - **F7 Ergebnis:** siehe Nachtrag bei F6 (5 Treffer, Zubkov 2019, Volovik 2022/23; zu Wellen nichts).

- **F8, 09:54:52, arXiv-API Sammelsuche: GWTC-4.0 Ausbreitung/Kosmologie (Xi_0, Reibung) ODER Pulsar-Timing
  Gravitonmasse:**
  - Erwartet: LVK 2025 (GWTC-4.0) mit Schranke auf modifizierte Ausbreitung (Xi_0 nahe 1, Fehler ~ 30 bis 50 %);
    PTA-Gravitonmasse m_g < ~1e-23 bis 1e-24 eV aus der Hellings-Downs-Form. Ausdrueckliche Daempfungs-Schranke
    ("viscosity of spacetime") erwarte ich dort nicht.
  - **F8 Ergebnis (09:55:14, 25 Treffer):**
    - Bestaetigt, mit Zahlen an der Quelle (Abstract):
      - LVK GWTC-4.0 Kosmologie (2509.04348, Sept. 2025): Xi_0 = 1,4 +1,0/-0,4 (68,3 %), 1,4 +2,8/-0,6 (90 %);
        Xi_0 = 1 ist ART. H0 = 75,4 +12,8/-9,1 (mit GW170817).
      - LVK GWTC-4.0 Tests II (2603.19020, Maerz 2026): keine Abweichung von der ART, auch nicht bei "dispersive or
        birefringent propagation"; m_g <= 1,92e-23 eV/c^2 (90 %).
      - PTA: NANOGrav 15 Jahre m_g < ~8,6e-24 eV, CPTA 3,8e-23 eV (2307.04680, 90 %); MeerKAT-PTA 4,5 Jahre
        m_g < 2,10e-23 eV (2607.14790, Juli 2026), getragen von der Quadrupol-Korrelation.
    - Keine ausdrueckliche Daempfungs-/Viskositaetsschranke im Fenster (wie erwartet).
    - Keine Verletzung. Aber die Xi_0-Schranke ist schwaecher als erwartet (90 % bis 4,2).
  - **Rechnung [ES] mit K1/K2 (nur Groessenordnung, Annahmen offen):**
    - Daempfung: d_GW/d_EM = exp(T/(2 tau)). Xi_0 (68 %) <= 2,4; bei z ~ 0,5 (Rueckblick ~5 Gyr) etwa
      d-Verhaeltnis <= 1,8 -> tau >= ~4 Gyr; mit 90 % (<= 2,8 bei z ~ 0,5) tau >= ~2,4 Gyr. Die Xi_0-Form passt
      nicht genau zu konstanter Daempfung; deshalb nur "tau von der Ordnung Gyr".
    - Dispersion: k-Luecke wirkt wie |m| c^2/hbar = 1/(2 tau). m_g <= 1,92e-23 eV -> tau >= hbar/(2 m_g c^2)
      = 6,58e-16 eV s / 3,84e-23 eV = 1,7e7 s (~0,5 Jahr). PTA 8,6e-24 eV -> tau >= 3,8e7 s (~1,2 Jahre).
    - ~~GW170817-Geschwindigkeit (F1): Delta v/c ~ 1/(8 (omega tau)^2) <= 3e-15 bei ~100 Hz -> omega tau >= ~6e6,
      tau >= ~1e4 s.~~
      [Berichtigung ~~10:10~~ [nach date 10:10:20]: falsche Seite der Schranke. In K1 ist die Gruppengeschwindigkeit > c, also gilt die
      obere Grenze +7e-16: 1/(8 (omega tau)^2) <= 7e-16 -> omega tau >= 1,3e7; bei omega = 2 pi 100 Hz = 628/s
      tau >= 2,1e4 s (~6 h). Groessenordnung unveraendert.]
    - Vorzeichen-Probe (Gegensweep, [M]): Die k-Luecke wirkt wie Re(omega)^2 = c^2 k^2 - 1/(4 tau^2), also wie ein
      NEGATIVES A_0 (tachyonartig, v_Phase < c, v_Gruppe > c). Die zitierten m_g-Schranken gelten fuer m_g^2 > 0.
      Die Uebersetzung tau >= hbar/(2 m_g c^2) ist deshalb nur Groessenordnung, kein Beleg.
    - Folge: Die Amplitude (Standardsirenen) schraenkt tau um 9 bis 10 Zehnerpotenzen staerker ein als Phase und
      Dispersion. omega tau >= ~1e19 bei 100 Hz.

- **F9, 09:55:49, arXiv-API Sammelsuche: Einstein-Aether nach GW170817 ODER Hess/Springel Voronoi-Lagrange:**
  - Erwartet: Aether-Kopplung |c13| <~ 1e-15 aus der Schwerewellen-Geschwindigkeit (Oost/Mukohyama/Wang 2018,
    Gong u. a. 2018). Hess/Springel 2010: Voronoi-Teilchenhydrodynamik aus einer diskreten Lagrange-Funktion,
    erhaelt Energie, Impuls, Entropie (ohne Schocks).
  - **F9 Ergebnis (09:56:08, 8 Treffer):**
    - Bestaetigt: Oost/Mukohyama/Wang 2018 (1802.04303): aus GW170817 "|c_13| <= 10^-15". Doppelpulsare engen den
      Rest um etwa eine Zehnerpotenz weiter ein (2104.04596). 2601.13061 (Jan. 2026): Graviton-Zahl der Tensormoden
      im Aether erhalten (keine Daempfung in naechster Ordnung).
    - **V-F9a (Verstoss, mittel, RG4/Uebernahme):** Hess/Springel 2010 (0912.0629) nennt im Abstract keine
      Lagrange-Herleitung und keine exakte Energieerhaltung, sondern (sinngemaess) die noetige kuenstliche
      Viskositaet und Korrekturkraefte, die die Teilchen geordnet und das Voronoi-Gitter regelmaessig halten.
      Auch Voronoi-Teilchen brauchen also (a) Dissipation fuer Schocks und (b) eine Ordnungskraft fuer gute Zellen.
      Parallele [ES]: TAKT-DYNAMIK-1 brauchte Delaunay als Auswahlregel.
- **F10, 09:56:24, arXiv-PDF 0912.0629 (Hess/Springel), pdftotext, grep "Lagrang", "conserv", "entropy":**
  - Erwartet: Bewegungsgleichungen aus einer diskreten Lagrange-Funktion mit Voronoi-Volumen; ohne kuenstliche
    Viskositaet erhalten Energie und Entropie; Ableitungen der Voronoi-Volumina stetig beim Nachbarwechsel.
  - **F10 Ergebnis (09:56:36, Volltext 1956 Zeilen):** bestaetigt, mit einer Zusatzstelle, die genau TAKT-DYNAMIK-1
    trifft:
    - Z. 90-93 (sinngemaess): Teilchenmodell aus einer diskretisierten Lagrange-Funktion, Massen je Element streng
      konstant.
    - Z. 183-197 (sinngemaess): Delaunay-basierte Dichte (DTFE) ist ungeeignet: Ein unendlich kleiner Schritt kann
      das Volumen der zugehoerigen Delaunay-Zelle endlich aendern; dann ist die thermische Energie keine stetige
      Funktion der Teilchenorte. Das ist der Befund von TAKT-DYNAMIK-1 (Gewicht je Tetraeder springt) in der
      Hydrodynamik, 2010 [ES].
    - Z. 195-200: Voronoi-Volumina haengen immer stetig von den Orten ab, weil Delaunay-Zuege genau dann geschehen,
      "when the corresponding Voronoi faces have vanishing area".
    - Z. 277-281 (sinngemaess): Die Lagrange-Form liefert von selbst Bewegungsgleichungen, die die Erhaltungssaetze
      erfuellen.
    - Z. 606-609 (sinngemaess): Auch mit Formkraeften in der Lagrange-Funktion bleiben Gesamtenergie, Impuls und
      Entropie genau erhalten. Z. 600ff: Ohne Formterme traegt VPH keine Wellen an der Nyquist-Frequenz regulaerer
      Gitter.
    - Folge [ES]: K5 ist Literaturstand. Fuer Finns Netz: Traegheit auf duale (Voronoi-/Umkugel-)Masse legen, aus
      einer Lagrange-Funktion ableiten; dann ist die Energie am Delaunay-Zug stetig. Das ist schaerfer als A2
      (Volumen je Tetraeder) in HODGE-MASSE-1, denn Tetraedervolumina springen am Zug (Z. 183-197).

- **F11, 09:56:56, arXiv-API: viskoelastisch / k-Luecke und Schwerewellen bzw. Raumzeit:**
  - Erwartet: wenige Treffer; holographische Viskoelastik (massive Gravitation im Bulk = viskoelastischer Festkoerper
    am Rand, Alberte/Baggioli/Pujolas); Daempfung von Schwerewellen in viskosen Medien. Keine Arbeit, die die
    Maxwell-k-Luecke auf Schwerewellen im Vakuum anwendet und mit Daten vergleicht.
  - **F11 Ergebnis (09:57:11, 28 Treffer, meist fachfremd):**
    - **V-F11a (Verstoss, klein):** Carcione/Ba 2024 (2405.20920): Schwerewellen ueber die Analogie
      linearisierte ART ~ Elektromagnetismus ~ Viskoelastik (SH-Wellen) mit Maxwell-Daempfungsterm; Phasen- und
      Energiegeschwindigkeit, Guete, Daempfung; Beispiele Sonne-Erde und Erde-Mond. Datenvergleich im Abstract
      nicht genannt. Es gibt also eine Maxwell-Schwerewellen-Theorie, aber (nach Abstract) ohne Datenschranke.
    - Gamble/Flurchick 2017 (1801.00350): "spacetime as a relativistic viscoelastic continuum", axiomatisch.
    - 2512.10905 (Dez. 2025): holographisch; Stoerungen eines AdS-Schwarzen-Lochs folgen viskoelastischer
      Hydrodynamik (Regime: Fluessigkeit am Rand, Gravitation im Inneren).
    - Kein Treffer verbindet die k-Luecke mit LIGO- oder PTA-Daten. Meine Rechnung K2/F8 ist deshalb [ES], nicht
      Literatur.

- **F12, 09:57:30, arXiv-API: DT/CDT/Kausalmengen und (gas/liquid/fluid/Schwerewellen/Graviton), neueste zuerst:**
  - Erwartet: keine Phase mit dem Namen Gas und flachem isotropem Grenzfall samt Schwerewellen. Treffer eher
    "gas of baby universes", Graviton-Propagator in CDT/EDT (Spektraldimension, de Sitter), Kausalmengen
    Kontinuum gegen Kristall. Im 24-Monats-Fenster hoechstens Einzelarbeiten.
  - **F12 Ergebnis (09:57:44, 22 Treffer):**
    - **V-F12a (Verstoss, gross, RG5/Frage 2):** In der Literatur zu Zufallsflaechen heisst "dynamisch
      trianguliert" schlicht "fluid": hep-lat/9305012 (1993, "Freezing a Fluid Random Surface"): ein Term mit dem
      Betrag der inneren Kruemmung friert die Zuege ein und interpoliert "between dynamically triangulated (ie
      fluid) and crystalline random surfaces". Auch Membranphysik (1405.1496 "self-avoiding fluid surface model on
      dynamically triangulated lattices"; flippy 2023) nutzt Kanten-Zuege als Modell fluessiger Membranen mit
      Biegesteifigkeit kappa. Erwartung korrigiert: Die "Gas/Fluessig"-Frage ist in DT keine Phase, sondern die
      Definition des Ensembles; Kristall = feste Verknuepfung.
      - [ES] Zwei Regime: In DT (gleichseitig) aendert jeder Zug die Fehlwinkel, darum kann ein Kruemmungsterm die
        Zuege einfrieren. In Finns eingebettetem Delaunay-Netz sind flache Zuege kruemmungsfrei (UMKLAPP-1); dort
        friert die Regge-Energie nichts ein.
    - **V-F12b (Verstoss, mittel, Gegensweep):** 2512.02782 (Dez. 2025): Fuer Kruemmungsschwankungen mit endlicher
      Korrelationslaenge ist "phase diffusion, rather than amplitude attenuation or mode mixing" die fuehrende
      Spur; Phasenvarianz waechst linear mit der Strecke; Planck-Schwankungen weit unter heutiger Empfindlichkeit.
      Erwartung korrigiert: Ein energieerhaltendes Raum-Gas zeigt sich zuerst als Phasendiffusion, ein
      dissipatives als Daempfung. Zwei Regime, zwei Datenspuren.
    - **V-F12c (Verstoss, mittel, Gegensweep):** 2106.01297 (2021): eine "certain sort of discrete Lorentzian
      simplicial complex" kann Minkowski nicht von einem bestimmten Schwerewellen-Ausbruch unterscheiden;
      Argument fuer Kausalmengen. Betrifft Simplex-Netze grundsaetzlich (Eindeutigkeit der Kontinuumsnaeherung).
    - 2504.11047 (Maas/Plaetzer/Pressler 2025): 4D-CDT, Kruemmung-Kruemmung-Korrelatoren "consistent with a massive
      state" (Geon-Hinweis), nach den Autoren hoechstens ein Hinweis. Keine masselosen Wellen gezeigt.
    - Keine Phase "Gas" mit flachem isotropem Grenzfall und Schwerewellen in DT, CDT oder Kausalmengen gefunden
      (24-Monats-Fenster abgedeckt, Treffer bis Juni 2026).

- **F13, 09:58:57, arXiv-API Gegensweep: Kritik an emergenter Gravitation / Analog- und Kondensatbildern, neueste
  zuerst:**
  - Erwartet: Weinberg-Witten als Hauptschranke; Analogmodelle liefern Kinematik, keine Einstein-Dynamik
    (Rueckwirkung); Lorentz-Feinabstimmung; im Fenster 1 bis 3 Arbeiten, eher Uebersichten.
  - **F13 Ergebnis (09:59:16, 30 Treffer, viel Rauschen):** Keine gezielte Kritik an Volovik- oder
    Kondensatbildern im Fenster; "Volovik" 0-mal, "condensate" 2-mal (nicht einschlaegig). Einschlaegig nur:
    2606.13522 (Juni 2026): vollstaendige Rueckgewinnung der ART verlange wirksame Metrik bzw. Kontinuumsgrenze
    bzw. "Einstein-like dynamics" plus Messbarkeitsbedingungen; Faelle u. a. Jacobsons Zustandsgleichung und
    Schwerewellen-Nachweis (methodische Kritik). 2507.16570 (2025): nichtlineare Analogmetrik in Graphen, Dynamik
    aus der Elektronen-Hydrodynamik, nicht aus Einstein-Gleichungen. Teilweise Verstoss gegen die Erwartung:
    Weinberg-Witten-Kritik im Fenster nicht gefunden. Aeltere Kritik (Carlip 2014, GLS 2008, BHS 2006) bleibt
    Stand. Urteil zu Kritik: "nach Recherchestand keine neue Gegenarbeit im Fenster", nicht "unbestritten".

- **F14, 09:59:36, arXiv-API Sammelabruf: Gompper/Kroll (Netzmodelle fluessiger Membranen, Kanten-Zuege) ODER
  Kleinert (Weltkristall ohne Schersteifigkeit, "floppy", zweite Gradientenelastizitaet):**
  - Erwartet: Gompper/Kroll: Netze mit Kanten-Zuegen = fluessige Membranen (kein Schermodul), feste Netze =
    polymerisierte Membranen (Schermodul); Biegesteifigkeit in beiden. Kleinert: Weltkristall, dessen Energie nur
    von Kruemmung (zweite Ableitungen) abhaengt, ergibt Einstein-Gravitation; "floppy" = ohne Scherrueckstellkraft.
  - **F14 Ergebnis (09:59:51, 2 Treffer):** **V-F14a (Verstoss, klein):** Gompper/Kroll nicht gefunden; Kleinerts
    Weltkristall mit zweiter Gradientenelastizitaet nicht auf arXiv. Einziger Kleinert-Treffer: Diamantini/
    Kleinert/Trugenberger 1999 (cond-mat/9903021) "Floppy Membranes": spannungsfreie Flaechen ohne aeussere
    Steifigkeit, Schwankungen nur durch Biegeelastizitaet vierter Ordnung, bleiben glatt (D = 2). Thema
    Membranen, nicht Raum. K3 bleibt [M]/[ES], gestuetzt nur durch Kleinert/Zaanen 2004 und hep-lat/9305012.
  - Lokal (~~10:01~~ [ungemessen; zwischen date 09:59:51 und 10:02:18], grep, kein Abruf): Dittrich/Hoehn (Pachner-Zuege als kanonische Zeitentwicklung) ist im Projekt
    schon gefuehrt: RUNDE-37/pachner-takt-1/KARTE.md, skalar-sektor-l/DOSSIER.md, RUNDE-41/42/46. Kein Abruf noetig.
    (grep brach nach 60 s ab, Liste unvollstaendig.)

## 3a. Zusatz der Leitung (eingegangen waehrend der Arbeit, aufgenommen 10:02:18 CEST, woertlich)

> Zusatz der Leitung 10:0x (Finn, 05.10., woertlich: "Check dazu auch noch mal navier stokes die Lösung die published wurde passt die zu unserem Modell?"). Gehoert zu deiner Karte, weil der Raum als Gas bzw. Fluessigkeit gedacht wird. RG1 bis RG5 bleiben unveraendert. Neu ist RG6, getrennt gekennzeichnet als "Zusatz der Leitung".
>
> **Stand der Leitung (eine WebSearch 10:0x, nur Suchtreffer, keine Primaerquelle):**
> - OpenAI hat am 08.09.2026 einen Beweis samt Lean-Formalisierung veroeffentlicht: Eine anfangs ruhende, glatte Fluessigkeit entwickelt unter glatter aeusserer Kraft bei endlicher Energie in endlicher Zeit eine Singularitaet.
> - OpenAI sagt, das sei nicht genau das Preisproblem.
> - Forscher fragen, wie das Ergebnis zustande kam.
> - Quellen-Kandidaten: https://openai.com/index/navier-stokes-solution/ und Presseberichte.
>
> **Bitte pruefen, an Primaerquellen:**
> 1. **Was genau ist bewiesen?**
>    - Raum (R^3 oder T^3), inkompressibel ja/nein, Art und Abklingen der Kraft, Energiebedingungen.
>    - Welcher Fefferman-Fall (A bis D) ist es, und warum nicht das Preisproblem?
>    - Gibt es Paper bzw. arXiv-Fassung und Lean-Code?
>    - Wer hat geprueft, und welche Kritik gibt es?
> 2. **Passt es zu Finns Modell? [H, ES]**
>    - (a) Fuer ein endliches Netz bzw. eine DEC-Diskretisierung mit Energieungleichung existieren Loesungen global; eine Kontinuums-Singularitaet zeigt sich dort als Kaskade bis zur Netzweite. Pruefe, ob das stimmt und ob es Literatur dazu gibt.
>    - (b) Der zaehe Term von Navier-Stokes ist auf Netzen ein Hodge-Laplace auf 1-Formen. Finns Takt ist 8 mal der Hodge-Laplace auf 0-Formen (TAKT-UMKLAPP-1). Gibt es DEC-Navier-Stokes auf Simplizialnetzen (z. B. Mohamed/Hirani/Samtaney), und was folgt daraus fuer ein Gas-Netz?
>    - (c) Gibt es eine veroeffentlichte Verbindung zwischen dieser Blow-up-Klasse und emergenter Raumzeit, Analog-Gravitation (akustische Metrik) oder Turbulenz-Kaskaden bzw. SOC?
> 3. **Vorhersagen der Leitung, vor deinen Abrufen notiert:**
>    - NS1 [H]: Bewiesen ist ein Blow-up mit Kraft fuer inkompressibles 3D-Navier-Stokes; die Kraft erfuellt die Abklingbedingungen des Preisproblems nicht. 55 %.
>    - NS2: Auf einem endlichen Netz gibt es keine Singularitaet; das ist vorab ableitbar, nur Kontrolle. 85 %.
>    - NS3 [H]: Eine veroeffentlichte Verbindung zu emergenter Raumzeit bzw. Quantengravitation gibt es nicht. 70 %.
>
> **Budget:** +5 Netzabrufe (also hoechstens 20) und +20 Minuten. Nimm diesen Zusatz woertlich in ARBEITSFELD.md auf und berichte RG6 bzw. NS1 bis NS3 in einem eigenen Abschnitt "Navier-Stokes" im DOSSIER.
>
> **Personen:** Nenne Personen nur als Autoren veroeffentlichter Arbeiten bzw. als Organisation.

- Anmerkung des Agenten: Die Nachricht nennt "RG6" als neu, gibt aber keinen RG6-Wortlaut; die Vorhersagen
  heissen NS1 bis NS3. Ich fuehre RG6 als Sammelname fuer NS1 bis NS3 und urteile nach deren Wortlaut. (Rueckfrage Q3.)
- Neues Budget: hoechstens 20 Abrufe (bisher 14 verbraucht), Zeitbox bis 11:02:40 CEST (Start + 80 min).
- Schreibtisch vor Abruf (NS2, [M]): Eine Galerkin- bzw. DEC-Diskretisierung mit endlich vielen Unbekannten ist ein
  ODE-System mit lokal Lipschitz-stetiger rechter Seite. Gilt eine Energieungleichung dE/dt <= -nu D + (f, u) mit
  D >= 0, dann bleibt E auf jedem endlichen Zeitintervall beschraenkt (Gronwall), in endlicher Dimension sind alle
  Normen gleichwertig, also gibt es keine Explosion in endlicher Zeit: globale Loesung. Voraussetzung: der
  Advektionsterm ist energieneutral diskretisiert ((B(u,u), u) = 0). Ohne diese Eigenschaft kann auch das ODE
  explodieren. Darum ist NS2 nur mit "energieerhaltender Advektion" vorab ableitbar.

- **F15, 10:02:52, WebFetch https://openai.com/index/navier-stokes-solution/ (Primaerquelle der Organisation):**
  - Erwartet: Datum 08.09.2026; Aussage: glatte, ruhende Anfangsdaten, glatte Kraft, endliche Energie,
    Singularitaet in endlicher Zeit, inkompressibel, 3D; Raum vermutlich R^3 oder T^3; Lean-Formalisierung;
    Hinweis, dass die Kraft die Abklingbedingungen der Clay-Fassung (Fefferman C bzw. D) nicht ganz erfuellt
    (z. B. nicht in der verlangten Raum-Zeit-Abklingklasse). Link auf Paper (arXiv oder PDF) und Lean-Repositorium.
    Pruefer: eher interne bzw. Lean-Kernel-Pruefung, externe Gutachten offen.
  - **F15 Ergebnis (~~10:03~~ [ungemessen; zwischen date 10:02:52 und 10:03:12]):** HTTP 403 Forbidden, kein Inhalt. Zaehlt als Abruf. Primaerseite der Organisation
    nicht gelesen.
- **F16, 10:03:12, WebSearch "OpenAI Navier-Stokes blow-up proof Lean September 2026 arXiv":**
  - Erwartet: Treffer mit Adressen des Papers (arXiv oder openai.com/PDF), des Lean-Repositoriums (GitHub) und
    Presseberichten (Quanta, Nature News, New Scientist); Stimmen von Mathematikern, eher vorsichtig ("nicht das
    Preisproblem", "Kraft ausgesucht"). Suchtreffer-Text ist keine Quelle; nur Adressen fuer F17.
  - **F17 Ergebnis (10:03:49, 30 Treffer, davon >= 10 direkte Folgearbeiten Sept. 2026, alle Abstract [S]):**
    - **V-F17a (Verstoss, gross, NS1/Preisfrage):** 2609.23868 (Petrillo/Glimm, 20.09.2026, sinngemaess): Am 7. und
      8. September 2026 habe programmatische Suche Singularitaeten geliefert: eine erzwungene NS-Singularitaet bei
      jeder festen Viskositaet, also "statements (C) and (D) of the Clay problem", dazu zwei Euler-Singularitaeten;
      der ungezwungene Fall (A), (B) bleibe offen. Diese Autoren ordnen das Ergebnis also Fefferman (C) UND (D) zu,
      nicht "Kraft ausserhalb der Abklingbedingungen". Erwartung (und NS1-Teil 2) dadurch in Frage gestellt.
    - 2609.10269 (Cao/Chi, 09.09., sinngemaess): baut auf der als gesichert behandelten kompakten, glatt erzwungenen
      OpenAI-Konstruktion auf; die Ergebnisse gelten fuer "spacetime-compact forces" und fuer die schnell abklingende
      Datenklasse der Clay-Fassung; Bruch aus der Ruhe auf R^3; keine eigene neue formale Verifikation.
    - 2609.10262 (09.09.): Kraft "remains smooth through the blowup time"; solche Kraefte dicht in relativem
      L^1_t H^s_x genau fuer s < 1/2, auf T^3 und R^3.
    - 2609.20803 (17.09.): OpenAI-Konstruktion mit C-unendlich-Kraft; Eigenschaften (i) anisotrope Typ-II-Schranken,
      (ii) exakt axialsymmetrischer Kern. Satz: Mit reell-analytischer Kraft sind solche Loesungen regulaer; die
      Kraft kann am Singularpunkt weder verschwinden noch analytisch sein. Grenze des Mechanismus, keine Widerlegung.
    - 2609.35406 (28.09.): lesbare Fassung des Profil-Teils von OpenAIs Manuskript "Finite Time Blowup for
      Navier-Stokes"; "We regard OpenAI's work as a major advance on the Navier-Stokes Millennium Prize Problem";
      Profile glatt, axialsymmetrisch; Teil II (Restkorrektur durch Pulse) angekuendigt.
    - 2609.17642 (Duraiswami, 15.09., kritisch-physikalisch, sinngemaess): Kern-Geometrie = exakte Wirbelstroemung
      zwischen poroesen Waenden (Gumerov/Duraiswami 1998); die Kegelbedingung entspricht Rayleighs Kriterium und
      verlangt Radien der Ordnung 10^20; eine echte Fluessigkeit kavitiert (Wasser) bzw. bildet Stoesse (Luft) vorher.
    - 2609.26790 (Cheskidov/Dai/Palasek, 22.09., Kaskaden, sinngemaess): inverse Energiekaskade (fruehere Arbeit
      2511.09556) gibt sofortigen Typ-I-Blow-up in scharfen Klassen; im Obukhov-Schalenmodell Vorwaertskaskade ohne
      Kraft mit Blow-up "comparable to the recent forced Navier-Stokes blow-up of OpenAI". 2609.13056
      (Schorlepp/Rosenhaus/Falkovich, 11.09.): Wirbel-Instanton in Turbulenz, nach den Autoren auffallend aehnlich
      zum OpenAI-Mechanismus.
    - 2609.23868 ausserdem (sinngemaess): Lean-4-Saetze ueber Mathlib, die Bibliothek enthaelt aber kein NS-Objekt
      (NS nur als Annahme); keine endliche Rechnung bezeugt eine Galerkin-gleichmaessige Obergrenze; im Rechentest
      (128^3, 256^3) bricht die Fluss-Untergrenze in der Skala an der Kolmogorov-Wellenzahl -> Stuetze fuer
      Zusatz 2(a) [S Abstract].
    - Keine arXiv-Fassung des OpenAI-Manuskripts in den Treffern; Titel laut 2609.35406 "Finite Time Blowup for
      Navier-Stokes".
  - **F16 Ergebnis (~~10:03~~ [ungemessen; zwischen date 10:03:12 und 10:03:37]):** 9 Adressen, nur Presse/Blogs (rits.shanghai.nyu.edu, theneuron.ai, lilting.ch,
    interestingengineering.com, unite.ai, pebblous) und die gesperrte openai.com-Seite. Suchtext (keine Quelle,
    nur Hinweis): Ankuendigung 08.09.2026; Mechanismus ein Wirbel, der sich nach innen windet und streckt; einen
    Tag zuvor Lean-gepruefte Blow-up-Beweise "for related fluid equations" einer anderen Autorengruppe;
    Streit um Urheberschaft. Kein Paper-Link im Suchtext. **V-F16a (klein):** Es gibt eine zweite, fruehere
    Arbeit (07.09.2026) zu verwandten Gleichungen; das stand nicht in der Leitungs-Notiz.
- **F17, 10:03:37, arXiv-API: Navier-Stokes/Euler blow-up mit Lean bzw. formal, eingereicht ab 2026-08, neueste
  zuerst:**
  - Erwartet: die Arbeit vom 07.09.2026 (verwandte Gleichungen, z. B. Euler mit Rand, Boussinesq oder
    verallgemeinertes NS) auf arXiv; die OpenAI-Arbeit vielleicht nicht auf arXiv. Erste Kommentar-Arbeiten
    moeglich.
- **F18, 10:04:46, WebFetch Wayback-Abbild der OpenAI-Seite
  (https://web.archive.org/web/2026/https://openai.com/index/navier-stokes-solution/):**
  - Erwartet: Wortlaut der Organisation: R^3 (vermutlich), inkompressibel, Ruhe-Anfangsdaten, glatte kompakte Kraft,
    endliche Energie, Wirbelkern; Bezug auf Fefferman (C)/(D) und ein Vorbehalt "nicht genau das Preisproblem"
    (vermutlich: Preis verlangt Begutachtung/Veroeffentlichung, oder Geist der Frage = ohne Kraft). Links auf
    Manuskript-PDF und Lean-Code.
  - **F18 Ergebnis (~~10:05~~ [ungemessen; zwischen date 10:04:46 und 10:05:29]):** Werkzeug verweigert web.archive.org ("unable to fetch"). Kein Inhalt. Vorsorglich als
    Abruf gezaehlt. Umgehung per curl oder mit Browser-Kennung (openai.com 403) mache ich nicht.
    -> Wortlaut der Organisation bleibt ungelesen; Theorem nur ueber Folgearbeiten (Selbstanzeige).
- **F19, 10:05:29, arXiv-API Sammelsuche fuer Zusatz 2(a)-(c) und NS3:**
  (DEC + Navier-Stokes) ODER (spektral abgeschnittenes Euler + Thermalisierung) ODER (Titel Navier-Stokes + Einstein)
  ODER (Navier-Stokes + blow-up/Singularitaet + emergente Raumzeit/Analoggravitation/akustische Metrik/
  Quantengravitation/holographisch/fluid-gravity).
  - Erwartet: Mohamed/Hirani/Samtaney 2016 (DEC-NS auf Simplizialflaechen, Stromfunktion bzw. 1-Formen,
    Hodge-Laplace); Elcott u. a. 2007 eher nicht auf arXiv; Cichowlas u. a. 2005 (abgeschnittenes Euler
    thermalisiert, Energie staut sich an der Abschneide-Wellenzahl); Bredberg/Keeler/Lysov/Strominger 2011
    ("From Navier-Stokes to Einstein"); fluid/gravity mit Turbulenz (Eling/Fouxon/Oz 2010, Adams/Chesler/Liu
    2013). Zur Blow-up-Klasse selbst und emergenter Raumzeit: nichts (NS3 eher eingetroffen), hoechstens die
    allgemeine Frage "NS-Singularitaet <-> Horizont" in fluid/gravity.
  - **F19 Ergebnis (10:05:44, 34 Treffer):**
    - Bestaetigt (2b): Mohamed/Hirani/Samtaney 2015/16 (1508.01166): DEC-NS auf Simplizial-Flaechennetzen; Masse
      und Wirbelstaerke "conserved up to machine precision"; kinetische Energie (reibungsfrei) nur mit Fehler
      zweiter Ordnung in Netzweite und Zeitschritt. Nur Flaechen (2D); 3D nur hybrid DEC + Fourier (2409.04731).
    - **V-F19a (Verstoss, gross, Zusatz 2(a)/(b) und Kern der Karte):** Korn 2026 (2605.16554, Mai 2026,
      sinngemaess): kompressibles barotropes NS auf Delaunay-Voronoi-Netzen per DEC: Jede dichteunabhaengige
      Massematrix mit partiell-integrationstreuer Divergenz traegt ein scharfes O(h^2)-Energieresiduum unbestimmten
      Vorzeichens, das keine Operatorwahl beseitigt; "The density-weighted mass matrix is the unique algebraic
      remedy" und stellt die exakte Gesamtenergie her; fuer das dichtegewichtete Verfahren globale Wohlgestelltheit
      fuer nu >= 0 in d = 2, 3. Parallele [ES]: TAKT-DYNAMIK-1
      fand einen Energiesprung unbestimmten Vorzeichens (Lesart R daempft, P verstaerkt) mit gleichem Gewicht je
      Zelle. Korn: ohne Masse/Dichte im Gewicht bleibt ein Residuum, mit ihr exakte Energie. Das stuetzt die
      Richtung von HODGE-MASSE-1 (A2), aber Korns Netz bewegt sich nicht; Umklappen ist dort nicht behandelt.
    - Korn 2026 (2605.13048, inkompressibel, Delaunay-Voronoi auf geschlossenen Mannigfaltigkeiten): Energie- und
      Kelvin-Erhaltung; "at the discrete level, energy conservation is a stability property"; Grenzwerte der
      diskreten NS sind Leray-Hopf-Schwachloesungen. Stuetzt 2(a) [S Abstract].
    - Thermalisierung (2(a)): Cichowlas/Bonaiti/Debbasch/Brachet 2005 (nlin/0410064): abgeschnittenes Euler bildet
      thermalisierte Moden zwischen einer Uebergangs- und der Hoechst-Wellenzahl; sie wirken als Dissipation auf
      grosse Skalen. 2209.05046 (2022): Galerkin-abgeschnittenes 3D-Euler relaxiert ins absolute Gleichgewicht
      (Gibbs, Gleichverteilung) und kann "evidence for or against finite-time blow-up" in Rechnungen verzerren.
    - NS <-> Einstein (2(c)/NS3): Bredberg/Keeler/Lysov/Strominger 2011 (1101.2451): zu jeder Loesung des
      inkompressiblen NS in p+1 Dimensionen gibt es eine duale Vakuum-Einstein-Loesung in p+2 Dimensionen.
      Allgemeine Abbildung, kein Bezug auf die Blow-up-Klasse. Ein Treffer zu "NS-Blow-up und emergente Raumzeit
      bzw. Analoggravitation" fehlt.
- **F20 (letzter Abruf), 10:06:24, arXiv-PDF 2609.35406 (lesbare Fassung Teil I), pdftotext, grep:**
  - Erwartet: Satz in der Einleitung: R^3 (oder R^3 und T^3), inkompressibel, nu > 0 fest, u0 = 0, Kraft
    C-unendlich mit kompaktem Traeger in Raum und Zeit, endliche Energie, Blow-up zur Zeit T; Bezug auf Fefferman
    (C)/(D); Literaturangabe des OpenAI-Manuskripts mit Adresse; Lean erwaehnt; Pruefstand: Teil II offen.
  - **F20 Ergebnis (10:06:43, Volltext 13 955 Zeilen, Lei/Ren, v2 vom 29.09.2026):**
    - Bestaetigt: Konstruktion axialsymmetrisch, glatt; Inkompressibilitaet im Profilansatz (Z. 228, Abschn. 1.2:
      radiales Druckgleichgewicht und Inkompressibilitaet legen P und U^r fest). Teil II (Restkorrektur durch Pulse)
      offen. Einziges Zitat: "We regard OpenAI's work as a major advance on the Navier-Stokes Millennium Prize
      Problem" (Abstract, Z. 13-14; 13 Woerter).
    - Literaturangaben: [21] OpenAI, "Finite Time Blowup for Navier-Stokes", Manuskript vom 8. September 2026,
      166 S.; [22] OpenAI, "Finite Time Blowup for the Euler Equation", 8. September 2026, 57 S. (nach Lei/Ren:
      ungezwungener Euler-Blow-up aus glatten, kompakt getragenen Anfangsdaten); [2] Alpoege/Buckmaster 2026,
      "Blowup for the Euler equations with smooth forcing" (R^3, glatte Daten, glatte Kraft). Keine Adresse fuer
      [21]/[22].
    - **V-F20a (Verstoss, mittel):** Keine Clay-Fall-Zuordnung (A bis D) in Lei/Ren, kein Wort zu Lean; Erwartung
      "(C)/(D) und Lean hier" verfehlt. Die (C)/(D)-Zuordnung steht nur bei 2609.23868 (Abstract).
    - **V-F20b (Verstoss, mittel):** OpenAI hat am selben Tag ein zweites Manuskript zu UNGEZWUNGENEM Euler-Blow-up
      aus glatten, kompakt getragenen Daten veroeffentlicht. Das stand nicht in der Leitungs-Notiz.
    - Abrufbudget erschoepft (20 von 20).

## 4. Erwartungsverstoesse (das eigentliche Ergebnis; Rangfolge ~~10:11~~ [ungemessen; zwischen date 10:10:20 und 10:12:30])

1. V-F12a: "dynamisch trianguliert" heisst in der Zufallsflaechen-/Membranliteratur "fluid"; Kruemmungsterm friert
   die Zuege ein (hep-lat/9305012). Gas = DT-Ensemble, keine Phase.
2. V-F3a/V-F3b + F10 + V-F19a: Erhaltung im Moving Mesh aus Flussform (AREPO) bzw. Lagrange-Form (VPH), nicht aus
   den Nullflaechen; AREPO wandelt Bewegung in Waerme ("spurious dissipation"); Delaunay-Zellgewichte springen,
   Voronoi-Gewichte nicht (Hess/Springel = TAKT-DYNAMIK-1-Befund); Korn 2026: Massematrix ohne Dichte ->
   Energieresiduum unbestimmten Vorzeichens.
3. V-F6a/b/c: Volovik ueber Quasiteilchen hinaus: superplastischer Vakuumkristall (2020), Tetraden-Higgs-Gravitonen
   (2021), masseloses "Zweiter-Schall-Graviton" in de Sitter (2026, Typ offen).
4. V-F17a/V-F20a: Folgearbeiten ordnen den NS-Blow-up Clay (C) und (D) zu und nennen kompakte Kraefte in der
   Clay-Datenklasse; Gegenteil von NS1-Teil 2; OpenAI-Wortlaut ungelesen.
5. V-F12b: Kruemmungsschwankungen -> Phasendiffusion statt Daempfung (2025). Zwei Datenspuren.
6. V-F5a: GFT-Inhomogenitaeten folgen im einfachen Fall nicht der ART (2025).
7. V-F12c: diskrete lorentzsche Simplex-Komplexe unterscheiden Minkowski nicht von einem Wellenausbruch (2021).
8. V-F1a: kein Graph endlicher Valenz Lorentz-vertraeglich; Gas-Netz = Ruhesystem = Aether (|c13| <= 1e-15).
9. V-F20b/V-F16a: zweites OpenAI-Manuskript (ungezwungenes Euler) und eine fruehere verwandte Arbeit (07.09.).
10. V-F9a, V-F11a, V-F14a, V-F1b, V-F1c: klein.

## 4a. Gegensweep (Regel 4), ~~10:11~~ [ungemessen; zwischen date 10:10:20 und 10:12:30]

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- G1 "Die Schwerewellen-Daten stimmen in der Amplitude mit der ART." GEPRUEFT (F8): Xi_0 = 1,4 +1,0/-0,4; die ART
  liegt genau am unteren Rand des 68-%-Intervalls. Kein Signal (Populationsmodell-abhaengig), aber auch nicht
  "perfekt ART". Die Richtung Xi_0 > 1 ist die Richtung einer Daempfung. Muss im Dossier stehen, ohne Deutung.
- G2 "Die m_g-Schranken begrenzen die k-Luecke." GEPRUEFT ([M]): Vorzeichen verschieden (k-Luecke ~ A_0 < 0).
  Nur Groessenordnung.
- G3 "Die GW170817-Schranke gilt fuer die Gruppengeschwindigkeit, und die Seite ist -3e-15." GEPRUEFT: Seite war
  falsch (berichtigt auf +7e-16).
- G4 "Finn meint mit Gas das Netz." GEPRUEFT an den Quellen: weitere Lesarten gefunden: Kondensat/"Gas" von
  Quanten-Simplizes (GFT, 2403.10741), verduenntes Gas von Wurmloechern (BABY-UNIVERSUM-L), thermodynamische
  Zustandsgleichung (Jacobson 1995), Bose-Gas-Analog (GLS 2008).
- G5 "Ein Planck-Gas hat tau ~ Planck-Zeit." NICHT geprueft, [H]. Traegt den Schluss "Scherung ausgeschlossen".
- G6 "Duale Gewichte sind auch am 3-2-Zug im gekruemmten Netz stetig." NICHT geprueft; TAKT-DYNAMIK-1 TD0 zeigt
  Rest ~ Fehlwinkel. Offen.
- G7 "OpenAI-Satz ist inkompressibel, 3D, R^3." TEILS geprueft: inkompressibel und axialsymmetrisch bei Lei/Ren
  (Volltext); R^3 und T^3 nur aus Abstracts von 2609.10262/10269; Kraftklasse nur aus Folgearbeiten.

## 4b. Kalibrierung (~~10:11~~ [ungemessen; zwischen date 10:10:20 und 10:12:30])

- (a) gemessen: Datenschranken (Xi_0, m_g, Delta v/c, c13), Projektzahlen (TD-1, UK-1, TG-2), Volltextstellen
  Springel/Hess-Springel/Lei-Ren.
- (b) nuetzlich verdichtet: Scherung-gegen-Kruemmung-Kette (K3, K4, K5, K6), tau-Uebersetzung (K2), Zwei-Regime-
  Tabelle, GAS-NETZ-1.
- (c) gewachsene Gewissheit ohne neue Evidenz: "Kruemmung entkoppelt vom Maxwell-Mechanismus" fuehlt sich seit F2
  sicherer an; neue Evidenz dafuer ist nur Analogie (Kleinert/Zaanen, Membranen, DT = fluid), keine Rechnung an
  Finns Netz mit Gas-Bewegung. Warnzeichen: Die Frage hat sich in 3 Teilfragen aufgeloest (statisch, Zug-Energie,
  3-2-Rest), meine Sicherheit stieg dabei. Gehoert in den Bericht.

## 5. Offene Rueckfragen (wandern mit)

- Q1 Gilt K4 (keine statische Schersteifigkeit) auch fuer die Glas-Netze mit Umklappen, oder nur ohne?
- Q2 Ist die Sprungursache in TAKT-DYNAMIK-1 (A0 je Tetraeder) mit dualem Gewicht (K5) vorab null? Nicht nachrechnen,
  nur als Vorschlag fuehren. -> In GAS-NETZ-1 aufgenommen (2-3-Zug vorab stetig, 3-2-Rest offen).
- Q3 (an die Leitung) Die Zusatz-Nachricht nennt RG6 ohne Wortlaut. Ich urteile ueber NS1 bis NS3 und fuehre RG6 als
  Sammelname. Bitte bestaetigen oder Wortlaut nachreichen.
- Q4 OpenAI-Primaerseite (403) und Manuskript-Adresse ungelesen. Wer Zugriff hat: Wortlaut zu "nicht genau das
  Preisproblem" und Kraftklasse nachlesen.
- Q5 GW170817-Standardsirene (Abbott u. a. 2017, Nature) fuer eine saubere tau-Schranke ueber 130 Mio. Jahre nicht
  gelesen (Budget).

## 6. Gestrichen

- ~~F2-Zeit "09:51 (date 09:50:49 + Schreibzeit)"~~ (geschaetzt; berichtigt bei F2).
- ~~omega tau >= ~6e6 aus der Seite -3e-15~~ (falsche Seite; berichtigt in F8-Rechnung).
- ~~10:14 bis 10:16~~ [Berichtigung: Endzeit war vorab geschaetzt; gemessen: nach date 10:12:30 begonnen, fertig
  bei date 10:14:54]: Mehrfachzitate je Quelle auf Paraphrase umgestellt (Regel: hoechstens ein kurzes Zitat je Quelle,
  unter 15 Woertern). Inhalt, Fundstellen und Zeilennummern unveraendert; die woertlichen Fassungen stehen in
  quellen/ (Rohdaten), nicht mehr im Feld. Ein Zitat ueber 15 Woerter (Volovik 2020) gekuerzt.

## 7. Abschluss

- Dossier fertig geschrieben, Abschluss 2026-10-05 10:22:36 CEST (date). Abrufe 20 von 20. Keine weiteren Netzabrufe.
