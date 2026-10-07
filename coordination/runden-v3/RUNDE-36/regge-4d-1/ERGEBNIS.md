# REGGE-4D-1: Ergebnis (Runde 36, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 00:54:11 CEST.
  - Quelle gelesen vor 01:09:04 CEST.
  - Plantext ab 01:16:51 CEST.
  - Rauchlaeufe 23:18:42 bis 23:21:08 UTC.
  - Eingefroren 01:21:49 CEST: PLAN.md.eingefroren-20261004-012149 und Code-Kopien *.eingefroren-20261004-012149;
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlauf 23:22:41 bis 23:23:10 UTC, Auswertung 23:23:16 bis 23:23:25 UTC, alle rc = 0.
  - Text ab 01:27:19 CEST.
- Der Code ist nach dem Einfrieren unveraendert; die Pruefsummen auf der .69 und lokal stimmen ueberein.
- Alle Zahlen sind linearisierte Gitterrechnungen auf der .69 (reines numpy, float64, Spur cpu3), keine Messdaten.
  Die Rechnung ist euklidisch und off-shell.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (Regge/Williams 2000, arXiv:gr-qc/0012035, S. 2-5 und 22-25)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik
  - [E] hier gerechnet
  - [H] Hypothese
  - [F] Festlegung im Plan
- **Vorzeichen** [F2]: Ich zaehle mit H = -M, M ist die Hesse-Matrix von S = sum A_t eps_t. H hat das Vorzeichen der
  euklidischen Einstein-Hilbert-Wirkung (Spin 2 positiv), auf die sich die Karte bezieht.

## 1. Ergebnis zuerst

1. **Die effektive Form auf h_mu_nu ist auf 0,04 % genau Einsteins linearisierte Wirkung, mit Normierung [E].**
   - Integriert man die Gittermoden aus (Schur-Komplement), bleibt bei abs(k) = 0,05 in allen 8 Richtungen
     H_eff = c k^2 (P2 - 2 P0s) mit c = 0,2499 (Erwartung 1/4 [M]).
   - Das entspricht genau S = 1/2 Int R sqrt(g) [S, Gl. 1-2].
   - Je Punkt: fuenf Eigenwerte +0,2499 k^2 (Spin 2), einer -0,4999 k^2 (konformer Modus, Faktor -2), vier 0
     (Eichung).
   - **G2 eingetroffen:** c0s/c2 = -1,9984 bis -2,0071 bei abs(k) <= 0,2, also hoechstens 0,36 % von -2 entfernt.
   - **G3 eingetroffen:** Die 40 Spin-2-Werte streuen um 0,034 % (0,05), 0,14 % (0,1) und 0,55 % (0,2).
   - Abweichungen wachsen wie k^2 (Gitterdispersion), bei 0,4 bis 2,8 %.
2. **G0 nicht eingetroffen, wie vorab vorhergesagt (A1, 90 %).**
   - Flachheit (1,8e-15) und Hermitezitaet (3,5e-12) sind erfuellt. Bei k = 0 gibt es aber 11 statt 10 Nullmoden.
   - Die elfte ist Rocek/Williams' "fifth zero mode corresponding to ... the hyperbody diagonal" [S].
   - **Mechanismus** [M, numerisch bestaetigt]: Alle 14 Dreiecke an der Hyperdiagonale (0, a, 1111) haben bei a einen
     rechten Winkel (Thales: (-a).(1111 - a) = 0). Ihre Flaechen haengen in erster Ordnung nicht von dieser Kante ab
     (dA/ds = 0,0 exakt). Damit verschwinden Zeile und Spalte von M bei **jedem** k, auch bei k = 0.
   - Die Hyperdiagonale ist eine "tote" Variable; sie kommt in der quadratischen Wirkung nicht vor.
3. **G1 nicht eingetroffen nach der eingefrorenen Klassenregel [F9]; die Zaehlung selbst stimmt.**
   - An allen 32 Punkten gibt es 5 Nullmoden (4 exakte Eichmoden plus Hyperdiagonale; von der Karte erlaubt).
   - Sechs Moden skalieren wie k^2, auf 0,9 % genau.
   - Vier Gittermoden sind O(1) mit 2, 2, 2, 8 (positiv).
   - Gescheitert ist meine Klassenregel (h-Anteil eta > 1/2): In den Richtungen (1,-1,0,0) und (1,1,-1,-1) hat je ein
     positiver k^2-Modus eta = 0,38 und wurde als Gittermode gezaehlt. Das ergibt dort 4+/1- statt 5+/1-.
   - **Ursache** [M]: Alle Eigenvektoren mit Eigenwert != 0 stehen senkrecht auf dem Nullvektor der Hyperdiagonale.
     Moden mit grossem u^T h u (u = 1111) verlieren deshalb h-Anteil. Diese Folge von A1 habe ich beim Festlegen der
     Regel uebersehen.
   - **Klassenfrei** (beschreibend, nicht geurteilt): An allen 4095 Impulsen q != 0 der Brillouin-Zone (8^4) hat
     H(q) genau 5 Nullmoden, 9 positive und **genau einen negativen** Eigenwert.
4. **3D-Kontrolle mit demselben Code** (nicht geurteilt):
   - c2 = 0,24995 und c0s/c2 = -1,0000 bis -0,9999, wie fuer d = 3 erwartet: -(d - 2) = -1 [M].
   - Keine Zusatz-Nullmode; eine Gittermode 3,5.
   - Damit ist die Kette Geometrie -> M(k) -> Schur -> Projektoren auch in einer zweiten Dimension richtig normiert.
5. **Bedeutung:** Fuer lange Wellen geben die Regge-Dreiecke im 4D-Kuhn-Gitter genau Einsteins Spin-2-Struktur,
   isotrop und fuenffach entartet, samt konformem Minus-Modus mit Faktor -2.
   - Das ist Rocek/Williams 1981 nachgerechnet [S, sekundaer], mit der Normierung und dem Mechanismus der fuenften
     Nullmode.
   - Hineingesteckt ist die Regge-Wirkung (Regime A).
   - Nicht geprueft: Lorentz-Signatur, die zwei propagierenden Polarisationen, Kopplung an Materie.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 7 durch code/regge4d_auswertung.py; Werte in lauf-69/auswertung.json (Felder
"vermerk" nachgetragen, Urteile und Werte unveraendert, siehe Selbstanzeige 6).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kennzahlen |
|---|---|---|---|---|
| G0 | flach < 1e-12; M(k) hermitesch; bei k = 0 genau 10 Nullmoden (affin) | 85 % | **nicht eingetroffen** | (a) max abs(eps) = 1,8e-15 erfuellt; (b) 3,5e-12 (64 Zufalls-k), 3,0e-12 (Leiter) erfuellt; (c) **11** Nullmoden (abs(lambda) <= 6,3e-12 bei Lambda = 8), danach 2, 2, 2, 8. Affine im Kern (1,0e-12); elfte Kern-Richtung ganz ausserhalb (Singulaerwert 1,000), Hyperdiagonale im Kern (3,7e-13) |
| G1 | kleines k: 4 Eichmoden, 5 positive + 1 negativer Modus ~ k^2, uebrige 5 Gittermoden; Zusatz-Nullmode erlaubt | 50 % | **nicht eingetroffen** | Nullmoden 5 an allen 32 Punkten, Eichresiduum <= 7,8e-13, k^2-Skalierung <= 0,90 %: erfuellt. **Vorzeichen in der Klasse eta > 1/2:** 24 Punkte 5+/1-, 8 Punkte (Richtungen 1,-1,0,0 und 1,1,-1,-1) 4+/1-. **Gitter O(1):** 6 Richtungen 0,994 bis 1,006; 2 Richtungen bis 4,0 (0,1) und 16,0 (0,2), wegen des falsch eingeordneten k^2-Modus |
| G2 | c0s/c2 = -2 auf 10 % bei abs(k) <= 0,2 | 55 % | **eingetroffen** | -1,9984 bis -2,0071; max. Abweichung 0,36 % (Hyperdiagonale, 0,2); bei 0,05: -1,9999 bis -2,0004 |
| G3 | Spin-2 richtungsunabhaengig auf 5 %, fuenffach entartet | 55 % | **eingetroffen** | max abs(x/Mittel - 1) = 0,034 % / 0,14 % / 0,55 % bei 0,05 / 0,1 / 0,2; Mittel 0,24994 / 0,24978 / 0,24911 |

- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "G1 bis G3 treffen ein" ist formal nicht ausgeloest, weil G1 nach der Regel verfehlt ist.
  - "G1 verfehlt (mehr Nullmoden oder kein Minus-Modus)" trifft in diesem Wortlaut nicht zu: Es gibt genau die
    erlaubte fuenfte Nullmode und genau einen Minus-Modus.
  - Die verlangte Beschreibung der Gitterartefakte steht in Abschnitt 4.

**Agenten-Vorhersagen** (PLAN Abschnitt 8, vor jeder Rechnung)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (90 %) | Hyperdiagonale bei jedem k exakter Nullvektor (Thales); 11 Nullmoden bei k = 0; G0 nicht eingetroffen | **eingetroffen**: dA/ds_hd = 0,0 exakt; Residuum 3,7e-13 an allen Punkten; 11 Nullmoden bei k = 0 |
| A2 (75 %) | 5 Nullmoden; 6 Kontinuumsmoden 5+/1-; 4 Gittermoden O(1) | **teilweise**: 5 Nullmoden, 6 k^2-Moden mit 5+/1- (klassenfrei) und 4 Gittermoden (2, 2, 2, 8) eingetroffen; nach der Klassendefinition [F9] in 2 von 8 Richtungen verfehlt, wie G1 |
| A3 (70 %) | c2 = 1/4 und r = -2 auf <= 1 % (0,05), r auf <= 3 % (0,2) | **eingetroffen**: c2 = 0,24991 bis 0,24999 (0,04 %); r 0,02 % (0,05), 0,36 % (0,2) |
| A4 (80 %) | Schur gegen direkte Form < 1 % bei 0,1 | **eingetroffen**: hoechstens 0,12 % |
| A5 (75 %) | 3D: keine Zusatz-Nullmode, 6 Nullmoden bei k = 0; 3/2+/1-/1; c2 = 1/4, r = -1 auf 1 % | **eingetroffen**: c2 = 0,24995, r = -0,99986 bis -1,00000 (0,05) |
| A6 (85 %) | Hermitezitaet und Weg T gegen J <= 1e-9; flach <= 1e-13 | **eingetroffen**: 3,5e-12; 1,9e-12; 1,8e-15 |
| A7 (60 %) | keine weiteren Nullmoden in der BZ ausser q = 0 | **eingetroffen**: 4095 x (5 null / 9 positiv / 1 negativ), q = 0: 11/4/0 |

## 3. Tabellen

### 3.1 Spektrum von H(k) bei abs(k) = 0,05 [E]

(15 Eigenwerte; an allen 32 Leiterpunkten Nullmoden mit abs(lambda)/Lambda <= 3,9e-13; s = l^2,
Standardskalarprodukt)

| Richtung | negativ | positive k^2-Moden (x 1e-4) | Gittermoden | eta des k^2-Modus mit kleinstem eta |
|---|---|---|---|---|
| (1,0,0,0) | -4,42e-4 | 1,10; 1,56; 1,56; 6,25; 6,25 | 2,000; 2,000; 2,001; 7,999 | 0,86 (neg.) |
| (1,1,0,0) | -5,74e-4 | 1,60; 3,12; 3,12; 4,69; 7,07 | 2,000; 2,000; 2,001; 7,998 | 0,69 (neg.) |
| (1,-1,0,0) | -3,12e-4 | 0,69; 0,71; **1,33**; 4,01; 7,13 | 2,000; 2,000; 2,000; 7,999 | **0,377** (der Modus 1,33e-4) |
| (1,1,1,0) | -7,99e-4 | 2,60; 2,60; 5,70; 6,25; 6,25 | 2,000; 2,001; 2,001; 7,997 | 0,62 (neg.) |
| (1,1,1,1) | -1,04e-3 | 3,12; 3,12; 7,03; 7,03; 7,03 | 2,001 (3x); 7,997 | 0,58 (neg.) |
| (1,1,-1,-1) | -2,30e-4 | 0,78; 0,78; **1,33**; 3,12; 7,03 | 2,000 (3x); 7,999 | **0,376** (der Modus 1,33e-4) |
| (1,1,1,-1) | -3,64e-4 | 1,27; 1,27; 1,88; 5,76; 5,76 | 2,000; 2,000; 2,000; 7,999 | 0,83 (neg.) |
| (1,2,3,4) | -8,79e-4 | 2,65; 3,02; 5,44; 6,57; 7,05 | 2,000; 2,000; 2,001; 7,997 | 0,61 (neg.) |

- Bei k = 0: 11 Nullmoden, dann 2,0000; 2,0000; 2,0000; 8,0000 (auf 2e-12).
- Die Gittermoden haben bei k -> 0 feste Werte; das passt zu Rocek/Williams' "they enter without omega's" [S].
- In H sind sie positiv, in der rohen Hesse-Matrix von S negativ.
- Rohe Signatur von M = Hess(S): 1 positiv (konform), 9 negativ (5 Spin 2 + 4 Gitter), 5 null.
- Die eta-Spalte nennt nur den kleinsten h-Anteil unter den k^2-Moden. Die Schwelle 1/2 trennt in 6 Richtungen, in 2
  nicht. Bild: lauf-69/bild-eigenwerte-n4.png (dort ist der falsch eingeordnete Modus als grauer Punkt auf einer
  k^2-Linie sichtbar).

### 3.2 Effektive Form (Schur), Koeffizienten [E]

| Richtung | c2 (0,05) | c0s/c2 (0,05) | c0s/c2 (0,2) | Spin-2 min-max/k^2 (0,2) | c0s/c2 (0,4) |
|---|---|---|---|---|---|
| (1,0,0,0) | 0,24995 | -2,0002 | -2,0036 | 0,2484-0,2498 | -2,014 |
| (1,1,0,0) | 0,24993 | -2,0002 | -2,0031 | 0,2483-0,2498 | -2,012 |
| (1,-1,0,0) | 0,24998 | -2,0001 | -2,0021 | 0,2493-0,2501 | -2,008 |
| (1,1,1,0) | 0,24992 | -2,0004 | -2,0059 | 0,2481-0,2497 | -2,023 |
| (1,1,1,1) | 0,24991 | -2,0004 | -2,0071 | 0,2478-0,2498 | -2,028 |
| (1,1,-1,-1) | 0,24999 | -1,9999 | -1,9984 | 0,2496-0,2499 | -1,994 |
| (1,1,1,-1) | 0,24996 | -2,0003 | -2,0044 | 0,2490-0,2497 | -2,017 |
| (1,2,3,4) | 0,24991 | -2,0004 | -2,0057 | 0,2478-0,2498 | -2,023 |

- **Gesamtabweichung** norm(H_eff - (1/4) k^2 (P2 - 2 P0s))/norm(...): hoechstens 0,044 % (0,05), 0,17 % (0,1),
  0,70 % (0,2), 2,75 % (0,4).
- **Eichsektor:** c1 und c0w <= 1,6e-8 (0,05), da die Gitter-Eichmoden exakt sind. c0sw <= 1,2e-4, also 5e-4 relativ
  zu c2.
  - Die Kontinuums-Eichmoden h = k xi + xi k sind nur bis O(k^2) Nullvektoren: Rest 1,7e-4 (0,05), 2,8e-3 (0,2).
- **Spinmischung** norm(P_J K P_J')/norm(K): <= 1,1e-4 (0,05), <= 1,8e-3 (0,2), <= 7,1e-3 (0,4).
- **Schur gegen direkte Form B0^T H B0:** <= 2,9e-4 (0,05), 1,2e-3 (0,1), 4,6e-3 (0,2).
  - Die direkte Form allein gibt r = -1,9997 bis -1,9998 (0,05) bzw. -1,9946 bis -1,9970 (0,2).
  - Die Gittermoden aendern also erst in O(k^4), wie in PLAN Abschnitt 4 hergeleitet [M].
- Gitterblock C^T H C: 0 (Hyperdiagonale, im Schur-Komplement verworfen) und 2,000; 2,000; 2,001; 7,998 (0,05).
- Bild: lauf-69/bild-koeffizienten-n4.png. Die Kurven bis abs(k) = pi zeigen die Gitterdispersion; c2 faellt bei
  abs(k) = 1 auf 0,220 (Hyperdiagonale) bis 0,246 (quer dazu).

### 3.3 3D-Kontrolle (Kuhn 3D, Gelenke = Kanten) [E]

- Flach 1,8e-15. Bei k = 0: 6 Nullmoden (affin), Gittermode 3,500.
- Bei 0,05 bis 0,4: 3 Nullmoden (Eichung), 2 positive und 1 negative k^2-Mode, 1 Gittermode 3,41 bis 3,50.
- c2 = 0,24995 (0,05); c0s/c2 = -0,99986 bis -1,00000 (0,05), -0,9978 bis -1,0000 (0,2).
- Spin-2-Streuung 0,29 % bei 0,2.
- BZ (16^3): 4095 x (3 null / 3 positiv / 1 negativ), q = 0: 6/1/0.
- Keine Zusatz-Nullmode, denn in 3D ist das Gelenkmass die Kantenlaenge selbst, und dl/ds != 0.
- Die d = 3-Fassungen der Regeln G0 bis G3 sind alle erfuellt (lauf-69/auswertung.json, "kontrolle_3d_regeln_d3").
- Bilder: lauf-69/bild-eigenwerte-n3.png, lauf-69/bild-koeffizienten-n3.png.

## 4. Gitterartefakte (Karte: "beschreiben, welche")

1. **Tote Hyperdiagonale** [M, E]:
   - dA_t/ds_hd = (s_b + s_c - s_hd)/(16 A) = 0 fuer alle 14 Dreiecke an ihr, weil der Winkel gegenueber der
     Hyperdiagonale recht ist. Die Ecken des Wuerfels liegen auf der Kugel mit der Hyperdiagonale als Durchmesser.
   - Folge: Die Laenge der Hyperdiagonale kommt in der Wirkung zweiter Ordnung nicht vor, bei jedem k.
   - Das ist Rocek/Williams' fuenfte Nullmode [S]. Sie ist keine Eichmode; die Bewegungsgleichung legt sie nicht
     fest.
   - Fuer Achsen-, Flaechen- und Raumdiagonalen gibt es dagegen stets Dreiecke mit nicht rechtem Gegenwinkel [M].
2. **Vier massive Gittermoden** (2, 2, 2, 8 in s-Einheiten bei k -> 0; positiv in H). Sie koppeln an h erst in O(k^2)
   und aendern die effektive Form erst in O(k^4).
3. **Gitterdispersion:** Spin-2- und Spin-0-Koeffizient fallen wie k^2 ab, je nach Richtung verschieden stark.
   - Am staerksten laengs der Hyperdiagonale, am schwaechsten quer dazu (1,1,-1,-1).
   - Spinmischung und Anisotropie bleiben bei abs(k) <= 0,2 unter 0,6 %.
4. **Keine Doppler- und keine Schachbrettmoden:** In der ganzen Brillouin-Zone (8^4) gibt es ausser den 5
   Nullmoden keine weiteren, und ueberall genau einen negativen Eigenwert.

## 5. Kontrollen

- **Geometrie:**
  - Flach 1,8e-15; unter Skalierung l x 1,3: 1,8e-15; unter zufaelliger affiner Verzerrung 3,6e-15.
  - Simplizes je Dreieck 4 bis 6, je Kante 12 bis 24.
  - Flache Diederwinkel nur pi/4, pi/3, pi/2.
  - Je Ecke 15 Kanten, 50 Dreiecke, 24 Simplizes.
- **Schlaefli:** je Simplex 8,4e-13; global sum_tau A_tau E_tau,d(0) = 3,6e-11.
- **Ableitungen:**
  - Richardson-Fehlerschaetzung 7,5e-12.
  - Weg T (Torus) gegen Weg J (lokale Jacobimatrizen) 1,9e-12.
  - Torus L = 3 gegen L = 4 bitgleich (900 Koeffizienten).
  - Betroffene Dreiecke je Kantentyp 47 bis 89, alle in [-1, 1]^4 (keine Bildueberlappung).
- **Mittelpunktskonvention:** Imaginaerteil von M(k) <= 1,7e-12 relativ; M ist reell, wie vorhergesagt.
- **Nullraum:** Bei k != 0 liegt der numerische Nullraum bis auf 2e-8 in span(Eichmoden, Hyperdiagonale).
  - Der Rest faellt wie 1/k^2 (4e-9 bei 0,1; 1e-9 bei 0,2).
  - Das passt zu Ableitungsfehlern von etwa 1e-12, geteilt durch den kleinsten k^2-Eigenwert (7e-5 bei 0,05).
- **Schwellenabstand:** Bei abs(k) = 0,05 ist der kleinste k^2-Eigenwert 8,6e-6 Lambda, also Faktor 9 ueber der
  Nullschwelle 1e-6 der Karte.
  - Unter abs(k) ~ 0,02 wuerden k^2-Moden als null gezaehlt. Das betrifft nur die feinen Bildkurven (ab 0,01): Dort
    fehlen einzelne der kleinsten Punkte.
- **Latten (v3):**
  - L1 (kann scheitern): ja.
    - G0 (c) war vorab als Scheitern vorhergesagt (A1).
    - G2/G3 haetten durch eine anisotrope Form scheitern koennen: Linearisiertes EH um eine konstante Metrik
      G = a delta + b u u^T hat dieselben Eichbahnen und dieselbe S4 x Z2-Symmetrie [M, H]. Die Rechnung ist mit
      b = 0 vertraeglich (isotrop auf 0,04 % bei abs(k) = 0,05).
  - L2 (Gegenprobe): Weg T gegen J; L = 3 gegen 4; Schur gegen direkt; BZ-Zaehlung gegen Leiter; 3D-Kontrolle.
  - L3 (Numerik): 1e-12 bis 1e-15.
  - L4 (schon bekannt): Rocek/Williams 1981 "shown to agree with the continuum propagator in the weak field limit"
    [S, sekundaer], dort auch die fuenfte Nullmode. Neu hier: Normierung 1/4 auf 0,04 % und der Thales-Mechanismus
    (ob er in der Literatur steht, ist nicht geprueft).
  - L5 (Messbezug): keiner.

## 6. Selbstanzeigen

1. **G0 vorab ableitbar.** Das Scheitern stand vor jeder Rechnung im Plan (A1, 90 %). Die Karte (85 %) hatte die
   fuenfte Nullmode bei k = 0 nicht vorgesehen.
2. **G1 scheitert an meiner Klassenregel [F9], nicht an der Zaehlung.**
   - Ich habe die Folge von A1 fuer die h-Anteile nicht durchdacht: Eigenvektoren stehen senkrecht auf e_hd.
   - Die Regel bleibt eingefroren; das Urteil ist "nicht eingetroffen".
   - Die klassenfreien Zaehlungen (BZ-Signatur, Inertia von Schur-Form und Gitterblock) sind nachtraeglich als
     Lesehilfe ausgewertet und nicht geurteilt.
   - Eine Regel nach Haynsworth-Inertia oder k^2-Skalierung haette den Fall richtig gezaehlt; vorab festgelegt war
     sie nicht.
3. **G2 und G3 sind weitgehend vorab erwartbar:**
   - Cheeger/Mueller/Schrader-Konvergenz [S, Regge/Williams S. 3, nur als Hinweis], Eichinvarianz, Inversionssymmetrie.
   - A3 sagte 70 % voraus.
   - Scheitern war aber moeglich (Abschnitt 5, L1).
4. **Rauchlaeufe** (PLAN Abschnitt 11): Vor dem Einfrieren gesehen:
   - die 4D-Geometrie (G0 (a) und Teil (b));
   - dA/ds_hd = 0;
   - die volle 3D-Kontrolle.
   - Ein 4D-Spektrum oder eine 4D-Form wurde vor dem Einfrieren nicht gerechnet.
   - Vor dem Einfrieren behoben: Die Betraege wurden als Normen gesucht; jetzt gilt "betrag_nominal".
   - Schwellen unveraendert.
5. **Festlegungen mit Gewicht:**
   - [F1] s = l^2: Die Signatur ist davon unabhaengig.
   - [F2] H = -M: Mit der rohen Hesse-Matrix lautet G1 umgekehrt 1+/5-.
   - [F6] Komplement mit Hyperdiagonale: Wirkt erst in O(k^4); die direkte Form ergibt dieselben Urteile G2/G3.
6. **auswertung.json nachbearbeitet:**
   - Die Felder "vermerk" wurden nach dem Lauf per jq eingetragen.
   - Urteile und Werte sind gegen die Maschinenfassung lauf-69/auswertung.maschine.json per diff identisch.
7. **Quelle:**
   - Ein Abruf: PDF Regge/Williams 2000, gelesen S. 2-5 und 22-25.
   - Rocek/Williams 1981 selbst nicht gelesen.
   - Barnes-Rivers-Projektoren nicht nachgeschlagen, selbst hergeleitet und mit TT- und konformem Modus geprueft [M].
     Die 3D-Kontrolle bestaetigt die d-Abhaengigkeit -(d - 2).
8. **Reichweite:**
   - Euklidisch, linear, off-shell.
   - Die Zahl propagierender Polarisationen (2), die Lorentz-Signatur und die Kopplung an Materie sind nicht
     geprueft.
   - "5 Spin-2-Moden" meint die fuenf Komponenten des Projektors P2 der quadratischen Form.
9. **Spuren:**
   - Nur cpu3, hoechstens ein Lauf zugleich.
   - Fuenf Starts: rauch1, rauch2, Probe der Auswertung, haupt, auswertung. Alle unter 30 s.
10. **Zeitbox:** Start 00:54:11, Text ab 01:27:19 CEST, innerhalb von 150 min.

## 7. Bedeutung

- **Zu Finns Frage "Wie kommen wir auf die Spin-2-Kopplung aus Punkten, Strichen, Dreiecken?":**
  - Man nehme die Striche als Laengen, die Kruemmung als Spaltwinkel an den Dreiecken und die Regge-Summe A eps als
    Energie. Dann ergibt das 4D-Kuhn-Gitter fuer lange Wellen genau die linearisierte Einstein-Wirkung, mit dem
    richtigen Faktor 1/2 Int R sqrt(g).
  - Spin 2 ist isotrop und fuenffach entartet. Die Eichfreiheit ist exakt (Eckenverschiebungen).
  - Der konforme Modus hat genau -2 mal die Spin-2-Steifigkeit, also das "falsche Vorzeichen", das laut TENSOR-EIS-N
    die Anziehung gleicher Massen traegt. Spin 2 und dieser Minus-Modus kommen zusammen.
- **Aber** (wie im Dossier, Regime A):
  - Das ist hineingesteckt. Die Regge-Wirkung ist die diskrete Einstein-Wirkung [S, Gl. 1-2].
  - Hergeleitet ist nur, dass das Kuhn-Gitter sie ohne Verzerrung weitergibt: keine Anisotropie, keine
    Zusatz-Minusmoden, die tote Hyperdiagonale harmlos.
  - Aus Punkten und Strichen allein, ohne diese Regel, folgt hier nichts.
- **Naechster Schritt [H]:**
  - Lorentz-Fassung (eine Zeitrichtung) oder Hamilton-Zaehlung, um die zwei propagierenden Polarisationen zu sehen.
  - Oder die Gegenprobe auf einem Gitter ohne rechte Winkel (z. B. verzerrter Hyperkubus wie bei Rocek/Williams'
    Flaechenvariablen [S, S. 24]). Dort sollte die fuenfte Nullmode verschwinden, und G0 (c) wuerde eintreffen.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-012149, EINGEFROREN-SHA256.txt
- code/:
  - regge4d.py: Gitter, Geometrie, Ableitungen (Wege T und J), M(k), Spektren, Schur-Form, Projektoren, BZ
  - regge4d_auswertung.py: Urteile und Bilder
  - beide mit Kopien *.eingefroren-20261004-012149
- lauf-69/:
  - haupt.json (alle Rechenwerte), haupt.log
  - auswertung.json (Urteile mit Vermerken), auswertung.maschine.json (Maschinenfassung), auswertung.log
  - Bilder bild-eigenwerte-n4.png, bild-koeffizienten-n4.png, bild-eigenwerte-n3.png, bild-koeffizienten-n3.png
  - PRUEFSUMMEN.txt
- rauch-69/: rauch1.json/.log; r2/ (rauch2, Probe der Auswertung auf 3D-Daten, Probebilder)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde36-regge4d/ (code/, rauch/, lauf/)

## 9. Einfach gesagt

Wir haben einen vierdimensionalen Raum aus lauter gleichen Bausteinen gebaut und nur die Laengen der Striche veraendert;
die Kruemmung sitzt, wie Regge es vorschlaegt, als kleiner Spaltwinkel an den Dreiecken. Fuer lange Wellen verhaelt
sich dieses Netz genau wie Einsteins Schwerkraft: fuenf gleich steife Spin-2-Verformungen, in jeder Richtung gleich,
und eine "Aufblas"-Verformung mit genau minus doppelt so grosser Steifigkeit, das "falsche Vorzeichen", das gleiche
Massen einander anziehen laesst. Dazu kommen vier Verschiebungen ohne Energie, vier steife Gitterschwingungen ohne
Rolle fuer lange Wellen und ein "toter" Strich, die lange Wuerfeldiagonale, der nichts kostet, weil alle Dreiecke an
ihm rechte Winkel haben. Zwei Kartenvorhersagen sind formal nicht eingetroffen: G0 wegen dieser toten Diagonale (das
hatten wir vorher ausgerechnet) und G1 wegen unserer eigenen Sortierregel, nicht wegen der Physik. Kommt Spin 2 aus
Dreiecken? Ja, aber nur, weil wir Regges Regel "Kruemmung mal Flaeche" hineinstecken; aus Punkten und Strichen allein
kommt es hier nicht.
