# REGGE-TORSION-L: Arbeitsfeld (feldforscher, eine Datei fuer alles; Gestrichenes bleibt stehen)

- Start 2026-10-04 23:15:51 CEST (date). Zeitbox 35 min, also bis 23:50:51 CEST.
- Budget: hoechstens 3 Abrufe (WebFetch, arXiv-API bzw. arxiv.org/abs bzw. /pdf). Keine Websuche.
- Kennzeichen: [S] Quelle mit Abschnitt/Gleichung, [S Abstract], [L] Gedaechtnis, [M] Mathematik, [ES] eigener
  Schluss, [H] Hypothese, [P] Projektdatei.
- Erwartungen RT1 bis RT3 stehen bindend in KARTE.md und werden hier nicht geaendert.

## 0. Vorgelesen (nur lesen, 23:15:51 bis 23:16:15 CEST)

- RUNDE-44/GEMEINSAMES-NETZ-v3.md: vorhanden, ganz gelesen. Fuer diese Karte tragend:
  - L1 (eine Schrittregel; skalare Regel zweiter Klasse, auch langwellig auf gefuelltem Netz) [P].
  - L3 (Schwerkraft aus demselben Netz; Spin-2-Ausbreitung bindet, TT anisotrop) [P].
  - L4 (Spin 1/2 als Dynamik): Guertel-Trick im SO(3)-Drehfeld auf Finns Diamant-Netz, quasistatisch; keine
    fermionische Quantisierung; Levin/Wen: Fermionen in lokalen bosonischen Modellen nur mit Eichfeld; Rahmung der
    Kanten gibt Fermion nur algebraisch und bei lokal gelesener Rahmungsregel, im Modell spinlos (TWIST-PYRO-1,
    TWIST-SPIN-1) [P].
  - Tabelle 1, Knoten: "ein Drehfeld (Rahmen) je Knoten" [P].
- RUNDE-37/guertel-finn-netz-1/ERGEBNIS.md: vorhanden, ganz gelesen. SO(3)-Einheitsquaternion-Feld je Knoten des
  Diamant-Netzes (Knoten = Tetraedermitten); Bindungsenergie 2(1 - cos omega) je Kante; 6/6 Stoesse legen 420/450 Grad
  stetig in die Gegendrehung ab; SO(2) nicht [P].
- RUNDE-37/takt-umbenennung-l/DOSSIER.md: vorhanden, Abschn. 1 und 2 gelesen. Bahr/Dittrich 2009: Regge-Eichsymmetrie
  (Eckverschiebungen) linear um flach exakt, gekruemmt "quadratically in the curvature" gebrochen; Moderator
  Fehlwinkel je Simplex [P, dort S].
- RUNDE-37/gamma-netz-l/DOSSIER.md: vorhanden, Abschn. 1 und 5.1 gelesen. Skalare Regel = Paar zweiter Klasse
  (Konfigurationshaelfte diskrete Hamilton-Bedingung, Impulshaelfte Eichwahl), von Hand gesetzt [P].
- Keine Datei fehlte.

## 1. Vorwissen zur Quelle [L]

- arXiv 2610.00593 ist nach meinem Trainingsstand (bis Juni 2026) erschienen. Ich kenne die Arbeit nicht. Alles
  Folgende vor dem Abruf ist Erwartung, kein Wissen.
- [L] Verwandte Linien, die ich kenne (nicht hier geprueft):
  - Poincare-Eichgittertheorie / Einstein-Cartan auf Simplizes: Variablen Kantenvektoren (Koframe) plus
    Lorentz-Holonomien je Dualkante; Torsion als Nichtschliessen transportierter Dreiecke (z. B. Drummond 1986,
    Caselle/D'Adda/Magnea 1989, Kaku/Smolin-Gitter; unsicher in Details) [L?].
  - Spinschaum / twisted geometries (Freidel/Speziale 2010): Dreiecke passen in der Form nicht zusammen; manche
    deuten das als Torsion (z. B. "Twisted geometries, twistors and conformal transformations"; "torsion in twisted
    geometries" Haggard/Rovelli/Wieland/Vidotto 2013?) [L?].
  - Yongge Ma (Beijing Normal University) arbeitet zu Schleifenquantengravitation; "Ma" in der Autorenliste koennte er
    sein [L?, nicht geprueft].

## 2. Abrufprotokoll (Erwartung vor dem Abruf, dann Ausgang)

### Abruf 1 (arXiv-API, export.arxiv.org/api/query?id_list=2610.00593)

- Erwartung, geschrieben 2026-10-04 23:16:15 CEST (date), vor dem Abruf:
  - Titel passt ("Dynamics of Regge calculus with torsion"), Autoren Yan, Ding, Ma.
  - Abstract nennt: Kantenvektoren (oder Tetraden je Simplex) und Holonomien bzw. Zusammenhangsvariablen
    (SO(3,1) oder SO(4)) als unabhaengige Variablen; Torsion als Nichtschliessen bzw. Fehlpassung der
    Kantenvektoren nach Paralleltransport; eine diskrete Einstein-Cartan- (oder Holst-)Wirkung; Kontinuumsgrenze
    Einstein-Cartan. "Dynamics" heisst vermutlich Bewegungsgleichungen und/oder kanonische Analyse mit
    Zwangsbedingungen.
  - Spin-1/2-Materie im Abstract: eher nicht (passt zu RT3).
  - Wahrscheinlichkeit, dass mindestens eine dieser Hauptannahmen (Variablen, Kontinuumsgrenze) verletzt wird: ~40 %.
- Ausgang, notiert 2026-10-04 23:17:45 CEST (date); Kopie quellen/A1-arxiv-api-2610.00593.txt:
  - **Weitgehend bestaetigt** (Variablen, Torsion als Fehlpassung, diskrete EC-Wirkung, 3D euklidisch und 4D
    Lorentz) [S Abstract].
  - **Kleine Verstoesse:**
    - V-A1a: vier Autoren (Yan, Ding, Ma, **Cong Zhang**), nicht drei. Folgenlos fuer die Sache.
    - V-A1b: "Dynamics" heisst im Abstract nur: zwei Bewegungsgleichungen aus der Variation nach Kantenvektoren und
      Holonomien. Von kanonischer Analyse, Zwangsbedingungen oder Eichsymmetrien steht **nichts** im Abstract.
    - V-A1c: Kontinuum nur als "consistent with the corresponding equation in the continuum theory" (Kantenvektor-
      Gleichung) und "torsion-free holonomies satisfy the latter equation" (Holonomie-Gleichung). Das ist eine
      Existenzaussage (torsionsfrei loest), **keine Eindeutigkeitsaussage** (nur torsionsfrei loest). Fuer RT2
      entscheidend: Im Kontinuum folgt T = 0 im Vakuum eindeutig [L]; ob das auf dem Netz auch gilt, sagt der
      Abstract nicht.
    - V-A1d: Kantenvektoren sind **je Simplex** vergeben ("In each simplex"); dieselbe Kante hat in zwei Nachbarsimplizes
      zwei Vektoren. Ob deren **Laengen** gleich sein muessen, sagt der Abstract nicht. Wenn nicht, ist die Geometrie
      ueber die Grenzflaeche unstetig (wie "twisted geometries") [ES, offen].
  - Lage der Torsion [S Abstract]: je Paar (Kante auf der Grenzflaeche, Grenzflaeche zwischen zwei Simplizes), als
    Vektor e_sigma(l) - h e_sigma'(l). [ES] Im Kontinuum entspricht das dem Integral der Torsions-2-Form ueber eine
    "gemischte" Flaeche aus Kante l und Dualkante (Weg durch die Grenzflaeche) [ES, zu pruefen am Volltext].

### Abruf 2 (Volltext-PDF, arxiv.org/pdf/2610.00593v1, per curl in quellen/, dann pdftotext)

- Kanal: curl statt WebFetch, damit eine woertliche Kopie mit Gleichungen entsteht (Vorbild TAKT-UMBENENNUNG-L,
  ARBEITSFELD Z. 179: "PDF -> pdftotext"). Zaehlt als Abruf 2 von 3. Selbstanzeige im DOSSIER.
- Erwartung, geschrieben 2026-10-04 23:17:45 CEST (date), vor dem Abruf:
  - E2a: Variablen: Kantenvektoren e_sigma(l) in R^n je Simplex mit Schliessbedingung je Dreieck innerhalb des Simplex
    (Simplex ist im eigenen Rahmen flach); Holonomien h_{sigma sigma'} in SO(3) bzw. SO(3,1) auf Dualkanten.
  - E2b: Torsion T_{sigma sigma'}(l) = e_sigma(l) - h e_sigma'(l). Laengen duerfen sich unterscheiden (60 %), d. h.
    nicht-metrische bzw. "verdrehte" Geometrie.
  - E2c: Wirkung: Summe ueber Gelenke (Dreiecke in 4D, Kanten in 3D) von Bivektor/Kantenvektor mal Log der
    Holonomie um das Gelenk (Barrett-artige erste Ordnung, Palatini/Holst-artig).
  - E2d: Keine kanonische Analyse, keine Klassifikation erster/zweiter Klasse (75 %). Eichsymmetrie hoechstens lokale
    Drehung/Lorentz je Simplex genannt.
  - E2e: Eindeutigkeit der torsionsfreien Loesung im Vakuum nicht bewiesen (60 %); Kontinuumsgrenze nur als formale
    Entsprechung der Gleichungen, keine Konvergenzrechnung (70 %).
  - E2f: Keine Spin-1/2-Materie gebaut (70 %); hoechstens als Ausblick genannt.
  - E2g: Bezug zu twisted geometries / LQG im Text (70 %), weil Ma und Zhang aus der LQG kommen [L?].
- Abruf: curl 2026-10-04 23:18:22 bis 23:18:23 CEST (quellen/A2-abrufzeit.txt), 1 042 363 Byte, PDF 1.7, 18 Seiten;
  Text quellen/A2-2610.00593v1.txt (pdftotext -layout, 1418 Zeilen; Z. = Zeile dort). Ganz gelesen bis Z. 1247,
  Anhang B und Literatur nur ueberflogen.
- Ausgang, notiert 2026-10-04 23:22:37 CEST (date):
  - E2a **eingetroffen**: Kantenvektoren l_p^I(i) je Kante je Simplex, Schliessbedingung je Dreieck (Gl. 2), n^2
    unabhaengige Komponenten je Simplex = konstantes Vielbein (Gl. 6-9); Holonomien h_ij in SO(n) bzw. SO+(1,n-1) je
    orientiertem Uebergang durch eine Grenzflaeche (Gl. 14-16) [S Abschn. II A].
  - **E2b VERLETZT (wichtigster Verstoss):** Die Laengen passen. "Compatibility of the intrinsic geometry of the common
    interface means that the two vectors are related by a local gauge transformation", l_p(j) = Lambda_ij l_p(i)
    (Gl. 13, Z. 216-222); in 4D: "have to be identical up to an SO+(1,3) gauge transformation" (Abschn. V, Z. 784-788).
    Die Geometrie ist also Regge-Geometrie (gleiche Form der gemeinsamen Grenzflaeche), **keine** twisted geometry;
    die twisted geometries werden ausdruecklich abgegrenzt ("reduce to Regge geometries once the shape-matching
    conditions are imposed", Abschn. I, Z. 38-40). Torsion ist damit **nur eine Zusatzdrehung** je Grenzflaeche:
    torsionsfrei heisst h_ij wirkt auf die Kantenvektoren der Grenzflaeche wie Lambda_ij (Gl. 27/28, Z. 304-337;
    "the effect of torsion contributes an additional rotation", Z. 88-90).
    - Korrigierte Erwartung: Torsion je Grenzflaeche = Gruppenelement Lambda_ij^-1 h_ij, also n(n-1)/2 Zahlen
      (3 in 3D, 6 in 4D) [M, ES; im Text nicht so gezaehlt].
  - E2c **eingetroffen, praeziser**: 3D: S = - Summe_B 1/(2 m_B) Summe_i eps_IJK l_B^I(i) (Ln h_B^(i))^JK (Gl. 47),
    gemittelt ueber die m_B Startsimplizes um das Gelenk; 4D: S = Summe_B 1/(2 m_B) Summe_i tr(A_B(i) Ln h_B^(i))
    (Gl. 78), A_B Bivektor des Gelenkdreiecks (Gl. 79). Matrix-Logarithmus statt h (Abgrenzung zu Caselle/D'Adda/
    Magnea [30], Z. 613-620).
  - E2d **eingetroffen**: keine kanonische Analyse; Eichgruppe nur lokal SO(n) bzw. SO+(1,n-1) je Simplex (Gl. 10-12,
    20). Kein Wort zu Eckverschiebungen, Diffeomorphismen, erster/zweiter Klasse (grep: "hamiltonian", "canonical"
    nur als Jordan-Normalform, "first class", "diffeomorph", "translation" ohne Treffer).
  - E2e **eingetroffen**: "Though it is not easy to solve Eq. (112), we check whether the torsion-free holonomy is a
    solution" (Abschn. VI B, Z. 1138-1140); gezeigt nur: torsionsfrei loest Gl. (112) ueber [A_B, h_B] = 0 (Gl. 113)
    und die Bivektor-Schliessung (Gl. 115). Eindeutigkeit nicht gezeigt. Kontinuum: Kantengleichung (87) impliziert das
    kovariante Integral der Tetradengleichung, G^I(W) = 0 bis auf Randterme (Gl. 103); sie ist **schwaecher** als die
    Kontinuumsgleichung (Z. 1039-1043). Keine Konvergenzrechnung, keine Numerik, keine Linearisierung (grep
    "propagat", "lineari", "numeric", "wave", "axial" ohne Treffer). Variation braucht Gelenk-Holonomien nahe 1:
    |eta| < ln 2, |theta| < pi/3 (Gl. 105-107).
  - E2f **eingetroffen**: Materie nicht gebaut. "It is interesting to study the coupling of the present discrete
    gravity with matter fields. In particular, it is interesting to see whether the torsion is determined
    algebraically by the fermions as the case of continuous theory" (Abschn. VII, Z. 1225-1229).
  - E2g **eingetroffen**: LQG-, Spinschaum- und twisted-geometry-Bezug (Abschn. I, Lit. [9]-[18], [32]).
  - Zusatzbefunde (nicht vorhergesagt):
    - Z1: Drei Lager der Literatur, wo Torsion sitzt: konstant im Simplex [24 Drummond 1986], Dirac-delta auf der
      Grenzflaeche [24, 25], Versetzung (Burgers-Vektor) am Gelenk [26 Schmidt/Kohler 2001, 27 Pereira/Vargas 2002]
      (Abschn. I, Z. 79-97). Gewaehlt: Grenzflaeche. Drummonds Schluss "traegt nicht zur Wirkung bei" sei falsch
      (Z. 108-111, mit [29] Gronwald 1995).
    - Z2: Torsionsfluss in kruemmungsfreien Bereichen = Burgers-Vektor (Gl. 23-26).
    - Z3: In 3D sieht die Wirkung nur die Drehung der Gelenk-Holonomie **um die Kante** (eps_IJK l^I (Ln h)^JK
      projiziert den Drehvektor auf l) [M, an Gl. 47]; torsionsfrei ist das genau der Fehlwinkel (Gl. 70, 74, 76).
    - Z4: Die 4D-Rueckfuehrung auf Regge ist im Text nicht ausgefuehrt (Abschn. V enthaelt das Wort "Regge" nicht;
      Abschn. IV ist nur 3D, Gl. 76). Der Abstract sagt "they return" (beide). [ES] Aus Gl. (113) folgt sie leicht;
      nicht von mir nachgerechnet.
    - Z5: Lorentz-Fall: Kantenvektoren duerfen nicht lichtartig sein; zeitartige muessen gleich zeitorientiert sein
      (Abschn. V, Z. 784-794).

### Abruf 3 (arXiv-API-Suche, Gegensweep und Regel 7: Torsion + Regge/simplizial/Spinschaum, neueste zuerst)

- Zweck: (a) die [L]-Liste bekannter Simplex-Arbeiten mit Torsion/Spin pruefen, (b) 24-Monats-Pruefung vor jedem
  "nicht gebaut / nicht belegt" ueber die Arbeit hinaus (Regel 7), (c) ob jemand Spin-1/2 an Regge-Torsion koppelt.
  Messschranken bleiben dafuer [L] ohne Zahlen (Karte: "Zahlen nur mit Quelle").
- Erwartung, geschrieben 2026-10-04 23:23:40 CEST (date), vor dem Abruf:
  - 2610.00593 steht oben.
  - Unter den 30 neuesten Treffern viel Rauschen (Torsion im Sinn von Homologie/Topologie, "simplicial" in Mathematik,
    Festkoerper), etwa 30 bis 50 %.
  - Einschlaegig vor allem Spinschaum/LQG (twisted geometries, Holst/Immirzi, Fermionen im Spinschaum).
  - In den letzten 24 Monaten **keine** Arbeit, die Spin-1/2-Materie an Torsion auf einem Regge- bzw. Simplex-Netz
    koppelt (70 %).
  - Keine Arbeit, die Ausbreitung (Wellen, Linearisierung) von Torsion auf einem Simplex-Netz rechnet (65 %).
- Ausgang, notiert 2026-10-04 23:27:28 CEST (date); Kopie quellen/A3-arxiv-api-suche-torsion-regge.txt:
  - 118 Treffer insgesamt; die 30 neuesten reichen zurueck bis 2021-09.
  - 2610.00593 oben: **eingetroffen**.
  - **Rauschen VERLETZT (staerker):** 26 von 30 sind Torsion im Sinn von Homologie, Gruppen, Topologie oder Algebra,
    erwartet 30 bis 50 %. Einer (2604.22845, Iosifidis) meint Regge-Trajektorien der Hadronphysik.
  - **Kein einziger Spinschaum-Treffer** in den 30 neuesten (seit 2021-09). Nicht vorhergesagt; die Erwartung
    "einschlaegig vor allem Spinschaum/LQG" ist verletzt. Moegliche Ursache Suchdesign (Abstracts nennen "torsion"
    selten) [ES].
  - Spin-1/2 an Torsion auf Simplex-Netz in 24 Monaten: **kein Treffer** (eingetroffen, nach Recherchestand mit
    dieser Abfrage; Regel 7: "nicht belegt", nicht "gibt es nicht").
  - Ausbreitung von Torsion auf Simplex-Netz: kein Treffer, der sie rechnet. **Unerwartet einschlaegig:**
    Christiansen/Hu/Lin 2023 (2312.11709), "Extended Regge complex for linearized Riemann-Cartan geometry": "we
    construct a discrete version of linearized Riemann-Cartan geometry" [S Abstract, sekundaer]. Das ist das
    Werkzeug, mit dem man die Frage RT2 linear stellen koennte; ob sie es tun, sagt der Auszug nicht.
  - Chamseddine/Malaeb/Najem 2024 (2409.04375): diskrete Gravitation, loesen die Spin-Zusammenhangs-Gleichungen aus
    der Torsionsbedingung [S Abstract, sekundaer]. Das ist torsionsfrei gesetzt, nicht Torsion als Freiheitsgrad.
- Budget: 3 von 3 Abrufen verbraucht. Kein weiterer Abruf.

## 3. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

Notiert ab 2026-10-04 23:27:28 CEST (date).

| Nr | Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Der Abstract sagt "they return to the corresponding Regge actions" (3D und 4D); also ist beides gezeigt | **ja, im Text** (grep "Regge", Abschn. IV/V) | **Nur 3D ausgefuehrt** (Gl. 70-76). Abschn. V enthaelt das Wort "Regge" nicht; die 4D-Rueckfuehrung ist behauptet, nicht vorgerechnet. Aus Gl. (113) wohl leicht [ES, nicht nachgerechnet] |
| G2 | Finns Netz ist ein Simplizialkomplex, in dem Tetraeder Flaechen teilen; dann gilt die Arbeit direkt | **ja, Projektdateien** | **Nein.** Finns Netz teilt Ecken, nicht Flaechen: "Im Pyrochlor gehoert jede Kante genau einem Tetraeder" (EINE-WELT-LOCH-1/KARTE.md Z. 11, nach TETRAEDER-L) [P]; Diamant-Knoten = Tetraedermitten, Nachbarn "ueber die geteilten Ecken" (GUERTEL-FINN-NETZ-1/ERGEBNIS.md Z. 20) [P]. Grenzflaechen im Sinn der Arbeit gibt es erst im gefuellten Netz (Stumpf-Tetraeder-Loecher gefuellt); ob das eine volle Triangulierung ist, habe ich nicht geprueft |
| G3 | "Dynamik" heisst Zeitentwicklung | ja (Text) | Nein: kovariante Euler-Lagrange-Gleichungen einer 4D-Wirkung, kein Takt, keine Zeitschritte, keine Hamilton-Form |
| G4 | Die Torsion der Arbeit ist die, an die Dirac-Teilchen koppeln | nur grep | Im Kontinuum koppeln minimal gekoppelte Dirac-Felder nur an den total antisymmetrischen (axialen) Teil der Torsion [L, Hehl u. a. 1976]. Die Arbeit zerlegt die diskrete Torsion nicht in Teile (grep "axial", "irreducib" ohne Treffer). Offen |
| G5 | Die Eichsymmetrien sind vollstaendig behandelt | grep | Nur lokale Drehung/Lorentz je Simplex. Eckverschiebungen (Diffeomorphismen, Bahr/Dittrich) fehlen ganz |
| G6 | Holonomien in SO(n) reichen fuer Spin 1/2 | nicht geprueft (Gedaechtnis) | [L] Spinoren brauchen Uebertragung in Spin(n) (SU(2) bzw. SL(2,C)); SO(n)-Holonomien legen sie nur bis aufs Vorzeichen fest; die konsistente Wahl ist eine Spinstruktur. Die Arbeit arbeitet nur in SO(n) bzw. SO+(1,3) |

- Mindestens einer geprueft: G1 und G2 an Quelle bzw. Projekt, G3 und G5 am Text.

## 4. Eigene Schluesse und Hypothesen (Arbeitsstand, wandern ins DOSSIER)

- ES1: Torsion je Grenzflaeche = Zusatzdrehung Lambda_ij^-1 h_ij in G, n(n-1)/2 Zahlen (3D: 3 je Dreieck). [M, ES]
- ES2: 3D-Wirkung zaehlt nur die Drehung der Gelenk-Holonomie um die Kante; ein "Band mit markierter Seite" um eine
  Kante herumgefuehrt liest also den Fehlwinkel (Kruemmung), nicht Torsion. [M an Gl. 47, 70, 74; ES]
- ES3: Ein Band auf der **Dualkante** (Verbindung zweier Zellen), dessen markierte Seite sich um die Verbindung
  dreht, ist eine der drei Torsionskomponenten je Dreieck (Drehung um die Flaechennormale) [ES]. Die zwei Kippungen
  haben kein Band-Bild.
- ES4: Das SO(3)-Feld aus GUERTEL-FINN-NETZ-1, gelesen als Holonomie h_ij = q_j q_i^-1 auf flacher Geometrie, ist reine
  Torsion ohne Kruemmung (Weitzenboeck-Lage). Seine Bindungsenergie 2(1 - cos omega) ist ein Torsion-zum-Quadrat-Term;
  so einen Term hat die EC-Wirkung nicht. In EC hat diese Lage Wirkung null, und im Kontinuum verbietet die
  Zusammenhangsgleichung sie im Vakuum [L]. [ES, H]
- ES5 (Regel 6): Drei Wege zu "Spin im Netz" im Projekt (Guertel-Trick im Drehfeld, Rahmung der Kanten, Torsion als
  Spindichte-Platz) teilen dieselbe Groesse: die relative Drehung des Zell-Rahmens ueber eine Verbindung. Ob sie eigene
  Energie hat (Cosserat/Poincare-Eich-Regime) oder keine (EC-Regime), entscheidet, ob sie sich ausbreitet. [H]
- Offene Rueckfrage an die Leitung (wandert mit): Gilt Finns Band auf seinen Linien (Primaerkanten) oder auf den
  Verbindungen zwischen Zellen (Dualkanten)? Nur im zweiten Fall gibt es eine direkte Entsprechung (ES3).

## 5. Abschluss

- DOSSIER.md geschrieben ab 2026-10-04 23:29:25 CEST (date); zwei Wortlaut-Korrekturen per sed um 23:31:50 CEST
  ("der Kanten-Kanten-Block"; "Netz aus Tetraedern" in Einfach gesagt).
- Urteile: RT1 teilweise eingetroffen; RT2 aus der Quelle nicht entscheidbar (nach Recherchestand nicht belegt);
  RT3 eingetroffen.
- Groesste Verstoesse: V1 (Form passt, Torsion = reine Zusatzdrehung je Grenzflaeche), V2 (4D-Regge-Rueckfuehrung
  nur behauptet), V3 (keine Eich-/Zwangsanalyse jenseits der Rahmendrehung), V4 (Finns Netz teilt Ecken).
- Offene Rueckfrage an die Leitung (wandert mit): Band auf Linien oder auf Verbindungen zwischen Zellen?
- Kartenvorschlag: TORSION-STEIF-1 (DOSSIER Abschn. 5).
Abschlusszeit: 2026-10-04 23:32:01 CEST
- 23:32: Zeilenangabe Z. 1207-1209 kurz auf 1206 geaendert und zurueckgesetzt (1207 war richtig).
