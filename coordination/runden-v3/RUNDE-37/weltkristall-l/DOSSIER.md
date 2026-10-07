# WELTKRISTALL-L: Dossier (feldforscher fuer die Leitung claude-primary)

- **Zeiten (alle per date):** Start 2026-10-05 07:05:07 CEST. Arbeitsfeld ab 07:09:29. Netzabrufe F1 bis F8 von 07:12:00
  bis 07:18:03. Dieses Dossier ab 07:24:23, Hauptteil fertig 07:29:11 (date; danach nur diese Zeile, 07:29:18).
- **Auftrag:** Finn, woertlich: "Denk das weiter" (zur 600-Zelle aus ZELLE600-1). Karte KARTE.md bindend; WK1 bis WK4 und
  ihre Bedeutung unveraendert.
- **Kennzeichen:** [S] an der Quelle gelesen (mit Abschnitt, Gleichung oder Seite), [S Abstract], [L] Gedaechtnis,
  [L?] unsicher, [M] Schreibtisch (Kopfrechnung, nicht maschinell geprueft), [ES] eigener Schluss, [H] Hypothese,
  [P] Projektdatei.
- **Art:** Nur Literatur und Schreibtisch. Keine Messdaten, keine Rechnung auf der .69, nichts synthetisch Gerechnetes.
- **Arbeitsfeld mit allen Erwartungen und Ausgaengen:** ARBEITSFELD.md. Quellenkopien: quellen/ (Dateiname mit Abrufzeit).

## 1. Ergebnis zuerst

1. **H1 ist im Kern dynamische Triangulierung (DT), keine neue Idee.**
   - Fuer gleichseitige Tetraeder ist die Regge-Wirkung eine reine Zaehlung (Ambjorn/Goerlich/Jurkiewicz/Loll 2012,
     Gl. 70 [S]).
   - "Flach im Mittel" heisst dort N1/N3 = 6 arccos(1/3)/(2 pi). Das ist dasselbe wie q = 5,1043 Tetraeder je Kante und
     f6 = 10,43 % [M]. Die Zahl der Karte stimmt.
   - "Lambda klein" ist in DT der kleine Abstand der nackten Kopplung von einer Zaehl-(Entropie-)Schwelle (Abschn. 7.1 [S]).
   - Reine Zaehlung waehlt nicht von selbst "flach", sondern Knaeuel (crumpled phase, S. 83 [S]).
   - Die Zufallsform ~ N^(-1/2) passt nur in 4D zu Lambda. Als 3D-Raumkruemmung ist sie um rund 32 Groessenordnungen
     ausgeschlossen (Omega_k) [M].
2. **H2: Die Hopf-Faserung der 600-Zelle ist eine saubere diskrete Faserung, aber eine Fock-Kugel, keine
   Kustaanheimo/Stiefel-Bruecke.**
   - Die 120 Ecken bilden 12 Zehnecke ueber den Ecken eines Ikosaeders [M]. Der Rahmen (Clifford-Parallelen, Zehneck-
     Grosskreise) steht bei Kleman/Friedel 2008 [S].
   - Der faserfeste Teil des 600-Zellen-Laplace ist exakt das Doppelte des Ikosaeder-Laplace: 0; 5,528; 12; 14,472 [M],
     gegen die Eigenwerte aus ZELLE600-1 [P] geprueft.
   - Die n^2-Schalen n = 2, 4, 6 haben gar keinen faserfesten Anteil. Fuer KS fehlt der Radius.
   - KS und 600-Zelle verbindet keine gefundene Arbeit (F4, mit 24-Monats-Fenster).
3. **H3: Das 600-Zellen-Universum ist alt und gut belegt; neu waere nur die unimodulare Zeit, und die ist klassisch vorab
   ableitbar.**
   - Collins/Williams 1973 bauten Friedmann-Modelle aus "5, 16, or 600 dust-filled tetrahedrons" [S Abstract]. Es folgen
     viele Nachfolger bis Tsuda 2021 und Dittrich/Gielen/Schander 2022.
   - Gielen/Ried nennen feinere Triangulierungen ausdruecklich als naechsten Schritt [S]. Ihre klassischen Loesungen sind
     "mostly the same" wie im Standard-Regge-Kalkuel [S].
4. **H4: Kleinerts Weltkristall liest freie Rahmendrehungen eher als Eichfreiheit bzw. kondensierte Versetzungen.**
   - Torsion gegen Kruemmung ist dort eine Eichwahl (Einstein- gegen Teleparallel-Eichung) [S Abstract, Bennett u. a. 2013].
   - Versetzungen sind kondensiert, Torsion daher unsichtbar [S Abstract, Kleinert/Zaanen 2004]. Das passt zur Energie null
     und zum Nullband an allen k in TORSION-STEIF-1 [P, ES].
   - In der 600-Zelle laufen Kleman/Friedels "Disvektionen" (gekruemmte Versetzungen) laengs der Hopf-Fasern; der kleinste
     Burgers-Vektor ist eine Kante [S]. **H2 und H4 sind dort dieselbe Struktur.**
5. **Groesster Fund fuer Finns Netz: Im Frank-Kasper-Kristall C15, der geordnet "geplaetteten 600-Zelle", bilden die
   Defektlinien ein Diamantgitter** (Doye/Wales 2001, S. 3 [S]). Das Kupfer-Teilgitter des Vorbilds MgCu2 ist ein
   Pyrochlor [L].
   - Finns Diamant-/Pyrochlor-Netz ist damit das Defektgeruest des geordneten Zweigs.
   - Kartenvorschlag DEFEKT-NETZ-1: TT-Isotropie von C15 und A15 gegen Netz V.

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | Erwartet | Gefunden | Quelle |
|---|---|---|---|
| V1 | Karte: "Lambda bzw. Flachheit als Abzaehlung" nicht gefunden, also eigene Hypothese | Die Regge-Wirkung gleichseitiger Simplexe **ist** eine Zaehlung (Gl. 70, 73). Lambda ist dort der Abstand zur Entropieschwelle, auf die fein abgestimmt werden muss. | AGJL 2012 [S] |
| V2 | Diamant-Netz gehoert auf S^3 zur 120-Zelle (KEGEL-4D-L V3), nicht zur 600-Zelle | Im flachen Raum ist das Diamantgitter das **Disklinationsnetz von C15**, also der geordneten geplaetteten 600-Zelle | Doye/Wales 2001, S. 3 [S] |
| V3 | Kleinert: "Versetzung = Torsion" reicht, die 4 Rahmendrehungen waeren Versetzungen | Kleinerts Modell hat eine **Eichsymmetrie Torsion <-> Kruemmung**; im nematischen Weltkristall sind Versetzungen kondensiert, Torsion unsichtbar | Bennett u. a. 2013, Kleinert/Zaanen 2004 [S Abstract] |
| V4 | Sadoc/Mosseri beschreiben die Hopf-Faserung der {3,3,5} | Auf arXiv nicht (5 Treffer: Phyllotaxis, Kollagen, Qubits). Belegt ist sie bei Kleman/Friedel, und dort als **Bahn der Disvektionen** | F3; K/F 2008 VII.C.2, Anh. D [S] |
| V5 | Zufallsschwankung ~ 1/sqrt(N) erledigt die Feinabstimmung "von selbst" | Nur in d = 4 dimensional passend; reine Zaehlung (Entropie) zieht den Mittelwert weg von flach (crumpled) | [M]; AGJL S. 83 [S] |
| V6 | Coxeters statistische Wabe (q = 5,104, Z = 13,4) auf arXiv auffindbar | 0 Treffer; bleibt [L] | F7 |
| V7 (klein) | Liu/Williams und DGS nennen die 600-Zelle im Abstract | Nicht ausdruecklich; die 600-Zelle bei DGS nur ueber Gielen/Ried (Tab. 3 von [5]) | F1 [S Abstract]; Gielen/Ried Abschn. IV [S] |

## 3. Urteile WK1 bis WK4

| Nr | Erwartung (Karte, unveraendert) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| WK1 | [L?] Nelson 1983 beschreibt Metallglaeser als "geplaettete" 600-Zelle mit Disklinationslinien; der mittlere Defektanteil folgt aus der Krumm-Flach-Bilanz | 75 % | **im Kern eingetroffen, nur ueber Sekundaerquellen; die Zahl selbst nicht an einer Quelle** | Tarjus u. a. 2005, S. 9-10 [S]: Nelson und Mitarbeiter, Rueckweg von der {3,3,5} in den flachen Raum "necessarily forces in topological defects", vor allem Disklinationen. Fussnote [44] [S]: "positive and negative disclinations must balance each other to ensure that space is 'flat' on average"; relativ zur Ikosaeder-Vorlage ein Ueberschuss von "-72 Grad"-Keildisklinationen. Kleman/Friedel S. 39-40 [S, P R22]. Nelson 1983 selbst nicht gelesen (nicht frei). Die Zahl f* = 10,43 % steht in keinem gelesenen Text; sie ist [M], die Zuschreibung an Coxeter 1958 [L]. |
| WK2 | [L?] Sadoc/Mosseri beschreiben die Hopf-Faserung der 600-Zelle mit dem Ikosaeder als Basis | 70 % | **in der Sache eingetroffen, in der Zuschreibung nicht belegt** | Sadoc/Mosseri: auf arXiv kein solcher Abstract (F3); ihr Buch 1999 [L?]. Kleman/Friedel 2008, Anh. D und VII.C.2 [S]: Clifford-Parallelen, Hopf-Faserung, Grosskreise aus 10 Kanten, 12 naechste Nachbarn auf einem Ikosaeder. Ikosaeder als Basis der 12 Zehnecke: [M] (Abschn. 4, H2), gegen ZELLE600-1 geprueft. |
| WK3 | [L?] Collins/Williams 1973 rechneten ein Friedmann-Universum aus der 600-Zelle im Regge-Kalkuel | 60 % | **eingetroffen** | INSPIRE (Abstract von APS) [S Abstract]: "Models for the Friedmann Universe are constructed from 5, 16, or 600 dust-filled tetrahedrons connected so as to form a closed space. Using the techniques of Regge calculus the time development ... compared with the standard analytic solution". |
| WK4 | [H] Eine Arbeit, die Lambda bzw. Flachheit ausdruecklich aus dem Defektanteil eines Tetraeder-Netzes ableitet, gibt es nicht (nach Recherchestand) | 60 % | **nach Wortlaut eingetroffen; die vorab notierte Bedeutung traegt nur eingeschraenkt** | F5 (alle Jahre, 24-Monats-Fenster mit vier Treffern aus 2025 abgedeckt) und F7: keine solche Arbeit. Aber AGJL 2012 [S]: Gl. (70) ist die Flachheitsbedingung als Zaehlung; Abschn. 7.1: Lambda als Abstand zur Zaehlschwelle. "H1 als eigene Hypothese" gilt nur fuer die Sprache "Defektanteil" und die Bruecke zu Frank-Kasper/Nelson, nicht fuer den Kern. |

**Bedeutung nach der Karte, angewandt:**
- WK1 bis WK3 sind in der Sache eingetroffen. Damit gilt die Lesart der Karte: Die 600-Zelle ist die gemeinsame Mitte von
  Kristall (FK), Glas (Nelson), Kosmologie (Collins/Williams) und Wasserstoff-Geometrie (Fock). Neu ist nur die
  Kombination.
- WK4 ist nach Wortlaut eingetroffen. Die vorab notierte Folge ("H1 ist eine eigene Hypothese fuer Finn") muss ich
  einschraenken: Der Zaehlkern ist DT (V1). Die "klare Grenze" (Datenprobleme der einfachen Zufallsform) gilt weiter
  [P GLIED-10] und wird um die Dimensionsschranke (3D ausgeschlossen) ergaenzt.

## 4. H1 bis H4

### H1: Lambda bzw. Flachheit als Abzaehlproblem

- **Literatur [S]:**
  - **AGJL 2012, Abschn. 2.5:** "the action becomes simple, depending only on the global number of simplices and
    (d - 2)-subsimplices".
  - **Gl. (70)**, 3D, alle Tetraeder gleichseitig: S_E = -2 pi kappa N1 + N3 (6 kappa arccos(1/3) + (sqrt 2/12) lambda).
    "One recognizes arccos 1/3 as the dihedral angle of an equilateral tetrahedron, and the term 2 pi N1 as coming from the
    2 pi which enters in the definition of the deficit angle". Dazu Gl. (71): N0 - N1 + N3 = 0.
  - **Gl. (73)**, 4D CDT: S_E = -(kappa0 + 6 Delta) N0 + kappa4 (N4^(4,1) + N4^(3,2)) + Delta (2 N4^(4,1) + N4^(3,2)).
    kappa4 wird auf den kritischen Wert kappa4(kappa0, Delta) gesetzt (S. 32).
  - **Abschn. 7.1, S. 68:** "The cosmological-constant term contributes at the same leading order as the entropy (the
    number of triangulations with a given number N4 of four-simplices) ... the exponential growth defines a critical
    point, to which one has to fine-tune the bare cosmological constant ... the renormalized, physical cosmological constant
    is defined by this approach to the critical value". In 2D: lambda = lambda_c + Lambda a^2 (Gl. 114, 127).
  - **S. 83:** Bei kappa0 = 0 (feste N4, "no action, but only the entropy") liegt die "crumpled phase": "a few links and
    their vertices acquire a very high order"; "These 'crumpled' triangulations are the generic, entropically preferred
    triangulations." Mit wachsendem kappa0 folgt ein Uebergang erster Ordnung zu verzweigten Polymeren.
  - **Tarjus u. a. 2005, Fussnote [44]:** "flat on average" als Ausgleich positiver und negativer Disklinationen.
  - **everpresent Lambda [P, GLIED-10]:** ZAS 2018 "fits as well as LCDM" (Existenz). DNY II 2024: echte Daten atypisch.
    Simon 2026 (Zenodo, unbegutachtet): SN-Gewinner scheitern an DESI DR2 (Delta chi^2 +128 bis +1974).
- **Schreibtisch [M]:**
  - **M1:** theta = arccos(1/3) = 1,230959 rad, delta5 = 2 pi - 5 theta = 0,128388 rad, delta6 = delta5 - theta.
    Mittel null bei f* = delta5/theta = 0,10430. Allgemein (beliebige Mischung): mittlere Zahl q = 2 pi/theta = 5,1043.
    Ueber Z (Nachbarn je Ecke): Tetraeder je Ecke 2Z - 4, also q = 6(Z - 2)/Z, flach bei Z = 13,397.
  - **M2:** Integral R dV = 2 Summe(l delta) (Regge). Mit N1/N3 = 6/q und V = N3 l^3/(6 sqrt 2) folgt
    <R> = 72 sqrt(2) theta Delta f/(q l^2) ~ 24,6 Delta f/l^2. Die Karte hat die Skalierung richtig, der Vorfaktor ist ~25.
    Probe an der 600-Zelle (q = 5, f = 0, l = 1/phi): 6,845, gleich 2 x 57,131/16,6925 aus ZELLE600-1 [P].
  - **M3 (DT-Form):** Summe_e delta_e = 2 pi N1 - 6 theta N3. Mit Gl. (71) ist flach gleichbedeutend mit N1/N3 = 1,1755 bzw.
    N0/N3 = 0,1755. Die 600-Zelle hat N0/N3 = 0,2, ist also positiv gekruemmt; das Vorzeichen stimmt.
  - **M5 (Lambda ist 4D):** Ein 3D-Netz misst die Raumkruemmung (Omega_k). Lambda gehoert zum 4D-Netz mit dem Dreieck als
    Scharnier: theta4 = arccos(1/4) = 75,52 Grad, q4 = 4,767, mit 4er- und 5er-Dreiecken f5* = 0,767. Fuenf 4-Simplexe je
    Dreieck ueberall geben das hyperbolische {3,3,3,5}, also das falsche Vorzeichen fuer Lambda > 0 [P KEGEL-4D-L].
  - **M6 (Zufallsform):** Ein Mittel ueber N Scharniere schwankt ~ N^(-1/2). Mit N ~ (H l_P)^(-d) Zellen im Hubble-Volumen
    gilt <R> ~ l_P^-2 (H l_P)^(d/2). **Nur fuer d = 4 ist das ~ H^2.**
    - 3D-Abschaetzung mit Vorfaktoren: Streuung 0,377 rad je Kante, N1 ~ 2,6e184 im Hubble-Volumen, sigma_R ~ 5e-92 l_P^-2.
    - Daraus Omega_k ~ 6e29, gegen |Omega_k| < ~2e-3 [L]: **rund 32 Groessenordnungen zu gross.**
  - **M7 (Zahl 1e-122):** Lambda l_P^2 = 3 Omega_L (H0 l_P/c)^2 = 2,85e-122 (H0 = 67,4, Omega_L = 0,685).
    - 4D, gleichseitig, l = l_P: <R4> ~ 103 Delta f/l^2 = 4 Lambda, also Delta f ~ 1e-123. Allgemein Delta f ~ Lambda l^2.
    - Fuer die Raumflachheit: Delta f < ~7e-126.
    - "Etwa 1e-122" stimmt also als Groessenordnung, aber nur fuer l = l_P.
  - **D6 (Irrationalitaet):** Exakt flach verlangt theta/pi = N1/(3 N3), also rational. Nach Niven ist arccos(1/3)/pi
    irrational [L-Satz]. Darum ist **kein endliches oder periodisches Netz regulaerer Tetraeder im Mittel exakt flach**.
    - FK-Kristalle haben rationale q: C15 q = 51/10 = 5,1000 (Z = 40/3), A15 q = 46/9 = 5,1111 (Z = 27/2) [M, Z-Werte L].
    - Sie liegen beidseits von q* und gleichen den Rest durch Verzerrung aus (flacher Raum, Spannung statt Kruemmung).
- **Bekannt [P]:** 7,36 Grad, 5,104, 63,2 Grad (GEOMETRIE-XD); Frank-Kasper als Disklinationsnetz, "decurving"
  (R22 geometrie-stand); everpresent Lambda mit Datenproblemen (GLIED-10); {3,3,3,5} hyperbolisch (KEGEL-4D-L).
- **Neu [H]:** Nur die Uebersetzung "Lambda klein = Defektanteil auf 1e-122 genau" und die Bruecke DT <-> Frank-Kasper:
  - C15 und A15 liegen beidseits der Flachheitszahl, also mit entgegengesetztem Kruemmungsvorzeichen im starren Bild.
  - Ob diese Bruecke so in der Literatur steht, habe ich nicht gezielt gesucht.
  - Die Dimensionsschranke (M6) ist vermutlich bekannt (Sorkin), aber nicht geprueft.

### H2: Hopf-Faserung als diskrete Kustaanheimo/Stiefel-Bruecke

- **Literatur [S]:**
  - **Kleman/Friedel 2008, Anh. D:** Rechte Schrauben x e^(alpha q) erzeugen Clifford-Parallelen, "S3 as a fiber bundle
    of great circles S1 over a great sphere S2, the Hopf fibration" (Fig. 36).
  - **Kleman/Friedel 2008, Abschn. VII.C.2 (S. 57):** Fuer alpha = pi/5 ist die Verschiebung "precisely the length of an
    edge"; sie fuehrt zu einem der "twelve nearest neighbors, which are at the vertices of an icosahedron". Die Bahn ist
    ein Grosskreis aus 10 Kanten; es gibt 72 solche Kreise (6 je Ecke).
  - **Mosseri/Sadoc 2025** (2511.15450, im 24-Monats-Fenster) [S Abstract]: Punktmenge auf S^3 "using a Hopf fibration
    approach" (Phyllotaxis), ohne 600-Zelle.
  - **KS:** Zheng u. a. 2026 (2609.19159) [S Abstract]: KS plus "fiber invariance under the Hopf fibration" ergibt
    g_n = n^2 im Kontinuum. Kibler/Negadi 2004: q-Deformation. **Keine** Arbeit verbindet KS mit der 600-Zelle (F4).
    Auch die 41 Abstracts zu "600-cell" (KEGEL-4D-L A1, heute 06:18) enthalten nichts dazu [P].
- **Schreibtisch [M]** (Einzelheiten ARBEITSFELD Abschn. 4):
  - **D1:** Rechte Nebenklassen x C10_q: 12 Zehnecke. Das Hopf-Bild x q x^-1 ist die Ikosaeder-Bahn von q, also 12
    Ikosaeder-Ecken.
  - **D2 (faserfester Sektor, Faserladung s = 0):** Er hat 12 Funktionen: 1 aus Grad 0, 3 aus Grad 2, 5 aus Grad 4 und 3
    aus dem 3'-Niveau. Die Grade 1, 3 und 5 tragen nichts, weil halbzahlige Spins unter C10 kein Gewicht 1 haben.
  - **D3:** Dort ist der 600-Zellen-Laplace genau 2 x Ikosaeder-Laplace: 0; 10 - 2 sqrt 5 = 5,528; 12;
    10 + 2 sqrt 5 = 14,472.
    - Das sind die ZELLE600-1-Niveaus 0; 5,52786; 12; 14,47214 [P], ohne Rest.
    - Die drei Eigenwerte erzwingen: Jede Ecke hat 2 Nachbarn auf ihrem Zehneck und je 2 auf den 5 benachbarten Zehnecken.
  - **D4:** Die n^2-Schalen sind Focks Kugelfunktionen vom Grad n - 1 (Impulsraum).
    - In KS liegt Wasserstoff im Sektor s = 0 mit den Graden 0, 2, ..., 2(n - 1) und braucht den Radius r = |u|^2.
    - Auf einer einzigen S^3-Schale bleibt davon nur der Winkelteil l = 0, 1, 2. Dazu kommt ein Bruchstueck von l = 3 als
      3' aus Grad 6; das passt zu "aus Grad 6 gefaltet" in ZELLE600-1.
  - **D5 (Ringe):** Unter der Lesart "Rechts-Stabilisator eines Rings = C10" umhuellen die 20 Boerdijk-Coxeter-Ringe 20
    Fasern derselben Faserung. Ihre Basispunkte sind die 20 Flaechenmitten des Ikosaeders (Dodekaeder-Ecken).
    - Jeder Ring besteht aus den 3 Zehnecken seiner Flaeche (30 Ecken); jedes Zehneck liegt in 5 Ringen.
    - [M, nicht gegengerechnet.]
- **Bekannt [P]:** Fock/KS, n^2 - s^2, Faserladung (KEGEL-4D-L); Spektrum und 20er-Zerlegung (ZELLE600-1).
- **Neu [H]:**
  - Die Faser-Zerlegung des 600-Zellen-Spektrums (D2, D3) fand ich in keinem Abstract (A1, F4). Gezielt nach "Hopf
    quotient 600-cell spectrum" gesucht habe ich nicht. Die Sache ist vollstaendig ableitbar, also Mathematik, keine
    Physik-Vorhersage.
  - Die Sektoren s ungleich 0 (Faserladung nur modulo 10 definiert) waeren diskrete Monopol-Kugelfunktionen auf dem
    Ikosaeder, also ein diskretes MICZ-Gegenstueck [H]. Die Literatur dazu habe ich nicht geprueft (Budget).

### H3: 600-Zellen-Universum mit Volumen-Takt

- **Literatur [S]:**
  - **Collins/Williams 1973** [S Abstract]: siehe WK3.
  - **Barrett/Galassi/Miller/Sorkin/Tuckey/Williams 1997** (gr-qc/9411008) [S Abstract, A1]: "a 600--cell Friedmann
    cosmology".
  - **De Felice/Fabri 2000/2001** [S Abstract, A1]: Die 600-Zellen-Entwicklung stoppt bei endlichem Volumen; "already
    studied before and all authors found a stop point".
  - **Liu/Williams 2016a** [S Abstract]: Collins/Williams- und Brewin-Modelle fuer Lambda-FLRW. Mit mehr Tetraedern wird es
    besser; alle Modelle enden, wenn zeitartige Streben lichtartig werden.
  - **Tsuda/Fujiwara 2021** [S Abstract, A1]: "Collins-Williams formalism", Lambda > 0. Die 4-Polytop-Universen wechseln
    zwischen Ausdehnung und Kontraktion; pseudo-regulaere Verfeinerung der 600-Zelle naehert das Kontinuum.
  - **Dittrich/Gielen/Schander 2022** [S Abstract]: Lorentz-Pfadintegral mit 4-Polytopen und Schalen, Lambda,
    No-Boundary-Vorschlag. Laut Gielen/Ried Abschn. IV [S]: "In table 3 of [5] ... the more refined 600-cell model results
    in much better agreement with the continuum".
  - **Gielen/Ried 2026** [S]:
    - Abschn. V: Klassisch sind die Loesungen der unimodularen Fassung "mostly the same as the ones of standard Regge
      calculus".
    - Unterschiede: die Rolle von Lambda und "the constraint that compact spacetimes without boundary must have zero
      4-volume".
    - Beide Modelle beruhen auf der 5-Zelle; "it would be worth investigating models based on more refined
      triangulations, again perhaps along the lines of [5]".
    - Abschn. III: "unimodular time has an interpretation as a volume time".
- **Schreibtisch [M, ES]:**
  - Im Collins/Williams-Modell mit 600-Zellen-Schnitten ist der unimodulare Zeitschritt das 4-Volumen der Schicht, also
    eine Zaehlung der Zellen mal Zellvolumen. "Finns Takt zaehlt Volumen" ist damit woertlich Gielen/Rieds unimodulare Zeit.
  - Regel 6: Fuer "Lambda klein" gibt es drei Wege (DT-Abstimmung, everpresent-Schwankung, unimodulare
    Integrationskonstante). Alle koppeln Lambda an dieselbe Groesse: das 4-Volumen bzw. die Zahl N4. H1 und H3 haengen an
    dieser einen Kopplung [ES].
- **Bekannt [P]:** Gielen/Ried (RUNDE-45/quellen-leitung); Tsuda 2021 (KEGEL-4D-L A1).
- **Neu [H]:**
  - Ein 600-Zellen-Modell mit unimodularer Zeit ist im Fenster 2025-06-24 bis 2026-10-05 nicht belegt (F8). Gielen/Ried
    kuendigen es an.
  - **Ableitbarkeit:** Klassisch ist es vorab ableitbar (gleiche Loesungen wie Standard-Regge, Zeit = 4-Volumen). Eine
    Rechnung waere Nachbau, keine Messung.
  - Nicht ableitbar waere erst der Quantenteil (Ueberlagerung von Lambda) oder der No-Boundary-Fall (siehe 5.2).

### H4: Freie Rahmendrehungen als Versetzungen im Weltkristall

- **Literatur [S]:**
  - **Kleinert/Zaanen 2004** [S Abstract]: Gravitation aus einem Weltkristall, der "a quantum phase transition to a nematic
    phase by a condensation of dislocations" durchlaufen hat. Titel: "Explaining the Absence of Torsion".
  - **Bennett/Das/Laperashvili/Nielsen 2013** (1209.2155) [S Abstract] ueber Kleinerts Modell: "Einstein's gravitation has
    a zero torsion as a special gauge, while a zero connection is another equivalent gauge with nonzero torsion which
    corresponds to ... teleparallelism. Any intermediate choice ... is also allowed."
  - **Kleman/Friedel 2008, VII.C.2** [S]: Versetzungen der gekruemmten {3,3,5} sind "Disvektionen" (linke und rechte
    Schrauben). Ihr Burgers-"Vektor" liegt tangential an den Clifford-Parallelen der Hopf-Faserung; der kleinste ist eine
    Kante.
  - Kein Treffer verbindet den Weltkristall mit Lambda aus der Defektdichte (F5). Jizba/Kleinert/Scardigli 2010:
    Unschaerfe auf einem Planck-Gitter.
- **Schreibtisch [M, ES]:**
  - TORSION-STEIF-1 [P]: 4 Nullmoden je Zelle, reine Rahmendrehungen mit x = D omega (Weitzenboeck), Energie null in der
    Einstein-Cartan-Wirkung, und zwar an **allen** 3915 k ungleich 0 (Nullband).
  - Ein Nullband an allen k ist das Kennzeichen einer lokalen Freiheit. Das passt zu beiden Lesarten:
    - (a) Eichrichtung (Kleinerts Torsion-Kruemmungs-Eichung);
    - (b) Maxwell-artige "weiche Mechanik" (18 Drehungen gegen 14 Bedingungen, wie lose Gelenke).
  - [L] Kondo, Bilby, Kroener: Versetzungsdichte = Torsion. Ein Kristall nur mit Versetzungen ist ein Weitzenboeck-Raum.
  - [L] Cartan/Schouten 1926: Auf S^3 = SU(2) ist die Clifford-Parallelitaet ein kruemmungsfreier Zusammenhang mit
    Torsion.
  - [ES] Auf der 600-Zelle sind also "Hopf-Faser", "Disvektion" und "Teleparallel-Rahmen" dieselbe Struktur.
- **Bekannt [P]:** Weltkristall: Disklination -> Kruemmung, Versetzung -> Torsion (R34); Schmidt/Kohler [L?] (R22); die
  4 Nullmoden (TORSION-STEIF-1).
- **Neu [H]:** Die 4 Nullmoden als diskretes Gegenstueck von Kleinerts Eichfreiheit oder eines kondensierten
  Versetzungssektors. Kleinert 2010 ("new gauge symmetry", arXiv 1005.1460 [L]) ist nicht abgerufen.

## 5. Regime, Moderatoren, Unterscheidungspunkte

### 5.1 Zwei Regime (Regel 1)

- **Regime A, bekannte Geometrie in neuer Kombination:** H1 = DT-Zaehlform, H2 = Gruppentheorie von 2I (Fock), H3 =
  Collins/Williams plus Gielen/Ried, H4 = Kroener/Kleinert. Alle vier liegen nach dieser Recherche hier.
- **Regime B, neuer physikalischer Gehalt:** Er laege nur vor, wenn eine Groesse ohne abgestimmte Kopplung von selbst
  richtig herauskaeme. Fuer H1 hiesse das: eine lokale Regel, die Delta f schneller als N^(-1/2) gegen null treibt. Gefunden
  habe ich dafuer nichts. Die Entropie treibt sogar weg (crumpled).
- **Moderatoren:**
  - **H1:** (i) Starre gleichseitige Kanten (Zaehlung = Kruemmung, DT) gegen elastische Kanten im flachen Raum (Zaehlung =
    Spannung, FK/Nelson). (ii) 3D-Schnitt (Omega_k) gegen 4D (Lambda).
  - **H2:** Welche S^3 (Fock-Impulsraum gegen KS-Konfigurationsraum) und welcher Fasersektor s.
  - **H3:** Offene Schicht gegen geschlossene 4-Geometrie; klassisch gegen Quanten.
  - **H4:** Ob eine Rahmensteifigkeit existiert (Energie auf Omega).

### 5.2 Unterscheidungspunkte (Regel 2)

| Paar | Wo sie messbar auseinanderlaufen | zugaenglich? |
|---|---|---|
| H1: starr (DT) gegen elastisch (FK) | Holonomie um eine Kante: starr dreht ein Band um delta (7,36 Grad an 5er-Kanten), elastisch um 0. Das misst der Arm "Linien" aus TORSION-STEIF-1 [P] | am Modell ja, in der Natur nein |
| H1: 3D-Zaehlung (Omega_k) gegen 4D-Zaehlung (Lambda) | Skalierung N^(-1/2): nur d = 4 gibt H^2 | **entschieden** [M]: 3D-Zufallsform um ~32 Groessenordnungen ausgeschlossen |
| H1: DT-abgestimmt (konstant) gegen everpresent (schwankend) | Zeitverlauf von Lambda, besonders frueh (r_d, CMB) | ja, Daten sprechen gegen die einfache everpresent-Form [P GLIED-10: DNY II, Simon 2026 unbegutachtet] |
| H1: neue Physik gegen DT umbenannt | eine Regel ohne abgestimmte Kopplung mit <Delta f> -> 0 schneller als N^(-1/2) | Modell ja; bisher in DT nein (crumpled) [S] |
| H2: Fock- gegen KS-Lesart | Faserladung der Niveaus: ungerade Grade (n = 2, 4, 6) haben keinen s = 0-Anteil; s = 0 ist das Ikosaeder | ja, **am Schreibtisch entschieden** [M]: Die n^2-Schalen sind Fock |
| H3: Standard- gegen unimodularen Regge | geschlossene kompakte 4-Geometrie (No-Boundary): unimodular verlangt 4-Volumen null [S Gielen/Ried]; Quanten-Ueberlagerung von Lambda | klassisch-offen nein (gleiche Loesungen); No-Boundary am Modell ja |
| H4: Eichrichtung gegen weiche Mechanik (physikalische Versetzung) | eine Energie direkt auf den Rahmendrehungen Omega: Eichmoden bleiben null, weiche Moden werden gehoben. In TORSION-STEIF-1 nicht gerechnet (dort Selbstanzeige 9) | am Modell ja; in der Natur nur ueber Spin-Torsions-Kontakt (praktisch unzugaenglich [L]) |

## 6. Kartenvorschlag (einer): DEFEKT-NETZ-1

- **Frage:** Laufen Schwerewellen (TT) auf den Frank-Kasper-Kristallen C15 und A15, den geordnet "geplaetteten
  600-Zellen" mit fast regulaeren Tetraedern, gleichmaessiger in alle Richtungen als auf Finns Netz V?
- **Warum jetzt:** Finns Weiche "Kristall/Glas: beide Zweige testen" (05.10.). Den Glas-Zweig decken TT-GLAS-1/2 ab
  [P], den Kristall-Zweig bisher nur V (6,34 %).
  - C15 ist der Kristall, den die 600-Zelle im flachen Raum vorschlaegt.
  - Seine Defektlinien bilden ein Diamantgitter [S Doye/Wales], sein Cu-Teilgitter ist ein Pyrochlor [L].
- **Netze:**
  - C15 (MgCu2-Typ, 24 Atome je kubischer Zelle) und A15 (Cr3Si-Typ, 8 Atome). Ideallagen ohne freie Parameter.
  - Die Wyckoff-Lagen vor dem Bau an einer Kristallographie-Quelle lesen; hier nur [L].
  - Tetraedrisierung per Delaunay mit demselben Code wie TT-GLAS-1.
- **Vorhersagen (vor jeder Rechnung):**

| Nr | Vorhersage | Art | Wahrsch. |
|---|---|---|---|
| DN0 | Kontrolle: Delaunay gibt nur Tetraeder; jede Kante traegt 5 oder 6; q = 5,1000 (C15) und 46/9 = 5,1111 (A15) auf 1e-9; die 6er-Kanten von C15 bilden ein Diamantnetz | Kontrolle, vorab ableitbar | 85 % |
| DN1 | Spanne s(C15) < s(V) = 6,34 % | [H] | 55 % |
| DN2 | s(C15) < s(A15) | [H] | 55 % |
| DN3 | s(C15) < 3 % | [H] | 30 % |

- **Bedeutung (vorab):**
  - **DN1 und DN2 treffen ein:** Ikosaedrische Nahordnung (die 600-Zellen-Mitte) ist der Weg zur TT-Isotropie im
    Kristall-Zweig. Begruendung [M]: Die Ikosaedergruppe hat Invarianten erst bei l = 0, 6, 10, ..., also keine bei l = 4;
    das l = 6-Stueck verbietet nach R45 die Eichinvarianz [P, dort M]. C15 hat 2/3 Ikosaederplaetze, A15 nur 1/4.
  - **DN1 scheitert:** Die kubische l = 4-Anisotropie dominiert unabhaengig von der Nahordnung. Die 600-Zellen-Bruecke
    bringt fuer TT keinen Vorteil.
  - **DN0 scheitert:** Delaunay ist entartet (kosphaerische Punkte). Dann zuerst die FK-Tetraeder aus der Kristallographie
    statt per Delaunay bauen.
- **Ableitbarkeitsprobe:**
  - DN0 ist vorab ableitbar (Kontrolle).
  - Die Spanne ist es nicht. Kubische Symmetrie laesst einen freien l = 4-Koeffizienten der TT-Steifigkeit; sein Wert
    haengt an den verzerrten Kantenlaengen der Z14-, Z15- und Z16-Umgebungen. Eine geschlossene Form kenne ich nicht [M].
  - DN1 und DN2 koennen also scheitern und bestehen.
- **Projekt-grep (07:20, alle Dateitypen, Ausschluesse wie vorgeschrieben):**
  - "DEFEKT-NETZ", A15, C15, Cr3Si, MgCu2, "Laves-Phase", "Friauf": keine Netzrechnung. Treffer nur Gleichungsnummern
    (A15) bzw. eine Konstante C15 in Beweisskripten.
  - Diamant + Disklination (*.md): nicht im Projekt.
  - Vorhanden und anschlussfaehig: TT-ISO-1 (V), TT-GLAS-1/2 (Glas), DANZER-NAEHERUNG-1.
  - Abgrenzung: Danzer ist der aperiodische Zweig mit exakter Ikosaedersymmetrie (Isotropie dort per Gruppentheorie,
    R45 [P]). DEFEKT-NETZ-1 prueft den periodischen FK-Zweig, in dem die kubische l = 4-Anisotropie global erlaubt ist.
    Offen ist also, wie viel der lokalen Ikosaeder-Isotropie im Kristall uebrig bleibt.
- **Aufwand:** klein (Zellen mit 8 bzw. 24 Punkten, periodische Superzellen wie TT-ISO-1), Kleintest-Spur auf der .69.
  Synthetisch, keine Messdatenbestaetigung.

## 7. Gegensweep (Regel 4), offene Fragen, Kalibrierung

### 7.1 Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1, geprueft:** Ist der Fasersektor der 600-Zelle wirklich das Ikosaeder? Bestanden. Alle drei faserfesten Eigenwerte
  aus ZELLE600-1 sind exakt 2 x Ikosaeder. Nebenergebnis: Die Nachbarverteilung 2 + 5 x 2 ist erzwungen.
- **G2, geprueft:** Vorzeichen der DT-Form an der 600-Zelle (Euler 120 - 720 + 600 = 0; N0/N3 = 0,2 > 0,1755, positiv).
  Bestanden.
- **G3, geprueft (an der Quelle):** Waehlt reine Zaehlung von selbst "flach"? **Nein** (crumpled, AGJL S. 83). Damit
  setzt die Zufallsform von H1 einen schon abgestimmten Mittelwert voraus.
- **G4, geprueft:** Messen "Delta = +0,0043" (R17/R22) und f* - f6(C15) = 0,0043 dasselbe? Nein. Das erste ist eine
  Energiedifferenz gekoppelter Ikosaeder. Keine Verbindung.
- **G5, nicht geprueft:** Sind die 4 Nullmoden genau Kleinerts neue Eichsymmetrie? Kleinert 2010 ist nicht abgerufen.
- **G6, nicht geprueft:** die Lesart "Rechts-Stabilisator C10" fuer die Ring-Basis (D5).
- **G7, nicht geprueft:** Meint H1 Lambda oder Omega_k? Die Karte sagt "bzw."; ich habe beides getrennt behandelt (M5, M6).

### 7.2 Offene Fragen

1. Nelson 1983 im Original: Steht dort die Dichte der -72-Grad-Linien als Zahl? Nicht frei zugaenglich.
2. 3D-EDT: Liegt der mittlere N0/N3-Sprung am Uebergang erster Ordnung beiderseits von 0,1755 (flach)? [L?] Nicht geprueft.
3. Wie lautet die Literatur zu diskreten Monopol-Kugelfunktionen auf dem Ikosaeder (Sektoren s ungleich 0 der
   600-Zelle)? Nicht geprueft.
4. Werden die 4 Rahmen-Nullmoden durch eine Energie auf Omega gehoben? Das ist der Unterscheidungspunkt fuer H4 (5.2),
   klein und rechenbar. Bewusst nicht als zweite Karte gefuehrt.
5. Unimodularer No-Boundary-Fall mit 600-Zellen-Rand: Was erzwingt die Bedingung "4-Volumen null" dort?
6. Das 24-Monats-Fenster fuer "unimodular + Regge" ist nur bis 2025-06-24 abgedeckt (F8 von Kombinatorik ueberflutet).

### 7.3 Kalibrierung

- **(a) Gemessen:** nichts Neues. Benutzt sind gerechnete Geometriezahlen aus ZELLE600-1 [P] als Probe.
- **(b) Nuetzlich verdichtet:**
  - H1 = DT-Zaehlform (Gl. 70);
  - der Hopf-Quotient der 600-Zelle = Ikosaeder mit doppeltem Laplace;
  - C15-Defektnetz = Diamant;
  - die Kopplung Lambda <-> 4-Volumen als gemeinsame Groesse von H1 und H3.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Die 4 Nullmoden sind Eichrichtungen" (nur Abstracts plus Nullband-Argument);
  - "Ringe ueber dem Dodekaeder" (D5);
  - "FK-Kristalle sind TT-isotroper" (reine Hypothese, darum Karte).
- **Warnzeichen:** Meine Sicherheit, dass H1 im Kern nicht neu ist, stieg waehrend der Recherche stark. Sie stuetzt sich
  auf [S] (Gl. 70, Abschn. 7.1). Sie gilt aber nur fuer den Zaehlkern, nicht fuer die FK-Bruecke, die ich nicht gezielt
  gesucht habe.

## 8. Quellenliste

**Abgerufen (quellen/, Abrufzeit im Dateinamen):**
- Ambjorn, J.; Goerlich, A.; Jurkiewicz, J.; Loll, R. (2012): Nonperturbative quantum gravity. Phys. Rep. 519, 127.
  https://arxiv.org/abs/1203.3591. [S] Abschn. 2.5, Gl. (70), (71), (73), S. 32, Abschn. 7.1 (S. 68), S. 83,
  Gl. (114), (127). Datei quellen/F6-arxiv-1203.3591-agjl-20261005-071527.pdf/.txt
- Collins, P. A.; Williams, R. M. (1973): Dynamics of the Friedmann universe using Regge calculus. Phys. Rev. D 7,
  965-971. https://doi.org/10.1103/PhysRevD.7.965. [S Abstract] ueber INSPIRE (Quelle APS), 61 Zitate.
  Datei quellen/F2-inspire-collins-williams-20261005-071225.json
- Liu, R. G.; Williams, R. M. (2016a): Regge calculus models of the closed vacuum Lambda-FLRW universe. Phys. Rev. D 93,
  024032. https://arxiv.org/abs/1501.07614 [S Abstract]
- Liu, R. G.; Williams, R. M. (2016b): Regge calculus models of closed lattice universes. Phys. Rev. D 93, 023502.
  https://arxiv.org/abs/1502.03000 [S Abstract]
- Dittrich, B.; Gielen, S.; Schander, S. (2022): Lorentzian quantum cosmology goes simplicial. Class. Quant. Grav. 39,
  035012. https://arxiv.org/abs/2109.00875 [S Abstract]
- Tsuda, R.; Fujiwara, T. (2017): Expanding polyhedral universe in Regge calculus. PTEP 2017, 073E01.
  https://arxiv.org/abs/1612.06536 [S Abstract]
- Kleinert, H.; Zaanen, J. (2004): World nematic crystal model of gravity explaining the absence of torsion. Phys. Lett.
  A 324, 361. https://arxiv.org/abs/gr-qc/0307033 [S Abstract]
  (Diese fuenf: quellen/F1-arxiv-idlist-20261005-071200.xml)
- Bennett, D. L.; Das, C. R.; Laperashvili, L. V.; Nielsen, H. B. (2013): The relation between the model of a crystal
  with defects and Plebanski's theory of gravity. Int. J. Mod. Phys. A 28, 1350044. https://arxiv.org/abs/1209.2155
  [S Abstract]
- Jizba, P.; Kleinert, H.; Scardigli, F. (2010): Uncertainty relation on world crystal and its applications to micro
  black holes. Phys. Rev. D 81, 084030. https://arxiv.org/abs/0912.2253 [S Abstract]
- Carvalho, A.; Furtado, C. (2025): Conformal geometry and regularization of disclinations by a cosmological constant in
  (2+1) dimensions. https://arxiv.org/abs/2509.01635 [S Abstract]
  (Diese drei: quellen/F5-arxiv-weltkristall-lambda-defekt-20261005-071434.xml)
- Mosseri, R.; Sadoc, J.-F. (2025): Some attempts toward 3-dimensional phyllotaxy. https://arxiv.org/abs/2511.15450;
  Charvolin, J.; Sadoc, J.-F. (2011, 2013): https://arxiv.org/abs/1102.2359, https://arxiv.org/abs/1310.6853;
  Mosseri, R.; Dandoloff, R. (2001): https://arxiv.org/abs/quant-ph/0108137; Mosseri, R. (2003):
  https://arxiv.org/abs/quant-ph/0310053. [S Abstract] quellen/F3-arxiv-sadoc-mosseri-hopf-20261005-071236.xml
- Zheng, G.; Chen, P.; Wang, M.; Xue, W.; Zhang, B. (2026): Three-dimensional Coulomb discrete spectrum via symplectic
  geometry and phase-space constraints. https://arxiv.org/abs/2609.19159; Kibler, M. R.; Negadi, T. (2004): On the
  q-analogue of the hydrogen atom. https://arxiv.org/abs/quant-ph/0408151. [S Abstract]
  quellen/F4-arxiv-ks-diskret-20261005-071257.xml
- Gielen, S.; Ried, S. (2026): Unimodular boundary time for Regge calculus. https://arxiv.org/abs/2610.03479.
  [S] Abschn. III, IV, V (Projektkopie RUNDE-45/quellen-leitung); F8 bestaetigt sie als einzigen Gravitations-Treffer:
  quellen/F8-arxiv-unimodular-regge-20261005-071803.xml
- F7 (quellen/F7-arxiv-statistical-honeycomb-20261005-071624.xml): 0 Treffer.

**Lokal im Projekt gelesen (kein Abruf):**
- Kleman, M.; Friedel, J. (2008): Disclinations, dislocations and continuous defects: a reappraisal. Rev. Mod. Phys. 80,
  61. https://arxiv.org/abs/0704.3055. [S] Abschn. VII.C.1-2 (S. 57-58), Anh. D (S. 66-67). Text:
  RUNDE-22/geometrie-stand/hilfs/kleman-friedel-0704.3055.txt
- Tarjus, G.; Kivelson, S. A.; Nussinov, Z.; Viot, P. (2005): The frustration-based approach of supercooled liquids and
  the glass transition. J. Phys.: Condens. Matter 17, R1143. https://arxiv.org/abs/cond-mat/0509127. [S] S. 9-10,
  Fussnote [44]. Text: RUNDE-17/quellen-frustration/hilfs/p4-cm0509127.txt
- Doye, J. P. K.; Wales, D. J. (2001): Polytetrahedral clusters. https://arxiv.org/abs/cond-mat/0012333. [S] S. 1-3.
  Text: RUNDE-17/quellen-frustration/hilfs/p11-cm0012333.txt
- Aus KEGEL-4D-L A1 (all:"600-cell", 2026-10-05 06:18) [S Abstract]: Barrett, J. W.; Galassi, M.; Miller, W. A.;
  Sorkin, R. D.; Tuckey, P. A.; Williams, R. M. (1997), Int. J. Theor. Phys. 36, 815, https://arxiv.org/abs/gr-qc/9411008;
  De Felice, A.; Fabri, E. (2000, 2001), https://arxiv.org/abs/gr-qc/0009093, https://arxiv.org/abs/gr-qc/0106077;
  Tsuda, R.; Fujiwara, T. (2021), PTEP 2021, 083E01, https://arxiv.org/abs/2011.04120
- Projekt [P]: ZELLE600-1, GEOMETRIE-XD (R27), geometrie-stand (R22), WEITERGEDACHT (R34), KEGEL-4D-L, TORSION-STEIF-1,
  GLIED-10-KOLLAPS-EVERPRESENT-20260925.md (Simon 2026, DNY II 2024, ZAS 2018), TT-GLAS-1 (V 6,34 %).

**Nur Gedaechtnis [L]/[L?]:** Coxeter 1958 (Close-packing and froth, Illinois J. Math. 2, 746: statistische Wabe);
Nelson 1983 (PRB 28, 5515); Nelson/Spaepen 1989; Sadoc/Mosseri 1999 (Geometrical Frustration); Cartan/Schouten 1926;
Niven 1956; Kondo/Bilby/Kroener (Versetzungsdichte = Torsion); Kleinert 2010 (arXiv 1005.1460); MgCu2-Teilgitter
(Cu Pyrochlor, Mg Diamant); A15-/C15-Koordinationszahlen; |Omega_k| < 2e-3.

## 9. Selbstanzeigen

1. Alle Zahlen sind Kopfrechnung ohne maschinelle Probe (lokal kein python, awk, perl oder Rechenlauf).
2. Sieben Abrufe liefen per curl (arXiv-API, INSPIRE-API, arxiv.org-PDF) statt WebFetch, damit Quellenkopien entstehen.
   Das F6-PDF habe ich lokal mit pdftotext in Text umgewandelt (IO, keine Rechnung).
3. **L2 (Doye/Wales):** Die Erwartung stand erst nach dem Lesen im Arbeitsfeld. Dort ist das als Berichtigung B1
   vermerkt; der Satz "vor dem Lesen notiert" ist falsch.
4. Lokale Quellentexte (Kleman/Friedel, Tarjus, Doye/Wales) und die A1-Datei aus KEGEL-4D-L habe ich ohne Abrufzaehlung
   genutzt. Das spart Budget, aber die A1-Abfrage stammt von 06:18 und ist nicht von mir.
5. F8 war als 24-Monats-Suche nur teilweise wirksam (von Kombinatorik ueberflutet, Abdeckung bis 2025-06-24). F7 lieferte
   0 Treffer; ein Syntaxproblem der OR-Verknuepfung ist nicht ausgeschlossen. Nicht wiederholt (Budget).
6. D5 (Ringe ueber dem Dodekaeder) beruht auf meiner Lesart von "Rechts: 12 disjunkte Ringe mit 360 Tetraedern" in
   ZELLE600-1.
7. Nelson 1983 und Coxeter 1958 sind nicht gelesen. WK1 ist nur ueber Sekundaerquellen geurteilt.
8. Den Kartenvorschlag habe ich gegenueber dem Kandidaten der Karte veraendert: C15 zusaetzlich zu A15, Begruendung
   Diamant-Defektnetz. Die Wyckoff-Lagen sind [L].

## 10. Einfach gesagt

Die 600-Zelle ist die perfekte "Tetraeder-Kugel"; ein flacher Raum aus Tetraedern entsteht nur, wenn ungefaehr jede zehnte
Kante sechs statt fuenf Tetraeder traegt. Genau diese Zaehlregel benutzen Physiker seit den 1990er-Jahren als
Schwerkraft-Formel ("dynamische Triangulierung"), und dort ist auch die winzige kosmologische Konstante eine Frage sehr
genauen Zaehlens: Neu ist die Idee also nicht, nur ihre Sprache. Ueberraschend war, dass im Kristall C15, der geordnet
"flachgedrueckten 600-Zelle", die Fehlerlinien ein Diamantgitter bilden, also genau die Form von Finns Netz. Die
Hopf-Faserung zerlegt die 600-Zelle sauber in 12 Zehnerringe ueber einem Ikosaeder, ist aber eher eine Fock-Kugel als
eine Bruecke zwischen Kepler und Oszillator. Als kleiner naechster Test lohnt sich, ob solche Kristalle Schwerewellen
gleichmaessiger in alle Richtungen laufen lassen als Finns Netz V.
