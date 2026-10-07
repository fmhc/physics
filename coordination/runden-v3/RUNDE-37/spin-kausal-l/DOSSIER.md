# SPIN-KAUSAL-L: Dossier (Feldforscher fuer die Leitung, Runde 38)

- **Zeiten (date):** Start 2026-10-04 08:57:56 CEST, Text ab 09:24:59 CEST, Zeitbox 60 min.
- **Arbeitsdatei:** ARBEITSFELD.md, mit Abrufprotokoll, Notizen und Schreibtisch S1.
- **Kennzeichen:**
  - [S] selbst an der Quelle gelesen (lokaler Text oder PDF per pdftotext)
  - [S Abstract] Abstract woertlich ueber die arXiv-API; den Volltext habe ich dann nicht gelesen
  - [L] aus dem Gedaechtnis, [L?] unsicher
  - [ES] eigener Schluss; Algebra nicht gegengelesen
  - [H] Hypothese
- **Art des Ergebnisses:** reine Literatur und Schreibtisch. Keine Rechnung, keine Messdaten.

## 1. Ergebnis zuerst

1. **Fuer Spin 1/2 auf Kausalmengen in 3+1 gibt es keine Bauweise, die nur die Ordnung benutzt. Das ist offen [S].**
   - Die vorhandenen Vorschlaege setzen Zusatzstruktur ein:
     - Sverdlov 2008: Vierbeine aus Holonomien
     - Noldus 2013: Clifford-Struktur, "the dimension is put in by hand"
     - Gudder 2015: eigene gitterartige Kausalmenge
   - Johnston 2010 gibt nur Skizzen ("task for future work"). Nomaan X 2023 fuehrt Fermionen als kuenftige Richtung.
   - In den letzten 24 Monaten fand ich keine neue Bauweise (fuenf arXiv-Abfragen). Das ist "nach Recherchestand nicht
     belegt", nicht "unmoeglich".
2. **Das Hindernis liegt vor dem Spin, beim Tangentialraum [S, ES].**
   - Surya 2019: Es ist "no well defined representation of non-trivial tensorial fields on causal sets" bekannt.
     Grund: Die Valenz ist unendlich, also gibt es keinen lokalen Tangentialraum.
   - Bombelli u. a. 2009 (Satz 2 bei Surya; die Koautoren Henson und Sorkin weiss ich nur aus dem Gedaechtnis [L])
     verbietet, aus der Streuung aequivariant eine Richtung oder einen Rahmen je Element zu waehlen.
   - Euklidisch geht das (kompakte Gruppe), lorentzsch nicht. Das ist der Moderator.
3. **Schreibtisch S1 [ES]:**
   - Jede retardierte "Wurzel des Propagators" (Johnstons Weg 6.4) braucht an jedem Element ein nilpotentes
     Kontaktglied ungleich 0. Grund: Auf Links liegt kein Zwischenelement.
   - Daraus folgt Spinraum s >= 2. Ein skalarer Ansatz (s = 1) ist ausgeschlossen.
   - Aber s = 2 ist trivial loesbar, ohne Spin (Reduktion auf erste Ordnung). Die Wurzelbedingung erzwingt also eine
     Verdopplung, keinen Spin. Das passt zu Noldus.
   - Ein spinorielles Kontaktglied waere eine Null-Flagge je Element. Die ist nach dem BHS-Muster nicht aequivariant
     waehlbar.
4. **Uebertrag der QCA-Befunde [ES]:**
   - "Spin erzwungen durch Isotropie" braucht eine Gruppe, die auf einer endlichen Nachbarmenge wirkt. Ein Netz ohne
     Symmetrie hat keine.
   - Uebertragbar ist nur "Spin eingeloetet plus Isotropie im Mittel". Das geht im kompakten Fall (raeumliches
     Zufallsnetz), auf der Kausalmenge nur halb-intrinsisch ueber die Einbettung oder mit eingesetzten Rahmen.
5. **Unerwarteter Literaturtreffer [S, ES]:**
   - Foster/Jacobson 2016 bauen ein 3+1-Schachbrett mit Spin auf **tetraedrischen Nullschritten**, mit
     Schrittgeschwindigkeit 3c, ohne Verdopplung und nicht unitaer. Fuer die Dirac-Masse benutzen sie BCC.
   - Unsere unitaere 4-Zustands-Regel aus QCA-DIAMANT-4 Teil B (v = 1/3) ist nach meiner Algebra deren unitaere
     Erweiterung.
6. **Rechenkarte (Abschn. 8):** SPIN-ZUFALLSNETZ-1, ein eingeloeteter Weyl-Operator auf einem 3D-Poisson-Voronoi-Netz.
   - Vorab ableitbar: hermitesch, zwei exakte Nullmoden, Spur des lokalen Geschwindigkeitstensors genau 3, also v = 1
     im Mittel.
   - Offen und damit scheiterfaehig: Wird der Weyl-Ast mit Helizitaet von der Unordnung zerstoert? Kommen Doppler
     zurueck?

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | Erwartet | Gefunden | Fundstelle |
|---|---|---|---|
| V3 (S1) | Johnstons Wurzelweg ist eine 2D-Skizze; ob er die Spingroesse festlegt, ist offen | Johnston hofft ausdruecklich, die Wurzel erzwinge die Spingroesse. Noldus: "the dimension is put in by hand". S1: Die Wurzel erzwingt s >= 2 (nilpotentes Kontaktglied je Element), s = 2 geht aber trivial ohne Spin | Johnston 2010, Abschn. 6.4 [S]; Noldus 2013, S. 2 [S]; S1 [ES] |
| V6 | Projektstand (SCHACHBRETT-KAUSAL-1): 3+1-Schachbrett "nicht einfach", nur Zitate von 1984. Meine Vorhersage A10: FJ 2016 auf festem Gitter, ohne besonderen Bezug zu unseren Netzen | Foster/Jacobson 2016: Weyl-Schachbrett auf **tetraedrischen** Nullschritten (unser S_+), Verdopplung umgangen ("lack of a local action"), nicht unitaer, **BCC fuer die Dirac-Masse** (wie QCA-DIAMANT-4 Teil B), Verweis auf die unitaere BCC-Regel (D'Ariano/Perinotti, Grundlage von QCA-TETRA-1) | arXiv:1610.01142, Abstract, pdftotext-Zeile 107, Abschn. "Fermion doubling?", Schluss [S] |
| V1 | Surya 2019 nennt Fermionen als offen | Surya erwaehnt Fermionen, Spinoren und Dirac **gar nicht**. Sie sagt Staerkeres: Schon nichttriviale Tensorfelder sind nicht wohldefiniert, und ein lokaler Tangentialraum fehlt | Surya, lokale Textdatei Z. 7928-7931, 7314-7322 [S] |
| V2 | Neuere Vorschlaege nach 2015 (Rahmen/Clifford je Element, Quantenlaeufe) | Die Vorschlaege sind aelter (2008, 2013/15, 2015). Nach 2015 nur Uebersicht und Formalismus; keine Kausalmengen-Quantenlaeufe | A1, A6, A9, A11 [S Abstract/Titel] |
| V7 | Zufallsgitter verhindert Verdopplung nicht [L?] | Gespalten: Doppler kehren mit Eichfeld zurueck (Griffin/Kieu); je nach Gitterart (Kieu u. a.); Unterdrueckung durch spontane chirale Brechung schon frei (Cohen 4D) | A13 [S Abstract] |
| V4 | Johnston Kap. 6 nur 2D | 6.3 (Schachbrett) ist 2D. 6.4 ist dimensionsunabhaengig formuliert ("for the 4-spinor theory in d = 4, I would be a 4 × 4 matrix"), aber ohne Loesung | Johnston 2010, S. 150-151 [S] |
| V5 (Methode) | arXiv-Abfrage findet Foster/Jacobson | A8 verlangte "Feynman" im Abstract und fand die Arbeit nicht. A9 (Titel und Autor) fand sie. A7 war zu breit (244 fachfremde Treffer) | Abrufprotokoll |

## 3. Erwartungen der Karte mit Ausgang

| Nr | Erwartung | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | 3+1-Fermionen auf Kausalmengen offen; Surya 2019 nennt es als offen [L?] | **teils eingetroffen.** Offen: ja. Nomaan X 2023 nennt Fermionen als kuenftige Richtung, Johnston 6.4 "task for future work", in 24 Monaten keine Bauweise. Surya nennt Fermionen aber nicht; sie sagt allgemeiner, dass Tensorfelder fehlen | Nomaan X 2023, Abschn. "Fermions" und Schluss [S]; Johnston 2010, 6.4 [S]; Surya Z. 7928-7931 [S]; A1/A6/A9/A11 |
| E2 | Johnston Kap. 6: 2D-Ansaetze, kein 4D-Dirac-Operator | **teils eingetroffen.** Kein 4D-Operator: ja. Aber 6.4 ist allgemein-dimensional angelegt und will die Spingroesse aus der Wurzel gewinnen. 6.2 kritisiert Sverdlov | Johnston 2010, 6.2-6.4, S. 143-151 [S] |
| E3 | Neuere Vorschlaege nach 2015 auf Kausalmengen (Rahmen/Clifford je Element, Quantenlaeufe) [L?] | **nicht eingetroffen (nach Recherchestand nicht belegt).** Rahmen- und Clifford-Ideen gibt es, aber vor 2015 (Sverdlov 2008, Noldus 2013/15). Gudder 2015 arbeitet auf eigener c-causet-Struktur. Nach 2015 nur 3+1-Schachbrett auf festem Gitter (Foster/Jacobson 2016), nicht auf Kausalmengen | A1, A6, A9, A11; Sverdlov, Noldus [S]; Gudder [S Abstract] |
| E4 | Ausweg: Spinor als Zusatzfeld mit lokaler Lorentz-Eichgruppe (Rahmen je Element) [ES] | **eingetroffen als Literaturweg, mit Hindernis.** Sverdlov: "fermions can be interpreted as local frame defined by non-orthonormal vector fields", Vierbeine aus Holonomien. Johnston: "not clear in what way the Lorentz-transformation properties of a spinor are included". Nach BHS koennen die Rahmen nicht aus der Streuung kommen. Sie muessen eigene Freiheitsgrade sein, mit nicht kompakter Gruppe [ES] | Sverdlov 2008, Abstract und Abschn. 4 [S]; Johnston 6.2 [S]; Surya Satz 2 [S] |
| E5 | Statistische Lorentz-Invarianz reicht, damit sich ein eingesetzter Spinor im Mittel richtig dreht [H] | **gespalten (drei Regime, Abschn. 5).** (i) Mit kovarianten Einbettungsgroessen (sigma.Delta): im Mittel trivial richtig, vorab ableitbar [ES]. (ii) Mit Rahmen, die aus der Streuung gewaehlt werden: unmoeglich (BHS) [S]. (iii) Euklidisch bzw. raeumlich kompakt: moeglich [S] | Surya Z. 1525-1600 [S]; Catterall u. a. 2018 [S Abstract]; S1 [ES] |

## 4. Literaturstand (kurz)

- **Kausalmengen, Fermionen:**
  - Johnston 2010, Doktorarbeit, Kap. 6 [S]. Zwei Ideen: Schachbrett ueber Kettenintervalle (2D) und Wurzel des
    retardierten Propagators R_m^2 = -rho K_R ⊗ I (allgemein-dimensional).
    - 6.4: "Ideally, we would like the size of this spin-space to be determined by the act of taking the square root of
      KR". Schluss: "This remains a task for future work."
    - Fussnote 2: "since spinors cannot be defined for an arbitrary Lorentzian manifold, it may be over-optimistic to
      try to define them for an arbitrary causal set."
  - Sverdlov 2008 [S]: Vierbeine aus Holonomien, Spinor aus deren "leftover degrees of freedom". Nur Lagrangedichten,
    keine Numerik. Johnston 6.2 nennt das "very complicated".
  - Noldus 2013/2015 [S]:
    - Clifford-wertige "generating structure" K auf Diagonale und Links mit KK* + K*K = 2·1⊗I.
    - "not enough information is present in the causal set itself to find a unique solution [...] the dimension is put
      in by hand".
    - Beispiele nur mit 2 Elementen und am "Diamanten".
  - Gudder 2015 [S Abstract]: "covariant causal set (c-causet)"; ein Wachstumsmodell, in dem "the structure of a
    four-dimensional discrete manifold emerges", darauf ein diskreter freier Dirac-Operator. Das ist eine eigene
    gitterartige Struktur, keine Streuung [ES].
  - Nomaan X 2023 (Uebersicht) [S]:
    - Fuer Fermionen braucht man erst "the retarted Green function analogue on the causal set". Die fermionische
      Pauli-Jordan-Fassung (Antivertauscher) sei dann leicht.
    - Johnstons Wurzel: "not unique in general [...] we may need further constraints".
  - Jones/Yazdi 2026 (2602.16782) [S Abstract]: Spektralentropie "for both bosonic and fermionic field theories";
    Kausalmengen-Beispiel nur in 1+1.
- **Kausalmengen, Grundsatz:**
  - Surya 2019 [S]: Ein lokaler Tangentialraum ist "not possible, since the valency of the graph is infinite" (Z.
    7314-7317). Sie empfiehlt "scalar quantities, rather than more general tensorial ones".
  - Satz 2 (Bombelli u. a. 2009): Es gibt keine aequivariante messbare Richtungsabbildung C(M^d) -> H^(d-1). Euklidisch
    ist eine konsistente Richtung waehlbar (Z. 1525-1600).
  - Sverdlov 2018 [S Titel]: Elektromagnetismus "on edges rather than points". Vektor- und Eichfelder gibt es also nur
    als Vorschlaege.
- **Gitter und Netze mit Spin (ausserhalb der Kausalmengen):**
  - Foster/Jacobson 2016 [S]: 3+1-Weyl-Schachbrett auf tetraedrischen Nullschritten.
    - Rechtshaendiger Schritt ~ Projektor auf den Spin in Schrittrichtung, Amplitude i^(±T) 3^(-B/2) 2^(-N).
    - Keine Verdopplung, nicht unitaer. "Lorentzian lattice schemes ensuring 4D Lorentz symmetry in the continuum limit
      of an interacting theory are not known."
  - D'Ariano/Perinotti 2014 (Projekt, QCA-TETRA-1 [S]): unitaere BCC-Weyl-Regel. Isotropie unter L_2 erzwingt Spin 1/2.
  - Kaehler-Dirac auf zufaelliger Geometrie (Catterall/Laiho/Unmuth-Yockey 2018) [S Abstract]: "natural extension of
    staggered fermions to random geometries without requring vielbeins and spin connections". Euklidische DT.
  - Zufallsgitter-Fermionen [S Abstract]:
    - Griffin/Kieu 1992: "the doublers suppressed in the free field case are revived for random lattices in the
      continuum limit unless gauge interactions are implemented in a non--invariant way"
    - Kieu/Markham/Paranavitane 1994: "arbitrary randomness by itself is shown to be not a sufficient condition to
      remove the fermion doublers"
    - Cohen 2006: "the random lattice does so by spontaneous chiral symmetry breaking even in the free theory"
- **Aus dem Gedaechtnis, nicht geprueft [L?]:**
  - Jacobson 1984, Spinorketten-Pfadintegral in 3+1 (nur als Zitat bei Johnston [S])
  - Christ/Friedberg/Lee 1982, Zufallsgitter (nur als Zitat bei Surya [S])
  - Friedman/Sorkin 1980, Spin 1/2 aus Topologie
  - Meyer 1996, skalare QCA trivial
  - Finsters kausale Fermionsysteme (Spinraeume primaer). In A1 kein Treffer, nicht abgerufen.

## 5. Regime und Moderatoren (Regel 1)

| Moderator | Regime 1 | Regime 2 | Beleg |
|---|---|---|---|
| M1 Kompaktheit der Ensemble-Gruppe | euklidisch bzw. raeumlich (SO(d), S^(d-1) kompakt): Richtung bzw. Rahmen je Punkt waehlbar, Ensemble im Mittel invariant; Spinoren auf Zufallsgittern und Kaehler-Dirac auf DT moeglich | lorentzsch (H^(d-1) nicht kompakt): keine aequivariante Richtung (Satz 2), also kein Rahmen aus der Streuung | Surya Z. 1525-1600 [S]; Catterall 2018 [S Abstract] |
| M2 Raumzeitdimension | 1+1: zwei Nullrichtungen, beide unter Boosts fest; R/L ohne Rahmen; SCHACHBRETT-KAUSAL-1 geht | ab 2+1: Nullrichtungen S^1 bzw. S^2 ohne invariantes Wahrscheinlichkeitsmass unter SL(2,R) bzw. SL(2,C); Spinamplituden brauchen Richtungen im Inneren | [ES]; Johnston 6.3 [S] |
| M3 Unitaritaet bzw. lokale Wirkung | Foster/Jacobson: nicht unitaer, ohne lokale Wirkung, keine Doppler | D'Ariano/Perinotti: unitaer, lokal, Doppler an H, P, P' (QCA-TETRA-1) | FJ 2016 [S]; QCA-TETRA-1 [S, Projekt] |
| M4 Zufallsgitter: Kopplung und Gitterart | frei bzw. bestimmte Gitterart: Doppler unterdrueckt | mit Eichfeld bzw. andere Gitterart: Doppler zurueck | A13 [S Abstract] |
| M5 Groesse der Kausalmenge (Wurzelfrage) | Noldus: 2 Elemente und Diamant, viele Loesungen | grosse gestreute Mengen mit Kovarianz im Mittel: Eindeutigkeit unbekannt [H] | Noldus [S] |

- **Regel 6, Kopplung vor Bauteil [ES]:** Es gibt mindestens sechs Wege zu Spin 1/2:
  1. Gittergruppe (QCA)
  2. Projektor auf die Schrittrichtung (Foster/Jacobson)
  3. Holonomie-Vierbeine (Sverdlov)
  4. Clifford-Struktur von Hand (Noldus)
  5. Ladung plus Monopol (LADUNG-MONOPOL-1)
  6. Formen statt Spinoren (Kaehler-Dirac) bzw. Topologie (Friedman/Sorkin [L?])
  - Gemeinsam ist die **Verloetung**: eine feste Kopplung zwischen inneren Drehungen und Raum-Drehungen, sodass 360
    Grad als -1 wirken. Auf der Kausalmenge fehlt nicht der Spinor, sondern das Gegenstueck zum Loeten: eine lokale
    Drehung bzw. ein Tangentialraum (Surya Z. 7314).
  - Die gesuchte Groesse ist deshalb die Loetform. Ein weiterer Spinor-Bauteil ist es nicht.

## 6. Unterscheidungspunkte (Regel 2)

- **U1 (E5 kompakt gegen lorentzsch):**
  - Groessenabhaengigkeit der Rahmenstatistik:
    - Euklidisch ist die Verteilung der gewaehlten Richtung gleichverteilt und unabhaengig von der Gebietsgroesse.
    - Lorentzsch muss jede Waehlregel eine Rapiditaetsverteilung haben, die mit dem IR-Abschnitt waechst (Satz 2).
  - In einer Simulation zugaenglich (Gebiet vergroessern), physikalisch nicht.
- **U2 (Johnstons Hoffnung gegen Noldus):**
  - Die triviale s = 2-Loesung aus S1 erfuellt alle Bedingungen, die Johnston nennt (retardiert, Quadrat, Traeger auf
    Diagonale und Relationen). Sie transformiert aber trivial.
  - Auseinander laufen beide erst, wenn man verlangt, dass der innere Raum aequivariant eine SL(2,C)-Darstellung
    traegt. Gerade dann greift das BHS-Muster (Null-Flagge je Element).
  - Ohne Zusatzstruktur ist das empirisch nicht unterscheidbar.
- **U3 (Foster/Jacobson gegen D'Ariano):**
  - Bei Wellenzahlen an den Zonenecken H, P, P' hat die unitaere Regel ungedaempfte Kegel (W = ±I).
  - Bei FJ sind die rein imaginaeren Frequenzwurzeln gedaempft, hoechstens mit 1/sqrt(3) je Schritt [S].
  - Auf dem Gitter mit kurzwelligen Paketen messbar; physikalisch bei Planck-Impuls, also unzugaenglich.
- **U4 (1+1 gegen 2+1):**
  - 2+1 ist die kleinste Dimension, in der eine Schachbrett-Kettensumme im Inneren Richtungen braucht [ES].
  - Dort laufen "nur Ordnung" und "Ordnung plus Einbettung" auseinander. Das waere der erste Ort fuer eine
    Kausalmengen-Spinorkarte.

## 7. Projektbezug: Uebertrag der QCA-Befunde auf Netze ohne Symmetrie

1. **Was nicht uebertragbar ist [ES]:**
   - QCA-TETRA-1 und QCA-DIAMANT-4 leiten Spin 1/2 aus drei Dingen ab: einer Gruppe, die auf der endlichen
     Sprungmenge wirkt, Unitaritaet und minimaler Dimension. Die Wirkung ist dann projektiv.
   - Ein Zufallsnetz hat keine solche Gruppe, eine Kausalmenge zusaetzlich unendliche Valenz und keinen globalen Takt.
   - "Spin erzwungen" bleibt damit eine Eigenschaft von Netzen mit Symmetrie, also von Weiche (A).
2. **Was uebertragbar ist:** "Spin eingeloetet, Isotropie im Mittel".
   - **(a) Lokale Rahmen (E4):**
     - Auf raeumlichen Zufallsnetzen geht das, die Gruppe ist kompakt (Surya, euklidischer Fall [S]).
     - Auf der Kausalmenge nur mit eigenen Rahmenfeldern (Sverdlov) oder Clifford-Daten von Hand (Noldus). Aus der
       Streuung selbst sind sie nicht waehlbar (Satz 2).
   - **(b) Gemittelte Isotropie (E5):**
     - Kompakt: Auf dem Voronoi-Netz ist die erste Ordnung im Mittel exakt isotrop (Schreibtisch D3 in Abschn. 8).
       Offen ist die Wirkung der Unordnung.
     - Lorentzsch: nur mit kovarianten Einbettungsvektoren, also halb-intrinsisch wie die Enden in
       SCHACHBRETT-KAUSAL-1, jetzt aber auch im Inneren.
3. **Wurzelweg, Schreibtisch S1 (ARBEITSFELD) [ES]:**
   - Ansatz: R_0 retardiert, D_x auf der Diagonale, M_xy auf Relationen. Dann gilt (R_0^2)_xx = D_x^2 = 0.
   - Auf einem Link (x,y), wo kein Element dazwischen liegt: (R_0^2)_xy = D_x M_xy + M_xy D_y = -rho K_xy I_s, und
     das ist ungleich 0.
   - Also ist D_x nilpotent und ungleich 0, und s >= 2.
   - Fuer s = 2 genuegt R_0 = 1 ⊗ E12 - rho a L ⊗ E21. Wegen E12 E21 + E21 E12 = 1 und E12^2 = E21^2 = 0 folgt
     R_0^2 = -rho Phi ⊗ 1.
   - Das ist die Reduktion auf erste Ordnung, kein Spinor.
   - Spinoriell waere D_x = sigma.m_x mit komplexem Nullvektor m_x, also eine Flagge je Element. Fuer Nullrichtungen
     gibt es unter Lorentz kein invariantes Wahrscheinlichkeitsmass. Das BHS-Argument sollte deshalb uebertragbar sein
     [ES, nicht bewiesen].
   - [H]: Die Eckpaare in SCHACHBRETT-KAUSAL-1 sind vermutlich die 1+1-Form dieser Kontaktglieder. In 1+1 sind die
     zwei Nullrichtungen boostfest. Nicht geprueft.
4. **Foster/Jacobson und unsere Rechnungen [S, ES]:**
   - Der FJ-Schritt (1/2) Sum_a e^(ik.h_a) P(n_a) ist nach meiner Algebra die Einschraenkung von QCA-DIAMANT-4 Teil B
     (W = C·diag(e^(ik.h_a)), 4 Zustaende, Darstellung 2+2') auf den Spinorteil 2.
     - Grundlage: <a|P_2|a> = 1/2 und |<a|P_2|b>|^2 = 1/12 aus QCA-DIAMANT-4. Normiert ergibt das Spin-Kohaerenzzustaende
       mit |<xi_a|xi_b>|^2 = 1/3, also FJs Faktor 3^(-1/2) je Knick.
     - Unser v = 1/3 ist FJs "step speed 3c". FJ benutzen fuer die Dirac-Masse ebenfalls BCC mit Gegenrichtung fuer die
       andere Chiralitaet.
   - Die L4-Frage von QCA-DIAMANT-4 ("Ob die T-kovariante Muenze-mal-Verschiebung [...] in der Literatur steht") ist
     damit teilweise beantwortet: Die nicht unitaere 2-Zustands-Form steht bei FJ, die unitaere 4-Zustands-Form nach
     meinem Recherchestand nicht.
5. **Fuer Finns Weiche [ES, vorlaeufig]:**
   - (A) kann Spin aus Symmetrie erzwingen.
   - (B) kann Spin nach Literaturstand nur mit Zusatzstruktur tragen: Einbettung, Rahmenfelder oder Clifford-Daten.
     Der Grund ist strukturell, nicht numerisch: keine Tensorfelder aus der Ordnung, BHS.
   - (C) ist ungeprueft.
   - Das ist eine Lesart aus Literatur und Schreibtisch. Gemessen ist dabei nichts.

## 8. Vorschlag Rechenkarte: SPIN-ZUFALLSNETZ-1 (je Lauf <= 10 min, kann scheitern)

- **Frage:** Ueberlebt ein eingeloeteter Spin-1/2-Weyl-Teilchen auf einem Netz ohne jede Symmetrie als sauberer
  Kegel mit Helizitaet, oder zerstoert die Unordnung ihn bzw. bringt Doppler zurueck?
  - Das ist der kompakte Fall (Regime M1-1), also (A) ohne Gittergruppe bzw. ein fester Schaum.
- **Netz:**
  - N Poisson-Punkte mit Dichte 1 im periodischen Wuerfel, Delaunay-Nachbarn ueber periodische Kopien.
  - Daten: Voronoi-Flaechen A_xy, Zellvolumina V_x, Einheitsvektoren e_xy.
  - N = 1000 (Rauch), 2000 und 4000 (Haupt), je 4 Saaten.
- **Regel (Loetung):**
  - H0_xy = (i/2) A_xy sigma.e_xy und H = V^(-1/2) H0 V^(-1/2).
  - Dichte Diagonalisierung (2N <= 8000) oder Lanczos um E = 0. Einzeln etwa 1 bis 3 min auf einem Kern [ES,
    Schaetzung, nicht gemessen].
- **Kontrolle:** einfach-kubisches Gitter mit denselben Formeln (A = 1, Abstand 1).
- **Schreibtisch, vorab ableitbar [ES]:**
  - **D1 hermitesch:** (i A sigma.e_xy)^† = i A sigma.e_yx.
  - **D2 zwei exakte Nullmoden:** psi = V^(1/2) u mit konstantem Spinor u, denn Sum_f A_f n_f = 0 (geschlossene
    Zelle).
  - **D3 erste Ordnung:**
    - H0 e^(ik.r) u ≈ -e^(ik.r_x) sigma^T M_x k mit M_x = Sum_f A_f h_f n_f n_f^T, wobei h_f = d_xy/2 der
      Abstand zur Voronoi-Flaeche ist.
    - Die Pyramidenzerlegung gibt Sum_f A_f h_f = 3 V_x **exakt**, also Spur(M_x/V_x) = 3 an jedem Knoten.
    - Im Mittel folgt ein isotroper Weyl-Kegel mit v = 1. Nur der spurfreie Teil schwankt von Knoten zu Knoten
      ("zufaelliges Vierbein").
  - **D4 Kontrolle:** Kubisch gilt H = -Sum_j sigma_j sin k_j. Das gibt 8 Weyl-Knoten (4 je Chiralitaet), v = 1,
    N(eps) = 8 V eps^3/(6 pi^2).
  - **Nicht ableitbar:**
    - die Renormierung v_eff durch den spurfreien Teil
    - ob die Helizitaet ueberlebt
    - wohin die "gestaffelten" Doppler auf einem nicht bipartiten Netz gehen
    - ob rho(0) > 0 wird (Unordnungsband)
    - Die Literatur ist hier gespalten (V7, M4). Nielsen-Ninomiya auf der periodischen Superzelle verlangt nur
      Chiralitaetssumme 0 je Bandpaar, nicht bei E = 0 [L?].
- **Vorhersagen (Wahrscheinlichkeiten sind mein Vorschlag [H], die Leitung legt fest):**
  - **SZ0 Kontrolle:** kubisch n_s = 8 ± 0,5 aus N(eps) fuer eps <= 0,3, Nullmoden wie D2. 95 %, ableitbar.
  - **SZ1 Weyl-Ast mit Helizitaet:**
    - Die Spektralfunktion (Projektion der Eigenzustaende auf e^(ik.r) u) bei |k| <= 0,5 zeigt einen linearen Ast mit
      v_eff in [0,6; 1,1] und Helizitaetsbetrag |<sigma.k̂>| >= 0,8.
    - Bei N = 4000 in 4 von 4 Saaten. 45 %.
  - **SZ2 keine zweite Art bei kleinen Energien:**
    - n_s = N(eps)·6 pi^2 v_eff^3/(V eps^3) <= 1,5 fuer eps im Fenster [2 eps_min, 0,3], wobei eps_min der
      Endlichkeitsabstand ist. 35 %.
    - Scheitern hiesse: Doppler bzw. Unordnungszustaende bei E ≈ 0.
  - **SZ3 stabil gegen N:** SZ1-Groessen bei N = 2000 und 4000 innerhalb 2 SE. 60 %.
- **Kann scheitern:** SZ1 bis SZ3 haengen an der Unordnung und sind nicht ableitbar. SZ0 und D2/D3 pruefen nur den
  Code.
- **Bedeutung, vorab festzulegen:**
  - SZ1 und SZ2 treffen ein: Ein Netz ohne Symmetrie traegt einen eingeloeteten Spin-1/2-Kegel. Die QCA-Befunde
    uebertragen sich als "verloetet plus gemittelt".
  - SZ1 scheitert: Spin 1/2 braucht im Modell Netzsymmetrie oder Glaettung. Das spraeche fuer (A) mit Gittergruppe.
- **Grenzen:**
  - Globaler Takt (Hamilton-Operator), also nicht Weiche (B). Die Loetung ist eingesetzt, nicht erzwungen. Keine
    Masse.
  - **Literatur vor der Karte:** Christ/Friedberg/Lee 1982 und Griffin/Kieu 1992-93 lesen (L4), dazu
    Weyl-Halbmetalle mit Unordnung [L?].
- **Alternative fuer Spalte (B), nur Skizze [H]:** SPINOR-KETTE-2P1.
  - 2+1-Kettensumme auf einer Streuung mit Gewichten aus Einbettungsvektoren (gamma.Delta), also halb-intrinsisch.
  - Das Mittel ist kovariant und per Faltungsreihe vorab ableitbar [ES].
  - Scheiterfaehig ist die Streuung:
    - Gewichte mit gamma.Delta/tau sind nahe dem Lichtkegel unbeschraenkt.
    - Mein Schreibtisch gibt ein logarithmisch divergentes zweites Moment im Kontinuum [ES, grob]. Das Rauschen
      koennte also langsamer als rho^(-1/2) fallen.
  - Vor der Karte noetig: Gewichte so bestimmen, dass das Mittel den 2+1-Dirac-Propagator trifft (eigene Rechnung).

## 9. Gegensweep-Befunde (Regel 4)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. **"Keine Projekt-Vorarbeit" (geprueft):**
   - Fuer Kausalmengen-Fermionen stimmt es.
   - Aber RUNDE-22/geometrie-stand/ERGEBNIS.md (Z. 61, 790) nennt schon Kaehler-Dirac-Fermionen auf zufaelliger
     Geometrie (Catterall u. a. 2018), als [L?]. Mit der Spinfrage verknuepft war das nicht.
   - UEBERLEITUNGEN-EMERGENZ.md Z. 122: "Spin 1/2 auf Kausalmengen ist offen [L?]".
2. **"Arbeiten benutzen meine Stichworte" (geprueft):**
   - A9 mit "causet(s)" brachte nichts Neues.
   - A11 listet die 60 neuesten "causal set"-Abstracts. Unter den etwa 22 Kausalmengen-Physik-Titeln seit 2025-04
     keiner zu Spin, Spinor oder Fermion.
   - Ungeprueft bleiben Formulierungen wie "partial order", "discrete spacetime", "poset".
3. **"Spin 1/2 heisst Spinorfeld" (teils geprueft):**
   - Kaehler-Dirac (Formen) kommt ohne Vierbein aus [S Abstract].
   - [H]: Auf einer Kausalmenge sind Ketten die Simplizes des Ordnungskomplexes, d. h. ein Korand d waere intrinsisch.
     Ob es einen Kaehler-Dirac-Operator auf Kausalmengen gibt, ist nach Recherchestand nicht belegt (keine Abfrage
     dazu).
4. **"Mein Gedaechtnistitel Foster/Jacobson stimmt" (geprueft):** Ja, und der Inhalt traegt mehr als erwartet (V6). A8
   haette ihn faelschlich verneint (Methodenbefund: Abfrage zu eng).
5. **"BHS gilt auch fuer Null-Flaggen" (nicht bewiesen):** Satz 2 spricht von zeitartigen Richtungen.
   - Uebertragung: Fuer Nullrichtungen (S^2 unter SL(2,C)) gibt es kein invariantes Wahrscheinlichkeitsmass. Das
     Argument sollte tragen [ES].
6. **"Die Johnston-PDF der anderen Karte ist dieselbe Arbeit" (geprueft):** pdfinfo 172 Seiten, Titel "Quantum Fields
   on Causal Sets"; gelesen S. 140-155.

## 10. Kalibrierung

- **(a) An der Quelle gelesen:**
  - Surya-Zitate (Tensorfelder, Tangentialraum, Satz 2, euklidischer Fall)
  - Johnston 6.2-6.4
  - Sverdlov (Holonomien), Noldus ("dimension is put in by hand")
  - Nomaan X ("further constraints")
  - Foster/Jacobson (Tetraeder, keine Doppler, nicht unitaer, BCC fuer die Masse)
  - Abstracts von Catterall, Gudder, Griffin/Kieu, Kieu u. a., Cohen
  - die arXiv-Abfragen
- **(b) Nuetzlich verdichtet [ES]:**
  - S1 (nilpotentes Kontaktglied, s >= 2, triviale s = 2-Loesung)
  - Moderatoren M1 und M2
  - Loetform als Kopplungsgroesse (Regel 6)
  - FJ als Einschraenkung unserer unitaeren 4-Zustands-Regel
  - Spur(M_x/V_x) = 3 auf Voronoi-Netzen
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):**
  - Meine Sicherheit, dass "Spin nur aus der Ordnung" auf Kausalmengen unmoeglich sei, ist gewachsen. Gestuetzt ist
    sie durch:
    - fehlende Literatur (kein Beweis)
    - die BHS-Analogie (fuer Null-Flaggen nicht bewiesen)
    - S1, das nur fuer retardierte Wurzeln eines link-getragenen Propagators gilt
  - Zugleich hat sich die Frage in Regime zerlegt (M1, M2, Einbettung ja oder nein). Ein "unmoeglich" darf daraus
    nicht werden. Richtig ist: "keine Bauweise bekannt, und fuer zwei naheliegende Wege gibt es strukturelle
    Hindernisse".

## 11. Offene Fragen

1. Tragen Rahmen als Eichfreiheitsgrade mit nicht kompakter Gruppe (Sverdlovs Holonomie-Integration)? Ist das
   Integral ueber SO(3,1) nach Eichfixierung endlich?
2. Gibt es einen Kaehler-Dirac-Operator auf dem Ordnungskomplex einer Kausalmenge? Er braeuchte keine Rahmen, haette
   aber 4 "Geschmaecker" [H].
3. Ist QCA-DIAMANT-4 Teil B exakt die unitaere Erweiterung des FJ-Schachbretts? Das muss gegen FJ Gl. (11) geprueft
   werden.
4. **Fermionischer SJ-Zustand in 1+1:** Nach Nomaan X ist das leicht, sobald S_R existiert, und SCHACHBRETT-KAUSAL-1
   liefert S_R. Das waere ein billiger Folgeschritt.
5. Ist die u/v-Zerlegung einer 2D-Ordnung bis auf Vertauschung eindeutig (offene Frage aus SCHACHBRETT-KAUSAL-1)?
   - Madsen 2026, "On the Uniqueness of Embeddings of Causal Sets" (2607.05840), koennte das beruehren. Nur der Titel
     ist gelesen.
6. Erzwingt Johnstons Wurzel auf grossen Streuungen mit Kovarianz im Mittel eine eindeutige Loesung (M5)?

## 12. Selbstanzeigen

1. **Scratchpad-Verstoss:**
   - Um 09:05 habe ich beim Zaehlen eine Dateiliste (6,5 KB, nur Namen von Scout-Cache-Dateien) nach
     /tmp/claude-1000/scout-cs-list.txt geschrieben.
   - Um 09:05:52 geloescht, ls bestaetigt. Inhalt ohne Geheimnisse.
2. **Zeitangaben:** Zwei Zeilen im Abrufprotokoll (A1, L2) standen zuerst mit geschaetzten Zeiten. Sie sind auf
   date-Fenster berichtigt.
3. **Fremde Abrufdateien:**
   - Johnstons Doktorarbeit habe ich nicht neu abgerufen. Ich habe die heute schon von einer anderen Karte geladene PDF
     im tool-results-Ordner der Sitzung gelesen.
   - Dort nur lesend: pdfinfo und die erste Seite der heute geladenen PDFs, um sie zu finden.
4. **Abrufe:**
   - 13 von 15 WebFetch, keine Websuche. A7 war zu breit und prueft nichts, A8 zu eng.
   - Viermal konnte der Zusammenfasser das PDF nicht lesen (A2, A3, A5, A10). Gelesen habe ich dann per pdftotext auf
     stdout.
5. **Nur Abstract:** Catterall u. a., Gudder, Griffin/Kieu, Kieu u. a. und Cohen sind nicht am Volltext gelesen.
   Hatsugai/Wen/Kohmoto ist nur als Titel per Werkzeugauszug bekannt.
6. **Kein Gegenleser:** S1, D2/D3 und die FJ-Einschraenkung sind meine eigene Algebra, nicht frisch gegengelesen.
7. **Werkzeuge:**
   - Benutzt: grep, sed, jq, tr, sort, uniq, head, tail, wc, cut, find, xargs, pdftotext, pdfinfo, date, ls, rm, du.
   - Kein python und kein perl, keine Laeufe auf der .69. Kein Peerbus, kein Commit, kein Journal.
   - **Selbstanzeige awk:** Um 09:28 rief ich in einer Befehlszeile versehentlich "awk 2>/dev/null; true" auf.
     awk lief ohne Programm, die Ausgabe war unterdrueckt, Wirkung keine. Trotzdem ein Verstoss gegen "lokal kein awk".

## 13. Quellenliste (Abrufstand 2026-10-04, Zeiten aus dem Abrufprotokoll)

- **S. Surya**, "The causal set approach to quantum gravity", Living Rev. Relativ. (2019) [L], arXiv:1903.11544.
  - Lokale Textfassung RUNDE-22/geometrie-stand/hilfs/surya-1903.11544.txt, gelesen 09:04-09:05.
  - Z. 1525-1600, 7314-7322, 7928-7931, 8982-8990, 9242-9250 [S]
- **S. P. Johnston**, "Quantum Fields on Causal Sets", Doktorarbeit, Imperial College London 2010, arXiv:1010.5514.
  https://arxiv.org/abs/1010.5514
  - PDF aus dem tool-results-Ordner (heute von anderer Karte geladen), gelesen 09:09-09:12, S. 140-155 [S]
- **R. Sverdlov**, "Spinor fields in Causal Set Theory", arXiv:0808.2956v1 (2008). https://arxiv.org/abs/0808.2956
  - Abruf A2 09:07:57-09:08:42, pdftotext [S]
- **J. Noldus**, "Free Fermions on causal sets", arXiv:1305.0443v3 (2013, v3 26.01.2015).
  https://arxiv.org/abs/1305.0443
  - Abruf A3 09:07:57-09:08:42, pdftotext [S]
- **Nomaan X**, "Quantum Field Theory On Causal Sets", arXiv:2306.04800v1 (2023). https://arxiv.org/abs/2306.04800
  - Abruf A5 09:12:20-09:14:41, pdftotext [S]
- **B. Z. Foster, T. Jacobson**, "Spin on a 4D Feynman Checkerboard", arXiv:1610.01142v1 (2016).
  https://arxiv.org/abs/1610.01142
  - Abstract per API (A9), PDF A10 09:19:31-09:19:54, pdftotext [S]
- **S. Gudder**, "Inflation and Dirac in the Causal Set Approach to Discrete Quantum Gravity", arXiv:1507.01281 (2015);
  "A Unified Approach to Discrete Quantum Gravity", arXiv:1403.5338 (2014). Abstracts A9 [S Abstract]
- **S. Catterall, J. Laiho, J. Unmuth-Yockey**, "Kähler-Dirac fermions on Euclidean dynamical triangulations", Phys.
  Rev. D 98, 114503 (2018), arXiv:1810.10626. Abstract-Teil A4 [S Abstract, unvollstaendig]
- **C. J. Griffin, T. D. Kieu**, "How Do Fermions Behave on a Random Lattice?", hep-lat/9211022 (1992) [S Abstract,
  A13]. Dazu hep-lat/9210005 und hep-lat/9307011 nur als Werkzeugauszug (A12).
- **T. D. Kieu, J. F. Markham, C. B. Paranavitane**, "More on random-lattice fermions", hep-lat/9412048 (1994) [S
  Abstract, A13]
- **S. D. Cohen**, "QCD, Symmetry Breaking and the Random Lattice", hep-lat/0602021 (2006) [S Abstract, A13]
- **J. Y. L. Jones, Y. K. Yazdi**, "Spectral Spacetime Entropy for Quasifree Theories", arXiv:2602.16782 (2026)
  [S Abstract, lokal im Scout-Cache und A1]
- **R. Sverdlov**, "Electromagnetic Lagrangian on a causal set that resides on edges rather than points",
  arXiv:1805.08064 (2018) [S Titel, A6]
- **Madsen** (Erstautor; Vorname und Koautoren nicht gelesen), "On the Uniqueness of Embeddings of Causal Sets",
  arXiv:2607.05840 (2026) [S Titel, A11]
- **Abfragen (arXiv-API export.arxiv.org):**
  - A1: causal set(s) x fermion/spinor/Dirac
  - A6: causal set(s) x spin structure/tetrad/vierbein/quantum walk/Clifford/vector field/gauge field/electromagnetic
  - A7: ti:checkerboard (Fehlgriff)
  - A8: checkerboard/checkers x Feynman
  - A9: checkerboard x Jacobson oder causet(s) x fermion/spinor/Dirac
  - A11: causal set(s), neueste 60
  - A12: random lattice x fermion/doubling/Dirac/Weyl
  - A13: id_list
- **Lokal, Projekt:**
  - SCHACHBRETT-KAUSAL-1/ERGEBNIS.md, QCA-TETRA-1/ERGEBNIS.md, QCA-DIAMANT-4/ERGEBNIS.md
  - KAUSAL-4D-STABIL-L/DOSSIER.md (Abschn. 9, 12), RUNDE-38/WEICHE-STAND-20261004.md
  - RUNDE-22/geometrie-stand/ERGEBNIS.md (Z. 61, 790), RUNDE-37/UEBERLEITUNGEN-EMERGENZ.md (Z. 122)
  - Scout-Cache research-scout-claude-20260913/http-cache (Fenster 2026-08-31 bis 2026-10-02)

## 14. Einfach gesagt

Ein Elektron hat einen "halben Spin": Erst nach zwei vollen Umdrehungen ist es wieder ganz wie vorher. Auf einem
regelmaessigen Kristallnetz bekommt man das fast geschenkt, weil die Drehsymmetrie des Netzes es erzwingt. Auf dem
zufaelligen Raumzeit-Netz der Kausalmengen gibt es aber keine Drehungen, nicht einmal feste Richtungen. Deshalb hat
nach unserer Suche noch niemand gezeigt, wie dort ein Elektron mit halbem Spin von selbst entsteht; alle Vorschlaege
setzen eine Art Kompass an jeden Netzpunkt von Hand ein. Wir schlagen eine kleine Computerprobe vor, ob ein solcher
eingesetzter halber Spin auf einem ganz unregelmaessigen Netz wenigstens stabil laeuft; das ist Literatur und
Ueberlegung, keine Messung.
