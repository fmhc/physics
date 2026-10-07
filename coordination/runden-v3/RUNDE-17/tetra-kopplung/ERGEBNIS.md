# TETRA-KOPPLUNG: Ergebnis (Code-Agent, Runde 17, v3 explorativ)

- Geschrieben ab 2026-10-02 11:23:38 CEST (date). Start der Arbeit 10:54:07 CEST, Plan eingefroren 11:08:43 CEST
  (`PLAN.md.eingefroren-20261002-110843`), vor dem ersten .69-Lauf. Nachtrag 1 eingefroren 11:21:09 CEST, nach den
  Hauptlaeufen, als nachtraeglich markiert (`PLAN-NACHTRAG-1.md.eingefroren-20261002-112109`).
- Alle Rechnungen auf der .69 ueber kleintest.sh, Spur cpu6, alle rc = 0. Die Zeitstempel in den Dateinamen unter `aus/`
  und `logs/` sind UTC (Uhr der .69), also CEST minus 2 h.
- Lineare Elastizitaet, eps = 0,05, k = 1, Bindungslaenge 1. Energien in Einheiten k x (Bindungslaenge)^2. Alle Energien
  skalieren exakt mit eps^2. E_int < 0 heisst Anziehung, E_int > 0 Abstossung.

## 1. Ergebnis zuerst

1. **Runde Klumpen in einem runden Medium spueren sich kaum (K1 eingetroffen).** Im Dreiecksgitter faellt die Kopplung
   zweier Q-A wie 1/d^4, nicht wie 1/d^2: E_int = 0,0037 cos(6 theta)/d^4, Exponent 3,98 bis 4,03. Bei d = 10 ist das
   80- bis 100-mal schwaecher als bei zwei Q-B im selben Gitter. Die Kontrolle M-iso4 (Quadratgitter mit isotropen elastischen
   Konstanten) zeigt dasselbe 1/d^4. Entscheidend ist also die elastische Isotropie, nicht die Gittergeometrie.
2. **Unrunde Klumpen oder ein unrundes Medium koppeln mit 1/d^2 in 2D (K2, K3 eingetroffen).**
   - Anisotropes Quadratgitter, Q-A/Q-A: Achse -0,0023/d^2 (Anziehung), Diagonale +0,0036/d^2 (Abstossung).
   - Isotropes Dreiecksgitter, Q-B/Q-B parallel: der Laenge nach -0,0031/d^2 (Anziehung), seitlich +0,0036/d^2
     (Abstossung).
   - Das Vorzeichen haengt von der Richtung und von der Ausrichtung ab. Bei 60 Grad zieht das parallele Paar nicht an,
     es stoesst sich ab (+), das gedrehte zieht an (-).
3. **Im fcc-Raum (Anisotropie A = 2) koppeln schon runde Klumpen mit 1/d^3.**
   - [100]: -0,0019/d^3 (Anziehung). [110] und [111]: +0,0013/d^3 bzw. +0,0022/d^3 (Abstossung).
   - Gemessene Exponenten: 2,98, 3,13 und 2,89.
   - K4 ist nach der vorab festgelegten Regel trotzdem **offen**: Auf [111] lagen zu wenige Punkte fuer das untere
     Halbfenster. Die nachtraegliche Zusatzrechnung im groesseren Gitter erfuellt alle Kriterien ([111]: 2,91, Band
     2,84 bis 2,96); den Ausgang aendert sie nicht.
4. **K5 nicht eingetroffen.** Zwei parallele Q-B sind im fcc nicht in jeder Richtung staerker gekoppelt als zwei Q-A.
   - Entlang ihrer eigenen Achse [110] faellt ihr Verhaeltnis von 1,8 (d = 4) auf 0,51 (d = 22).
   - In [100] liegt es bei etwa 3,9, in [111] bei etwa 2,3.
   - Auf gleiche Quellstaerke normiert ist Q-B nur in [100] staerker (1,05 bis 1,10).
5. **Bedeutung fuer Finn (gemaess Karte, K1 bis K3 eingetroffen):** Spannungen koppeln verspannte Klumpen, aber nur,
   wenn Klumpen oder Umgebung "unrund" sind. Runde Klumpen in einem runden Medium spueren sich kaum (1/d^4 statt 1/d^2).
   Ob anziehend oder abstossend, haengt von Richtung und Ausrichtung ab. Die Kraft entsteht aus der Geometrie und ist
   nicht eingesetzt [H]. Zusatz aus K5: "unrund" heisst nicht automatisch "staerker". Laengs der gemeinsamen Achse
   koppeln zwei laengliche Klumpen ab d = 8 schwaecher als zwei runde; vermutlich heben sich runder und laenglicher Anteil
   dort teilweise auf [H].

## 2. Vorhersagen K1 bis K5

Exponent n = -Steigung von log abs(E_int) gegen log d im Fernfenster: 2D [16, 50], fcc [7,5, 22,6]. In Klammern stehen
die Exponenten der unteren und der oberen Fensterhaelfte (Band). Vorzeichen: "+" abstossend, "-" anziehend.
Vorfaktoren als Mittel von d^m E_int im Fenster.

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| K1 | M-iso, Q-A/Q-A faellt schneller als 1/d^2, Rest ~ 1/d^4 (75 %) | **eingetroffen** (auch "~ 1/d^4" in allen drei Richtungen) | 0 Grad: n = 4,02 (4,04; 4,01), "+", d^4 E = +0,0037. 19,1 Grad: n = 4,03 (4,04; 4,02), "-", -0,0016. 30 Grad: n = 3,98 (3,97; 3,99), "-", -0,0036. Form: 0,0037 cos(6 theta)/d^4 (fig-winkel) |
| K2 | M-aniso2, Q-A/Q-A ~ 1/d^2, Vorzeichenwechsel Achse gegen Diagonale (70 %) | **eingetroffen** | Achse 0 Grad: n = 2,00 (2,00; 2,00), "-", d^2 E = -0,0023. Diagonale 45 Grad: n = 2,02 (2,02; 2,01), "+", +0,0036. Zwischen 26,6 Grad (nicht entscheidend): n = 1,88 (1,76; 1,96), "+", +0,00015, nahe einem Nulldurchgang; Vorzeichenwechsel im Gesamtfenster bei d = 6,7 bis 8,9 |
| K3 | M-iso, Q-B/Q-B ~ 1/d^2, ungleich null, Vorzeichen haengt von der Orientierung ab (80 %) | **eingetroffen** | Parallel: 0 Grad n = 2,00 "-" (-0,0031); 19,1 Grad 2,00 "-" (-0,0026); 30 Grad 2,01 "-" (-0,0018); 60 Grad 2,03 "+" (+0,0016); 90 Grad 1,99 "+" (+0,0036). Um 60 Grad gedreht: 0 Grad "-" (-0,0010, naeh.); 19,1 Grad "-" (-0,0014, naeh.); 30 Grad "-" (-0,0014, exakt); 60 Grad "-" (-0,0010, naeh.); 90 Grad "+" (+0,0007, naeh.); n = 1,96 bis 2,02. Entgegengesetzt bei 60 Grad |
| K4 | M-fcc, Q-A/Q-A ~ 1/d^3, Vorzeichenwechsel [100] gegen [111] (65 %) | **offen** (nach Regel; Daten passen) | [100]: n = 2,98 (2,99; 2,97), "-", d^3 E = -0,0019. [110]: 3,13 (3,21; 3,07), "+", +0,0013. [111]: 2,89 (unteres Halbfenster nur 2 Punkte, nicht berechenbar; oberes 2,93), "+", +0,0022. Nachtraeglich (M = 80, Fenster [9,4, 28,3]): [100] 2,99 (2,99; 2,98), [110] 3,08 (3,12; 3,06), [111] 2,91 (2,84; 2,96), Vorzeichen gleich |
| K5 | M-fcc: abs(E_int) fuer Q-B/Q-B groesser als fuer Q-A/Q-A bei gleichem d (70 %) | **nicht eingetroffen** | Verhaeltnis Q-B parallel zu Q-A: [100] 3,86 bis 4,04 (14 von 14 Punkten > 1); [111] 2,12 bis 2,32 (8 von 8); [110] 0,51 bis 1,80, nur 4 von 19 Punkten > 1 (nur d <= 7). Auf gleiche Dipolstaerke normiert ((p_B/p_A)^2 = 3,67): [100] 1,05 bis 1,10, [111] 0,58 bis 0,63, [110] 0,14 bis 0,49 |

- **Weitere Zahlen.** Q-B parallel im fcc entlang der eigenen Achse [110]: n = 3,61 (3,92; 3,43), nachtraeglich 3,41.
  Das Fernverhalten ist dort noch nicht erreicht; der 1/d^3-Anteil ist klein. Die uebrigen fcc-Q-B-Strahlen liegen bei
  n = 2,85 bis 3,00.
- **Zusatzkontrolle M-iso4 (Zusatz, nicht in der Karte):**
  - Q-A/Q-A: n = 3,99 (0 Grad), 3,96 (26,6 Grad), 4,01 (45 Grad), Form -0,0042 cos(4 theta)/d^4.
  - Q-B/Q-B: dagegen 1/d^2 (n = 1,98 bis 2,01, ausser 45 Grad mit 1,76 nahe einem Nulldurchgang).
- **Eigene Vorab-Erwartungen (PLAN Abschnitt 6, nicht bindend):**
  - M-aniso2 Q-A: vorab -0,0022 / +0,0035 / +0,0002, gemessen -0,0023 / +0,0036 / +0,00015.
  - M-iso Q-B parallel: vorab -0,0031 axial und +0,0037 seitlich, gemessen -0,0031 und +0,0036.
  - M-iso Q-A: vorab cos(6 theta)/d^4, so gemessen.
  - Die Kontinuumsrechnung trifft die Gitterwerte auf etwa 5 %.

## 3. Kontrollen

| Kontrolle | Ergebnis |
|---|---|
| C1 FFT gegen spsolve (periodisch, kleine Gitter, alle 4 Medien, Q-A und Q-B) | max. relative Abweichung der Verschiebungen 1,1e-15 bis 5,9e-15 |
| C2 quadratisch in eps (0,025; 0,05; 0,1) | E_self und E_int (vier Terme): Verhaeltnisse genau 4,0 in allen Faellen. Selbstanzeige: Die Verdopplung ist im Binaerformat exakt; der Test zeigt nur, dass der Code kein nichtlineares Glied enthaelt |
| C3 vier Terme gegen bilinear | periodisch (d = 3 bis 6, alle Medien): Abweichung <= 1e-17 absolut (relativ <= 1e-12). Fester Rand (2D, R = 8): E(nur 1) und E(nur 2) unterscheiden sich, z. B. 0,004620 gegen 0,004633; vier Terme = bilinear in beide Richtungen auf <= 4e-18 |
| C4 Energieformel | Bindungssumme = (1/2) s k s - (1/2) f u auf Maschinengenauigkeit |
| C5 elastische Konstanten | M-iso 1,2990 / 0,4330 / 0,4330 (A = 1,000); M-aniso2 2,000 / 1,000 / 1,000 (A = 2,000); M-iso4 1,500 / 0,500 / 0,500 (A = 1,000); fcc 1,4142 / 0,7071 / 0,7071 (A = 2,000) |
| C6 Systemgroessen | Je drei Groessen: 2D n = 100, 200, 400; fcc M = 16, 32, 64. Untergrund b/N siehe unten. Nach Abzug stimmen E_inf aus N2 und N3 auf 5 % bis zum groessten vergleichbaren d: 2D d = 47 bis 50, fcc d = 9,8 bis 11,3 (nachtraeglich 12,2 bis 14,1). Das ist jeweils die Grenze des Vergleichs (L/4 des mittleren Systems), keine gefundene Abweichung. Ausnahmen: M-aniso2 Q-A 26,6 Grad nur bis d = 31 (nahe Nullstelle), M-aniso2 Q-B gedreht 26,6 Grad bis d = 18,6 (Vorzeichenwechsel), M-iso4 Q-B gedreht 26,6 Grad bis d = 38,7, fcc nachtraeglich Q-B parallel [110] bis 13,0. Ohne Abzug nur bis d = 2,6 bis 16 |
| C7 Einzelquelle gegen Eshelby [L?] | E_self(Q-A): M-iso 0,00457 (Kontinuum 0,00138 mit a = 1 bis 0,00500 mit a = WS); M-aniso2 0,01024 (0,0032 bis 0,0100); M-iso4 0,00689 (0,0021 bis 0,0067); fcc 0,01138 (0,0023 bis 0,0133). Alle in derselben Groessenordnung, nahe dem Wert mit a = WS (Gitter durch Kontinuum: 0,91; 1,02; 1,03; 0,85). Von der unrelaxierten Fehlpassungsenergie (1/2) Sum k s^2 bleiben 61, 68, 69 und 76 %. E_self(Q-B): 0,00671, 0,01523, 0,01038, 0,02004 |
| C8 Symmetrie | Gleichwertige Strahlen stimmen auf ~1e-11 relativ (M-iso 0 = 60 Grad, 30 = 90 Grad; Quadrat 0 = 90 Grad, 26,6 = 63,4 Grad; fcc [110] = [1-10], [100] = [001]) |
| Fester Rand (optional, 2D, R = 50 und 100) | Nach Abzug des 1/N-Untergrunds aus beiden Groessen stimmt E_int mit dem periodischen E_inf ueberein: in allen 1/d^2-Faellen (M-iso Q-B parallel, M-aniso2 Q-A und Q-B parallel; Achse und Diagonale) auf <= 0,04 % (d ~ 5), <= 0,2 % (d ~ 10) und <= 0,9 % (d ~ 20), Vorzeichen ueberall gleich. Beim 1/d^4-Fall M-iso Q-A: 0,1 bis 0,2 % (d ~ 5), 2 bis 3 % (d ~ 10), 38 bis 46 % (d ~ 20; dort ist der Randterm 30-mal groesser als das Signal) |

**Untergrund (Bildquellen).**
- Periodisch gilt E_per = E_inf + b/N. Fuer die isotropen Q-A-Faelle stimmt b mit der Formel P^2/(A0 C11):
  - M-iso: numerisch 0,020001 (Streuung 5e-9), Formel 0,020000.
  - M-iso4: numerisch 0,026666, Formel 0,026667.
- Die 1/N-Skalierung bestaetigen die Schaetzungen aus N1/N2 und N2/N3, z. B. M-aniso2 Q-A 0,0376 und 0,0376.
- Ohne diesen Abzug waere K1 nicht entscheidbar gewesen: Bei n = 200 betraegt b/N = 5e-7, das Signal bei d = 50
  dagegen 6e-10.

## 4. Abbildungen (`aus/`)

- `fig-eint-M-iso-20261002-091854.png`, `fig-eint-M-aniso2-...png`, `fig-eint-M-iso4-...png`,
  `fig-eint-M-fcc-...png`: abs(E_int) gegen d (log-log) je Medium. Drei Felder: Q-A/Q-A, Q-B parallel, Q-B gedreht.
  - Gefuellte Punkte bedeuten E > 0 (abstossend), offene E < 0 (anziehend).
  - Grau sind Hilfslinien d^-2/d^-4 (2D) bzw. d^-3/d^-5 (fcc).
  - Gleichwertige Richtungen liegen deckungsgleich uebereinander (C8).
- `fig-winkel-20261002-091854.png`: d^m E_int gegen den Winkel fuer drei d-Ringe (2D, n = 400). Die Kurven fallen
  zusammen. Damit sind Abfallgesetz und Winkelform direkt sichtbar (cos 6 theta, cos 2 theta, cos 4 theta).
- `fig-feld-20261002-091854.png`: Verschiebungsfeld einer Einzelquelle.
  - Gezeigt: M-iso Q-A und Q-B, M-aniso2 Q-A, fcc Q-A und Q-B (Ebene z = 0).
  - Dazu der Abfall abs(u) gegen d: in 2D ~ 1/d, im fcc ~ 1/d^2.

## 5. Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Grenzen**
- Nur lineare Elastizitaet. Nichtlineare Terme (zweite Ordnung, Polarisierbarkeit) sind nicht gerechnet. Das 1/d^4 in
  K1 ist reine Gitterdiskretheit innerhalb der linearen Theorie.
- Q-A und Q-B sind Modellquellen ("rund" und "axial"), keine echten Ikosaeder oder 19er-Cluster. Die fcc-Federn
  erfuellen die Cauchy-Relation (Paarkraefte).
- **Bereich in d:**
  - 2D: Fit bis 50, Daten bis 100.
  - fcc: bis 22,6, nachtraeglich bis 28,3.
  - Asymptotik jenseits davon ist nicht gezeigt. Fuer fcc Q-B entlang [110] ist sie noch nicht erreicht.
- **Gedrehte Q-B:** Wegen des Mittelpunktsversatzes sind manche Strahlen naeherungsweise (Abstand zum Strahl <= 0,55,
  untere Fenstergrenze 5). Die fuer K3 entscheidende 60-Grad-Richtung des gedrehten Paars ist naeherungsweise. Die
  Winkelabbildung zeigt dort einen klaren negativen Wert (Nullstelle erst bei etwa 80 Grad).
- Fester Rand nur in 2D; fuer fcc nur periodisch.

**Selbstanzeigen**
- **Lesen ausserhalb des Ordners:** Ich habe Kopf und Ablaufteil von
  `/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh` gelesen (grep/sed). Ziel war, Aufruf und Logausgabe zu
  verstehen. Dazu kam ein Verzeichnislisting von `/home/fmh/fmhc-physics-remote/` und `RUNDE-17/`.
- **Code nach den Hauptlaeufen geaendert:** Fuer Nachtrag 1 wurde nur der Aufrufzweig von hauptfcc geaendert. Die
  Fassung der Hauptlaeufe liegt unveraendert unter `hilfs/tetra-v1-hauptlaeufe.py`. Fuer die Standardgroessen verhalten
  sich beide Fassungen gleich.
- **K4:** Die Regel "beide Halbfenster" war bei der Planung nicht gegen die duenne [111]-Punktfolge geprueft
  (Schreibtischrechnung je Strahl fehlte). Deshalb ist K4 "offen", obwohl alle verfuegbaren Zahlen passen.
- **K3 ist eine schwache Vorhersage:** Ein einziges entgegengesetztes Vorzeichen in fuenf Richtungen genuegt. Das
  Kreuzglied isotrop mal deviatorisch macht das fast unvermeidlich. Scheitern konnte K3 an Exponent und
  Nicht-Null-Bedingung.
- Hilfsauswertung mit jq (`hilfs/rand_vergleich*.jq`). Lokal liefen kein python, kein awk und kein bc.

**Laufzeiten** (Service-Laufzeit laut kleintest.sh, Spur cpu6, MemoryMax 4 GB)

| Lauf | UTC-Start | Laufzeit |
|---|---|---|
| pruef | 09:18:03 | 1,6 s |
| haupt2d | 09:18:10 | 2,8 s |
| hauptfcc (M = 16, 32, 64) | 09:18:21 | 13,9 s |
| auswert + Bilder | 09:18:54 | 12,0 s |
| rand (fester Rand 2D) | 09:20:11 | 7,1 s |
| hauptfcc-nachtrag (M = 20, 40, 80) | 09:21:44 | 13,7 s |

**sha256**

```
d9a9b8b6d2482a37c9a40495837c662df7183a8867936a134277df7638696d26  hilfs/tetra-v1-hauptlaeufe.py (Hauptlaeufe)
6effbcd7979219769fa5aa0b86209dd4fb157c989eccf94b81e36e31f796b64d  code/tetra.py (Nachtrag 1)
8cd9eea489abf39307f4ff3a6589edf0b2648993f7613aacf722670d2f432e0d  PLAN.md.eingefroren-20261002-110843
299e03ac0c9de592fb70aa26554c14093c727f5cfdec7c0d2afb02dc8827a57a  PLAN-NACHTRAG-1.md.eingefroren-20261002-112109
4183da76d4347d271326895ce04d3a579e510dcacc7d81a15d2560c640713641  aus/pruef-20261002-091803.json
551d7eb6a0dafdb000391e75067be1ff3307dda45c51af2af336cc1611340c73  aus/haupt2d-20261002-091811.json
540231ebae9f51327a61045a86b4dae1195f82d1468e8057bb6f4b1b094e2cc7  aus/haupt2d-20261002-091811.npz
ed4d23a0f365589fe03dcab052094e99cec6337ca5acff0db0990b7fc76a9774  aus/hauptfcc-20261002-091821.json
9aa9851ce70c5fdac9b09be82b7d81f7126d3750731c1cc98de59a9cac425912  aus/hauptfcc-20261002-091821.npz
358f17da51f1e0e8aa9d23f36bc2d24cb86e5d8e923a69e44cd88b7993d69917  aus/auswert-20261002-091854.json
2e41158702c8ccd377fca19f12b8a0d02fc1f287cd2e20f1cddfe92faa353cfd  aus/rand-20261002-092012.json
e8f84c70895d622dfce3d661b95312edb09b5ae8bff08918293b80fe55accf52  aus/hauptfcc-nachtrag-20261002-092144.json
28116cf6794cc55b608e5bcdd69c0612b70c4269d5dbb5bce516303d1463717b  aus/hauptfcc-nachtrag-20261002-092144.npz
df9b8462d6aaa36fbc556857b5688975d04f6c7573449db0bea83786b55404f4  aus/fig-eint-M-iso-20261002-091854.png
27e71e44cff8eeb33433460a1d54ada3c91647bedab96e61b091624c2e5453d7  aus/fig-eint-M-aniso2-20261002-091854.png
d82f909172c4bd1198e7ebd06b4b21a0775399f32183b6c232660dea2039187d  aus/fig-eint-M-iso4-20261002-091854.png
16df189301d593d2cf178aed4559751dcf12f15238f1cc8eccb80353d8e899c4  aus/fig-eint-M-fcc-20261002-091854.png
1d510c3905531938ebe3a76e518b87aec6d226d60e43531a479aedd20b532e61  aus/fig-winkel-20261002-091854.png
d5b0da1c2d0288b825841b42aca5557658cc607b3b2d008b9a855b09ef0a9f96  aus/fig-feld-20261002-091854.png
```

Die JSON- und NPZ-Dateien auf der .69 (`/home/fmh/fmhc-physics-remote/runde17-tetra-kopplung/aus/`) haben dieselben
Hashes. Die Logs liegen in `logs/`.

## 6. Einfach gesagt

Wir haben ein Netz aus Federn gebaut und an zwei Stellen ein paar Federn etwas zu kurz gemacht. So entstehen zwei
"verspannte Klumpen". Dann haben wir gemessen, ob die beiden Klumpen voneinander wissen. Sind Klumpen und Netz
gleichmaessig rund, merken sie fast nichts voneinander. Die Wirkung faellt mit der vierten Potenz des Abstands, also
sehr schnell. Ist einer der beiden laenglich oder ist das Netz in manchen Richtungen steifer, dann spueren sie sich
deutlich und ueber groessere Strecken. In manchen Richtungen ziehen sie sich dann an, in anderen stossen sie sich ab.
Laengliche Klumpen sind aber nicht immer staerker gekoppelt: Hintereinander in einer Reihe spueren sie sich ab
etwa acht Gitterabstaenden sogar schwaecher als zwei runde.
