# ARBEITSFELD EW-BAELLE (Runde 20, Literatur-Agent)

- Start: 2026-10-02 17:18:32 CEST (date). Zeitbox 60 min, also bis etwa 18:18.
- Karte gelesen: KARTE.md (Fragen 1-5, E1-E5 der Leitung, Bedeutung). Erwartungen der Leitung bleiben unveraendert.
- Marken: [S] gelesen (Primaerquelle), [L?] nur Abstract/Zitat, [H] eigene Schlussfolgerung.
- Regel: vor jedem Abruf eine Zeile Erwartung (EA-n), danach Ausgang (bestaetigt / VERSTOSS).

## Erwartungsprotokoll je Abruf

- EA-1 (vor Abruf arxiv.org/abs/2609.19293): Vier Autoren (Herdeiro, Kunz, Kleihaus, Radu), v1 vom 29.09.2026,
  Abstract wie im Scout; Kommentarzeile mit Seitenzahl.
  - Ausgang (17:19): KLEINER VERSTOSS. v1 vom 16.09.2026 18:03 UTC, v2 vom 29.09.2026 10:10 UTC ("references added").
    Die Karte nennt 29.09. als Einreichung, das ist v2. 27 Seiten, 5 Abbildungen, hep-th + gr-qc.
    Neu: ZWEI Familien, kugelsymmetrisch "elektrisch" und axialsymmetrisch "magnetisch". Gelesen wird v2.
- EA-2 (vor Lesen PDF v2, Seiten 1-10; PDF lokal: quelle/arXiv-2609.19293v2.pdf, geladen 17:20:10):
  Lagrangedichte WS bosonisch, Ansatz mit W ~ e^{-i w t}, Higgs-Betrag h(r), A_0/Z_0; Randbedingungen;
  Frequenzintervall bis M_W; keine lineare Stabilitaetsanalyse.
  - Ausgang (17:24, Seiten 1-21 gelesen, Text zusaetzlich per pdftotext nach quelle/arXiv-2609.19293v2.txt fuer grep):
    bestaetigt: harmonische Zeitabhaengigkeit, phi(r), A_0/a_0 statisch, Intervall w_min < w <= M_W, keine
    Stabilitaetsanalyse (nur Ausblick S.21). VERSTOESSE (voll analysiert, s. Abschnitt "Verstoesse"):
    - VS-a: Higgs kaum abgesenkt. e-Beispiel (Abb. 3) phi im Kern etwa 0.8, Minimum etwa 0.77 bei endlichem Radius;
      m-Beispiel (Abb. 2) Minimum etwa 0.96. Text S.18: phi knotenfrei, phi(0) != 0 "for all solutions obtained so far".
      Kein Beutel, das Wort "bag" kommt nicht vor. Meine V1 sagte nichts dazu, die Leitung erwartete >= 30 % (E1).
    - VS-b: Das SM-Hindernis ist beta (M_H/M_W), nicht th_W (S.19): th_W laesst sich bei grossem w und kleinem beta
      annaehern, beim SM-Wert beta^2 = 0.3029 bisher keine Loesung. Meine V4 (Coulomb, g') war FALSCH.
    - VS-c: Alle gezeigten Familien haben leichtes Higgs: beta 0.0632 bis 0.152, also M_H < M_W [H, aus
      beta^2 = (M_H/M_W)^2/8], und liegen nah an der Schwelle (w/M_W >= 0.94 in Abb. 4).
    - VS-d: Energiedichte der e-Kugel ist hohl-schalenfoermig: T_tt im Zentrum etwa halb so gross wie das Maximum
      bei endlichem Radius (Abb. 3, Einschub); phi mit lokalem Minimum bei endlichem Radius; V mit einem Knoten.
    - VS-e: Gauss/Kopplung q aendert die Loesungen im gPH-Modell nur quantitativ (S.6, Abb. 1). Damit ist die
      Gauss-Bedingung als "Hauptunterschied" (E5) unwahrscheinlich.
- EA-3 (vor Abruf hochaufgeloeste Seite 18, Abb. 3): phi(0) zwischen 0.78 und 0.82, Minimum knapp darunter.
  - Ausgang (17:26): bestaetigt. Ablesung Abb. 3 (220 dpi, quelle/seite18-18.png): phi(0) etwa 0.80, Minimum etwa
    0.77 bei log10 r etwa 1.1; V(0) etwa 0.11, H-Maximum etwa 0.15, A_0(0) etwa -0.08, a_0(0) etwa -0.04;
    T_tt(0) etwa 0.0012, Maximum etwa 0.0022 bei log10 r etwa 1.1. Ablesung, keine Rechnung.
- EA-4 (vor Abruf Ref. [19], arXiv:2301.04172, Proca-Higgs-Baelle, JCAP 05 (2023) 022): reeller Skalar im Kern
  abgesenkt, aber nicht null; Intervall w_min < w < mu, Massenluecke, Rueckkehr/zwei Aeste; keine Stoerungsanalyse;
  vermutlich ein Hinweis auf Friedberg-Lee-Sirlin als skalares Vorbild.
  - Ausgang (17:27, PDF v1 geladen 17:26:16, Text quelle/ref19-arXiv-2301.04172.txt): teils bestaetigt, VERSTOSS:
    - bestaetigt [S]: Abstract und Abschn. 2.1 (S.5-6, Gl. (10)): PH-Modell ist "vector version of the scalar
      Friedberg-Lee-Sirlin model"; FLS-Lagrangedichte Gl. (10) mit Kopplung (1/2) phi^2 psi psi* und KEINER
      expliziten Masse des komplexen Feldes. Abschn. 2.2, Gl. (14)-(17): Higgs ausintegriert gibt anziehende
      quartische Proca-Selbstwechselwirkung -(A Abar)^2/M_rho^2.
    - VERSTOSS VS-f [S] Abschn. 3.2 S.11-12, Abb. 1: ungeeichte PH-Baelle haben M -> unendlich fuer w -> 1 (= mu),
      die M(w)-Kurve SCHNEIDET SICH SELBST (fuer alle gerechneten lambda), mindestens drei Aeste gezeigt, eine
      minimale Frequenz konnten die Autoren "so far" nicht bestimmen; "inside the spiral" (S.10, Zeile 518).
      Dagegen EW-Baelle (2609.19293 S.18, Abb. 4): zwei Aeste, M und Q bleiben bei w -> M_W ENDLICH.
      Also: der Uebergang ungeeicht -> EW aendert die globale Aststruktur (Spirale -> zwei Aeste mit endlichem Ende).
    - S.12 [S]: Obergrenze in lambda (bei w = 0.95), oberhalb keine Loesungen; grosses lambda -> freie Proca-Theorie,
      die keine flachen Solitone hat.
    - Fussnote 5 [S]: Grundzustand = Zeitkomponente f(r) mit einem Knoten.
- EA-5 (vor Ansicht Ref. [19] Abb. 2 links, Einschub, w = 0.80, lambda = 0.005): phi(0) deutlich abgesenkt,
  etwa 0.2 bis 0.5 (kleines lambda macht das Absenken billig).
  - Ausgang (17:28): VERSTOSS VS-g. Ablesung Ref. [19] Abb. 2 links, Einschub (200 dpi, quelle/ref19-seite-13.png):
    phi(0) etwa 0.74, Minimum etwa 0.63 bei r etwa 4, bei r = 10 etwa 0.86. Auch beim ungeeichten PH-Ball mit sehr
    kleinem lambda kein Beutel; Absenkung 25-40 %, Minimum schalenfoermig bei endlichem Radius.
    Ladungsdichte j^t ist im Zentrum NULL, Maximum bei r etwa 4 (Ladung sitzt in einer Schale); -T^t_t mit flachem
    Maximum bei r etwa 2.5. Loesung auf dem ersten Ast, M = 48.26, Q = 51.45 (Bildunterschrift).
    Skalierung Ref. [19] Gl. (32)-(34): Vektormasse 1, Skalarmasse^2 = 2 lambda [H aus Gl. (34)]. Abb. 2 rechts:
    bei w = 0.95 enden die Loesungen bei lambda etwa 0.57 (Ablesung), also Skalar/Vektor-Massenverhaeltnis bis etwa
    1.07 [H, Kopfrechnung sqrt(2*0.57)]. M2 (Verhaeltnis 1) laege beim ungeeichten PH-Modell knapp INNERHALB.
- EA-6 (vor Ansicht hochaufgeloeste Seiten 17 und 19, Abb. 2 und 4 der EW-Arbeit): w_min/M_W der e-Familien
  zwischen 0.94 und 0.98, steigt mit beta; zweiter Ast endet bei w = M_W mit grosser Masse.
  - Ausgang (17:31): im Kern bestaetigt, Randwerte leicht daneben. Ablesung Abb. 4 (240 dpi, quelle/seite19-19.png):
    e, tan th_W = 0.04: w_min/M_W etwa 0.935 (beta 0.0894), 0.975 (0.1096), 0.988 (0.1183).
    m, tan th_W = 0.01: w_min/M_W etwa 0.944 (beta 0.1096), 0.982 (0.1342), 0.998 (0.1523).
    Beide Aeste erreichen in der Abbildung die Linie w = M_W mit endlicher Masse: unterer Ast e etwa 20-45 M_0,
    oberer Ast e etwa 340 (beta 0.1183) bzw. 700 (beta 0.1096) M_0, beta 0.0894 laeuft oben aus dem Bild.
    Der untere Ast hat kurz vor w = M_W einen kleinen Haken nach oben (Massenminimum knapp unter M_W, passt zu S.18).
    Abb. 2 (m, 200 dpi): phi(0) etwa 0.996, Minimum etwa 0.962 bei th = pi/2, r etwa 40. Bestaetigt.
    [H] w_min rueckt mit wachsendem beta rasch an M_W heran; die Familien enden vermutlich knapp ueber dem
    groessten gezeigten beta (Extrapolation aus drei Punkten, nicht belegt).
- Ref. [59] im Text (S.22 Fn. 3): dos Santos Costa Filho, Gervalle, "Bosonic stars with dark electroweak fields",
  arXiv:2609.19273 (gleichzeitig, gravitierend, kugelsymmetrisch). Noch nicht abgerufen.
- EA-7 (vor Websuche, Regel 7 und Gegensweep): Zu "electroweak balls" gibt es ausser 2609.19293 und [59] nichts
  (zu neu); keine Stabilitaets- oder Modenanalyse; zu Proca-Higgs-Baellen hoechstens [20] (spinning, 2024),
  keine Arbeit zu gebundenen Zustaenden im Kontinuum.
  - Ausgang (17:31): NICHT DURCHFUEHRBAR. WebSearch meldet "200 of 200" Suchen der Sitzung verbraucht; Hinweis, keine
    weiteren Suchen abzusetzen. Ich umgehe das nicht ueber Suchseiten per WebFetch.
    Folge fuer den Bericht: Jede Fehlanzeige zur Literatur lautet "nach Recherchestand (2609.19293, Ref. [19],
    Abstract [59]) nicht belegt", nie "gibt es nicht" oder "widerlegt" (Regel 7 nicht erfuellbar, offen vermerkt).
- EA-8 (vor Abruf arxiv.org/abs/2609.19273, Ref. [59], nur Abstract, zweite zitierte Arbeit): gravitierende
  kugelsymmetrische Einstein-WS-Loesungen mit harmonischem W-Kondensat in einem verborgenen Sektor; keine lineare
  Stabilitaetsanalyse.
  - Ausgang (Abruf zwischen 17:31:08 und 17:33:45): teils bestaetigt, VERSTOSS VS-h [L?, nur Abstract]:
    v1 16.09.2026 (derselbe Tag wie v1 der EW-Arbeit), 37 S. Abstract: regulaer, kugelsymmetrisch, "static condensate
    of the massive W and Z bosons"; Newton-Konstante UND elektroschwache Massenverhaeltnisse auf physikalischen
    Werten gehalten, als dunkler EW-Sektor gedeutet. Stabilitaet/Moden/Abstrahlung/Higgs im Inneren im Abstract nicht
    erwaehnt. Verstoss: Mit Gravitation gibt es offenbar Loesungen bei physikalischen Massenverhaeltnissen, die flache
    EW-Arbeit findet dort keine. [H] Das spricht dafuer, dass das beta-Hindernis eine Eigenschaft der flachen Familien
    ist, nicht des Feldinhalts. Nicht weiter geprueft (Rahmen: hoechstens drei zitierte Arbeiten, nur Abstract).

## Gegensweep (17:34): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 "e" heisst "elektrisch geladen". GEPRUEFT: falsch gelesen waere es. "e/m" ist die Proca-Multipolklasse
  (S.5-6, nach [41]); auch die m-Loesungen tragen elektrische Ladung (S.14: "the solitons carry a non-vanishing
  electric charge"). Fuer Frage 5 zaehlt nur: e ist kugelsymmetrisch.
- G2 w ist eine physikalische Frequenz. GEPRUEFT: nein, Gl. (22) verschiebt w in die Potentiale; w ist durch
  A_0, a_0 -> 0 im Unendlichen festgelegt. "Oberes Ende = M_W" gilt in dieser Eichung; Kanalschwellen |w +- Om| > M_W
  ebenso.
- G3 l ist fuer Stoerungen der e-Loesung ein guter Index (keine Isospin-Verdrehung wie beim Sphaleron).
  GEPRUEFT an Gl. (20)-(21): nur dt und dr, feste tau-Richtungen, Funktionen nur von r. Invariant unter gewoehnlichen
  Drehungen [H aus S]. Damit ist "l = 0" im ueblichen Sinn definiert.
- G4 Das Photon ist auch im Inneren masselos. GEPRUEFT an Gl. (16): Massenterme enthalten nur W und die Kombination
  g'a - gV^3 (Z-Richtung); die Photonkombination aus Gl. (13) kommt im Massenterm nicht vor [H aus S]. Gilt, solange
  phi != 0 (unitaere Eichung); phi ist knotenfrei (S.18).
- G5 Die SM-Huerde ist der Mischungswinkel (Coulomb). GEPRUEFT: nein, beta (S.19).
- G6 v2 = v1 bis auf Referenzen. NICHT geprueft (nur Kommentarzeile "references added").
- G7 Transversale Vektormoden beginnen bei l = 1. Nur indirekt geprueft: S.6 (m hat kein Kugelgegenstueck, beginnt
  bei l = 1; e-Ansatz allgemein drei Potentiale, l = 0 nur zwei). Lehrbuchaussage selbst in dieser Karte ohne
  Quelle [H].
- G8 Die 24-Monats-Suche (Regel 7) ist gelaufen. NEIN, Budget erschoepft (EA-7).

## Eigene Vorannahmen vor dem Lesen (nicht die der Leitung, nur fuer meine Verstoesse)

- V1: W-Kondensat mit harmonischer Zeitabhaengigkeit e^{-i w t}, Kugelansatz wie bei Proca-Sternen (W_0(r), W_r(r)),
  Higgs-Betrag h(r), dazu A_0 und Z_0 als statische Begleitfelder.
- V2: Frequenzintervall w_min < w < M_W, M(w) mit Spitze (cusp) bei w_min, zwei Aeste.
- V3: Keine Stoerungsanalyse, hoechstens Q-gegen-Masse-Kriterium.
- V4: Bei SM-Kopplungen keine Loesung wegen Coulomb-Abstossung (g' != 0) oder wegen M_H/M_W.

## Fundstellen (Rohnotizen)

Achtung Notation: In der Arbeit ist psi der REELLE Skalar (Proca-Higgs-Teil, Abschn. 2). Unser psi (komplex) entspricht
dort dem komplexen Vektor A bzw. W. Im ERGEBNIS immer "psi_M2" gegen "psi_HKKR" trennen.

Seiten 1-7 (gelesen 17:21-17:23):
- S.1 Abstract [S]: "smooth, finite-energy solitons", e-Typ kugelsymmetrisch, m-Typ axialsymmetrisch; endliches
  Frequenzintervall, Massenluecke, zwei Aeste; "electroweak counterparts of Proca-Higgs balls"; keine Loesungen bei
  gemessenen SM-Kopplungen und Massenverhaeltnissen "for the families studied here".
- S.3 Fussnote 1 [S]: Ponton, Bai, Jain [40]: elektroschwach-symmetrische Dunkelmaterie-Baelle mit Higgs-Erwartungswert
  im Inneren etwa null; laut Autoren eine andere Klasse (brauchen Zusatzskalar).
- S.3 Fussnote 2 [S]: bisherige Proca-Higgs-Modelle laut Autoren alle ungeeicht.
- Abschn. 2.1, Gl. (1) [S]: gPH-Modell: Maxwellfeld X, reeller Skalar psi_HKKR, geeichter komplexer Vektor A,
  Massenterm (kappa/2) psi^2 A Abar; U(psi) = lambda/4 (psi^2 - v^2)^2; Vakuum psi = v, Vektormasse mu = v sqrt(kappa).
  Ausdruecklich KEIN Eich-Higgs-Mechanismus (psi neutral).
- Gl. (3) [S]: Lorenz-artige Bedingung folgt dynamisch aus den Feldgleichungen (keine Eichwahl).
- Abschn. 2.2, S.5-6 [S]: Einteilung nach Multipolzahl l (Ref. [41], axialsymmetrische Proca-Sterne): e-Familie enthaelt
  die kugelsymmetrischen Proca-Sterne als l = 0-Glied; m-Familie hat KEIN Kugelgegenstueck, beginnt bei l = 1.
- Gl. (5) [S]: e-Ansatz A = e^{-i w t}[i V(r) dt + H(r) dr]; Gl. (6): X = A_0(r) dt, psi(r). Vier ODEs im e-Sektor.
- S.6 [S]: Restliche U(1)-Eichfreiheit: elektrisches Potential verschwindet im Unendlichen. Numerik mit v = 1.
- S.6 [S]: gPH-Solitone nicht als infinitesimale Vakuumstoerung; nur in 0 < w_min < w <= mu; endliche Massenluecke;
  Existenzgebiet in Kopplungen beschraenkt (nicht fuer beliebig grosse lambda und/oder q).
- Abb. 1 [S]: e-Loesungen, kappa = 1/4, lambda = 0.08, v = 1, w = 0.495 (mu = 0.5); Energiedichte und V(r) fuer
  wachsendes q (bis 0.08). Higgs-Profil psi(r) in Abb. 1 NICHT gezeigt.
- Abschn. 3, Gl. (7) [S]: S_WS mit SU(2)-Potentialen V^a, U(1)-Potential a, Doublet Phi, Potential
  lambda (Phi^dagger Phi - v^2/2)^2; Vorfaktor -1/(4 pi).

Seiten 8-14 (gelesen 17:24-17:27):
- Gl. (12) [S]: M_W = g v/2, M_Z = (1/2) sqrt(g^2+g'^2) v, M_H = v sqrt(2 lambda). tan th_W = g'/g, e = g sin th_W.
- Gl. (13) [S]: Z = cos th V^3 - sin th a; A~ = sin th V^3 + cos th a (masselos), "in a gauge in which the Higgs
  field tends asymptotically to the vacuum".
- Gl. (14)-(16) [S]: unitaere Eichung Phi = (0, phi)/sqrt2, phi reell; W = V^1 + i V^2, D = nabla + i g V^3.
  Massenterm (1/8) g^2 W Wbar phi^2 -> W-Masse^2 proportional phi^2 (verschwindet bei phi = 0).
  Zusatz (1/8)(g' a - g V^3)^2 phi^2 (Z-Masse ebenfalls ~ phi), Potential lambda/4 (phi^2 - v^2)^2.
- Gl. (18) [S]: Identifikation mit gPH: W = A, phi = psi_HKKR, V^3 = X, kappa = g^2/4, q = g. Ausdruecklich KEINE
  konsistente Abschneidung (Hyperladungsfeld a, nichtabelscher Anteil von W^3, Higgs-Kopplung an g'a - gV^3).
- Abschn. 4.1, Gl. (20) [S] e-Ansatz: V_mu dx^mu = H(r)(cos wt tau1 + sin wt tau2)/g dr
  + [V(r)(sin wt tau1 - cos wt tau2)/g + A_0(r) tau3/g] dt; Gl. (21): a = (1/g') a_0(r) dt, Phi = phi(r) v/sqrt2 (0,1).
  Also: geladenes W hat NUR dt- und dr-Komponenten (wie Proca-Stern l = 0), keine Winkelkomponenten.
- Gl. (19) [S] m-Ansatz: S(r,th)(sin wt tau1 + cos wt tau2)/g dphi + A_0(r,th) tau3/g dt; kein Kugelgegenstueck.
- S.10 [S]: Vakuum A_0 = a_0 = 0, phi = 1; e: H = V = 0.
- Gl. (22) [S]: Resteichfreiheit A_0 -> A_0 + Om, a_0 -> a_0 + Om, w -> w - Om. Festlegung A_0, a_0 -> 0 im Unendlichen,
  damit w Q-Ball-artig die Familie beschriftet. => w ist eichabhaengig definiert (Festlegung im Unendlichen).
- Gl. (23) [S]: r = rbar/(g v), A_0 = g v Abar_0, a_0 = g v abar_0, w = g v wbar. Drei dimensionslose Parameter:
  g'/g = tan th_W (SM 0.54880), beta^2 = lambda/g^2 = (1/8)(M_H/M_W)^2 (SM 0.3029), und w mit "bound-state condition"
  w <= M_W. In diesen Einheiten M_W = 1/2 [H, aus (12) und (23)].
- S.12 [S]: Finite Differenzen [44], Fehler < 1e-3; e-Loesungen zusaetzlich mit Kollokation [45,46], Fehler ~1e-10.
- Abschn. 4.2 S.12 [S]: geladenes Vektorfeld faellt mit sqrt(M_W^2 - w^2) ab.
- m-Sektor Gl. (24)-(28), Asymptotik Gl. (31) [S]: S ~ exp(-r sqrt(M_W^2-w^2)) sin^2 th; A_0 und a_0 je Yukawa-Anteil
  exp(-M_Z r)/r plus gemeinsames Q/r; phi = 1 + c2 exp(-M_H r)/r. S.14: "the solitons carry a non-vanishing electric
  charge" (gemeinsames Q/r = masseloses EM-Feld). Gl. (32): physikalische Ladung = Q/e.
- ~~Gl. (33)-(34) [S]: Virialidentitaet nur fuer m-Loesungen (Deser [47]).~~ GESTRICHEN 17:35: falsch, S.16 Gl. (45)
  gibt die Virialidentitaet auch fuer e. Richtig: Gl. (33)-(34) fuer m, Gl. (45) fuer e; laut S.16 nur Genauigkeitstest,
  "does not help to understand heuristically the existence".

Seiten 15-22 (gelesen 17:24-17:26, Abbildungen nachgelesen 17:26-17:31):
- Gl. (36)-(38) [S], e-Sektor: L_YM = -(1/2g^2)[(A_0' - H V)^2 + (V' + (w + A_0) H)^2]; L_M = -(1/2g'^2) a_0'^2;
  L_H = (v^2/2)[phi'^2 - (1/4) phi^2 ((a_0 - A_0)^2 + V^2 - H^2) + (1/2) lambda v^2 (1 - phi^2)^2].
  [H] Das Higgs-Potential im Kern ist (lambda v^4/4)(1 - phi^2)^2; bei phi = 0 waere das die Beutelenergiedichte.
- Gl. (39) [S]: algebraische Gleichung fuer H. Gl. (40): ODEs fuer V, A_0, a_0, phi. Gl. (41): Zwangsbedingung,
  folgt differentiell aus (39), (40); Konsistenzpruefung.
- Gl. (42)-(43) [S]: Regularitaet am Ursprung, freie Konstanten phi_0, v_0, A_00, a_00; H(r) ~ r.
- Gl. (44) [S]: phi = 1 + z0 exp(-M_H r)/r; H, V ~ exp(-sqrt(M_W^2 - w^2) r); A_0 = Q/r + c2 exp(-M_Z r)/r;
  a_0 = Q/r - c2 (g'^2/g^2) exp(-M_Z r)/r. S.16: Coulomb-Schwanz ist der einzige langreichweitige Anteil.
- S.16 [S] Randbedingungen e: r = 0: H = V' = A_0' = a_0' = phi' = 0; r -> inf: H = V = A_0 = a_0 = 0, phi = 1.
- S.17-18 [S]: m-Energiedichte ueberwiegend torusfoermig, T_tt(0) klein, aber nicht null. e: V hat einen radialen
  Knoten (von den Proca-Stern-Saaten [6] geerbt); Higgs knotenfrei, phi(0) != 0, evtl. lokales Minimum bei endlichem r.
- Gl. (46) S.18 [S]: w_min < w <= M_W, w_min > 0. w -> M_W verbindet NICHT mit dem Vakuum; M und Q bleiben endlich
  (Massen- und Ladungsluecke). M(w) und Q(w) mit Minimum zwischen w_min und M_W; bei w_min Umkehr auf zweiten Ast;
  zwei Loesungen gleicher Frequenz mit verschiedener Masse, Ladung, Profil. Vergleich mit geeichten Q-Baellen [48-51].
- S.19 [S]: zwei Aeste in beiden Sektoren fuer alle betrachteten (th_W, beta); diese legen w_min und damit das
  Existenzgebiet fest. Keine Loesung bei gleichzeitig gemessenem g'/g und lambda/g^2; th_W erreichbar bei grossem w
  und kleinem beta; bei beta^2 = 0.3029 bisher keine Loesung. "should not be interpreted as a general non-existence
  result": echtes Ende, Grenze der numerischen Fortsetzung oder (S.21) eingeschraenkter Ansatz.
- S.21 [S]: Ausblick: hoehere Multipole, radial oder winkelmaessig angeregte Loesungen, rotierende Loesungen;
  statische l = 1-e-Loesungen und rotierende Loesungen bereits gefunden (noch unveroeffentlicht). "A systematic study
  of linear stability and non-linear dynamics is equally important" (Zitat gekuerzt). Schwarzschild-Hintergrund:
  Vorab-Suche findet Loesungen, aber nicht bei gemessenen Kopplungen.
- S.22 Fn. 3 [S]: gleichzeitige Arbeit [59] zu gravitierenden kugelsymmetrischen Einstein-WS-Loesungen.
- S.20 Abb. 5 [S]: nur kuenstlerische Darstellung.
- Volltextsuche (pdftotext + grep, 17:24): "photon", "Gauss", "bag", "Friedberg", "breath", "quasinormal",
  "oscillat" kommen nicht vor; "radiat" nur in "superradiant" (S.2, S.22) und einem Literaturtitel (Korrektur
  17:40, vorher stand "ausser Literaturtitel"); "stabil" nur im Ausblick und in Literaturtiteln.
- Ref. [19] S.5 [S] (Zeile 190-191 im Text): phi = 0 ist konsistente Abschneidung, "complex (massless) vector",
  "Einstein-(double)Maxwell theory". Grundlage fuer [H] "l = 0-Vektorkondensat kann keinen phi = 0-Kern fuellen".

## Abschluss

- ERGEBNIS.md geschrieben ab 17:37:23 (date), danach Gegenlesen vorwaerts: sechs Korrekturen (m-Beispiel Minimum statt
  Kern; q-Aussage gilt fuer gPH; "radiat"/superradiant; Moderator-Satz als [H]; Fensterbreite; Zitatwortlaut Ref. [19]).
- Gegenlesen rueckwaerts (17:42, tac): fuenf weitere Korrekturen (zwei "Gl. (17)" getrennt; phi-Spanne praezisiert;
  "Coulomb deckelt Ladung" als Vorwissen markiert; Einfach-gesagt-Satz als unsere Ueberlegung markiert; Frage-5-Punkt
  auf lineare Ordnung und Eichung von Gl. (22) eingeschraenkt).
- Ende der Arbeit: 2026-10-02 17:43:11 CEST (date), also etwa 25 min von 60. Kein git, kein Peerbus, keine Rechnung.
- Lokale Quellkopien in quelle/ (PDF 4,3 MB und 1,1 MB, Texte, vier PNG-Seiten); nur Lesekopien.

- Nachtrag zu Zeile "Ref. [59] ... Noch nicht abgerufen": inzwischen Abstract abgerufen (EA-8).
- Nachtrag zu V2: Spitze (cusp) in M(w) bei w_min war falsch gedacht. Die Arbeit hat bei w_min einen Umkehrpunkt;
  das Massenminimum liegt zwischen w_min und M_W (S.18).

## Gestrichen

- Virialidentitaet "nur m" (s. oben, 17:35).

## Offene Rueckfragen

- R1 an die Leitung: Was bezeichnet "unser E1/E2" in Frage 5 der Karte? Ohne Projektdateien nicht klaerbar; ich
  vergleiche mit der M2-Kanalstruktur aus dem Auftrag.
- R2 an die Leitung: "Kanalmassen 1 und sqrt 2" (Frage 4). Meine Lesart: psi_M2-Masse im Kern (chi = 0) ist 1,
  Vakuummassen von psi_M2 und chi sind sqrt 2. Bitte bestaetigen.
