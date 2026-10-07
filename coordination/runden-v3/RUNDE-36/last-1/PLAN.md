# LAST-1: Plan (Code-Agent, Runde 36)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-03 22:42:21 CEST, Plantext ab 23:02:23 CEST (date).
- Die Vorhersagen L0 bis L4 und ihre Schwellen stehen unveraendert in KARTE.md. Was die Karte offenlaesst, lege ich
  hier vor dem Einfrieren fest; solche Festlegungen tragen das Zeichen [F].
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese, [F] Festlegung.
- Rauchlaeufe vor dem Einfrieren (Abschnitt 9) zeigen nur Kontrollgroessen, Zeiten und die elastischen Konstanten,
  keine Pi_12-Werte.

## 1. Netz und Einheiten

- fcc-Stabnetz wie NETZ-C-1 (Code RUNDE-35/netz-c-1/code/netz_a.py, Modell W1):
  - Stablaenge 1 ("Kantenlaenge 1" wie in NETZ-C-1), kubische Kante a = sqrt2, Volumen je Knoten Omega = 1/sqrt2.
  - Zentralfedern k = 1.
  - Winkelfedern: je Knoten alle 66 Stabpaare, Zeile sqrt(k_theta) d(cos theta) mit normierten Stabvektoren;
    kollineare Paare haben keinen linearen Term.
  - Zwei Fassungen: k_theta = 0 ("aniso") und k_theta = 1/18 ("iso").
- r ist in Stablaengen gemessen [F]. Bei zwei Staeben ist r der Abstand der Stabmitten (= Gitterverschiebung R).
- Periodisches Gitter aus L^3 kubischen Zellen (4 L^3 Knoten, Kante L sqrt2). Rechnung auf dem einfach-kubischen
  Hilfsgitter (2L)^3 mit Weite 1/sqrt2; Knoten sind die Punkte mit gerader Indexsumme.
- Statik: K u = f, geloest je Wellenvektor mit der 3x3-Bloch-Matrix D(q) (Zentral- plus Winkelanteil, aus denselben
  Zeilen wie NETZ-C-1), irfftn auf dem halben Gitter. float64.

## 2. Quellen und Definition von Pi_12

- **(a) Punktlast:** Einheitskraft f = z-Dach auf einem Knoten; beide Lasten gleich gerichtet. [F: f laengs [001].]
  Die Richtung von r relativ zu f wird ueber die Richtungsliste variiert.
- **(b) Dilatationszentrum:** die 12 Staebe um einen Knoten mit Ruhelaenge 1 + delta, delta = 1.
- **(c) zu langer Stab:** ein Stab laengs [110] mit Ruhelaenge 1 + delta; der zweite parallel, um R verschoben.
  [F: Stabrichtung [110].]
- Linear gerechnet: Pi skaliert mit f^2 bzw. delta^2; Vorzeichen und Exponenten haengen davon nicht ab.
- **Eingepraegte Dehnungen:** Ersatzkraefte f = B^T k e0 (e0 = Ruhelaengenaenderung je Stab).
  - Die Winkelfedern behalten ihre Ruhewinkel.
  - Kraefte: f(Ende) = +k delta d-Dach, f(Anfang) = -k delta d-Dach; Nettokraft und Nettomoment sind null.
- **Gesamtpotential:**
  - Lasten: Pi = U_el - f.u.
  - Eingepraegte Dehnung: Pi = U_el (keine aeussere Arbeit).
  - Im Gleichgewicht: Pi = -(1/2) f^T K^-1 f, bei Eigendehnung + (1/2) e0^T k e0.
- **Wechselwirkung:** Pi_12(R) := Pi(Paar) - Pi(einzeln) - Pi(einzeln) = -f1^T K^-1 f2.
  - Bei Eigendehnung ist das genau, solange die beiden Quellen keinen Stab teilen. Fuer r >= sqrt2 ist das erfuellt;
    der Term e0_1 k e0_2 faellt dann weg.
  - Berechnet fuer alle R zugleich: Pi_12(R) = -(1/N) sum_{q != 0} S(q) e^{-i q R}, S = f^H D(q)^-1 f.
  - Kontrolle K2: Pi(Paar) - 2 Pi(einzeln) explizit im Ortsraum (Federenergien einzeln summiert, aus dem geloesten Feld).
- **Vorzeichen:** Pi_12 < 0 heisst Anziehung (das Paar liegt energetisch tiefer als getrennt; bei mit r fallendem
  Betrag zeigt -dPi_12/dr zueinander). Pi_12 > 0 heisst Abstossung.

## 3. Torus, q = 0 und Hintergrundkorrektur

### 3.1 Torus

- q kongruent 0 entfaellt (genau zwei Punkte des Hilfsgitters).
- Lasten: Das entspricht einem gleichfoermigen Gegenkraft-Hintergrund -f/N je Knoten; die Summe aller u ist 0.
- Eigendehnungen: feste Zelle, keine mittlere Dehnung.
- Erwartung im isotropen Kontinuum [M]: Zwei isotrope Dilatationszentren haben auf dem Torus die konstante
  Wechselwirkung +P^2/((lambda + 2 mu) V), P = 4 k delta, im unendlichen Medium dagegen 0.
- Fuer Punktlasten erwarte ich einen konstanten Versatz von der Ordnung 1/(mu L) plus Terme ~ r^2/L^3, wie beim
  Coulomb-Gitter mit Hintergrund [L]. Das ist die Scheinanziehung bzw. -abstossung aus TENSOR-EIS-0.

### 3.2 Korrektur [F]: Ewald-artige Kontinuumskorrektur

- Formel: dPi(r) = Pi_torus,kont(r) - Pi_unendlich,kont(r) = -[(1/V) sum_{q != 0} - Integral d^3q/(2 pi)^3] g(q) S_kont(q) e^{i q r}.
- S_kont:
  - Monopol (a): s(q-Dach)/q^2 mit s = (Gamma^-1)_zz.
  - Dipol (b): s = 16 q-Dach.Gamma^-1.q-Dach.
  - Dipol (c): s = (d.q-Dach)^2 d.Gamma^-1.d mit d = [110]/sqrt2.
  - Gamma_ik = C_ijkl q-Dach_j q-Dach_l aus den gemessenen C11, C12, C44 des jeweiligen Netzes.
- Gewichte: g = (1 + a q^2) e^{-a q^2} (Monopol) bzw. e^{-a q^2} (Dipol), a = sigma^2/2, sigma = L_box/8.
- Der Rest (1 - g) S ist bei q -> 0 von der Ordnung q^2. Er gibt nur Bildbeitraege der Ordnung sigma^2/L^5 (Dipol)
  bzw. sigma^4/L^5 (Monopol); diese werden vernachlaessigt.
- Integral radial geschlossen, Winkel per Gauss-Legendre (32 in t) x 64 (phi). Summe ueber |m_i| <= 14, abgeschnitten
  bei 1e-18 des groessten Gewichts.
- Korrigierter Wert: Pi_korr = Pi_torus - dPi.
- Gitterabweichungen von S_kont gehen nur mit 1/V ein.
- Fuer die Verschiebung der Punktlast (Kontrast zu L4) wird ebenso u_korr = u_torus - dG f gebildet.

### 3.3 Kontinuumsvergleich (beschreibend, kein Urteil)

- Punktlast: Pi_unendlich,kont = -(1/(8 pi^2 r)) Kreisintegral ueber q-Dach senkrecht zu r von (Gamma^-1)_zz
  (Synge/Lifshitz [L]). Fuer isotropes Gamma ist das genau Kelvin.
- Dipole: Pi_unendlich,kont = (1/(8 pi^2 r^3)) Kreisintegral von d^2 s/dt^2 bei t = q-Dach.r-Dach = 0 [M, hier
  hergeleitet aus Integral q^2 cos(q b) dq = -pi delta''(b)]. Fuer die isotrope Dilatation ist es null.

### 3.4 Groessenreihe

- L = 32, 64, 128 (Kante 45, 91, 181 Stablaengen).
- Hauptwerte: L = 128, korrigiert. Faellt L = 128 aus, sind L = 64 die Hauptwerte (offengelegt).
- Groessenprobe K4 (beschreibend):
  - alle Urteile auch mit L = 64 korrigiert;
  - groesste relative Abweichung der korrigierten Werte L = 64 gegen 128 auf den bewerteten Punkten;
  - unkorrigierte Torus-Werte werden mitberichtet.

## 4. Messgroessen

- **Richtungsliste [F]:**
  - alle teilerfremden (h, k, l) mit |h|, |k|, |l| <= 3 in einer Halbkugel (Pi_12(R) = Pi_12(-R)), deren Gitterschritt
    hoechstens 16/3 ist, sodass mindestens 3 Punkte in [4, 16] liegen;
  - Gitterschritt: (h, k, l) a/2 bei gerader Summe h + k + l, sonst 2 (h, k, l) a/2;
  - enthalten sind [100], [110], [111] und weit mehr als 12 weitere.
- Punkte je Richtung: alle Gittervektoren auf dem Strahl mit 2 <= r <= 16.
- **Abfallexponent [F]:** p = -Steigung der Ausgleichsgeraden log|Pi_12| gegen log r ueber alle Punkte der Richtung
  mit 4 <= r <= 16 (Fenster W = [4, 16]). Beschreibend dazu [6, 16] und [8, 16].
- **Schalen-RMS [F]:** fuer k = 2 bis 16 der RMS von Pi_12 ueber alle Gittervektoren mit k - 0,5 <= r < k + 0,5;
  p_schale aus k = 4 bis 16.
- **Huellkurven-Exponent (nur L2) [F]:** E(r) = max ueber r' >= r (bis 16) von |Pi_12(r')| je Richtung;
  p_env = -Steigung von log E gegen log r in W. Er ist robust gegen Vorzeichenwechsel; bei glattem Potenzgesetz ist
  er gleich p.
- **Verschiebung (L4) [F]:**
  - Feld u einer einzelnen Quelle; Schalen-RMS von |u| um die Quellmitte (b: Knoten; c: Stabmitte), Schalen
    k = 4 bis 16, p_u = -Steigung.
  - Fuer (b) und (c) ohne Bildkorrektur; der Bildterm ist bei L = 128 hoechstens 0,3 % bei r = 16 (isotrop, [M]), und
    die Groessenreihe zeigt ihn.
  - (a) als Kontrast mit korrigiertem u.
- **Kelvin:** Pi_K(r) = -[(3 - 4 nu) + (r-Dach.z-Dach)^2]/(16 pi mu (1 - nu) r), mit mu = C44 und
  nu = C12/(2 (C12 + C44)) aus den gemessenen Konstanten des iso-Netzes.
- **Elastische Konstanten:** D(q) = Omega C_ijkl q_j q_l bei |q| = 1e-4 laengs [100] (C11, C44) und [110] (C12);
  Probe bei 2e-4.

## 5. Urteilsregeln (mechanisch in code/auswertung.py)

- **L0:**
  - aniso: |C11/(2 C44) - 1| <= 1e-6 und |C12/C44 - 1| <= 1e-6 [F: relativ];
  - iso: |A - 1| <= 0,01 mit Zener-Verhaeltnis A = 2 C44/(C11 - C12).
  - Beide erfuellt -> eingetroffen.
- **L1 (a), Hauptwerte, beide Netze:**
  - (i) Pi_korr < 0 fuer alle Gittervektoren mit 3 <= r <= 16 [F: "alle Richtungen" = alle Gittervektoren, nicht nur
    die Liste];
  - (ii) p in [0,9; 1,1] fuer jede Richtung der Liste, und p_schale in [0,9; 1,1];
  - (iii) iso: |Pi_korr/Pi_K - 1| <= 0,05 fuer alle Gittervektoren mit 6 <= r <= 16.
  - Alle drei erfuellt -> eingetroffen, sonst nicht eingetroffen.
- **L2 (b), iso gegen aniso, Hauptwerte:**
  - (i) Verhaeltnis |Pi_iso|/|Pi_aniso| <= 0,05 am Gitterpunkt mit r am naechsten an 8 laengs [100], [110] und [111]
    (bei Gleichstand der kleinere r), und Verhaeltnis der Schalen-RMS bei k = 8 <= 0,05.
    [F: bewertet die drei genannten Richtungen und die Schale; alle Listenrichtungen werden berichtet. Grund: Nahe dem
    Knotenkegel der anisotropen Wechselwirkung geht der Nenner gegen null.]
  - (ii) Abfall: p_schale(iso) >= 2,6 und p_env(iso) >= 2,6 in [100], [110] und [111].
    [F: "mindestens wie r^-3" mit der Toleranz 0,4 aus L3.]
  - Beide erfuellt -> eingetroffen.
- **L3 (b), aniso, Hauptwerte:**
  - (i) p in [2,6; 3,4] in [100], [110] und [111], und p_schale in [2,6; 3,4] [F: Begruendung wie bei L2(i)];
  - (ii) Vorzeichen von Pi_korr laengs [100] auf allen Punkten mit 4 <= r <= 16 einheitlich, ebenso laengs [111], und
    beide entgegengesetzt.
  - Beide erfuellt -> eingetroffen.
- **L4 (b, c), beide Netze, Hauptwerte:** p_u in [1,7; 2,3] in allen vier Faellen -> eingetroffen.
  [F: Toleranz 0,3; das entscheidet r^-2 gegen r^-1.]
- **"nicht auswertbar":** wenn eine Codekontrolle K1 bis K3 verfehlt ist, oder wenn Hauptlauf und Ersatz L = 64
  fehlen.

## 6. Kontrollen

- K1: Ortsraum-Residuum max |dU/du - f + f_mittel| <= 1e-9 max|f|; L = 16, beide Netze, alle Quellen, sechs Paare und
  die Einzelquellen.
- K2: explizites Pi(Paar) - 2 Pi(einzeln) gegen den Korrelationsweg, relative Abweichung <= 1e-9.
- K3: Werte auf ungeraden Hilfsgitterpunkten <= 1e-12 relativ; genau 2 Nullpunkte q kongruent 0 je Gitter.
- K4: Groessenreihe (Abschnitt 3.4), beschreibend.
- K5: Kontinuum.
  - Synge-Kreisintegral im iso-Netz gegen Kelvin (gleich bis auf Quadraturfehler).
  - iso-Dilatation im Kontinuum = 0.
  - Gitterwerte gegen Kontinuum bei grossem r (beschreibend).
- K6: Quadraturproben.
  - Ewald 32x64 gegen 64x128.
  - Dipolformel mit Schritt h gegen h/2, 128 gegen 256 phi-Punkte.
- K7: C bei |q| = 1e-4 gegen 2e-4.
- K8 [M]: Erwartete Konstanten (aus Tabelle A1, Gegenleser 3.1, hier nachgerechnet):
  - C11 = sqrt2 (1 + 14 k_theta), C12 = sqrt2 (1/2 - 7 k_theta), C44 = sqrt2 (1/2 + 6 k_theta).
  - iso: mu = 5 sqrt2/6 = 1,1785, lambda = sqrt2/9 = 0,1571, nu = 1/17 = 0,0588, Kompressionsmodul 2 sqrt2/3
    (wie aniso; Winkelfedern aendern ihn nicht).

## 7. Vorab ableitbar und Literatur

- L0 ist vorab ableitbar (K8); "eingetroffen" prueft dort den Code, nicht die Physik.
- L1:
  - Im Kontinuum ist das Vorzeichen fuer gleich gerichtete Lasten vorab klar [M]: -f.G.f < 0, weil G positiv definit
    ist.
  - Dass die Gitter-Green-Funktion fuer grosse r in Kelvin uebergeht, ist bekannt [L].
  - Offen sind: Korrektur, Gitterabweichung bei r >= 6, Anisotropie.
- L2: Im unendlichen isotropen Kontinuum ist die Wechselwirkung null [L?: Bitter/Crum; hier [M] nachgerechnet:
  s ist konstant]. L2 prueft also die Gitterkorrekturen jenseits der elastischen Ordnung und die Torusbehandlung.
- L4: Fernfeld eines Kraftdipols ~ r^-2 [M].

## 8. Bilder (lauf-69/)

- Pi_12(r) doppelt-logarithmisch je Quelle und Netz: [100], [110], [111] und Schalen-RMS, Vorzeichen markiert.
- Richtungsabhaengigkeit: r^p Pi_12 bei r nahe 8 ueber alle Listenrichtungen (Winkelkarte).
- Kelvin-Verhaeltnis (iso, a).
- Torus-Effekt: unkorrigiert gegen korrigiert, L = 32/64/128.
- |u| als Schalen-RMS (L4).

## 9. Laeufe

- **Rauch vor dem Einfrieren:**
  - rauch1 (cpu, 21:02 UTC): Kontrollen bei L = 8 (K1 bis K3 erfuellt), elastische Konstanten, Zeiten L = 32/64,
    Quadraturprobe 64x128 gegen 96x192 (<= 7e-14).
  - rauch2 (cpu6, 21:04 UTC): Quadratur 32x64 gegen 64x128 (<= 7e-14, deshalb 32x64), Ewald fuer alle 26 550
    Gittervektoren 4 s, Felder L = 128 in 26 s bei 1,8 GB.
  - rauch3 (cpu, cpu6, ab 21:09 UTC): ganze Kette auf L = 32/64 (kontrolle, kontinuum, lauf, auswertung), um
    auswertung.py auf Laufzeitfehler zu pruefen. Ich lese dabei nur Rueckgabewerte, Fehlermeldungen und Dateinamen,
    nicht die Ausgaben der Auswertung.
  - In keinem Rauchlauf sehe ich Pi_12-Werte. Gesehen habe ich die elastischen Konstanten (L0, vorab ableitbar).
- **Haupt (nach dem Einfrieren), ueber kleintest.sh, hoechstens zwei zugleich, alles in lauf/:**
  - cpu6: lauf --L 128 (beide Netze).
  - cpu: lauf --L 32 --L 64, danach kontrolle --L 16, kontinuum.
  - Danach auf cpu: auswertung.py.
- Eingefroren werden PLAN.md, code/last1.py und code/auswertung.py (sha256 in code/pruefsummen-einfrieren.txt).
