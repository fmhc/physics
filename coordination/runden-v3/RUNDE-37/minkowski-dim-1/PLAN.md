# MINKOWSKI-DIM-1: Plan (Code-Agent, Runde 48)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-05 10:58:12 CEST (date).
- Plan geschrieben ab 2026-10-05 11:20:20 CEST (date), nach den Rauchtests R1 bis R3, vor jedem echten Lauf.
- Karte KARTE.md unveraendert. Die Vorhersagen MD0 bis MD4 und ihre Bedeutungszeilen gelten woertlich. Dieser Plan legt
  nur Netze, Operatoren, Raster, Laeufe und die mechanische Auswertung fest.
- Code (sha256 in EINGEFROREN-SHA256.txt):
  - code/md.py (neu: MD0, MD1, MD3, MD4, Auswertung)
  - code/bagdim_st.py: Kopie von RUNDE-24/bag-dim/code/bagdim.py mit drei Zusaetzen (Graph st, Spektrum-Bauprobe und
    Eigenwerte fuer st, Option --periode); Modell, Minimierung, Starts, Wahl und Diagnose unveraendert
  - unveraendert kopiert: tu.py, tg.py, uk.py, ew.py, mn.py, tg_auswertung.py, tp.py (TAKT-UMKLAPP-1), dn.py, tti.py,
    nachtrag_kinetik.py (DEFEKT-NETZ-1), bagdim.py (BAG-DIM, nur Referenz)
  - code/haupt.sh (Laufketten), code/rauch1.sh, code/rauch2.sh (Rauchtests)
- .69: /home/fmh/fmhc-physics-remote/minkowski-dim-1/ (code/, rauch/, rauch2/, lauf/). Lokal nur Lesen, Schreiben, ssh,
  scp, rsync, jq, sha256sum.
- Zeitbox 120 min ab 10:58:12 CEST.

## 1. Netze

| Netz | Bau (Funktion) | Ecken je Zelle | Herkunft |
|---|---|---|---|
| V | tg.netz_V() | 10 (fcc-Primitivzelle, kubische Kante 1) | EINE-WELT-LOCH-1, TT-ISO-1 |
| S | tu.netz_aus_ew('S') | 6 | nur Kontrolle (S = C15, DEFEKT-NETZ-1) |
| C15 | dn.kristall('C15') + dn.periodisch_delaunay | 24 (kubische Zelle) | DEFEKT-NETZ-1 (Delaunay, Gleichstaende 0) |
| A15 | dn.kristall('A15') + dn.periodisch_delaunay | 8 (kubische Zelle) | DEFEKT-NETZ-1 (Delaunay, Gleichstaende 0) |
| Glas | tg.zufallsnetz(512, saat), Saaten 1 bis 4 | 512 (Torus) | TT-GLAS-2 (dk512-A/B) |
| Sierpinski-Tetraeder st:n | bagdim_st.sierpinski_tetraeder(n): Ecken und Kanten der 4^n kleinsten Teiltetraeder | N = 2 4^n + 2, 6 4^n Kanten | neu |

- Sierpinski-Tetraeder: grosses Tetraeder mit den Ecken (0,0,0), (1,1,0), (1,0,1), (0,1,1) mal 2^n. Mittelknoten = Mitte
  der Kante (0,0,0)-(2^n, 2^n, 0); Abstand 2^(n-1) zu zwei Ecken, 2^n zu den anderen beiden (wie BAG-DIM beim Dreieck).
  Bauprobe in R2: st:3 N = 130, 384 Kanten, 4 Ecken mit Grad 3, sonst Grad 6, d_rand = 4 (alles wie Soll).
- C15/A15: Die Gleichstaende (>= 5 Punkte auf einer Umkugel) werden im Lauf mit dn.gleichstaende neu gezaehlt (berichtet).

## 2. Operatoren und Normierung

- **Takt:** T = 8 d0^H *1 d0 je Bloch-k. *1 = umkreisbasierte, vorzeichenbehaftete Hodge-Sterne (tu.hodge, unveraendert).
  Das ist Finns Takt P = -W^H B W (HT0 in TAKT-UMKLAPP-1, Rest <= 6,6e-16 auf V und S). Hier je Netz an drei
  Zufalls-k gegen tu.takt_mats geprueft (Abschnitt 8).
- ***0** je Ecke = umkreisbasiertes duales Volumen sum_Kanten l A*/6 (dieselbe Formel wie in tu.hodge, dort nicht
  zurueckgegeben). Kontrolle: sum *0 = Zellvolumen.
- **Gewertet (MD3, MD4): X = *0^-1 T**, also das verallgemeinerte Eigenwertproblem T x = lambda *0 x, gerechnet als
  *0^-1/2 T *0^-1/2.
  - **Begruendung:**
    - Mit *0 ist X die DEC-Form des Laplace-Beltrami-Operators auf Funktionen [L]. Die Waerme fliesst dann im
      physikalischen Volumen, und bei feinem Netz gehen die Eigenwerte gegen k^2 des Kontinuums. Nur so ist "d_s im
      Grossen = 3" die Kontinuumsaussage.
    - Ohne *0 haette jede Ecke dasselbe Gewicht, unabhaengig von ihrem Volumen. Auf V schwankt *0 stark
      (TAKT-UMKLAPP-1: kleinster Wert 0,0161 bei Zellvolumen 0,25 fuer 10 Ecken).
    - Der Faktor 8 verschiebt nur die sigma-Skala. d_s, Maximum und Stufenregel haengen nicht davon ab.
  - Voraussetzung *0 > 0 an allen Ecken: in R2 auf V, C15, A15 und einem Glas N = 512 erfuellt (0 nicht positive
    Eintraege); TAKT-UMKLAPP-1: V, S, Glas N = 128 ebenso. Fehlt sie bei einem Netz, gilt dort T allein (markiert).
- **Berichtet, ohne Wertung:** T allein (Knotengewicht 1) und der Graph-Laplace der Netzkanten (Kantengewicht 1).
- **MD1 und MD2:** Graph-Laplace mit Gewicht 1 (Karte; BAG-DIM).

## 3. d_s(sigma)

- P(sigma) = (1/N_ges) sum exp(-sigma lambda) ueber alle Eigenwerte; d_s = -2 d ln P/d ln sigma = 2 sigma <lambda>_sigma.
- Oertliche Steigung: d d_s/d ln sigma = d_s - 2 sigma^2 Var_sigma(lambda) (exakt, keine numerische Ableitung). Fuer die
  Stufenregel gilt die Steigung je Dekade: d d_s/d log10 sigma = ln 10 mal d d_s/d ln sigma.
- **Periodische Netze:** Gamma-zentriertes k-Gitter n^3 der Zelle; gewertet n = 40 (V, S, A15) bzw. 32 (C15),
  Kontrolle n = 20 bzw. 16. N_ges = n^3 mal Ecken je Zelle.
- **Glas:** Eigenwerte bei k = 0 (Torus des Glases, N_ges = 512), wie die Karte sagt ("ueber Eigenwerte"). Kontrolle:
  k-Gitter 2^3 der Glaszelle (N_ges = 4096).
- **Raster:** sigma mal lambda_mittel = 10^(j/100), j = -300..500 (8 Dekaden, 100 Punkte je Dekade); lambda_mittel =
  Mittel aller Eigenwerte des Operators.
- **Zulaessig:** P(sigma) >= 8/N_ges. Begruendung [M, Gauss-Naeherung]: Die Bildkorrektur des Torus ist dann in d_s
  unter 1e-3. P faellt monoton, also ist das ein Anfangsstueck des Rasters.
- **MD1 analytisch:** d_s = 12 sigma (1 - I1(2 sigma)/I0(2 sigma)) mit scipy.special.i0e/i1e, sigma = 10^(j/100),
  j = -300..400. Feines Maximum: minimize_scalar (bounded) zwischen den Nachbarn des Rastermaximums.
- **MD2-Spur:** Graph-Laplace des Sierpinski-Tetraeders, volles eigvalsh (wie BAG-DIM K0): Stufe 6 (N = 8194) gewertet,
  Stufen 4 und 5 berichtet. Die Eigenwerte werden gespeichert.

## 4. Kaestchenzaehlung (MD0)

- **a** = mittlere Kantenlaenge von V (arithmetisch ueber die 68 Kanten der Primitivzelle; md.py rechnet sie aus dem
  Netz). Strukturwert aus R2: a = 0,35897 (kubische Kante 1), Kanten 0,2165 bis 0,4146, groesster
  Inkugeldurchmesser 0,154, Dreiecksflaeche je kubischer Zelle 23,82.
- **2-Geruest von V** = Vereinigung aller Dreiecke (uk.flaechen, jede Flaeche einmal: 116 je Primitivzelle; die kubische
  Zelle ist die Primitivzelle plus drei fcc-Verschiebungen).
  - Jedes Dreieck wird auf einem baryzentrischen Gitter mit Punktabstand h <= eps/8 abgetastet.
  - Gezaehlt werden die Kaestchen des Torus, die mindestens einen Punkt enthalten.
  - Feste Verschiebung des Geruests gegen das Kaestchengitter: (0,0123457; 0,0234568; 0,0345679).
- **Kleines Fenster** (gewertet fuer "Kaestchen <= a/8"): Torus der kubischen Zelle (L = 1), eps = 1/m,
  m_j = round((8/a) 2^(j/4)), j = 0..12; es zaehlen nur Werte mit a/64 <= eps <= a/8.
- **Grosses Fenster** (gewertet fuer "Kaestchen >= 2a"): Torus aus 8^3 kubischen Zellen (L = 8), eps = 8/m, alle ganzen
  m mit 2a <= eps <= 10a.
- **Uebergang** (nur berichtet): L = 1, m = 1..ceil(8/a).
- **Schaetzer:** Kleinste-Quadrate-Steigung von ln N gegen ln(1/eps) ueber alle Werte des Fensters. Berichtet: Sekanten
  zwischen Nachbarn.
- **Sierpinski-Tetraeder** (gewertet):
  - Ecken der Stufe 10: 2 4^10 + 2 = 2 097 154 Punkte (grosse Kante sqrt2 in Wuerfeleinheiten).
  - eps_j = 2^(-7 + j/4), j = 0..20: fuenf volle Oktaven, 1,5 Dekaden; eps_min = 5,7 kleinste Kanten.
  - Gitterverschiebung wie oben; Steigung wie oben.
  - Berichtet: Stufe 8 nach derselben Regel, dyadisch ausgerichtete Kaestchen 2^-q (q = 2..7, ohne Verschiebung),
    Ein-Oktaven-Sekanten.

## 5. Beutel (MD2, wie BAG-DIM)

- Modell (FLS, lam = g = 1, Knoten- und Kantengewicht 1), L-BFGS-B, Konvergenzregel, Starts, Wahl und Diagnose wie
  BAG-DIM (Code unveraendert in bagdim_st.py).
- **Graph:** st:7 (N = 32770, 98304 Kanten, d_rand = 64 bis zur naechsten Ecke).
- **Raster:** Q_k = 40 (4 sqrt6)^(k/8), k = 0..32 (Q = 40 bis 3,7e5).
  - Eine Periode = Faktor 2 im Radius = Faktor 4 sqrt6 = 9,798 in Q (Volumen mal 4, sqrt(lambda_1) durch sqrt6; wie
    BAG-DIM 3 sqrt5 beim Dreieck) [M].
  - 8 Schritte je Periode; volle Perioden sind ganze Schrittzahlen.
- **Starts je k:**
  - fort (ausser am ersten k eines Laufs)
  - frisch mit R0 = max(2; 1,2 Q^0,3037), dazu R0 mal 1,5 und R0/1,5 (pruef-k alle, wie BAG-DIM beim Dreieck)
  - flach an k = 8 und 16; dE/dQ an k = 12 und 24
  - b = 1/(d_f + d_w/2) = 1/(2 + log2(6)/2) = 0,3037 [M]. a = 1,2 gesetzt; R4: frischer Start bei Q = 1e5 kompakt,
    Rg = 40, nB = 4873.
- **Wahl** wie BAG-DIM: kleinste Energie unter den konvergierten kompakten Beuteln am Mittelknoten. Kompakt (BAG-DIM):
  zusammenhaengend, Abstand zum Mittelknoten <= 2, |f|-Maximum <= 3 Schritte, >= 50 % von S im Beutel, nB <= N/4,
  Rs + 10 <= d_rand.
- **Beutelbereich (gewertet):** laengste zusammenhaengende Folge von k, an denen
  - (i) ein kompakter Beutel gewaehlt ist und
  - (ii) kein konvergierter Start mit dmin <= 2 (also am Mittelknoten) tiefer liegt als der gewaehlte.
  - Regel (ii) ist neu, aus der BAG-DIM-Selbstanzeige: Dort nahm die Wahl am obersten Punkt einen Nebenast, weil der
    tiefste zentrale Beutel nur an der Fuellgrenze nB <= N/4 scheiterte. Der Bereich ohne (ii) wird berichtet.
- **p ueber volle Perioden (gewertet):** Sekante ln(E(k_o)/E(k_o - 16)) / ln(Q(k_o)/Q(k_o - 16)) ueber zwei volle
  Perioden am oberen Ende des Bereichs (k_o = oberstes k). Hat der Bereich weniger als 17 k: eine Periode (markiert);
  weniger als 9 k: offen. Berichtet: alle gleitenden Ein- und Zwei-Perioden-Sekanten.

## 6. Laeufe (nur .69, kleintest.sh; Spuren cpu2, cpu3, cpu4; je Aufruf hoechstens 10 min)

| Spur | Kette (nacheinander; Startskript code/haupt.sh) |
|---|---|
| cpu2 | M1 kubisch; M0 kasten; S4, S5, S6 spektrum st:4, st:5, st:6; BD beutel k 22..25; BB beutel k 12..17 |
| cpu3 | T1 takt V, S, C15, A15; T2 takt Glas N = 512, Saaten 1 bis 4; BE beutel k 26..28; BA beutel k 0..11 |
| cpu4 | BF beutel k 29..32; BC beutel k 18..21 |
| cpu2 (danach) | AW auswertung ueber lauf/ |

- Beutel-Laeufe: --budget 560 (der Code bricht vor einem k ab, wenn verbraucht + 1,3 x letzter Punkt > 560 s).
- **Restlaeufe:** Stoppt ein Beutel-Lauf am Budget, laeuft der Rest ab dem ersten fehlenden k als neuer Lauf mit sonst
  gleichen Argumenten (Datei b_st_<x>2.json). Bricht ein Lauf mit Fehler ab, wird er einmal unveraendert wiederholt.
  Beides wird offen vermerkt; danach laeuft die Auswertung erneut (auswertung2.json).
- Die Auswertung legt alle Starts aller b_st*.json je k zusammen (wie BAG-DIM).

## 7. Mechanische Auswertung (md.py auswertung, auf der .69 ueber kleintest.sh)

- **MD0 eingetroffen**, wenn alle drei gelten:
  - Steigung im kleinen Fenster (V) in [1,9; 2,1]
  - Steigung im grossen Fenster (V) in [2,9; 3,1]
  - Steigung Sierpinski-Tetraeder Stufe 10 in [1,95; 2,05]
- **MD1 eingetroffen**, wenn
  - das feine Maximum in [3,4; 3,8] liegt und
  - d_s sich 3 von oben naehert: an allen Rasterpunkten sigma >= sigma_max ist d_s > 3, d_s faellt dort monoton, und
    d_s(10^4) - 3 <= 1e-3.
- **MD2 eingetroffen**, wenn beide Teile gelten:
  - (a) Spur: Mittel ueber eine log-Periode (Stufe 6) in [1,467; 1,627] (1,547 +- 0,08, Kartenwortlaut).
    - Mittel ueber [s0, 6 s0] = (1/ln 6) Integral d_s d ln sigma = -2 ln(P(6 s0)/P(s0))/ln 6 (Faktor 6 in sigma = Faktor
      2 in der Laenge).
    - Zulaessig: sigma >= 1 und P(sigma) >= 10/N. sigma_b = groesstes zulaessiges sigma des Rasters 10^(j/100),
      j = -200..600.
    - Gewertet: das Fenster mit der geometrischen Mitte sqrt(1 mal sigma_b). Ist sigma_b < 6, ist (a) offen.
    - Berichtet: alle gleitenden Fenster (kleinster, groesster, mittlerer Wert), Stufen 4 und 5, die Plateau-Regel aus
      BAG-DIM.
  - (b) Beutel: p ueber volle Perioden (Abschnitt 5) mit |p - 0,607| <= 0,03 und |p - 0,607| < |p - 0,667|.
- **MD3 eingetroffen**, wenn fuer jedes der Netze V, C15 und A15 (X = *0^-1 T, gewertetes k-Gitter) gilt:
  - Das groesste d_s im zulaessigen Bereich ist > 3,2 und liegt im Inneren (nicht am ersten oder letzten zulaessigen
    Rasterpunkt).
  - Es gibt keine Stufe. Stufe (Kartenwortlaut): eine Zone von mindestens einer halben Dekade in sigma
    (zusammenhaengende Rasterpunkte, log10(sigma_bis/sigma_von) >= 0,5), in der an jedem Punkt
    |d d_s/d log10 sigma| < 0,1 und 1,6 <= d_s <= 2,4 gilt.
  - "Oertliche Steigung" wird je Dekade gemessen. Berichtet: die laengsten flachen Zonen ohne Band.
- **MD4 eingetroffen**, wenn das Mittel der vier Glas-Maxima (X = *0^-1 T, k = 0) hoechstens Maximum(V) - 0,2 ist
  (Maximum von V wie in MD3).
  - Liegt das Gamma-Maximum einer Saat nicht im Inneren ihres zulaessigen Bereichs, gilt fuer diese Saat das Maximum
    aus dem k-Gitter 2^3 (markiert).
  - Berichtet: jede Saat einzeln, und ob alle vier einzeln die Bedingung erfuellen.
- Passt ein Ausgang nicht in die Bedeutungszeilen der Karte, wird er beschrieben, nicht umgedeutet.

## 8. Kontrollen (Plan, nicht Karte; nur berichtet)

- Bloch-Matrix gegen tu.takt_mats: L1 relativ <= 1e-12, P gegen 8 L1 relativ <= 1e-10, je Netz an drei Zufalls-k.
- *0 > 0 und sum *0 = Zellvolumen (auf 1e-12); *1 >= 0; kleinster Roh-Eigenwert >= -1e-10 lambda_max.
- S gegen C15 (gleiche Struktur, andere Zelle): Maximum und d_s gleich (Abweichung berichtet).
- k-Gitter: Maximum im gewerteten gegen das Kontroll-Gitter; Glas k = 0 gegen 2^3.
- MD1: periodisches 64^3-Gitter (Produktformel) gegen Bessel bis sigma = 20; eigvalsh eines periodischen 8^3-Gitters
  gegen die Produktformel; numerische Ableitung von ln P an vier sigma; Asymptotik 3 + 3/(8 sigma).
- MD2: Bauproben (N, Kanten, Grade, d_rand); dE/dQ = omega (|rel| <= 1e-4); Nebentaeler (Zahl der k, an denen x1,5 oder
  /1,5 tiefer lag, groesste Abstaende); Rand- und Fuellzustaende aus den flachen Starts.
- MD0: im grossen Fenster alle Kaestchen getroffen (N = m^3; vorab sicher, da eps > groesster Inkugeldurchmesser [M]);
  N(L = 8, eps = 1) = 512 N(L = 1, eps = 1); Sierpinski Stufe 8 gegen 10; dyadische Kaestchen.

## 9. Rauchtests (vor dem Einfrieren; Netze, Raster und Groessen kommen in keinem echten Lauf vor, ausser R2 r8)

- **R1** (09:14:36 bis 09:15:01 UTC; rauch/, rauch1.sh, md.py.rauch1): md.py takt (V, S, C15, A15 mit k-Gitter 6^3/4^3,
  Glas N = 128 Saat 901) und kasten mit kleinen Einstellungen, nur Schluessel; kubisch nur Schluessel; bagdim_st
  spektrum st:3 (Bauprobe) und beutel st:4 (k 0..2, nur Konvergenz); beutel st:7 bei Q = 1e5 (ein frischer Start).
  Alle rc = 0.
- **R2** (09:17:29 bis 09:17:44 UTC; rauch2/, rauch2.sh, md.py.rauch2): ganze Kette mit kleinen Einstellungen (k-Gitter
  6^3/4^3, Glas N = 512 Saat 901, drei Kaestchengroessen, Sierpinski Stufe 6, Spektren st:3 und st:4, Beutel st:6
  k 0..20), danach die Auswertung. Alle rc = 0.
  - r8 ist der echte MD1-Lauf (kubisch, deterministisch). Er lief vor dem Einfrieren mit; sein Ergebnis wurde nicht
    angesehen.
- **R3** (09:20:11 bis 09:20:12 UTC): Auswertung des eingefrorenen md.py ueber rauch2/, rc = 0.
- **Gelesen:** nur rc, Laufzeiten, Schluessel und Typen der Ausgaben, Bauproben, Konvergenz, die Matrix-Kontrollen
  (Rest <= 3,1e-15), *0 (keine nicht positiven Eintraege, sum *0/V = 1) und die Strukturwerte von V (Abschnitt 4).
  - Dazu bei r4 (st:7, Q = 1e5, ein frischer Start): nB = 4873, Rg = 40, kompakt, 1042 Iterationen, 20,6 s. Das diente
    der Wahl des Q-Bereichs.
  - Keine Energien, keine Exponenten, keine d_s- oder Steigungswerte.
- **Aenderungen nach R1:** Option --klein (kleine Einstellungen mit voller Ausgabe fuer den Probelauf der Auswertung);
  Sierpinski-Schluessel in der Auswertung variabel.
- **Aenderungen nach R2:**
  - MD2-Spurgrenze von P >= 50/N auf 10/N gesenkt. Grund: Im Probelauf hatte st:4 kein zulaessiges Fenster (nur der Typ
    "null" gesehen). Eine Schaetzung von P(1) ~ 0,04 zeigt, dass 50/N auch bei Stufe 6 nur etwa eine Periode liesse.
  - MD4-Ersatzregel (k-Gitter 2^3, wenn das Gamma-Maximum am Rand liegt).

## 10. Grenzen

- Keine Journaleintraege, keine Peerbus-Nachrichten, keine Aenderungen an Karten oder anderen Runden.
- Code und Plan nach dem Einfrieren unveraendert. Abweichungen werden offen mit Grund und Zeit vermerkt.
- Prozesse nur per PID bzw. Unit. Skripte werden nie in place ueberschrieben (Upload unter neuem Namen, dann mv).
  Zeiten per date. Lokal kein Interpreter.
- Synthetische Modellrechnung, keine Messdatenbestaetigung.

## 11. Pruefsummen beim Einfrieren

- Siehe EINGEFROREN-SHA256.txt (lokal) und EINGEFROREN-SHA256-69.txt (.69). Eingefroren zum dort genannten Zeitpunkt.
