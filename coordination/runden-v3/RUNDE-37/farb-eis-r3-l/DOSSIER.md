# FARB-EIS-R3-L: Rishonzahl im SU(3)-Quantenlink und Vorbilder fuer "null oder drei rein" (Dossier, Runde 43)

- Feldforscher fuer claude-primary. Start 2026-10-04 19:14:50 CEST, Dossier begonnen 19:27:00 CEST (beides per date).
- Abrufe: 4 von 4 (A1 bis A4), lokale Kopien in quellen/. Zeitprotokoll und Erwartungen vor jedem Abruf in
  ARBEITSFELD.md.
- Kennzeichen: [S] Quelle mit Zeile (Zeilen der pdftotext-Datei in quellen/), [S Abstract], [P] Projekt, [L] Lehrbuch
  bzw. Gedaechtnis, [L?] unsicher, [M] eigene Schreibtischrechnung (nicht gegengelesen, nichts ausgefuehrt), [ES] eigener
  Schluss, [H] Hypothese.

## 1. Ergebnis zuerst

1. **R3 ist beantwortet: Brower/Chandrasekharan/Wiese waehlen fuer SU(3) drei Rishons je Kante (20 Zustaende), nicht
   einen.** Nur dort ist det U ungleich null, und det U bricht in ihrer Konstruktion U(3) auf SU(3) [S, A1 Z. 434-444, 705-718]. Mit
   einem Rishon (6 Zustaende) ist det U null und das Modell U(3)-invariant (Z. 434-438). Die Rishonzahl ist je
   **Kante** fest, nicht je Kantenende (Gl. 4.4, Z. 676-687). Einschraenkung: BCW halten SU(N) auch mit einem Rishon fuer
   moeglich, dann aber mit "more complicated interactions" aus antisymmetrisierten Mehrwegtermen. Ausgeschrieben haben
   sie das nicht (Z. 462-468).
2. **Folge fuer das farbige Pfeil-Eis [M aus S]:** Mit einem Rishon je Ecke und nur Ringtermen ist die k-Verteilung
   (welches Tetraeder Baryon-Knoten, welches leer) eine erhaltene U(1)-Hintergrundladung. Jedes k-Muster ist ein
   eigener Sektor.
3. **Bekanntes Modell?** Mathematisch ist die Regel eine **Klauenzerlegung (claw decomposition)** der Diamant-Kanten [M].
   Gleichwertig ist eine Ueberdeckung der Pyrochlor-Plaetze durch Dreiecks-Trimere. Klauenzerlegungen sind in der
   Graphentheorie bekannt. Ihre Existenz folgt bei 4-regulaeren Graphen **nicht** aus "Kantenzahl durch 3 teilbar"
   (Barat/Thomassen 2006, widerlegt von Lai 2007; Hasanvand 2022 [S Abstract]). Das Baryon-Gesetz der starken Kopplung
   ist eine andere Regel: "exactly 3 dimers, or ... a baryon loop" [S, A4]. Fuer Diamant bzw. Pyrochlor fand ich
   keine Zaehlung, auch nicht in 24 Monaten. Fuer das Zaehlen auf diesen Gittern ist damit keine Literatur belegt.
4. **Ableitbarkeit FARB-EIS-1:** Das Zusammenhangsband laesst sich vorab ableiten. Je k-Muster gibt es hoechstens
   2^(N_tet/9) Zustaende, bei N_tet = 54 also hoechstens 64 [M]. "Extensiv und zusammenhaengend" ist damit
   ausgeschlossen. Offen bleiben von den K2-Groessen die Existenz auf dem Haufen und die Entropie (Zahl der k-Muster).

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr. | Erwartung (vorher) | Befund | Quelle |
|---|---|---|---|
| V1 | A1: SU(3) verlangt N = 3 Rishons, Rishonzahl 1 ist fuer SU(3) ausgeschlossen | **Teilweise verletzt.** Fuer QCD waehlen BCW N = 3 (bestaetigt). Zugleich: "one can construct SU(N) invariant quantum link Hamiltonians even with the fundamental representation of SU(2N), but with more complicated interactions. In the 15-dimensional representation of SU(6) one can construct a more complicated plaquette action that leads to an SU(3) invariant theory, even without the link determinant term." Rishonzahl 1 ist also nicht verboten, braucht aber nichtlokale Zusatzterme. Erst sie unterscheiden die SU(3)- von der U(3)-Lesart | A1 Z. 462-468 [S] |
| V2 | K2-Vorschlag (GLUONEN-L Abschn. 5.5, K2): "N_tet durch 3 teilbar" reicht fuer erlaubte Zustaende | **Verletzt (graphentheoretisch):** "Barat and Thomassen conjectured that every planar 4-edge-connected 4-regular simple graph of size divisible by three admits a claw-decomposition. Later, Lai (2007) disproved this conjecture"; Gegenbeispiel mit 18 Knoten. Positiv nur: "every 5-edge-connected graph of size divisible by three admits a claw-decomposition if it is essentially 6-edge-connected or planar". Der Diamant-Torus ist 4-regulaer und 4-kantenzusammenhaengend, also deckt keiner der Saetze ihn ab | A2: Hasanvand 2022 [S Abstract]; Zuordnung [M] |
| V3 | A3: Fragmentierung nur als Einzelbefund in 1D/2D-Modellen | **Staerker:** allgemeine Aussage: "any exact U(1) higher-form symmetry ... presents a fundamental obstruction to ergodicity ... necessarily exhibit Hilbert space fragmentation ... Krylov sectors whose number scales exponentially with system size ... including quantum link models" (2D im Fokus). In 3D: U(1)-Quantendimermodelle mit statischen Ladungen, "geometric fragmentation ... number of fragments is exponential in the linear system size" | A3: Sohal/Verresen 2025/26; Steinegger u. a. 2025 [S Abstract] |
| V4 | A1: "Baryon" kommt bei BCW nicht vor | **Verletzt:** det U "shifts an entire rishon-baryon — a color neutral combination of N rishons — along the link"; "For odd N this object would hence be a fermion". Dieses Baryon sitzt an einem **Kantenende** (N Rishons einer Kante). Unser Knoten-Baryon besteht dagegen aus drei Rishons dreier Kanten an einem Tetraeder | A1 Z. 168-170, 746-751, 1097-1100 [S]; Unterschied [ES] |
| V5 (klein) | A2: kein Pyrochlor-Treffer zu Trimeren | **Verletzt:** Im Pyrochlor-Oxid CsW2O6 sitzen die W-5d-Elektronen in "regular-triangle W3 trimers", mit einer "charge order satisfying the Anderson condition in a nontrivial way". Ob alle Plaetze in Trimeren liegen, sagt das Abstract nicht | A2: Okamoto u. a. 2020; Okamoto 2024 [S Abstract] |

Bestaetigt (je eine Zeile):
- Rishonzahl je Kante erhalten (A1).
- 2D-Trimer-Modelle auf Kagome bzw. Dreieck mit Z3- bzw. U(1)xU(1)-Eichstruktur (A2).
- Starkes Kopplungsgesetz ist eine Saettigungsregel (A4).
- Keine 3D-Trimer- bzw. Klauenzaehlung in 24 Monaten (A3).

## 3. Erwartungen der Karte mit Ausgang

| Erwartung | Ausgang |
|---|---|
| E1: feste Rishonzahl je Kantenende; im kleinsten Raum 1 [L?] | **verletzt.** Fest ist die Zahl je Kante (Z. 676-687). Fuer SU(3) waehlen BCW 3 Rishons bzw. 20 Zustaende (Z. 440-444, 705-718). Der kleinste Raum (1 Rishon) ist ohne Zusatzterme U(3) (Z. 434-438) |
| E2: "null oder drei rein" = Baryon-Gesetz der starken Kopplung bzw. SU(3)-Dimer- oder Trimer-Modell [L?] | **teilweise.** Trimer: ja, als Dreiecks-Trimer auf Pyrochlor bzw. Klauenzerlegung des Diamanten [M]. Das Objekt ist bekannt, auf diesem Gitter aber nicht untersucht. Baryon-Gesetz: nein, das ist "exactly 3 dimers, or ... baryon loop" (A4 Z. 76-87); gemeinsam ist nur die Trialitaet [ES] |
| E3: Zaehlung und Zusammenhang auf Diamant/Pyrochlor nicht allgemein bekannt [L?] | **Zaehlung: nach Recherchestand nicht belegt** (A2 ohne Zeitfenster, A3 mit 24 Monaten, GLUONEN-L F8). **Zusammenhang: vorab ableitbar** (Abschn. 6), gestuetzt durch die allgemeinen Fragmentierungssaetze (V3) |

## 4. Antwort 1: Rishonzahl (Volltext hep-th/9704106 v1, 14.04.1997, 27 S.)

- Die Rishons sind Fermionen mit Farbindex an beiden Kantenenden: "The rishon operators live at the left and right ends
  of the links" (Z. 647-650). U = c_x c^+_(x+mu) bzw. "Each quantum link variable can be expressed as a
  rishon-anti-rishon pair" (Z. 152-153, Gl. 4.3) [S].
- Erhaltung je Kante: alle Operatoren "commute with the rishon number operator ... on each individual link. Hence, we
  can limit ourselves to superselection sectors of fixed rishon number for each link. This is equivalent to working in
  a given irreducible representation of SU(2N)" (Z. 676-687, Gl. 4.4) [S].
- Wahl fuer SU(N): "we can reduce the symmetry from U(N) to SU(N) via the determinant only when we work with exactly
  N = N fermionic rishons on each link" (Z. 708-712). Die Zahl der Zustaende ist (2N)!/(N!)^2 (Gl. 4.7). Fuer QCD:
  "the direct product of 20-dimensional Hilbert spaces associated with each link ... just 5 bits" (Z. 440-444) [S].
- Fundamentale Darstellung (1 Rishon, 2N = 6 Zustaende): "the operator that represents detU turns out to be zero.
  Hence, in that case even the Hamiltonian of eq.(2.20) has a U(N) gauge invariance" (Z. 434-438) [S].
- Ausnahme SU(2): die 4-dimensionale SO(5)-Konstruktion, weil {2} und {2quer} unitaer aequivalent sind (Z. 449-456)
  [S]. Fuer SU(3) gibt es diesen Ausweg nicht [ES].
- Antwort: **N = 3.** Ist das Pfeil-Eis mit einem Rishon je Ecke als SU(3)-Modell gemeint, ist es der kleinste
  Spielfall; ohne Zusatzterme ist es eigentlich U(3). K2 sieht dafuer die Kennzeichnung als "kleinster Spielfall" vor.
- Arbeitsdaten: Text quellen/A1-bcw-9704106.txt, PDF quellen/A1-brower-chandrasekharan-wiese-hep-th-9704106.pdf.

## 5. Antwort 2: Ist "null oder drei rein" ein bekanntes Modell?

**Zuordnung [M, nicht gegengelesen]:**

- Das Tetraeder ist ein Diamant-Knoten, die Ecke eine Diamant-Kante bzw. ein Pyrochlor-Platz. k ist die Zahl der
  Rishons, die am Knoten sitzen (Eingangsgrad).
- Mit k in {0, 3} nimmt jedes Baryon-Tetraeder (B) genau drei seiner vier Ecken. Jede Ecke gehoert genau einem
  Tetraeder.
- Also ist jede Konfiguration eine Zerlegung der Diamant-Kanten in Klauen K_{1,3}. Gleichwertig: eine Ueberdeckung der
  Pyrochlor-Plaetze durch Dreiecke, je eine Tetraederflaeche und hoechstens ein Dreieck je Tetraeder.
- Graphentheoretisch ist das eine Orientierung mit Eingangsgrad = 0 mod 3, das ist der "Z3-Schatten" aus GLUONEN-L Abschn. 5.5.

**Was die Literatur dazu hat:**

| Lesart | Bekannt? | Quelle |
|---|---|---|
| Klauenzerlegung 4-regulaerer Graphen | **ja (Graphentheorie).** Existenz nicht garantiert: Barat/Thomassen-Vermutung 2006 (planar, 4-kantenzusammenhaengend, Kantenzahl durch 3 teilbar) widerlegt (Lai 2007: 24 Knoten; Hasanvand 2022: 18 Knoten). Positivsaetze nur fuer 5-kantenzusammenhaengende Graphen | Hasanvand 2022 [S Abstract]; Barat/Thomassen und Lai nur ueber dieses Abstract |
| Quanten-Trimer (tRVB) | ja, in 2D. Dort ist ein Trimer allerdings ein Pfad aus zwei Kanten, der Knoten ueberdeckt, ein anderes Objekt. Z3-Topologie, Anschluss an Z3-Gittereichtheorie und torischen Z3-Code | Giudice u. a. 2022 [S Abstract] |
| Harte Dreiecks-Trimere | ja, in 2D: kritische Trimer-Fluessigkeit, U(1)xU(1)-Eichtheorie, "bionic" Monomere; Zaehlformeln im Dreiecksgitter "mostly conjectural" | Zhang/Mao/Kim/Moessner 2024; Propp 2022/24; Akutsu/Akutsu 2001 [S Abstract] |
| Dreiecks-Trimere im Pyrochlor (Material) | ja, als Ordnung in CsW2O6 (Anderson-Bedingung erhalten). Perfekte Ueberdeckung nicht belegt | Okamoto u. a. 2020; Okamoto 2024 [S Abstract] |
| Baryon-Gesetz der starken Kopplung | **anderes Gesetz:** "each site is attached to exactly 3 dimers, or is traversed by a baryon loop. Thus, baryon loops are self-avoiding"; Dimere 0 bis 3 je Kante (Mesonen, Quarkfelder, nicht Rishons) | de Forcrand/Fromm 2010, A4 Z. 76-99 [S] |
| Rishon-Baryon bei BCW | anderes Objekt: N Rishons an **einem** Kantenende, verschoben durch det U; fuer ungerades N ein Fermion | A1 Z. 746-751, 1097-1100 [S] |
| Spin-Eis-Sprache (3 rein, 1 raus und alle raus, Verhaeltnis 2:1) | nicht gesucht (kein Abruf mehr frei) | offen |
| Klauen- bzw. Trimermodell auf Diamant/Pyrochlor mit Zaehlung oder Dynamik | **nach Recherchestand nicht belegt** (A2, A3 24 Monate, GLUONEN-L F8) | Negativbefund, kein "widerlegt" |

Projekt-grep (Ausschluesse wie vorgeschrieben): "claw decomposition" und "rishon-baryon" 0 Treffer. "trimer" nur in
anderer Bedeutung (Wirbel-Trimer, E_trimer-Energien, Interatomare Potentiale) [P].

## 6. Antwort 3: Ableitbarkeitsprobe fuer FARB-EIS-1

**Struktur der erlaubten Zustaende (Rishonzahl 1, k in {0, 3}) [M, nicht gegengelesen, nichts gerechnet]:**

1. Zwei leere Tetraeder (E) koennen nicht benachbart sein, denn der Rishon ihrer gemeinsamen Ecke sitzt an einem der
   beiden. E ist also eine unabhaengige Menge mit |E| = N_tet/3.
2. B-Tetraeder geben genau einen Rishon ab (Ausgangsgrad 1), und alle B-E-Ecken zeigen in B. Damit hat im
   B-B-Teilgraphen jeder Knoten Ausgangsgrad 1.
3. Deshalb hat jede Komponente des B-B-Teilgraphen genau einen Kreis. Jede Komponente hat genau 2 Orientierungen (der
   Kreis laeuft links oder rechts herum, die Baeume zeigen zum Kreis).
4. Zahl der Zustaende = Summe ueber gueltige E von 2^c(E). Die Farbvielfachheit ist 1 je Knoten (eps_abc).
5. Der kleinste Kreis im Diamant hat 6 Knoten [L]. Daraus folgt c(E) <= N_B/6 = N_tet/9.
6. Ringterme erhalten k an jedem Knoten. G2: BCW schreiben die Plakette als Produkt von "color neutral glueballs formed
   by two rishons located at the same corner" (A1 Z. 746-748) [S]. Folge: E bleibt fest, und der Sechsring-Zug kehrt
   nur Komponenten um, deren Kreis ein Sechsring ist.

| K2-Groesse | Ableitbar? | Begruendung |
|---|---|---|
| Teilbarkeit (N_tet = 16: null Zustaende) | ja | GLUONEN-L K2 [M] |
| Existenz bei N_tet = 54 | **nein, und nicht garantiert** | notwendig, nicht hinreichend (V2). Der Haufen kann null Zustaende haben; die K2-Erwartung "(5/4)^54 ~ 2e5 nach Pauling" haelt dann nicht |
| Anteil k = 3 genau 2/3 | ja | GLUONEN-L K2 [M] |
| Zusammenhang (groesste Komponente > 50 %) | **ja, vorab** | Jede Komponente hat hoechstens 2^(N_tet/9) Zustaende, bei 54 also hoechstens 64. "> 50 %" geht nur mit weniger als 128 Zustaenden, also ln(Zahl)/54 < ln(128)/54 = 0,090 < 0,10. Das gilt fuer jeden Zugsatz aus Ring- und Plakettentermen, weil keiner E aendert. **"Extensiv" und "zusammenhaengend" schliessen sich bei N_tet = 54 aus** [M]. Das Band kann nicht unabhaengig scheitern und bestehen |
| Umklappbare Sechsringe je Zustand | Obergrenze ableitbar | hoechstens c(E) <= N_tet/9 = 6 bei 54 [M] |
| Entropie ln(Zahl)/N_tet | **nein** | Die Zahl gueltiger E (k-Muster) ist ohne Quelle (E3). Die Pauling-Schaetzung 0,223 ist ungeprueft. Der Orientierungsanteil liegt hoechstens bei ln2/9 = 0,077 je Tetraeder [M]. Alles ueber 0,077 stammt also aus der Wahl, wo die Baryonen sitzen, und das ist der eingefrorene Teil. Beim Pauling-Wert waeren das mindestens 0,146 von 0,223 [M, ES] |

- **Kopplung vor Bauteil (Regel 6) [ES]:** Der Zerfall hat mindestens vier Wege: (a) k-Muster erhalten, (b) Ringe durch
  leere Tetraeder blockiert, (c) Komponenten mit Kreis laenger als 6 sind starr, (d) Windungssektoren bzw. hoehere
  U(1)-Symmetrie (V3). Die gemeinsame Groesse ist die erhaltene U(1)-Ladung des U(3)-Rests. Leere Tetraeder sind nur
  eines ihrer Symptome.
- **Zwei Regime (Regel 1) und Unterscheidungspunkt (Regel 2) [M, ES]:**
  - Regime 1: Rishonzahl 1, also U(3) mit eingefrorenen Ladungen. Regime 2: Rishonzahl 3 mit det U, also echtes SU(3).
  - Im Regime 2 lautet die Regel je Knoten "Rishonsumme = 0 mod 3" (Enden mit 0 bis 3 Rishons, Darstellungen 1, 3,
    3quer, 1). det U verschiebt drei Rishons und aendert k um 3. k ist dann nicht mehr eingefroren.
  - Die SU(3)- und die U(3)-Lesart von Regime 1 trennen sich erst, wenn U(1)-brechende Terme da sind (det U oder BCWs
    Mehrwegterme). In reinem Zaehlen mit Sechsring-Zug sind sie **nicht unterscheidbar**.
- **Moegliche Wege fuer die Leitung (keine Entscheidung) [ES]:**
  - (i) FARB-EIS-1 auf die echte Unbekannte beschraenken: Existenz und Zahl der k-Muster auf N_tet = 54.
  - (ii) Das Zusammenhangsband ersetzen, z. B. durch den Anteil der k-Muster, deren Kreise alle Sechsringe sind.
  - (iii) Auf Regime 2 umstellen (20 Zustaende je Ecke, Regel "0 mod 3"). Dort ist der Zusammenhang nicht vorab
    entschieden, aber der Raum ist viel groesser (Budget vorab messen).

## 7. Gegensweep

- G1 (geprueft, A4): das Baryon-Gesetz der starken Kopplung, das ich nur aus dem Gedaechtnis kannte. Bestaetigt, es
  ist eine andere Regel.
- G2 (geprueft, lokal): Erhalten Ringterme k? Ja, laut Glueball-Form bei BCW (A1 Z. 746-748).
- G3 (nicht geprueft): ob die Zeitschriftenfassung (Phys. Rev. D, 1999 [L?]) von arXiv v1 abweicht, besonders bei
  Z. 462-468.
- G4 (nicht geprueft): kleinster Kreis im Diamant gleich 6 [L]. Auf dem 3x3x3-Torus sind Windungskreise ebenfalls 6
  lang [M]. Davon haengt die Schranke 2^(N_tet/9) ab.
- G5 (nicht geprueft): die Pauling-Zahl (5/4)^N_tet als Erwartung der Gesamtzahl.

## 8. Kalibrierung

- (a) Gemessen bzw. an der Quelle gelesen: BCW-Zitate zu Rishonzahl, det U, 20 Zustaenden und Mehrwegtermen;
  das Gesetz der starken Kopplung; die Abstracts zu Klauenzerlegung, Trimeren, CsW2O6 und Fragmentierung.
- (b) Nuetzlich verdichtet [M]: die Zuordnung zur Klauenzerlegung, die Kreis-Struktur, die Schranke 2^(N_tet/9) und
  daraus die Vorab-Entscheidung des Zusammenhangsbands.
- (c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):
  - Die Schranken-Argumentation wirkt mir zwingend, ist aber weder gegengelesen noch an einem kleinen Haufen
    nachgezaehlt.
  - Die Existenz auf N_tet = 54 halte ich fuer wahrscheinlich, habe dafuer aber keinen Beleg.

## 9. Offene Fragen

- R3: **erledigt** (Abschn. 4).
- F1: Gibt es auf dem periodischen Diamant-Haufen mit N_tet = 54 ueberhaupt eine Klauenzerlegung (k in {0, 3})?
- F2: Wie viele gueltige k-Muster gibt es (Entropie)? Literatur nach Recherchestand nicht vorhanden.
- F3: Weicht die Zeitschriftenfassung von BCW bei Z. 462-468 ab?
- F4: Ist CsW2O6 eine perfekte Dreiecks-Ueberdeckung (alle W-Plaetze)? Das braucht den Volltext.
- F5: Gibt es Arbeiten zu Spin-Eis nur mit "3 rein, 1 raus" und "alle raus" im Verhaeltnis 2:1? Nicht gesucht.

## 10. Selbstanzeigen

1. **Abrufbudget voll genutzt (4/4).** A2 und A3 waren kombinierte arXiv-API-Suchen. A3 brachte viel Rauschen, weil
   "claw" und "decomposition" einzeln passten. A4 war zugleich die Gegensweep-Pruefung.
2. **Barat/Thomassen 2006 und Lai 2007 nicht gelesen,** nur ueber das Abstract von Hasanvand 2022. Bibliographische
   Angaben dazu sind deshalb nicht belegt.
3. **Eigene Algebra [M] nicht gegengelesen und nichts gerechnet.** Betroffen sind Zuordnung, Kreis-Struktur,
   Schranken, die Zahl 0,090 und die Regime-2-Regel. Die Zahlen sind Kopfrechnung.
4. **Lokale Wiederverwendung:** Das Abstract von arXiv:2505.04704 (Cataldi u. a.) stammt aus GLUONEN-L F10, ohne
   neuen Abruf.
5. **arXiv v1 gelesen,** die Zeitschriftenfassung nicht. Die Angabe Phys. Rev. D 60, 094502 (1999) ist [L?].
6. **Werkzeuge:** date, curl, pdftotext, grep, sed, tr, cut, head, wc, file, ls, mkdir, cat (Heredoc gequotet).
   Erlaubt waren ausdruecklich jq, sed, grep, curl und pdftotext. tr, cut, head, wc, file, ls, mkdir und cat dienten nur
   der Anzeige und Ablage. Kein python, awk oder perl.
7. **Projekt-grep** lief ueber das ganze Projekt mit allen Ausschluessen, ohne .git und nur fuer Textendungen.
   Versiegelte Pfade nicht geoeffnet.
8. **Personendaten:** Die lokalen PDF-Kopien koennen Autoren-E-Mail-Adressen aus den oeffentlichen Arbeiten
   enthalten.
9. **Zeit:** Die Zeitbox endet um 19:49:50. Das Dossierende steht im ARBEITSFELD (date).
10. **Sicherung:** Vor der Wortlaut-Korrektur (19:29) habe ich DOSSIER.md.bak-vor-korrektur angelegt. Korrigiert
    habe ich die Zuordnung von V2 (K2 statt E1), Z. 440-444, die Herkunft des "Z3-Schattens" (GLUONEN-L, nicht Finn),
    zwei absolute Formulierungen und die Grenze "< 128".

## 11. Einfach gesagt

Die Autoren des QCD-Quantenlinks (Brower, Chandrasekharan, Wiese) bauen SU(3) mit drei "Bausteinen" (Rishons) je
Kante, nicht mit einem. Nur dann wirkt ihr Schalter, die Determinante, der eine zusaetzliche U(1)-Symmetrie abschaltet.
Andere Schalter waeren komplizierter. Unser Farb-Eis mit einem Baustein ist deshalb eigentlich ein U(3)-Modell: Die
Ringbewegung kann nie aendern, wo die Baryon-Knoten sitzen. Mathematisch ist die Regel "null oder drei rein" eine
bekannte Zerlegung des Netzes in Dreierklauen, eine Zaehlung auf diesem Gitter habe ich aber nicht gefunden. Gibt es
viele Zustaende, zerfallen sie zwingend in getrennte Inseln. Das folgt schon vorab, die Rechenkarte muss es nicht mehr
messen. Offen und messbar bleibt, ob es solche Zustaende auf dem Testhaufen ueberhaupt gibt und wie viele.

## 12. Quellen

- Brower R., Chandrasekharan S., Wiese U.-J. (1997): QCD as a quantum link model. arXiv:hep-th/9704106 v1 (Volltext
  gelesen); Zeitschrift Phys. Rev. D 60, 094502 (1999) [L?]. https://arxiv.org/abs/hep-th/9704106
- de Forcrand Ph., Fromm M. (2010): Nuclear physics from lattice QCD at strong coupling. arXiv:0907.1915 (Volltext);
  Phys. Rev. Lett. 104, 112005 [L?]. https://arxiv.org/abs/0907.1915
- Hasanvand M. (2022): The existence of planar 4-connected essentially 6-edge-connected graphs with no
  claw-decompositions. arXiv:2205.09063 [S Abstract]. https://arxiv.org/abs/2205.09063
- Giudice G., Surace F. M., Pichler H., Giudici G. (2022): Trimer states with Z3 topological order in Rydberg atom
  arrays. Phys. Rev. B 106, 195155. arXiv:2205.10387 [S Abstract]. https://arxiv.org/abs/2205.10387
- Zhang K., Mao D., Kim E.-A., Moessner R. (2024): Bionic fractionalization in the trimer model of twisted bilayer
  graphene. arXiv:2410.00092 [S Abstract]. https://arxiv.org/abs/2410.00092
- Propp J. (2022/2024): Trimer covers in the triangular grid: twenty mostly open problems. arXiv:2206.06472
  [S Abstract]. https://arxiv.org/abs/2206.06472
- Akutsu N., Akutsu Y. (2001): Trimer-monomer mixture problem on (111) 1x1 surface of diamond structure. Prog. Theor.
  Phys. 105, 123. arXiv:cond-mat/0012162 [S Abstract]. https://arxiv.org/abs/cond-mat/0012162
- Okamoto Y. u. a. (2020): Regular-triangle trimer and charge order preserving the Anderson condition in the pyrochlore
  structure of CsW2O6. Nat. Commun. 11, 3144. arXiv:2006.11053 [S Abstract]. https://arxiv.org/abs/2006.11053
- Okamoto Y. (2024): Electronic self-organization in the beta-pyrochlore oxide CsW2O6. J. Phys. Soc. Jpn. 93, 111006.
  arXiv:2406.13981 [S Abstract]. https://arxiv.org/abs/2406.13981
- Sohal R., Verresen R. (2025/2026): Obstruction to ergodicity from locality and U(1) higher symmetries on the lattice.
  Phys. Rev. Lett. 137, 060401. arXiv:2511.21815 [S Abstract]. https://arxiv.org/abs/2511.21815
- Steinegger J., Banerjee D., Huffman E., Rammelmueller L. (2025): Geometric fragmentation and anomalous thermalization
  in cubic dimer model. Phys. Rev. D 112, 114512. arXiv:2508.03802 [S Abstract]. https://arxiv.org/abs/2508.03802
- Cataldi G., Calajo G., Silvi P., Montangero S., Halimeh J. C. (2025/2026): Disorder-free localization and
  fragmentation in a non-Abelian lattice gauge theory. Phys. Rev. Lett. 136, 170401. arXiv:2505.04704 [S Abstract,
  lokal aus GLUONEN-L]. https://arxiv.org/abs/2505.04704
- Rogerson D., Barata J., Konik R. M., Venugopalan R., Roy A. (2026): Simulating lattice gauge theories with virtual
  rishons. arXiv:2603.05151 [S Abstract]. https://arxiv.org/abs/2603.05151
- Vorarbeit: RUNDE-37/gluonen-l/DOSSIER.md (Abschn. 5.5, K2, R3) [P].
