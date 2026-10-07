# ARBEITSFELD GAMMA-NETZ-L (feldforscher, Runde 43)

- Start: 2026-10-04 19:33:05 CEST (date). Zeitbox 75 min, Ende spaetestens 20:48:05 CEST.
- Karte gelesen: RUNDE-37/gamma-netz-l/KARTE.md (Erwartungen E1-E4 der Leitung, Fragen 1-4).
- Regeln: max. 8 Abrufe, keine Websuche, lokale Kopie je Abruf in quellen/, kein python/awk/perl, Code nur lesen.

## Offene Rueckfragen (wandern mit)

- R1 (an Leitung/Finn): Sitzt die Energie einer Masse in Finns Bild in der Regel je Ecke (Quelle der skalaren Regel)?
  Zaehlt ihre Energie mit dem Takt der Ecke (Multiplikator der Regel)? Davon haengt gamma ab, nicht von einer Rechnung.
- R2 (an Leitung): Die Karte nennt REGGE-ZEIT-1 und REGGE-4D-SCHIEF-1 nicht im Projektstand; beide haben gamma(r) fuer
  eine ruhende Masse im 4D-Regge-Netz schon gerechnet [P]. Absicht oder Luecke?

## Leseprotokoll Projektstand (19:33 bis 19:46)

- SCHREIBTISCH-QBALL-EIS-LAPSE (R35): drei Wege zu h_00; voller Faktor 2 nur mit h_00 und h_ij; Netz-Lichtgeschwindigkeit
  allein = Einstein 1911 = halbe Ablenkung [P].
- EINE-WELT-LOCH-1 ERGEBNIS: 2 masselose TT-Moden auf V und S, 26 (V) gelueckt; Stabilitaet nur auf Zwangsflaeche;
  Spur-Eichdefekt Median 0,91 (L = 16), k -> 0 nicht gerechnet; TT-Tempo anisotrop: [100] 0,11889 / 0,12643 (6,3 %),
  [111] entartet, linear bis 8,5e-8, also langwellig [P].
- **ew.py gelesen (nicht ausgefuehrt), Kernbefund [M, Codelesung]:**
  - Z. 219-228: crow_v = - Summe_{e an v} (Phase) B[e, :]; c = crow^dagger. Also c_v = - B w_v mit w_v = Eck-Skalierung
    (a_e = 1 fuer alle Kanten an v, Bloch-Phase fuer die Nachbarzelle). Das ist exakt, per Konstruktion.
  - Z. 7 und Z. 168: B = l (Summe_t d theta_t/d l) l, also (B a)_e = - l_e delta eps_e. Damit
    c_v^dagger a = Summe_{e an v} l_e delta eps_e (Docstring Z. 7 bestaetigt).
  - Z. 253-259, 315-318: Zwangsflaeche = orthogonales Komplement von Bild [M, c]. Fuer a: M^dagger a = 0 (Eichwahl) und
    c^dagger a = 0 (Regel). Durch die symmetrische Reduktion S^dagger A S gilt dasselbe fuer p: M^dagger p = 0
    (Impulsbedingung, erzeugt die Eckverschiebung) und c^dagger p = 0 (Eichwahl fuer die Regel).
  - Z. 397-401: "Spur-Eichdefekt" = ist A c_v im Bild von M? Das prueft, ob der Fluss der Regel eine Eckverschiebung ist,
    also ob die Regel erster Klasse ist. Median 0,91: auf dem Gitter nicht erster Klasse, schon flach.
  - Kein Lapse, keine Materie, keine Quelle in ew.py.
- Lesart [ES]: Regel = Euler-Lagrange-Gleichung der 3D-Regge-Wirkung fuer Eck-Skalierung = eckweise integrierte
  linearisierte Skalarkruemmung delta R^(3) = 0 = linearisierte Vakuum-Hamilton-Bedingung bei Zeitsymmetrie;
  c^dagger p = 0 ist das Gitter-Gegenstueck von maximalem Slicing (tr pi = 0) [ES, Kontinuumsanalogie].
- Statik [ES, Schreibtisch]: Mit Quelle und Multiplikator mu: B a = - C mu = B W mu, also a = W mu + Eichung (exakt,
  da B auf dem eichfreien Raum bei k != 0 invertierbar ist, Z2 im ERGEBNIS). Raum = Eck-Skalierung durch den
  Multiplikator. Mit GR-Normierung (ein Hamilton H = Summe N_v (- Regge_v/16 pi G + Energie_v)) wird
  delta l/l = -(delta N_1 + delta N_2)/2, also Psi = Phi, gamma = 1, unabhaengig von A, Paarung R1/R2 und der 1/2.
- **Projekt-grep (Ausschluesse gesetzt) fand:**
  - REGGE-ZEIT-1 [P]: 4D-Regge (Kuhn), Masse ueber Eigenzeit an Zeitkanten: gamma -> 1 im Fernfeld, nahe
    gamma - 1 ~ 2,2/r^2 (Achse), Diagonale kinematisch 0,82 bis 0,95. "gamma = 1 im Fernfeld war nach REGGE-4D-1 vorab
    erwartbar."
  - REGGE-4D-SCHIEF-1 [P]: schiefes Netz, gamma(6) = 1,056 / 1,308 / 1,113 je Achse, (gamma - 1) r^2 -> +1,65 / +1,65
    / -1,1; Zusatz ~ exp(-r/2,7) auf A e_y, positiv.
  - TAKT-UMBENENNUNG-L [P]: BPS 2011 gesundes Horava gamma = beta = 1 trotz lambda != 1; projizierbar keine lokale
    Hamilton-Bedingung (Mukohyama 2009); Brans-Dicke gamma != 1 bei voller Symmetrie; "Gemeinsam ist beiden Haelften die
    lokale Hamilton-Bedingung, nicht die 1/2"; Bahr/Dittrich: 4D-Regge flach exakt, gekruemmt gebrochen.
  - GRAVITON-NETZ-L [P]: E1 (Rocek/Williams, Propagator) im Kern [S sekundaer]; Regime A/B/C (Carlip 2012); 2+1:
    Kegel, kein Newton-Grenzfall (Carlip 2005 [S]).
  - STRANG-ANKER-L [P]: Cassini (Will 2014 [S-lokal]); c_T/c - 1 in [-3e-15; 7e-16] [P, LICHT-GLEICH-L];
    gamma = 1/(D - 3) [ES].
- Damit E1 und E2 schon im Projekt beantwortet: kein Abruf dafuer.

## Abrufprotokoll (Erwartung vor Abruf, date-Zeit)

| Nr | Erwartung geschrieben (date) | Ziel | Erwartung |
|---|---|---|---|
| F1 | 19:46:54 | arXiv-API, Suche Glickenstein "conformal variations" | Konforme (Eck-)Variationen stueckweise flacher 3D-Metriken; Ableitung des Regge-/EH-Funktionals danach = Skalarkruemmung je Ecke (Summe l_e eps_e); Linearisierung = diskreter Laplace |
| F2 | 19:46:54 | arXiv-API, Suche Regge + (deflection, bending, post-Newtonian, Newtonian potential) | Wenige Treffer; Hamber/Williams 1995 (Newton-Potential im Quanten-Regge, ~1/r im glatten Bereich); kein gamma fuer Regge berechnet |
| F3 | 19:48:21 | arXiv-API, Suche abs:"Regge calculus" + (Schwarzschild, Newtonian, geodesic, lensing, light) | Brewin/Gentle-Arbeiten zu Regge-Schwarzschild und Konvergenz; Hamber/Williams 1995; keine gamma- oder Ablenkungsrechnung |
| F4 | 19:48:21 | arXiv-API id_list 0911.3401 (Perivolaropoulos, massive Brans-Dicke) | gamma(r) = (3 + 2 omega - e^(-m r))/(3 + 2 omega + e^(-m r)); gamma < 1; -> 1 fuer m r >> 1 (E3 der Karte, Vorzeichen) |
| F5 | 19:48:21 | arXiv-API, Suche emergentes Graviton (Gitter/Qubit/Spinfluessigkeit) + (post-Newtonian, PPN, light bending, universal coupling) | Keine Arbeit berechnet gamma fuer ein Gitter-Graviton; hoechstens allgemeine Kopplungsargumente (E4) |

**Ausgang F1 und F2 (Abrufe 1 bis 3):**
- F1a (19:47:33): http ohne Weiterleitung, Antwort leer (0 Byte). Zaehlt als Abruf 1 (ohne Inhalt).
- F1 (19:47:39, Abruf 2), quellen/F1-api-glickenstein-conformal.xml: Glickenstein 2011, arXiv:0906.1560, J. Differential
  Geom. 87, 201-237: "conformal variation"; "formulas for the derivatives of curvature resemble the formulas for the change
  of scalar curvature under a conformal variation of Riemannian metric"; "variation of certain curvature functionals,
  including Regge's formulation of the Einstein-Hilbert functional (total scalar curvature)" [S Abstract]. Dazu
  Champion/Glickenstein/Young 2010, arXiv:1007.0048: "Yamabe problem", "discrete conformal classes" [S Abstract].
  -> Erwartung im Kern bestaetigt; die Formel Summe l_e eps_e und "Laplace" stehen nicht im Abstract. Eine Zeile, weiter.
- F2 (19:48:00, Abruf 3), quellen/F2-api-regge-ablenkung-newton.xml: 30 Treffer, fast alle Regge-Wheeler (Schwarzes
  Loch) oder Regge-Trajektorien; Suchwort unscharf. Einziger Regge-Kalkuel-Treffer: arXiv:1507.06836 "Discrete geodesics
  and cellular automata": Periheldrehung eines merkurartigen Planeten mit diskreten Geodaeten in vorgegebener
  diskretisierter Raumzeit [S Abstract]. Hamber/Williams nicht gefunden.
  -> Teilweise verletzt (Suchdesign, nicht Welt). Folge: F3 mit Phrase "Regge calculus".

**Ausgang F3 bis F5 (Abrufe 4 bis 6; gelesen vor der Unterbrechung, hier nachgetragen nach den lokalen Kopien):**
- F3 (19:48:42, Abruf 4), quellen/F3-api-regge-calculus-statik.xml, 16 Treffer. Relevant [S Abstract]:
  - Khatsymovsky 2020, arXiv:2008.13756 (Universe 6, 185): Schwarzschild-Problem im Regge-Kalkuel, Finite-Differenzen-
    Form der EH-Wirkung, "at large distances is close to the continuum Schwarzschild geometry", Kruemmung im Zentrum auf
    der Elementarlaenge abgeschnitten. Dazu 2019, arXiv:1912.12626 (IJMPA 35, 2050058).
  - Miller 1995, arXiv:gr-qc/9502044 (CQG 12, 3037): einzelne Regge-Gleichungen konvergieren mit a^2, Mittel ueber lokale
    Gleichungen mit a^3, numerisch a^4.
  - Chakrabarti/Gentle/Kheyfets/Miller 1999, arXiv:gr-qc/9810031 (CQG 16, 2381): Geodaetenabweichung; Kontinuum und
    Simplizes stimmen ueberein, wenn man die Regge-Beitraege ueber ein Flaechenelement summiert; Beziehung Kruemmung zu
    Fehlwinkeln.
  - Arrighi/Dowek 2015, arXiv:1507.06836: Periheldrehung mit diskreten Geodaeten (vorgegebene Raumzeit).
  -> Erwartung im Kern bestaetigt (keine gamma- oder Ablenkungsrechnung gefunden); Brewin nicht unter den Treffern,
     Hamber/Williams wieder nicht. Eine Zeile, weiter.
- F4 (19:48:46, Abruf 5), quellen/F4-api-0911.3401.xml: Perivolaropoulos 2010, PRD 81, 047501: Schranken fuer omega "for
  any field mass"; "for omega = O(1) the solar system constraints relax for a field mass m >~ 20 x m_AU = 20 x 1e-27 GeV"
  [S Abstract]. Die Formel gamma(r) steht nicht im Abstract.
  -> Yukawa-Abschwaechung im Kern bestaetigt; Formel und Vorzeichen nicht pruefbar am Abstract. Ersatz ohne Abruf: Will
     Z. 1905: 1/(2 + omega_BD) = 2 alpha_0^2/(1 + alpha_0^2) [S-lokal]. Masseloser gesunder Skalar: gamma < 1.
- F5 (19:48:51, Abruf 6), quellen/F5-api-emergent-graviton-ppn.xml: 2 Treffer, beide ohne gamma: Sexty/Wetterich 2012,
  arXiv:1208.2168 (2D-Sigma-Modell mit Gitter-Diffeomorphismen, Metrik als Ordnungsparameter); Zufallsnetze 2106.08911.
  -> E4 im Kern bestaetigt, nach Recherchestand (eine API-Suche) keine gamma-Rechnung fuer Gitter-Gravitonen. Eine Zeile.

## Unterbrechung

- Letzte gemessene Zeit vor dem Abbruch: 19:51:49 CEST (date, Ausgabe des Will-grep). Laut Leitung Abbruch gegen 19:53
  durch ein Sitzungslimit, Limit seit 21:20 zurueckgesetzt.
- Wiederaufnahme 2026-10-04 21:35:52 CEST (date).
- Verbraucht vor der Unterbrechung (streng, mit 19:53:00 gerechnet): 19 min 55 s. Rest: 55 min 05 s. Neues Ende
  spaetestens 22:30:57 CEST.
- Abrufe verbraucht: 6 von 8 (F1a leer, F1 bis F5). Erwartungen standen fuer F1 bis F5 vor dem jeweiligen Abruf.

## Abrufprotokoll nach der Wiederaufnahme

| Nr | Erwartung geschrieben (date) | Ziel | Erwartung |
|---|---|---|---|
| F6 | 21:36:28 | arXiv-API id_list hep-th/9406163 (Hamber/Williams, Newton-Potential im Quanten-Regge) [L, ID aus dem Gedaechtnis] | Statisches Potential zweier schwerer Massen aus Korrelationen von Geodaeten- bzw. Wilson-Linien; anziehend; im glatten Bereich mit Newton ~1/r vertraeglich; nichts zu gamma oder Lichtablenkung |
| F7 | 21:37:53 | arXiv-API Suche au:Hamber + (running, Newton's constant) + (static, isotropic, post-Newtonian) | Kovariante nichtlokale Feldgleichungen mit laufendem G(Box); statische isotrope Loesung mit G(r), Korrekturen ~ (r/xi)^(1/nu); keine vDVZ-Aussage, kein gamma |

**Ausgang F6 (21:36:52, Abruf 7), quellen/F6-api-hep-th-9406163.xml: ERWARTUNG VERLETZT.**
- Hamber/Williams 1995, Nucl. Phys. B435, 361-398 [S Abstract]: Wilson-Linien der schweren Teilchen; "the continuum analog
  of this quantity reproduces the Newtonian potential in the weak field expansion"; im glatten AdS-artigen Bereich, "the
  only phase where a sensible lattice continuum limit can be constructed", gilt: "non-linear graviton interactions give
  rise to a potential which is Yukawa-like, with a mass parameter that decreases towards the critical point where the
  average curvature vanishes."
- Korrigierte Erwartung: Im fluktuierenden (Quanten-)Regge-Netz ist das statische Potential nicht 1/r, sondern
  Yukawa-artig; langreichweitig nur am kritischen Punkt. Linear-klassisch (ew.py, REGGE-ZEIT-1, Khatsymovsky) gibt es
  diese Abschirmung nicht.
- Voller Zyklus:
  - Regel 1, zwei Regime [ES]: (I) klassisch-linear: masselose TT, 1/r, gamma -> 1. (II) fluktuierend: Yukawa, Masse
    -> 0 nur am kritischen Punkt. Moderator: Abstand zum kritischen Punkt (Kopplung G gegen G_c; bei Finns Netz die
    Fluktuationsstaerke, z. B. Temperatur wie bei FLUSS-1), messbar als Korrelationslaenge xi gegen a und r.
  - Unterscheidungspunkt [ES]: r ~ xi (exponentieller Abfall). Fuer gamma bei r << xi: Ist die Masse Fierz-Pauli-artig
    (linear, ohne Eichinvarianz), gaebe vDVZ 3/4 der Ablenkung, also gamma = 1/2 [P: GEGENLESEN-R35 B7, RUNDE-22
    dunkel-zeit nach Hinterbichler 2012]; ist sie ein laufendes G bei erhaltener Kovarianz, bliebe gamma = 1 [L?].
    Cassini (gamma = 1 auf 2e-5) trennt beides.
  - Abgrenzung zum Schreibtisch der Leitung: Dort sind Yukawa-Anteile Zusaetze von Gittermoden auf Gitterreichweite
    neben dem masselosen 1/r (harmlos). Bei Hamber/Williams ersetzt Yukawa das 1/r (gefaehrlich).
  - Folge: F7 (letzter Abruf) prueft, ob Hamber/Williams die Abschirmung kovariant deuten.

**Ausgang F7 (21:38:14, Abruf 8 von 8), quellen/F7-api-hamber-running-g.xml:** Hamber/Williams 2007, PRD 75, 084014,
arXiv:hep-th/0607228: Korrekturen zur statischen isotropen Loesung aus nichtperturbativen Effekten; "slow rise of the
effective gravitational coupling with distance"; Skala "related to the observed effective cosmological constant";
"covariant non-local effective field equations ... examined in the case of the static isotropic metric" [S Abstract].
-> Erwartung im Kern bestaetigt (kovariant, laufendes G); gamma steht nicht im Abstract. Eine Zeile. Abrufe erschoepft.

## Zwischenergebnisse (21:41:22)

- **gamma-Formel im Hamilton-Regime [ES, Schreibtisch, Vorzeichen gegen das Kontinuum geprueft, nicht am Gitter]:**
  H = - kappa_g S_Regge + Summe_v mu_v (- kappa' c_v^dagger a + m_v) + ...; statisch: kappa_g B a = kappa' C mu, mit
  C = - B W folgt a = -(kappa'/kappa_g) W mu + Eichung. Testmasse (1 + mu) m, also Phi = mu; delta l/l =
  -(kappa'/kappa_g)(mu_1 + mu_2) = - Psi. Ergebnis gamma = 2 kappa'/kappa_g.
  - Ein Hamilton mit eckgewichteter Regge-Energie (S_N = Summe_e N_e l_e eps_e, N_e = Mittel der Eck-Lapses) gibt
    kappa' = kappa_g/2, also gamma = 1. Vorzeichen: W^dagger B W negativ definit (Inertie, [P]-Zaehlung 10 negative
    Richtungen = 10 Ecken), also mu < 0 nahe der Masse: Uhren langsamer, Anziehung.
  - Unabhaengig von A, Paarung R1/R2, Fuellung V/S und der 1/2. Abhaengig nur vom Verhaeltnis kappa'/kappa_g (Regel 6:
    Kopplungsgroesse statt Bauteil).
- Kontinuumsprobe [M]: delta G_ij[2 phi delta] = -(d_i d_j - delta_ij Lap) phi (d = 3); statisch delta G_ij[h + 2 Phi
  delta] = 0, also h = -2 Phi delta, Psi = Phi.
- Dimension [ES]: Konforme Ableitung von Int sqrt(h) R ist (d - 2) sqrt(h) R; gamma_D = 1/(D - 3) = 1/(d - 2). In d = 2
  ist die Regge-Wirkung Summe eps_v = 2 pi chi konstant, B = 0: Regel = Fehlwinkel an der Ecke, kein Lapse-Gefaelle,
  kein Newton, Licht am Kegel abgelenkt; E - 3V = 0 auf dem Torus.
- Marolf (GEMEINSAMES-NETZ-L [P]): universelle nichtlineare Kopplung verlangt eichredundante Kantenlaengen; in ew.py ist
  die Regel zweiter Klasse -> Spannung, betrifft gamma linear nicht [ES].

## Gegensweep (21:41:22)

- G1 "gamma ist der bindende Anker" -> GEPRUEFT an nachtrag-69/kinetik.json (jq): TT-Tempo omega^2/k^2 langwellig in
  allen 5 ausgelesenen Paarungen anisotrop: A1-R1 0,11889 bis 0,12643 (6,3 %), A1-R2 0,12325 bis 0,12714 (3,2 %),
  A2-R1 0,14807 bis 0,15684 (5,9 %), A3-R1 0,0052083 bis 0,0057584 (10,6 %), A3-R2 0,0050477 bis 0,0052083 (3,2 %)
  [P, Quotienten von Hand]. Licht als Vektorfeld ist bei kubischer Symmetrie langwellig isotrop (Rang 2) [M]. c_T-Anker
  1e-15 [P]. -> Bindend ist die Spin-2-Ausbreitung, nicht gamma.
- G2 "Cassini misst die Ablenkung" -> GEPRUEFT an Will 2014 lokal Z. 2358-2364: Doppler/Laufzeit (Shapiro), naechster
  Abstand 1,6 R_sun; Ablenkung und Laufzeit haengen beide an (1 + gamma)/2 (Z. 2172, 2354).
- G3 "Licht sieht Kantenlaenge und Takt" -> nicht pruefbar (kein Licht in ew.py); offen.
- G4 "Vorzeichen/Normierung meiner Ableitung" -> nur Kontinuumsprobe; Gitter offen (Rechenkarte).
- G5 "Phasen von c passen zu W" -> [P] cM_null <= 4,0e-15 ist die notwendige Folge c^dagger M = - W^dagger B M = 0.

## Zwischenergebnisse (alt)

(siehe oben)

## Abschluss (21:47:17)

- DOSSIER.md geschrieben ab 21:42:58 CEST; Gegenlese-Durchgang durch mich: drei Stellen berichtigt (Schwanzbereich
  -1,1 bis +2,2 statt "+1,65 bis +2,2"; Vorzeichen der Poisson-Gleichung (-W^dagger B W) mu = -(kappa_g/kappa'^2) m;
  "Tabellenkopf" -> ERGEBNIS-Tabelle Abschn. 5; Gitterweite einheitlich "unter einigen 1e3 km"); Tabellen auf
  Spaltenzahl geprueft.
- Abrufe 8 von 8. Rueckfragen R1, R2 und offene Fragen O1 bis O5 stehen im DOSSIER Abschn. 10.
- Kein frischer Gegenleser (nicht im Auftrag); Empfehlung an die Leitung: Abschn. 5.2 (Schreibtischformel) fremd lesen
  lassen, bevor sie in Texte geht.

## Gestrichenes

(nichts)
