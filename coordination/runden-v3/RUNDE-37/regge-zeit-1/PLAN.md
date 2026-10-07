# REGGE-ZEIT-1: Plan (Code-Agent, Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 03:02:55 CEST (date). Plantext ab 03:38:02 CEST (date).
- Grundlage: KARTE.md. Vorhersagen Z0 bis Z3 und ihre Schwellen sind unveraendert uebernommen. Was die Karte offen
  laesst, ist als [F] festgelegt.
- Kennzeichen: [S] an der Quelle gelesen, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [M] eigene Mathematik,
  [F] Festlegung dieses Plans, [H] Hypothese.
- **Vor diesem Plan gesehen** (offengelegt):
  - Rauchlauf 0 (.69, 01:15:18 bis 01:15:26 UTC, Spur cpu, rc = 0), nur Struktur, keine Quelle, keine Loesung.
  - **Befund:** Die Hyperdiagonale (die fuenfte Nullmode aus REGGE-4D-1) aendert die Fehlwinkel. Es gilt
    norm(E(k) e_top) = 5,47 (k = 0) bzw. 5,45 bis 5,47 (vier statische k); die Norm von E(k) ist 22,8.
  - Bei k = 0 ist abs(d eps/d s_top) = 1 an allen Achse-Achse-Dreiecken, darunter die (tau,x)- und (y,z)-Typen.
    1/sqrt 2 gilt an Achse-Flaeche-Dreiecken, 1 an Flaeche-Flaeche-Dreiecken, 0 an Dreiecken mit Raumdiagonale.
  - Dagegen sind A(k) e_top = 0 exakt und M(k) e_top = 6e-12 (Nullmode der Wirkung). Die Eichmoden aendern die
    Fehlwinkel nicht (4,7e-13 relativ).
  - **Folge:** Die Fehlwinkel einzelner Dreiecke sind in der linearen Kuhn-Regge-Loesung nicht festgelegt. Der Hinweis
    "die Diagonalmode darf sie nicht aendern" ist fuer rohe Fehlwinkel falsch. Abschnitt 3 legt deshalb vor jeder
    Rechnung mit Quelle eine Fixierung fest.

## 1. Gitter, Zeitachse, Statik [M]

- 4D-Kuhn-Gitter wie REGGE-4D-1 (code/regge4d.py, unveraendert importiert, sha256 2708f33b... wie die eingefrorene
  Fassung): 15 Kanten, 50 Dreiecke, 24 Simplizes je Ecke; Variablen s = l^2; Weg T (Torus L = 4, Richardson) fuer
  d eps/d s.
- **Zeit tau = Achse 0** [F]. Alle Achsen sind unter S4 gleichwertig. x, y, z sind die Achsen 1, 2, 3.
- **Statisch:** k_tau = 0. Das 4D-Problem wird je raeumlichem k = 2 pi n/L auf dem Torus L^3 geloest. Der Kern ist
  M(k_tau = 0, k) aus REGGE-4D-1; die Summe ueber die Zeitabstaende steckt in M(k) bei k_tau = 0.
- **Groessen:** L = 16, 24, 32 (Karte). Geurteilt wird auf **L = 32**, dem groessten L der Karte [F7]. L = 64 wird
  zusaetzlich nur als Torusprobe gerechnet (beschreibend, kein Urteil).

## 2. Wirkung, Vorzeichen, Quelle [M]

- **Wirkung:** S_E = -(1/(8 pi G)) sum_t A_t eps_t + M sum_WL l_e.
  - sum A eps entspricht 1/2 Int R sqrt(g) [S, Regge/Williams Gl. 1-2, gelesen in REGGE-4D-1]. Also ist
    S_E = -(1/(16 pi G)) Int R sqrt(g) + M Int ds, die euklidische Einstein-Wirkung mit Punktteilchen.
- **Feldgleichung** (Schlaefli): dS_E/ds_e = -(1/(8 pi G)) sum_t (dA_t/ds_e) eps_t + M (dl_e/ds_e) [e in WL] = 0.
  - Mit dl/ds = 1/(2 l) = 1/2 an Zeitkanten der Laenge 1: sum_t (dA_t/ds_e) eps_t = 4 pi G M fuer e in WL, sonst 0.
  - Linear mit M = Hess(sum A eps) aus REGGE-4D-1 (dort H = -M): **M(k) u(k) = 4 pi G M e_tau**.
  - Die Quelle haengt nicht von k ab: Die Weltlinie liegt bei x = 0, die Mittelpunktsphase der Zeitkante ist bei
    k_tau = 0 gleich 1.
- **Vorzeichen am Kontinuum geprueft [M]:**
  - Aus S_E folgt G^tau_tau = -8 pi G M delta^3 (Variation: dS/dg_mn = (1/16 pi G) G^mn sqrt g + (M/2) u^m u^n delta^3).
  - Die statische Loesung ist h_tautau = 2 Phi und h_ij = -2 gamma Phi delta_ij mit gamma = 1 und
    Laplace Phi = 4 pi G M delta^3, also Phi = -G M/r.
  - Linearisiert G_tautau = -2 Laplace Phi und G_ij = 0. Zeitkanten werden nahe der Masse kuerzer (Rotverschiebung),
    Raumkanten laenger.
- **Beschreibende Probe:** Bei k_tau = 0 aendern weder Eichmoden noch Hyperdiagonale die Zeitkanten (sin(k_tau/2) = 0).
  - delta s_tau(x) = 2 Phi(x) ist also eichfrei.
  - Bericht f(r) = -r (delta s_tau + 2 G M xi/L + (4 pi/3) G M r^2/L^3)/(2 G M) auf der x-Achse mit xi = -2,837297 [L],
    Erwartung 1 (Anziehung). Kein Urteil.
- **Normierung:** G = 1, M = 1. Alles ist linear in G M.

## 3. Loesung, Nullraum, Fixierung der Hyperdiagonale [M, F]

- **Nullraum je k != 0 [F1]:** analytisch die 4 Gitter-Eichmoden u_d = sin(k.d/2) d_mu (exakte Nullvektoren,
  REGGE-4D-1) und e_top.
  - Geloest wird auf dem orthogonalen Komplement Q_c (10-dimensional): u = Q_c (Q_c^T M Q_c)^-1 Q_c^T s.
  - Die numerischen Eigenvektoren werden dafuer nicht benutzt. Bei abs(k) = 0,2 sind sie nur auf etwa 1e-9 genau
    (REGGE-4D-1: 2e-8 bei 0,05, faellt wie 1/k^2).
- **Quelle auf dem Nullraum [Karte Z0]:** norm(P_null s)/norm(s) mit P_null = Projektor auf die analytische Basis.
  - Bei k_tau = 0 ist das exakt 0 [M]: e_tau hat in jeder Eichmode die Komponente sin(k_tau/2) = 0, und e_tau steht
    senkrecht auf e_top.
  - Mitberichtet: Residuum der Gleichung, Nullraumresiduum norm(M Q_null)/Lambda, kleinster Eigenwert auf dem
    Komplement.
- **k = 0 entfaellt:** gleichfoermiger Hintergrund -M/L^3 je Zeitkante. Bei k = 0 hat e_tau einen affinen Anteil; das
  ist die Hintergrundladung. Sie wird in Abschnitt 5 korrigiert.
- **Fixierung der Hyperdiagonale [F2]** (geltende Fassung nach Rauchlauf 2, siehe Abschnitt 11):
  - Die Loesung hat u_top = 0, da e_top im Nullraum liegt. Die Fehlwinkel haengen aber von u_top ab (Vorbemerkung).
  - **Festlegung:** je k wird u_top so gewaehlt, dass die Fehlwinkel im quadratischen Mittel ueber die 50 Typen am
    kleinsten sind: u_top = c = -(v^+ eps)/(v^+ v) mit v = E(k) e_top. Das ist eps -> P eps, die Projektion senkrecht
    zu v.
  - **Eigenschaften [M]** (im Lauf geprueft, beschreibend):
    - (a) Exakt frei von der Diagonalmode (Projektion).
    - (b) Exakt frei von Eichmoden, denn E g = 0.
    - (c) 2 pi-periodisch in k, also reelle Felder ohne Sprung am Zonenrand.
    - (d) Die Wirkung aendert sich nicht, denn M e_top = 0.
  - Dieselbe Projektion mit v0 = E(0) e_top wird auf die Kalibrierung angewandt (Abschnitt 4).
  - [M, grob] Die O(k)-Anteile von v(k) heben sich in den paar-gemittelten Quadraten in fuehrender Ordnung auf
    (Inversionspartner). Der Rest ist O(1/r^2) relativ. Ungeprueft; die Groessenreihe ist die Probe.
  - **Verworfene erste Fassung:** u_top = sinc(k.1111/2) 1111^T (S'B0')^+ u_14, die glatte Einbettung.
    - Sie ist nicht 2 pi-periodisch, denn sinc(x + pi m) ist nicht +-sinc(x). Ein Sprung am Zonenrand gibt im Ortsraum
      einen Schwanz ~ (-1)^x/x.
    - Gesehen in Rauchlauf 2: Imaginaerteil 0,19 bei max abs(eps) 4,8.
- **Ohne Fixierung (u_top = 0)** werden die Achsenwerte nur berichtet [F]. Erwartung [M]: Dort entsteht ein
  Fehlwinkelanteil ~ E e_top 1111^T h 1111 ~ Phi ~ 1/r statt 1/r^3.

## 4. Fehlwinkel, Dreiecke, Kalibrierung [M, F]

- **Fehlwinkel:** eps_t(x) = (1/L^3) sum_{k != 0} exp(i k.(x + c_t)) (E(k) u(k))_t mit c_t = Schwerpunkt. Inverse FFT
  je Dreieckstyp; Imaginaerteil berichtet.
- **Welche Kruemmung ein Dreieck misst [M]:** Der Fehlwinkel eines Gelenks ist die Drehung in der Ebene **senkrecht**
  zum Gelenk (R^abcd = sum_t eps_t U_t^ab U_t^cd delta_t, U_t = Normalenbivektor [L]).
  - (tau,x)-Dreiecke messen also vor allem R_yzyz (raeumlich, ~ gamma), (y,z)-Dreiecke R_tauxtaux (Newton).
  - Die Karte ordnet umgekehrt zu ("(tau,x) ~ R_tauxtaux"). Bei gamma = 1 ist das gleichgueltig. Die
    Kartenlesart (Kehrwert des naiven Verhaeltnisses) wird mitberichtet.
- **Symmetrie [M]:** sigma = (tau y)(x z) ist eine Achsenvertauschung, also eine Kuhn-Symmetrie. Sie bildet den Typ
  (e_tau, e_x) auf (e_y, e_z) ab.
  - Fuer jede statische Vakuumkruemmung mit gamma = 1 auf der x-Achse gilt sigma^* R = R (euklidisch Ricci-flach:
    K(P) = K(P senkrecht)). Dann sind die Fehlwinkel beider Typen am selben Ort gleich, unabhaengig von Kalibrierung.
  - **Aber:** Ein Dreieck sieht im Gitter nicht nur die Sektionalkruemmung seiner Normalebene (Uebersprechen). Fuer
    gamma != 1 ist das Verhaeltnis deshalb nicht gamma, und die Orte der Dreiecke stimmen nicht ueberein. Darum gilt
    die Kalibrierung [F3].
- **Quadrate statt Einzeldreiecke [F4]:**
  - Je Koordinatenebene (mu, nu) zerfaellt das Quadrat [p, p + e_mu + e_nu] in die Typen (e_mu, e_nu) und
    (e_nu, e_mu). Deren Mittel ist punktsymmetrisch um die Quadratmitte (Inversion ist Kuhn-Symmetrie), der
    Gradientenfehler also O(1/r^2).
- **Kalibrierung [F3]:** Antwort C_t[R] auf konstante Kruemmung.
  - Quadratisches h, Kantenlaengen per Linienintegral (exakt), Fehlwinkel ueber die Schablone von Weg T.
  - Die vier Gittermoden (C4 aus REGGE-4D-1) werden wie in der Loesung versklavt:
    C4^T M(0) (ds_kin + C4 w) = 0.
  - Danach dieselbe Projektion wie [F2] mit v0 = E(0) e_top (geltende Fassung; erste Fassung: Linienintegral der
    Hyperdiagonale).
  - Geurteilt wird mit der **versklavten** Kalibrierung [F3]. Die kinematische Fassung (ohne Versklavung, projiziert)
    liefert gamma_kin, nur als Bericht.
  - Basis: Phi_ij (6 Komponenten), je Teil N (h_tautau = 2 Phi_q) und S (h_ij = -2 Phi_q delta_ij),
    Phi_q = 1/2 Phi_ij x^i x^j.
  - **Kontrollen** (beschreibend):
    - Riemann-Normalkoordinaten gegen statische Eichung (gleiche Kruemmung) muessen dieselben Fehlwinkel geben.
    - Verschiebung des Ursprungs darf nichts aendern.
    - Groesse des Versklavungsanteils.
- **Vorhersage je Quadrat:** P^N = C[N(Phi(c))], P^S = C[S(Phi(c))] an der exakten Quadratmitte c, mit
  Phi_ij = -G M (3 c_i c_j - r^2 delta_ij)/r^5.

## 5. Torus-Korrektur [M, F5]

- **Poisson-Summe mit kubischer Bildsumme [M]:**
  eps_L(x) = sum_n eps_inf(x + n L) - (1/L^3) <F(k -> 0)>, mit <.> = Mittel ueber die Richtungen von k -> 0.
  - Kontinuumsprobe: d_i d_j G_L = Bildsumme + delta_ij/(3 L^3) passt zum r^2/(6 L^3)-Glied wie in REGGE-RAND-1.
  - Der Hintergrundterm enthaelt den geometrischen Hintergrund und einen Kontaktterm der Gittermoden. Beide werden
    direkt aus dem Gitterspektrum genommen.
  - <F(0)> ist das Mittel ueber +-e_x, +-e_y, +-e_z bei abs(k) = 0,02 und 0,01, mit Richardson. Fuer quadratische
    Formen in k-Dach ist das exakt.
- **Bilder:** sum_{n != 0} eps_inf(x + n L) ~ C[Kruemmung der Bilder]. Die Bilder sind Einsteins Punktmasse
  (gamma = 1, G der Wirkung) in kubischer Summe ueber abs(n)_inf <= 16. Die Kalibrierung wird ueber alle 6
  Phi-Komponenten angewandt.
- **Korrigiert:** eps_korr = eps_L + (1/L^3) <F(0)> - C[Bild]. Roh und beide Anteile werden berichtet.
- **Bei gamma = 1** heben sich die (harmonischen) Bildglieder im Verhaeltnis heraus (sigma-Symmetrie, Abschnitt 4).
  Sie wirken nur auf G.
- **Gegenprobe:** Groessenreihe L = 16, 24, 32 und 64 (beschreibend).

## 6. Messvorschriften [F6]

- **x-Achse** (Z1), Punkte x0 = 1 ... L/2 - 1:
  - E_tx(x0) ist das Mittel der (tau,x)-Quadrate mit Zentren (x0 - 1/2, 0, 0) und (x0 + 1/2, 0, 0).
  - E_yz(x0) ist das Mittel der vier (y,z)-Quadrate mit Zentren (x0, +-1/2, +-1/2).
  - Beide sind torus-korrigiert; P^N und P^S werden ebenso gemittelt.
  - **2x2-Loesung:** E_tx = alpha P^N_tx + beta P^S_tx und E_yz = alpha P^N_yz + beta P^S_yz. Daraus
    **gamma = beta/alpha** (raeumliche gegen zeitliche Kruemmung) und alpha = G_gemessen/G_Wirkung.
  - Mitberichtet: naives Verhaeltnis E_tx/E_yz, Kartenlesart (Kehrwert), ortskorrigiertes Verhaeltnis
    (E/P^GR je Gruppe), Kondition.
- **r^3-Profil** (Z2): einzelne (tau,x)-Quadrate mit Zentren r = x0 + 1/2 auf der Achse, torus-korrigiert.
  - Q(r) = r^3 E(r).
  - G_Karte = Mittel ueber r von E(r)/P^GR(r), mit P^GR = P^N + P^S (Einstein, G der Wirkung). Das folgt der Karte:
    G aus delta eps(tau,x).
  - Mitberichtet: alpha aus der 2x2-Loesung (Newton-Amplitude h_tautau).
- **Diagonale (1,1,0)** (Z3), Punkte (n, n, 0):
  - (tau,z)-Quadrate mit Zentren (n, n, +-1/2) gegen (x,y)-Quadrate mit Zentren (n +- 1/2, n +- 1/2, 0).
  - Das sind zueinander senkrechte Ebenen mit dem staerksten Signal (K(tau z) = K(xy) = -G M/r^3 bei gamma = 1).
  - Dieselbe 2x2-Loesung. Grund: Die Ebenen (tau, n) und (n senkrecht, z) mit n = (1,1,0)/sqrt 2 tragen keine
    Gitterdreiecke senkrecht zueinander.
- **Bereich:** 6 <= r <= L/2 - 2, also auf L = 32 6 <= r <= 14 (Karte). Fuer Z3 gilt derselbe Bereich [F]: n = 5 bis 9.

## 7. Urteilsregeln (vor jeder Rechnung mit Quelle; mechanisch in code/regge_zeit_auswertung.py)

- **Z0 eingetroffen**, wenn alle drei Teile gelten (Karte):
  - (a) 4D: Fuer L = 16, 24 und 32 gilt max_k norm(P_null s)/norm(s) <= 1e-12 (analytischer Nullraum [F1]).
  - (b) 3D: max abs(eps) ausserhalb der Weltlinie <= 1e-12 * 8 pi G M.
  - (c) 3D: abs(eps_WL/(8 pi G M) - 1) <= 1e-10.
  - Beides torus-korrigiert, also mit dem Kleink-Mittel wie in 4D.
  - 3D-Rechnung [F]: Kuhn 3D, Zeit = Achse 0, L3 = 32, d theta/d s per komplexem Schritt (Gram-Inverse,
    Leitungshinweis regge_schaum.py). Weg T nur als Gegenprobe.
- **Z1 eingetroffen**, wenn auf L = 32 fuer alle x0 mit 6 <= x0 <= 14 gilt: abs(gamma - 1) <= 0,02 (Karte).
- **Z2 eingetroffen**, wenn auf L = 32 beide Teile gelten (Karte):
  - (a) max ueber r in [6, 14] von abs(Q(r)/Mittel(Q) - 1) <= 0,02
  - (b) abs(G_Karte - 1) <= 0,02
- **Z3 eingetroffen**, wenn auf L = 32 fuer alle n mit 6 <= n sqrt 2 <= 14 gilt: abs(gamma_diag - 1) <= 0,03 (Karte).
- **Nicht auswertbar:**
  - Z1 bis Z3, wenn max abs(eps_flach) > 1e-8 oder L = 32 fehlt.
  - Z1 oder Z3, wenn die Kondition des 2x2-Systems > 1e3 ist.

## 8. Agenten-Vorhersagen (vor jeder Rechnung mit Quelle)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Z0 (a) ist exakt erfuellt (<= 1e-15, analytisch 0); 3D mit komplexem Schritt: ausserhalb <= 1e-13, WL auf <= 1e-12 | 75 % |
| A2 | Ohne Fixierung (u_top = 0) faellt r^3 E_tx auf der Achse nicht flach aus, sondern waechst etwa wie r^2 (1/r-Anteil) | 70 % |
| A3 | Kalibrierung: RNC gegen statisch <= 1e-12 relativ; der Versklavungsanteil ist >= 1 % (Gittermoden wirken auf die Fehlwinkel) | 70 % |
| A4 | Z1 eingetroffen: gamma(2x2) = 1 auf 2 % fuer 6 <= r <= 14 | 60 % |
| A5 | Z2 (a) verfehlt am grossen r-Ende (Bildkorrektur reicht nicht auf 2 %) oder bei r = 6 (Gitterkorrektur O(1/r^2)) | 50 % |
| A6 | Potentialprobe f(r) = 1 auf 1 % fuer 6 <= r <= 12 (L = 32) | 70 % |
| A7 | Z3 eingetroffen | 55 % |

## 9. Kontrollen (beschreibend)

- Flachheit; Weg T gegen komplexen Schritt (4D und 3D); Gram-Winkel gegen winkel().
- Hermitezitaet und Imaginaerteil von M(k); Imaginaerteil der Fehlwinkelfelder.
- Fehlwinkel einer Eichmode (E g); norm(E e_top).
- Fixierung: glatt exakt, eichkovariant, unabhaengig vom top-Wert.
- Kalibrierung: RNC gegen statisch; Verschiebung; Versklavungsanteil; Antwortmatrix auf der Achse
  (Uebersprechen); Sektionalkruemmungen der Teile N und S.
- Hintergrund: Differenz kappa = 0,02 gegen 0,01.
- Groessenreihe; Potentialprobe; Werte ohne Fixierung.

## 10. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde37-zeit/ (code/, rauch/, lauf/); nur ueber kleintest.sh, Spuren cpu
  und cpu6, hoechstens zwei zugleich.
- **Rauchlauf 1** (vor dem Einfrieren): `regge_zeit.py rauch1.json 8,12 16`. Er prueft die Codepfade und die
  Kontrollen; auf L <= 12 liegt kein Punkt im Bereich 6 <= r <= L/2 - 2. Was gesehen wird, steht in Abschnitt 11.
- **Hauptlauf:** `regge_zeit.py haupt.json 16,24,32,64 32`, dann `regge_zeit_auswertung.py`. Je Lauf unter 10 min
  erwartet.
- **Abbruch:**
  - Wenn eine Teilrechnung nach zwei ernsthaften Versuchen nicht laeuft: "nicht gerechnet" mit Grund.
  - Code-Aenderungen nach dem Einfrieren nur bei echten Fehlern, offengelegt.

## 11. Rauchlaeufe (Protokoll)

- Abschnitte 1 bis 10 standen vor Rauchlauf 1. Geaendert danach: nur [F2] (Fixierungsregel, Abschnitt 3) und die
  Projektion in der Kalibrierung (Abschnitt 4). Alle Schwellen und Urteilsregeln sind unveraendert.
- **Rauchlauf 0:** siehe Kopf.
- Alle Rauchlaeufe: L = 8 und 12, L3 = 16, Spur cpu, rc = 0 ausser rauch1. Auf L <= 12 liegt kein Punkt im
  Urteilsbereich. Die gamma-, alpha- und Profilwerte dieser Rauchlaeufe habe ich nicht angesehen, auch die
  Probebilder bild-gamma.png und bild-r3-eps.png nicht.
- **rauch1** (01:37:59 bis 01:38:07 UTC): Abbruch. Die Normalgleichung der sinc-Fixierung ist am Zonenrand
  (k.d = +-2 pi) singulaer. Behoben mit Pseudoinverse.
- **rauch2** (01:40:12 bis 01:40:24 UTC): lief durch. Imaginaerteil der Fehlwinkelfelder 0,19 bei max 4,8.
  - Ursache: Die sinc-Regel ist nicht periodisch. Sie ist deshalb durch die Projektion [F2] ersetzt.
- **rauch3** (01:45:44 bis 01:45:56 UTC; Auswertungsprobe bis 01:46:10 UTC). Gesehen:
  - Imaginaerteil 1,8e-15. Periodizitaet von F 1,4e-14; F(-k) = konj F(k) auf 8,7e-15.
  - Diagonalmode 4,6e-16, Eichmode 5,5e-12.
  - Quelle auf dem Nullraum 3,7e-16 bzw. 5,4e-16 (L = 8, 12); Gleichungsresiduum 2,5e-11.
  - Flach 1,8e-15; Weg K gegen T 3,8e-12; Gram-Winkel gegen winkel() 2,2e-16.
  - **Kalibrierung:**
    - RNC gegen statisch 5e-12 bzw. 9,5e-12; Verschiebung 2e-10.
    - Versklavungsanteil 59 % bzw. 44 %, Projektionsanteil 4,6 % bzw. 2,5 %.
    - Gittermodenblock C4^T M0 C4 = -8, -2, -2, -2.
    - **Antwort auf die Achsenkruemmung** (Einheit 2 G M/r^3):
      - kinematisch: (tau,x)-Typen N 0 (1e-12), S 1,000; (y,z)-Typen N 1,000, S 0. Das bestaetigt die Zuordnung zur
        Normalebene (Abschnitt 4) mit Umrechnungsfaktor 1.
      - versklavt: (tau,x) N -0,25, S 1,25; (y,z) N 1,25, S -0,25. Die Summe fuer Einstein (N + S) ist 1,00 in beiden
        Faellen.
      - (tau,z) und (x,y) entsprechend: -0,5/0 und 0/-0,5 kinematisch.
    - Folge fuer die Lesbarkeit (vorab gerechnet [M]): Bei der versklavten Kalibrierung ist d(E_tx/E_yz)/d gamma = 1,5
      bei gamma = 1, bei der kinematischen 1. Eine Abweichung des naiven Verhaeltnisses um x entspricht also
      gamma - 1 = x/1,5 (geurteilt) bzw. x (Bericht).
  - Hintergrund-Richardson: kappa-Differenz 5e-5 bei max abs(F0) 7,5.
  - 3D (L3 = 16): eps_WL = 25,1327412287178 gegen 8 pi = 25,1327412287183; ausserhalb 5,5e-14.
- **rauch4** (01:47:25 bis 01:47:39 UTC, mit Auswertungsprobe): nur Codepfad nach Ergaenzung von gamma_kin (Bericht),
  rc = 0.
