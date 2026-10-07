# ZUS-10: zehn Ideen zu Zusammenhaengen (Runde 9, v3)

- **Beginn: 2026-09-30 07:42:35 CEST (date, erste Messung des Auftrags).** Schreibbeginn dieser Datei: 08:02:07 CEST (date).
  Ende: letzte Zeile (nach dem Schreiben gemessen).
- Auftrag: Leitung claude-primary nach Finn 07:41 ("ideate noch mal 10 ideen zu zusammenhängen und prüfe die"). Bearbeiter:
  Anthropic-Agent (Opus). **Nur Ideation; geprueft wird durch einen frischen Agenten.**
- Gelesen: RUNDE-08.md, RUNDE-09.md (Stand 07:42), RUNDE-08/gf-bic/ERGEBNIS.md (ganz), RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md
  (Abschnitte 1 bis 4.6), RUNDE-08/VORHERSAGEN-SP1.md, RUNDE-09/koll1/PLAN.md, RUNDE-06/ERGEBNISSE-R6-A.md (R-2, R-2z),
  RUNDE-06.md (Z. 120 bis 145), RUNDE-07/ERGEBNISSE-R7-A.md (R5F-c, per grep), Argumentlisten von bic2.py, gfbic.py,
  gfbic_q3.py, t5k.py, r5f.py (per grep), WARUM-SPIN-2.md (Gliedliste, per grep). FA-1 nur ueber RUNDE-09.md.
- Nicht geoeffnet: KS-1-Ergebnisse, T8-SOLL-*, vertraege-20260925/, ks-1-dk-lauf(e)/, Geheimnisordner. Kein Interpreter, kein
  awk, keine Rechnung ausser Kopfrechnung (markiert **(Hand)**).
- Blindheit: Laufordner von SP-1 (RUNDE-08/sp1/lauf-*), KOLL-1 (RUNDE-09/koll1/lauf-*) und BIC-4 habe ich nicht geoeffnet.
  Die Vorhersagen der Ideen 3, 4 und 6 sind deshalb vor jedem Blick auf deren Ergebnisse geschrieben. Idee 1 ist an
  R8-Rasterwerten geeicht; das steht dort.
- Markierungen: **[H]** Hypothese, **[L?]** Literatur aus dem Gedaechtnis, nicht an der Quelle geprueft, **(Hand)**
  Kopfrechnung aus Berichtswerten. **Alles ist Modellaussage; nichts hier ist Messdatenbestaetigung.**
- Codehinweise fuer die Pruefung:
  - `bic2.py pole` und `bruecke` rechnen fest mit beta = 0,5 (Konstante BETA, Zeile 68); `--beta` wirkt nur bei `exakt`
    und `kurve`.
  - `gfbic.py ueberlapp` hat `--xmin --xmax --dx --hp`.
  - Laeufe auf der .69 ueber kleintest.sh, je hoechstens 10 min.

## Uebersicht

| Nr. | Titel | verbindet | Pruefweg |
|---|---|---|---|
| 1 | Zwei Leitern, zwei Formfaktoren: Volumenquelle (j1-Nullstellen) gegen Wandquelle | GF-BIC zweite Leiter, BIC-3 Phasenregel | **Rechnung** gfbic.py ueberlapp |
| 2 | Der Gegenlaeufer ist ein Rotor: Q in Feld 1 plus Anti-Q in Feld 2 am selben Ort | GF-BIC-2, ROT-2, Chem 14, FA-1 | Papier, dann Codeerweiterung |
| 3 | Die zweite Fuetter-Spitze fuehrt ueber die Dimensionsbruecke zur l = 1-Stelle | R5F-b, SP-1 (l = 1 bei 0,7554), Bruecke R6 | **Rechnung** bic2.py bruecke |
| 4 | Rayleigh-Tropfen l = 2: gebunden, dann Wigner-Schwelle, aber keine stille Stelle | Tropfen (R3/R6), Phasenregel | **Rechnung** bic2.py pole |
| 5 | Ordnung der ersten strahlenden Oberwelle: Lebensdauerstufen statt Neuron-Schwelle | Codex eps^4, Tropfen, nu_0 des gemischten Balls, Bio 13 | Papier, Literatur |
| 6 | Kein Dunkelzustand zweier Baelle in 3D (Dicke gegen Wellenleiter) | R-2/R-2z (1D), KOLL-1 (3D), Hierarchie-Toys | Papier; KOLL-1-Lauf (laeuft) |
| 7 | Der Rest der Q/Anti-Q-Vernichtung ist ein Oszillon | Chem 14, Literatur Oszillonen/Ladungstausch | Rechnung t5k.py (kleine Aenderung) |
| 8 | Kavitation und Duennwand-Grenze sind derselbe Koexistenzpunkt | R5F-c (86/91), Duennwand-Theorie | Papier; **Rechnung** r5f.py kavitation |
| 9 | Spinmischung wie im Spinor-Kondensat: Verstimmung schliesst die Instabilitaet | GF-BIC (Einkomponentenball instabil), Spinor-BEC | Papier; 1-Zeilen-Aenderung gfbic.py |

Rechnungen mit den genannten Codes (je hoechstens 10 min): Ideen 1, 3, 4; dazu 8 (r5f.py) und 7 (t5k.py, kleine Aenderung).

---

## Idee 1: Zwei Leitern, zwei Formfaktoren

- **Verbindet:**
  - zweite Leiter (psi_2-Gegenlaeufer): RUNDE-08/gf-bic/ERGEBNIS.md, Abschnitt 3.2 (acht Nullstellen von I(omega)) und R9.1
  - Phasenregel der Atmungsleiter: RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md 4.1; RUNDE-08/VORHERSAGEN-BIC3.md
  - bekannte Physik: Formfaktor einer homogenen Kugel; Bohr-Sommerfeld mit Maslov-artigem Versatz; Cooper-Minimum der
    Photoionisation (Vorzeichenwechsel eines Uebergangsmatrixelements) [L?]
- **Hypothese [H]:**
  - Die zweite Leiter entsteht aus einer **Volumenquelle**: Die goldene Regel enthaelt I = Int Phi f^3 r dr.
    - f^3 ist im Balleinneren flach.
    - Phi ist dort sin(k3 r) mit k3^2 = 9 omega^2 - U'(S0) ~ 8 omega^2, weil im Inneren U'(S0) ~ omega^2 gilt.
    - Fuer eine flache Kugel ist Int_0^R r sin(k r) dr = 0 genau bei tan(kR) = kR, also bei den Nullstellen x_{1,n} von j_1
      (4,4934 / 7,7253 / 10,9041 / 14,0662 / 17,2208 / 20,3713 / 23,5195 / 26,6661 / 29,8116).
  - Mit R = R_tw = 1/(2 sqrt(beta) (omega^2 - 1/2)) wird bei beta = 0,5 die Phase besonders einfach:
    **X = k3 R_tw = 2 omega/(omega^2 - 1/2)** (Hand).
  - Regel: **X_n = x_{1,n} + delta**, delta klein und positiv.
  - Die erste Leiter hat dagegen eine Wandquelle (sp V_c in der Wand) mit anderer Innenwellenzahl k_c -> 1,95. Beide
    Leitern sind Bohr-Sommerfeld-Bedingungen, aber mit verschiedenem Versatz:
    - Volumen: Versatz -> 1/2 (j_1-Nullstellen, asymptotisch (n + 1/2) pi)
    - Wand: theta' ~ 0,68 bis 0,79 in k_c R_tw (VORHERSAGEN-SP1.md)
  - Ein Rydberg-Gesetz (1/n^2) ist damit ausgeschlossen, wie schon ABSTAND zeigt.
- **Eichung (Hand, aus den R8-Rasterwerten, also nicht blind):**
  - X - x_{1,n} = 0,595 / 0,274 / 0,128 / 0,063 / 0,112 fuer n = 1 bis 5 (0,86575 / 0,71079 / 0,64568 / 0,61061 / 0,58852).
  - Der Rest faellt mit n; n = 5 ist nur "knapp" aufgeloest. Fuer n >= 6 nehme ich 0 <= delta <= 0,13.
- **Vorhersage vorab (beta = 0,5, g -> 0, Hand):**

  | n | X-Fenster | omega*^2 | 1/(omega^2 - 1/2) | R8-Raster (unsicher) |
  |---|---|---|---|---|
  | 6 | 20,37 bis 20,50 | **0,5742 +- 0,0003** | 13,5 | 0,57524 |
  | 7 | 23,52 bis 23,65 | **0,5637 +- 0,0002** | 15,7 | 0,56556 |
  | 8 | 26,67 bis 26,80 | **0,5558 +- 0,0002** | 18,0 | - |
  | 9 | 29,81 bis 29,94 | **0,5496 +- 0,0002** | 20,2 | 0,55116 (liegt zwischen n = 8 und 9) |

  - Asymptotischer Schritt der zweiten Leiter in 1/(omega^2 - 1/2): **pi/(2 omega_c) = 2,22 +- 0,02** (n = 6 bis 9). Die
    erste Leiter hat 2,28 bis 2,30. Die zweite Leiter faellt also je Stufe um etwa 0,07 weiter hinter die erste zurueck.
- **Pruefweg (Rechnung, 2 x hoechstens 10 min, .69):**
  - `gfbic.py ueberlapp --xmin 0.545 --xmax 0.5625 --dx 0.0025 --hp 0.02 --out aus-ueberlapp-fein-a`
  - dasselbe mit `--xmin 0.5625 --xmax 0.580`
  - Vorzeichenwechsel von I linear interpolieren; bei Bedarf Kontrolle mit `--hp 0.01`.
  - Papier: dieselbe Variable X auf die erste Leiter anwenden (Gegenprobe).
- **Scheitert, wenn:**
  - eine der Stellen n = 6 bis 9 mehr als 0,0003 ausserhalb ihres Fensters liegt, oder
  - das feine Raster die R8-Werte 0,5752 und 0,5656 bestaetigt, oder
  - zwischen zwei vorhergesagten Stellen eine weitere liegt, oder
  - der mittlere Schritt fuer n = 6 bis 9 bei 2,26 oder mehr liegt (dann verhaelt sich die zweite Leiter wie die erste).
- **Gegenprobe:**
  - Die erste Leiter darf die j_1-Regel in X nicht erfuellen: Sie liegt bei X/pi ~ n + 0,85 bis 0,91 (Hand, n = 1 bis 5),
    mit Schritten ueber pi.
  - Z3 (0,551156 bei g = 0,4985) muss bei g -> 0 in 0,5558 oder 0,5496 muenden. Das verlangt |c| < 0,02 in
    omega*^2 = omega0^2 + c g^2; zum Vergleich hat Z1 c = 0,017.
- **Einfach gesagt:** Die zweite Leiter strahlt aus dem ganzen Ballinneren, die erste nur aus der Wand; deshalb sollten ihre
  stillen Stellen einem anderen, schon bekannten Zaehlgesetz folgen, das sich an den naechsten vier Stellen pruefen laesst.

## Idee 2: Der Gegenlaeufer ist ein Rotor, ein Q-Ball in Feld 1 plus ein Anti-Q-Ball in Feld 2 am selben Ort

- **Verbindet:**
  - GF-BIC: Gegenlaeufer psi_2 ~ f e^{+i omega t} strahlt bei 3 omega; zweite Leiter mit Umlauf -1/+1/+1
    (RUNDE-08/gf-bic/ERGEBNIS.md 1.3, 3.1, R9.1)
  - ROT-2: innerer Rotor der relativen Phase (RUNDE-09.md, Nachtrag 07:42:41)
  - Chem 14: Q und Anti-Q im selben Feld vernichten sich (RUNDE-08.md)
  - FA-1: Stern mit gleichlaeufigen Phasen (RUNDE-08/fa1/ERGEBNIS.md)
- **Hypothese [H]:**
  - Bei g = 0 hat U(S) mit S = |psi_1|^2 + |psi_2|^2 die Symmetrie O(4). Deshalb ist
    psi_1 = cos(alpha) f e^{-i omega t}, psi_2 = sin(alpha) f e^{+i omega t} fuer jedes alpha exakt stationaer (Hand).
  - Das ist ein **gegenlaeufiger Zwei-Feld-Ball**: Feld 2 traegt Antiteilchen. Die relative Phase laeuft mit 2 omega, der
    Zustand ist also ein schneller Rotor.
  - Erst der Paarterm (g J) koppelt die Phasen. Er erzeugt Quellen ~ f^3 e^{-+3 i omega t}, also eine "katalysierte
    Q/Anti-Q-Vernichtung" in freie Quanten bei 3 omega.
  - **Die zweite Leiter ist genau die Menge der stillen Stellen dieses Rotors im Grenzfall alpha -> 0.**
- **Vorhersage vorab:**
  - (a) alpha -> 0: Die Abstrahlrate des Rotors ist die Gegenlaeufer-Breite, -Im nu/g^2 = 8,3e-5 an P1 (R8, 3.1).
  - (b) Endliches alpha: Feld 1 wird bei -3 omega (und ueber sp bei 5 omega) mit Quelle ~ cos(alpha) sin^2(alpha) f^3
    getrieben. Sein Formfaktor gehoert zum Zweikanal-Operator (dp, sp) und nicht zu U'; er verschwindet deshalb an den
    Stellen der zweiten Leiter im Allgemeinen nicht.
    - Folge: **Die stillen Stellen werden fuer alpha > 0 zu Minima.**
    - Restrate / Einhuellende ~ tan^2(alpha) (Hand, fuehrende Ordnung): bei alpha = 0,1 etwa 1e-2 bis 1e-1 der
      Nachbarbreite.
  - (c) Exakte Stille bei endlichem alpha braucht zwei Formfaktoren null, also Kodimension 2: hoechstens isolierte Punkte
    (omega^2, alpha).
  - (d) Langsame Rotoren (Relativfrequenz Omega < (2/3)(1 - omega) bei symmetrischer Aufteilung) strahlen ueber den
    Paarterm linear nicht, weil ihre Quellfrequenzen omega +- 3 Omega/2 unter der Masse liegen (Hand). Das ist eine Antwort
    fuer ROT-2: "wo strahlen sie nicht?"
- **Pruefweg:**
  - Papier (1 h): Linearisierung um den gegenlaeufigen Ball in erster Ordnung in g; pruefen, ob alpha -> 0 exakt die
    R8-Formel mit I = Int Phi f^3 r dr gibt.
  - Rechnung erst nach Codeerweiterung (1 bis 2 h): gfbic.py ueberlapp um den zweiten Kanal (psi_1 bei nu = 4 omega, zwei
    offene Kanaele 5 omega und 3 omega, Koeffizienten wie bic2) erweitern; danach Raster bei alpha = 0,05 / 0,1 / 0,2 um
    0,7107 (je unter 10 min).
  - Literatur: "O(4) Q-ball two complex fields counter-rotating", "Q-ball anti-Q-ball bound state two fields",
    "charge-swapping Q-balls", "U(1)xU(1) Q-balls".
- **Scheitert, wenn:**
  - der Grenzfall alpha -> 0 nicht die R8-Gegenlaeuferbreite ergibt (dann ist die Gleichsetzung falsch), oder
  - die Stelle 0,7107 auch bei alpha = 0,1 und 0,2 exakt still bleibt (Rest < 1e-4 der Einhuellenden); dann gibt es eine
    zusaetzliche Symmetrie.
- **Gegenprobe:**
  - Gleichlaeufige Zustaende (gemischter Ball psi_1 = psi_2, FA-1-Stern) haben statische Paarterme und keine 3-omega-Quelle
    in erster Ordnung in g. Dort darf es keine Entsprechung dieser Leiter geben.
  - In einem Feld (Chem 14) gibt es keine O(4)-Drehung, die Q und Anti-Q am selben Ort stationaer macht; dort vernichten
    sie sich.
- **Einfach gesagt:** Ein Teilchenball in der einen Feldsorte und ein Antiteilchenball in der anderen koennen am selben Ort
  sitzen; nur der Paarterm laesst sie langsam zerstrahlen, und an den Stellen der zweiten Leiter tut er das nicht.

## Idee 3: Die zweite Fuetter-Spitze fuehrt ueber die Dimensionsbruecke zur l = 1-Stelle

- **Verbindet:**
  - R5F-b: Die zweite Fuetter-Spitze ist die ungerade 1D-Mode, 1,7777169 - 1,328e-5 i bei omega^2 = 0,70 (RUNDE-08.md)
  - V6/SP-1: Minimum der l = 1-Breite bei ~0,7554 (RUNDE-08.md)
  - Dimensionsbruecke (RUNDE-06.md; THEORIE 4.2: Nullstellenlinien als Faecher mit epsilon ~ (d - 1))
- **Hypothese [H]:**
  - Die ungerade 1D-Mode und der 3D-l = 1-Atmungspol sind derselbe Pol, stetig ueber d verbunden, wie beim l = 0-Pol in
    Runde 6.
  - Die l = 1-Nullstellenlinie durch (d = 3; 0,7554) kreuzt omega^2 = 0,70 bei kleinerem d.
- **Vorhersage vorab (Hand):**
  - Faecherregel epsilon(d) = epsilon(3) (d - 1)/2 mit epsilon(3) = 0,2554 ergibt d = 2,57 bei omega^2 = 0,70.
  - Bei l = 0 lag die Bruecke um 0,1 bis 0,2 unter dieser Regel.
  - Vorhersage: **V-foermiges Minimum von |Im rho(d)| bei d = 2,5 +- 0,2**, mindestens 100-mal tiefer als die Nachbarn im
    Raster 0,1.
  - Endpunkt bei d = 3: Re rho = 1,76352 +- 0,001 (R6: l = 1 bei 0,70: 1,7635198).
  - Schwaecher [H]: ein zweites Minimum bei d = 1,9 +- 0,25, verzahnt mit den l = 0-Minima (1,5 und 2,25).
- **Pruefweg (Rechnung, hoechstens 10 min, .69):**
  - `bic2.py bruecke --omega2 0.7 --l 1 --start "1.7777169-1.328e-5j" --dims 1,1.25,1.5,1.75,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3 --h 0.02 --budget 540 --out aus-bruecke-l1-070`
  - Gegenprobe gleich danach mit l = 0 (Start 1.4937770-6.716e-5j, dieselbe feine d-Liste).
- **Scheitert, wenn:**
  - im Bereich d = 2,3 bis 2,9 kein V-Minimum liegt, oder
  - die Spur bei d = 3 nicht am 3D-l = 1-Pol endet (Abweichung > 0,005); dann ist die zweite Fuetter-Spitze nicht der
    1D-Verwandte der l = 1-Mode.
- **Gegenprobe:**
  - l = 0 mit feiner d-Liste: Die R6-Minima bei ~1,5 und ~2,25 muessen nach THEORIE 4.2 echte Nullstellen (V-Form) sein.
  - l = 1 und l = 0 muessen sich entlang d abwechseln.
- **Einfach gesagt:** Die zweite Spitze beim Fuettern im eindimensionalen Modell ist vermutlich dieselbe Schwingung wie das
  seitliche Schwappen in 3D, und auf dem Weg von 1D nach 3D muesste sie einmal ganz still werden.

## Idee 4: Rayleigh-Tropfen l = 2: gebunden, dann Wigner-Schwelle, aber keine stille Stelle

- **Verbindet:**
  - Tropfenschwingung: 2D auf 6 bis 7 % (RUNDE-03.md); 3D gebunden bei 0,6 mit rho_2 = 0,0741 (RUNDE-06.md); bei 0,8 breit
    mit 0,19173 - 4,57e-2 i
  - Phasenregel (THEORIE 4.1) und SP-1 (l = 2-Ast endet an der Kante bei ~0,670)
  - bekannte Physik: Wigner-Schwellengesetz Gamma ~ q^(2l+1) fuer eine Resonanz knapp ueber der Schwelle [L?]
- **Hypothese [H]:**
  - Die Rayleigh-Mode ist unterhalb der Kante 1 - omega **ohne Feinabstimmung still** (gebunden, beide Kanaele zu).
  - Beim Kantenuebertritt wird sie eine Resonanz mit Gamma ~ q^5 (l = 2).
  - Oberhalb bleibt ihre Wandphase Phi = q R_tw klein (bei 0,8 etwa 0,32 pi, Hand). Die Phasenregel erlaubt dort keine
    stille Stelle.
  - Die Antwort auf "Wird die Rayleigh-Schwingung an einer Stelle still?" lautet also: ueberall unterhalb der Kante, darueber
    nirgends.
- **Vorhersage vorab (Hand):**
  - Kantenuebertritt bei **omega^2 = 0,70 +- 0,04**. Potenzgesetz aus den R6-Punkten rho_2 ~ epsilon^0,86 ergibt 0,725,
    Rayleigh-Skalierung epsilon^1,5 ergibt 0,68.
  - Knapp darueber gilt **d ln(-Im rho)/d ln q = 5 +- 1,5** (Wigner, l = 2).
  - Von der Kante bis 0,90 waechst -Im rho monoton; **kein V-Einbruch unter 1e-6**; Phi/pi < 0,5.
  - l = 3 tritt frueher ueber die Kante, bei 0,62 bis 0,66 (Rayleigh-Verhaeltnis rho_3/rho_2 = sqrt(30/8) = 1,94).
- **Pruefweg (Rechnung, 2 bis 3 Aufrufe je hoechstens 10 min, .69):**
  - `bic2.py pole --l 2 --omega2 0.64,0.67,0.70,0.73,0.76 --h 0.02,0.01 --bereich alles --out aus-pole-l2-rayl-a`
  - `bic2.py pole --l 2 --omega2 0.80,0.84,0.88 --h 0.02,0.01 --bereich resonanz --out aus-pole-l2-rayl-b`
  - Gegenprobe: `--l 3 --omega2 0.60,0.63,0.66 --bereich alles`
  - Auswertung: niedrigster l = 2-Pol (Re rho < 0,3) gegen 1 - omega; Steigung aus den ersten zwei Resonanzpunkten.
- **Scheitert, wenn:**
  - der Uebertritt ausserhalb 0,64 bis 0,78 liegt, oder
  - die Steigung unter 3 oder ueber 7 liegt, oder
  - auf dem Rayleigh-Ast oberhalb der Kante ein V-Einbruch unter 1e-6 erscheint (dann gibt es einen zweiten Mechanismus
    neben der Phasenregel).
- **Gegenprobe:** l = 3 muss vor l = 2 uebertreten. Ohne Tropfenbild (Ordnung verkehrt) ist die Rayleigh-Deutung des
  3D-Asts zweifelhaft.
- **Einfach gesagt:** Solange die Tropfenschwingung langsamer ist als die leichteste Welle, die sie abgeben koennte, bleibt
  sie ganz von selbst still; wird sie schneller, strahlt sie, und eine stille Stelle wie bei der Atmung gibt es dann nicht.

## Idee 5: Ordnung der ersten strahlenden Oberwelle: Lebensdauerstufen statt Neuron-Schwelle

- **Verbindet:**
  - Codex: Nichtlinear strahlt die stille Atmung ueber die zweite Oberwelle, Fluss ~ eps^4 (THEORIE 4.4; RUNDE-08/gf-bic
    ERGEBNIS 1.4)
  - gebundene Tropfenmode (RUNDE-06, V9: rho_2 = 0,00769 / 0,01386 / 0,02093 / 0,02872 bei 0,52 bis 0,55; 0,0741 bei 0,6)
  - Pseudo-Goldstone-Mode nu_0 des gemischten Balls (ERGEBNIS 2.4)
  - Bio 13: keine Neuron-Schwelle (RUNDE-09.md)
  - bekannte Physik: nichtlineare goldene Regel fuer innere Moden (Soffer und Weinstein 1999; Bambusi und Cuccagna 2011;
    Manton und Merabet 1997, Kink-Wackelmode ~ t^(-1/2)) [L?]
- **Hypothese [H]:**
  - Eine innere Mode der Frequenz rho strahlt erst in der Ordnung k = kleinste ganze Zahl mit omega + k rho > 1 (bzw.
    |omega - k rho| > 1).
  - Dann gilt Fluss ~ eps^(2k) und spaet A ~ t^(-1/(2k-2)) [L?].
  - Lebensdauern springen deshalb in Stufen, wenn k rho(omega^2) die Kante kreuzt. Das ist eine **scharfe Schwelle in
    omega^2**, nicht in der Anregungsstaerke (dort sah Bio 13 keine).
- **Vorhersage vorab (Hand):**

  | Mode | omega^2 | rho | 1 - omega | k | Fluss |
  |---|---|---|---|---|---|
  | stille Atmung P1 | 0,7977 | 1,7446 | 0,107 | 2 | eps^4 (Codex, stimmt) |
  | Tropfen l = 2 | 0,60 | 0,0741 | 0,225 | **4** | eps^8, A ~ t^(-1/6) |
  | Tropfen l = 2 | 0,55 | 0,0287 | 0,258 | **9 bis 10** (Rand) | eps^18 oder mehr |
  | Tropfen l = 2 | 0,52 | 0,0077 | 0,279 | **37** | praktisch ewig |
  | nu_0 gemischt M1 | 0,7557 | 0,0687 | 0,131 | 2 (knapp: 2 nu_0 = 0,137) | eps^4 |
  | nu_0 gemischt M3 | 0,5663 | 0,2182 | 0,247 | 2 | eps^4 |

  - Bei M1 liegt 2 nu_0 nur 0,007 ueber der Kante: Etwas kleineres omega^2 oder kleineres g sollte k auf 3 heben; die
    Lebensdauer springt dort.
- **Pruefweg:**
  - Literatur (1 h): Gesetz A ~ t^(-1/(2k-2)) und Fluss ~ eps^(2k) an der Quelle pruefen; Suchbegriffe "nonlinear Fermi
    golden rule internal mode Klein-Gordon", "Soffer Weinstein radiation damping", "Q-ball internal mode radiation".
  - Papier: k-Tabelle aus den Berichtswerten nachrechnen (Pruef-Agent).
  - Rechnung (optional, ueber 10 min, Codeaenderung): achsensymmetrischer Einzelball mit l = 2-Verformung (koll1.py, voll)
    bei 0,60, eps = 0,02 / 0,04; Energiefluss gegen eps.
  - Klein (unter 10 min): gfbic_gem.py bzw. gfbic.py fuer nu_0 bei M1 mit g = 0,15 / 0,10, um den Punkt 2 nu_0 = 1 - omega
    zu finden (Wechsel k = 2 -> 3).
- **Scheitert, wenn:**
  - die Literatur fuer Ordnung k ein anderes Gesetz nennt (z. B. Fluss ~ eps^(2k-2)), oder
  - eine nichtlineare Rechnung bei 0,60 fuer die Tropfenmode Fluss ~ eps^4 oder eps^6 zeigt (dann oeffnet ein anderer Kanal
    frueher).
- **Gegenprobe:** Die stille Atmung (k = 2) muss eps^4 geben. Das ist bekannt und nur Konsistenz, keine neue Pruefung.
- **Einfach gesagt:** Wie lange eine Schwingung im Ball ueberlebt, haengt davon ab, die wievielte Oberwelle als erste
  entkommen kann; das gibt Lebensdauerstufen mit scharfen Kanten, aber keine Schwelle in der Staerke des Anstosses.

## Idee 6: Kein Dunkelzustand zweier Baelle in 3D (Dicke gegen Wellenleiter)

- **Verbindet:**
  - R-2 und R-2z: 1D, exakt dunkler Zustand, Periode lambda = 2,985 (RUNDE-06/ERGEBNISSE-R6-A.md)
  - KOLL-1: 3D-Paar, J_rad ~ Gamma e^{-iqd}/(qd) (RUNDE-09/koll1/PLAN.md)
  - Codex' Hierarchie-Toys (RUNDE-09.md)
  - bekannte Physik: Dicke/Lehmberg, Paar aus isotropen Strahlern Gamma_+- = Gamma0 (1 +- sin(qd)/(qd)); im 1D-Wellenleiter
    exakt dunkle Zustaende bei Abstaenden n lambda/2 (Wellenleiter-QED); in 3D-Gittern Subradianz nur bei Abstand
    < lambda/2 [L?]
- **Hypothese [H]:**
  - Der 1D-Dunkelzustand ist der Wellenleiter-Fall: nur zwei Abstrahlrichtungen, Gamma_AB = Gamma0 cos(qd + 2 delta).
    Probe (Hand): 1D bei 0,7 mit rho = 1,4938 gibt q = sqrt((0,8367 + 1,4938)^2 - 1) = 2,105, also 2 pi/q = 2,985. Das ist
    genau die R-2-Periode.
  - In 3D gilt fuer s-Wellen-Strahler Gamma_+- = Gamma0 (1 +- sin(qd)/(qd)); einen dunklen Zustand gibt es abseits der
    stillen Stelle nicht.
  - Eine subradiante Kette braucht Abstaende < lambda/2 = pi/q ~ 1,3; die Baelle sind aber ~5 bis 6 breit.
  - Folge: In 3D ist die stille Stelle des einzelnen Balls der **einzige** Weg zu einer verlustarmen Kette.
- **Vorhersage vorab (Hand, 0,76, q = 2,3999):**
  - |Gamma_+ - Gamma_-|/(Gamma_+ + Gamma_-) = |sin(qd)/(qd)| = **0,038 / 0,017 / 0,024 bei d = 10 / 12 / 14**, dazu hoechstens
    +-0,03 fuer Streuung am Nachbarball.
  - Keine kollektive Mode unter 0,9 Gamma0 bei d >= 10.
- **Pruefweg:**
  - KOLL-1 (lin-Stapel, laeuft ohnehin): symmetrische und antisymmetrische Anfangsanregung bei 0,76, Abklingraten auslesen;
    kein eigener Lauf noetig.
  - Papier: sinc-Formel aus der Greenschen Funktion der l = 0-Auslaufwelle herleiten.
  - Literatur: Lehmberg 1970 (PRA 2, 883); Asenjo-Garcia u. a. 2017 (PRX 7, 031024); van Loo u. a. 2013 (Science 342, 1494)
    [L?].
- **Scheitert, wenn:** bei 0,76 und d >= 10 eine kollektive Mode Gamma < 0,5 Gamma0 hat. Dann tragen Nahfeld oder
  Mehrfachstreuung mehr als gedacht, und die Hierarchie-Toys waeren fuer Q-Baelle doch tragfaehig.
- **Gegenprobe:** Im 1D-Code (reflexion.py, R-2) muss die Periode 2 pi/q auch bei einem anderen omega^2 (z. B. 0,6) stimmen.
- **Einfach gesagt:** Auf einer Linie koennen sich zwei Baelle ihre Abstrahlung gegenseitig ganz ausloeschen, im Raum aber
  kaum; im Raum hilft nur, dass jeder Ball fuer sich schon still ist.

## Idee 7: Der Rest der Q/Anti-Q-Vernichtung ist ein Oszillon

- **Verbindet:**
  - Chem 14: Das Paar zerstrahlt, Rest 0,022 (d = 8) bzw. 0,016 (d = 12); 95 % der Energie abgestrahlt, also ~5 % bleiben
    (RUNDE-08.md)
  - bekannte Physik: Oszillonen in Potentialen mit anziehendem phi^4- und abstossendem phi^6-Term ("flat-top oscillons");
    Ladungstausch-Q-Baelle aus nahe gestarteten Q/Anti-Q-Paaren (Copeland, Saffin und Zhou, PRL 113, 231603 (2014);
    Folgearbeiten zur Lebensdauer) [L?]. Unser U = S - S^2 + S^3/2 hat genau diese Form.
- **Hypothese [H]:** Der Rest ist keine langsame Strahlung, sondern ein langlebiges Oszillon, das je nach Lage der Ladungen
  neutral ist oder zwischen links und rechts die Ladung tauscht.
- **Vorhersage vorab:**
  - (a) Energie in |x| < 15 bei T = 1000 mindestens 3 % der Anfangsenergie; zwischen T = 1000 und 3000 faellt sie um weniger
    als den Faktor 2.
  - (b) Hauptfrequenz des Rests Omega zwischen 0,75 und 1,0 (unter der Masse).
  - (c) schwaecher: Die Ladung links wechselt mindestens 10-mal das Vorzeichen, mit Q_links ~ -Q_rechts (Ladungstausch).
    Sonst ist es ein neutrales Oszillon mit |Q_links| < 0,01.
  - (d) Nahe gestartete Paare (d = 4, 6) lassen mehr Rest als d = 8 und 12.
- **Pruefweg (Rechnung, kleine Aenderung):**
  - RUNDE-08/chem14/t5k.py: Abstand und T als Argumente, Messung von Energie in |x| < 15, Q_links, Q_rechts und dem
    Spektrum am Nullpunkt.
  - Laeufe d = 4 / 6 / 8, T = 3000 (1D, p4000, je ~1 bis 3 min).
  - Literatur: "charge-swapping Q-balls", "Q-ball anti-Q-ball collision oscillon", "flat-top oscillon sextic".
- **Scheitert, wenn:** die Energie in |x| < 15 bis T = 2000 unter 0,5 % faellt oder die Restfrequenz ueber 1 liegt; dann war der
  Rest nur verzoegerte Abstrahlung.
- **Gegenprobe:**
  - Einzelball ohne Partner, dieselbe Messung: kein Oszillon-Signal (Chem-14-Kontrolle erweitert).
  - Paar mit relativer Phase pi/2 statt 0: Der Rest sollte sich aendern, wie in der Ladungstausch-Literatur [L?].
- **Einfach gesagt:** Wenn Teilchenball und Antiteilchenball sich vernichten, bleibt vermutlich ein kleiner, lange
  zitternder Klumpen uebrig, den man aus anderen Feldmodellen als Oszillon kennt.

## Idee 8: Kavitation und Duennwand-Grenze sind derselbe Koexistenzpunkt

- **Verbindet:**
  - R5F-c: Kavitation im dichten Kondensat; die Energieregel trifft 86 von 91; fuenf Fehltreffer sind schmale Dellen
    (w = 1 bis 2) (RUNDE-07/ERGEBNISSE-R7-A.md)
  - Duennwand-Grenze S_c = 1/(2 beta), omega_c^2 = min U/S (THEORIE 4.1)
  - bekannte Physik: Laplace-Druck, klassische Keimbildung, Coleman-Keim; der Q-Ball bei festem omega ist ein Sattel wie
    ein kritischer Keim [L?]
- **Hypothese [H] (Hand):**
  - Ein homogenes Kondensat der Dichte S0 mit omega^2 = U'(S0) hat den Druck P = S0 U'(S0) - U(S0) = S0^2 d(U/S)/dS.
    Bei beta = 0,5 gilt **P = S0^2 (S0 - 1)**.
  - Die gerechneten Faelle S0 = 0,70 bis 0,80 stehen unter Zug (P = -0,147 bis -0,128). Nur deshalb kann eine Delle
    aufreissen.
  - Der groesste Zug liegt am Spinodalpunkt S0 = 2/3, der Zug verschwindet bei S_c = 1: Das ist **derselbe Punkt**, der die
    Duennwand-Grenze des Q-Balls festlegt.
  - Q-Ball-Radius und kritischer Hohlraum folgen demselben Laplace-Gesetz, einmal fuer das dichte Innere im Vakuum, einmal
    fuer das Vakuum im gedehnten Kondensat.
  - Schmale Dellen heilen, weil sie schmaler als der kritische 1D-Keim sind (Breite w*(S0)); die Energieregel allein prueft
    das nicht.
- **Vorhersage vorab:**
  - (a) S0 >= 1 (P >= 0): **keine einzige Delle kavitiert**, auch die tiefste nicht.
  - (b) S0 = 0,95: Kavitation nur fuer deutlich breitere Dellen als bei 0,70 bis 0,80.
  - (c) Die 1D-Keimbarriere waechst mit S0 -> 1 monoton gegen 2 sigma_c = 1/sqrt 2 = 0,707. Einheiten
    E = Int(|phi'|^2 + U - omega^2|phi|^2) dx, Wandspannung sqrt(beta) S_c^2/2 (Hand); die Konvention in r5f.py ist zu
    pruefen.
  - (d) Alle fuenf Fehltreffer haben w < w*(S0), alle richtig kavitierenden w >= w*(S0).
  - (e) 3D [H]: Im Inneren eines Q-Balls herrscht Ueberdruck (Laplace), dort kavitiert nichts.
- **Pruefweg:**
  - Rechnung (.69, CPU-Spur, hoechstens 10 min): `r5f.py kavitation --teil raster --s0 0.95,1.05,1.2 --stufe grob`.
    Risiko: F_b ist fuer S0 >= 1 nicht definiert; notfalls nur die Klasse heilt/kavitiert auswerten.
  - Papier bzw. Quadratur: kritischer 1D-Keim (statische Loesung mit f -> f0 bei +-unendlich), Breite w* und Barriere F_b
    je S0.
- **Scheitert, wenn:**
  - bei S0 >= 1,05 eine Delle dauerhaft aufreisst, oder
  - die fuenf Fehltreffer breiter sind als w*, oder
  - F_b fuer S0 -> 1 nicht gegen einen endlichen Wert ~2 sigma_c laeuft (1D).
- **Gegenprobe:** Die bekannten Laeufe bei 0,70 bis 0,80 muessen P < 0 haben (Hand: ja). Ein Lauf knapp oberhalb 2/3
  (z. B. 0,68) sollte die kleinste Barriere zeigen.
- **Einfach gesagt:** Ein dichter Klumpen reisst nur auf, wenn er unter Zug steht, und dieser Zug verschwindet genau bei
  der Dichte, bei der Q-Baelle ihre duenne Wand bekommen; darueber sollte nichts mehr aufreissen.

## Idee 9: Spinmischung wie im Spinor-Kondensat: Verstimmung schliesst die Instabilitaet

- **Verbindet:**
  - GF-BIC: Der einkomponentige Ball ist fuer g != 0 instabil, psi_1 psi_1 -> psi_2 psi_2 exakt resonant; lambda = 0,046 /
    0,126 / 0,294 bei g = 0,2 / 0,5 / 1,0 an P1; Zwei-Moden-Formel trifft bei 0,2 auf 2 % (RUNDE-08/gf-bic/ERGEBNIS.md 1.1)
  - Gesamtformel mit N Komponenten gleicher Masse (KANDIDAT.md)
  - bekannte Physik: Spinmischung im Spinor-Kondensat (m = 0 -> +1, -1), instabil nur in einem Fenster des quadratischen
    Zeeman-Effekts (Klempt u. a. 2010; Luecke u. a. 2011; Kawaguchi und Ueda 2012) [L?]
- **Hypothese [H] (Hand, Zwei-Moden-Naeherung wie PLAN 1.4):**
  - Bekommt psi_2 eine Massenverstimmung delta (Masse^2 = 1 + delta), dann gilt fuer die projizierten Gleichungen
    (delta - 2 omega nu) a = g J K b und (delta + 2 omega nu) b = g J K a, mit K = kappa = <f^4>/<f^2>.
  - Daraus folgt nu^2 = (delta^2 - g^2 J^2 K^2)/(4 omega^2).
  - **Instabil nur fuer |delta| < |g| J kappa**, mit lambda(delta) = sqrt(g^2 kappa^2 - delta^2)/(2 omega). Das ist ein
    Kreisgesetz wie beim Spinor-Kondensat.
  - Probe: delta = 0 gibt an P1 0,2 x 0,4046/1,786 = 0,0453, gemessen 0,0462.
- **Vorhersage vorab:**
  - P1, g = 0,2: Fenster **|delta| < 0,081 (+-10 %)**; bei delta = 0,05 ist lambda = 0,036 (+-10 %); bei delta = 0,10 stabil.
  - Folge fuer die Gesamtformel: Schon kleine Massenunterschiede zwischen den Komponenten schuetzen einkomponentige Baelle
    [H].
- **Pruefweg:**
  - Rechnung nach 1-Zeilen-Aenderung (delta auf die Diagonale des psi_2-Operators in gfbic.py spektrum), dann
    `spektrum --stellen P1 --g 0.2` fuer delta = 0 / 0,05 / 0,08 / 0,10 (je ~4 min, .69).
  - Literatur: "spin-mixing instability quadratic Zeeman window", "parametric amplification spinor condensate".
- **Scheitert, wenn:** die Instabilitaet bei delta = 0,10 bestehen bleibt oder lambda(0,05) ausserhalb 0,030 bis 0,042 liegt.
  Dann ist die Zwei-Moden-Naeherung fuer die Verstimmung unbrauchbar.
- **Gegenprobe:** delta -> -delta ergibt dasselbe Fenster (symmetrisch in delta, Hand). Bei g = 0 bleibt nu = +-delta/(2 omega)
  reell (keine Instabilitaet).
- **Einfach gesagt:** Zwei Teilchen der einen Sorte wandeln sich nur deshalb muehelos in zwei der anderen um, weil beide
  Sorten gleich schwer sind; sind sie etwas verschieden schwer, sollte der reine Ball wieder stabil werden, wie man es aus
  Atomwolken mit Spin kennt.


- **Verbindet:**
    Fresnel-Mitnahme in erster Ordnung gleich Einstein (RUNDE-09/PAPIER-G2-ST2.md)
  - Spin-2-Kette (art-grenzen-20260921/WARUM-SPIN-2.md): Glied 1 (Quelle T_mn, also auch T_0i), Glied 9 (Selbstkopplung),
    Glied 10 (Eindeutigkeit)
  - bekannte Physik: Gordon-Metrik bewegter Medien g = eta + (1 - 1/n^2) u u (analoge Gravitation) [L?]
- **Hypothese [H]:**
    Massstabsfaktor).
  - Mit n^2 - 1 ~ 4 Phi/c^2 gibt sie g_0i = -4 Phi v_i/c^3, also genau Einsteins Wert fuer eine bewegte Masse (Hand).
    Die Mitfuehrung ist damit die Kopplung an T_0i aus Glied 1.
  - Zwei Folgerungen:
    - (a) Das Mitfuehrungsfeld muss das Vektorpotential des Massenstroms sein (Dipol ~ 1/r^2 bei Rotation), keine starre
      Mitdrehung.
    - (b) Nichtlinear ist offen, ob Kerr in (konform skalierter) Gordon-Form darstellbar ist. Fuer die akustische Form
      (raeumlich konform flach) verneint das Garat und Price 2000 ("keine konform flachen Schnitte der Kerr-Raumzeit");
      Visser und Weinfurtner 2005 bilden Kerr nur in der Aequatorebene nach [L?].
    ein Unterscheider ueber Glied 9/10.
- **Vorhersage vorab:**
  - (a) Starre Mitdrehung gaebe eine Praezession ~ 1/r statt 1/r^3. Zwischen GP-B (r ~ 7030 km) und LAGEOS (r ~ 12270 km)
    liegt der Faktor 1,75 statt 5,3 (Hand); das ist durch die uebereinstimmenden Messungen ausgeschlossen.
  - (b) Die Literatur zeigt, dass Kerr nicht exakt als Gordon-Metrik eines isotropen bewegten Mediums geschrieben werden
    kann. Die Abweichung beginnt bei O(a^2 M/r^3) im Spin-Quadrupol.
  - Messbar waere das an Kerr-Ringdown-Obertoenen (LVK) oder an der Form des EHT-Schattens, beides heute auf ~10 % [L?].
- **Pruefweg:**
  - Literatur (1 h): "Kerr metric Gordon optical metric moving medium", "analogue Kerr rotating dielectric", Garat und Price
    PRD 61, 124011 (2000), Visser und Weinfurtner CQG 22, 2493 (2005) [L?].
- **Scheitert, wenn:**
    Papier-Agenten), oder
    Schwarze Loecher ununterscheidbar, und (b) entfaellt.
  Unterschied koennte erst bei schnell rotierenden Schwarzen Loechern auftauchen, falls sich deren Raumzeit nicht als
  bewegtes Medium schreiben laesst.

---

## Nicht aufgenommen (mit Grund)

- **Stelle-Tal gegen eine Q-Ball-Laenge: kein tragfaehiger Zusammenhang.**
  - Das Q-Ball-Modell rechnet in Einheiten m = 1. Jede Laenge (R_tw, 1/kappa_c, 2 pi/q) laesst sich durch Wahl von m auf
    38,75 um legen; das ist keine Vorhersage.
  - Ein Zusammenhang braeuchte ein dimensionsloses Verhaeltnis aus zwei gemessenen Groessen (Memory-Regel "entstandene Skala
    braucht zwei gemessene Groessen").
  - Das einzige dimensionslose Stelle-Mass, lambda0/lambda2 = 1,63 bis 1,70 an der Zungenspitze, haengt an der
    Korrelationsannahme rho = 0,90 bis 0,98 (PAPIER-ST1-G1.md). Ein Abgleich mit Q-Ball-Verhaeltnissen waere
    Zahlenmystik (look-elsewhere).
  - Ausserdem hat das Q-Ball-Modell keinen Gravitationssektor.
- **Quantentropfen (Petrov) als Laborsystem fuer stille Stellen:** zurueckgestellt.
  - Struktur aehnlich (flaches Profil, zwei Bogoliubov-Kanaele, Kopplung mit Vorzeichenwechsel in der Wand).
  - Die Monopolmode grosser Tropfen ist aber gebunden; ueber der Emissionsschwelle liegen nur kleine, dickwandige Tropfen
    oder radiale Obertoene.
  - Die Uebertragung der Phasenregel ist deshalb unsicher. Erst nach Idee 1 und 4 sinnvoll.
- **"Isomere" gegen Kern-Ramsauer-Effekt / Cooper-Minimum:** nur als Literaturanker in Idee 1 genannt, ohne eigene Vorhersage.

## Einfach gesagt

Die zehn Ideen verbinden unsere Einzelbefunde zu wenigen Grundmustern:
- Stille Stellen entstehen, wenn eine Quelle im Ball genau so geformt ist, dass sich ihre Wellen nach aussen ausloeschen.
  Die zweite Leiter folgt einer Kugelform, die erste einer Wandform.
- Schwingungen, die zu langsam fuer jede Welle sind, sind ohnehin still.
- In drei Dimensionen koennen sich zwei Baelle ihre Abstrahlung kaum gegenseitig wegnehmen.
  Gegenstuecke in Kondensaten, Oszillonen und der Gravitationsphysik.

Drei Ideen lassen sich mit vorhandenen Programmen in je zehn Minuten pruefen (1, 3, 4), zwei weitere mit kleinen
Aenderungen (7, 9). Alles hier ist Hypothese im Modell, keine Messung.

**Ende: 2026-09-30 08:06:02 CEST (date, nach dem Schreiben gemessen).** Dauer 23 min 27 s, Budget 35 min.
