# SKALAR-MISCH-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Start 2026-10-05 09:03:03 CEST (date). Plantext ab 09:39:41 CEST (date), vor jeder Hauptrechnung. Zeitbox 120 min,
  also bis 11:03:03 CEST.
- Grundlage: KARTE.md (SM1 bis SM3 und ihre Bedeutung unveraendert). Karte: Frage, Rechnung, SM1, SM2,
  Ableitbarkeitsprobe, "Kann scheitern" und Abgrenzung sind **woertlich aus dem Vorschlag** (SKALAR-SEKTOR-L,
  Abschnitt 9); SM3 und der Kennzahlen-Abgleich (~1e-5) sind **Zusatz der Leitung**. Diese Trennung gilt auch im Bericht.
- Code: code/inz.py, pn.py, ew.py, tp.py, mn.py, nachtrag_iso.py unveraendert aus IMPULS-NETZ-1 (sha256 e65a5cbf...,
  c8034e40..., fa7b6417..., 419d7da6..., b36984d3..., 1c92cb23...); tti.py aus TT-ISO-1 (6d6b6f7b...) nur als Referenz
  kopiert, nicht importiert. Neu: code/smi.py (importiert die sechs Dateien unveraendert).
- Kennzeichen: [M] eigene Mathematik (vorab), [E] gerechnet, [P] Projektdatei, [ES] eigener Schluss, [F] Festlegung,
  [H] Hypothese. Alles synthetische Gitterrechnung (numpy, 1 Thread), keine Messdaten.

## 0. Zusatz der Leitung 09:2x (woertlich aufgenommen, vor dem Einfrieren eingetroffen)

> Zusatz der Leitung (09:2x), beschreibend und ohne Urteil. Deine Vorhersagen und Bedeutungen bleiben unveraendert.
> - Anlass: TAKT-DYNAMIK-1 (RUNDE-37/takt-dynamik-1/ERGEBNIS.md) fand Folgendes: Beim Delaunay-Umklappen springt die
>   Energie einer Welle um 0,2 bis 0,5 % je Zug. Der Sprung sitzt in der Bewegungsenergie mit J = 1 je Zelle, also
>   gleiche Traegheit unabhaengig von der Groesse. Die Regge-Energie bleibt dabei stetig.
> - Folgerung: Damit zeigen jetzt drei Befunde auf die Bewegungsenergie: deine Leckage, die TT-Anisotropie (TT-GLAS-2)
>   und dieser Energiesprung.
> - Bitte: Wenn es in deiner Zeitbox ohne Verzug der Hauptaufgabe geht, nimm in deine Gewichtsfamilie je Tetraederart
>   einen beschreibenden Punkt auf, die "Hodge-Masse": Bewegungsgewichte aus den umkreisbasierten dualen Massen (z. B.
>   Gewicht je Zelle proportional zu ihrem Volumen bzw. zu den dualen Massen *0 oder *1, wie sie TAKT-UMKLAPP-1 baut).
>   Berichte fuer diesen Punkt TT-Spanne und Bahnlagen-Gang.
> - Form: Den Zusatz nimmst du woertlich als "Zusatz der Leitung 09:2x" in PLAN.md auf, falls er vor dem Einfrieren
>   kommt. Kommt er danach, rechnest du ihn als Nachtrag nach dem Einfrieren und kennzeichnest ihn so.
> - Grenze: Geht es nicht in der Zeitbox, genuegt ein Satz im Bericht.

- Umsetzung [F]: Je Zelle summiert *0 (umkreisbasiert) zum Zellvolumen (TAKT-UMKLAPP-1 K3: Summe *0 = V [P]); je
  Tetraederart ist das also V_t. J ist im Code das Gewicht des Hamilton-Terms (inverse Masse, TT-ISO-1 [P]). Darum zwei
  beschreibende Punkte in F1: **H-a: J_t proportional zu 1/V_t** (Masse proportional zum Volumen, wie die Paarung A2) und
  **H-b: J_t proportional zu V_t** (Gewicht wortgleich "proportional zum Volumen"). Volumina je Art rechnet smi.py
  (Kegel 5/4, Sechseck 3/4 von Finn [P, TT-ISO-1 1.3]). Beschreibend, kein Urteil.

## 1. Begriffe und Messgroessen [F]

- Netz V, Paarung A1R1, Impulskopplung wie IMPULS-NETZ-1 (R1, p = S y + p_J, J' = -M^H sigma, P1-Spannung).
  Kopplungsvektor e_j = (1 - P_c) A p_j; Kopplung einer gleichfoermigen Spannung T an Zweig j:
  g_j(T) = X_j^H [S^H(-sigma(T)) - A_red^-1 S^H A P_M sigma(T)], normiert Gn = g/(omega_j sqrt(C_E)), C_E = 4 V_Z^2/s^2
  (genau wie inz.isotropie und inz.kreisbahnen; dort mit TT-Kopplung 1 + 1,8e-6 [P]).
- Spannungsbasis je Richtung n (ni.basis_tt): h+, hx (TT), L1, L2 (quer-laengs), nn, Ptr (quere Spur).
- **nn-Anteil von e_j je TT-Zweig (Schritt 1):** C_nn,j = abs(Gn_j(nn))^2 und das Verhaeltnis C_nn,j/C_TT,j
  (C_TT,j = Summe ueber h+, hx). Zweigunabhaengig: **tau(n) = Gn_TT^-1 Gn(nn)**, die TT-Spannung, die dieselben
  Zweig-Amplituden erzeugt wie eine Einheits-nn-Spannung (Basis h+, hx). Die Zweige sind bei J_iso fast entartet
  (1e-5), daher ist die Zuordnung "je Zweig" basisabhaengig; tau ist es nicht.
- **200 Richtungen:** pn.richtungen(10, 20) (Gauss-Legendre x gleichmaessig), kl = 0,01, J_iso, mit Impulskopplung.
- **Bahnlagen-Gang:** Mit G(m) = G_rad/G der Kreisbahn mit Normale m (12 Bahnen wie IMPULS-NETZ-1 5.2) und
  G = a + b Summe m_i^4 (kleinste Quadrate ueber die 12 Bahnen) ist **Gang := -b** (IMPULS-NETZ-1: +0,004077).
  - Gang(kl = 0,01): wie inz.kreisbahnen dyn (lineare Zerlegung der Quelle in die 6 Basis-Spannungen, alle Spalten).
  - Gang_0 (langwellig): TT-Kopplung isotrop gesetzt, G = Summe w abs(T_TT + tau T_rest)^2/Summe w abs(T_TT)^2 mit
    statischem tau (weiche Moden von B_red), extrapoliert k -> 0 (s. u.).
- **TT-Spanne:**
  - TT-ISO-1-Definition: max/min - 1 von omega^2/k^2 ueber 13 Richtungen x 2 Zweige x |k| = 1e-3, 2e-3 (kubisch).
  - langwellig (TT-Spanne_0): Masse der zwei weichen Moden in der affinen TT-Basis, Mh = H^-H (V_s^H A_red^-1 V_s) H^-1
    mit H = pinv(S^H a_aff(h+, hx)) V_s; Lagrange-Extrapolation in s^2 aus |k| = 0,01; 0,02; 0,03; 0,04 auf k = 0;
    TT-Spanne_0 = max/min - 1 der Eigenwerte von Mh_0 an den 13 Richtungen. Begruendung: Die TT-Steifigkeit ist
    langwellig exakt isotrop (eichinvariante 2-Ableitungs-Wirkung = linearisierte EH [M/L]; gerechnet Kh_0 = 0,2500000000
    mit Spanne 3,6e-9, Rauchtest r1), die ganze Anisotropie sitzt in Mh.
- **Gewichtsfamilien (kubisch symmetrisch) [F]:** J relativ zu finn_auf = 1, log10 in [-2; 2] wie TT-ISO-1.
  - F1 (Fd-3m, Inversion erhalten): finn_auf = finn_ab, kegel_T1 = kegel_T2, sechs_T1 = sechs_T2: **2 freie Gewichte**.
  - F2 (F-43m, Punktgruppe T_d, weiter kubisch): alle 6 Code-Arten: **5 freie Gewichte**.
  - Nicht gerechnet: die feineren Bahnen unter F-43m (Sechseck-Tetraeder je zwei Bahnen, TT-ISO-1 Plan 1.1 [P]): 7.
  - Gemeinsame Skalierung aller J aendert weder Spanne noch Gang (Verhaeltnisse) [M].

## 2. Ableitbarkeitsprobe und Schreibtisch (vor jeder Hauptrechnung)

### 2.1 Struktur der Mischung [M]

- Kubische Bilinearformen auf symmetrischen Tensoren haben drei Koeffizienten (A1, E_g, T2g). Der Kreuzterm zwischen
  TT(n) und einer aus n gebauten Richtung (nn oder Ptr) ist dann <h_TT, Gamma nn> = (beta_E - beta_T) <h_TT, Lambda_n[D]>,
  D(n) = diag(n_i^2), Lambda_n = TT-Projektion. **Niedrigste Winkelform des nn-Anteils: tau(n) = kappa Lambda_n[D(n)].**
- abs(Lambda_n[D])^2 = 2 s4 - 2 s6 + s4^2/2 - 1/2 (s4 = Summe n_i^4, s6 = Summe n_i^6): null bei [100] und [111]
  (wie C_nn = 0 dort, IMPULS-NETZ-1 5.3), 1/8 bei [110], 0,0512 bei [210], 1/72 bei [211], 0,04628 bei (1,2,3).
- **Abgleich mit [P] (IMPULS-NETZ-1 zusatz.json, mit J, kl 0,01):** C_nn/abs(Lambda[D])^2 = 0,010569 ([110]), 0,010182
  ([210]), 0,010569 ([211]), 0,010569 ((1,2,3)). Also kappa^2 = 0,01057, abs(kappa) = 0,1028; bei [210] (s4 = 0,68)
  3,7 % kleiner: ein hoeherer Winkelanteil ist vorhanden, aber klein [M aus P].

### 2.2 Winkelformel W2 (Schritt 2, vorab festgelegt) [M]

- Mit tau = kappa Lambda_n[D], isotroper TT-Kopplung (Einstein-normiert), Quelle T = eps eps^T (eps = u + i w) und
  exakter Kugelintegration gilt
  **G_W2(m) = 1 + (4/315) kappa^2 + (Summe m_i^4 - 3/5) (5 kappa/126 - kappa^2/819)**, also
  **Gang_W2 = -(5 kappa/126 - kappa^2/819)**.
  - Herleitung: Kreuzterm 2 kappa Re <(n.eps)^2 conj(eps^T Lambda_n[D] eps)> / <abs(Lambda_n[T])^2> mit
    <abs(Lambda_n[T])^2> = 8/5; fuer m = [001] ist der Mittelwert 4/315, also Kreuzterm kappa/63; sein Orientierungsmittel
    ist null (isotroper 4-Tensor, tau TT), also Kreuzterm = (5 kappa/126)(Summe m^4 - 3/5). Quadratterm:
    Orientierungsmittel (1/3)<abs(Lambda[D])^2> = (1/3)(4/105) = 4/315; bei m = [001] 10/819, also Anteil
    -(kappa^2/819)(Summe m^4 - 3/5). Kugelmomente <n_x^2a n_y^2b n_z^2c> = (2a-1)!!(2b-1)!!(2c-1)!!/(2(a+b+c)+1)!!.
- **kappa fuer W2:** reelles kappa aus Schritt 1, gewichtete kleinste Quadrate von tau(n) gegen Lambda_n[D] ueber die
  200 Richtungen (Quadraturgewichte); Imaginaerteil und Restanteil werden berichtet.
- **Vorab ableitbar [M aus P], keine Messung:**
  - abs(kappa) = 0,1028 (aus C_nn([110]) [P]) gibt abs(Gang_W2) = 0,004079 +- 0,000013: **0,0040925 fuer kappa < 0,
    0,0040667 fuer kappa > 0**, gegen 0,004077 [P] (+0,38 % bzw. -0,25 %). Isotroper Anteil (4/315) kappa^2 = 1,342e-4
    gegen 1,3495e-4 [P] (-0,6 %).
  - Der **Betrag** von SM1 ist damit vorab ableitbar (innerhalb 10 %). **Nicht ableitbar ist das Vorzeichen von kappa:**
    Nur kappa < 0 gibt den gemessenen Gang (G(111) > G(001)); mit kappa > 0 hat Gang_W2 das falsche Vorzeichen und SM1
    verfehlt nach Wortlaut. Die Messung (Schritt 1) prueft also das Vorzeichen und die Winkelform an 200 Richtungen.
  - Ebenfalls vorab [M]: **G(m) ist fuer jede Kopplung exakt linear in Summe m_i^4** (Quelle quartisch in eps,
    phasenunabhaengig, kubisch invariant; Grad <= 4 in m). Der Fit "auf etwa 1e-8" in IMPULS-NETZ-1 5.2 ist also
    Algebra, kein Befund.
  - V1 fehlt in der Bahnrechnung (IMPULS-NETZ-1 5.2 [P]); W2 betrifft nur den Spannungskanal mit J.

### 2.3 Klaerung der ~1e-5 aus TT-ISO-1 (Zusatz der Leitung zur Probe): Schreibtisch, dann Rauchtest

- **Schreibtisch [M, mit H]:** Langwellig ist die TT-Masse m(n) = m0 + delta_TT P_E|TT(n) + c(n) Lambda[D] (x) Lambda[D]
  mit c >= 0: delta_TT = E/T2-Unterschied der reduzierten Form, c aus der Kopplung an die eine n-abhaengige
  Luecken-Richtung der Zwangsflaeche (quere Spur, durch c^H p = 0 mit Untergitter-Anteil). Exakte TT-Isotropie
  verlangt **zwei Bedingungen**: delta_TT = 0 und c = 0 (TT-ISO-1 Plan 1.2 zaehlte ebenfalls zwei [P]). c ist ein
  Quadrat; seine Nullstelle ist doppelt, eine Suche nach max/min (Nelder-Mead) bleibt dort leicht stehen.
- **Rauchtests r1 bis r3 (Werte gelesen, weil die Karte diese Klaerung vor dem Plan verlangt) [E]:**
  - J_iso: delta_TT = -6,2e-8, Lambda[D]-Anteil Q([110]) = 1,117e-5 = TT-Spanne_0 1,119e-5 (TT-ISO-1-Definition
    1,127e-5, wie TT-ISO-1 1,12e-5 [P]). Der Rest von J_iso ist also ganz der c-Term, nicht delta_TT.
  - Entlang der Kurve delta_TT = 0 in F1 (Ast durch J_iso) faellt Q monoton zu kleineren Kegel-Gewichten:
    1,10e-5 bei log10 J_Kegel = -1,05; 3,34e-6 bei -1,35 (log10 J_Sechseck = 0,038). Auf den anderen Aesten Q >= 1,5e-4.
    Eine Nullstelle von Q bei endlichen Gewichten fand der Rauchtest nicht.
  - LM ab J_iso auf der vollen 13-Richtungen-Spanne kriecht (2 % je Schritt, 80 Schritte: 1,12e-5 -> 5,9e-6).
- **Antwort (vor dem Plan):** Die 1,1e-5 sind **weder ein Rundungsrest noch ein fester Boden der Familie F1**.
  TT-ISO-1 stand auf der Kurve delta_TT = 0 an einer Stelle mit c-Term 1,1e-5; F1 senkt ihn weiter, aber nur in Richtung
  immer traegerer Kegel (J_Kegel -> 0); eine exakte Loesung bei endlichen Gewichten zeigt der Rauchtest in F1 nicht
  [E, Rauchtest]. **Folge fuer SM3 [ES]:** In F1 ist eine exakte Loesung nicht zu erwarten; offen bleibt F2.
- **Genauigkeitsboden (Rauchtest r1) [E]:** Mh_0 an Symmetriebildern gleich auf 1,5e-15 ([100]), 1,5e-14 ([111]),
  2,9e-11 (allgemeine Richtung); 3- gegen 4-Punkt-Extrapolation 1,3e-12; Im(Mh_0) 3,4e-12. **Die langwellige
  TT-Spanne ist also nur auf etwa 3e-11 aufloesbar**, die Schranke 1e-12 von SM3 liegt darunter (Regel in 5).

### 2.4 Zaehlung (vorab) [M, H]

| | F1 (Fd-3m) | F2 (T_d) |
|---|---|---|
| freie Gewichte | 2 | 5 |
| Bedingungen TT-Isotropie (langwellig) | 2 (delta_TT, c) | 2 |
| Bedingung Gang = 0 (niedrigste Ordnung) | 1 (kappa = 0; Gang_W2 = 0 nur bei kappa = 0 oder kappa = 32,5) | 1 |
| Summe | 3 > 2: generisch keine gemeinsame Loesung | 3 <= 5: generisch eine 2-dimensionale Schar, **falls** c bei endlichen Gewichten null werden kann |

- Vorbehalt [H]: Bei J_iso haben TT-Rest (c Lambda[D] (x) Lambda[D]) und nn-Anteil (kappa Lambda[D]) dieselbe
  Winkelform. Haben beide eine Ursache, sind es nur zwei Bedingungen. Das prueft die Rechnung (Kurve und Ableitungen),
  es geht in kein Urteil ein.
- **Nicht ableitbar:** ob c in F2 bei endlichen positiven Gewichten verschwindet; ob dort zugleich Gang = 0; ob die
  Loesung stabil ist; ob der nn-Anteil allein den Gang traegt (prueft W1, s. 3).

## 3. Rechnung (smi.py)

- **Schritt 1 (tabelle):** 200 Richtungen, kl = 0,01, J_iso: omega^2/k^2 je Zweig, C_TT,j, C_nn,j, Verhaeltnis,
  tau(n) (Re, Im), Lambda_n[D], C_L, C_Ptr; benannte Richtungen [110], [210], [211], (1,2,3), [100], [111]; kappa
  (Fit, Imaginaerteil, Restanteil), kappa je Richtung gegen s4 (beschreibend).
- **Schritt 2:** G(m) der 12 Bahnen: [P]-Werte (IMPULS-NETZ-1 lauf-69/zusatz.json, dyn_J_iso), neu exakt (Tabelle),
  Kontrolle inz.kreisbahnen (eingefroren, unveraendert aufgerufen), **W2 (Formel 2.2, primaer)**, W2 per Quadratur
  (Kontrolle der Formel), **W1** (tau aus der Tabelle, nur nn-Spalte, beschreibend: traegt der nn-Anteil allein?).
- **Schritt 3 (suche, karte):**
  - J_iso und die Hodge-Punkte H-a, H-b (Zusatz 09:2x): alle Kennzahlen (beschreibend).
  - F1: Kurve delta_TT = 0 (Ast durch J_iso), log10 J_Kegel = -2 ... -0,3 in 18 Schritten, log10 J_Sechseck per
    Halbierung (50 Schritte); je Punkt alle Kennzahlen. Dazu LM ab J_iso auf das kompakte Residuum
    r = (delta_TT, sqrt(Q), Q-Nebendiagonale, Gang_0) (wurzelgezogenes Q, damit die doppelte Nullstelle zur einfachen
    wird; 25 Schritte, zentrale Differenzen h = 1e-6).
  - F2: Ableitungen von (delta_TT, Q, Nebendiagonale, Gang_0) nach den 5 log-Gewichten bei J_iso (zentral, h = 1e-4);
    LM auf dasselbe Residuum aus 3 Starts: J_iso, TT-ISO-1-Bestwahl alle Arten (0,829; 9,78; 99,8; 31,9; 0,049),
    J_iso + Zufall (Saat 5, +-0,2 Dekaden); je 25 Schritte, je hoechstens 150 s.
  - Stabilitaet (511 k, L = 8 wie TT-ISO-1): A_red und B_red positiv definit, kleinstes omega^2/groesstes, fuer J_iso,
    jeden LM-Endpunkt und den Kurvenpunkt mit kleinster TT-Spanne.
  - Karte F1 (fuer das Bild, beschreibend): 31 x 31 in log10 J_Kegel in [-2; 1], log10 J_Sechseck in [-1,5; 1,5]:
    TT-Spanne_0 und Gang(kl = 0,01).
- **Bild (auf der .69):** F1-Karten (TT-Spanne, Gang) mit Kurve und Suchwegen, LM-Verlaeufe, Kennzahlen entlang der
  Kurve gegen log10 J_Kegel, 12 Bahnen mit W2.

## 4. Kontrollen

- KA: Summe_t J_t A_t gegen pn.A_J (Rauchtest r1: 4,4e-16).
- KB: G(m) neu (Tabelle) gegen [P] und gegen inz.kreisbahnen: Soll <= 1e-9.
- KQ: W2-Formel gegen W2-Quadratur (200 Richtungen): beschreibend (Quadraturfehler).
- KL: C_L und C_Ptr mit J klein (IMPULS-NETZ-1: <= 6e-11 bzw. 1,6e-13 [P]).
- KR: Rang [M, c] = 40 an allen Richtungen.

## 5. Urteilsregeln (mechanisch in smi.py urteil)

- **SM1** ([H] die Winkelformel aus Schritt 2 trifft den Koeffizienten 0,004077 auf 10 %):
  - Nach Kartenwortlaut: abs(Gang_W2/0,004077 - 1) <= 0,10 (Gang_W2 aus Formel 2.2 mit kappa aus Schritt 1;
    Vorzeichen zaehlt).
  - Nach Plan: dazu an allen 12 Bahnen abs(G_W2(m) - G_P(m)) <= 0,1 x 0,004077 x 2/3 = 2,72e-4 (10 % des Gang-Hubs
    zwischen Summe m^4 = 1/3 und 1). Verfehlt KB (> 1e-9): nicht entscheidbar.
- **SM2** ([H] Gewichte mit TT-Spanne < 1e-6 und Bahnlagen-Gang < 1e-5):
  - Nach Kartenwortlaut: es gibt einen gerechneten Gewichtssatz (F1 oder F2, im Bereich, A_red an den gerechneten k
    positiv definit) mit TT-Spanne (TT-ISO-1-Definition) < 1e-6 und abs(Gang(kl = 0,01)) < 1e-5.
  - Nach Plan: derselbe Satz zusaetzlich stabil an den 511 k und mit TT-Spanne_0 < 1e-6, abs(Gang_0) < 1e-5.
- **SM3** (Zusatz der Leitung; [H] TT-Spanne und Gang beide < 1e-12, exakte Loesung):
  - Nach Kartenwortlaut: es gibt einen gerechneten Satz mit TT-Spanne_0 < 1e-12 und abs(Gang_0) < 1e-12.
  - Nach Plan: dazu stabil an den 511 k. Liegt der kleinste gefundene Wert max(TT-Spanne_0, abs(Gang_0)) unter
    1e-10 (drei mal Boden 2,9e-11), aber nicht unter 1e-12: **nicht entscheidbar (Rechengenauigkeit)**; liegt er
    darueber: verfehlt.
- "Es gibt" heisst: unter den gerechneten Saetzen (J_iso, Hodge-Punkte, Kurvenpunkte, LM-Endpunkte). Eine erfolglose
  Suche ist kein Beweis der Nichtexistenz; Bericht sagt das.
- Bedeutung der Ausgaenge: wie auf der Karte; nichts daran geaendert.

## 6. Agenten-Erwartungen (vorab; kein Kartenurteil)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| Z1 | KB: G neu gegen [P] <= 1e-9 | 90 % |
| Z2 | kappa < 0 (SM1 nach Wortlaut trifft ein) | 65 % |
| Z3 | Restanteil von tau gegen kappa Lambda[D] <= 10 % | 70 % |
| Z4 | F2-LM erreicht TT-Spanne_0 < 1e-6 und abs(Gang_0) < 1e-5 zugleich | 30 % |

## 7. Laeufe (.69, kleintest.sh, Spuren cpu5 und cpu6, 1 Thread, <= 600 s)

- Arbeitsordner /home/fmh/fmhc-physics-remote/skalar-misch-1/; Code nach dem Einfrieren in code/ (neuer Ordner, scp, nie
  in place). Rauchtests liefen aus code-r1 bis code-r4 (r1 bis r3 Werte gelesen, s. 2.3; r4a bis r4f nur Rueckgabewert).

| Lauf | Spur | Aufruf | Schaetzung |
|---|---|---|---|
| T1 | cpu5 | smi.py tabelle --out lauf/tabelle.json | < 30 s |
| S1 | cpu6 | smi.py suche --fam F1 --out lauf/suche-F1.json | 2 bis 4 min |
| S2 | cpu5 | smi.py suche --fam F2 --out lauf/suche-F2.json | 6 bis 9 min |
| K1 | cpu6 | smi.py karte --out lauf/karte.json | 2 bis 3 min |
| UR | cpu6 | smi.py urteil --tabelle lauf/tabelle.json --suche lauf/suche-F1.json lauf/suche-F2.json --out lauf/urteile.json | < 5 s |
| BI | cpu6 | smi.py bild ... --bild lauf/bild-skalar-misch.png --out lauf/bild.json | < 10 s |

- Bricht S2 an der Laufzeit ab: einmal mit weniger Starts (gekennzeichnet). Kein neuer Lauf nach 10:50 CEST.
