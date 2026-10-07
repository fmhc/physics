# REGGE-WELLE-SCHIEF-1: Plan (Code-Agent, Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 05:08:26 CEST (date). Plantext ab 05:23:53 CEST (date).
- Grundlage: KARTE.md. Die Vorhersagen WS0 bis WS5 und ihre Schwellen sind unveraendert uebernommen. Was die Karte offen
  laesst, ist mit [F] festgelegt. Kartenluecken und Lesarten stehen in Abschnitt 4, vor dem Einfrieren.
- **Vor diesem Plantext gestartet** (offengelegt): Rauchlauf s = 0 (Kuhn-Netz, abs(k) = 0,3/0,6, 3 Richtungen; .69,
  Spur cpu5, Start 03:22 UTC). Er ist beim Schreiben der Abschnitte 1 bis 7 nicht angesehen. Zu s != 0 ist nichts
  gerechnet.
- **Code:**
  - Unveraendert kopiert: regge4d.py (2708f33b...), regge_zeit.py (889d9b38...), regge_schief.py (374806ed...,
    REGGE-4D-SCHIEF-1), regge_welle.py (3f5fe0f5..., REGGE-WELLE-1).
  - Neu: code/regge_welle_schief.py (Rechnung) und code/regge_welle_schief_auswertung.py (Urteile, Bilder).
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier nur ueber die Vorgaengerkarten)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik (Schreibtisch)
  - [F] Festlegung dieses Plans
  - [H] Hypothese

## 1. Netz und Umrechnung physikalisch zu Gitter-k [M, F1]

- **Netz** wie REGGE-4D-SCHIEF-1 (regge_schief.GitterSchief): Kuhn-Kombinatorik, Ecken X -> x = A X.
  - A = diag(1, A_raum), A_raum = 1 + s B, B = default_rng(20261004).uniform(-1, 1, (3, 3)) (regge_schief.matrix_B).
  - s = 0; 0,1; 0,2 (Karte). Kantenvektoren A d, Laengenquadrate s_e = abs(A d)^2. Torus L = 4 nur fuer Weg T.
- **Konvention, gegen regge_schief.py geprueft [M]:**
  - Ebene Welle exp(i k_lat.X) = exp(i k_lat.A^-1 x) = exp(i k_phys.x) mit k_phys = A^-T k_lat, also
    **k_lat = A^T k_phys**. So steht es in regge_schief.teil1_matrix (`git.A.T @ kp`).
  - Der Auftrag schreibt x_phys = B x_gitter und k_gitter = B^T k_phys. Das ist dieselbe Regel, wenn B die Abbildung
    meint. Im Code heisst die Abbildung A, B ist die Zufallsmatrix in A = 1 + s B.
  - Metrikstoerung physikalisch: delta s_d = (A d)^T h (A d) (regge_schief.GitterSchief.B0).
  - Eichmoden: u_d ~ sin(k_lat.d/2) (A d).xi. Ihr Spann ist gleich dem von sin(k_lat.d/2) d_mu, weil A invertierbar
    ist. Ich nutze die zweite Form (regge_welle.nullbasis), damit s = 0 bitgleich mit REGGE-WELLE-1 rechnet.
- **Zeitachse** [M]: A e_0 = e_0. A^T mischt Zeit und Raum nicht, also k_tau,lat = k_tau,phys = i omega. Die Zeitkante hat
  die Laenge 1. omega ist also in physikalischen Einheiten, wie in REGGE-WELLE-1. **v = Re omega / abs(k_phys).**
- **Richtungen und Betraege [F2]:**
  - Die 24 raeumlichen Richtungen aus REGGE-WELLE-1 (regge_welle.richtungen), jetzt als **physikalische**
    Einheitsvektoren n. Abs(k_phys) = 0,05; 0,1; 0,2; 0,4; 0,8 (Karte). k_lat,raum = A_raum^T abs(k) n.
  - abs(k_lat)/abs(k_phys) liegt zwischen den Singulaerwerten von A_raum: 0,721 bis 1,268 bei s = 0,2 (REGGE-4D-SCHIEF-1).
- **Symmetrien [M]:**
  - Die Inversion X -> -X vertauscht mit A und bleibt Symmetrie. Damit bleibt die Paarprobe "Nullstellen bei -n =
    konjugierte bei n" (REGGE-WELLE-1) gueltig.
  - Die Permutationen der Raumachsen sind durch B gebrochen. (3,1,2) ist keine Kopie von (1,2,3) mehr.

## 2. Form, Fortsetzung, Nullraum [M]

- **Form** wie REGGE-WELLE-1 Abschnitt 1: M(k) = A(-k)^T E(k), Laurent-Polynom in z = exp(i k_tau/2) = exp(-omega/2).
  - Die Klasse regge_welle.Form ist unveraendert. Sie liest dA/ds ueber git.gelenk_ableitung (schiefe Fassung) und die
    Fehlwinkelableitungen aus Weg T auf dem schiefen Torus.
  - Die Phasen haengen an Gitterpositionen und Gitter-k.
- **Nullraum und Komplement:**
  - s = 0: 4 Gitter-Eichmoden + e_top, Q0 10-dimensional, **derselbe Rechenweg wie REGGE-WELLE-1**.
  - s != 0: nur die 4 Eichmoden. REGGE-4D-SCHIEF-1 (SC1, [S] ueber die Karte) zeigt: e_top ist dort keine Nullmode.
    Q0 ist dann 11-dimensional.
  - Die negative Diagonalmode bleibt also in F(omega) = Q0^T M(i omega, k_s) Q0 enthalten. Ihre Nullstellen sind
    gesucht.
- **Zaehlung [M, wie REGGE-WELLE-1]:**
  - Fuer jedes regulaere Komplement (rho > 0) aendert ein Wechsel det F nur um einen Faktor det(T)^2 != 0.
  - Nullstellen von det F mit rho > 0 sind daher Nullstellen der Form auf dem Quotienten nach den Eichmoden
    (intrinsisch).
  - Wo Q0 kein Komplement ist (rho = 0), entstehen Scheinnullstellen; dort ist die Physikalitaet etwa 0.

## 3. Messvorschriften [F]

- **Wie REGGE-WELLE-1, gleiche Konstanten aus regge_welle.py:**
  - Bereich R = {0 < Re omega <= 3 abs(k), abs(Im omega) <= 0,5 abs(k)}, abs(k) = abs(k_phys).
  - PEP-Wurzeln, Aberth in R', Windungszahl auf dem Rand von R.
  - Reelle Achse s(omega) mit Brent-Minima.
  - Pruefwerte s, rho, Physikalitaet; Sperren [F7] (Abschnitt 5).
  - Geister: 3 abs(k) < Re omega <= 2,4.
  - Kinetik-Matrix (omega^2-Koeffizient der direkten h-Form, physikalisches h).
- **Je Nullstelle:**
  - v = Re omega/abs(k) und Im omega.
  - **Polarisationsanteile** am TT-optimalen Vertreter w der Klasse u + range N(omega) (REGGE-WELLE-1 Abschnitt 9):
    - TT: eichinvariant, raeumlich, transversal zu n (physikalisch), spurfrei.
    - Lapse/Shift: Zeitanteil h_0mu der h-Anpassung w ~ B h.
    - **Diagonalanteil** [F3]: eindeutige Zerlegung w = B h + c_top e_top + C4 c4, mit C = [e_top, C4] aus
      regge4d.komplement und physikalischem B. diag = abs(c_top)/abs(w); Gitterrest C4: abs(C4 c4)/abs(w).
    - Dazu dieselben Anteile am kleinsten Vertreter (orthogonal zu range N(omega)), beschreibend.
  - Zuordnung (beschreibend): TT, wenn TT >= 0,95. Sonst "Diagonal/Gitter", wenn diag + C4 > Lapse/Shift, sonst
    "Lapse/Shift".
- **[F5] Polarisationen:**
  - Das sind die Lichtkegel-Nullstellen (LK, 0,5 <= v <= 1,5) in R. Sind es mehr als zwei, zaehlen die zwei mit dem
    groessten TT-Anteil.
  - Aufspaltung = abs(v1 - v2).
- **[F6] Zensus** (Kartenluecke K1):
  - Erfasst werden alle PEP-Wurzeln mit -1e-6 <= Re omega <= 2,4 und abs(Im omega) <= pi, gemeinsam per Aberth
    verfeinert.
  - Re >= 0 genuegt, weil die Nullstellenmenge unter omega -> -conj(omega) symmetrisch ist (REGGE-WELLE-1 Abschnitt 1).
  - abs(Im) <= pi erfasst jede Gitterwelle einmal: omega und omega +- 2 pi i sind dieselbe Welle, weil
    k_tau -> k_tau + 2 pi die Eichmoden nur mit Vorzeichen je Kante aendert [M].
  - Klassen:
    - unklar: s > 1e-9
    - Schein: rho < 0,05 oder Physikalitaet < 0,1
    - intrinsisch: sonst
  - **Ergaenzung nach den Rauchlaeufen, vor dem Einfrieren (Abschnitt 9, Fehler 2):**
    - Das Fenster ist abs(Im omega) <= pi + 1e-3, damit Wurzeln genau auf Im = +-pi mit beiden Kopien erfasst werden.
    - Kopien omega und omega -+ 2 pi i (Abstand <= 1e-6 (1 + abs(omega))) gelten als **eine** Welle.
    - Vertreter ist die Kopie mit dem groessten rho, also mit dem regulaersten Komplement. Ihre Klasse zaehlt.
    - Begruendung [M]: Die intrinsische Nullstelle ist dieselbe; rho und Physikalitaet haengen nur davon ab, wie das
      feste Q0 an der jeweiligen Kopie zu N liegt.
    - Schwellen (1e-9, 0,05, 0,1) unveraendert.
- **[F7] Euklidische Linie** (Kreuzung der Karte):
  - Rechnung: k = (kappa, k_lat,raum), kappa auf 257 Punkten in [-pi, pi]. Gezaehlt wird die Zahl negativer
    Eigenwerte von H = -M (Schwelle 1e-6 x Mittel, wie REGGE-4D-SCHIEF-1).
  - [M] Ein Wechsel bei kappa* heisst: Eine Mode geht bei reellem k_tau durch null. Das entspricht einer intrinsischen
    Wurzel auf der imaginaeren omega-Achse bei abs(Im omega) = abs(kappa*), also einer anwachsenden Gitterwelle.
  - **Kreuzungspunkt** heisst ein Punkt (s, Richtung, Betrag) mit Wechsel. Kreuzungspunkte werden getrennt ausgewiesen.
    Alle Urteile werden zusaetzlich ohne sie berechnet.
- **Formkontrolle G [F4]** je s:
  - (a) Laurent-Form bei reellem Gitter-k gegen git.matrizen: <= 1e-12 (96 Punkte).
  - (b) Eich-Nullvektoren bei komplexem k_tau: <= 1e-10 (64 Punkte).
  - Schwellen wie W0 in REGGE-WELLE-1. Ist G verfehlt, sind alle Punkte dieses s gesperrt.
  - Beschreibend: Residuum von e_top (bei s != 0 erwartet O(s)).
- **Beschreibend:**
  - Wuerfelgitter-Formel v_hk = 2 asinh(sqrt(sum_i sin^2(k_i/2)))/abs(k_phys): mit k = k_lat (Karte) und zusaetzlich
    mit k = k_phys.
  - Gegenprobe Weg K (komplexer Schritt mit schiefen Laengen) fuer x+, xyz+, 123, fib05 bei 0,05 und 0,8.
  - Inversionsprobe n gegen -n.

## 4. Kartenluecken, Lesarten und Hinweise (vor dem Einfrieren)

- **K1 (Kartenluecke, WS3 und WS4 "nahe der reellen Achse"):**
  - Die Karte erwartet: Ist die Diagonalmode dynamisch krank, zeigt sie sich als zusaetzliche laufende oder wachsende
    Welle.
  - [M] Ein Nulldurchgang bei reellem euklidischem k_tau = kappa* ist eine rein imaginaere Wurzel omega = -+i kappa*.
    Sie waechst wie exp(kappa* t) und liegt fuer abs(k) <= 0,8 meist weit ausserhalb von R (abs(Im) <= 0,5 abs(k)).
  - Eine Gittermode mit Frequenz der Ordnung 1 laege bei kleinem abs(k) rechts von R (Re > 3 abs(k)).
  - Im Kartenwortlaut (Bereich R wie REGGE-WELLE-1) koennen WS3 und WS4 solche Wurzeln nicht sehen.
  - **Festlegung:** Hauptlesart = Kartenwortlaut mit R. Zusatzlesart "Zensus" ([F6]), vorab festgelegt. Beide werden
    berichtet.
- **K2 (WS5, "v"):** Die Karte definiert v fuer die laufenden Moden. Hauptlesart (Kartenwortlaut): alle Nullstellen in
  R. Zusatzlesart: nur die zwei Polarisationen [F5].
- **K3 (WS0, Rauschen; keine Schwellenaenderung):**
  - Die zwei Wurzeln des Paars sind nur auf etwa 1e-8 abs(k) bestimmt (REGGE-WELLE-1: Paar auf <= 9e-9 abs(k)
    zusammen).
  - 1e-9 in v erreicht daher nur derselbe Rechenweg, keine unabhaengige Nachrechnung.
  - s = 0 laeuft hier mit denselben Modulen und in derselben Reihenfolge. WS0 prueft also die Einbindung in den schiefen
    Code (Netz, Form, Komplement), nicht die Physik neu.
- **K4 (WS1, "v"):** v = Re omega/abs(k) (Hauptlesart; die Karte trennt v und Im omega). Zusatzlesart komplex:
  abs(omega/abs(k) - 1) <= 1e-3.
- **K5 (Kreuzung):** "Zonenpunkte nahe der Kreuzung" ist ueber die euklidische Linie festgelegt ([F7]).
  - Die Kreuzung aus REGGE-4D-SCHIEF-1 liegt statisch bei k_lat,x ~ 2,9. Unsere abs(k_lat) <= 1,02 liegen weit davon.
  - In 4D betraf der Vorzeichenwechsel dort aber 544 von 4096 BZ-Punkten, also vermutlich vor allem grosse k_tau [H].
    Genau das prueft die euklidische Linie.
- Keine Schwelle und keine Vorhersage der Karte ist geaendert.

## 5. Sperren (je Punkt) [F7, wie REGGE-WELLE-1]

Ein Punkt (s, Richtung, Betrag) ist gesperrt, wenn eine dieser Bedingungen gilt:

1. Windungszahl mehr als 0,05 von einer ganzen Zahl entfernt, oder Phasensprung >= 0,5 rad auch bei vierfacher Dichte.
2. Windungszahl != Zahl der verfeinerten Nullstellen in R.
3. Eine Nullstelle in R mit s(omega_j) > 1e-9.
4. Eine Nullstelle in R mit rho < 0,05 oder Physikalitaet < 0,1.
5. min rho auf dem Rand von R < 0,05.
6. Nullvektor-Residuum auf der reellen Achse > 1e-8.
7. Formkontrolle G dieses s verfehlt.

Die Urteile sind dreiwertig wie in REGGE-WELLE-1:

- Ein Verstoss an einem ungesperrten Punkt ergibt "nicht eingetroffen".
- Sonst ergibt ein gesperrter Punkt im Urteilsbereich "nicht auswertbar".
- Sonst "eingetroffen".

## 6. Urteilsregeln (vor jeder Rechnung zu s != 0)

- **WS0:** eingetroffen, wenn an allen gemeinsamen Punkten von s = 0 und REGGE-WELLE-1 (lauf-69/haupt.json, 120 Punkte)
  alle drei Bedingungen gelten, sonst "nicht eingetroffen" (keine Sperre):
  - gleiche Windungszahl
  - gleiche Zahl der Nullstellen in R
  - max abs(v_neu - v_alt) <= 1e-9; Nullstellen nach Re omega sortiert, v = Re omega/abs(k)
- **WS1:** s = 0,1 und 0,2, abs(k) = 0,05, alle 24 Richtungen. Je Punkt muss gelten:
  - Windungszahl 2
  - genau 2 Nullstellen in R
  - beide mit abs(v - 1) <= 1e-3
  - Zusatzlesart komplex (K4).
- **WS2:** s = 0,2, abs(k) = 0,8.
  - **Eingetroffen**, wenn an mindestens einer ungesperrten Richtung mit mindestens 2 LK-Nullstellen gilt:
    abs(v1 - v2) > 1e-4 (Polarisationen [F5]).
  - **Nicht eingetroffen**, wenn alle 24 Richtungen ungesperrt sind, mindestens 2 LK-Nullstellen haben und ueberall
    abs(v1 - v2) <= 1e-4 gilt.
  - Sonst "nicht auswertbar".
- **WS3:** s = 0,1 und 0,2, alle 240 Punkte.
  - Hauptlesart: Windungszahl in R = 2.
  - Zusatzlesart Zensus: genau 2 intrinsische Zensuswurzeln je Punkt. Ein Punkt mit unklaren Zensuswurzeln ist dafuer
    gesperrt.
  - **Kontrolle der Zensuslesart:** Bei s = 0 muss jeder der 120 Punkte genau 2 intrinsische und keine unklaren
    Zensuswurzeln haben. Sonst ist die Zensuslesart "nicht auswertbar".
- **WS4:** s = 0,1 und 0,2, alle 240 Punkte.
  - Hauptlesart: Alle Nullstellen in R haben abs(Im omega) <= 1e-6 (absolut, Karte).
  - Zusatzlesart Zensus: Alle intrinsischen Zensuswurzeln haben abs(Im omega) <= 1e-6. Es gilt dieselbe Kontrolle wie
    bei WS3.
- **WS5:** s = 0,2, abs(k) = 0,4 und 0,8 (48 Punkte).
  - **Eingetroffen**, wenn an einem ungesperrten Punkt eine Nullstelle in R v > 1 + 1e-6 hat (Kartenwortlaut K2).
  - **Nicht eingetroffen**, wenn alle 48 Punkte ungesperrt sind und keine solche Nullstelle haben.
  - Sonst "nicht auswertbar".
  - Zusatzlesart: dieselbe Regel nur mit den Polarisationen.
- Alle Urteile werden zusaetzlich ohne Kreuzungspunkte [F7] berechnet.
- Die Urteile entstehen mechanisch durch code/regge_welle_schief_auswertung.py und stehen in lauf-69/auswertung.json.

## 7. Agenten-Vorhersagen (Schreibtisch, vor jeder Rechnung mit s != 0)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | WS0 eingetroffen, und zwar bitgleich (max abs(dv) = 0) | 80 % |
| A2 | Formkontrolle G haelt fuer s = 0,1 und 0,2: (a) <= 1e-15, (b) <= 1e-11; e_top-Residuum bei s = 0,2 >= 1e-3 | 80 % |
| A3 | WS1 eingetroffen; dabei max abs(v - 1) bei 0,05 <= 5e-4 | 70 % |
| A4 | WS2 eingetroffen. Gegenhypothese [H]: Die exakte Entartung in REGGE-WELLE-1 kommt von einer skalaren Gitter-Laplace-Struktur, det F ~ D(k)^2 g(k); die bliebe im schiefen Netz und gaebe keine Doppelbrechung | 55 % |
| A5 | WS3 Hauptlesart eingetroffen (in R nur das Paar) | 60 % |
| A6 | WS4 Hauptlesart eingetroffen | 55 % |
| A7 | Kontrolle der Zensuslesart haelt: Die Wurzeln bei Im omega = +-1,02 abs(k) aus REGGE-WELLE-1 sind Scheinwurzeln (rho < 0,05) | 55 % |
| A8 | Bei s = 0,2 gibt es Kreuzungspunkte (Vorzeichenwechsel auf der euklidischen Linie), also intrinsische Wurzeln auf der imaginaeren Achse | 45 % |
| A9 | WS5 Hauptlesart nicht eingetroffen (kein v > 1 + 1e-6) | 60 % |
| A10 | Die Wuerfelgitter-Formel mit Gitter-k gilt bei s != 0 nicht; Abweichung bei 0,05 von der Groessenordnung abs(abs(A^T n) - 1), also >= 1e-2 in mindestens einer Richtung | 85 % |

## 8. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde37-welle-schief/ (code/, rauch/, lauf/, ref/).
  - Start nur ueber kleintest.sh, Spuren cpu5 und p4000b (nur CPU-Rechnung), hoechstens zwei zugleich.
  - ref/: welle1-haupt.json und welle1-rauch2.json, Kopien aus /home/fmh/fmhc-physics-remote/runde37-welle/.
- **Rauchlaeufe** (vor dem Einfrieren): `regge_welle_schief.py rauch <s> rauch/rauch-s<s>.json`.
  - s = 0; 0,1; 0,2, nur abs(k) = 0,3 und 0,6, Richtungen x+, xyz+, fib05 (nicht im Urteilsbereich).
  - s = 0 wird gegen rauch2 aus REGGE-WELLE-1 (gleiche Punkte) gehalten.
  - Dazu die Probe der Auswertung (Modus probe).
- **Hauptlaeufe:** `regge_welle_schief.py haupt <s> lauf/haupt-s<s>.json` je s, dann die Auswertung. Je Lauf unter
  5 min erwartet.
- Code-Aenderungen nach dem Einfrieren nur bei echten Fehlern, offengelegt.

## 9. Rauchlaeufe (Protokoll, vor dem Einfrieren)

- Abschnitte 1 bis 8 standen vor dem ersten Rauchlauf zu s != 0 und sind danach unveraendert. Einzige Ausnahme ist die
  Ergaenzung zu [F6] in Abschnitt 3 (Fehler 2 unten). Schwellen, Urteilsregeln und Agenten-Vorhersagen sind
  unveraendert.
- Alle Laeufe: .69, nur abs(k) = 0,3 und 0,6, Richtungen x+, xyz+, fib05. Zeiten UTC aus den Starterzeilen.
- **Laeufe:**
  - Fassung 1 (Zensus mit gemeinsamer Aberth-Iteration):
    - s = 0, 03:22:29 bis 03:22:48, cpu5, rc = 0.
    - s = 0,1, 03:25:27 bis 03:25:39, cpu5, **rc = 1** (Fehler 1). Gesehen nur die Zeile x+, 0,3: Windung 2, Zensus
      3 intrinsisch, euklidisch 2 negative Eigenwerte.
    - s = 0,2: **nicht gestartet**. Shell-Klammerung `cd ... && (A) & (B) &`: Das cd galt nur fuer A, B fand den
      Logpfad nicht. Nichts gerechnet.
  - Fassung 2 (Newton je Zensuswurzel, sha e2563678...):
    - s = 0,1, 03:27:15 bis 03:27:36, cpu5.
    - s = 0,2, 03:27:16 bis 03:27:37, p4000b.
    - s = 0, 03:27:51 bis 03:28:10, cpu5.
    - Probe der Auswertung, 03:28:10 bis 03:28:17.
    - Alle rc = 0.
  - Fassung 3 = Endfassung (Fenster pi + 1e-3; Paarung in der Auswertung; sha db3a1643... und d4a3d70d...):
    - s = 0,1, 03:30:35 bis 03:30:56, p4000b.
    - s = 0,2, 03:30:39 bis 03:30:59, cpu5.
    - s = 0, 03:30:59 bis 03:31:19, cpu5.
    - Probe, 03:31:19 bis 03:31:25.
    - Alle rc = 0.
- **Gesehen (Endfassung; Fassung 2 gleich bis auf die Zensuszaehlung):**
  - s = 0 ist gegen rauch2 aus REGGE-WELLE-1 an allen 6 Punkten **bitgleich** (Nullstellen, Windung, TT-Anteile;
    Vergleich per jq und cmp).
  - Formkontrolle G (s = 0,1 / 0,2): (a) 5,7e-16 / 6,9e-16; (b) 1,4e-12 / 1,6e-12; e_top-Residuum min 2,8e-2 /
    4,9e-2. k = 0: 11. Eigenwert -0,381 / -0,934, wie REGGE-4D-SCHIEF-1.
  - **In R** (je s 6 Punkte):
    - Windung 2,000, genau das Paar, reell (abs(Im omega) <= 3,6e-11), TT >= 0,9967.
    - **Das Paar spaltet auf:** s = 0,1: 1,1e-4 (x+, 0,3) bis 4,9e-3 (xyz+, 0,6). s = 0,2: 3,9e-4 (x+, 0,3) bis
      1,5e-2 (fib05, 0,6).
    - v < 1 ueberall (hoechstens 0,9979).
  - **Zensus:**
    - s = 0: genau 2 intrinsische Wurzeln je Punkt; alle anderen sind Scheinwurzeln auf der imaginaeren Achse (rho = 0,
      Physikalitaet 0). Das bestaetigt A7 an diesen 6 Punkten.
    - s != 0: je Punkt **eine zusaetzliche intrinsische, gestaffelte Welle** bei Im omega = +-pi (z = -i exp(-Re/2),
      Vorzeichenwechsel je Zeitschritt).
      - Re omega ~ 2,30 bis 2,33 (s = 0,1), ~ 0,18 bis 0,42 (s = 0,2).
      - Diagonalanteil 0,38 bis 0,97, Lapse/Shift 0,33 bis 0,93, rho 0,08 bis 0,67.
    - s = 0,2, x+, 0,6: zwei intrinsische Wurzeln auf der imaginaeren Achse (+-2,7655i). Auf der euklidischen Linie
      wechselt dort die Signatur bei kappa = +-2,761 (Kreuzungspunkt).
  - **Probe der Auswertung** (0,3/0,6; keine Kartenaussage):
    - WS0 eingetroffen.
    - WS1 nicht eingetroffen (Betrag 0,3 statt 0,05).
    - WS2 eingetroffen.
    - WS3 und WS4: Hauptlesart eingetroffen, Zensuslesart nicht eingetroffen.
    - WS5 nicht eingetroffen.
    - 1 Kreuzungspunkt. Bilder angesehen: keine.
- **Gefundene Fehler (Messung, keine Schwelle):**
  1. Die gemeinsame Aberth-Iteration ueber alle Zensuswurzeln lief bei s = 0,1 aus dem Ruder (singulaere Matrix).
     - Ersetzt: Wurzeln in R' uebernehmen den Aberth-Wert der Hauptrechnung (wie REGGE-WELLE-1).
     - Alle anderen bekommen gedaempftes Newton je Wurzel, Schritt hoechstens 0,05 max(abs(k), abs(omega)), mit
       Fehlerschutz ("unklar").
  2. Das geschlossene Fenster abs(Im) <= pi zaehlte Wurzeln auf Im = +-pi doppelt (omega und omega - 2 pi i, z. B.
     fib05, 0,6: 0,38295 +- 3,14159i).
     - Ob die zweite Kopie im Fenster lag, hing an Rundung im Bereich 1e-9.
     - Ihre rho-Werte unterscheiden sich, weil das feste Q0 an beiden Kopien verschieden zu N liegt.
     - Berichtigt nach dem Plantext ("jede Gitterwelle einmal"): Ergaenzung zu [F6].
- **Selbstanzeige Vorwissen:**
  - Die Rauchlaeufe machen WS2 (Aufspaltung bis 1,5e-2 schon bei 0,6) und die Zensuslesarten von WS3 und WS4
    (gestaffelte Welle an jedem Rauchpunkt mit s != 0) weitgehend vorhersehbar.
  - WS3 und WS4 in der Hauptlesart sind wahrscheinlich (nichts Zusaetzliches in R).
  - Bei den Kartenbetraegen 0,05 bis 0,8 ist zu s != 0 nichts gerechnet. WS1 und WS5 habe ich dort nicht gesehen.
