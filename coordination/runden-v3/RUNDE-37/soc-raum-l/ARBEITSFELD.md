# SOC-RAUM-L: Arbeitsfeld (feldforscher fuer die Leitung claude-primary)

- Start 2026-10-05 09:58:17 CEST (date). Arbeitsfeld angelegt ab 10:03:26 CEST (date).
- Zeitbox 60 min (bis etwa 10:58, Grenze aus der Startzeit gerechnet), hoechstens 15 Netzabrufe.
- Regel: vor jedem Abruf hier Erwartung mit Zeit (date), danach Ausgang. Gestrichenes bleibt stehen (~~so~~).
- Kennzeichen: [E] [M] [S] [L] [H] [P], dazu [ES] eigener Schluss.

## A. Gelesen (Projekt, nur lesen) [P]

- URSUPPE-1 (R22), Ergebnis 1-4: Zufallsgraphen ohne Regel kein Plateau der spektralen Dimension; "viele Dreiecke"
  klumpt (K7-Klumpen); Flaechenregel gibt Flicken mit Raendern; CDT umgeht das mit Bausteinen fester Dimension.
- UMKLAPP-1 (R46), Abschnitt 2: flacher 2-3-Zug kostet keine Regge-Energie (|Delta S| <= 3,6e-12, UK0);
  Delaunay-Umklappanteil phi_T ~ 7,5 a, Steigung 0,95, ohne Schwelle im Mittel (UK1); je Netz eine Schwelle
  (kleinster Randabstand); 96 % Einzelzuege bei a = 1e-3; Anteil der Flaechen mit Randabstand < x waechst wie
  x^0,958 (~2 x), also endliche Dichte bei null. Zufallszuege machen instabil (UK2 verfehlt).
- TAKT-DYNAMIK-1 (R47), Abschn. 2 und 5: Delaunay-Zuege waehrend der Welle stabil, Zufallszuege nicht; Energie ueber
  Zuege nicht erhalten (je Zug 0,2-0,46 % H0; Lesart R verliert, Lesart P gewinnt); Regge-Energie beim 2-3-Zug exakt
  stetig [M]; Sprung sitzt in der Bewegungsenergie (A0, J = 1); 3-2-Zug aendert in Ordnung des Fehlwinkels der
  wegfallenden Kante; Wirkung ~ A (Zahl der Zuege ~ A); bei echter GW-Dehnung ~1e-21 entsprechend weniger Zuege.
- TT-GLAS-2: Berichtigung (nur 112 k-Klassen, nicht ganze Zone); Spanne ~ N^(-0,56) (95 %: -0,65 bis -0,48),
  4,66 % bei N = 1024; Anisotropie sitzt in der Traegheit/Projektion, nicht in Relaxation.
- WELTKRISTALL-L, H1: DT-Lambda = kleiner Abstand der nackten Kopplung zur Zaehl-(Entropie-)Schwelle, Feinabstimmung
  noetig (AGJL 2012 Abschn. 7.1, S. 68 [S dort]); reine Zaehlung ergibt Knaeuel (S. 83); Zufallsform N^(-1/2) nur in 4D
  ~ Lambda.
- GEMEINSAMES-NETZ v4.1, Abschn. 0 und 2: L2 Isotropie (GW170817 ~1e-15 gegen Netz V 6,34 %, Glas ~N^(-1/2)); L3;
  L10: drei Befunde zeigen auf die Bewegungsenergie; HODGE-MASSE-1 laeuft (volumengewichtete Bewegungsenergie).

## B. Bausteine verketten, vor jedem Abruf (Schreibtisch)

- **B1 [M, ES]:** Fuer Punkte in allgemeiner Lage ist die Delaunay-Zerlegung eindeutig, also eine Funktion der Lagen.
  Bei stetigem, langsamem Antreiben aendert sie sich nur, wenn fuenf Punkte kosphaerisch werden; generisch ist das ein
  einzelner 2-3- oder 3-2-Zug. Im Grenzfall langsamen Antreibens hat die rein geometrische Delaunay-Regel also
  Lawinengroesse 1 und kein Gedaechtnis (keine Hysterese, keine gespeicherte "Spannung").
  Passt zu UMKLAPP-1 (96 % Einzelzuege, phi_T proportional a) [P]. Folge: Rein geometrisches Delaunay-Umklappen ist
  kein SOC-Kandidat; es braucht eine Rueckkopplung (Zug -> Kraefte -> Lagen) oder eine Hysterese (Zug erst bei
  Randabstand < -eps).
- **B2 [M, P]:** Schlaefli: dS/dl_e = delta_e. Beim flachen 2-3-Zug bleiben die Fehlwinkel aller alten Kanten gleich,
  die neue Kante hat delta = 0 (TD Abschn. 2.2/5.2 [P]). Also aendert ein 2-3-Zug weder Energie noch Kraefte im
  Regge-Teil; beim 3-2-Zug nur in Ordnung des Fehlwinkels der wegfallenden Kante. Die Kopplung von Zug zu Zug laeuft in
  Finns Netz heute nur ueber die Bewegungsenergie (A0, J = 1), die HODGE-MASSE-1 gerade stetig machen will [ES].
- **B3 [L, zu pruefen]:** SOC braucht neben Antreiben, Schwelle, Umverteilung auch Erhaltung im Inneren bzw.
  verschwindende Ableitung; versteckte Abstimmung = Verhaeltnis Antreiben/Ableitung -> 0 (Dickman u. a. 2000;
  Bonachela/Munoz 2009).
- **B4 [P, ES]:** UMKLAPP-1 misst fuer das ungetriebene Poisson-Delaunay-Netz theta ~ 0 (Dichte der Randabstaende bei
  null endlich). Marginal-Stabilitaetstheorie (zu pruefen): getriebene amorphe Festkoerper haben eine Pseudoluecke
  P(x) ~ x^theta mit theta > 0. -> moeglicher Unterscheidungspunkt im Projekt: theta nach langem Antreiben.
- **B5 [P, L]:** In DT wird Lambda auf lambda_c abgestimmt (AGJL 2012, ueber WELTKRISTALL-L). In Simulationen wird
  meist N fest gehalten (kanonisch), dann faellt lambda heraus; das ist eine Ensemblewahl, keine Dynamik [L].
  kappa0 und Delta muessen weiter an eine Uebergangslinie zweiter Ordnung [L].

## C. Vorhersagen der Karte (unveraendert) und meine Lage vorab

| Nr | Kurz | Wahrsch. Karte | meine Lage vorab |
|---|---|---|---|
| SO1 | SOC-QG-Arbeiten gibt es (mind. Ansari/Smolin 2008); keine mit Kontinuumsgrenzfall + GW | 70 % | eher ein |
| SO2 | kein gezeigter Selbstabstimm-Mechanismus in Regge/DT/CDT | 70 % | eher ein |
| SO3 | amorphe Festkoerper: potenzgesetzliche plastische Lawinen; T1-Lawinen in Schaeumen dokumentiert | 80 % | ein; Schaum-Teil unsicher (Durian/Dennin fanden teils lokale Ereignisse) |
| SO4 | Schranken schliessen SOC-Raum mit Planck-naher Lawinenskala nicht aus; Ausschluss braucht Modellabbildung | 55 % | eher ein, aber "random walk"-Rauschen ist ausgeschlossen |

## D. Abrufplan (hoechstens 15)

- F1 arXiv-API, Abstracts per id_list: Ansari/Smolin, Quantum Graphity, Caravelli/Markopoulou, Trugenberger,
  Kelly/Trugenberger/Biancalana, Bianconi/Rahmede, Khoury u. a., Giudice u. a. (IDs aus dem Gedaechtnis, Titel pruefen).
- F2 arXiv-API, Suche SOC + Quantengravitation/Raumzeit, nach Datum (24-Monats-Pflicht).
- F3 arXiv-API, Titelsuche Marginal-Stabilitaet/Fliessen (Lin u. a. 2014, Mueller/Wyart 2015), Kritik (Dickman u. a.
  2000, Bonachela/Munoz 2009, Watkins u. a. 2016), Jamming (O'Hern u. a. 2003).
- F4 arXiv-API, Schaum-T1-Lawinen (Durian 1995, Tewari u. a. 1999, Dennin, Kabla/Debregeas).
- F5 arXiv-API, Raumzeit-Rauschen (Holometer 2016/2017, Perlman u. a. 2015, neuere LIGO/GQuEST).
- F6 Kritik an SOC, letzte 24 Monate.
- F7 Gittergravitation + Selbstabstimmung (DT/CDT/Regge + self-organized/self-tuning), letzte 24 Monate.
- F8 bis F15: Volltexte fuer Exponenten, Gegensweep, Reserve.

## E. Abrufe: Erwartung vorher, Ausgang nachher

- **F1 Erwartung (10:04:13, date):**
  arXiv-API id_list hep-th/0412307, 0801.0861, 1008.1340, 1610.05934, 1901.09870, 1511.04539, 2003.12594, 2105.08617.
  Erwartet: Ansari/Smolin schlagen eine Spin-Netz-Evolution mit Sandhaufen-artiger lokaler Regel vor und finden
  numerisch Potenzgesetze (SOC), ohne Kontinuumsgrenzfall und ohne Schwerewellen. Graphity: Abkuehlen (abgestimmte
  Temperatur) statt SOC; Caravelli/Markopoulou: Tieftemperaturzustaende sind keine regulaeren Gitter. Trugenberger:
  Phasenuebergang zu geometrischer Phase bei abgestimmter Kopplung. Bianconi: wachsende Komplexe, emergente
  hyperbolische Geometrie, kein SOC-Anspruch. Khoury u. a.: Landschaft/Multiversum als SOC (Higgs nahe kritisch).
  Giudice u. a.: Selbstorganisierte Lokalisierung (kosmologisch, nahe kritisch). Einige IDs koennen falsch sein.
- **F1 Ausgang (Abrufe 1 und 2; ~~Auswertung ab 10:05~~ [geschaetzt; berichtigt: nach 10:04:24 (Abruf 2) und vor 10:05:10 (F2-Erwartung), beides date]):** weitgehend bestaetigt, eine Zeile je Quelle, Verstoesse ausgefuehrt.
  - Ansari/Smolin (hep-th/0412307, CQG 25:095016): bestaetigt (Sandhaufen-Analogie, "some correlation functions become
    scale invariant"). **Verstoss klein:** Es entwickeln sich nur die Spins auf einem **festen Graphen** ("frozen spin
    networks ... evolve on a fixed graph"); Geometrie/Verknuepfung selbst ist nicht dynamisch. Damit ist es von Finns
    Umklapp-Dynamik weiter entfernt als erwartet.
  - Konopka/Markopoulou/Severini (0801.0861): bestaetigt; Ordnung in einer Niedrigenergie-Phase (Abkuehlen), kein SOC.
  - Caravelli/Markopoulou (1008.1340): **Verstoss:** Meine Erinnerung "Tieftemperaturzustaende sind keine regulaeren
    Gitter" steht nicht im Abstract (Mittelfeld, Valenz als Ordnungsparameter). Wird nicht behauptet.
  - Trugenberger (1610.05934): bestaetigt, Quantenphasenuebergang = kritischer Punkt (abgestimmt).
  - Kelly/Trugenberger/Biancalana (1901.09870): bestaetigt im Kern (kontinuierlicher Uebergang = UV-Vervollstaendigung,
    also abgestimmter Punkt). **Fuer URSUPPE-1 wichtig:** Zufallsgraphen mit Ollivier-Kruemmungs-Wirkung ordnen sich zu
    "cubic complexes up to defects" (Wirkungsminima); es gibt also eine lokale Regel, die aus einer Suppe Geometrie macht.
  - Bianconi/Rahmede (1511.04539): bestaetigt; Nichtgleichgewichts-Wachstum, verallgemeinertes Flaechengesetz, kein SOC.
  - Kartvelishvili/Khoury/Sharma (2003.12594): **Verstoss mittel:** Trotz Titel "Self-Organized Critical" liegt die
    Kritikalitaet "precisely at the critical Page lifetime distribution", also an einem abgestimmten Punkt; das
    Selbstorganisierende kommt aus einem gesonderten Auswahlargument (Suchoptimierung). 1/f-Spektrum dort gezeigt.
  - Giudice/McCullough/You (2105.08617): bestaetigt; Phasenuebergaenge als Attraktoren, Parameter "localised around the
    critical value", auch fuer kleines Lambda vorgeschlagen (Kontinuum, Inflation, kein Gitter).
- **F2 Erwartung (10:05:10, date):**
  arXiv-API-Suche (Abstract) "self-organized/organised criticality" UND (quantum gravity | spacetime | space-time |
  cosmological constant | triangulation | emergent geometry), nach Datum absteigend, 40 Treffer. Erwartet: wenige
  Arbeiten, vor allem Kosmologie/Landschaft und Netzwerk-Analogien; in den letzten 24 Monaten (ab 10/2024) hoechstens
  ein bis drei Arbeiten, keine mit Kontinuumsgrenzfall und Schwerewellen; keine Gitter-QG-Arbeit mit Selbstabstimmung.
- **F2 Ausgang (Abruf 3; ~~Auswertung ab 10:06~~ [geschaetzt; berichtigt: nach 10:05:16, vor 10:05:48, date]):** im Kern bestaetigt (keine Arbeit ab 10/2024 mit diesen Begriffen im
  Abstract; keine mit Kontinuumsgrenzfall und Schwerewellen). **Verstoss klein:** Die Ansari/Smolin-Linie lebt weiter:
  Chen/Zhu 2008 (IJMPA 23:3891, gr-qc/0701175; Graph fest, nur Farben), Dantas 2021 (CQG, 10.1088/1361-6382/ac25e1,
  arXiv 2105.11958: Potenzgesetz der Lawinengroessen, "slowly expanding, 2-dimensional dual (triangulated) space",
  "without fine-tuning"), Dantas 2023 (Ann. Phys., 10.1002/andp.202400109, arXiv 2305.16009: SOC-Entropie -> BTZ-
  Umfangsgesetz nur "by an appropriate adjustment of a potential function", also mit Anpassung).
  **Kritik-Baustein gefunden (Primaer-Abstract):** Vespignani/Zapperi 1998 (PRE 57:6345, cond-mat/9709192): Kontroll-
  parameter = Antriebsraten; SOC-Skalen nur "In the limit of vanishing control parameters"; dieser Grenzfall entspricht
  dem Zusammenbruch der Raum-Zeit-Lokalitaet der Regeln; Dissipation fuehrt einen eigenen Exponenten ein (Endlichkeit).
  Randliteratur im Treffer (Castro/Granik/El Naschie 2000) nicht gewertet.
- **F3 Erwartung (10:05:48, date):**
  INSPIRE, alle Arbeiten, die Ansari/Smolin zitieren, juengste zuerst. Erwartet: 20 bis 50 Zitate; juengste aus
  2024-2026 sind Netz-/Emergenz-Arbeiten (Dantas, Bianconi, Graphity-Nachfolger), keine ausdrueckliche Widerlegung,
  keine Gitter-QG-Arbeit (DT/CDT/Regge), die eine Selbstabstimmung zeigt.
- **F3 Ausgang (Abruf 4):** Abruf gescheitert (INSPIRE-Filter refersto mit alter arXiv-Kennung griff nicht). Nicht
  wiederholt, um Budget zu sparen; 24-Monats-Pflicht fuer SOC+QG ist ueber F2 (arXiv) gedeckt und wird mit einer
  Websuche ergaenzt (offen, siehe F-Liste). Erwartung weder bestaetigt noch verletzt.
- **F4 Erwartung (10:06:16, date):**
  arXiv-API Titelsuche: Lin/Lerner/Rosso/Wyart 2014, Mueller/Wyart 2015, Dickman u. a. 2000 (Paths to SOC),
  Bonachela/Munoz 2009, Watkins u. a. 2016 (25 years SOC), O'Hern u. a. 2003 (Jamming), Sornette u. a. 1995 (Mapping
  SOC onto criticality), Moretti/Munoz 2013 (Griffiths-Phasen). Erwartet: Lin u. a.: Fliessuebergang als dynamischer
  Uebergang, Lawinen tau ~ 1,2-1,4, Pseudoluecke theta > 0 (etwa 0,4-0,6), Lawinen-Abschneiden waechst mit N.
  Mueller/Wyart: Marginalstabilitaet generisch bei Lawinen und langreichweitiger Wechselwirkung. Dickman: SOC =
  Absorptionsuebergang, versteckt abgestimmt ueber Antrieb/Ableitung -> 0. Bonachela/Munoz: ohne Erhaltung keine echte
  SOC. O'Hern: Punkt J isostatisch bei phi_c, Ueberschuss-Kontakte ~ (phi - phi_c)^0,5, also abgestimmt (p -> 0).
  Moretti/Munoz: ausgedehnter kritischer Bereich ohne Abstimmung in heterogenen Netzen.
- **F4 Ausgang (Abruf 5; ~~Auswertung ab 10:07~~ [geschaetzt; berichtigt: nach 10:06:22, vor 10:07:00, date]):** bestaetigt fuer die Kritik-Literatur, je eine Zeile:
  - Sornette/Johansen/Dornic 1995 (J. Phys. I France 5:325, adap-org/9411002): SOC = Abstimmung des Ordnungsparameters
    auf verschwindend klein, aber positiv; Kontrollparameter dann genau kritisch; erklaert das langsame Antreiben.
  - Dickman/Munoz/Vespignani/Zapperi 2000 (Braz. J. Phys. 30:27): SOC = langsames Antreiben eines Absorptions-
    uebergangs mit erhaltener Dichte; Wege: Extremaldynamik oder Antrieb -> 0.
  - Bonachela/Munoz 2009 (J. Stat. Mech. P09009): ohne Erhaltung keine echte Kritikalitaet; die Nachladerate muss
    abgestimmt werden, bei endlichem N praezise ("SOqC"). Bonachela u. a. 2010 (P02015) dasselbe fuer Neuronennetze.
  - Watkins u. a. 2016 (Space Sci. Rev. 198:3), Aschwanden u. a. 2016, McAteer u. a. 2016: Uebersichten; Streit, was
    SOC, SOC-aehnlich und nicht SOC ist (Phasenuebergaenge, Perkolation, Verzweigung u. a.).
  - Moretti/Munoz 2013 (Nat. Commun. 4:2521): Griffiths-Phase = ausgedehnter kritikaehnlicher Bereich aus
    Strukturunordnung, statt eines singulaeren Punkts.
  - Mueller/Wyart 2015 (Annu. Rev. CMP 6, DOI 10.1146/annurev-conmatphys-031214-014614): Pseudoluecke der lokalen
    Felder und "crackling" sind eng verbunden **in Systemen mit langreichweitiger Wechselwirkung**.
  - Lin/Lerner/Rosso/Wyart 2014 (PNAS 111:14382): drei unabhaengige Exponenten theta, d_f, z; Aehnlichkeit mit Depinning
    und Unterschiede; 2D und 3D. **Keine Zahlen im Abstract** -> Volltext noetig (Erwartung offen).
  - **Verstoss klein:** O'Hern u. a. 2003 (PRE 68:011306): Punkt J liegt bei T = 0 **und verschwindender angelegter
    Spannung** (also ein Punkt, an den man heranfaehrt); er ist "reminiscent of an ordinary critical point", aber die
    Exponenten haengen nicht von der Dimension, dafuer vom Paarpotential ab. "Isostatisch" steht nicht im Abstract.
    Dazu Kommentar Donev/Torquato/Stillinger/Connelly 2004 (PRE 70:043301) mit Antwort (PRE 70:043302): Streit um
    die Definitionen (Zufallsdichtpackung). Die Karten-Praemisse "stellen sich von selbst auf den isostatischen Punkt
    ein" ist damit nur protokollbedingt richtig (man komprimiert bis zur Schwelle) [ES].
- **F5 Erwartung (10:07:00, date):**
  arXiv: Schaum-Umordnungen (Durian 1995 Blasenmodell, Tewari u. a. 1999, Gopal/Durian 1995, Dennin/Knobler 1997,
  dazu Abstract-Suche foam + T1 + avalanche). Erwartet: zwei Lager. Simulationen (Durian, Okuzono/Kawasaki, Kabla)
  finden bei kleiner Scherrate potenzartige Energieabfaelle mit Abschneiden; Experimente (Gopal/Durian, Dennin/Knobler)
  finden lokale, wenig korrelierte T1-Ereignisse ohne systemweite Lawinen. Moderator: Fluessigkeitsanteil (nass, nahe
  Jamming, gegen trocken), Scherrate, Systemgroesse.
- **F5 Ausgang (Abruf 6; ~~Auswertung ab 10:08~~ [geschaetzt; berichtigt: nach 10:07:05, vor 10:08:17, date]): Erwartungsverstoss (gross, voller Zyklus).**
  - Tewari/Schiemann/Durian/Knobler/Langer/Liu 1999 (PRE 60:4385, cond-mat/9904101), 2D-Blasenmodell, abhaengig von
    Systemgroesse, Scherrate, Dissipation und Gasanteil:
    - **trocken:** "a well-defined quasistatic limit at low shear rates where localized rearrangements occur at a
      constant rate per unit strain", unabhaengig von Systemgroesse und Dissipation; passt zu Experimenten in 2D und 3D.
    - **nass (zunehmend):** Verteilung der Ereignisgroessen wird zum Potenzgesetz, nur durch die Systemgroesse
      abgeschnitten, "consistent with criticality at the melting transition".
  - Erwartet hatte ich zwei Lager "Simulation gegen Experiment". Tatsaechlich trennt **ein Moderator im selben Modell**:
    der Gasanteil (trocken gegen nass). Das Potenzgesetz gehoert zur **Kritikalitaet am Schmelz-(Jamming-)Punkt**, also zu
    einem abgestimmten Punkt, nicht zu SOC. Trocken: lokale Ereignisse mit fester Rate je Dehnung, keine Lawinen.
  - **Korrigierte Erwartung:** T1-Lawinen gibt es nur nahe dem Verlust der Steifigkeit; ein steifes ("trockenes") Netz
    zeigt Einzelereignisse proportional zur Dehnung.
  - **Bruecke zu Finns Netz [P, ES]:** UMKLAPP-1 fand genau das trockene Bild: phi_T ~ 7,5 a (fester Anteil je Dehnung,
    Steigung 0,95), 96 % Einzelzuege. Finns Netz liegt nach dieser Analogie im trockenen Regime.
  - Folkerts/Stanwyck/Shpyrko 2012 (arXiv 1202.5594): alternder Schaum, zwei Komponenten (lawinenartige Ereignisse und
    stetiges Fliessen); bestaetigt nur "dokumentiert", keine Exponenten.
- **F6 Erwartung (10:08:17, date):**
  Volltext Lin/Lerner/Rosso/Wyart 2014 (arXiv-PDF 1403.6735v5). Erwartet: Lawinengroessen P(S) ~ S^-tau mit tau etwa
  1,2 bis 1,4; Pseudoluecke theta etwa 0,5-0,6 (2D) und 0,3-0,4 (3D); fraktale Dimension d_f etwa 0,9-1,1 (2D) und
  1,3-1,5 (3D); Abschneiden S_c ~ L^d_f; Skalenrelation tau = 2 - theta/(theta + 1) * d/d_f (o. ae.).
- **F6 Ausgang (Abruf 7; ~~Auswertung ab 10:09~~ [geschaetzt; berichtigt: nach 10:08:21, vor 10:08:49, date]):** bestaetigt (eine Zeile, Zahlen an der Stelle): Tab. 1 S. 3 (gemessen
  2D/3D im Elasto-Plastik-Modell): theta 0,57 / 0,35; d_f 1,10 / 1,50; tau 1,36 / 1,45; z 0,57 / 0,65; beta 1,52 / 1,38;
  nu 1,16 / 0,72; Relation tau = 2 - theta/(theta+1) * d/d_f (Gl. 7); S_c ~ L^d_f (Gl. 4). S. 4: tau = 1,36 +- 0,03
  (2D), 1,45 +- 0,05 (3D) bei fester Spannung; S. 5: theta = 0,57 +- 0,01 bzw. 0,35 +- 0,01. Tab. 2: Experimente tau
  1,37-1,49 (3D). **Wichtigster Satz (S. 2):** Bei monotonem Kern (Depinning, kurzreichweitig) gilt P(x) ~ x^0; bei
  langreichweitigem Kern wechselnden Vorzeichens (|G| ~ 1/r^d) muss P(x) bei null verschwinden, sonst "a small
  perturbation ... would cause extensive rearrangements". Nur 3D-Werte ueber tau leicht ueber meiner Spanne.
  **[ES] Bruecke:** UMKLAPP-1 misst fuer Finns ungetriebenes Netz theta ~ 0. Mit langreichweitiger Kopplung der Zuege
  waere dieser Zustand instabil (Lawinen, bis sich eine Pseudoluecke bildet); ohne Kopplung (Schlaefli, B2) bleibt er
  ruhig. theta nach langem Antreiben trennt die beiden Faelle.
- **F7 Erwartung (10:08:49, date):**
  arXiv-Suche: Voronoi- bzw. Vertex-Modelle (Gewebe, 2D/3D) mit Lawinen und T1 bzw. Umordnungen. Grund: Im Voronoi-
  Modell waehlt die Delaunay-Zerlegung der bewegten Punkte die Topologie, genau wie in Finns Netz (B1), aber mit Energie
  (Flaeche/Umfang bzw. Volumen/Oberflaeche) als Rueckkopplung. Erwartet: einige Arbeiten (2018-2025) finden unter
  langsamer Scherung lawinenartige Umordnungen mit Potenzgesetz nahe dem Steifigkeitsuebergang (Formindex p0 ~ 3,81 in
  2D, s0 ~ 5,4 in 3D, Merkel/Manning 2018), also wieder abgestimmt; fern davon lokale T1. Kein SOC-Anspruch ohne Abstimmung.
- **F7 Ausgang (Abruf 8; ~~Auswertung ab 10:10~~ [geschaetzt; berichtigt: nach 10:08:55, vor 10:09:37, date]): Erwartungsverstoss (mittel).**
  - Popovic/Druelle/Dye/Juelicher/Wyart (arXiv 2002.05133, 2020): Ein Vertex-Modell fuer Zellpackungen zeigt das Bild
    plastischer amorpher Stoffe; von oben an die Fliessspannung heran divergieren Lawinengroesse und -dauer. Wenn die
    Energie von der Topologie abhaengt, ist der Stabilitaetsabstand x proportional zur Laenge L der Kante, die beim
    plastischen Ereignis verschwindet; P(x) ist dann **allein aus der Geometrie messbar**. Im Fluegelepithel der
    Fruchtfliege folgt P(L) einem Potenzgesetz mit Exponenten wie im Modell in seiner festen Phase.
  - Verstoss gegen meine Erwartung: Der kritische Punkt ist hier der **Fliessuebergang** (den quasistatisches Dehnen von
    selbst ansteuert), nicht der Steifigkeitsuebergang (Formindex); und die Pseudoluecke ist **an echtem Gewebe aus der
    Geometrie** gemessen. Merkel/Manning (3D-Voronoi) kam in diesem Abruf nicht vor; nicht behauptet.
  - **[ES] Bruecke:** In 3D ist der Randabstand einer Delaunay-Flaeche (Kugeltest) das Gegenstueck zur Laenge der
    dualen Voronoi-Kante, die beim 2-3-Zug auf null schrumpft (die beiden Umkugelmittelpunkte fallen zusammen). Damit
    ist UMKLAPP-1s P(Randabstand) ~ x^0 (Dichte endlich) die direkte Entsprechung zu P(L). Einschraenkung: Popovic u. a.
    brauchen eine topologieabhaengige Energie; Finns flacher 2-3-Zug kostet keine Energie (UK0), dort ist x rein
    geometrisch, nicht mechanisch.
  - Beifang: Sadhu 2010 (1009.5995): SOC-Modell eines umordnenden Wasserstoffbruecken-Netzes in Eis (Vier-Vertex-Modell,
    nicht erhaltend), drei Lawinenarten mit einfacher Endlichkeits-Skalierung; nur Abstract, Bezug zur Eisregel [H].
- **F8 Erwartung (10:09:37, date):**
  arXiv Titel: Holometer 2016 (Kreuzspektren) und 2017 (Scherrauschen), Perlman u. a. 2015 (Bildverschmierung),
  Amelino-Camelia 1999 (Interferometer als QG-Detektoren), GQuEST 2024. Erwartet: Holometer schliesst Hogans
  holographisches Rauschen (Planck-Amplitude, bestimmte raeumliche Korrelation) mit hoher Signifikanz aus; Perlman u. a.
  schliessen Zufallsweg- (alpha = 1/2) und holographische (alpha = 2/3) Abstandsschwankungen per Bildverschmierung aus
  (umstritten); Amelino-Camelia: Zufallsweg-Modell mit l_P waere in Interferometern messbar; GQuEST zielt auf
  Verlinde/Zurek-Schwankungen. Alle Schranken gelten fuer bestimmte Modelle, nicht fuer "SOC-Raum" allgemein.
- **F8 Ausgang (Abruf 9; ~~Auswertung ab 10:11~~ [geschaetzt; berichtigt: nach 10:09:44, vor 10:10:16, date]):** teils bestaetigt, ein Verstoss.
  - Perlman u. a. 2015 (ApJ 805:10, arXiv 1411.7262): bestaetigt. delta_l ~ l^(1-alpha) l_P^alpha; Chandra alpha >~ 0,58
    (schliesst Zufallsweg alpha = 1/2 aus), Fermi alpha >~ 0,67, TeV alpha >~ 0,72; "seem to rule out alpha = 2/3".
  - **Verstoss klein:** Holometer 2016 (PRL 117:111102, arXiv 1512.01216) nennt im Abstract eine Empfindlichkeit
    (2,1e-20 m/sqrt(Hz); PSD unter t_p = 5,39e-44/Hz fuer Bandbreiten > 11 kHz), keinen ausdruecklichen Ausschluss eines
    Modells. Holometer 2017 (CQG 34:165005, arXiv 1703.08503): Schranken fuer "a set of models of spatial shear noise
    correlations"; der Aufbau ist **nur fuer Korrelationen mit Scher-Symmetrie** empfindlich. Ein Raumrauschen ohne
    Scher-Symmetrie (z. B. isotropes Atmen) faellt nicht unter diese Schranke [ES].
  - GQuEST (Vermeulen u. a., PRX 15:011034, 14.02.2025; im 24-Monats-Fenster): Entwurf, noch keine Schranke; Ziel sind
    "geontropische" Schwankungen (Verlinde/Zurek-Umfeld).
  - Amelino-Camelia 1999 unter diesem Titel nicht auf arXiv gefunden; nicht zitiert.
- **F9 Erwartung (10:10:16, date):**
  arXiv nach Datum: (spacetime/space-time fluctuations | holographic noise | quantum gravity noise) UND (interferometer |
  LIGO | gravitational wave detector). Erwartet: 2024-2026 einige Arbeiten (Verlinde/Zurek-"Pixellon"-Schranken aus
  LIGO/Virgo-Daten, GQuEST-Folgearbeiten, Rauschmodelle fuer Einstein-Teleskop/Cosmic Explorer); keine Arbeit zu
  SOC- bzw. Lawinen-Raumzeitrauschen; keine Schranke, die einen allgemeinen "SOC-Raum" ohne Modellabbildung ausschliesst.
- **F9 Ausgang (Abruf 10; ~~Auswertung ab 10:12~~ [geschaetzt; berichtigt: nach 10:10:22, vor 10:10:45, date]):** im Kern bestaetigt, ein kleiner Verstoss.
  - Sharmila/Vermeulen/Datta (Nat. Commun. 17:701, 2026; arXiv 2505.22892): Fuer die Suche nach Raumzeit-Schwankungen
    "a correspondence between the expected output signals and different gravity models is needed"; drei Klassen nach
    Abfall und Symmetrie der Zweipunkt-Korrelation; LIGO besser fuer "Gibt es sie?", Tischgeraete (QUEST, GQuEST) fuer
    die Signaturen. **Stuetzt den zweiten Halbsatz von SO4 direkt (Abbildung noetig).**
  - Sharmila 2026 (2608.00907): Fisher-Information fuer Staerke und Korrelationslaenge; Lee/Zurek 2025 (PRD 111:124037):
    eichinvariante Eigenzeit-Observable fuer beliebige Stoerungen. Kein SOC- oder Lawinen-Rauschmodell.
  - Verstoss klein: Neue Daten-Schranken (z. B. aus LIGO-Daten fuer Verlinde/Zurek) tauchten in dieser Suche nicht auf;
    nicht behauptet, dass es keine gibt.
- **F10 Erwartung (10:10:45, date):**
  arXiv nach Datum: (dynamical triangulation(s) | causal dynamical triangulations | Regge calculus) UND (fine-tuning |
  self-tuning | self-organized | without tuning). Erwartet: einige Arbeiten, die die Abstimmung der nackten kosmologischen
  Konstante bzw. eines Massterms nennen (Standard); keine, die einen Mechanismus zeigt, der ohne Abstimmung zum
  kritischen Punkt fuehrt. Moeglich: Hinweise, dass feste Gesamtzahl der Simplexe (kanonisch) Lambda ersetzt.
- **F10 Ausgang (Abruf 11; ~~Auswertung ab 10:13~~ [geschaetzt; berichtigt: nach 10:10:51, vor 10:12:02, date]):** im Kern bestaetigt (kein Selbstabstimm-Mechanismus), ein Verstoss.
  - Benedetti (Handbook of Quantum Gravity, Springer 2024; arXiv 2212.11043): Um Horava-Lifshitz oder ART zu erreichen,
    "one would likely need to fine tune some of the parameters in the CDT action, or additional ones". Bestaetigt SO2.
  - **Verstoss mittel:** Laiho/Bassler/Coumbe/Du/Neelakanta (PRD 96:064015, 2017; arXiv 1604.02745), EDT: "a
    fine-tuning is necessary"; sie deuten sie als Wiederherstellung einer vom Gitter gebrochenen **Zielsymmetrie**
    (allgemeine Koordinateninvarianz). Nach Abstimmung eines Massterms: Kontinuumsgrenzfall, 4D-Geometrie, und die
    kosmologische Konstante in Planck-Einheiten ist O(1) im UV und "undergoes renormalization group running to small
    values in the infrared" ("naturally small", unter Vorbehalt "If these findings hold up"). Es gibt also im Gitter
    einen **Anspruch auf kleines Lambda ohne Lambda-Abstimmung**, erkauft mit einer anderen Abstimmung.
  - Ambjorn/Loll/Watabiki/Westra/Zohren 2008 (PLB 665:252): 2D-CDT mit Topologieaenderung braucht keinen Doppel-
    Skalierungs-Limes mit Abstimmung der Kopplungen; betrifft die Topologie-Kopplung in 2D, nicht den kritischen Punkt
    von Lambda. Ambjorn/Goerlich/Jurkiewicz/Loll 2008 (PRD 78:063544): de-Sitter-Universum "without ... excessive
    fine-tuning" (also nicht ohne).
  - **[ES] Bruecke:** "Feinabstimmung = Wiederherstellung einer vom Gitter gebrochenen Symmetrie" passt genau auf Finns
    Isotropie-Problem (Gitter bricht die Drehsymmetrie; TT-ISO-1 stimmt J ab). Dort ist Symmetrie (ikosaedrisch) oder
    Mittelung der natuerliche Ersatz, nicht SOC.
- **F11 Erwartung (10:12:02, date):**
  Websuche (breiter als arXiv, Zeitschriften 2025-2026): "self-organized criticality" emergent spacetime quantum gravity.
  Erwartet: nichts Neues ausser Dantas (2021/2023) und allgemeinen Netz-Arbeiten; evtl. populaere Texte. Keine Arbeit mit
  Kontinuumsgrenzfall und Schwerewellen.
- **F11 Ausgang (Abruf 12, ~~ab 10:15~~ [geschaetzt; berichtigt: nach 10:12:02, vor 10:12:21, date]):** bestaetigt, eine Zeile: Websuche liefert nur Ansari/Smolin und Dantas 2021,
  nichts aus 2025-2026. Fuer SO1 gilt im 24-Monats-Fenster: nach Recherchestand keine neue SOC-QG-Arbeit.
- **F12 Erwartung (10:12:21, date):**
  Neuheitsprobe fuer SOC-UMKLAPP-1, arXiv: (Delaunay | bistellar | Pachner | "edge flip" | "flip graph") UND (avalanche(s)
  | self-organized criticality). Erwartet: wenige Treffer, meist Granulat-Arbeiten, die Delaunay nur zur Auswertung nutzen,
  oder Mathematik zu Flip-Graphen (Mischzeiten); keine Lawinenstatistik von Delaunay-Zuegen unter langsamem Antreiben in
  einem Gravitations- oder Netz-Raum-Modell.
- **F12 Ausgang (Abruf 13, ~~ab 10:16~~ [geschaetzt; berichtigt: nach 10:12:28, vor 10:13:04, date]):** bestaetigt, sogar staerker (null fachnahe Treffer statt "wenige"). Eine
  Lawinenstatistik von Delaunay-/Pachner-Zuegen unter langsamem Antreiben ist auf arXiv unter diesen Woertern nicht
  belegt. Die Sache selbst steht aber unter anderem Namen in der Schaum- und Vertex-Literatur (T1 = dualer Flip; F5, F7).
  "Neu" also nur im engen Sinn (Finns Netz, Regge-Energie, Takt).

## F. Zeitberichtigung (Selbstanzeige)

- Die "Auswertung ab ..."-Zeiten bei F1 bis F12 und die Abrufzeiten 12 und 13 waren geschaetzt bzw. falsch
  abgeschrieben (meine Zeitschaetzung lief rund 3 min vor). Gestrichen und daneben mit date-Grenzen berichtigt,
  Sicherung *.bak-vor-zeitberichtigung. Ab jetzt nur noch date-Werte.
- Zeitberichtigung eingetragen 10:13:26 (date).

## G. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. **"SOC erzeugt 1/f-Rauschen"** (Karte, Frage 4; BTW-Titel). Gegen-Erinnerung [L]: Fuer den BTW-Sandhaufen wurde
   frueh ein 1/f^2-Spektrum gefunden. -> wird mit Abruf 14 geprueft.
2. **"Delaunay-Zuege unter langsamem Antreiben sind Einzelereignisse"** (B1): eigene Schreibtisch-Herleitung [M];
   gestuetzt durch UMKLAPP-1 (96 % Einzelzuege), nicht an Literatur (kinetische Delaunay-Zerlegung) geprueft.
3. **"Der Randabstand entspricht der Laenge der schrumpfenden Voronoi-Kante"** (F7-Bruecke) und **"T1 in 3D = dualer
   2-3-Zug"**: Schreibtisch [M, L], nicht an Quelle geprueft.
4. **"Finns Netz ist 'trocken' (fern vom Steifigkeitsverlust)"**: Analogie [H]; im flachen Regge-Netz sind Eckverschiebungen
   Eichmoden (Energie null), das passt nicht 1:1 zum Schaum.
5. **"Kleine Kopplung durch Schlaefli"** (B2): Energie-Stetigkeit ist im Projekt gemessen (UK0, TD), die Kraefte nach
   dem Zug nicht.
6. **"Die Karten-Praemisse: Packungen stellen sich von selbst auf den isostatischen Punkt ein"**: teils geprueft (F4:
   Punkt J bei verschwindender Spannung, also protokollbedingt).
- **F13 (Abruf 14) Erwartung (10:13:43, date), Gegensweep Punkt 1:**
  arXiv: Laurson/Alava/Zapperi 2005 "Power spectra of self-organized critical sandpiles" und Abstracts mit 1/f + sandpile.
  Erwartet: Der Spektralexponent haengt von den Lawinenexponenten ab und ist im Allgemeinen nicht 1 (BTW eher ~2 fuer das
  Aktivitaetssignal); 1/f ist keine allgemeine SOC-Folge. Falls bestaetigt: "1/f-Rauschen" taugt nicht als Signatur
  eines SOC-Raums ohne Modell.
- **F13 Ausgang (Abruf 14; Auswertung ab 10:14:20, date): Erwartungsverstoss (mittel), Gegensweep-Befund.**
  - Laurson/Alava/Zapperi 2005 (J. Stat. Mech. L11001, cond-mat/0509401): BTW und Manna: Spektren 1/f^alpha, alpha
    "significantly smaller than 2" und gleich dem Exponenten zwischen Lawinengroesse und -dauer. **Meine Erinnerung
    "BTW ~ 1/f^2" ist damit fuer dieses Signal nicht gestuetzt** (gestrichen); 1/f ist es auch nicht.
  - Yadav/Ramaswamy/Dhar 2012 (PRE 85:061114, 1203.5912), exakt geloester gerichteter Sandhaufen: Massen-Schwankungen
    1/f in einem Frequenzband, **Aktivitaets-Schwankungen im selben Band linear in f**. Das Spektrum haengt also an der
    Observablen.
  - Davidsen/Paczuski 2002 (PRE 66:050101): 1/f^alpha kann aus Korrelationen **zwischen** Lawinen entstehen (Modell).
  - Im 24-Monats-Fenster: Chhimpa/Yadav 2025 (arXiv 2507.21484): BTW/Manna-Aktivitaet hat drei Bereiche (flach, Buckel,
    1/f^alpha bei hohen Frequenzen), alle mit Systemgroessen-Skalen. Kumar/Chhimpa/Yadav 2026 (2605.25884): OFC lokal
    nahezu 1/f im Mittelbereich, 1/f^2 bei hohen Frequenzen; Dissipation aendert den dynamischen Exponenten.
  - **Korrigierte Erwartung:** "1/f" ist keine allgemeine SOC-Signatur; Exponent und Form haengen an Observable
    (Masse/Volumen gegen Aktivitaet/Zugrate), Frequenzbereich und Erhaltung. Fuer einen SOC-Raum muss die Abbildung
    "welche Netzgroesse koppelt ans Interferometer" vor jeder Schranke stehen (stuetzt SO4, zweiter Halbsatz).
- **F14 (Abruf 15, letzter) Erwartung (10:14:20, date):**
  arXiv: Hamber, Regge-Gitter-Gravitation (au:Hamber AND ti:lattice). Erwartet: Kontinuumsgrenzfall nur an einem
  nichttrivialen Fixpunkt G_c, nu ~ 1/3, d. h. G muss auf G_c abgestimmt werden; kein Selbstabstimm-Mechanismus.
- **F14 Ausgang (Abruf 15; Auswertung ab 10:17:13, date):** bestaetigt, eine Zeile: Hamber 2009 (GRG 41:817): Gitter-Kontinuum ueber einen nichttrivialen UV-Fixpunkt (kritisches Verhalten, Universalitaet); Hamber 2015 (PRD 92:064017): Vergleich mit vermutetem nu = 1/3; skalierte kosmologische Konstante als IR-Abschneider. Das Wort 'Abstimmung' steht nicht im Abstract; dass die nackte Kopplung an G_c heranmuss, ist [L, ES].

## H. Gegensweep-Ergebnis (Regel 4)

- Geprueft: Punkt 1 ("SOC = 1/f") mit Abruf 14 -> **Verstoss**: 1/f ist keine allgemeine SOC-Folge; Exponent haengt an
  Observable und Bereich; meine Erinnerung "BTW 1/f^2" ist fuer das Lawinensignal nicht gestuetzt (Laurson u. a. 2005).
- Teilgeprueft: Punkt 6 (Jamming "von selbst") mit Abruf 5 -> nur protokollbedingt (Spannung -> 0).
- Ungeprueft (als Selbstanzeige ins Dossier): Punkte 2 bis 5.

## I. Dossier

- Dossier ab 10:17:13 (date).
- Dossier fertig 10:22:34 (date). Abrufe 15 von 15. Kein Journal, kein Peerbus, kein Commit.
