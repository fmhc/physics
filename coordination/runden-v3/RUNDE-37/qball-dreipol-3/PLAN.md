# QBALL-DREIPOL-3: Plan (Code-Agent, Runde 43, Fast Lane)

- Code-Agent fuer claude-primary. Start 2026-10-04 19:07:16 CEST (date). Plantext begonnen 19:24:01 CEST (date).
- Zeitbox 90 min, also bis 20:37:16 CEST.
- **Reihenfolge offen gelegt:** Code zuerst, dann ein Leitungstest und eine Laufzeitprobe auf der .69, beide nur mit
  fremdem g4 = +0,1 (Abschnitt 9). Hauptwerte (g4 = -0,1) habe ich nicht gerechnet und nicht gesehen.
- **Grundlagen [P]:**
  - KARTE.md: Fragen, Vorhersagen DR0 bis DR2, Wahrscheinlichkeiten und Bedeutung unveraendert.
  - QBALL-DREIPOL-2: ERGEBNIS.md, PLAN.md, code/ (dreipol2.py eingefroren 20261004-182806), lauf-69/ mit Nachtrag N1
    (3D, Q1 = 200/400/800) und N2; QBALL-DREIPOL-1 nur ueber DREIPOL-2.
  - AGENTS.md, Regel Dimensionsvergleich (2D und 3D getrennt ausweisen; ueber KARTE.md und DREIPOL-2).
- **Kennzeichen:** [M] Mathematik, [E] gerechnet im Modell, [P] Projektdatei, [L] Literatur, [H] Hypothese.
- Alles ist eine synthetische Rechnung im Modell, **keine Messdatenbestaetigung**.

## 1. Modell und Code (unveraendert aus QBALL-DREIPOL-2)

- Drei komplexe Komponenten, V = U(S) + g4 sum_a |phi_a|^4, U(S) = S - S^2 + S^3/2, S = sum_a |phi_a|^2; U(1)^3.
- Fluss bei festen Ladungen Q_a (E_Q = W + sum_a Q_a^2/(2 Lam_a)), halbimplizit, tau = 0,5, c = 1; spektral,
  periodisch; torch/CUDA float64 (kein CPU-Fallback); radialer Bezug tridiagonal auf der CPU.
- **code/dreipol2.py** ist die eingefrorene Datei aus DREIPOL-2, Byte fuer Byte kopiert (sha256 gleich), und wird nur
  importiert. Einpolball, Mischball (Start: radialer Ball mit g_eff = g4/3), beruehrendes Dreieck (d0 = 2R, Ecken
  90/210/330 Grad), Paarabstaende, Reinheit (Voronoi), Kabsch-Abstand: alles von dort.
- **Neu (code/dreipol3.py):** nur Ablaeufe: Bisektion mit Ableitbarkeitsprobe je Schritt, Sektorstart, Radien,
  3D-Stoerungen. **code/auswertung3.py:** Urteile, Tabellen, Bilder.

## 2. Ableitbarkeitsprobe (vor den Hauptlaeufen)

1. **Pflichtprobe je Lauf (Karte), mechanisch im Lauf und vor dem Fluss:** Jeder Bisektionsschritt rechnet erst
   Einpolball, Mischball (3 Q1) und E_Tropfen, dann die Startenergie E_start des beruehrenden Dreiecks. Die Zeile
   "vorab" (mit Zeitstempel) wird geschrieben, **bevor** der Fluss vom beruehrenden Dreieck beginnt.
   - **Erzwungen** heisst: E_start < E_Misch (Verschmelzen unerreichbar) oder E_start < E_Tropfen (Tropfen
     unerreichbar). Der Fluss senkt E monoton.
   - Ein erzwungener Schritt zaehlt nur als Kontrolle. Die Bisektion **endet** dort; die Klammer bleibt beim letzten
     gueltigen Stand.
   - **E_Tropfen** kommt aus einem eigenen Fluss vom **Sektorstart** (Abschnitt 4): radiales Mischballprofil 3 Q1,
     in drei Farbsektoren um die z-Achse geteilt. Endet dieser Fluss im Tropfen, ist E_Tropfen sein Endwert; sonst
     gibt es "keinen Tropfen vom Sektorstart" und die Probe laeuft nur gegen E_Misch.
   - Liegt schon der Sektorstart unter E_Misch, ist dieser Hilfslauf selbst erzwungen. Sein Endpunkt bleibt ein
     Fixpunkt; die Auswertung vermerkt das.
   - Bekannte Werte [P, DREIPOL-2 N1 und A.json]: 3D Q1 = 400: E_start - E_Misch = +33,94; Q1 = 800: +32,94
     (E_Tropfen 3,32 unter E_Misch). 2D Q1 = 60: E_start 141,83, E_Misch 138,98, Tropfen 138,835. Fuer diese drei
     Kontrollen ist kein Start erzwungen.
2. **DR0 ist Nachbau:**
   - 3D Q1 = 800 laeuft mit denselben Argumenten wie N1 (N = 80, L = 48). Erwartet ist der N1-Wert bitnah; das ist
     Kontrolle, kein Befund.
   - 2D Q1 = 60 laeuft wie der DREIPOL-2-Nachbau (N = 256, L = 64, Fluss bis 1e-7).
   - 3D Q1 = 400 lief in N1 mit L = 40 (h = 0,5). Hier laeuft es mit L = 48 (h = 0,6) wie alle 3D-Schritte.
3. **DR1:**
   - P1/P2 (gleichfoermiger Phasenversatz) sind exakte Symmetrien (U(1)^3), wie DREIPOL-2 Plan 2.2: vorab ableitbar.
   - L1/L2 sind eine Symmetrieklasse (D3 x S3, DREIPOL-2 Plan 2.4); das gilt in 3D ebenso.
   - Nullmoden in 3D: drei Verschiebungen, drei Drehungen. "Endabstand" misst daher nur die Form (Abschnitt 5).
   - Nicht ableitbar: das Hesse-Spektrum ausserhalb des Unterraums. Neu in 3D ist die Richtung aus der Ebene: Der
     symmetrische Fluss in DREIPOL-2 hat die Spiegelung z -> -z erhalten.
   - Energetisch erzwungen ist die Rueckkehr nicht: Auch wenn der gestoerte Start unter E_Misch liegt, bleiben
     andere Endzustaende moeglich. Die Auswertung vermerkt je Stoerung, ob der Start unter E_Misch lag.
4. **DR2 im Kartenwortlaut ist weitgehend vorab ableitbar [M]:**
   - Bei duenner Wand ist die Ladungsdichte im Inneren eines einfarbigen Gebiets fast unabhaengig von Q. Dann gilt
     Q ~ R^D, und der Tropfen mit Gesamtladung 3 Q1 hat R_Tropfen/R_1(Q1) = 3^(1/D).
   - Das sind 1,732 in 2D und 1,442 in 3D, Verhaeltnis 1,201. Das liegt schon innerhalb von 30 %, gleich wo die
     Schwelle liegt.
   - Dicke Waende verschieben das; das Urteil ist also nicht ganz festgelegt, aber stark vorgespannt.
   - Mit dem Einpolball gleicher **Gesamt**ladung (3 Q1) waere das Verhaeltnis bei duenner Wand sogar ~1 in beiden
     Dimensionen.
   - **Darum:** Das Planurteil zu DR2 nutzt R* **absolut** (Laengeneinheit 1/m). Der Kartenwortlaut (normiert)
     laeuft getrennt, mit dem Vermerk "weitgehend vorab ableitbar".
   - Was die Duennwand-Formel absolut sagt [M, Modellrechnung, H]: Drei Keilsektoren mit Grenzspannung sigma und
     Volumengewinn Delta je Volumen ergeben R* = c_D sigma/Delta.
     - 2D: drei Grenzlinien der Laenge R gegen die Flaeche pi R^2, also c_2 = 3/pi = 0,955.
     - 3D: drei Halbscheiben 3 pi R^2/2 gegen das Volumen 4 pi R^3/3, also c_3 = 9/8.
     - Bei gleichem sigma/Delta waere R*_3D/R*_2D = 1,18. Die Aussenflaeche (rein gegen gemischt) ist dabei nicht
       mitgezaehlt.
     - sigma und Delta haengen von om an der Schwelle ab; om an der Schwelle ist in 2D und 3D nicht vorab bekannt.
       Das absolute Urteil ist daher **nicht** ableitbar.
5. **Drei Schwellbegriffe:**
   - (a) Ausgang des Flusses vom beruehrenden Dreieck. Das ist der Kartenauftrag und die Hauptgroesse der Bisektion.
   - (b) Existenz eines Tropfens vom Sektorstart (beschreibend, aus denselben Schritten).
   - (c) Energiekreuzung E_Tropfen = E_Misch (beschreibend).
   - Urteile nutzen nur (a). (a), (b) und (c) koennen verschieden liegen; der Fluss bei festen Ladungen findet das
     Becken seines Starts, nicht das globale Minimum.

## 3. Numerik

**3D (Teil A 3D und Teil B):**
- N = 80, L = 48 (h = 0,6) fuer alle 3D-Schritte, wie DREIPOL-2 Hauptlauf und N1 bei Q1 = 800.
  - Gitterprobe DREIPOL-2 r2 [P]: Einpolball Q = 2500, N = 80 gegen 128: 2,3e-9 relativ.
  - Bei Q1 = 400 ist die Wand dicker (om = 0,794). Ein spektrales Gitter wird dadurch eher genauer.
- Kasten: Mischball 3 Q1 = 2400 hat R_halb 6,75 [P]; das beruehrende Dreieck bei Q1 = 800 reicht bis ~2 (rho + R) =
  4,31 R = 19 < 24.
- Einpolball und Mischball: Toleranz 1e-6, hoechstens 20000 Schritte bzw. 90 s (wie DREIPOL-2 Teil B).
- Fluesse: Toleranz 1e-6 (wie DREIPOL-2), hoechstens 60000 Schritte bzw. **75 s je Fluss**.

**2D (Teil A 2D):**
- N = 256, L = 64 (h = 0,25), wie DREIPOL-1/-2.
- Einpolball und Mischball mit den Vorgaben aus DREIPOL-2 Teil A (Toleranz 1e-8, 6000 Schritte, 120 s).
- Fluesse: Toleranz 1e-7 (wie der Nachbau in DREIPOL-2), hoechstens 60000 Schritte bzw. **45 s je Fluss**.
- Bei Q1 = 15 bis 30 werden die Baelle dicker (om naeher an 1). L = 64 nehme ich ohne eigene Probe als ausreichend an
  [H]; der Rand liegt 32 vom Mittelpunkt.

**Laufzeitprobe** (rauch-69/zeit/, fremdes g4 = +0,1, Hauptgroesse; Abschnitt 9) [E]:
- 3D N = 80: 6,7 ms je Flussschritt mit Beobachter, Stoerungsfluss 7,3 ms.
- 2D N = 256: 1,29 ms je Flussschritt.
- Einheitenlaufzeit 18 bis 24 s bei 2 x 1000 Schritten (3D) bzw. 2 x 3000 Schritten (2D); Einheitenstart ~3 s.
- **Obergrenzen je Einheit:**
  - Keine neue Bisektionsstufe nach 330 s Rechenzeit.
  - Ein 3D-Schritt (zwei Fluesse) dauert hoechstens ~155 s, also endet die Einheit nach hoechstens ~490 s.
  - Teil B: keine neue Stoerung nach 420 s, ein Stoerungsfluss hoechstens 60 s, also hoechstens ~500 s.
  - Alles liegt unter RuntimeMaxSec 600 von kleintest.sh.

## 4. Parameter und Bisektionsregel (vorab gebunden)

**Teil A, Schwelle (g4 = -0,1):**
- **3D:** obere Klammer Q1 = 800 (Kontrolle), untere Klammer Q1 = 400 (Kontrolle), dann **6 Halbierungen**
  (Endbreite 6,25).
- **2D:** obere Klammer Q1 = 60 (Kontrolle). Abstieg Q1 = 30, 20, 15 bis zum ersten Verschmelzen; jeder Tropfen
  senkt die obere Klammer. Dann **6 Halbierungen**.
- **Je Schritt in dieser Reihenfolge:**
  1. Einpolball Q1 (R = R_halb) und Mischball 3 Q1, je radial und auf dem Gitter
  2. Sektorstart und Fluss bei festen Ladungen (Q_a = Q1), daraus E_Tropfen
  3. beruehrendes Dreieck d0 = 2R, E_start, Zeile "vorab" (Abschnitt 2.1)
  4. Fluss vom beruehrenden Dreieck
- **Ausgang eines Flusses:**
  - **Tropfen:** konvergiert, Gestalt "Dreieck" (kleinster Paarabstand > R) und Reinheit jeder Farbe >= 0,5.
  - **verschmolzen:** konvergiert und groesster Paarabstand < 0,25 R. Das ist die Gestaltregel aus DREIPOL-2.
  - **sonst offen** (auch: nicht konvergiert, gleich welche Gestalt).
- **Bisektionsregel:**
  - Tropfen: Q_hi = Q.
  - verschmolzen: Q_lo = Q.
  - offen oder erzwungen: Abbruch; die Klammer bleibt.
  - Klammer am Ende [Q_lo, Q_hi], Schwelle Q1* = Mitte, Halbbreite angeben.
  - Bricht schon die obere Klammer (kein gueltiger Tropfen) oder findet der 2D-Abstieg bis 15 kein Verschmelzen, gibt
    es keine Klammer.
- **Sektorstart:**
  - Profil f(r) des radialen Mischballs (3 Q1, g_eff = g4/3).
  - psi_a = f(r) sqrt(w_a) mit w_a = softmax_b(beta x.e_b)_a, e_b in Richtung 90/210/330 Grad (Ebene x-y), beta = 1,5.
  - Die Farben teilen sich glatt; in der Mitte ist das Feld gemischt, die Summe der w_a ist 1.

**Teil B, Stabilitaet 3D:** Q1 = 800, g4 = -0,1, N = 80, L = 48.
- **Referenz:** Fluss vom beruehrenden Dreieck bis 1e-6 (wie N1), dann weiter bis 1e-9 (hoechstens 20000 Schritte
  bzw. 90 s). R = R_halb des Einpolballs Q1 = 800.
- **Stoerungen (Urteil), Groessen wie DP1:**
  - **V1:** Pol 1 (Farbe 1, Ecke 90 Grad) um 0,15 R tangential (+x) und zusaetzlich 0,15 R aus der Ebene (+z).
  - **V2:** Pol 2 um 0,15 R radial nach aussen (in der Ebene) und zusaetzlich 0,15 R aus der Ebene (+z).
  - **L1:** 5 % der Farbe 2 aus Klumpen 2 nach Klumpen 1, gleichphasig (psi_2 -> sqrt(0,95) psi_2 + sqrt(0,05)
    psi_2 verschoben). Alle Q_a bleiben 800 (Fluss bei festen Ladungen).
  - **L2:** 5 % der Farbe 1 aus Klumpen 1 nach Klumpen 2.
  - **P1:** Phase von Komponente 2 um pi/2. **P2:** Phasen von Komponente 2 und 3 um 2 pi/3 und 4 pi/3.
- **Beschreibend, ohne Urteil:**
  - **Z1:** Pol 1 nur um 0,15 R aus der Ebene.
  - **R5, R20:** glattes komplexes Rauschen (k_c = 2) auf allen Komponenten, 5 % (Saat 11) bzw. 20 % (Saat 12) der
    lokalen Feldstaerke, wie DREIPOL-2 N2.
- Stoerungsfluesse bis Residuum < 1e-8, hoechstens 30000 Schritte bzw. 60 s je Stoerung.

**Teil C, Schwellradius:**
- **R*** = Ersatzradius R_eq des Tropfens (Ende vom beruehrenden Dreieck) am oberen Klammerende Q_hi. Das ist das
  kleinste Q1 mit gueltigem Tropfen; es wird nicht interpoliert.
- **R_eq:** int S dV = S_max Omega_D R_eq^D, mit Omega_2 = pi und Omega_3 = 4 pi/3. Glatt, fuer jede Gestalt
  definiert; bei duenner Wand gleich dem Radius.
- **Normiert:** R*_norm = R_eq(Tropfen)/R_eq(Einpolball Q_hi).
- **Beschreibend:**
  - R_vol (Gebiet S > S_max/2 als Kugel bzw. Scheibe)
  - R_rms
  - R_halb des Einpolballs
  - om an der Schwelle

## 5. Messgroessen

- **Je Bisektionsschritt:**
  - E_1 (Gitter, radial), om, R_halb und Radien des Einpolballs
  - E_Misch (Gitter, radial) und Radien
  - 3 E_1
  - die Zeile "vorab": E_start, E_Misch, E_Tropfen, Differenzen, erzwungen ja/nein
  - fuer beide Fluesse: Status, Schritte, E am Ende, Paarabstaende/R, Reinheit, Gestalt, Ausgang, Radien und
    Verlauf (alle 50 Schritte: E, Residuum, Paarabstaende, Reinheit)
  - Bilder: Startfeld, beide Endfelder (3D: Ebene z = 0)
- **Teil B, je Stoerung:**
  - Start und Ende: E - E_ref, Residuum, Schwerpunkte, Paarabstaende
  - **d_form** = max_ab abs(D_ab - D_ab,ref)/R
  - **d_rms** = RMS-Abstand der drei Schwerpunkte zum Referenzdreieck nach bester Verschiebung und Drehung (Kabsch
    in 3D, ohne Spiegelung), durch R
  - Reinheit
  - Bilder: Ebene z = 0 und Seitenansicht (Projektion ueber y)

## 6. Urteilsregeln (vorab, in Zahlen; Code: code/auswertung3.py)

| Nr | Plan (Hauptregel) | Kartenwortlaut |
|---|---|---|
| DR0 | **Eingetroffen**, wenn alle drei Teile halten. 3D Q1 = 800: Ausgang Tropfen und E_Misch,Gitter - E_Ende = 3,32 +- 0,1. 3D Q1 = 400: Ausgang verschmolzen. 2D Q1 = 60: Ausgang Tropfen, max_ab abs(D_ab/R / 1,245 - 1) <= 0,02 und abs(Luecke/0,146 - 1) <= 0,10 (DP0-Regel). **Nicht eingetroffen**, wenn ein Teil mit gueltigem Ausgang (Tropfen/verschmolzen) verfehlt; sonst nicht auswertbar | gleich (Kartenwortlaut ist schon in Zahlen; "wie DREIPOL-2" = DP0-Regel) |
| DR1 | Je Stoerung V1, V2, L1, L2, P1, P2 drei Faelle. **"zurueck":** Fluss konvergiert (Residuum < 1e-8), d_form < 0,02, d_rms < 0,02 und abs(E_Ende - E_ref) < 1e-3. **"nicht zurueck":** konvergiert, aber nicht zurueck; oder E_Ende < E_ref - 1e-3; oder nicht konvergiert mit d_rms am Ende > d_rms am Start. **Sonst "offen".** Eingetroffen, wenn alle sechs "zurueck"; nicht eingetroffen, wenn eine "nicht zurueck"; sonst nicht auswertbar | je Stoerung am Flussende (gleich welcher Status): d_rms < 0,02 R und abs(E_Ende - E_ref)/E_ref < 1e-3. Eingetroffen, wenn alle sechs; sonst nicht eingetroffen |
| DR2 | **R* absolut** (R_eq des Tropfens bei Q_hi, Laengeneinheit 1/m), 2D gegen 3D: **eingetroffen** bei max/min <= 1,3, sonst **nicht eingetroffen**. **Nicht auswertbar**, wenn in einer Dimension keine Klammer besteht, das obere Ende kein gueltiger Tropfen ist oder (Q_hi - Q_lo)/Q_hi > 0,10 | **R* normiert** (R_eq Tropfen / R_eq Einpolball gleicher Ladung Q1 = Q_hi), sonst gleich. Vermerk: weitgehend vorab ableitbar (2.4) |

- **Mechanische Vermerke:**
  - "P1/P2 vorab ableitbar; L1/L2 eine Klasse"
  - je erzwungener Schritt "nur Kontrolle"
  - je erzwungener Sektorlauf ein Hinweis
  - je Stoerung "Start unter E_Misch" (ja/nein)
  - "DR2 normiert weitgehend vorab ableitbar (3^(1/D))"
- **Nur beschreibend:** Z1, R5, R20; Schwellen (b) und (c); R_vol, R_rms; om an der Schwelle; Klammern selbst
  (Q1*(3D), Q1*(2D)); alles aus Sektorlaeufen.
- Die Zahlen der Bisektion beantworten die erste Kartenfrage direkt (Klammer je Dimension). Dafuer gibt es keine
  Vorhersage mit Wahrscheinlichkeit, also kein Urteil.

## 7. Laeufe (.69, kleintest.sh, Spuren p4000a und p4000b, GPU)

| Spur | Lauf | Inhalt | Obergrenze |
|---|---|---|---|
| p4000a | bisekt3 | Teil A 3D: Kontrollen 800, 400, 6 Halbierungen | ~490 s |
| p4000b | bisekt2 | Teil A 2D: Kontrolle 60, Abstieg 30/20/15, 6 Halbierungen | ~430 s |
| p4000b | stab3 | Teil B: Referenz und 9 Stoerungsfluesse (6 mit Urteil) | ~500 s |

- Laufskripte code/laeufe-p4000a.sh, code/laeufe-p4000b.sh. Danach die Auswertung: kleintest.sh p4000a dp3-aw
  code/auswertung3.py lauf (< 1 min).
- Ausgaben auf der .69 unter /home/fmh/fmhc-physics-remote/qball-dreipol-3/lauf/, danach per scp nach lauf-69/.
- **Start:** Skripte erst per scp/mv an ihren Platz, Hashes pruefen, **danach** starten (eigener Befehl). Der
  Hintergrundstart ohne "cd && ... &", damit kein ssh offen bleibt (Abschnitt 9).
- Jede Einheit: CPUQuota 100 %, MemoryMax 4G, RuntimeMaxSec 600 (kleintest.sh).

## 8. Erwartungen des Agenten (vorab, ohne Urteil)

- **E0:** DR0 trifft ein (95 %); die beiden Nachbauten sind bitnah, Q1 = 400 verschmilzt auch bei h = 0,6.
- **E1:** Unsicher. Die Keilaufteilung hat weniger innere Flaeche als Schichten (3 pi R^2/2 gegen ~5,8 R^2 fuer zwei
  Schnitte), also erwarte ich keine Umlagerung aus der Ebene. Zugleich liegt der Tropfen nur 0,17 % unter dem
  Mischball und kann weich sein. Rueckkehr: 60 %.
- **E2:** Ich erwarte Q1*(3D) zwischen 500 und 700 und Q1*(2D) zwischen 30 und 55.
  - R* absolut ~5 bis 6 in beiden Dimensionen, also Plan-DR2 50 %.
  - Normiert erwarte ich wegen der Geometrie "eingetroffen" (85 %).

## 9. Leitungstest und Laufzeitprobe (vor dem Einfrieren; fremde Werte)

- **Leitungstest** (rauch-69/pipe/, 17:19:15 bis 17:19:50 UTC, code/pipe-test.sh):
  - Alle Modi mit fremden Werten (g4 = +0,1, 3D N = 32, 2D N = 64, 20 bis 40 Schritte) und die Auswertung liefen
    durch, alle rc = 0, ohne Traceback.
  - Gelesen habe ich Rueckgabecodes, Laufzeiten, die Bildvermerke, ein Testbild und die Urteilsfelder der
    Testauswertung. Diese sind ohne Bedeutung (Fremdwerte, Fluesse nicht konvergiert).
- **Zweiter Auswertungstest** (rauch-69/pipe2/):
  - Dieselben Testdaten, mit jq eine kuenstliche Klammer gesetzt (2D 24/25, 3D 790/800, Ausgang "Tropfen"). So laeuft
    auch der DR2-Zweig und das Klammerbild einmal.
  - Danach kam der Vermerk "Start unter E_Misch" (Teil B) in auswertung3.py; die neue Fassung lief in diesem Test.
- **Laufzeitprobe** (rauch-69/zeit/, 17:21:42 bis 17:22:48 UTC, code/zeit-test.sh): Hauptgitter, g4 = +0,1, feste
  Schrittzahlen (Abschnitt 3).
- **ssh-Befund:** Der Start mit "cd X && nohup setsid ... &" hielt die ssh-Sitzung bis zum Ende des Tests offen
  (zweimal, ~35 s und ~66 s). Ursache ist die Unterschale von "&&" im Hintergrund. Fuer die Hauptlaeufe starte ich
  ohne "&&" (geprueft mit sleep: Rueckkehr sofort).

## 9a. Lesarten und Abweichungen von der Karte (vor dem Einfrieren begruendet)

1. **E_Tropfen vor jedem Lauf:** Die Karte nennt keinen Weg. Ich nehme den Fluss vom Sektorstart (2.1); er laeuft im
   selben Schritt vor dem Hauptfluss. Gibt es keinen Tropfen vom Sektorstart, pruefe ich nur gegen E_Misch.
2. **2D "nach unten ab Q1 = 60":** Abstieg 30, 20, 15 bis zum ersten Verschmelzen, dann Halbierung. Die Karte nennt
   keine untere Klammer.
3. **Stoerungen in 3D "wie DP1":** Die Groessen (0,15 R, 5 %) und Arten sind wie DP1. V1 und V2 bekommen zusaetzlich
   0,15 R aus der Ebene, weil der symmetrische Unterraum in 3D auch die Spiegelung z -> -z enthaelt. Sonst laege
   keine der sechs Stoerungen ausserhalb dieser Spiegelung (P1/P2 und L1/L2 erhalten sie).
4. **"Endabstand < 2 % R":** Formabstand (d_form und d_rms nach Kabsch) wie DP1, R = R_halb des Einpolballs
   Q1 = 800. **"Energie gleich auf 1e-3":** Plan absolut, Kartenwortlaut relativ, wie DP1.
5. **R*:** Plan absolut (Begruendung 2.4), Kartenwortlaut normiert mit dem Einpolball Q1 ("Einpol-Radius gleicher
   Ladung" = Einpolball mit der Ladung eines Pols). Radiusmass in beiden Lesarten R_eq.
6. **"gleich auf 30 %":** max/min <= 1,3 (strengere der ueblichen Lesarten).
7. **Schwelle:** Klammer der Bisektion; R* am oberen Klammerende, ohne Interpolation.
8. **Kontrolle Q1 = 400 (3D):** auf dem Gitter aller 3D-Schritte (L = 48), nicht mit L = 40 wie N1.

## 10. Grenzen

- Fluss bei festen Ladungen, keine Zeitentwicklung. Der Ausgang haengt am Becken des Starts.
- Ein Gitter je Dimension; 3D mit h = 0,6. Keine eigene Gitter- oder Kastenprobe bei kleinem Q1 (2D bis 15).
- Sektorstart mit einem beta; E_Tropfen nur, wenn der Sektorlauf im Tropfen endet.
- Teil B: sechs Richtungen (drei Klassen nichttrivial) und drei beschreibende Stoerungen, kein Hesse-Spektrum.
- R* ist ein Radiusmass von vielen; die beschreibenden Masse zeigen die Spannweite.
