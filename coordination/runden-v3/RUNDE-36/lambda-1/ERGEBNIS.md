# LAMBDA-1: Ergebnis (Code-Agent fuer die Leitung, Runde 36, explorativ)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 00:17:02 CEST; Quellen gelesen 00:35 bis 00:42 CEST (5 von 6 erlaubten Abrufen).
  - Plantext ab 00:43:01 CEST.
  - Rauchlaeufe 22:46:53 bis 22:48:17 UTC (PLAN Abschnitt 8).
  - Eingefroren 2026-10-04 00:48:47 CEST:
    - PLAN.md.eingefroren-20261004-004847 (sha256 7305627c...);
    - code/lam.py (65dac72d...) und code/lam_auswertung.py (3a6522e1...), Kopien *.eingefroren-20261004-004847;
    - code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe 22:48:54 bis 22:55:46 UTC, alle rc = 0. Auswertung 22:55:54 bis 22:55:57 UTC.
  - Text ab 00:57:13 CEST.
  - Code nach dem Einfrieren unveraendert; die Pruefsummen auf der .69 und lokal stimmen ueberein, und auswertung.json
    nennt fuer alle Eingaben dieselben Skript-Pruefsummen.
- Alle Zahlen sind Gitterrechnungen auf der .69 (lauf-69/), keine Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (Abstracts, siehe PLAN-Kopf);
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher;
  - [H] Hypothese;
  - [M] vorab hergeleitet (PLAN Abschnitt 2);
  - [E] hier gerechnet;
  - [F] Festlegung im Plan.
- **Einheiten:** J = g = 1, Massen m1 = m2 = 1, r in Gitterabstaenden.
  - c ist der Koeffizient im Spurglied -c (E^ii)^2; lambda = c/(3c - 1).
  - P0 = Gl. 32 ohne Strafterme, P1 = Gu/Wen-Gittermodell mit U_v = U_s = 1.

## 1. Ergebnis zuerst

1. **Die Zuordnung der Karte stimmt, und das Gitter bildet Horavas lambda-Skalarmodus exakt nach [M, E].**
   - c ist im Code genau der Spurkoeffizient (Impulsbild pi^ij pi_ij - c pi^2); Gu/Wen entspricht c = 1/2, also
     lambda = 1.
   - Das Gitter hat einen Skalarmodus mit omega^2 = J (1 - 2c)(-g K^2 + 2 U_s K^4).
   - Ohne Strafterme ist das -((lambda - 1)/(3 lambda - 1)) xi K^2 mit xi = g J, also Horavas IR-Formel [L], an jedem
     Gitter-q. Der Abstand zum vollen Spektrum ist <= 1,2e-14 relativ.
2. **Freie Dynamik:** Das Wachstum ist um c = 1/2 asymmetrisch, und das Vorzeichen der Asymmetrie haengt am
   Strafterm [E].
   - P0: Wachstum nur fuer c < 1/2 (lambda > 1; fuer c < 1/3 lambda < 0), Rate sqrt(12 (1 - 2c)) an der Zonenecke.
     Fuer c > 1/2 gibt es kein Wachstum, aber einen Geist (negative Energie).
   - P1: Fuer c < 1/2 waechst es schwach bei kleinem k, fuer c > 1/2 stark an der Zonenecke; bei 1/2 +- 0,05 ist der
     Faktor 47.
   - Exponent 0,5000 in beiden Saetzen.
   - Das Wachstum bei 0,51 in TENSOR-EIS-N ist damit erklaert: Der Strafterm wirkt wie ein R^2-Glied und gibt dem Geist
     positive Gegenenergie [M].
3. **Der gefaehrliche Modus ist fast reine Eichung [E].**
   - E-Seite: zu 100 % die Eichrichtung von Gl. 23.
   - a-Seite: Eichung Gl. 15 plus ein kleiner Anteil Verletzung der Massenregel, 1/(1 + 2c^2/(1 - 2c)^2): 2,4 % bei
     c = 0,45, 0,08 % bei 0,49.
   - Fuer c -> 1/2 wird er zur Eichfreiheit; das ist das Gitterbild der Zeit-Umparametrisierung bei lambda = 1 [L].
4. **Auf der Zwangsflaeche waechst fuer kein c etwas (Projektion und Dirac-Gegenprobe) [E].** Drei Einschraenkungen
   [M, E]:
   - Die Flaeche ist nur bei c = 1/2 unter der Bewegung invariant. Fuer c != 1/2 braucht das Netz eine zusaetzliche
     Regel (E_T = 0); der invariante Unterraum hat dann Dimension 7 statt 8.
   - Fuer c > 1/2 liegt auf der Flaeche eine Richtung negativer Energie; der statische Wert ist dort ein Sattel.
   - Der wachsende Modus braucht neben Z nur einen sehr kleinen Schritt (f_off ab 0,008).
5. **Die statische Anziehung haengt gar nicht von c ab [M, E]: G_eff = 1,000125/(8 pi) fuer jedes c.**
   - L4 ist damit selbsterfuellend.
   - Die Bedeutungszeile der Karte "nur ihre Staerke haengt am Faktor" traegt nicht: Das Minus-Glied regelt die
     Stabilitaet, nicht die Staerke der Schwerkraft.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 00:48:47 CEST) durch code/lam_auswertung.py; alle Werte in lauf-69/auswertung.json.
Alle fuenf Ausgaenge standen vorab im Plan (Abschnitt 2, [M]).

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| L0 | c = 1/2 gibt die TENSOR-EIS-N-Werte (kein Wachstum, Rest < 1e-6; U = -1/(8 pi r) auf 1 % ab r = 8) | 90 % | **eingetroffen** | Rest max 1,71e-8 (P0 bis P6, TT ohne Wachstum); max abs(U 8 pi r + 1) = 0,41 % fuer 8 <= r <= 16; U_korr gegen TENSOR-EIS-N bitgleich (33 Punkte, Abweichung 0) |
| L1 | 1/3 < c < 1/2: exponentielles Wachstum, Rate ~ sqrt(1/2 - c), Exponent 0,5 +- 0,15 aus c = 0,45 bis 0,49 | 55 % | **eingetroffen** | Wachstum bei 0,40/0,45/0,48/0,49 in P0 und P1; p = 0,500000 (P0) und 0,500000 (P1); bei kleinstem q ebenfalls 0,500000 |
| L2 | Raten bei 1/2 +- 0,05 asymmetrisch, Unterschied > 20 % | 60 % | **eingetroffen** | P0: gamma(0,45) = 1,0954, gamma(0,55) = 0, Delta = 1; P1: 0,11141 gegen 5,2536, Delta = 0,979 (zur kleineren Rate: Faktor 47) |
| L3 | Auf der Zwangsflaeche (b) fuer kein c Wachstum; der gefaehrliche Modus lebt neben der Zwangsflaeche | 50 % | **eingetroffen** | Projektion: 0 wachsende q bei allen 12 c (P0, P1), -Re(omega^2)/s <= 4,0e-15; Dirac: 0 wachsende q, Dimension 7 (c != 1/2) bzw. 8 (c = 1/2), einheitlich; TT: 0; f_off des freien Modus 0,0081 bis 0,64 (> 1e-6) |
| L4 | Statische Anziehung bleibt fuer c != 1/2, G_eff(c) stetig, bei 1/2 gleich 1/(8 pi) | 55 % | **eingetroffen** (Vermerk: vorab ableitbar) | 8 pi G_eff = 1,000125 fuer alle c; Sprung 0; U < 0 und anziehend auf allen Strahlen; Kernabweichung delta_c <= 2,0e-15, max abs(E)/max abs(kappa) <= 2,4e-15 |

- **Bedeutung, wie auf der Karte vorab festgelegt** (Lesart in Abschnitt 6):
  - "L1 und L2 treffen ein" ist ausgeloest. Das Minus-Glied hat Horavas lambda-Struktur, und zwar exakt, nicht nur
    qualitativ.
  - "L3 trifft ein" ist ausgeloest, aber nur mit drei Einschraenkungen (Abschnitt 1, Punkt 4). "Entwarnung" gilt fuer die
    lineare, quellenfreie Dynamik mit strengen Regeln einschliesslich der Folgeregel E_T = 0.
  - "L4 trifft ein" ist ausgeloest. Die zweite Haelfte der Bedeutung ("nur ihre Staerke haengt am Faktor") ist **nicht**
    gedeckt: G_eff haengt nicht von c ab.
- **Agenten-Vorhersagen** (PLAN Abschnitt 3; gehen in kein Urteil ein):

  | Nr | Ergebnis |
  |---|---|
  | A1 | eingetroffen: 2,190890 / 2,000000 / 1,549193 / 1,095445 / 0,692820 / 0,489898, dann 0; Ort q = (-pi, -pi, -pi); Anteil 100 % bzw. 0 % |
  | A2 | eingetroffen: 0,222824 / 0,203410 / 0,157560 / 0,111412 / 0,070463 / 0,049825 bei K^2 = 0,229100; 2,349468 / 3,322650 / 5,253570 / 7,429670 / 10,507140 an der Zonenecke; Anteil wachsender q 0,62 % bzw. 99,38 % |
  | A3 | eingetroffen: Spektrum gegen Formel <= 1,2e-14 (c != 1/2, P0 bis P6), <= 1,7e-8 bei c = 1/2 |
  | A4 | eingetroffen: a-Seite Skalaranteil 0,470588 / 0,333333 / 0,111111 / 0,024096 / 0,003460 / 0,000832 und 0,000768 / 0,002950 / 0,016260 / 0,052632 / 0,140351; E-Seite Eichrichtung 1 auf 4e-16; TT und Vektor <= 7e-17; f_off min 0,00814 (P1, c = 0,51) |
  | A5 | eingetroffen: P0 gamma/\|K\| = sqrt(1 - 2c) auf 1e-15; P1 am kleinsten q Faktor 0,960802; Schnitt \|q\| = 1e-3: Abweichung 1,0e-6 bei P1 (genau die erwartete K^2-Korrektur, an der Grenze), 1e-15 bei P0 |
  | A6 | eingetroffen: Projektion -Re/s <= 4e-15; Invarianzdefekt 8,4e-16 bei c = 1/2, sonst genau \|1 - 2c\|/max(1, \|1 - 3c\|) (0,4 / 0,333 / 0,2 / 0,1 / 0,04 / 0,02 / ... / 0,364); Dirac 7 bzw. 8 |
  | A7 | eingetroffen: negative A-Richtung auf Z an 100 % der q fuer c > 1/2, an 0 % sonst; kleinster Wert -0,02 / -0,04 / -0,1 / -0,2 / -0,4 |
  | A8 | eingetroffen: 8 pi G_eff = 1,000125; delta_c <= 2,0e-15; E/kappa <= 2,4e-15; 0,41 %; Vergleich mit TENSOR-EIS-N 0 |
  | A9 | eingetroffen: 144 von 144 Polynomen gleich x^3 (x - K^2)^2 (x - s); P0 negative Wurzel an 6/6 Punkten fuer c < 1/2, 0/6 sonst; P1 an 6/6 fuer c > 1/2 (alle sechs Punkte haben K^2 > 1/2), 0/6 sonst; keine nicht reelle Wurzel |
  | A10 | eingetroffen: Ortsraum gegen Fourier <= 2,9e-13 absolut; kleinste omega^2: -1,2 / 0 (-2e-14) / 0 (-7e-14) / -27,6 |

## 3. Tabellen

### 3.1 Zuordnung und Horava-Vergleich [M, E]

| c | lambda | (lambda - 1)/(3 lambda - 1) | 1 - 2c | gamma/\|K\| bei kleinem k, P0 | sqrt(max(0, 1 - 2c)) |
|---|---|---|---|---|---|
| 0,30 | -3 | 0,4 | 0,4 | 0,632456 | 0,632456 |
| 1/3 | Pol | - | 1/3 | 0,577350 | 0,577350 |
| 0,40 | 2 | 0,2 | 0,2 | 0,447214 | 0,447214 |
| 0,45 | 1,2857 | 0,1 | 0,1 | 0,316228 | 0,316228 |
| 0,48 | 1,0909 | 0,04 | 0,04 | 0,200000 | 0,200000 |
| 0,49 | 1,0426 | 0,02 | 0,02 | 0,141421 | 0,141421 |
| 0,50 | 1 | 0 | 0 | 0 | 0 |
| 0,51 bis 0,70 | 0,9623 bis 0,6364 | < 0 | < 0 | 0 (Geist, omega^2 > 0) | 0 |

- (lambda - 1)/(3 lambda - 1) = 1 - 2c gilt auf Rundung.
- Horavas IR-Formel omega^2 = -((lambda - 1)/(3 lambda - 1)) xi k^2 [L] stimmt mit xi = g J ohne freien Parameter.
  Massstab ist der Gravitonmodus omega^2 = g J K^2 (Gl. 35), also gilt omega_s^2/omega_TT^2 = -(lambda - 1)/(3 lambda - 1).
- Das gilt fuer P0 nicht nur bei kleinem k: Mit k -> K = 2 sin(q/2) ist das ganze Gitterspektrum die Formel (A3).

### 3.2 Freie Dynamik: groesste Wachstumsrate, Ort, Zusammensetzung [E]

| c | gamma_max P0 | Ort P0 | gamma_max P1 | Ort P1 (K^2) | a-Seite: Anteil Massenregel | E-Seite: Anteil Eichrichtung Gl. 23 | f_off P0 / P1 |
|---|---|---|---|---|---|---|---|
| 0,30 | 2,1909 | Ecke | 0,22282 | 0,2291 | 0,4706 | 1 | 0,176 / 0,641 |
| 1/3 | 2,0000 | Ecke | 0,20341 | 0,2291 | 0,3333 | 1 | 0,160 / 0,545 |
| 0,40 | 1,5492 | Ecke | 0,15756 | 0,2291 | 0,1111 | 1 | 0,120 / 0,322 |
| 0,45 | 1,0954 | Ecke | 0,11141 | 0,2291 | 0,0241 | 1 | 0,079 / 0,153 |
| 0,48 | 0,6928 | Ecke | 0,07046 | 0,2291 | 0,00346 | 1 | 0,041 / 0,059 |
| 0,49 | 0,4899 | Ecke | 0,04982 | 0,2291 | 0,00083 | 1 | 0,024 / 0,029 |
| 0,50 | 0 | - | 0 | - | - | - | - |
| 0,51 | 0 | - | 2,3495 | 12 (Ecke) | 0,00077 | 1 | - / 0,0081 |
| 0,52 | 0 | - | 3,3226 | 12 | 0,00295 | 1 | - / 0,0118 |
| 0,55 | 0 | - | 5,2536 | 12 | 0,0163 | 1 | - / 0,0188 |
| 0,60 | 0 | - | 7,4297 | 12 | 0,0526 | 1 | - / 0,0267 |
| 0,70 | 0 | - | 10,507 | 12 | 0,1404 | 1 | - / 0,0379 |

- Die Anteile sind P0 und P1 gleich (auf 1e-15); der Rest der a-Seite ist Eichung Gl. 15 (a_L). TT- und Vektoranteil
  sind <= 1e-16.
- Anteil der q mit Wachstum:
  - P0: 100 % (c < 1/2), 0 % (c >= 1/2);
  - P1: 0,62 % (c < 1/2, K^2 < 1/2), 99,38 % (c > 1/2, K^2 > 1/2).
- P2 bis P6 (beschreibend): Bei c = 1/2 waechst nichts (Rest <= 1,4e-8); fuer c != 1/2 gilt die Formel auf <= 1e-14
  (auswertung.json, tabellen).
- Bild: lauf-69/bild-wachstum.png.
  - Oben: gamma_max gegen c, P0 links, P1 rechts, mit Horava-Kurve und den Werten auf der Zwangsflaeche.
  - Unten links: kleines k gegen sqrt(1 - 2c).
  - Unten rechts: Zusammensetzung.

### 3.3 Zwangsflaeche (b) [E]

| c | Projektion: wachsende q | Dirac: Dimension V* | Dirac: wachsende q | Invarianzdefekt von Z | Energie auf Z: kleinster A-Wert (Anteil q) | statischer Wert auf Z |
|---|---|---|---|---|---|---|
| 0,30 | 0 | 7 | 0 | 0,40 | +0,40 (0 %) | Minimum |
| 0,45 | 0 | 7 | 0 | 0,10 | +0,10 (0 %) | Minimum |
| 0,49 | 0 | 7 | 0 | 0,02 | +0,02 (0 %) | Minimum |
| 0,50 | 0 | 8 | 0 | 8,4e-16 | 0 (Eichung) | Minimum bis auf Eichung |
| 0,51 | 0 | 7 | 0 | 0,02 | -0,02 (100 %) | Sattel (E_T) |
| 0,55 | 0 | 7 | 0 | 0,10 | -0,10 (100 %) | Sattel |
| 0,70 | 0 | 7 | 0 | 0,36 | -0,40 (100 %) | Sattel |

- Gezeigt ist eine Auswahl, alle 12 c stehen in auswertung.json; P1 ist gleich (die Strafterme verschwinden auf Z).
- Die 8x8-Bewegungsmatrix auf Z hat max Re/||D|| = 1,9e-8 (P0) bzw. 2,9e-8 (P1). Das ist Jordan-Rundung der Kette
  E_T -> a_L, beschreibend.
- B auf ker c hat keine negative Richtung (kleinster Wert -6,8e-16 relativ).

### 3.4 Statik [E]

- U_inf nach Torus-Korrektur 128/192/256 ist bitgleich mit TENSOR-EIS-N (33 Strahlpunkte).
- Abweichung von -1/(8 pi r): 1,98 % ab r = 4 und 0,41 % ab r = 8. Unsicherheit der Torus-Anpassung 2,7e-4.
- **G_eff** aus 2105 Oktantpunkten mit 8 <= r <= 16:
  - 0,0397937, also 8 pi G_eff = 1,000125; mit Anpassung 64/128/256 0,0397938.
  - Die groesste Punktabweichung vom Ausgleich ist 0,40 %; das ist die kubische Anisotropie bei r = 8.
- **c-Unabhaengigkeit:** Der volle 16x16-KKT mit A(c) an 37 407 q (L = 32-Halbgitter plus 20 000 Zufalls-q) ergibt
  - eine Kernabweichung von 5e-17 bis 2,0e-15 relativ,
  - E <= 2,4e-15 relativ,
  - Zwangsresiduen <= 3e-14.
- Bild: lauf-69/bild-geff.png.

## 4. Kontrollen

- **K1, Operatoren** (Hauptlauf L = 32):
  - Kv Z_E <= 1,1e-15 und c Z_a <= 4,4e-15;
  - Summen der Zerlegungsanteile 1 auf 4,4e-16;
  - TT-Dynamik omega^2/K^2 = 1 auf 2e-15 fuer alle c.
- **K2, Ortsraum L = 6** (Stencils per np.roll):
  - c = 1/2 wie TENSOR-EIS-N: statisch 1,5e-16; Spektrum P0 4,9e-8, P1 1,2e-6 (Jordan).
  - c = 0,45 und 0,55, P0 und P1: Abweichung <= 2,9e-13 bei max omega^2 bis 27,6; Imaginaerteile <= 1,9e-13.
- **K3, Gu/Wen S. 19:** Matrixvergleich A 1,3e-15, B 4,3e-14; vertauschte Zuordnung 2,4 bzw. 38; Signaturen (5, 0, 1)
  und (2, 3, 1). Alles wie TENSOR-EIS-N, also gehoert die Kopie zu Gu/Wens Modell.
- **K4, exakt:**
  - 144 charakteristische Polynome gleich der Formel aus PLAN Abschnitt 2.
  - Alter Satz bei c = 1/2 wie TENSOR-EIS-N: Null vierfach, Jordan 4 (N), 2 (L).
  - lam 0,45/0,55 mit U = 1: negative Wurzeln, Jordan 2.
- **K5, Statik:**
  - Zwangsresiduen <= 2,2e-15;
  - kappa gegen kappa' <= 4,2e-15;
  - Minimumtest L = 64/128/192: 0 negative Tangentialeigenwerte;
  - Spiegel- und Vertauschungssymmetrie <= 7e-18;
  - G(0) = -0,12460 / -0,12548 / -0,12578 / -0,12592.
- **K6, Torus:** Abstand der Anpassungen 2,7e-4 (wie TENSOR-EIS-N).
- **Latten:**
  - L1 (kann scheitern): Alle Ausgaenge waren vorab ableitbar [M]. Scheitern konnten nur Code und Schreibtisch; echte
    Pruefungen dafuer waren K2, K4 und der Formelvergleich A3.
  - L2 (Gegenprobe): Projektion gegen Dirac gegen TT; Ortsraum gegen Fourier; Gleitkomma gegen exakt; KKT mit und ohne
    E-Teil.
  - L3 (Numerik): 1e-16 bis 1e-14, Jordan-Rundung 1e-8, Torus 2,7e-4.
  - L4 (schon bekannt):
    - Bekannt [L]: Horavas lambda und sein Zusatzmodus, im Kern auch der Geist-/Instabilitaetsbereich; ebenso, dass
      der konforme Modus die Spurstruktur festlegt.
    - Neu ist der exakte Gitternachbau samt Strafterm als z = 2-Glied und die Erklaerung des 0,51-Wachstums.
  - L5 (Messbezug): keiner.

## 5. Selbstanzeigen

1. **Vorab ableitbar:**
   - Alle fuenf Urteile und fast alle Zahlen standen vor der Rechnung im Plan (Abschnitt 2 und 3).
   - L4 ist konstruktionsbedingt wahr, weil c in der Statik nicht vorkommt.
   - Der L1-Exponent ist konstruktionsbedingt 0,5, denn bei festem K gilt gamma ~ sqrt(1 - 2c).
   - Die Rechnung prueft Rekonstruktion, Herleitung und Numerik; sie findet nichts, was der Schreibtisch nicht sagt.
2. **Horava nur teilweise an der Quelle:**
   - Die Dispersionsformel und die lambda-Bereiche (Geist bzw. Instabilitaet) sind [L].
   - Die Abstracts [S] bestaetigen nur das Qualitative: den Zusatzmodus aus der Brechung der Kovarianz, schnelle
     exponentielle Instabilitaeten, Geist-Instabilitaeten und den linearen Modus nur um inhomogene, zeitabhaengige
     Hintergruende.
   - Die Deutung des Strafterms als z = 2-Glied und die lambda-Unabhaengigkeit der Newton-Grenze sind [L?].
3. **Quellenwiedergabe:**
   - Die Abstracts kamen ueber das WebFetch-Werkzeug (ein kleines Modell gibt die Seite wieder).
   - Die ersten zwei API-Abrufe lieferten deutsche Paraphrasen, der dritte nur erste Saetze. Die Wortlaute stammen aus
     den arxiv.org/abs-Seiten von 0906.3046 und 0907.1636.
   - Die Zeichentreue ist nicht unabhaengig geprueft. Fuer Horava und Charmousis u. a. habe ich nur Teilsaetze.
4. **S1 lief mit --mitmin fuer alle drei Groessen**, wie der Befehl im Plan steht (die Option gilt fuer alle L). Die
   Plan-Schaetzung "~ 90 s" setzte stillschweigend nur L = 64 voraus. Folge: 174 s statt ~ 90 s und zusaetzlich der
   Minimumtest bei 128 und 192; auf die Urteile hat das keinen Einfluss.
5. **"Lebt neben der Zwangsflaeche" (L3) ist schwach erfuellt:**
   - Der freie Wachstumsmodus besteht ueberwiegend aus Eichrichtungen, die in Z liegen. f_off liegt zwischen 0,0081 und
     0,64.
   - Erfuellt ist "nicht in Z, braucht die Regelverletzung", nicht "ueberwiegend ausserhalb". Die Schwelle 1e-6 [F5]
     habe ich so gewaehlt; mit einer Schwelle von etwa 0,5 waere der zweite Teil verfehlt.
6. **A5 an der Grenze:** Beim P1-Schnitt weicht gamma/|K| um 1,0e-6 von sqrt(1 - 2c) ab, vorhergesagt war "auf 1e-6".
   Das ist die erwartete Korrektur sqrt(1 - 2K^2) mit K^2 = 1e-6.
7. **Bild:** Im P1-Feld verdeckt die Legende teilweise die Punkte bei c = 0,45 bis 0,49. Die P0-Punkte der
   Zusammensetzung liegen unter den gleichen P1-Punkten. Nach dem Einfrieren nicht geaendert.
8. **Rauchlaeufe:** offengelegt in PLAN Abschnitt 8, einschliesslich der Nebenbeobachtung aus rauch2 (P1 auf L = 8 ohne
   Wachstum fuer c < 1/2).
9. **Zeitbox:** Start 00:17:02, Text ab 00:57:13 CEST, innerhalb von 120 min.

## 6. Bedeutung [M, H]

- **Warum genau 1/2 [M]:**
  - Die Massenregel R^ii = 0 erzeugt die Eichung Gl. 23. Das Spurglied ist nur bei c = 1/2 invariant (PLAN Abschnitt 1).
  - Weicht c ab, wird die Eichrichtung E_T ein echter Freiheitsgrad und paart sich mit der Massenregel-Verletzung a_T.
  - Dieses Paar ist Horavas Zusatzmodus:
    - c < 1/2 (lambda > 1): Gradienteninstabilitaet mit omega^2 = -(1 - 2c) g J K^2;
    - c > 1/2 (1/3 < lambda < 1): Geist.
- **Strafterm [M]:** (U_s/2)(R^ii)^2 gibt dem Skalarmodus positive Energie 2 U_s K^4.
  - Fuer c < 1/2 daempft das die kurzen Wellen; die Instabilitaet bleibt nur bei K^2 < 1/2.
  - Fuer c > 1/2 trifft die positive Energie auf den Geist, und es waechst an der Zonenecke.
  - Die Asymmetrie aus L2 kehrt sich also mit dem Strafterm um. Die Karten-Erwartung "auf der Seite c > 1/2 wird es
    anders (Geist)" stimmt fuer P0 woertlich; in P1 ist der Geist die Ursache des starken Wachstums.
- **Strenge Regeln [M]:**
  - Auf Z waechst linear nichts. Ein Netz mit c != 1/2 muss dafuer aber eine Regel mehr halten (E_T = 0): Die
    Massenregel wird zweiter Klasse und verliert ihre Eichsymmetrie.
  - Das entspricht der nicht projizierbaren Horava-Fassung, in der der Modus um den flachen Hintergrund linear
    verschwindet [S, Blas/Pujolas/Sibiryakov], dort aber um inhomogene, zeitabhaengige Hintergruende auftaucht und sehr
    schnell instabil wird [S].
  - Fuer c > 1/2 bleibt auf Z eine Richtung negativer Energie. Ob sie nichtlinear Energie aufnimmt, ist offen [H].
- **Statik:**
  - Die Newton-Anziehung ist fuer jedes c dieselbe. Das Minus-Glied entscheidet nicht, wie stark die Schwerkraft ist,
    sondern ob das Netz um eine ruhende Masse herum ruhig bleibt.
  - Bei Horava steht lambda ebenso nur bei den Zeitableitungen K_ij [L?].
- **Fuer Finns Netz [H]:**
  - Ein zufaellig gewaehltes Minus-Glied liegt fast nie genau bei 1/2.
  - Darunter waechst das Netz exponentiell. Darueber traegt es einen Geist, der instabil wird, sobald irgendeine
    positive Regelstrafe mitwirkt (P1).
  - Was 1/2 festhaelt, ist eine Symmetrie: Die Massenregel muss Eichungen erzeugen, nicht nur Zustaende verbieten. Das
    ist die Gitterfassung der allgemeinen Kovarianz (Zeit-Umparametrisierung).
  - Der Ausweg "Regeln streng halten" kostet eine zusaetzliche Regel und laesst fuer c > 1/2 einen Geist zurueck.

## 7. Einfach gesagt

Im Netzmodell gibt es ein Energieglied mit Minuszeichen, dessen Staerke c man waehlen kann; Einsteins Theorie verlangt
genau c = 1/2. Nur bei genau 1/2 ist eine bestimmte Verschiebung im Netz bloss eine Umbenennung, die nichts kostet;
weicht c ab, wird daraus eine echte Schwingung, die bei c < 1/2 von selbst immer schneller anwaechst und bei c > 1/2
negative Energie traegt, genau wie der bekannte Zusatzmodus in Horavas Gravitationstheorie. Die Anziehung zweier
ruhender Massen ist dagegen fuer jedes c gleich gross: Das Minus-Glied bestimmt nicht die Staerke der Schwerkraft,
sondern ob das Netz um die Massen herum ruhig bleibt. Haelt das Netz seine Regeln streng ein, waechst zwar nichts, aber
dafuer braucht es bei c != 1/2 eine Zusatzregel und behaelt bei c > 1/2 eine Richtung mit negativer Energie. Deshalb
braucht ein Netz fuer Schwerkraft eine Symmetrie, die das Minus-Glied genau auf 1/2 festhaelt; Zufall reicht nicht.

## 8. Dateien

- PLAN.md und PLAN.md.eingefroren-20261004-004847
- code/:
  - lam.py: Rechnung (Statik, Abtastung, Kontrollen);
  - lam_auswertung.py: Urteile und Bilder;
  - beide mit eingefrorenen Kopien;
  - pruefsummen-einfrieren.txt.
- lauf-69/:
  - auswertung.json (Urteile, Tabellen, Kontrollen);
  - scan.json (c-Abtastung), kontrolle.json, statik-64-128-192 und statik-256 (.json/.npz);
  - tensor-eis-n-auswertung.json (nur Vergleich);
  - Logs;
  - Bilder bild-wachstum.png und bild-geff.png.
- rauch-69/: Rauchlaeufe rauch1 bis rauch6 (Logs und Ausgaben); scan-8.json ist die lokale Kopie von scan.json aus
  rauch2.
- Auf der .69: /home/fmh/fmhc-physics-remote/runde36-lambda/ (code/, rauch/, lauf/).
