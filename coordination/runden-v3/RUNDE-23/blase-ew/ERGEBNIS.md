Urteil: B1 eingetroffen, B2 eingetroffen, B3 eingetroffen nach Suchstand (Quote 3 von 3). Ergebnis: L <= 9.3 um (68 %); der Wert von 2024 (51 um) liegt in beta 30-fach ueber der Eot-Wash-Grenze von 2007. Auflagen A1 bis A4.

# BLASE-EW: Ergebnis der blinden Nachrechnung (Runde 23)

- Pruefer: pruefer-opus (Haus Anthropic), frisch, blind (dd-spuren/ und RUNDE-23.md nicht geoeffnet).
- Beginn: 2026-10-02 21:50:37 CEST (date). Letzte Messung vor Abschluss: 2026-10-02 22:08:28 CEST (date),
  also 17 min 51 s.
- Auflagen vor jeder Weitergabe:
  - A1: Dritte Nachrechnung als Neufit mit dem vollen Potential (QA Gl. 66), der Testmassen-Geometrie und den
    Daten. Bei L > ~13 um gilt die Reihe an den kleinsten Abstaenden nicht.
  - A2: Den Koeffizienten 3/2 und den Term zweiter Ordnung an der LaTeX-Quelle von QA oder QB pruefen. Gelesen
    habe ich nur das HTML-Rendering.
  - A3: Die B3-Suche um eine Volltextsuche erweitern (Scholar, zitierende Arbeiten). Bisher nur INSPIRE und
    arXiv.
  - A4: Nur die 68-%-Schranke (9.3 um) als QE-Wert zitieren. Die rund 13 um bei 95 % sind eine
    Gauss-Schaetzung [H].
- Karte: coordination/runden-v3/RUNDE-23/blase-ew/KARTE.md, sha256 9bef5ca33eb7473f47531574863e5c95cd5b4d155e4b09de683ec9c5199bfea2, 396 Woerter.
- Marken: [S] gelesen, [L?] nur Abstract oder Zitat, [H] eigene Schlussfolgerung, [E] Rechnung (Kopfrechnung).

## 1. Ergebnis zuerst

1. **Abbildung (B1 eingetroffen):**
   - Die Blase weicht in fuehrender Ordnung so ab: V = -G m1 m2/r [1 - (3/2)(L/r)^2] (QA Gl. 67, QB Gl. 23).
     Das ist genau der Eot-Wash-Potenzterm k = 3 mit beta_3 = -(3/2)(L/1 mm)^2. [S/E]
2. **Schranke (B2 eingetroffen):**
   - Aus abs(beta_3) <= 1.3e-4 (QE Tabelle I, 68 %) folgt L <= 9.3 um. [E]
   - Bei 95 % sind es grob 13 um (Gauss-Annahme). [E/H]
   - Das bestaetigt die DD-SPUREN-Kopfrechnung (9 um) unabhaengig.
3. **Wert von 2024:**
   - L = 51 um stammt aus Danielsson/Panizo (PRD 109, 026003, 2024), nicht aus Danielsson/Giri. [S]
   - Er gibt beta_3 = -3.9e-3, das 30-Fache der Grenze. Schon die Schranke von 2004 lag darunter, um den
     Faktor 1.4. [E]
   - Danielsson/Giri 2025/2026 nennen nur "of order 10^-5 m". Bei L = 10 um liegt der Wert knapp an der
     Grenze (Faktor 1.15). [S/E]
4. **Gegensweep:**
   - Fuer L <= 9.3 um gilt die Reihe im ganzen Datenbereich (55 um bis 9.53 mm). Die naechste Ordnung
     verstaerkt die Abweichung dort um 0 bis 21 %. [E]
   - Einwaende aus Material, Abschirmung oder Geometrie fand ich keine. [H]
   - Falsche Vergleichsgroessen wuerden 51 um faelschlich durchlassen: die Fat-Graviton-Grenze l_g <= 98 um
     und die Yukawa-Grenzen von 39 bis 56 um. [S/H]
   - Eine staerkere k = 3-Schranke seit 2007 fand ich nicht; HUST 2020 liegt etwa gleich (L < 9.0 um). [L?/E]
   - B3 ist nach Suchstand eingetroffen.
5. **Bedeutung (Karte):** Die dunkle Blase im Parameterwert von 2024 ist nach unserer Lesung schon durch Daten
   von 2007 ausgeschlossen [E, L5]. Vor jeder Weitergabe braucht es zwei Schritte:
   - eine dritte Nachrechnung, am besten ein Neufit mit dem vollen Potential QA Gl. (66);
   - den Quellenabgleich, vor allem den Koeffizienten 3/2 an der LaTeX-Quelle.
   - Das Modell als Ganzes ist damit nicht ausgeschlossen. [H]

## 2. Antworten auf die Fragen

### Frage 1: Form der Blasen-Abweichung

Quellen:
- QA: Danielsson, Giri, "Weak gravity at micron scales from dark bubble cosmology and its cosmological
  consequences", arXiv:2511.21362v2 (v1 26.11.2025, v2 22.06.2026), Phys. Rev. D 113, 126010 (2026). [S]
- QB: Danielsson, Giri, "Dark bubbles, dark dimensions and fat gravitons", arXiv:2606.20942v1 (18.06.2026). [S]
- QV (Vorlaeufer, "Wert von 2024"): Danielsson, Panizo, "Experimental tests of dark bubble cosmology",
  arXiv:2311.14589v2 (24./27.11.2023), laut INSPIRE Phys. Rev. D 109, 026003 (2024). [S]

Formel:
- QA, Abschnitt "Examining the gravitational potential", Gl. (67), eingeleitet mit "The first few terms at large r":
  V(rho) = G4 M4 [ 1/rho - 3 L^2/(2 rho^3) + 3 L^4 (31 - 18 log(rho/L))/rho^5 + ... ]. [S]
- QB, Abschnitt IV ("Fat gravitons"), Gl. (23): dieselbe Reihe mit ausgeschriebenem Minus,
  V(rho) = -G4 M4 [ 1/rho - 3L^2/(2 rho^3) + ... ]. [S]
- Fuer zwei Massen also V = -G m1 m2/r [1 - (3/2)(L/r)^2 + O(L^4/r^4 log)]. [H, Superposition siehe unten]

Parameter, Vorzeichen, Gueltigkeit:
- rho ist "the proper 4D radius on the brane" (QA); L ist die AdS5-Laenge (QA, Bildunterschrift Fig. 4:
  "in units of the AdS5 length L"). [S]
- Vorzeichen: Die Korrektur verkleinert den Betrag des Potentials. QA, Fig. 4: "Gravity on the dark bubble
  gets weaker at small distances." [S] In der Eot-Wash-Form heisst das beta < 0. [H]
- Gueltigkeit: Gl. (67) ist eine Entwicklung fuer grosse rho, also rho >> L. [S] Fuer rho -> 0 geht das
  Potential in 5D-Schwerkraft ueber, G5 M4/rho^2 (QA Gl. 64). [S] Die Reihe ist asymptotisch; zur
  Brauchbarkeit siehe Frage 4. [H]
- Linearitaet: QA Gl. (60), h_ab = 16 pi G4/q^2 G(q) (T_ab - T eta_ab/2), ist linear in der Quelle. [S]
  Daraus folgt Superposition ueber ausgedehnte Testmassen. [H]

Wert von L:
- 2024: QV, Tabelle 1: L = 5.1 x 10^-5 m (3.8 meV). [S] Abstract: "dark dimension of size 5 x 10^-5 m". [S]
  L ist dort der Radius des D3-Branen-Stapels (AdS5 x S5). [L?, nur WebFetch-Zusammenfassung]
  Probe [E]: hbar c / L = 1.973e-7 eV m / 5.1e-5 m = 3.87e-3 eV, passt zu 3.8 meV.
- 2025/2026: QA, Einleitung: "the AdS-scale should be of order 10^{-5}m". [S] QB, Abschnitt IV: "L∼10⁻⁵ m". [S]
  Einen genaueren Wert als "of order 10^-5 m" fand ich in QA nicht. [S, Suche per WebFetch]
- Befund zur Karte: Die 50 Mikrometer stammen aus Danielsson/Panizo (PRD 2024), nicht aus Danielsson/Giri.
  Danielsson/Giri 2025/2026 nennen nur die Groessenordnung 10 Mikrometer. [S/H]
- QB stellt die Blase als Umsetzung von Sundrums "fat graviton" dar (Abstract). [S] Das ist fuer Frage 4
  wichtig, weil Adelberger u. a. 2007 genau diese Variante mit anderer Kraftform getestet hat.

### Frage 2: Was begrenzt Adelberger u. a. 2007

Quelle QE: Adelberger, Heckel, Hoedl, Hoyle, Kapner, Upadhye, "Particle Physics Implications of a Recent Test
of the Gravitational Inverse-Square Law", arXiv:hep-ph/0611223v3 (7. Feb. 2007), Phys. Rev. Lett. 98, 131104
(2007). PDF Seiten 1 bis 4 gelesen. [S]

- Form, QE Gl. (18): V^k_ab(r) = -G (M_a M_b / r) beta_k (1 mm / r)^(k-1). [S] Gefittet wurde "a function that
  contained the Newtonian term and a single power-law term with k = 2, 3, 4, or 5". [S] Zusammen also
  V = -G M_a M_b / r [1 + beta_k (r0/r)^(k-1)] mit r0 = 1 mm, wie in der Karte. [S/H]
- Schranken, QE Tabelle I, Ueberschrift "68% confidence laboratory constraints on power-law potentials": [S]

| k | abs(beta_k), QE 2007 | abs(beta_k), fruehere Arbeit |
|---|---|---|
| 2 | 4.5 x 10^-4 | 1.3 x 10^-3 (Spero 1980 / Hoskins 1985, QE Ref. 15) |
| 3 | 1.3 x 10^-4 | 2.8 x 10^-3 (Hoyle u. a., PRD 70, 042004, 2004, QE Ref. 14) |
| 4 | 4.9 x 10^-5 | 2.9 x 10^-3 (QE Ref. 14) |
| 5 | 1.5 x 10^-5 | 2.3 x 10^-3 (QE Ref. 14) |

- Konfidenz: 68 %, nicht 95 %. [S] Die Tabelle nennt Betraege abs(beta_k), gilt also fuer beide
  Vorzeichen. [S fuer die Spaltenueberschrift, H fuer "beide Vorzeichen"] Mittelwert und Fehler des Fits
  stehen nicht in QE. [S, Seiten 1 bis 4]
- Ein Potenzterm je Fit, kein gemeinsamer Fit mehrerer k. [S]
- Daten: QE Ref. [1] = Kapner u. a., hep-ph/0611184, Phys. Rev. Lett. 98, 021101 (2007). [S] Abstand laut
  Kapner-Abstract "between 9.53 mm and 55 micrometers"; Yukawa mit Gravitationsstaerke ausgeschlossen bis
  56 Mikrometer (95 %), Extradimension hoechstens 44 Mikrometer. [L?, nur Abstract]
- Weitere Inhalte von QE, die hier zaehlen [S]:
  - "Fat graviton" (Sundrum), Gl. (17): F_fat(r) = -G M1 M2/r^2 [1 - exp(-(0.914 r/l_g)^3)], Maximum bei
    r = l_g. Ergebnis: "Our results require l_g ≤ 98 μm at 95% confidence."
  - Begruendung im Text: die Daten pruefen den Fernschwanz der Potentiale, und die Fat-Graviton-Kraft
    "falls off much more rapidly" als eine Yukawa-Kraft.
  - Probe der Form [E]: f(x) = (1 - exp(-x^3))/x^2 hat sein Maximum bei 3 y exp(-y) = 2 (1 - exp(-y)),
    y = x^3, umgestellt (3 y + 2) exp(-y) = 2. Mit y = 0.7635: exp(-0.7635) = exp(-0.75) x exp(-0.0135)
    = 0.4724 x 0.9866 = 0.466; (3 x 0.7635 + 2) x 0.466 = 4.29 x 0.466 = 2.00.
    x = 0.7635^(1/3) = 0.914, denn 0.914^2 = 0.8354, 0.8354 x 0.914 = 0.7635. Die Klammer ist also
    exp(-(0.914 r/l_g)^3); die PDF-Darstellung ist an dieser Stelle mehrdeutig.

### Frage 3: Schranke auf L, Rechnung

Alles Kopfrechnung [E]. Keine Rechnung auf der .69 (feste Prueferregel: kein ssh, kein Rechnen auf dem Rechner;
die Karte laesst Kopfrechnung als [E] zu).

Schritt 1, Abbildung:
- Blase (Frage 1): V = -G m1 m2/r [1 - (3/2) (L/r)^2 + ...].
- Eot-Wash (QE Gl. 18): V = -G m1 m2/r [1 + beta_k (r0/r)^(k-1)], r0 = 1 mm.
- Gleiche Potenz von 1/r: k - 1 = 2, also k = 3.
- Koeffizientenvergleich: beta_3 (r0/r)^2 = -(3/2)(L/r)^2, also beta_3 = -(3/2) (L/r0)^2.
- beta_3 < 0, die Schwerkraft wird schwaecher; QE Tabelle I begrenzt den Betrag. [E]

Schritt 2, Schranke aus QE Tabelle I (abs(beta_3) <= 1.3e-4, 68 %):
- (3/2)(L/r0)^2 <= 1.3e-4
- (L/r0)^2 <= (2/3) x 1.3e-4 = 0.8667e-4 = 86.67e-6
- L/r0 <= 9.31e-3, Probe: 9.31^2 = 86.49 + 2 x 9.3 x 0.01 + 0.0001 = 86.68
- Ergebnis: **L <= 9.3 Mikrometer (68 %)**. [E]

Schritt 3, die genannten Werte von L einsetzen:

| L | beta_3 = -(3/2)(L/1 mm)^2 | Verhaeltnis zu 1.3e-4 | Lesart |
|---|---|---|---|
| 51 um (QV, 2024) | -1.5 x 2.601e-3 = -3.90e-3 | 30.0 | weit ausserhalb |
| 50 um | -1.5 x 2.5e-3 = -3.75e-3 | 28.8 | weit ausserhalb |
| 10 um (QA/QB "order 10^-5 m") | -1.5 x 1.0e-4 = -1.5e-4 | 1.15 | knapp an der 68-%-Grenze |
| 9.3 um | -1.30e-4 | 1.00 | Grenze |

- In L gerechnet liegt 51 um um den Faktor 51/9.31 = 5.48 ueber der Grenze; 5.48^2 = 30.0. Die "etwa
  30-fach" der Karte meinen also beta, nicht L. [E]
- Auch die fruehere Schranke (Hoyle u. a. 2004, abs(beta_3) <= 2.8e-3, 68 %) gibt
  L <= sqrt((2/3) x 2.8e-3) mm = sqrt(18.67e-4) mm = 4.32e-2 mm = 43 um.
  Probe: 4.32^2 = 18.66. Der Wert 51 um lag also schon 2023/2024 ueber dieser aelteren Grenze, um den
  Faktor 3.90/2.8 = 1.39 in beta. [E]

Schritt 4, Konfidenz:
- QE nennt nur 68 %. Annahme [H]: Die Likelihood ist annaehernd gaussisch, mit Zentrum nahe 0; dann ist
  68 % etwa 1 sigma.
- 95 % zweiseitig (1.96 sigma): abs(beta_3) <~ 2.55e-4, also (L/r0)^2 <= 1.70e-4 und L <= 1.304e-2 mm,
  rund **13 um**. Probe: 1.304^2 = 1.700. [E unter Annahme H]
- Fuenffache 68-%-Grenze (6.5e-4): (L/r0)^2 <= 4.33e-4, L <= 2.08e-2 mm = 21 um. Probe: 2.08^2 = 4.33. [E]
- Damit 51 um durchgeht, muesste die Schranke 30-mal lockerer sein, unter der Gauss-Annahme also etwa
  30 sigma. [E/H]

Schritt 5, Probe mit der Literaturform von Murata u. a. 2026 (arXiv:2605.18212v2, Abschnitt 5.2, Gl. (3),
V = V_N [1 + (Lambda/r)^n]): [S, WebFetch-Zusammenfassung]
- Zuordnung: n = k - 1 = 2, Lambda = r0 sqrt(beta_3) = 1 mm x sqrt(1.30e-4) = 11.4 um, Probe 11.4^2 = 129.96. [E]
- Blase: (Lambda/r)^2 = (3/2)(L/r)^2, also L = Lambda/sqrt(1.5) = 0.8165 Lambda. [E]
- Die dort genannte HUST-Grenze Lambda < 11 um (n = 2, Tan u. a. 2020) gibt L < 0.8165 x 11 = 9.0 um. [E]
- Die Konfidenz nennt die Zusammenfassung nur als "95 % implied"; das Vorzeichen deckt Gl. (3) mit "+" ab. [L?]

Kurz: Unabhaengig nachgerechnet ergibt sich L <= 9.3 um (68 %), grob <= 13 um (95 %, Gauss-Annahme). Das
stimmt mit der DD-SPUREN-Kopfrechnung (L <~ 9 um) ueberein. Der Wert von 2024 liegt in beta 30-fach
darueber. [E]

### Frage 4: Gruende, warum die Abbildung nicht passt (Gegensweep)

G1, Gueltigkeit der Reihe (der wichtigste Punkt):
- Mit x = rho/L ist das Verhaeltnis zweiter zu erster Korrektur aus QA Gl. (67):
  [3(31 - 18 ln x)/x^5] / [-(3/2)/x^3] = 2 (18 ln x - 31)/x^2. [E]
  - Gleiches Vorzeichen (mehr Schwaechung) fuer ln x > 31/18 = 1.722, also x > 5.6.
  - Groesster Wert bei ln x = 80/36 = 2.22, x = 9.2: 2 x (40 - 31)/85 = +0.21.
  - x = 5.9: ln 5.9 = 1.776, 18 x 1.776 = 31.97, also 2 x 0.97/34.9 = +0.056.
  - x = 4: ln 4 = 1.386, 18 x 1.386 = 24.95, also 2 x (-6.05)/16 = -0.76.
  - x = 3: 2 x (19.77 - 31)/9 = -2.5, die Reihe bricht zusammen.
- An der Grenze L = 9.3 um ist der kleinste Abstand 55 um, also x = 5.9. Ueber den ganzen Datenbereich
  traegt die naechste Ordnung 0 bis +21 % zur Schwaechung bei, mit gleichem Vorzeichen. Der reine
  k = 3-Term ist dort also konservativ; die Schranke ist in sich stimmig. [E]
- Bei L = 51 um ist x = 1.1 beim kleinsten Abstand; dort gilt die Reihe nicht. [E]
  - Nach QA Gl. (64)/(65) und Fig. 4 wird die Schwerkraft unterhalb von L aber noch schwaecher (5D-Regime). [S]
  - Die wahre Abweichung bei 55 bis 100 um waere also gross, nicht klein. [H]
  - Ab x >= 5.6 (r >= 290 um) gilt die Reihe; dort betraegt das Defizit noch 1.5/x^2 = 4.8 % bei x = 5.6.
    Rechnung: 1.5/31.4 = 0.048. [E]
- Eine saubere Zahl fuer 13 um < L < 51 um verlangt einen Neufit mit dem vollen Potential QA Gl. (66) ueber
  Geometrie und Daten. Das geht nur mit den Rohdaten. [H]
- Absicherung der Rechnung:
  - Die Exponenten folgen aus der Dimension (1/rho gegen L^2/rho^3 gegen L^4/rho^5). [E]
  - Der Koeffizient 3/2 stammt aus dem HTML-Rendering. Damit 51 um die 68-%-Grenze bestuende, muesste er
    unter 1.3e-4/2.601e-3 = 0.050 liegen. Ein Lesefehler um Faktor 2 bis 3 aendert das Urteil nicht. [E]

G2, Abstandsbereich: Kapner u. a. 2007 decken 55 um bis 9.53 mm ab [L?]. Fuer L <= 9.3 um liegt der ganze
Bereich im Gueltigkeitsgebiet (siehe G1). Ein Potenzterm wird nicht exponentiell abgeschnitten; die Daten bei
grossen Abstaenden tragen mit. [H]

G3, Material: Die Blasenkorrektur sitzt im Propagator G(q) und koppelt an T_ab wie die Newton-Kraft
(QA Gl. 60). [S] Sie ist daher materialunabhaengig, und QE fittet beta_k mit M_a M_b, das passt. [H]
- Gegenstimme: Basile, Borys, Masias 2025 (arXiv:2507.03748; QA zitiert sie als Ref. 6) finden, dass
  "the gravitational and inertial masses of the proton differ significantly". [L?, Abstract]
- Das waere ein eigenes Problem des Modells (Aequivalenzprinzip). Am Verhaeltnis beta_3 aendert es nichts,
  solange Newton-Term und Korrektur dieselbe Quelle haben. [H]

G4, Abschirmung: Zwischen Pendel und Attraktor liegt eine Isolationsfolie; Lee 2020 nennt "the thicknesses of
the isolation foil". [S] Fuer die Blase gibt es keinen Abschirm- oder Chamaeleon-Mechanismus. Es ist
linearisierte Schwerkraft (QA Gl. 60), sie geht durch die Folie. [H] Die Abschirmung, die QE bei Chamaeleons
behandelt (Fig. 4, BeCu-Folie), gilt hier nicht. [S/H]

G5, Geometrie: QE fittet den Potenzterm fuer die echte Testmassen-Geometrie. [S: "fitting the combined data"]
Weil QA Gl. (60) linear ist, gilt Superposition, und die Abbildung auf Punktmassen-Ebene genuegt. [H]
Alle Paare Pendel-Attraktor-Element liegen mindestens um den Spalt (>= 55 um) auseinander. [H]

G6, Konfidenz und Vorzeichen: Die Tabelle gilt fuer 68 % und fuer abs(beta) [S]. Der 95-%-Wert ist
geschaetzt (Frage 3, Schritt 4). Das negative Vorzeichen der Blase ist durch den Betrag gedeckt. [H]

G7, Falsche Vergleichsgroessen (moegliche Ursache, warum 50 um in der Literatur stehen blieb):
- QB nennt die Blase eine Umsetzung von Sundrums "fat graviton". QE begrenzt diesen auf l_g <= 98 um (95 %).
  [S] Dieser Wert passt nicht zur Blase: Die Fat-Graviton-Kraft wird mit exp(-(0.914 r/l_g)^3) abgeschnitten.
  QE selbst sagt, sie "falls off much more rapidly". [S] Die Blase hat dagegen einen Potenzschwanz. Wer
  98 um nimmt, laesst 51 um faelschlich durch. [H]
- Ebenso gelten die Yukawa-Grenzen nicht fuer einen Potenzschwanz [H]:
  - 56 um, Kapner 2007 [L?]
  - 38.6 um, Lee 2020 [S]
  - 48 um, Tan 2020 [L?]
- QA schreibt, die Grenzen laegen "of precisely this order of magnitude". [S] Das passt zu diesen
  Yukawa-Skalen, nicht zur beta_3-Schranke. [H]

G8, Spaetere, staerkere Potenzterm-Schranken:
- Lee u. a. 2020 (Eot-Wash, arXiv:2002.11761, PRL 124, 101101): Abstaende 52 um bis 3.0 mm, Yukawa
  lambda < 38.6 um (95 %), Extradimension < 30 um. [S] Keine beta_k-Werte im Haupttext. [S, Volltextsuche]
  Ein staerkerer k = 3-Wert waere nur durch Neuauswertung zu haben. [H]
- Tan u. a. 2020 (HUST, PRL 124, 051301, laut INSPIRE ohne arXiv): "the constraints on the power-law
  potentials are improved by about a factor of 2 for k=4 and 5". [L?, Abstract] Fuer k = 3 steht dort keine
  Verbesserung. [L?]
- Murata u. a. 2026 (arXiv:2605.18212v2): HUST, n = 2, Lambda < 11 um, also L < 9.0 um (Frage 3, Schritt 5).
  [S/L?] Das ist praktisch dieselbe Schranke wie QE 2007, Lambda = 11.4 um.
- Die LHC-Zahl (Lambda < 4 um, ATLAS 2021) ist aus einem ADD-Modell umgerechnet. Auf die Blase uebertraegt
  sie sich nicht. [H]
- Ergebnis G8: Keine wesentlich staerkere direkte k = 3-Schranke gefunden. QE 2007 bleibt bis auf etwa
  10 % der Massstab. [H]

G9, Modellinterne Luecke: Ob im vollen Modell weitere Beitraege hinzukommen (etwa eine Branen-Biegung
ausserhalb von G(q)), konnte ich nicht pruefen. [offen]

## 3. Erwartungen B1 bis B3

| Nr | Erwartung (Karte, vorab) | Ausgang | Beleg |
|---|---|---|---|
| B1 | Abbildung auf einen einzelnen Potenzterm, k = 2 oder 3 (60 %) | eingetroffen | k = 3, beta_3 = -(3/2)(L/1 mm)^2 in fuehrender Ordnung. QA Gl. (67), QB Gl. (23), QE Gl. (18). Gilt fuer r >= 5.6 L; die naechste Ordnung traegt dort 0 bis +21 % mit gleichem Vorzeichen bei (Frage 3 Schritt 1, Frage 4 G1) [S/E] |
| B2 | Schranke L <~ 20 um, innerhalb Faktor ~2 der Kopfrechnung, 50 um ausgeschlossen (55 %) | eingetroffen | L <= 9.3 um (68 %, QE Tabelle I), grob <= 13 um (95 %, Gauss-Annahme). 51 um liegt in beta 30-fach darueber, in L 5.5-fach. Deckt sich mit der Kopfrechnung (9 um). Frage 3 [E] |
| B3 | Weder Danielsson/Giri noch Dritte haben die Variante mit Adelberger 2007 verglichen (70 %) | eingetroffen nach Suchstand (nicht abschliessend) | Kein Vergleich gefunden, siehe Liste unten [S/L?] |

Belege zu B3 (Suchstand):
- QA, Literaturliste (INSPIRE, 33 Eintraege): keine Arbeit von Eot-Wash oder HUST; nur das Review
  Murata u. a. 2015 (CQG 32, 033001). [S]
- QB, Literaturliste (INSPIRE, 39 Eintraege): Sundrum 2004 (fat gravitons), aber nicht QE, obwohl QE genau
  diese Variante testet. [S]
- INSPIRE-Zitate: QA hat 2, beide mit Danielsson. QV hat 14, davon 8 ohne Danielsson in der Autorenliste
  (bei den Vorlesungen 2412.08690 nur die ersten fuenf Namen gesehen). [S]
- Abstracts von 2 der 8 Arbeiten ohne Danielsson geprueft (2507.03748, 2411.05912): kein Vergleich. [L?]
  Bei den uebrigen 6 nur die Titel gesehen, keiner deutet auf einen Test des Abstandsgesetzes. [L?]
- Murata u. a. 2026 (Review): keine Erwaehnung der Blase. [S, WebFetch-Suche]
- QV selbst nennt "a modification of gravity at scales of order a few 10^-5 m" ohne Datenvergleich. [L?]

Bedeutung gemaess Karte (B1 und B2 eingetroffen): Die dunkle Blase im Parameterwert von 2024 ist nach unserer
Lesung schon durch Daten von 2007 ausgeschlossen [E, L5]. Vor jeder Weitergabe braucht es eine dritte
Nachrechnung und den Quellenabgleich.

Zusatz des Pruefers [H], nicht Teil der vorab festgelegten Bedeutung:
- QA und QB legen L nur auf "of order 10^-5 m" fest. Die Schranke schneidet den oberen Teil dieser
  Groessenordnung ab. L = 10 um liegt mit Faktor 1.15 knapp an der 68-%-Grenze.
- Das Modell als Ganzes ist damit nicht ausgeschlossen, nur der Wert von 2024.

## 4. Grenzen und Abrufprotokoll

Grenzen:
1. Lesetiefe der Quellen:
   - QA, QB und QV las ich ueber WebFetch (HTML, Zusammenfassung durch ein Kleinmodell). Im alttext von QA
     Gl. (67) erscheinen die Exponenten verstuemmelt als Indizes ("3L_{2}/(2 rho_{3})").
   - Gestuetzt wird die Lesung durch QB Gl. (23) (gleiche Reihe) und die Dimensionsprobe.
   - Den Koeffizienten 3/2 habe ich nicht an der LaTeX-Quelle geprueft; zur Robustheit siehe Frage 4 G1.
   - Den Term zweiter Ordnung, 3L^4(31 - 18 log(rho/L))/rho^5, halte ich fuer weniger sicher gelesen. Er
     betrifft nur G1.
2. Gegenlese-Stand der uebrigen Quellen:
   - QE habe ich vollstaendig als PDF gelesen (Seiten 1 bis 4) [S].
   - Kapner 2007 und Tan 2020 kenne ich nur aus dem Abstract [L?].
   - Hoyle 2004 nur aus QE Tabelle I.
   - Murata u. a. 2026 nur aus der WebFetch-Zusammenfassung.
3. QE nennt nur 68 %. Der 95-%-Wert (rund 13 um) beruht auf einer Gauss-Annahme [H].
4. Es gibt keinen Neufit mit dem vollen Potential QA Gl. (66), der echten Geometrie und den Rohdaten. Fuer
   L > ~13 um ist die Reihe bei den kleinsten Abstaenden nicht gueltig. Der Ausschluss von 51 um stuetzt sich
   dort qualitativ auf die noch staerkere Schwaechung unterhalb von L. Das ist ein Kandidat fuer die dritte
   Nachrechnung.
5. Die B3-Suche ist nicht abschliessend: nur INSPIRE und arXiv-API, kein WebSearch (Kontingent erschoepft),
   keine Volltexte der zitierenden Arbeiten.
6. Rechnen und Ablage:
   - Ich habe nicht auf der .69 gerechnet; die feste Prueferregel verbietet ssh. Alles ist Kopfrechnung mit
     offengelegtem Weg.
   - WebFetch legte die zwei PDFs (QE, Lee 2020) selbst unter ~/.claude/projects/.../tool-results/ ab.
   - Gelesen habe ich sie mit Read und pdftotext nach stdout. In den Scratchpad wurde nichts geschrieben.
7. Blindheit: dd-spuren/ und RUNDE-23.md habe ich nicht geoeffnet. Bekannt war nur die Kartenangabe "L <~ 9 um".

Abrufprotokoll (Zeitfenster zwischen date-Messungen; Einzelzeiten habe ich nicht gemessen):
- 21:50:37 bis 21:55:37 CEST:
  - Karte gelesen.
  - arXiv-API au:Danielsson AND au:Giri (18 Treffer).
  - arxiv.org/abs/2511.21362v2 und /abs/2606.20942v1.
  - arxiv.org/html/2511.21362v2, fuenf Abrufe: Formeln, Abschnitt, Gl. (63) bis (69), Suchbegriffe,
    Literatur.
  - arxiv.org/html/2606.20942v1.
  - arXiv-API au:Danielsson_U AND bubble, abs:"dark bubble".
  - /abs/2311.14589v2 und /html/2311.14589v2.
  - INSPIRE arxiv:2311.14589, mit Ergebnis PRD 109, 026003 (2024).
  - /abs/hep-ph/0611223 und /pdf/hep-ph/0611223v3, davon Seiten 1 bis 4 gelesen.
- 21:55:37 bis 22:03:06 CEST:
  - /html/2511.21362v2 (alttext) und /html/2311.14589v2 (Tabelle 1).
  - /abs/hep-ph/0611184 (Kapner).
  - INSPIRE refersto hep-ph/0611223; die Abfrage war fehlerhaft, das Ergebnis ist nicht verwertet.
  - arXiv-API Adelberger (zwei Abfragen).
  - /pdf/2002.11761v1 (Lee 2020), per pdftotext durchsucht.
  - arXiv-API "inverse-square" AND "power-law".
  - /html/2605.18212v2, zwei Abrufe.
  - Zwei arXiv-API-Abfragen zu Tan 2020, beide 0 Treffer.
  - INSPIRE doi:10.1103/PhysRevLett.124.051301.
  - INSPIRE refersto arxiv:2511.21362; die Abfrage war fehlerhaft, das Ergebnis ist nicht verwertet.
  - INSPIRE arxiv/2511.21362 und arxiv/2606.20942 (Literaturlisten).
  - INSPIRE refersto:recid:3086780 (2 Treffer) und refersto:recid:2726049 (14 Treffer).
- 22:03:06 bis 22:06:12 CEST: /abs/2507.03748 und /abs/2411.05912.
- Danach keine weiteren Abrufe.

## 5. Einfach gesagt

Eine neue Theorie sagt, dass die Schwerkraft auf winzigen Abstaenden etwas schwaecher wird. Wie stark, haengt
von einer Laenge L ab. Ein Labor in Seattle hat 2007 mit einer sehr feinen Drehwaage gemessen, wie sich kleine
Metallscheiben anziehen, und keine solche Schwaechung gefunden. Umgerechnet darf L hoechstens etwa 9 bis 13
Mikrometer betragen, rund ein Zehntel einer Haaresbreite. Der Wert von 2024, etwa 50 Mikrometer, haette eine
dreissigmal groessere Abweichung erzeugt, als die Messung zulaesst. Die neuere Fassung der Theorie mit "etwa
10 Mikrometer" liegt dagegen genau am Rand und ist nicht ausgeschlossen.
