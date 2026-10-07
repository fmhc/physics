# RUECKFLUSS-INFO-1: Plan (Runde 45, Luecke L5)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date):** Start 2026-10-05 04:52:01 CEST; Code ab etwa 05:00; Rauchlaeufe R1 bis R4 05:03:23 bis 05:04:28 CEST;
  Plantext ab 05:05:57 CEST.
- **Kennzeichen:** [M] eigene Mathematik (nicht gegengelesen); [E] Messung im Modell; [P] Projektdatei; [H] Hypothese;
  [R] im Rauchlauf gesehen.
- **Art:** Synthetische Rechnung an einem selbst gebauten Modell (SPIEGEL-HAELFTE-1). Keine Messdaten.
- **Karte:** KARTE.md, unveraendert. Vorhersagen RI0 bis RI3, Wahrscheinlichkeiten und Bedeutung von dort.

## 1. Ableitbarkeit und Altdaten (vor jeder Hauptrechnung)

- **FJ ist monoton [M], vorab ableitbar.** Der sichtbare FJ-Schritt K_t = e^{i alpha} P_2 S_t P_2 ist eine Kontraktion.
  Mit der Verlustflagge (Abschnitt 2) ist jeder Schritt eine CPTP-Abbildung, also faellt D_g unter FJ nie [BLP-Argument].
  Die Summe der Anstiege von D_FJ ist 0. Das ist eine Kontrolle, keine Messung.
- **W = 0 ist vorab ableitbar [M].** D(t) folgt aus der Bloch-Entwicklung (k-Raum-Kontrolle im Code). Altdaten [P]:
  w_2 pendelt bei W = 0 mit Periode 2 um etwa 1e-2 (0,98969 / 0,99986 / 0,98996 ...; spiegel-haelfte-1/lauf-69/haupt_1.json).
  Anstiege von D bei W = 0 sind kohaerentes Pendeln und keine Messung.
- **Heuristik zur Hoehe von D bei festen Takten [H].** Fuer A ⟂ B (Abschnitt 3) gilt D_u ≤ (n_A + n_B)/2. Bei bekannten
  festen Takten ist der Rueckfluss eine lineare Funktion des Startzustands; es gibt keinen Grund, dass er fuer A und B
  gleich ist. Bleibt |<a|b>| klein, folgt D_u ≈ w̄_2 = (n_A + n_B)/2. Dann traegt das zurueckgekehrte Gewicht fuer einen
  Beobachter, der die Takte kennt, volle Information. Der "Informationsanteil" q (Abschnitt 4) waere dann ≈ 1.
- **Altdaten zu RI1 [P, Selbstanzeige vorab].** In den sechs W = 2 pi-Saaten von SPIEGEL-HAELFTE-1 (haupt_3.json) faellt
  w_2(t) fast monoton. Je Saat steigt w_2 in 1, 8, 11, 5, 6 und 3 von 100 Schritten. In Saat 44000 gibt es einen einzigen
  Anstieg (t = 91, um 2,3e-4). Bei W = 2 pi ist schon der Rueckschritt t = 1 → 2 weg, der bei W = 0 da ist.
  - Gilt D ≈ w̄_2, so ist RI1 nach Plan eher nicht zu erwarten. Das ist eine Vorabschaetzung aus Altdaten und Heuristik,
    keine Messung.
  - Nicht ableitbar bleibt, ob D bei festen Takten anders laeuft als w̄_2 (wachsender und wieder fallender Ueberlapp
    <a|b>) und ob neu gezogene Takte etwas aendern.
  - Die Karte bleibt unveraendert.
- **sigma-Leiter.** N_FJ(t) ist vorab ableitbar (FJ-Referenz). Ob r an sigma haengt, ist nicht ableitbar (Karte).
- **Schaetzer bei neu gezogenen Takten [M, H; Selbstanzeige vorab].**
  - Mit M Ziehungen ist rho^A ≈ (1/M) Σ_m |a_m><a_m| vom Rang M. Der wahre Ensemblezustand hat einen inkohaerenten Teil
    von sehr hohem Rang. Die Rauschvektoren verschiedener Ziehungen stehen fast senkrecht aufeinander (unabhaengige
    Zufallsphasen auf ~1e4 Knoten).
  - Deshalb ueberschaetzt der Gram-Schaetzer den Spurabstand. Wegen der Konvexitaet der Spurnorm gilt im Mittel
    E[D̂] ≥ D. Bei gemeinsamen Ziehungen fuer A und B misst D̂ ungefaehr den mittleren Abstand bei bekannter Ziehung.
  - Vorab erwartet [H]: Die Nullkontrolle (Abschnitt 2.4) liegt in der Groessenordnung des inkohaerenten Gewichts
    (0,1 bis 0,2). RI2 waere nach Plan dann "nicht auswertbar". Das ist eine Eigenschaft des vorgeschriebenen Schaetzers,
    keine Messung.
  - Zusaetzlich gibt es eine erwartungstreue untere Schranke ueber eine Observable (Spin z, Abschnitt 2.5), nur
    beschreibend.
- **Projekt-grep:** laut Dossier keine Karte mit Spurabstand oder Loschmidt (Karte).

## 2. Definitionen

### 2.1 Reduzierter Zustand und Normierung (bindend)

- Sichtbarer Teil: a(t) = P_2 psi_A(t), b(t) = P_2 psi_B(t). P_2 wirkt am Knoten auf den 4-Zustand. Das ist die
  Einschraenkung auf den Unterraum, kein Tensorfaktor (Karte).
- rho_2^A = |a><a| ist unternormiert, n_A = tr rho_2^A = w_2^A.
- **Konvention (bindend): Verlustflagge.** Was nicht sichtbar ist, wird als ein gemeinsamer Zustand |⊥> gezaehlt:
  rho^A ↦ rho_2^A ⊕ (1 − n_A)|⊥><⊥|. Das ist normiert, und
  - D_g(t) = (1/2) ||rho_2^A − rho_2^B||_1 + (1/2) |n_A − n_B|.
  - Grund: So ist D_g der Spurabstand zweier normierter Zustaende, die aus dem Start durch eine CPTP-Abbildung entstehen
    (sichtbar oder "weg"). Ohne Rueckfluss (FJ) faellt D_g nie (Abschnitt 1). Jeder Anstieg ist Rueckfluss von
    Unterscheidbarkeit im Sinn von Breuer-Laine-Piilo.
- **Beschreibend, ohne Urteil:**
  - D_u = (1/2)||rho_2^A − rho_2^B||_1, ohne Flagge.
  - D_n = Abstand der normierten Zustaende rho_2/n, wie bei Kawabata/Ashida/Ueda. D_n kann auch ohne Rueckfluss steigen
    (Nachauswahl) und taugt deshalb nicht als BLP-Mass.

### 2.2 Feste Takte (exakt)

- Zwei reine, unternormierte Vektoren: ||aa^† − bb^†||_1 = sqrt((n_A + n_B)^2 − 4|<a|b>|^2) [M]. Das ist die
  2x2-Gram-Rechnung in geschlossener Form; im Rauchlauf gegen die Eigenwertrechnung geprueft.
- Je Saat ein Satz beta_x (wie SPIEGEL-HAELFTE-1). A und B laufen im Gleichschritt mit denselben Takten.
- Saatmittel: D̄_g(t) = Mittel der D_g(t) ueber die Saaten.

### 2.3 Neu gezogene Takte (Gram der 2M Vektoren)

- In jedem Schritt wird fuer die Nebenklasse dieses Schritts ein frisches Feld beta gezogen. Verteilung wie bei festen
  Takten: gleichverteilt in [pi − W/2, pi + W/2].
- **M = 8 Ziehungen**, vorab festgelegt. Ziehung m hat eigene Saat [Saatbasis, m]. A und B laufen in Ziehung m mit
  denselben Takten (gleiche Welt).
- rhô^A = (1/M) Σ_m |a_m><a_m|, ebenso rhô^B. Spurnorm exakt aus der Gram-Matrix G_ij = <y_i|y_j> der 2M Vektoren:
  - nichtverschwindende Eigenwerte von Σ s_i |y_i><y_i| = Eigenwerte von G^{1/2} S G^{1/2} mit S = diag(+1/M, −1/M).
  - Dazu die Spuren n̂_A, n̂_B und D̂_g wie in 2.1.

### 2.4 Nullkontrolle des Schaetzers (vorab festgelegt)

- Aus demselben Lauf:
  - D̂_null,A = Abstand zwischen A aus den Ziehungen 1 bis 4 und A aus den Ziehungen 5 bis 8. Der wahre Wert ist 0.
  - D̂_null,B ebenso.
  - Dazu D̂ mit M = 4 (Haelfte 1 und Haelfte 2), "getrennt" (A aus 1 bis 4, B aus 5 bis 8) und das Mittel der
    Abstaende je Ziehung.
- null_max = max ueber t ≤ 100 von max(D̂_null,A, D̂_null,B).

### 2.5 Spin-Schranke (beschreibend)

- S_z^A(t) = Σ_x a(x)^† sigma_z a(x) im C^2-Rahmen von V, mit Gewicht. Dann gilt
  D_g ≥ (1/2)|S_z^A − S_z^B| [M]: Observable mit Norm 1 auf dem sichtbaren Teil, 0 auf der Flagge.
- Bei neu gezogenen Takten ist das M-Mittel erwartungstreu, weil die Groesse linear in rho ist.
- Vergleich fest / neu / FJ zeigt, ob das zurueckgekehrte Gewicht Spin-Gedaechtnis traegt.

### 2.6 Anstiege (bindend)

- Zuwaechse d_t = D(t+1) − D(t), t = 0 bis 99.
- **Summe der Anstiege:** Σ_t max(d_t, 0), bis t = 100 (Karte).
- **"Steigt um mehr als 1e-3":** Wiederanstieg A_max = max ueber t ≤ 100 von [D(t) − min_{s ≤ t} D(s)] > 1e-3.
  Das heisst: D liegt irgendwann um mehr als 1e-3 ueber einem frueheren Wert.
- Beschreibend: groesste Episode (zusammenhaengende Folge positiver Zuwaechse) und groesster Einzelschritt.

### 2.7 Informationsanteil (beschreibend)

- q(t) = (D̄_g(t) − D_FJ,g(t)) / (w̄_2(t) − N̄_FJ(t)).
  - q ≈ 1: Das zurueckgekehrte Gewicht ist voll unterscheidend.
  - q ≈ 0: Es ist fuer A und B gleich (Rauschen).

## 3. Startzustaende

- **Spin** (Karte: "Spin oder Impuls"): u_A = V^† (1, 0), u_B = V^† (0, 1) im 2-Block, also Spin +z und −z im C^2-Rahmen
  von V wie in SPIEGEL-HAELFTE-1.
- Gleiches Paket g(y) = exp(−|y|^2/(4 sigma^2)), normiert. Beide liegen ganz in P_2. Es gilt <psi_A|psi_B> = 0, also
  D(0) = 1 (Rauchlauf: 1,4e−16).
- Grund gegen Impuls: verschiedene Impulse sind bei sigma = 4 nicht orthogonal, und der FJ-Verlust haengt stark an |k|.
  Damit waeren Gewichtsunterschiede und Information vermischt.

## 4. Laeufe, Gitter, Saaten

- Code: code/rueckfluss_info.py importiert code/spiegel_haelfte.py (Kopie, sha256 gleich dem Original dee64ac3...).
  - Kern unveraendert: Gitter (eine FCC-Familie), Paket, Verschiebung, Muenze (alpha = 0, beta = pi, P_2 sauber), feste
    Takte (default_rng(saat), Felder (4,N,N,N)).
  - 'schritt' wiederholt die Operationen von lauf_unordnung in derselben Reihenfolge.
- Auswertung: code/rueckfluss_auswertung.py (Regeln aus Abschnitt 5).
- **Gitter je sigma.** Der Rand wird bis t nicht erreicht; Pruefgroesse ist das Gewicht des Gesamtzustands jenseits
  0,75 R_in und 0,9 R_in, R_in = 0,8165 N Hop. Bei W = 0 lag die aeussere Schale in SPIEGEL-HAELFTE-1 bei t = 100 bei
  38 bis 40 Hop [P], also bei etwa 0,4 Hop je Schritt.

| Lauf | Inhalt | sigma | N (R_in) | t | Saaten | Spur | geschaetzt |
|---|---|---|---|---|---|---|---|
| F1 | fest, W = 0 (mit k-Raum-Kontrolle) und W = pi | 4 | 96 (78) | 100 | 45000; 45100 bis 45103 | p4000a | ~4 min |
| F2 | fest, W = 2 pi | 4 | 96 (78) | 100 | 46000 bis 46005 | cpu6 | ~4 min |
| N1 | neu gezogen, W = pi, M = 8 | 4 | 96 | 100 | [47000, m] | p4000a | ~7,5 min |
| N2 | neu gezogen, W = 2 pi, M = 8 | 4 | 96 | 100 | [48000, m] | cpu6 | ~7,5 min |
| L4a | Leiter, W = 2 pi, fest | 4 | 160 (131) | 200 | 49000, 49001 | p4000b | ~7 min |
| L4b | Leiter, W = 2 pi, fest | 4 | 160 | 200 | 49010, 49011 | p4000b | ~7 min |
| L8 | Leiter, W = 2 pi, fest | 8 | 128 (105) | 100 | 50000 bis 50005 | cpu6 | ~4,5 min |
| L12 | Leiter, W = 2 pi, fest | 12 | 160 (131) | 100 | 51000 bis 51003 | p4000a | ~6 min |
| A | Auswertung | | | | | cpu6 | < 1 min |

- Schaetzungen aus R2 bis R4 (Abschnitt 6). Alle neuen Saaten liegen ausserhalb der Saaten von SPIEGEL-HAELFTE-1
  (42000 bis 44xxx). RI0 ist damit eine echte Wiederholung mit neuen Takten. Mit denselben Saaten waere sie bitgleich und
  keine Pruefung.
- Ablauf: Je Spur eine Kette nacheinander, jeder Lauf ein eigener kleintest.sh-Aufruf (ein Thread, ≤ 10 min, 4 GB).
  p4000b nur, solange WM-1-MB nicht laeuft (der Starter prueft das).
- Faellt ein Lauf aus (rc ≠ 0 oder Zeitabbruch), sind die betroffenen Urteile "nicht auswertbar". Ein zweiter Versuch
  nur mit unveraendertem Code und Vermerk, oder mit weniger Saaten bzw. Schritten und Vermerk.

## 5. Urteilsregeln (vor den Hauptlaeufen festgelegt)

- **Vorbedingung RI1/RI2 (Mass gesund):**
  - FJ-Summe der Anstiege von D_g ≤ 1e−12;
  - Normerhalt ≤ 1e−10 in allen D-Laeufen;
  - Startueberlapp |<psi_A|psi_B>| ≤ 1e−12;
  - k-Raum-Kontrolle bei W = 0: |D_g(Gitter) − D_g(k-Raum)| ≤ 1e−8 fuer alle t ≤ 100.
  - Sonst "nicht auswertbar".
- **RI0 Plan:** F2, Zustand A (Spin +z, wie SPIEGEL-HAELFTE-1), r(100) = (w̄_2^A(100) − N_FJ^A(100))/(1 − N_FJ^A(100)) mit
  dem Saatmittel ueber 6 Saaten. Eingetroffen, wenn |r(100) − 0,440| ≤ 0,01. Vorbedingung: Randgewicht jenseits
  0,9 R_in ≤ 1e−5, sonst "nicht auswertbar".
- **RI0 Kartenwortlaut:** dieselbe Zahl, ohne Vorbedingung.
- **RI1 Plan:** F2 (W = 2 pi, fest), Saatmittel D̄_g: Wiederanstieg A_max > 1e−3 → eingetroffen, sonst nicht eingetroffen.
- **RI1 Kartenwortlaut:** Jede Saat einzeln. Eingetroffen, wenn alle sechs Saaten A_max > 1e−3 haben. Nicht eingetroffen,
  wenn keine. Sonst "gemischt (k von 6)".
- **RI2 Kartenwortlaut:** Gelesen als zwei Teile, die beide gelten muessen ("kein Anstieg ..., solange die Summe ... bei
  festen Takten groesser ist"):
  - (a) N2 (W = 2 pi, neu gezogen), D̂_g mit M = 8: A_max ≤ 1e−3.
  - (b) Summe der Anstiege bis t = 100: fest (F2, Saatmittel D̄_g) > neu (N2, D̂_g).
- **RI2 Plan:** wie Kartenwortlaut, mit Vorbedingung null_max ≤ 1e−3 (Abschnitt 2.4). Sonst "nicht auswertbar
  (Schaetzer-Bias)". Erwartung dazu in Abschnitt 1.
- **RI3 Plan:** Saatmittel r(100) fuer sigma = 8 (L8) und sigma = 12 (L12, falls gerechnet), je in [0,41; 0,47].
  Eingetroffen, wenn alle gerechneten Breiten im Band liegen. Vorbedingung: Randgewicht jenseits 0,9 R_in ≤ 1e−5 in L8
  und L12, sonst "nicht auswertbar". Standardfehler wird angegeben. Liegt eine Grenze innerhalb von 2 Standardfehlern,
  heisst das Urteil "knapp".
- **RI3 Kartenwortlaut:** dieselbe Zahl, ohne Vorbedingung.
- **Beschreibend, ohne Urteil:**
  - W = pi (fest und neu);
  - D_u, D_n, q(t), Spin-Schranke, Nullkontrolle, M = 4 gegen M = 8, "getrennt";
  - r(t) bis t = 200 bei sigma = 4 (L4);
  - r(100) bei sigma = 4 auf N = 160 gegen N = 96 (Gittereinfluss);
  - Zustand B in F2.

## 6. Rauchlauf (Eintrag nach dem Rauchlauf, vor dem Einfrieren)

Alle auf der .69 ueber kleintest.sh (UTC = CEST − 2 h); Dateien in rauch-69/.

| Lauf | Inhalt | Spur | Start (UTC) | Dauer | Speicher | rc |
|---|---|---|---|---|---|---|
| R1 | Kontrollen, N = 24, sigma = 4, 40 Schritte | cpu6 | 03:03:23 | 1,3 s | 58 MB | 0 |
| R2 | Zeit: fest, N = 96, W = 2 pi, 1 Saat, 10 Schritte | cpu6 | 03:03:38 | 9,1 s (Lauf 3,4 s) | 560 MB | 0 |
| R3, R4 erster Versuch | falsches Arbeitsverzeichnis (cd nur in der ersten Hintergrund-Teilshell) | p4000a, p4000b | 03:03:38 | – | – | 2 |
| R3 | Zeit: neu, N = 96, W = 2 pi, M = 8, 4 Schritte | p4000a | 03:03:58 | 25,5 s (Lauf 18,4 s) | 1991 MB | 0 |
| R4 | Zeit: Leiter, N = 160, sigma = 12, 1 Saat, 5 Schritte | p4000b | 03:03:58 | 29,5 s (Lauf 3,4 s) | 1794 MB | 0 |
| R5 | Codepfad N = 24: fest (W = 0 mit k-Raum, pi, 2 pi), neu (pi, 2 pi, M = 8), Leiter (sigma 4 bis t = 200, sigma 8), Auswertung | cpu6 | 03:08:10 bis 03:08:28 | je < 5 s | | alle 0 |

- R5: Die Auswertung (rueckfluss_auswertung.py) lief durch. Angesehen habe ich nur rc und die Schluessel, keine Werte. Davor
  wurde die Auswertung an den Plan angepasst (Wiederanstieg A_max statt Episode, Vermerk "knapp" bei RI3).

- **R1 [R], Kontrollen bei N = 24:**
  - 'schritt' gegen sh.lauf_unordnung: w_2 bitgleich (0).
  - FJ gegen sh.fj_referenz: bitgleich (0).
  - Gram gegen geschlossene Form: 1,3e−15.
  - Gram-Formel gegen volle Eigenwertrechnung (Zufallsvektoren, Betrag ~1e2): 1,4e−14.
  - k-Raum gegen Gitter bei W = 0: 5,8e−15.
  - Gram-Diagonale gegen w_2: 1,7e−15.
  - FJ-Summe der Anstiege: 0.
  - Startueberlapp: 1,4e−16.
- **Zeiten:** fest ~0,17 s je Zustand und Schritt (N = 96); neu ~4,2 s je Schritt (N = 96, M = 8, mit Gram);
  Leiter ~0,68 s je Schritt (N = 160). Daraus die Schaetzungen in Abschnitt 4.
- **Nicht angesehen:** D-Werte und w_2 aus R2 und R3 (nur rc, Zeit, Speicher). R1 lief bei N = 24 (Rand erreicht). Von R1
  habe ich nur die Kontrollzahlen gelesen, nicht die FJ-Kurve.

## 7. Grenzen

- Modellintern; keine Aussage ueber die Natur.
- Information heisst hier Unterscheidbarkeit zweier Spin-Startzustaende. Bei festen Takten setzt das voraus, dass der
  Beobachter die Takte kennt; bei neu gezogenen ist der Ensemblezustand gemeint.
- Der Schaetzer bei neu gezogenen Takten ist nach oben verzerrt (Abschnitt 1). Die Spin-Schranke ist nur eine untere
  Schranke.
- Zeitauflösung ein Schritt. Pendeln mit Periode 2 bis 4 (Nebenklassen-Takt) zaehlt als Anstieg.
- 4 bis 6 Saaten je Fall.
