# PAAR-REGGE-2: Ergebnis (Runde 46)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 05:42:36 CEST; Text dieser Datei ab 06:00:42 CEST
  (beides date). Zeitbox 90 min.
- Grundlage: KARTE.md (bindend); PLAN.md, eingefroren 05:57:04 CEST vor den Hauptlaeufen (EINGEFROREN-SHA256.txt).
- Kennzeichen: [E] gerechnet auf der .69, [M] von Hand (nicht gegengelesen), [S] an der Quelle gelesen, [P]
  Projektdatei, [L] Gedaechtnis, [H] Hypothese, [F] Festlegung des Plans, [D] Diagnose ohne Urteil, [ES] eigener
  Schluss.
- Massen in Einheiten sqrt(sigma). "Steigung 4/9" = Spannung 9/4 sigma (offen, adjungiert); "Steigung 1/2" =
  Spannung 2 sigma (geschlossen, gefaltet). Modell (I) = Steigung 1/2 mit a = 2; Modell (II) = Steigung 4/9 mit a = 1.

## 1. Zeiten und Laeufe

Alle Laeufe auf der .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, 1 Thread (CPUQuota 100 %,
OMP/BLAS 1), Grenze 600 s. Aufruf jeweils:
`bash kleintest.sh <spur> <name> /home/fmh/fmhc-physics-remote/paar-regge-2/<ordner>/paar_regge2.py <modus> <ausgabe>`.
Zeiten aus den Logs (UTC; CEST = UTC + 2 h).

| Lauf | Spur | Modus, Ordner | Start bis Ende (UTC) | Rechenzeit (Unit) | rc |
|---|---|---|---|---|---|
| R0a pr2rauch | cpu5 | rauch, rauch/ (vor dem Freeze) | 03:55:24 bis 03:55:26 | 1,8 s | **1** (Fehler im Rauchpfad, Selbstanzeige 2) |
| R0b pr2rauch2 | cpu5 | rauch, rauch/ (vor dem Freeze) | 03:55:35 bis 03:55:39 | 2,5 s (3,8 s) | 0 |
| R0c pr2rauchbild | cpu5 | bild aus rauch.json (vor dem Freeze) | 03:56:01 bis 03:56:04 | 1,7 s (3,1 s) | 0 |
| R1 pr2kontr | cpu5 | kontrollen, lauf/ (eingefroren) | 03:57:11 bis 03:57:20 | 7,4 s (8,7 s) | 0 |
| R2 pr2fits | cpu6 | fits, lauf/ (eingefroren), parallel zu R1 | 03:57:11 bis 03:57:55 | 42,8 s (44,1 s) | 0 |
| R3 pr2bild | cpu5 | bild aus fits.json, lauf/ (eingefroren) | 03:58:05 bis 03:58:09 | 1,8 s (3,2 s) | 0 |

- Freeze 05:57:04 CEST (= 03:57:04 UTC), also vor R1 bis R3. Code auf der .69 per scp nach *.neu und mv; sha256
  dort gleich dem eingefrorenen (53e1d960...).
- Versionen: Python 3.12.3, numpy 2.4.4, scipy 1.18.0.

## 2. Was Sharov und H5 schon enthalten

**Sharov (R1): Den Fit hat er nicht gemacht. Die Karte ist keine Nachrechnung.**
- Gelesen: S1 hep-ph/0612373 (2006) und S2 arXiv:0712.4052 (2007) im Volltext; S3 (Sharov 2008, Phys. Atom. Nucl. 71,
  574) nur Metadaten (quellen/, ABRUFE.log).
- Sharov rechnet klassische Rotationsloesungen des geschlossenen Strings mit zwei (bzw. n) Punktmassen [S].
  - Der Zustand (n1, n2) = (2, 0), "two masses ... connected two strings", hat die Steigung alpha'/2. Klassisch ist das
    unser Modell (I).
  - Asymptotik J ~ alpha' E^2 + alpha1 E^(1/2) + ... (S1 Gl. 47-48, S2 Gl. 75-76).
- S2 setzt Zahlen, statt sie zu fitten: gamma = 0,175 GeV^2, m = 700 MeV, Spin J = L + S mit S = 2 und einen
  Spin-Bahn-Term (Gl. 71-73) [S].
  - Fig. 3 vergleicht nur mit der Pomeron-Geraden J ~ 1,08 + 0,25 M^2. Es gibt keinen Gittermassen-Vergleich und kein
    chi^2.
  - Schluss von S1 und S2: "These corrections are to be significant for calculation of the intercept alpha0". Der
    Intercept bleibt also offen.
- [ES] Sharovs J = L + 2 wirkt zahlenmaessig wie a = 2 aus H5, hat aber eine andere Herkunft (Gluon-Spins).
- Offen: Sharov 2008 im Volltext. Die Referenzliste nennt die Gitterarbeiten von Morningstar/Peardon, Meyer/Teper,
  Meyer und Lucini/Teper/Wenger [S Metadaten].

**H5 (Sonnenschein/Weissman 2020) [S]:**
- Gl. (1.4) a_open = 1 und (1.5) a_closed = 2, jeweils fuer jedes D; Konvention J = alpha' M^2 + a.
- Abschn. 5.2.1: Der gefaltete geschlossene String mit Massen auf den Faltstellen ist klassisch "completely equivalent
  to an open string with massive endpoints ..., with the string tension effectively doubled".
  - Die Randbedingung (5.7) ist die [P]-Form von PAAR-REGGE-1 mit kappa = 2 [M].
- **Gl. (7.9), eps eindeutig:** "where eps1 = 1/gamma0 and eps2 = 1/gamma_l"; gamma0 und gamma_l sind nach (5.8) und
  (5.9) die Lorentzfaktoren der Faltstellen-Massen.
  - Die Variante (I') ist deshalb gerechnet: a = 2 - (43/(24 pi)) (eps1 + eps2) = 2 - 1,1406 eps in D = 4.
  - (7.9) ist eine Entwicklung fuer kleine Massen (eps klein).
- H5 macht keinen Gittervergleich, regt ihn aber an: "It will be interesting to see if there is evidence of mass
  corrections in YM by comparing with results from the lattice" (H5 Z. 2785-2786) [S].

## 3. Ergebnis zuerst

1. **PQ2 eingetroffen: Das offene adjungierte Paar (II) erreicht auf (A) mit einer Endmasse p >= 0,05 [E].**
   - Werte: m = 1,057 [1,042; 1,071], chi^2 = 1,98 (1 Freiheitsgrad), p = 0,16.
   - Modell: E(2) = 4,899 und E(4) = 7,433; Gitter: 4,894(22) und 7,60(12)*.
   - Endgeschwindigkeiten v_end(2) = 0,681 und v_end(4) = 0,788. v_end(2) liegt knapp unter dem Band [0,70; 0,82],
     also gilt das Band "uebrig".
   - Unter den zehn Kandidaten ist (II) der einzige mit p >= 0,05 auf (A). Danach kommt Steigung 1/2 mit a = 1 (p = 0,003).
2. **PQ1 nicht eingetroffen, und das war vorab ableitbar [E, M].**
   - In (I) ist das 2++ das ruhende Paar (J_cl = 0, E(2) = 2m). Das legt m = 2,439 fest; dann kommt E(4) = 8,157 statt
     7,60 heraus.
   - Ergebnis: chi^2 = 22,0, p = 2,7e-6. Die Schreibtischrechnung im Plan gab chi^2 ~ 22.
   - Die Variante (I') nach H5 (7.9) scheitert ebenfalls (chi^2 = 13,4, p = 2,5e-4). Sie laeuft dabei weit ausserhalb
     ihres Bereichs (eps = 0,68 bis 0,79).
3. **Das Urteil kippt mit der Masse des 4++ [E].**
   - Auf der MT-Geraden (B) mit 4++ ~ 8,29 erreicht (I) in allen drei Lesarten p >= 0,05: R3 0,56, R1 0,86, R2 0,58.
   - (II) scheitert dort in R3 (p = 2e-8) und R2 (8e-5); nur in der losen Lesart R1 besteht es (p = 0,20).
   - Welches Paar-Bild traegt, entscheidet also das 4++ (A&T 7,60* "likely" gegen MT ~8,29). Das ist der Moderator R4
     aus HISH-GLUEBALL-L.
4. **PQ3 nicht eingetroffen; fuer (I) und (II) vorab ableitbar [M, E].**
   - Mit festem Intercept gilt M(4)^2 - M(2)^2 >= 4 pi kappa = 25,1 bzw. 28,3, numerisch bestaetigt (K5). (C) hat
     11,7 +- 1,9.
   - Bestes chi^2 auf (C): 70,7 (Steigung 1/2, a = 0). Fuer (I) 308, (II) 139, (I') 95,6.
5. **Kontrollen [E]:**
   - PQ0 ist nach Plan eingetroffen. Nach Wortlaut nicht, und zwar vorab ableitbar: Die Karte rundet auf drei
     Stellen, gefordert ist 1e-6.
   - PAAR-REGGE-1 ist nachgerechnet; alle vier Sollwerte sind getroffen.
   - Der erste Hauptsatz dE/dJ = omega haelt auf 3,5e-9.

## 4. Urteile

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Kartenwortlaut |
|---|---|---|---|---|
| PQ0 | masselose Werte (I) 0 und 5,013, (II) 3,760 und 6,512 auf 1e-6 reproduziert | 90 % | **eingetroffen.** Loeser bei m = 1e-8 gegen geschlossene Form: 2e-8 (Wert 0) bzw. <= 2,9e-13 relativ. Geschlossene Form gegen Karte: 0; 2,6e-4; 5,8e-5; 4,1e-4 (alle <= 5e-4, Rundung) | **nicht eingetroffen** (vorab abgeleitet, PLAN 6 a): 5,013257, 3,759942 und 6,512411 weichen um 2,6e-4, 5,8e-5 und 4,1e-4 > 1e-6 von den gerundeten Kartenzahlen ab. Keine Messung |
| PQ1 | [H] (I) mit (A): eine Endmasse gibt p >= 0,05 | 35 % | **nicht eingetroffen.** m = 2,439, chi^2 = 22,04, p = 2,7e-6 | **nicht eingetroffen** (gleich). Vorab weitgehend ableitbar (PLAN 6 d: chi^2 ~ 22 [M]) |
| PQ2 | [H] (II) mit (A): eine Endmasse gibt p >= 0,05 | 35 % | **eingetroffen.** m = 1,057, chi^2 = 1,977, p = 0,160 | **eingetroffen** (gleich). Vorab offen (PLAN 6 e: chi^2 ~ 2 bis 4 [M]) |
| PQ3 | [H] mit (C) erreicht mindestens eines der Modelle p >= 0,05 | 45 % | **nicht eingetroffen.** (I) chi^2 = 308, (II) 139. Vorab ableitbar (PLAN 6 c) | **nicht eingetroffen.** Auch (I') chi^2 = 95,6, p = 1,4e-22 |

**Bedeutung nach der Vorab-Regel der Karte ("PQ1 oder PQ2 trifft ein"):**
- Wortlaut der Karte: Finns rotierendes Paar traegt die Gitter-Tensoren mit dem Literatur-Intercept und einer
  Endmasse. Das ist der erste Treffer des Paar-Bilds, unter dem Look-elsewhere-Vorbehalt.
- Der Treffer gilt fuer die offene adjungierte Lesart (II) mit dem A&T-4++. Die Einschraenkungen stehen in Abschn. 6.

**Kontrollen (R1, eingefrorener Code) [E]:**

| Kontrolle | Ergebnis |
|---|---|
| K1 (PQ0) | siehe Tabelle oben |
| K2 dE/dJ = omega | max. 3,5e-9 (kappa = 2 und 9/4) |
| K3 Stetigkeit bei J_cl -> 0 | E - 2m = 3,8e-4 bei J_cl = 1e-6 und 8e-7 bei 1e-10 |
| K4 Nachrechnung PAAR-REGGE-1 | (A) chi^2 370,766 / 202,110; (B-R3) m = 0,2577 / 0,4133, chi^2 70,077 / 67,030. Alle vier Sollwerte getroffen |
| K5 Steigungsschranke | min (E4^2 - E2^2)/(4 pi kappa) = 1 (bei m = 0) fuer alle zehn festen Kandidaten. (I'): 0,936 bei m = 0,14, also gilt dort die Schranke nicht, wie erwartet |
| K6 Variante | J(eta) streng monoton; a(eta -> 0) = 0,8594. Bei m = 1e-8 ist E(4) = 5,01337 (masselos 5,01326), E(2) = 0,092: Der Grenzwert 0 wird langsam erreicht [D] |
| K7 synthetische Rueckgewinnung | (I), (II), (I'): m = 1,300 aus Pseudodaten mit m = 1,3, chi^2 = 0 |
| Budget | 0,13 ms je Loesung |

Gegenrechnung von Hand [M] fuer PQ2, nach dem Lauf:
- Bei m = 1,0567, kappa = 9/4 und v = 0,68115 gibt die [P]-Formel J_cl = 1,0001 und E = 4,8990.
- Bei v = 0,78838 gibt sie J_cl = 3,0002 und E = 7,4335.
- Beides stimmt mit dem Lauf (4,8987; 7,4333).

## 5. Alle zehn Kandidaten (Look-elsewhere) [E]

Je Datensatz ein Fit, ein freier Parameter m im Bereich [0; 6], 1 Freiheitsgrad. In Klammern steht das
1-sigma-Intervall von m (Delta chi^2 <= 1). In jedem Fit hat das m-Gitter genau ein lokales Minimum (Ausnahme: (I')
auf B-R2 mit zwei) oder es liegt bei m = 0. Kein bestes m liegt am Rand 6.

**(A) A&T 2020: 2++ 4,894(22), 4++ 7,60(12)***

| Steigung, a | Modell | bestes m | chi^2 | p | v_end(2) | v_end(4) | E(2); E(4) | Band |
|---|---|---|---|---|---|---|---|---|
| 4/9, 0 | | 0 [0; 0,007] | 370,77 | 1,3e-82 | 1 | 1 | 5,317; 7,520 | traegt nicht |
| 4/9, 1/12 | | 0 [0; 0,008] | 202,11 | 7,2e-46 | 1 | 1 | 5,205; 7,441 | traegt nicht |
| 4/9, 1/6 | | 0 [0; 0,011] | 84,12 | 4,7e-20 | 1 | 1 | 5,091; 7,362 | traegt nicht |
| **4/9, 1** | **(II)** | **1,057 [1,042; 1,071]** | **1,977** | **0,160** | **0,681** | **0,788** | 4,899; 7,433 | uebrig |
| 4/9, 2 | | 2,436 [2,425; 2,447] | 45,62 | 1,4e-11 | 0 | 0,569 | 4,872; 8,401 | traegt nicht |
| 1/2, 0 | | 0 [0; 0,017] | 47,46 | 5,6e-12 | 1 | 1 | 5,013; 7,090 | traegt nicht |
| 1/2, 1/12 | | 0,019 [0; 0,081] | 24,09 | 9,2e-7 | 0,994 | 0,996 | 4,910; 7,018 | traegt nicht |
| 1/2, 1/6 | | 0,222 [0,191; 0,251] | 22,86 | 1,7e-6 | 0,931 | 0,951 | 4,910; 7,033 | traegt nicht |
| 1/2, 1 | | 1,187 [1,172; 1,201] | 8,73 | 3,1e-3 | 0,642 | 0,757 | 4,904; 7,250 | traegt nicht |
| **1/2, 2** | **(I)** | **2,439 [2,428; 2,450]** | **22,04** | **2,7e-6** | **0** | **0,554** | 4,878; 8,157 | traegt nicht |
| 1/2, 2 - 1,1406 eps | (I') | 1,286 [1,274; 1,298] | 13,43 | 2,5e-4 | 0,612 | 0,734 | 4,906; 7,165 | traegt nicht |

**(B) MT-Gerade s = 0,281(22), a0 = 0,93(24), Hauptlesart R3 (Sekante des Modells im Parameterraum)**

| Steigung, a | Modell | bestes m | chi^2 | p | v_end(2) | v_end(4) | Sekante (s; a0) | Band |
|---|---|---|---|---|---|---|---|---|
| 4/9, 0 | | 0,258 [0; 0,607] | 70,08 | 5,7e-17 | 0,928 | 0,948 | 0,440; -0,080 | traegt nicht |
| 4/9, 1/12 | | 0,413 [0; 0,716] | 67,03 | 2,7e-16 | 0,886 | 0,918 | 0,436; -0,075 | traegt nicht |
| 4/9, 1/6 | | 0,538 [0,155; 0,815] | 63,92 | 1,3e-15 | 0,852 | 0,894 | 0,431; -0,063 | traegt nicht |
| **4/9, 1** | **(II)** | 1,423 [1,199; 1,639] | 31,44 | 2,1e-8 | 0,614 | 0,734 | 0,384; 0,182 | traegt nicht |
| 4/9, 2 | | 2,384 [2,090; 2,681] | 0,363 | 0,547 | 0 | 0,574 | 0,271; 1,020 | uebrig |
| 1/2, 0 | | 0,721 [0,467; 0,942] | 109,68 | 1,2e-25 | 0,808 | 0,857 | 0,477; -0,390 | traegt nicht |
| 1/2, 1/12 | | 0,808 [0,570; 1,021] | 105,29 | 1,1e-24 | 0,786 | 0,841 | 0,473; -0,373 | traegt nicht |
| 1/2, 1/6 | | 0,891 [0,665; 1,098] | 100,84 | 1,0e-23 | 0,765 | 0,826 | 0,468; -0,353 | traegt nicht |
| 1/2, 1 | | 1,612 [1,422; 1,798] | 54,49 | 1,6e-13 | 0,571 | 0,696 | 0,416; -0,061 | traegt nicht |
| **1/2, 2** | **(I)** | 2,497 [2,241; 2,756] | 0,334 | 0,563 | 0 | 0,549 | 0,291; 0,845 | uebrig |
| 1/2, 2 - 1,1406 eps | (I') | 1,679 [1,513; 1,844] | 69,61 | 7,2e-17 | 0,555 | 0,681 | 0,434; -0,179 | traegt nicht |

**(C) A&T 2020: 2++ ex1 6,788(40), 4++ 7,60(12)*** (alle "traegt nicht")

| Steigung, a | Modell | bestes m | chi^2 | p | v_end(2) | v_end(4) | E(2); E(4) |
|---|---|---|---|---|---|---|---|
| 4/9, 0 | | 1,321 [1,293; 1,348] | 92,94 | 5,4e-22 | 0,707 | 0,775 | 6,678; 8,709 |
| 4/9, 1/12 | | 1,390 [1,364; 1,417] | 95,54 | 1,4e-22 | 0,692 | 0,763 | 6,676; 8,724 |
| 4/9, 1/6 | | 1,459 [1,433; 1,485] | 98,30 | 3,6e-23 | 0,677 | 0,752 | 6,675; 8,740 |
| **4/9, 1** | **(II)** | 2,146 [2,124; 2,169] | 139,43 | 3,5e-32 | 0,516 | 0,646 | 6,653; 8,958 |
| 4/9, 2 | | 3,286 [3,267; 3,305] | 377,96 | 3,5e-84 | 0 | 0,498 | 6,572; 9,841 |
| 1/2, 0 | | 1,517 [1,491; 1,542] | 70,68 | 4,2e-17 | 0,665 | 0,738 | 6,691; 8,566 |
| 1/2, 1/12 | | 1,577 [1,552; 1,602] | 72,81 | 1,4e-17 | 0,651 | 0,728 | 6,690; 8,580 |
| 1/2, 1/6 | | 1,638 [1,613; 1,663] | 75,08 | 4,5e-18 | 0,638 | 0,718 | 6,688; 8,596 |
| 1/2, 1 | | 2,252 [2,230; 2,274] | 108,97 | 1,6e-25 | 0,491 | 0,621 | 6,668; 8,800 |
| **1/2, 2** | **(I)** | 3,296 [3,276; 3,315] | 308,31 | 5,1e-69 | 0 | 0,483 | 6,591; 9,623 |
| 1/2, 2 - 1,1406 eps | (I') | 2,261 [2,240; 2,282] | 95,55 | 1,4e-22 | 0,490 | 0,616 | 6,675; 8,723 |

**(B) in den Lesarten R1 und R2 (chi^2; p; Band)**

| Steigung, a | R1 | R2 |
|---|---|---|
| 4/9, 0 | 2,80; 0,094; masselos | 26,83; 2,2e-7 |
| 4/9, 1/12 | 2,72; 0,099; masselos | 26,07; 3,3e-7 |
| 4/9, 1/6 | 2,63; 0,105; uebrig | 25,27; 5,0e-7 |
| 4/9, 1 (II) | 1,62; 0,203; uebrig | 15,64; 7,7e-5 |
| 4/9, 2 | 0,040; 0,842; uebrig | 0,398; 0,528; uebrig |
| 1/2, 0 | 3,67; 0,056; (a) traegt (v_end(2) = 0,789) | 34,52; 4,2e-9 |
| 1/2, 1/12 | 3,58; 0,059; (a) traegt (0,770) | 33,72; 6,4e-9 |
| 1/2, 1/6 | 3,49; 0,062; (a) traegt (0,752) | 32,88; 9,8e-9 |
| 1/2, 1 | 2,37; 0,124; uebrig | 22,54; 2,1e-6 |
| 1/2, 2 (I) | 0,031; 0,860; uebrig | 0,307; 0,580; uebrig |
| (I') | 2,78; 0,096; uebrig | 26,25; 3,0e-7 |

R2 ohne Bandangabe heisst "traegt nicht".

**Treffer (p >= 0,05) unter den zehn Kandidaten:**
- (A): 1 von 10, naemlich (II).
- (B-R3) und (B-R2): je 2 von 10, beide mit a = 2.
- (B-R1): 10 von 10.
- (C): 0 von 10.

**(I') im Einzelnen [E, D]:**
- Beim besten m auf (A) gilt: eps(2) = 0,791, eps(4) = 0,679; a(2) = 1,098, a(4) = 1,226.
- Die Terme hoeherer Ordnung von (7.9) betragen bei J = 2 +0,011 (2. Ordnung) und -0,096 (3. Ordnung), bei
  erster Ordnung -0,902. Die Entwicklung wird also bei eps ~ 0,8 benutzt, nicht bei eps << 1.
- Auf (B) und (C) liegt eps bei 0,73 bis 0,87.

## 6. Bedeutung fuer Finns rotierendes Paar [H]

- **Was traegt (p >= 0,05) [E]:** zwei Gluonen als Massen an einem adjungierten Flussrohr (Spannung 9/4 sigma), mit dem
  theoretischen Intercept a = 1 und einer einzigen Masse m ~ 1,06 sqrt(sigma).
  - Das trifft das leichteste 2++ und das 4++* von A&T 2020 mit p = 0,16.
  - In GeV ist m etwa 0,47 bis 0,49, wenn sqrt(sigma) ~ 0,44 bis 0,46 GeV ist [M]. Der Wert 0,46 folgt aus
    r0 sqrt(sigma) = 1,160 nach A&T [S] und r0 ~ 0,5 fm [L]. Sharov setzte 0,7 GeV [S].
- **Was nicht traegt [E]:** die geschlossene Lesart (I) mit a = 2 auf denselben Daten.
  - Sie liest das 2++ als ruhendes Paar; der ganze Drehimpuls 2 kommt aus dem Intercept (bei Sharov aus den
    Gluon-Spins).
  - Mit der Korrektur nach H5 (7.9) scheitert sie ebenfalls.
- **Vorbehalte:**
  - **Look-elsewhere:**
    - Zehn Kandidaten, jeder mit freier Masse. Auf (A) besteht genau einer, und zwar der von der Karte vorab
      benannte (II). Das staerkt PQ2 gegenueber einer Suche ueber alle zehn.
    - Auf der MT-Geraden (B) bestehen in R3 und R2 dagegen genau die beiden a = 2-Kandidaten, darunter (I); (II) faellt
      dort durch.
    - Das Ergebnis haengt also an der Zuordnung und Masse des 4++. A&T kennzeichnen ihr 4++ mit Stern ("likely").
      Es ist kein Befund, der beide Gitterlesarten traegt.
  - **Schwache Probe:** zwei Punkte, ein Parameter, ein Freiheitsgrad. Ein p >= 0,05 schliesst wenig aus.
  - **Modellrahmen:** klassisch bei J = 2 bis 4, also kurze Strings (Laenge 0,8 bis 1,5/sqrt(sigma)), wo die
    Entwicklung um lange Strings nicht gesichert ist. Spannung 9/4 sigma ohne Casimir-Varianten. Gitterdaten
    synthetisch (reine Eichtheorie), keine Messung der Natur.
  - **Endgeschwindigkeit:** v_end(2) = 0,681 und v_end(4) = 0,788 im Treffer. Das vorab feste Band [0,70; 0,82] fuer
    v_end(2) ist knapp verfehlt (1-sigma-Bereich 0,678 bis 0,684), daher "uebrig". Dass Finns 3/4 zwischen beiden
    Werten liegt, ist eine Beobachtung nach der Rechnung, ohne Band und ohne Urteil.
- **Lesart [ES]:** Jede der beiden Lesarten des Paars traegt einen der beiden Gitter-Datensaetze: die offene (A), die
  geschlossene (B). Unterscheiden wuerden Spin und Masse des leichtesten 4++ auf dem Gitter, nicht dieses Modell.

## 7. Selbstanzeigen

1. **Zeiten geschaetzt, dann berichtigt (quellen/ABRUFE.log).**
   - Zwei Kommentarzeilen trugen zuerst geschaetzte Uhrzeiten ("ab 05:46", "ab 05:47").
   - Gemessen war S3 um 05:45:49. Um 05:46:13 per date berichtigt; die Berichtigung ist im Log vermerkt.
2. **Rauchtest R0a mit rc = 1.** chi2_funktion kannte den synthetischen Datensatz nicht. Vor dem Freeze behoben;
   betroffen war nur der Rauchpfad. Der Fehler ist im Plan (Abschn. 10) offengelegt.
3. **Sicht vor dem Freeze:**
   - Das Bild des Rauchtests (rauch-69/rauch.png) zeigt die Gitterpunkte mit synthetischen Modellkurven bei m = 1,3.
   - Dazu kamen die Handrechnungen fuer PQ1 und PQ2 (PLAN 6 d, e).
   - Plan, Baender und Lesarten habe ich danach nicht geaendert.
4. **(I') ausserhalb des Gueltigkeitsbereichs:** Die Entwicklung (7.9) gilt fuer kleine eps; die besten Fits liegen
   bei eps = 0,68 bis 0,87. Der Term dritter Ordnung betraegt auf (A) 8 bis 11 % des ersten. Die Karte verlangt nur
   die erste Ordnung; das Ergebnis von (I') ist deshalb nur beschreibend belastbar.
5. **Festlegungen ueber die Karte hinaus [F]:**
   - m-Bereich bis 6;
   - J_cl = 0 als ruhendes Paar;
   - Baender je Kandidat statt "mindestens ein a";
   - PQ0 nach Plan mit den Toleranzen 1e-6 (Loeser) und 5e-4 (Rundung);
   - (I') zaehlt bei PQ3 nur nach Wortlaut, bei PQ1 nicht;
   - die Lesarten R1, R2, R3 und die Hauptlesart R3 aus PAAR-REGGE-1 uebernommen.
6. **Sharov 2008 nicht im Volltext gelesen** (kein arXiv, drei Abrufe verbraucht). Ein Gittervergleich dort ist nicht
   ausgeschlossen.
7. **grep ohne Pflicht-Ausschlussflags:**
   - Ich habe nur einzeln benannte Dateien durchsucht, ohne Rekursion: hish-glueball-l/{ARBEITSFELD,DOSSIER,KARTE}.md,
     H5-Textkopie, eigene Sharov-Textkopien, gluon-paar-l/quellen/F3*.
   - Die Flags --exclude-dir usw. fehlten. Kein versiegelter oder KS-1-Pfad wurde beruehrt.
8. **Werkzeuge:**
   - Lokal: date, ls, cat, cp, mv, mkdir, sed, grep, wc, file, which, sha256sum, curl (drei Abrufe), pdftotext, jq (nur
     lesen), scp, ssh. Kein python, awk oder perl lokal.
   - .69: mkdir, mv, cat, ls, sha256sum, uptime, systemctl --user list-units (lesend), dazu eine Warteschleife mit
     sleep 5 bis zum Laufende.
9. **Abweichungen von meinen Vorab-Schaetzungen [M]:**
   - Linearisiert hatte ich fuer (C) chi^2 >= ~50 abgeschaetzt; gerechnet ist es mindestens 70,7. Die Schranke war als
     untere Grenze gemeint, die Aussage bleibt richtig.
   - Fuer PQ2 hatte ich chi^2 ~ 3 erwartet, gerechnet sind 1,98.

## 8. Einfach gesagt

Finns Bild: zwei Gluonen, durch ein Kraftband verbunden, drehen sich umeinander. Wir haben zwei Fassungen aus der
Literatur nachgerechnet, jede mit ihrem theoretisch festen Startwert und genau einer einstellbaren Gluonmasse. Die
offene Fassung (ein Band, Startwert 1) trifft die beiden Glueball-Massen der neuesten Gitterrechnung innerhalb der
Fehler, mit einer Gluonmasse von etwa einem halben GeV; die geschlossene Fassung (doppeltes Band, Startwert 2) trifft
sie nicht. Bei der aelteren Gitterrechnung, in der der Spin-4-Glueball schwerer ist, ist es genau umgekehrt. Welche
Fassung stimmt, haengt also an diesem einen, noch unsicheren Spin-4-Zustand.

## 9. Dateien

- PLAN.md, PLAN.md.eingefroren-20261005-055704, EINGEFROREN-SHA256.txt.
- code/paar_regge2.py (+ .eingefroren-20261005-055704); code/paar_regge_kopie_paar-regge-1.py (unveraenderte Kopie).
- quellen/: S1, S2 (PDF und Text), S3 (INSPIRE-JSON), ABRUFE.log.
- lauf-69/: kontrollen.json/.log, fits.json/.log, bild.log, paar-regge-2.png, PRUEFSUMMEN.txt.
- rauch-69/: Rauchtest vor dem Freeze.
- BILD-J-gegen-M2.png (= lauf-69/paar-regge-2.png).
- .69: /home/fmh/fmhc-physics-remote/paar-regge-2/ (code/, lauf/, rauch/).

![J gegen M^2](BILD-J-gegen-M2.png)

- Links (A), Mitte (B) mit dem Fit in R3, rechts (C).
- Gezeigt sind die Gitterpunkte (Fehler in M^2 = 2 M dM), die masselosen Geraden von (I) und (II) sowie die besten
  Fits von (I) (blau), (II) (orange) und (I') (gruen, gestrichelt). Die Rauten markieren die Modellwerte bei J = 2 und 4.

## Zeitbox

- Start 2026-10-05 05:42:36 CEST; Abgabe 2026-10-05 06:04:16 CEST (date, beim Schreiben dieser Zeile gemessen), also innerhalb der 90 min.
