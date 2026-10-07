# SPIN-ZUFALLSNETZ-1: Plan (Runde 39, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Arbeitsplatz RUNDE-37/spin-zufallsnetz-1/.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 09:31:54 CEST. Code ab 09:44 CEST.
  - Erste Codefassung auf der .69 07:47:02 UTC (sha256 75d4eb57...); Rauchlaeufe ab 07:47:04 UTC (Abschnitt 9).
  - Plantext ab 09:51:43 CEST.
- **Kennzeichen:** [M] eigene Mathematik, [E] gerechnet (hier nur Rauchlauf), [F] Festlegung dieses Plans (nicht auf der
  Karte), [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen (laut Dossier), [H] Hypothese.
- Alles ist synthetische Netzrechnung. Keine Messdaten, keine Messdatenbestaetigung.

## 1. Vorhersagen der Karte (unveraendert uebernommen)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SZ0 | Kontrolle: Auf dem kubischen Gitter gibt dieselbe naive Konstruktion 8 Weyl-Punkte (Doppler) mit rho(E) ~ E^2 und dem Achtfachen der Kontinuums-Zustandsdichte | 85 % |
| SZ1 | [H] Auf dem Zufallsnetz folgt die Zustandsdichte nahe E = 0 dem Kontinuum eines einzelnen Weyl-Kegels (rho(E) ~ E^2/(2 pi^2 v^3) mit v aus der Gewichtung) innerhalb eines Faktors 1,5, ohne Achtfach-Ueberschuss | 35 % |
| SZ2 | [H] Langwellige Eigenzustaende haben definierte Helizitaet: Anteil der richtigen Helizitaet >= 0,9 im untersten Energiefenster | 45 % |
| SZ3 | Die Unordnung erzeugt eine endliche Zustandsdichte bei E = 0 (rho(0) > 0, Unordnungs-Weyl-Uebergang) | 50 % |

Die Bedeutungssaetze der Karte gelten unveraendert.

## 2. Netz

- N Poisson-Punkte mit Dichte 1 im Torus [0, L)^3, L = N^(1/3). Zufall: numpy default_rng([39, N, saat]).
- **Periodische Delaunay-Triangulierung** (scipy.spatial.Delaunay, Qhull) der Punktkopien in einem Saum s = 4 um den
  Grundwuerfel. Behalten wird je Torus-Tetraeder das Bild, dessen Schwerpunkt in [0, L)^3 liegt.
- **Pruefungen (je Netz, im Ergebnis berichtet):**
  - Umkugel jedes behaltenen Tetraeders liegt im erweiterten Wuerfel [-s, L + s]^3. Dann ist das Tetraeder auch
    gegen alle periodischen Bilder leer.
  - Euler-Charakteristik V - E + F - T = 0 (3-Torus); jedes Dreieck in genau zwei Tetraedern; Summe der
    Tetraedervolumen = L^3; jede Kante mit eindeutigem Bildversatz s_ij; alle N Knoten benutzt.
- **Voronoi-Facette je Delaunay-Kante** [M]:
  - Fuer jedes Tetraeder um die Kante (a, b) das vorzeichenbehaftete Viereck (Kantenmitte, Umkreismittelpunkt des
    Dreiecks abc, Umkreismittelpunkt des Tetraeders, Umkreismittelpunkt des Dreiecks abd); Vorzeichen aus der
    Orientierung det[b - a, c - a, d - a].
  - Die Summe ueber die Tetraeder ist die Facettenflaeche A_ij. Das gilt auch, wenn Umkreismittelpunkte ausserhalb
    liegen; die eingefuegten Dreiecks-Umkreismittelpunkte liegen auf den Voronoi-Kanten.
- **Zellvolumen** V_i = sum_j A_ij d_ij / 6 (Pyramiden; der Erzeuger liegt in seiner Zelle, die Facette im Abstand
  d/2).
- **Facettensummen als Pruefung:** Abschluss sum_j A_ij n_ij = 0 je Knoten (relativ zu sum_j A_ij); sum_i V_i = L^3;
  A_ij > 0.

## 3. Operator und Gewichte

- **Form** (Karte und Dossier Abschn. 8, keine Abweichung):
  - Block H0_ij = (i/2) A_ij (sigma . n_ij) exp(i theta . s_ij), H0_ji = H0_ij^dagger.
  - H = V^(-1/2) H0 V^(-1/2), gleichwertig zum Problem H0 phi = E V phi mit Massenmatrix V.
  - n_ij ist der Einheitsvektor von i zum Bild von j, theta eine Verdrillung (Bloch-Phase je Torusumlauf), sonst 0.
- **Begruendung der Gewichte [M]:**
  - Langwellig gilt H0 e^(ik.x) u ~ -e^(ik.x_i) (sigma . M_i k) u mit M_i = sum_j A_ij (d_ij/2) n_ij n_ij^T. Das
    nullte Glied faellt wegen des Abschlusses weg.
  - Spur M_i = sum_j A_ij d_ij/2 = 3 V_i exakt (Pyramiden). Damit ist Spur(M_i/V_i) = 3 an jedem Knoten.
  - Divergenzsatz: V_i 1 = sum_f A_f (c_f - x_i) n_f^T (c_f Facettenschwerpunkt). Der tangentiale Teil von
    c_f - x_i ist fuer beide Zellen einer Facette gleich, n_f wechselt das Vorzeichen. Deshalb gilt
    **sum_i M_i = L^3 * 1 exakt**: Das volumengewichtete Mittel des Geschwindigkeitstensors ist genau isotrop, v = 1.
    Erst im Rauchlauf als Zahl gesehen (Abweichung 1e-15); die Herleitung habe ich danach gemacht.
  - Lokal schwankt der spurfreie Teil ("zufaelliges Vierbein"), rms der Eigenwerte von M_i/V_i - 1 etwa 0,25.
  - A/d mit sigma . d_ij waere dasselbe. Ohne V waere v lokal proportional zu V_i. Die Massenmatrix gibt v = 1 ohne
    freie Konstante.
- **Vorzeichen:** H ~ -sigma . k. Zu E > 0 gehoert sigma . k^ = -1. Das ist in diesem Code die "richtige Helizitaet".
  -H waere die andere Chiralitaet mit gespiegeltem Spektrum; die Zaehlungen in |E| aendern sich dadurch nicht.
- **Vorab ableitbar [M]:**
  - D1: H ist hermitesch.
  - D2: Bei theta = 0 gibt es zwei exakte Nullmoden V^(1/2) u.
  - D5 (nicht auf der Karte): T = i sigma_y K kommutiert mit H, T^2 = -1. Bei theta = 0 ist daher jedes Niveau
    zweifach (Kramers).
  - D6: Spur H^3 = 0 exakt. Die drei Kantenrichtungen eines Dreiecks liegen in einer Ebene, also
    n_ij . (n_jk x n_ki) = 0. Erst im Rauchlauf gesehen, dann hergeleitet.
  - Keine E -> -E-Symmetrie: Das Netz ist nicht bipartit. Das kubische Gitter hat die Untergitter-Symmetrie.
- **Verdrillung theta:**
  - Gemittelt ueber zufaellige theta verschwinden die Schalenstufen des endlichen Torus. Die Kegelzaehlung wird dann
    glatt: Erwartung n(eps) = eps^3/(3 pi^2) je Knoten und Kegel.
  - Eine feste kleine Verdrillung THETA_EIG = (0,05; 0,08; 0,11) hebt die Kramers-Entartung fuer Eigenpaare und
    Spektralfunktionen auf.

## 4. Kontrolle SZ0 (kubisches Gitter)

- Dieselbe Funktion matrix() mit A = d = V = 1 und 6 Nachbarn. Damit gilt H(k) = -sum_a sigma_a sin k_a [M].
- Das gibt 8 Weyl-Punkte bei k in {0, pi}^3, je 4 jeder Chiralitaet. Bei geradem L und theta = 0 sind das 16 exakte
  Nullmoden.
- Verdrillungsgemittelt gilt n_s(eps) = 8 (1 + 0,3 eps^2 + ...) [M]. Das sind 8,10 bei 0,20 und 8,38 bei 0,40.

## 5. Verfahren

- **(a) KPM-Zustandsdichte, verdrillungsgemittelt:**
  - Jackson-Kern, M = 1024 Momente. Je Probe ein zufaelliges theta in [0, 2 pi)^3 und B Zufallsphasenvektoren.
  - Skalierung a = 1,05 max|E| + 0,02 (ARPACK, theta = 0), hoechstens die Gershgorin-Schranke.
  - Waechter: |mu_n| <= 1 + 1e-6, sonst ist der Lauf ungueltig.
  - n(eps) = Zustaende je Knoten mit |E| < eps, aus der exakt integrierten Chebyshev-Reihe.
  - n_s(eps) = n(eps) 3 pi^2/eps^3. Das ist die Zahl der Kegel mit v = 1 (Karte: "v aus der Gewichtung").
  - Standardfehler aus der Streuung der Proben.
- **(b) Spektralfunktion ebener Wellen (KPM, M = 2048, ein Vektor je Welle, ohne Stichprobe):**
  - chi_{k,h} = sqrt(V_i/sum V) e^(ik.x_i) u_h(k^), h Eigenwert von sigma . k^, k = (2 pi m + theta)/L.
  - N = 10^4: alle m != 0 mit |k| <= 0,5 (Schalen |m| = 1 und sqrt 2, 18 Wellen x 2 Helizitaeten).
  - N = 10^5: Auswahl m = (1,0,0), (2,0,0), (3,0,0), (1,1,0), (2,2,0), (1,1,1), (2,2,2).
  - Daraus: Gewicht im Fenster 0 < E <= 0,35 bzw. -0,35 <= E < 0, Spitzenlage (v_Spitze = |E_Spitze|/|k|), <H>, <H^2>.
- **(c) Eigenpaare nahe null (beschreibend und als Gegenprobe):**
  - Shift-Invert-ARPACK um sigma = 0 bei THETA_EIG, k = 150, Rayleigh-Ritz, Residuen.
  - Vollstaendigkeitsprobe per Inertia (LDL^H ohne Pivot, sigma = +-0,35), nur gueltig bei perm_r = perm_c.
  - Ebene-Wellen-Gehalt (m != 0, |k| <= 0,75) und Helizitaet je Zustand.
- **(d) Code-Kontrollen** (Modus kontrolle, auch im Hauptlauf wiederholt):
  - kubisch L = 6 und 7 dicht gegen analytisch, Nullmodenzahl
  - Zufallsnetz N = 1000 dicht: Kramers, Nullmoden, ARPACK gegen dicht, Inertia gegen dicht, KPM gegen dicht je theta
  - kubisch L = 12: KPM gegen analytisch je theta

## 6. Saaten, Laeufe, Rechenort

- **Zufallsnetze:**
  - N = 10^4, Saaten 1-4: KPM (a) mit 4 theta x 2 Vektoren, Spektralfunktionen (b) mit M = 2048.
  - N = 10^5, Saaten 1-2: KPM (a) mit 4 theta x 2 Vektoren; Spektralfunktionen (b, Auswahl) mit M = 1024 nur bei Saat 1
    (Laufzeit, Abschnitt 9).
  - Rueckfall, vorab festgelegt: Reicht die Zeitbox nicht fuer Saat 2 bei N = 10^5, urteilen SZ1 und SZ3 auf Saat 1
    allein (Vermerk).
  - Eigenpaare (c) bei N = 10^4 entfallen (Rauchlauf R2: ARPACK nach 6,5 min nicht fertig). Die Eigenzustands-Ebene
    deckt die Kontrolle K4 ab: dicht, N = 2000, Saat 998, alle Eigenpaare, F aus Eigenvektoren gegen F aus KPM
    (Fenster 0,6, weil bei N = 2000 die erste Kegelschale bei 0,50 liegt), IPR und Ebene-Wellen-Gehalt je Energie.
- **Kubisch:** L = 46 (N = 97336) mit KPM 4 x 4 und Spektralfunktionen (Auswahl, M = 2048); L = 22 mit KPM 4 x 2 und
  Spektralfunktionen (alle Wellen |k| <= 0,5, M = 2048).
- **Saaten:** Rauch 101-103, Kontrolle 998 und 999. Hauptlauf-Saaten vorher nie benutzt.
- **Laeufe** (je ein Starteraufruf, Ordner /home/fmh/fmhc-physics-remote/runde39-spin-zufall/):
  - M1 `kontrolle lauf/kontrolle.json`
  - M2 `gitter 46 lauf/gitter46.json kpm=1024,4,4 spek=2048,0.5`
  - M3 `gitter 22 lauf/gitter22.json kpm=1024,4,2 spek=2048,0.5`
  - M4 `netz 10000 1 2 lauf/netz1e4-a.json kpm=1024,4,2 spek=2048,0.5`
  - M5 `netz 10000 3 2 lauf/netz1e4-b.json kpm=1024,4,2 spek=2048,0.5`
  - M6 `netz 100000 1 1 lauf/netz1e5-1.json kpm=1024,4,2 spek=1024,0.5`
  - M7 `netz 100000 2 1 lauf/netz1e5-2.json kpm=1024,4,2` (ohne Spektralteil: Laufzeit, R4 zeigte rund 100 s je
    KPM-Block bei N = 10^5; der Spektralteil bei N = 10^5 ist beschreibend)
  - M8 `auswertung.py lauf`
- **Rechenort:** nur ueber kleintest.sh auf cpu5 und p4000b, hoechstens zwei zugleich, je Lauf <= 600 s, 1 Thread.

## 7. Urteilsregeln (mechanisch in code/auswertung.py)

- **SZ0 [F: Fenster, Toleranz, Teil (iii)]:**
  - Eingetroffen, wenn alle drei Teile gelten:
    - (i) Bei L = 46 liegt n_s(eps) (Mittel der Proben) fuer alle eps in {0,20; 0,25; 0,30; 0,35; 0,40} in
      [7,5; 8,5]. Die Toleranz 8 +- 0,5 stammt aus dem Dossier.
    - (ii) Bei geradem L und theta = 0 gibt es genau 16 Nullmoden (dicht, L = 6), also 8 Weyl-Punkte.
    - (iii) Code-Probe: KPM gegen analytisch je theta, max |Delta n| <= 0,01 je Knoten (L = 46).
  - Nicht eingetroffen, wenn (iii) gilt, aber (i) oder (ii) nicht.
  - Nicht auswertbar, wenn (iii) scheitert oder der Waechter anschlaegt.
- **SZ1:**
  - Messgroesse: n_s(eps) aus (a) bei N = 10^5, Mittel ueber alle Proben beider Saaten, v = 1.
  - Eingetroffen, wenn n_s(eps) fuer alle fuenf eps in [2/3; 1,5] liegt [F: Fenster]. Sonst nicht eingetroffen.
  - Nicht auswertbar bei Waechter- oder Geometriefehler.
  - Gegenprobe: dieselbe Regel bei N = 10^4. Wird berichtet; weicht ihr Urteil ab, kommt ein Vermerk.
- **SZ2:**
  - Messgroesse F_W = sum richtig / sum (richtig + falsch), ueber alle Wellen aus (b) bei N = 10^4, Saaten 1-4 gepoolt,
    und alle Zustaende mit 0 < |E| <= 0,35.
  - "Richtig" ist das Gewicht bei E > 0 fuer h = -1 und bei E < 0 fuer h = +1.
  - [M] Das ist genau der mit dem Ebene-Wellen-Gehalt gewichtete Anteil der richtigen Helizitaet aller
    Eigenzustaende im Fenster, denn sum_{n in W} |<chi_{k,h}|n>|^2 = <chi_{k,h}|P_W|chi_{k,h}>.
  - "Unterstes Energiefenster" = 0 < |E| <= 0,35 [F]. Die Zahl stand vor dem ersten Rauchlauf im Code
    (E_FENSTER). Grund: Bei N = 10^4 liegt die erste Kegelschale (2 pi/L = 0,29) innerhalb, die zweite (0,41)
    ausserhalb.
  - Eingetroffen, wenn F_W >= 0,9; sonst nicht eingetroffen.
  - Nicht auswertbar, wenn das mittlere Fenstergewicht je Welle < 0,05 ist (kein langwelliger Gehalt im Fenster) oder
    der Waechter anschlaegt.
- **SZ3:**
  - Messgroesse rho0 = n(0,05)/(2 x 0,05) aus (a) bei N = 10^5, in Zustaenden je Knoten und Energie.
  - Kegelerwartung im selben Fenster: rho_K = 0,05^2/(6 pi^2) = 4,2e-5.
  - Eingetroffen, wenn drei Bedingungen gelten [F]:
    - rho0 >= 3 rho_K
    - rho0 - rho_K >= 3 SE
    - rho0 bei N = 10^4 liegt im Faktor 2 bei rho0(N = 10^5) (Gegenprobe mit N, also kein Endlichkeitseffekt)
  - Nicht eingetroffen, wenn rho0 < 3 rho_K oder rho0 - rho_K < 3 SE.
  - Sonst nicht auswertbar.
  - Beschreibend, nicht geurteilt: Fit rho(E) = rho0 + c E^2 auf E in [0,05; 0,30].
- Die Urteile nach Kartenwortlaut stehen in ERGEBNIS.md neben den Plan-Urteilen.

## 8. Kartenwortlaut, Lesarten, Kartenfehler (vor dem Einfrieren)

- **K1 (Lesart SZ3):**
  - "rho(0) > 0" ist numerisch nur mit einer Nachweisgrenze entscheidbar. [L?] Seltene Gebiete geben bei jeder
    Unordnung ein exponentiell kleines rho(0) (Nandkishore/Huse/Sondhi 2014, aus dem Gedaechtnis).
  - Die Regel in Abschnitt 7 verlangt deshalb ein deutlich messbares rho0. Ein Urteil nach Wortlaut kann nur gleich
    oder "nicht entscheidbar" sein.
- **K2 (Ergaenzung, kein Fehler):** "Zwei exakte Nullmoden (k = 0)" gilt bei theta = 0. Zusaetzlich ist bei theta = 0
  jedes Niveau doppelt (Kramers, D5).
- **K3 (SZ0):** Das "Achtfache" gilt fuer eps -> 0. Die Gitterkorrektur betraegt +0,3 eps^2, im Fenster <= 5 %, und
  liegt innerhalb der Toleranz. Keine Berichtigung.
- **K4 (SZ1, "v aus der Gewichtung"):**
  - v = 1 gilt exakt im volumengewichteten Mittel (Abschnitt 3). Eine renormierte v_eff aendert n_s um 1/v_eff^3.
  - Das bleibt nach Karte im Urteil. v_eff aus den Spektralspitzen berichte ich getrennt und urteile darueber nicht.
- **K5 ("Isotropie" im Testteil der Karte, ohne Vorhersage):** v_Spitze je Richtungsklasse (Achse, Flaechen-, Raumdiagonale),
  beschreibend.
- **Kartenfehler:** keiner gefunden. Plan-Urteil und Wortlaut-Urteil koennen sich nur durch die [F]-Festlegungen
  unterscheiden.

## 9. Rauchlaeufe (offengelegt; Schwellen danach nicht geaendert)

- **R1 kontrolle** (cpu5, 07:47:04 bis 07:47:48 UTC, Codefassung 75d4eb57):
  - K1 kubisch dicht gegen analytisch <= 2,0e-14; L = 6 bei theta = 0: 16 Nullmoden, L = 7: 2.
  - K2 Zufallsnetz N = 1000 (Saat 999):
    - Euler 0, jedes Dreieck zweimal, Abschluss 6,9e-16, Volumensumme exakt.
    - Kramers 2,5e-14, genau 2 Nullmoden, Spektrum [-2,42; 2,40], Spur H^3 = 0 (1e-16).
    - ARPACK gegen dicht 2,5e-15.
    - **Inertia und dicht: 328 von 2000 Zustaenden mit |E| < 0,35.**
    - KPM gegen dicht max 0,033 je Knoten.
  - K3 kubisch L = 12: KPM gegen analytisch 0,022 je Knoten.
  - **Gesehen:** n(0,2) = 0,186 je Knoten. Das sind rund 690 Kegel-Einheiten. Die Zustandsdichte ist um E = 0 flach,
    etwa 0,47 je Knoten und Energie. Damit waren SZ1 (nicht eingetroffen) und SZ3 (eingetroffen) vor dem Hauptlauf
    absehbar.
- **R2 netz N = 10^4** (Saat 101, eig = 150; p4000b, 07:47:06 UTC):
  - ARPACK mit Shift-Invert war nach 6,5 min nicht fertig (Speicherspitze 1,5 GB). Um 07:53:34 UTC habe ich die
    eigene Unit gestoppt.
  - Folge: Eigenpaare bei N = 10^4 entfallen. Bei der flachen Dichte haetten 150 Paare ohnehin nur |E| < 0,02 erreicht.
- **R3 netz N = 10^4** (Saat 102; cpu5, 07:50:41 bis 07:52:14 UTC):
  - KPM 2 x 2: n(0,05) = 0,046, n(0,2) = 0,184, n(0,4) = 0,365 je Knoten.
  - Spektralfunktionen (38 Wellen, M = 2048, 82,5 s): F_W = 0,9907, mittleres G_richtig = 0,994, v_Spitze-Median 0,984.
  - Damit war auch SZ2 (eingetroffen) absehbar.
  - **Reihenfolge:** PLAN.md ist zuerst um 09:52:44 CEST geschrieben worden (mtime), mit den Regeln von Abschnitt 7.
    Die R3-Zeile stand seit 09:52:14 im Log. Gelesen habe ich sie um 09:52:47.
- **R4 netz N = 10^5** (Saat 103, KPM 1 x 4, Spektral M = 2048; p4000b ab 07:55:33 UTC): Netz 17,4 s, Euler 0,
  Abschluss 1,4e-14. KPM 1 x 4 mit Schranke: 96,7 s. Der Spektralteil mit M = 2048 lief beim Einfrieren noch.
  Erwartet ist, dass er an die 600-s-Grenze stoesst; deshalb gilt bei N = 10^5 M = 1024 und nur Saat 1.
- **R5 kontrolle mit K4** (cpu5, Lock ab etwa 07:57 UTC, Ende 08:01:01 UTC, Codefassung 460c0af6):
  - K1 bis K3 wie R1.
  - K4 (N = 2000, Saat 998, dicht, 191 s): F aus Eigenvektoren 0,9841 gegen KPM 0,9841 (Fenster 0,6); Gehalt im
    Fenster 14,351 gegen 14,365.
  - IPR x N: Median aller Zustaende 1,73, der 20 tiefsten 1,75. Deren Ebene-Wellen-Gehalt ist hoechstens 9,8e-4.
  - Damit sind A5 und A6 schon im Rauchlauf eingetroffen und A7 nicht. Gelesen habe ich das um 10:01 CEST, nach
    dem Schreiben von Abschnitt 10. M1 wiederholt K4 deterministisch mit derselben Saat.
- **Was vor und was nach R1 festgelegt wurde:**
  - Vor R1 im Code (sha256 75d4eb57, 07:47:02 UTC): E_FENSTER = 0,35, EPS_GITTER = 0,20 bis 0,40, EPS0 = 0,05,
    THETA_EIG, K_MAX.
  - Von der Karte: das SZ1-Band [2/3; 1,5]. Aus dem Dossier: die SZ0-Toleranz 8 +- 0,5.
  - Nach R1, vor dem Lesen von R3: die SZ3-Regel (3 rho_K, 3 SE, Faktor 2) und der Weg ueber Spektralprojektionen fuer
    SZ2. Der Grund war die flache Dichte; eine Schwelle wurde dafuer nicht veraendert.
  - Nach R2: Eigenpaare durch K4 ersetzt. Nach R4 (Netzzeit): Spektral-M bei N = 10^5 auf 1024 gesenkt. Das ist eine
    Laufzeitwahl, keine Schwelle.
- **Folge:** Der Hauptlauf ist im Wesentlichen eine Bestaetigung mit frischen Saaten, groesserem N und vollen
  Kontrollen. Ich zeige das in ERGEBNIS.md als Selbstanzeige an.

## 10. Agenten-Vorhersagen (nach R1 und R3, vor dem Hauptlauf; nicht unabhaengig, siehe Abschnitt 9)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | SZ0 eingetroffen, n_s im Fenster zwischen 8,0 und 8,45 | 95 % |
| A2 | SZ1 nicht eingetroffen, n_s(0,2) > 300 bei N = 10^5 | 95 % |
| A3 | SZ3 eingetroffen, rho0 in [0,35; 0,55] je Knoten und Energie bei N = 10^4 und 10^5 | 85 % |
| A4 | SZ2 eingetroffen, F_W >= 0,97 | 80 % |
| A5 | K4: abs(F_eigen - F_kpm) <= 0,02 | 75 % |
| A6 | K4: die 20 Zustaende naechst E = 0 haben je einen Ebene-Wellen-Gehalt (abs(k) <= 0,75) < 0,01 | 80 % |
| A7 | K4: IPR x N der 20 tiefsten Zustaende >= 3 x Median aller Zustaende (naher Null staerker lokalisiert) | 50 % |
| A8 | N = 10^5: v_Spitze fuer alle 7 Richtungen in [0,95; 1,00], Spanne <= 0,03 | 60 % |
| A9 | N = 10^5: rho(E) und rho(-E) weichen fuer abs(E) <= 0,5 irgendwo um mehr als 5 % ab | 40 % |
