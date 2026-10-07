Urteil: TRAEGT MIT EINSCHRAENKUNG (Herleitung und alle Zahlen stimmen. "Reparierbar" haelt nur als "im Mittel um eine Ordnung in m^2/sqrt(rho) unterdrueckt". Der Zuwachs aus SH2 ist kein reines Polmass. Die Hochrechnung gilt nur bei l nahe l_P und exakt sigma = 0.)

# Gegenlesen KAUSAL-4D-SCHICHT-1

- Gegenleser: frischer Agent (Claude, nicht Autor, nicht Rechner), Auftrag der Leitung claude-primary
- Beginn: 2026-10-04 09:42:37 CEST (gemessen mit date)
- Zeitbox: 45 min
- Gegenstand: RUNDE-37/kausal-4d-schicht-1/ (KARTE.md, PLAN.md, eingefrorener PLAN, ERGEBNIS.md, code/, lauf-69/auswertung.json)
- Arbeitsweise: nur lesen; Rechnungen im Kopf mit Rechenweg; keine Interpreter

## 1. Herleitung (Erwartungsformel, Normierung, Polformel V-J, Restformel V-0)

Alles im Kopf nachgerechnet; Bezeichnungen wie PLAN 2: c = pi rho/24, u = c tau^4, mu_n = u^n e^-u/n!,
a = sqrt(rho)/(2 pi sqrt 6), eps = sqrt 6/(2 pi sqrt rho).

**1.1 Erwartungsformel: richtig.**
- Entlang einer Kette y < z_1 < ... < x sind die offenen Intervalle paarweise disjunkt. Ein Punkt w in I(z_(i-1), z_i)
  und I(z_(j-1), z_j) mit i < j gaebe w < z_i <= z_(j-1) < w. Auch kein Kettenpunkt liegt in einem dieser Intervalle.
- Deshalb faktorisieren die Poisson-Wahrscheinlichkeiten "genau n_i Elemente". Mecke liefert rho^(j-1)
  (mu_(n_1) * ... * mu_(n_j)), und die geometrische Reihe gibt K_P~ = k~_gen/(1 + m^2 k~_gen) mit b rho = -m^2.
- Die Rekursion psi = (I - b Phi^T)^-1 J, phi = (1/rho) Phi^T psi ist (1/rho) K_R^T J mit K_R = Phi (I - b Phi)^-1.
- "K - I = Phi (I - b Phi)^-1" in PLAN 1 folgt Johnstons Konvention K = I + Phi (I - b Phi)^-1. So steht es in
  KAUSAL-WELLE-4D/PLAN.md Z. 21, gelesen. Das ist also kein Fehler; einen ersten Verdacht habe ich zurueckgezogen.

**1.2 Fouriertransformierte: richtig.** Bei k = 0 und omega = iZ gilt d^4x = tau^3 sinh^2 chi dtau dchi dOmega. Mit
K1(x) = x int sinh^2 t e^(-x cosh t) dt folgt F = (4 pi/Z) int tau^2 f K1(Z tau) dtau.

**1.3 Normierung: richtig.**
- int tau mu_n dtau = Gamma(n + 1/2)/(4 sqrt(c) n!). Gegenprobe: tau dtau = du/(4 sqrt(c) sqrt(u)).
- Die Bedingung sum a_n Gamma(n + 1/2)/n! = sqrt(c)/pi ist fuer Johnston erfuellt. Beide Seiten sind
  sqrt(rho)/(2 sqrt 6 sqrt pi).
- V-0: 2a sqrt(pi) - 2a sqrt(pi)/2 = a sqrt(pi). V-M: 3a sqrt(pi) - 4a sqrt(pi)/2 = a sqrt(pi). Beides stimmt.
- Die Reihe von K1 ist richtig: 1/x + ln(x/2) I1(x) + (x/4)(2 gamma - 1) + ...; der letzte Term kommt aus
  -(x/4)(psi(1) + psi(2)).

**1.4 ln Z^2-Koeffizient und Konstante: richtig.**
- int tau^3 mu_n dtau = 1/(4c) fuer jedes n. Daraus folgt der Koeffizient (pi/(4c)) sigma; fuer V-J ist das
  pi a/(4c) = sqrt 6/(2 pi sqrt rho) = eps.
- Konstante bei sigma = 0: (pi/(8c)) sum a_n psi(n + 1). Fuer V-0 ist das 2a(-gamma) - 2a(1 - gamma) = -2a, also
  -pi a/(4c) = -eps. Massenschale: M^2 = m^2/(1 - eps m^2).

**1.5 Z^2 ln Z^2-Koeffizient: richtig.**
- C = (pi/(32 c^(3/2))) sum a_n Gamma(n + 3/2)/n!, mit int tau^5 mu_n dtau = Gamma(n + 3/2)/(4 c^(3/2) n!).
- Fuer V-0 ist die Summe -a sqrt(pi)/2. Mit sqrt(c) = pi^(3/2) a (Normierung) vereinfacht sich das zu
  C_V0 = -1/(64 c) = -3/(8 pi rho) = -pi eps^2/4.

**1.6 Polformel V-J: richtig.** Bei Z^2 = -m^2 + delta (physikalisches Blatt: ln Z^2 = ln m^2 - i pi) gilt
Im delta = -pi eps m^4. Daraus Im omega^2 = pi eps m^4 und Im omega = pi eps m^4/(2 omega) = (sqrt 6/4) m^4/(omega
sqrt rho). Zahlen bei m = omega = 1: 0,612/2 = 0,306; 0,612/2,83 = 0,217; 0,612/4 = 0,153. Wie ERGEBNIS 3.1.

**1.7 Restformel V-0: richtig, dimensional und in der Ordnung.**
- Ansatz g = 1 + m^2 [1/Z^2 - eps + C Z^2 ln Z^2 + D Z^2 + ...] bei Z^2 = -M^2 + delta. Die nullte Ordnung
  verschwindet nach Definition von M.
- Dann bleibt delta/M^4 = -C M^2 (ln M^2 - i pi) - D M^2. Also Im delta = pi C M^6 = -3 M^6/(8 rho), daraus
  Im omega^2 = 3 M^6/(8 rho) und Im omega = 3 M^6/(16 rho omega).
- Vorzeichen: Wachstum, weil C_V0 < 0. Das passt zur Numerik (+0,0147).
- Dimension: [rho] = Masse^4, also M^6/(rho omega) = Masse. Das stimmt.
- Ordnung: Im omega/omega = (3/16)(M/omega)^2 (M^2/sqrt rho)^2. Das ist zweite Ordnung in m^2/sqrt(rho), bei V-J
  erste. "Rest hoeherer Ordnung" ist richtig.
- Zahlen mit omega = M, m = 1 (so auch der Code, schicht_auswertung.py Z. 319):
  - rho = 16: eps = 0,0975, M^2 = 1,108, M^5 = 1,292, mal 3/256 = 0,01514.
  - rho = 8: 0,0340. rho = 4: 0,0806.
- Die "13 / 5 / 3 %" sind auf den Formelwert bezogen: (0,0806 - 0,0701)/0,0806 = 13 %. Auf die Numerik bezogen sind es
  15 / 5,5 / 3,0 %. Das ist nur eine Formulierungsfrage (B8, gering).

**1.8 Warum der 1/sqrt(rho)-Term bei sigma = 0 verschwindet.**
- Den Imaginaerteil auf der Massenschale liefert nur der Schnitt der ln Z^2-Terme. Sie stammen aus ln(x/2) I1(x) in
  K1, und I1 ist eine Potenzreihe x/2 + x^3/16 + ...
- Der niedrigste Logterm hat den Koeffizienten pi/(4c) mal sigma. Grund: Das Gewicht tau^3 dtau ist das 4-Volumenmass
  je Hyperboloidschale. Jede Schicht n traegt dort gleich viel bei (int u^n e^-u/n! du = 1).
- Der Sprung ueber den Schnitt beginnt bei sigma = 0 deshalb erst mit Z^2 int tau^5 f. Das passt zu PLAN 4:
  D = 2 pi i (pi/(4c)) sigma.
- Dasselbe Prinzip steckt in den alternierenden BD-Summen (1, -9, 16, -8), die sich zu null addieren. Dort
  heben sich die Beitraege "far down the light cone" auf (Surya 2019, lokale Textfassung Z. 7375-7377, selbst gelesen).

**1.9 Nebenbefund zum festen Abstand (Behauptung 5).**
- Aus der Konstante -eps folgt auch das Residuum der Schale: k~/(dg/dZ^2) = M^4/m^4 = 1/(1 - eps m^2)^2.
- Fuer eine Mode mit k = 0 ist das Amplitudenverhaeltnis dann M^3/m^3 = 1,166 bei rho = 16. Mit e^(0,0147 * 3,2) =
  1,048 ergibt das ~1,22. Das liegt in der beobachteten Spanne 1,21 bis 1,29 [M, grob].
- "abs(E)/abs(K) = 1,21 bis 1,29" ist also vor allem eine Normierung der Schale, keine Massenverschiebung. Beide kommen
  aus demselben Term O(eps m^2) (B9, gering, nur Wortlaut).

## 2. Hochrechnung (omega ~ M, Planckdichte, "~6e24 Weltalter")

**2.1 Einsetzen: richtig.**
- Fuer ein ruhendes Teilchen ist k = 0, also omega = M.
- Bei l = l_P ist eps m^2 ~ 0,39 (m l)^2 ~ 4e-35 (Higgs), also M = m bis auf 1e-34.
- Je Eigenzeit gilt Im omega * (omega/M) = 3 M^5/(16 rho). Das ist bewegungsunabhaengig, die Lorentz-Probe ist
  dieselbe wie im Dossier 3.1.
- Mit rho = l^-4: Gamma_0 = (3/16) m^5 l^4 = (3/16)(m c^2/hbar)(m/m_P)^4 [1/s]. Die Einheiten stimmen.

**2.2 Zahlen (Kopfrechnung).** Werte: m_H = 125,1 GeV, m_P c^2 = 1,2209e19 GeV, hbar = 6,582e-25 GeV s,
Weltalter 13,8 Gyr = 4,355e17 s.
- m/m_P = 1,0247e-17. Daraus (m/m_P)^2 = 1,0499e-34 und (m/m_P)^4 = 1,1024e-68.
- m c^2/hbar = 1,9006e26 1/s.
- V-0: Gamma_0 = 0,1875 * 1,9006e26 * 1,1024e-68 = 3,93e-43 1/s. Das gibt 2,55e42 s je e-Faltung, also
  2,55e42/4,355e17 = **5,8e24 Weltalter**. "~6e24" stimmt.
- V-J zur Kontrolle: 0,6124 * 1,9006e26 * 1,0499e-34 = 1,22e-8 1/s. Das sind 8,18e7 s = **2,59 Jahre**; "~2,6 Jahre"
  stimmt.
- Top, 172,7 GeV: Faktor (125,1/172,7)^5 = 0,7244^5 = 0,199. Das gibt **1,2e24 Weltalter**; "~1e24" stimmt.

**2.3 Abhaengigkeit von der Konvention (B3, mittel).**
- Die V-0-Rate geht mit l^4, die V-J-Rate nur mit l^2.
- Mit der reduzierten Plancklaenge sqrt(8 pi) l_P wird die Zeit (8 pi)^2 ~ 630-mal kuerzer, also ~9e21 Weltalter. Das
  Dossier nennt fuer V-J den Faktor 25; fuer V-0 fehlt er im ERGEBNIS.
- Vertraeglich mit dem Weltalter (eine e-Faltung) waere V-0 fuer einen Higgs-schweren freien Skalar bis
  l ~ (5,8e24)^(1/4) l_P ~ 1,6e6 l_P ~ 2,5e-29 m. V-J verlangt dafuer l < 1,4e-5 l_P (Dossier).
- Die Aussage "bedeutungslos fuer physikalische Dichten" braucht deshalb den Zusatz "bei l in der Naehe von l_P".

**2.4 Gilt die Restformel fuer m^2/sqrt(rho) -> 0?** Ja, als fuehrender Term. Begruendung [M]:
- mu_n faellt wie e^(-c tau^4), daher sind alle Momente endlich. Die Reihe von K1 (bzw. I1) konvergiert, also ist die
  Entwicklung in Z^2/sqrt(c) konvergent und nicht nur asymptotisch.
- Auf der Schale ist das Entwicklungsmass eps M^2. Jeder weitere Logterm bringt einen Faktor eps M^2 (mit Log).
  Relative Korrekturen sind O(eps M^2 ln(1/(eps M^2))), bei Planckdichte ~1e-33.
- **Keine weiteren Nullstellen bei hoher Dichte (Skalierung):**
  - Es gilt m^2 k~_gen = (m^2/sqrt c) G(Z/c^(1/4)), mit einer variantenfesten Funktion G.
  - G ist auf dem physikalischen Blatt ausser bei Z = 0 beschraenkt. Im UV gilt k~ ~ 8 pi a_0/Z^4, wobei nur
    mu_0(0) = 1 zaehlt; fuer V-0 ist das doppelt so viel wie bei V-J.
  - Fuer m^2/sqrt(c) -> 0 gibt es deshalb nur die Schalennullstelle. Die Numerik bei rho = 4 bis 16 (keine weiteren
    Nullstellen) passt dazu.
  - Das ist eine Groessenordnungsrechnung, nicht streng.
- **Die Numerik traegt die Asymptotik nur schwach:**
  - Die drei Dichten haben eps M^2 = 0,24 / 0,16 / 0,11. Die relativen Abweichungen 13 / 5,2 / 2,9 % fallen schneller
    als eps M^2 (Verhaeltnis 0,54 / 0,33 / 0,27). Das passt, ist aber kein Test der Asymptotik.
  - Die Hochrechnung ruht auf der Herleitung (1.7), nicht auf den drei Punkten. ERGEBNIS L5 sagt das sinngemaess.
- **Voraussetzung sigma = 0 exakt (B4, mittel, [H]):**
  - Eine Restabweichung delta-sigma bringt den Term erster Ordnung mit dem Gewicht delta-sigma/a zurueck.
  - Damit V-0 beim Higgs bei l_P seinen Vorteil behaelt, muesste abs(delta-sigma/a) <~ ((3/16)/(sqrt 6/4)) (m l)^2
    ~ 0,31 * 1e-34 ~ 3e-35 sein.
  - Im flachen Mittelwertmodell ist sigma = 0 durch Konstruktion exakt (2a - 2a). In jeder Erweiterung ist es aber
    eine Feinabstimmung. Beispiele: gekruemmte Raumzeit (Kruemmungskorrekturen der Schichtmomente je n verschieden),
    Rand, Wechselwirkung.
  - Ob sie dort geschuetzt ist, ist offen. Das gehoert als Bedingung zur Hochrechnung.
- Weiter gelten die Bedingungen des Dossiers: freier Skalar, Mittel = wirksame Dynamik, keine QFT-Effekte.

## 3. Lesart ("Abhilfe reparierbar" bei Urteil nur auf rho = 16)

**3.1 Verfahren: in Ordnung.**
- Der Satz "reparierbare Eigenschaft des Kerns" ist die vorab festgelegte Bedeutung fuer "SH1 und SH2 treffen ein"
  (KARTE). Plan und Karte legen rho = 16 als Urteilsdichte fest. Ausgeloest ist der Satz also regelgerecht.
- Das ERGEBNIS legt rho = 8 (1,115, Graubereich) und rho = 4 (1,20, ueber der Scheiterschwelle) offen. Es schraenkt in
  Abschnitt 6 selbst ein ("traegt im Mittel und bis auf einen Rest hoeherer Ordnung").

**3.2 Inhaltlich ist "reparierbar" zu stark (B1, mittel).**
- Gezeigt ist eine parametrische Absenkung, kein Abstellen:
  - Das Verhaeltnis der Raten V-0/V-J ist (3 M^6/(16 rho))/((sqrt 6/4) m^4/sqrt(rho)), also ~0,31 M^2/sqrt(rho).
  - Bei rho = 16 ist das ein Faktor ~10 (0,0147 gegen 0,152).
  - Asymptotisch ist es ein Faktor ~(m l)^2.
- Das Ergebnis gilt nur unter diesen Bedingungen:
  - im Mittel ueber Streuungen
  - fuer einen freien Skalar in flacher Raumzeit
  - ueber eine Laufstrecke von 2/m
  - numerisch nur bei rho <= 16, wo eps M^2 = 0,11 bis 0,24 ist
  - mit exakt sigma = 0 (B4)
- Dazu bleiben der Preis (Streuung je Saat x2) und der statische Abstand O(m^2/sqrt rho) zum Kontinuum: 21 bis 29 % bei
  rho = 16.
- "Reparierbar" klingt nach "behoben". Treffender ist "um eine Ordnung in m^2/sqrt(rho) unterdrueckbar".

**3.3 Der Zuwachs Z misst nicht nur das Polwachstum (B2, mittel).**
- Kopfrechnung aus ERGEBNIS 3.1 und 3.3 (eta = 0, Fenster Delta t = 1,2). Allein vom Pol erwartet man
  ln Z = 1,2 Im omega.
- V-0, gemessen gegen nur vom Pol:

  | rho | ln Z gemessen | nur Pol | Verhaeltnis |
  |---|---|---|---|
  | 4 | ln 1,200 = 0,182 | 0,084 | 2,2 |
  | 8 | ln 1,115 = 0,109 | 0,039 | 2,8 |
  | 16 | ln 1,064 = 0,062 | 0,018 | 3,5 |

- V-J dagegen: 0,288 gegen 0,295, 0,261 gegen 0,237, 0,221 gegen 0,183. Hier traegt der Pol den Zuwachs weitgehend.
- **Folgen:**
  - Bei V-0 stammt der groessere Teil des Fensterzuwachses nicht aus dem Restpol. Moegliche Quellen sind Schnittbeitrag,
    Normierung und Dispersion bei verschobener Masse; die Ursache ist nicht geprueft [H].
  - Graubereich bei rho = 8 und Scheitern bei rho = 4 sprechen deshalb weniger gegen die Lesart, als es aussieht. Das
    Bestehen bei rho = 16 spricht aber auch weniger dafuer. Die Hauptaussage muss auf SH1 (Pol) ruhen, nicht auf SH2.
  - ERGEBNIS 2 sagt: "Die Vorhersage traegt aber erst ab etwa rho = 16; das passt zum Gang m^6/rho." Das stimmt so
    nicht. ln Z von V-0 faellt je Verdopplung von rho nur um 1,67 und 1,76, der Pol um 2,18 und 2,19. Der Gang liegt
    zwischen 1/sqrt(rho) und 1/rho.
  - "Einfach gesagt" schreibt "rund zehnmal langsamer". Das gilt fuer die Wachstumsrate am Pol. Im gerechneten Fenster
    waechst der Abstand zum Kontinuum bei V-0 nur etwa 3,6-mal weniger (ln Z 0,221 gegen 0,062) (B6, gering bis
    mittel).

**3.4 Behauptung 2 (V-M "die Welle klingt ab"): nur ab rho = 8 (B5, gering).**
- Bei rho = 4 ist Z(V-M) = 1,035 bzw. 1,036, also kein Abklingen. Die Blatt-II-Nullstelle liegt dort bei Re omega =
  1,47, fern der Schale (ERGEBNIS 3.1 selbst).
- "Klingt ab" gilt fuer rho = 8 und 16 im Fenster t = 2,0 bis 3,2.
- Die Einordnung "V-M ist keine Loesung, sondern das Spiegelbild" (ERGEBNIS 6) ist richtig.

**3.5 Behauptung 3 (keine weiteren Nullstellen): richtig im Wortlaut, in ERGEBNIS 6 verkuerzt (B7, gering).**
- Die Zaehlung sieht Nullstellen mit 0 < Im omega <= 0,05 ausserhalb S nicht (Re omega ausserhalb [0,5; 2]). In diesem
  Streifen liegt auch die Groessenordnung des V-0-Rests (0,015).
- ERGEBNIS 6 schreibt "In abs(omega) < 10 entstehen keine neuen instabilen Nullstellen" und laesst die Schwelle 0,05 weg.
- Plausibel ist dort keine Nullstelle: Fuer abs(omega) >= 2 ist abs(m^2 k~) etwa <= 1/4 plus Korrekturen. Geprueft ist
  das nicht. Die Schwelle gehoert in den Satz; alternativ min abs(g) auf dem Streifen angeben.

**3.6 Weitere Zahlen der Behauptungen: nachgerechnet und richtig.**
- Faktor 0,0701/0,0147 = 4,77.
- Streuungsverhaeltnis 0,636/0,310 = 2,05 (rho = 16) und 0,816/0,417 = 1,96 (rho = 8).
- 0,152/0,0147 = 10,4.

## 4. Literaturstand

**4.1 Selbst gelesen, lokal:** Surya 2019, coordination/runden-v3/RUNDE-22/geometrie-stand/hilfs/surya-1903.11544.txt.
- Z. 7337-7340, Bildunterschrift Fig. 14: "The nearest neighbours are the links or zero intervals, the next to nearest
  neighbours are the 1-element intervals". Die Schichten sind also Standardbegriff.
- Z. 7345-7357: Der 4D-BD-Operator (27) hat die Schichtkoeffizienten 1, -9, 16, -8 (Summe 0) vor einem Vorfaktor
  4/sqrt 6. Dazu: "Notice the alternating sum whose precise coefficients turn out to be very important to the continuum
  limit."
- Z. 7375-7377: "miraculous cancellations that make the contributions far down the light cone negligible". Das ist
  derselbe Mechanismus wie sigma = 0 hier (1.8).
- Z. 7404-7409 zu ASS: "indications that while the evolution in d = 2 is stable, it is unstable in d = 4". Dazu "still
  an open question whether there is a subfamily of these operators that lead to a stable evolution".
- Z. 8028-8057, Gl. (65) und (67): Johnstons 4D-Propagator springt nur ueber Links. Hop-Amplitude a, Stopp-Amplitude b,
  Gewicht a^(k+1) b^k L_k. Schicht-Spruenge kommen dort nicht vor.

**4.2 Ueber WebFetch, nur Abstracts (3 Abrufe, 09:53).**
- Ich habe das Werkzeug ausdruecklich um woertliche Wiedergabe gebeten. Die Texte sind trotzdem nicht gegen Rohtext
  geprueft. Ich stuetze mich nur auf die zitierten Saetze, nicht auf Deutungen.
- **ASS, arXiv:1403.1622:**
  - Sie bilden eine "infinite family of 'Generalized Causet Box (GCB) operators' parametrized by certain coefficients
    {a, b_n}" und leiten "the conditions on the latter needed for the usual d'Alembertian to be recovered in the
    infrared limit" her.
  - "For timelike p, g(p) has an imaginary part whose sign depends on whether p is past or future-directed".
  - Sie finden "evidence that the original 4D causal set d'Alembertian is unstable, while its 2D counterpart is
    stable".
- **Shuman, arXiv:2307.08864:** "we explore under what conditions a path sum will correspond to a scalar field
  propagator ... A family of solutions for the path sum is found and is verified numerically in a few specific
  cases." Ob die Familie Spruenge ueber n-Element-Intervalle mit sigma = 0 enthaelt und ob Wachstum vorkommt, sagt
  das Abstract nicht.
- **X/Dowker/Surya, arXiv:1701.07212:** "We examine the validity and scope of Johnston's models for scalar field
  retarded Green functions on causal sets in 2 and 4 dimensions". Das betrifft Riemann-Normal-Umgebungen, de Sitter
  und AdS. Schichten oder Anwachsen nennt das Abstract nicht.

**4.3 Einordnung.**
- **Bekannt:**
  - Schichtsummen ueber n-Element-Intervalle mit wechselnden Vorzeichen und Summe 0, als d'Alembert-Operatoren.
    Belegt fuer BD bei Surya; DG 2013 nennt Surya Z. 7325-7326 als Verallgemeinerung auf andere Dimensionen, den
    DG-Text selbst habe ich nicht gelesen.
  - Bedingungen an die Koeffizienten fuer den richtigen IR-Grenzfall (ASS) und ein Imaginaerteil bei zeitartigem p
    (ASS).
  - Die 4D-Instabilitaet des BD-Operators (ASS, Surya).
  - Das ERGEBNIS L4 nennt das zutreffend ("(4, -36, 64, -32)/sqrt 6, Summe 0").
- **Nicht gefunden:** Schicht-Spruenge in Johnstons Propagator-Pfadsumme mit sigma = 0, um das Anwachsen an der
  Massenschale zu unterdruecken.
- **Luecken:** Gelesen habe ich nur Abstracts und Surya. Die Volltexte von Shuman 2023 ("family of solutions"),
  Johnston 2014 und DG 2013 fehlen; Shuman ist der naechste moegliche Vorlaeufer.
- **Wortlaut:** "nach Lesestand nicht gefunden", nicht "neu" (B10, gering). So steht es im ERGEBNIS bereits ([L?]).
- **Empfehlung:** In L4 ausdruecklich festhalten, dass sigma = 0 das Propagator-Gegenstueck der bekannten BD-Ausloeschung
  "far down the light cone" ist. Das macht die Idee plausibler und weniger originell.

## 5. Befunde (nummeriert, Fundstelle, Schwere)

| Nr | Fundstelle | Befund | Schwere |
|---|---|---|---|
| B1 | ERGEBNIS 2 (Bedeutung), 6 ("Fuer die Karte"); KARTE Bedeutung | "Reparierbare Eigenschaft des Kerns" ist zu stark. Gezeigt ist eine parametrische Absenkung der Rate von O(m^2/sqrt rho) auf O(m^4/rho), im Mittel, freier Skalar, flach, rho <= 16 numerisch. Das Anwachsen ist nicht abgestellt (3.2). | mittel |
| B2 | ERGEBNIS 2 ("das passt zum Gang m^6/rho"), 3.3 | Der Fensterzuwachs Z von V-0 stammt nur zu ~28 bis 46 % aus dem Restpol (ln Z 0,062 gegen 1,2 Im omega = 0,018 bei rho = 16). Sein Gang mit rho (Faktor 1,67 und 1,76 je Verdopplung) ist nicht m^6/rho (Pol: 2,18 und 2,19). SH2 ist deshalb ein unscharfes Mass; die Hauptaussage ruht auf SH1 (3.3). | mittel |
| B3 | ERGEBNIS 5 L5, 6 ("bedeutungslos") | Die Hochrechnung haengt mit l^4 an der Laengenwahl: Mit reduzierter Plancklaenge ist die Zeit ~630-mal kuerzer (~9e21 Weltalter). Bedingung "l nahe l_P" nennen; die Weltaltergrenze fuer V-0 ist l <~ 1,6e6 l_P (2.3). | mittel |
| B4 | ERGEBNIS 5 L5, 6 | Die Hochrechnung setzt sigma = 0 exakt voraus. Jede Abweichung delta-sigma bringt den Term erster Ordnung zurueck; beim Higgs bei l_P muesste abs(delta-sigma/a) <~ 3e-35 sein. In Erweiterungen (Kruemmung, Rand, Wechselwirkung) ist das eine offene Feinabstimmung [H] (2.4). | mittel |
| B5 | Behauptung 2; ERGEBNIS 1.2 | "V-M: die Welle klingt ab" gilt nur fuer rho = 8 und 16; bei rho = 4 ist Z = 1,035 (3.4). | gering |
| B6 | ERGEBNIS 9 ("rund zehnmal langsamer"), 1.1 ("um eine Ordnung") | Das gilt fuer die Polrate. Im gerechneten Fenster waechst der Abstand zum Kontinuum bei V-0 nur ~3,6-mal weniger als bei V-J (3.3). | gering bis mittel |
| B7 | ERGEBNIS 6 ("keine neuen instabilen Nullstellen") | Ohne die Schwelle Im omega > 0,05 zu weit. Ausserhalb von S ist der Streifen 0 < Im omega <= 0,05 nicht gezaehlt (3.5). | gering |
| B8 | ERGEBNIS 1.1, 3.1 ("13 / 5 / 3 %") | Die Prozente sind auf den Formelwert bezogen; bezogen auf die Numerik sind es 15 / 5,5 / 3,0 % (1.7). | gering |
| B9 | Behauptung 5; ERGEBNIS 3.2 ("Massenverschiebung ... abs(E)/abs(K)") | Das Verhaeltnis 1,21 bis 1,29 ist vor allem das Schalenresiduum M^4/m^4 (Amplitude ~M^3/m^3 = 1,17 bei rho = 16) und etwas Wachstum. Ursache ist derselbe Term -eps (1.9). | gering |
| B10 | ERGEBNIS 5 L4 | Literatur: "nach Lesestand nicht gefunden" ist richtig, "neu" waere zu stark. Die Ausloeschung bei sigma = 0 ist das Gegenstueck der bekannten BD-Ausloeschung (Surya Z. 7375-7377); das sollte dort stehen. Shuman 2023 ist im Volltext ungeprueft (4.3). | gering |

**Ohne Befund nachgerechnet:**
- Erwartungsformel, Fourierformel, Normierung aller Varianten, K1-Reihe
- ln Z^2- und Z^2 ln Z^2-Koeffizienten, Konstante -eps
- Polformel V-J, Restformel V-0 (Vorzeichen, Dimension, Ordnung, Zahlen)
- Hochrechnung 5,8e24 / 2,6 Jahre / 1,2e24
- Faktoren 4,77, 10,4 und 2,05

**Quote:** 14 von 17 Pruefpunkten bestaetigt. Die drei uebrigen sind Aussagen, die weiter gehen als die Rechnung: B2
(Gang), B5 (V-M), B7 (Nullstellen).

## 6. Empfohlene Formulierung

Im Mittel ueber Streuungen senkt die Zweischicht-Sprungregel V-0 (Links 2a, 1-Element-Intervalle -2a, sigma = 0) die
Wachstumsrate an der Massenschale von (sqrt 6/4) m^4/(omega sqrt rho) auf 3 M^6/(16 rho omega). Die Numerik trifft das
bei rho = 4 / 8 / 16 auf 13 / 5 / 3 %, bei rho = 16 ist es ein Faktor 10 (0,0147 statt 0,152).
Abgestellt ist das Anwachsen nicht, aber um eine Ordnung in m^2/sqrt(rho) unterdrueckt. Bei l = l_P waere es fuer einen
Higgs-schweren freien Skalar bedeutungslos (~6e24 Weltalter je e-Faltung), sofern sigma = 0 exakt bleibt und das
Mittel die Dynamik beschreibt.
Der Preis ist doppelte Streuung je Saat, und der feste Abstand O(m^2/sqrt rho) zum Kontinuum bleibt.

## 7. Ende

- Abschluss: 2026-10-04 09:57:24 CEST (date). Gemessene Dauer 09:42:37 bis 09:57:24, also 14 min 47 s von 45 min.
- Gelesen:
  - KARTE, PLAN (cmp gleich der eingefrorenen Fassung) und ERGEBNIS ganz
  - DOSSIER Abschn. 3.1, 3.2, 4.1 bis 4.4, 8 bis 12; ARBEITSFELD 2b
  - KAUSAL-WELLE-4D/PLAN Z. 20-40 und 70-95
  - schicht_auswertung.py Z. 310-325
  - Surya-Textfassung in Ausschnitten
- Drei WebFetch-Abrufe (Abstracts von ASS, Shuman, X/Dowker/Surya).
- Nicht geoeffnet: auswertung.json im Detail, Felddateien, Bilder; die Codepruefung war nicht Auftrag.
- Kein python, awk oder perl; keine Peerbus-Nachricht, kein Commit, kein Journaleintrag. Geschrieben habe ich nur in
  diese Datei.
