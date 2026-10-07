# BEUTEL-1 Ergebnis (Runde 16, explorativ nach v3)

- Code-Agent, geschrieben ab 2026-10-02 09:13:56 CEST (date).
- Grundlagen:
  - Karte: KARTE.md (verbindlich, unveraendert).
  - Plan: PLAN.md.eingefroren-20261002-085745, eingefroren vor jedem Rauchtest und jedem .69-Lauf.
  - Nachtrag: PLAN-NACHTRAG-1.md.eingefroren-20261002-090719 (NACHTRAEGLICH, nach Lauf 1).
- Gewertet wird Lauf 1 (.69, Spur cpu6, 09:02:52 bis 09:03:07 CEST; Auswertung 09:05:35). Lauf 2 (Nachtrag)
  wiederholt Lauf 1 bitgleich.
- Alles ist modellintern. Es gibt keine Messdaten, und die Aussagen gelten nur fuer die drei Potentiale der Karte.

## 1. Ergebnis zuerst

1. **Alle sieben Vorhersagen B1 bis B7 sind eingetroffen.** Fuer Finns Frage gilt deshalb die vorab festgelegte
   Bedeutung:
   - Im Zweifeldmodell M2 baut sich der Ball eine eigene Huelle (chi(0) -> 0 innen, Friedberg-Lee-artige Struktur).
     Er bleibt aber ein Tropfen (E ~ Q) und wird kein Beutel. Die Huelle allein macht ihn nicht zum Hadron-Analogon.
   - Beutelverhalten (E ~ Q^(3/4)) entsteht erst mit freiem Inhalt in der Huelle (M3): masselos und ohne
     Selbstwechselwirkung.
   - Also: gleiche Familie, nicht dasselbe.
   - Literatur [L, Abstract arXiv:2405.09262]: Fuer FLS-Solitonen geht E bei grosser Ladung wie Q^(3/4). Mit einem
     stabilen Kondensat bzw. einer neuen Massenskala wird daraus das lineare Gesetz (Abschnitt 5a).
2. **M1 (Projektmodell):**
   - Grenzwerte auf dem Duennwand-Ast: E/Q -> 0,707106 und S(0) -> 1,000001. Fit in Q^(-1/3), Q bis 1e8, Radius bis 256.
   - p = d ln E / d ln Q liegt auf beiden Aesten zwischen 0,915 und 0,999 und nie im Band 0,70 bis 0,80.
3. **M2 (Codex-Zweifeldmodell):**
   - chi(0) faellt ab Q ~ 370 unter 0,1. Am Dickwand-Ende (omega^2 = 1,99) ist chi(0) = 0,960.
   - Grenzwerte auf dem Duennwand-Ast: E/Q -> 0,853266, S(0) -> 1,179653, Huellenanteil h -> 0,14554. Alle drei
     stimmen auf etwa 1e-6 mit der Schreibtischrechnung der Karte ueberein.
   - p liegt zwischen 0,896 und 0,998.
4. **M3 (Kontrolle):**
   - Bei Q = 1e5: p = 0,7503, h = 0,2497, E/Q^(3/4) = 4,187. Die Beutelformel gibt 4,189.
   - Die Q^(3/4)-Strecke (p in 0,70 bis 0,80) reicht von Q = 143 bis 1e5, also ueber einen Faktor 700.
5. **Kontrollen:** Eine Kontrolle wurde nur teilweise erfuellt.
   - Verfehlt: Der Gittervergleich dr 0,04 gegen 0,02 bei festem omega liegt nur fuer M1 innerhalb 1e-4. M2 hat
     1,8e-4, M3 1,9e-4.
   - Nachtrag: Die Konvergenz ist sauber zweiter Ordnung (Fehlerverhaeltnis 4,000). Mit dr 0,02 gegen 0,01 liegen
     alle Werte innerhalb 5e-5.
   - Virial: hoechstens 2,8e-4.
   - dE/dQ = omega: Median 1e-6 bis 3e-6 (Spline-Probe).
   - Konkurrenzzustand: Zwei verschiedene Starts enden bei neun Q-Werten auf derselben Energie (Abweichung <= 2,2e-12).

## 2. Vorhersagen B1 bis B7

Wertungsregeln stehen in PLAN.md Abschnitt 4 (vorab). "->" heisst: Grenzwert aus dem Fit a + b x + c x^2 mit
x = Q^(-1/3) ueber alle Punkte mit Halbwertsradius >= 50.

| Nr | Vorhersage | Ausgang | Zahlen |
|---|---|---|---|
| B1 | M1: E/Q -> 0,7071, S(0) -> 1 (auf 1 %) | eingetroffen | Grenzwert E/Q 0,7071058, S(0) 1,0000005 (23 Punkte, Q 8,1e5 bis 1e8); omega -> 0,70710678. Rohwerte bei Q = 1e8: 0,71004 und 1,00275, ebenfalls im Band |
| B2 | M1: keine Q^(3/4)-Strecke | eingetroffen | p stabil 0,915 bis 0,9986, instabil 0,951 bis 0,990. Kein einziger Punkt im Band 0,70 bis 0,80 |
| B3 | M2: chi(0) < 0,1 bei grossem Q; chi(0) > 0,8 nahe omega^2 -> 2 | eingetroffen | chi(0) = 8e-114 bei Q = 1e8 (Duennwand-Ast); chi(0) = 0,9604 bei omega^2 = 1,99 (Q = 144) |
| B4 | M2: E/Q -> 0,853 +- 0,01, S(0) -> 1,18 +- 0,02 | eingetroffen | Grenzwerte 0,853266 und 1,179653 (Schreibtisch 0,853267 und 1,179652). Rohwerte bei Q = 1e8: 0,85854 und 1,18354 |
| B5 | M2: h -> 0,15 +- 0,02, nicht 1/4 | eingetroffen | Grenzwert 0,145542 (Schreibtisch 0,145541), Rohwert 0,14540 |
| B6 | M2: keine Q^(3/4)-Strecke | eingetroffen | p stabil 0,896 bis 0,998, instabil 0,955 bis 0,995. Kein Punkt im Band |
| B7 | M3: p -> 0,75 +- 0,03, h -> 0,25 +- 0,03, E/Q^(3/4) -> 4,19 auf 15 % beim groessten Q | eingetroffen | Q = 1e5: p = 0,7503 (Rueckwaertsdifferenz; omega Q/E = 0,7503), h = 0,2497, E/Q^(3/4) = 4,187. Zum Vergleich Q ~ 1,07e4: 0,7515 / 0,2485 / 4,180; Q ~ 916: 0,7593 / 0,2408 / 4,137 |

Weitere Zahlen (nicht vorhergesagt, nur Befund):
- **Faltung (Q_min):**
  - M1: Q = 111,9 bei omega^2 = 0,928.
  - M2: Q = 66,0 bei omega^2 = 1,841.
  - M3: Q = 38,1 bei omega^2 = 1,825.
  - Dort liegt E/Q ueber der Vakuummasse: 1,017 > 1, 1,434 > 1,414 und 1,431 > 1,414.
- **E < m Q auf dem stabilen Ast** (Zerfall in freie Quanten energetisch verboten):
  - erst ab Q zwischen 140 und 159 (M1), 74 und 80 (M2), 42 und 45 (M3);
  - nahe der Faltung ist der klassisch stabile Ast also nur metastabil [L?].
- **Huellenbildung in M2:**
  - chi(0) = 0,098 bei Q = 372, unter 0,01 zwischen Q = 1375 und 1719, 0,960 am Dickwand-Ende.
  - Der Huellenanteil h steigt von 0,026 an der Faltung auf 0,1454 bei Q = 1e8.
  - chi(0) aendert sich entlang des ganzen Asts stetig. Hysterese wurde nicht gesehen.
- **M3-Beutel:**
  - chi(0) ist innen exponentiell klein (4e-78 bei Q = 1e5).
  - Die Wand liegt bei r ~ 17 ~ Q^(1/4) = 17,8.
  - S(0) waechst wie im Beutelbild mit R^2 (S(0) = 79 bei Q = 1e5).

## 3. Kontrollen

Laut Plan (Lauf 1, gewertet):

**Zwei Gitter (dr 0,04 gegen 0,02, R_max = 350):**
- Bei festem Q (Q-Ast): E weicht um <= 3,4e-6 (M1), 6,5e-6 (M2) und 2,4e-5 (M3) ab, omega um <= 1,6e-5.
- Bei festem omega (mu-Ast): Q und E weichen um <= 1,0e-4 (M1), 1,8e-4 (M2) und 1,9e-4 (M3) ab.
- Kriterium 1e-4: **teilweise erfuellt** (Q-Ast ja, mu-Ast nur M1).

**Radius (R_max 350 gegen 525, dr 0,04):**
- Alle Unterschiede liegen bei <= 4,4e-16, also bei Maschinengenauigkeit.
- f(R_max)/f(0) <= 1e-19.

**Virial |T - 3P|/T:**
- dr 0,04: hoechstens 1,25e-4 (M1), 2,4e-4 (M2), 2,8e-4 (M3).
- dr 0,02: <= 7,1e-5. dr 0,01: <= 1,8e-5.
- Kriterium < 1e-3: ueberall erfuellt.

**dE/dQ = omega, Trapezprobe je Intervall:**
- Hoechstwerte: 6,8e-4 (M1), 7,8e-4 (M2), 2,0e-3 (M3). Mediane: 5e-5, 7e-5, 1,3e-3.
- Der M3-Wert ist der Quadraturfehler der Probe selbst. Bei Schrittfaktor 1,25 und omega ~ Q^(-1/4) erwartet man
  etwa 1,6e-3.

**p aus Nachbarpunkten gegen omega Q/E:** Abweichung <= 0,0044.

**Loesungen:**
- 237 Grobgitter-Loesungen, alle knotenfrei.
- chi ist ueberall monoton.
- Restfehler je Punkt <= 9,5e-10.

Nachtrag 1 (NACHTRAEGLICH, PLAN-NACHTRAG-1):
- **N1, drittes Gitter dr = 0,01:**
  - Fehlerverhaeltnis (X_0,04 - X_0,02)/(X_0,02 - X_0,01): Median 4,000 in allen Modellen; 10./90. Perzentil
    4,000/4,000. Das ist saubere zweite Ordnung.
  - dr 0,02 gegen 0,01: Q und E <= 4,8e-5 bei festem omega und <= 5,9e-6 bei festem Q. Damit gilt 1e-4.
- **N2, Spline-Probe dE/dQ = omega** (kubischer Spline von omega Q ueber ln Q, je Ast integriert):
  - Median 1e-6 bis 3e-6.
  - Hoechstens 6,3e-4, an der Faltung, wo omega(Q) eine Wurzelspitze hat.
  - Ohne die zwei faltungsnaechsten Intervalle <= 2,7e-4.
- **N3, Konkurrenzzustand:**
  - Gradientenfluss bei festem Q aus zwei Starts: A = Stufe bzw. Beutel, B = Gauss-Profil mit chi = 1 ueberall.
    Danach Newton-Politur.
  - Q-Werte: M1 200, 800, 1e4; M2 150, 1100, 1e4; M3 100, 1000, 1e4.
  - Die Energien von A und B sind gleich (relativ <= 2,2e-12). Kein Nebental gefunden.
- **N4, Reproduktion:** Lauf 2 gibt die Punkte von Lauf 1 bitgleich wieder (Abweichung 0), 81/92/64 Punkte.

## 4. Abbildungen

Alle Abbildungen liegen in aus/auswertung/ und stammen aus Lauf 1. Lauf 2 erzeugt bytegleiche Bilder in
aus/auswertung2/.

- abb1-EQ.png: E/Q gegen Q fuer alle drei Modelle.
  - Stabiler Ast durchgezogen, instabiler gestrichelt.
  - Bei M1 und M2 die Linie omega_0, bei M3 die Beutelkurve (4 pi/3) Q^(-1/4).
- abb2-p.png: p(Q) mit Linien bei 0,75 und 1. Grau ist das Band 0,70 bis 0,80, Punkte sind die Probe omega Q/E.
- abb3-S0-chi0.png: S(0) und chi(0) gegen Q (bei M3 logarithmische y-Achse).
- abb4-profile.png: Profile f und g fuer drei Q je Modell.
  - M1: Q = 315, 1,08e5, 9,4e6.
  - M2: Q = 309, 9,5e4, 1,0e7.
  - M3: Q = 916, 1,07e4, 1e5.
- Punkttabellen: aus/auswertung/punkte-M1.csv, punkte-M2.csv, punkte-M3.csv.
- Gesamtzahlen: aus/auswertung/auswertung.json (Lauf 1) und aus/auswertung2/auswertung.json (mit Nachtrag).

## 5. Grenzen und Selbstanzeigen

**Ablauf:**
- Lokale Rauchtests (dr = 0,08, kleiner Q-Bereich) liefen nach dem Einfrieren und vor Lauf 1. Sie zeigten die
  Trends schon, z. B. M3 mit E/Q^(3/4) ~ 4,18 bei Q = 1e4.
- Danach habe ich Q_max fuer M3 auf 1e5 gesetzt; der Plan sagte "Q >= 1e4". Die Rauchtest-Ausgaben (hilfs/smoke-*) habe ich nach Abschluss geloescht.
- Die B7-Werte liegen auch bei Q ~ 1e4 und Q ~ 916 in allen drei Baendern. Die Wertung haengt also nicht an
  dieser Wahl.

**Auslegung:**
- B3 ist doppeldeutig: In 3D geht Q auch am Dickwand-Ende gegen unendlich, also gibt es dort ebenfalls "grosses Q".
  Ich habe das vor dem Lauf im Plan festgelegt: "grosses Q" bedeutet den Duennwand-Ast.
- B1, B4 und B5 sind Extrapolationen. Die Rohwerte bei Q = 1e8 liegen aber ebenfalls in den Baendern.

**Reichweite:**
- Ich habe nur kugelsymmetrische, knotenfreie Loesungen gerechnet.
- "Stabil" heisst hier nur dQ/domega < 0 [L?]. Es gab keine Zeitentwicklung und keine nichtradialen Stoerungen.
- Die Konkurrenzpruefung lief nur im Radialsektor, mit zwei Starts bei je drei Q-Werten.

**Numerische Pannen:**
- N3, M3 bei Q = 1e4: Der erste Versuch scheiterte fuer Start A.
  - Ursache: Der explizite chi-Schritt ist instabil, weil dt * U_gg ~ 0,05 * 100 > 2 (S(0) ~ 25).
  - Ich habe mit dt = 0,01 wiederholt (code/konkurrenz_m3.py). Danach sind A und B gleich (2,9e-13); Q = 1000
    wurde dabei auf 1e-13 bestaetigt.
  - Der Nachtrag nannte kein dt; das ist ein Ausfuehrungsdetail.
- M2-Fortsetzung: Bei omega^2 = 1,0836 scheiterte Newton zweimal, weil der Praediktor zu weit sprang. Mit halber
  Schrittweite lief es danach glatt weiter.

**Was nicht gemacht wurde:**
- Abgleich mit bekannten M1-Projektwerten: nicht gemacht, weil ich nur Karte, Codex-Datei und eigenen Ordner lesen
  durfte. Zum Abgleich durch die Leitung: Q_min = 111,86 bei omega^2 = 0,9285 und E/Q = 1,0173 dort.
- Literatur, nur auf Abstract-Ebene, siehe Abschnitt 5a. Volltexte habe ich nicht gelesen.
  - Weiter [L?]: das Kriterium dQ/domega < 0 und die Beziehung dE/dQ = omega. Beide stehen in keinem der gelesenen
    Abstracts.
  - Numerisch geprueft sind hier dE/dQ = omega (als Probe) und die Q^(3/4)-Skalierung in M3.

## 5a. Literatur (arXiv-API, nachgetragen ab 09:16:30 CEST)

Ablauf der Abfragen: vier Abfragen scheiterten (dreimal HTTP 429, einmal Zeitueberschreitung); die fuenfte und sechste
(09:15 bis 09:16 CEST) lieferten Treffer. Zitiert wird nur Abstract-Wortlaut.

- **arXiv:2405.09262** (E. Kim, E. Nugaev, Ya. Shnir, "Large solitons flattened by small quantum corrections"):
  - Kernsatz: "the asymptotic of a non-topological soliton's energy at large charge is changed from ~ Q^(3/4) to the
    linear law".
  - Ursache laut Abstract: eine neue Massenskala bzw. ein "stable condensate" im FLS-Modell. Die UV-Vervollstaendigung
    "allows thin-wall approximation".
  - [L, Abstract] Damit ist E ~ Q^(3/4) fuer FLS-Solitonen bei grosser Ladung gestuetzt. Ebenso gestuetzt ist, dass
    ein Inhalt mit eigener Massenskala bzw. Kondensat das lineare Gesetz gibt.
  - Das ist genau der hier gerechnete Unterschied: M3 gibt Q^(3/4). M2 hat innen Masse 1 und ein saettigendes
    Kondensat bei S0 = 1,18 und gibt deshalb E ~ Q. Die Zuordnung von M2 zu diesem Mechanismus ist meine Deutung [H].
- **arXiv:2303.09566** (J. Heeck, M. Sokhashvili, "Revisiting the Friedberg-Lee-Sirlin soliton model"):
  - Das FLS-Modell besteht aus einem komplexen Skalar, der die Noether-Ladung traegt, und einem reellen
    Skalar-Vermittler.
  - Die Autoren nennen "commonalities and differences with Q-ball solitons" [L, Abstract].
  - Das stuetzt die Karten-Aussage "gleiche Familie, nicht dasselbe" nur allgemein.
- **arXiv:2309.09661** (E. Kim, E. Nugaev): Q-Baelle einer effektiven Theorie reproduzieren FLS-Solitonen; dazu
  kommt "condensation of charged bosons on the domain wall" [L, Abstract].
- **arXiv:2605.25243** (Y.-X. Su u. a., 2026), Vorbehalt fuer "stabil":
  - Zitat: "configurations that are classically stable become unstable once Hartree fluctuations are included".
  - Unsere Stabilitaet ist nur klassisch [L, Abstract].

## 6. Laufzeiten und sha256

**Laufzeiten** (.69, Spur cpu6, systemd Service runtime; alle Laeufe rc = 0):

| Lauf | Zeit (CEST) | Laufzeit je Modell bzw. Schritt |
|---|---|---|
| Lauf 1 | 09:02:52 bis 09:03:07 | M1 4,9 s, M2 6,0 s, M3 3,6 s |
| Auswertung 1 | 09:05:35 | 6,3 s |
| Lauf 2 (Nachtrag) | 09:07:56 bis 09:08:37 | M1 10,1 s, M2 12,5 s, M3 18,7 s |
| Konkurrenz M3 mit dt 0,01 | 09:09:14 | 10,2 s |
| Auswertung 2 | 09:10:03 | 7,0 s |

Lokal liefen nur Rauchtests, je unter 1 s.

**sha256 Code** (lokal und auf der .69 gleich):

    f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb  code/beutel.py          (Lauf 1)
    128226b3866c15dbb40d886d11561916f1050869eb9a912343bc979b44d9b7f4  code/auswertung.py      (Auswertung 1)
    6875e6e511283afb3812e23a28722826fe0c1e338f70c09b0474dab16a6a80ad  code/beutel_v2.py       (Nachtrag)
    3aed91dfebcb7e30cd201d4df8528e55f173b3a12ebca397be3e40bcc9c4a871  code/auswertung_v2.py   (Nachtrag)
    6850b3407b2387de8e44d236f9077ebeef2a222fc29b209b9cec5f7e543ab0ff  code/konkurrenz_m3.py   (Nachtrag)

**sha256 Plan:**

    a20dcffd93c202c86806c30e41f9d4c787cab9d9e25f3934a3a5aa5e09395e0a  PLAN.md.eingefroren-20261002-085745
    e1d2325093013d96da0d528090c54ed30f560f2b5339fc95a391970dd9cd0c6d  PLAN-NACHTRAG-1.md.eingefroren-20261002-090719

**sha256 Ergebnisse:**

    e3131929a78a88c1d0a76ac85fcce62983935a057537ac9be65b55ba0642d56e  aus/lauf1/M1.json
    a38b36cd1ffc7b18927d7e2d9663b925c3542ffd951b0601ca9836eefa9e76a0  aus/lauf1/M2.json
    011bf2f2c361f1b9c66b8b83a12a64e4190f316f834ccc29f35fe4e034d6aa91  aus/lauf1/M3.json
    94284ad89327ada1417e73b5cb6300b13af3eeac6a2f1c199f681d0e772663d9  aus/lauf1/M1-profile.npz
    1bb153a166e15d8ca43848613e638e8e0d20978833be6c564dcf7bc33f926d8c  aus/lauf1/M2-profile.npz
    88c48c4ee3f30fa4d0f83ac529dde773c51b649163f8e011813590b8c44e0591  aus/lauf1/M3-profile.npz
    adc663bf582a855264d502315b6a4a092a8c10139229950575461ca87893d6aa  aus/auswertung/auswertung.json
    30bd5f742457704ad5fc6f88a5a3dc5de49e347de3a15dc869b6d0224a9d2f0a  aus/auswertung/abb1-EQ.png
    0e9e5f723e9db986a242b46aec9530e145d09fbc7b531c0025ccc6a227f74839  aus/auswertung/abb2-p.png
    72bda8f72c7f9ee3adee12db2d0adb7c7c7d0606dd32c16a25e7611d4dc5bb1e  aus/auswertung/abb3-S0-chi0.png
    256964b4e9bdf9a438bacf2e09b729cebb8548b6290abfcd3dc0d65c5036caaa  aus/auswertung/abb4-profile.png
    f2abb3aaddbdaf92d53c762d3138e001b55b37d8e898716e0bedf014ab9c415c  aus/auswertung/punkte-M1.csv
    d6ac4d24e05a20ea0c7835b35ef3e19839037e86c08f495f4b063200a4a3a468  aus/auswertung/punkte-M2.csv
    775bb44709c619c06b2ed25ff5441cec845ebeaf0b747ae19c684f2046e04531  aus/auswertung/punkte-M3.csv
    8690cd07f30e4982787830d048ff04affe0e31749972065cff11aaf5073b6472  aus/lauf2/M1.json
    dbd7d7d553ea887aeecf16fefb57f8750d37f8a4da38fdbf0138087391516f99  aus/lauf2/M2.json
    2b5cca1713525e5c10e606816421f2b1d07090ada8b48b152cafe9e30f031315  aus/lauf2/M3.json
    021d179f8287b48b6fad976a209d0da55fdb5af46a7546181b27d60269ac0f12  aus/lauf2/M3-konkurrenz-dt001.json
    c2a3dc739c5e2b3053e5e246d38df86a95a5a093d6ab62ac3de164e537d95a11  aus/auswertung2/auswertung.json

Remote-Spiegel: /home/fmh/fmhc-physics-remote/runde16-beutel-1/ (code/, aus/, aus2/, auswertung/, auswertung2/,
logs/). Logs liegen lokal unter aus/lauf1/logs/ und aus/lauf2/logs/.

## 7. Einfach gesagt

Ein Q-Ball ist ein Klumpen aus einem Feld, der sich selbst zusammenhaelt. Wir haben gerechnet, ob so ein Klumpen
eher ein Wassertropfen ist (doppelt so viel Inhalt kostet doppelt so viel Energie) oder ein Beutel wie bei den
Bausteinen von Atomkernen (doppelt so viel Inhalt kostet nur etwa 1,7-mal so viel).

Unser Projektball ist ein Tropfen. Gibt man ihm ein zweites Feld, baut er sich zwar eine echte Huelle, bleibt aber
trotzdem ein Tropfen. Ein Beutel entsteht erst, wenn der Inhalt in der Huelle frei herumschwingen kann. Die Huelle
allein reicht also nicht: Q-Ball und Hadronenhuelle sind verwandt, aber nicht dasselbe.
