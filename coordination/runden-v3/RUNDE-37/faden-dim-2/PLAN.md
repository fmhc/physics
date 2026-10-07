# FADEN-DIM-2: Plan des Code-Agenten (Runde 43, Fast Lane)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 21:59:20 CEST (date), Zeitbox 60 min (bis 22:59:20).
  Plan geschrieben ab 22:12:16 CEST (date), nach Kalibrierung (nur Knickdichte und kappa gesehen) und Rauchtest (nur
  Laufzeiten gesehen), vor jeder Rechnung mit Treffzahlen.
- Gelesen: KARTE.md (ganz); faden-dim-1/KARTE.md, PLAN.md, ERGEBNIS.md, code/faden.py (ganz); runden-v3/kleintest.sh
  (Kopf) und die .69-Fassung (Spurliste); weyl-linear-2/code/kette.sh (Muster).
- Kennzeichen: [E] gerechnet (.69), [M] eigene Mathematik von Hand (nicht gegengelesen), [L] Literatur aus dem
  Gedaechtnis ohne Abruf, [H] Hypothese, [F] Festlegung dieses Plans, [D] Diagnose nach Sicht.
- Vorhersagen FD0 bis FD2 und ihre Wahrscheinlichkeiten (85 / 60 / 75 %) bleiben wie in der Karte. Alles synthetisch.

## 1. Ableitbarkeitsprobe

### 1a. Kapazitaets-Skizze der Leitung (Karte, [M], ungeprueft) — Pruefung [M, L]

1. **Relativer Querverlauf.** r(x) = yA(x) - yB(x). Je Spalte ist der Schritt die Differenz zweier RSOS-Schritte;
   mittleres Schrittquadrat 2 rho (rho = Knickdichte). r ist geschlossen, weil beide Faeden geschlossen sind. Also
   eine Bruecke, die wie eine Irrfahrt mit etwa 2 rho L Einheitsschritten skaliert. **Stimmt** ("etwa": es kommen
   auch Schritte 0, sqrt 2 und 2 vor, das aendert nur Konstanten).
2. **Treffen = Verschiebung trifft die Spur.** Treffen heisst gemeinsamer Knoten in einer Spalte. Die starre
   Verschiebung addiert zu allen r(x) denselben Vektor S(t). Bei eingefrorener Form trifft also S(t) die Menge
   -{r(x)} (leicht verdickt durch die Kreuzterme yA(x) = yB(x+1) und yA(x+1) = yB(x)). **Stimmt fuer eingefrorene
   Form.** In RP aendern lokale Zuege die Form. Skalenargument [M]: Ein Brueckenstueck der raeumlichen Groesse r
   umfasst ~ r^2/rho Spalten und relaxiert (Rouse) in ~ (r^2/rho)^2 Sweeps; die Verschiebung durchquert r in
   ~ r^2 Schritten. Fuer r >> 1 ist die Form waehrend eines Vorbeigangs also eingefroren; die Formbewegung aendert
   Vorfaktoren (Skala ~ 1), nicht die Exponenten. Die Schwerpunktdrift durch lokale Zuege (~ 1/L je Sweep) ist
   gegen die starre Verschiebung (1 je Schritt) vernachlaessigbar.
3. **P ~ T cap/L^d.** Vom Gleichgewicht aus ist die Treffzeit einer kleinen Menge A auf dem Torus Z_L^d (d >= 3)
   naeherungsweise exponentiell mit Mittel ~ L^d/cap(A) [L], fuer T groesser als die Mischzeit ~ L^2 (hier
   T = 4 L^2, knapp). Genau gilt das fuer die **Rate** -ln(1 - P) ~ T cap/L^d; fuer P selbst nur bei kleinem P.
   **Stimmt fuer die Rate**, fuer P nur ohne Saettigung.
4. **Kapazitaet der Spur von n Schritten** [L]: d = 3 ~ n^(1/2) (Asselah/Schapira/Sousi 2018), d = 4 ~ n/log n
   (Lawler fuer den Erwartungswert, Asselah/Schapira/Sousi 2019 fuer das Gesetz der grossen Zahlen), d >= 5 ~ n
   (Jain/Orey 1968). **Ordnungen stimmen**; die Zuschreibung allein an Lawler ist ungenau. Fuer Bruecken gleich.
5. **Folgerung.** Rate D = 4: L^2 L^(1/2)/L^3 = L^(-1/2); D = 5: L^(-1)/log L; D = 6: L^(-2); glatt L^(3-D).
   **Stimmt.** "Grenze 3 bleibt asymptotisch" folgt daraus.
6. **Was die Skizze nicht abdeckt** [M, H]: (i) Vorasymptotik: Fuer kurze Spuren waechst cap schneller als n^(1/2)
   (zwischen n und n^(1/2)); das macht den effektiven Raten-Exponenten bei D = 4 eher flacher als -1/2. FADEN-DIM-1
   zeigte aber -0,58, obwohl dort die mit L wachsende Rauheit zusaetzlich abflacht. Bei kleinem L wirkt also noch
   etwas in die steilere Richtung (Anfangsphase: nahe startende Paare treffen sofort; -ln(1 - P) ist nur bei
   exponentieller Treffzeit linear in T) [H]. (ii) Uebergang von der Rate zu P (Saettigung bei P nahe 1).

**Urteil zur Skizze:** Sie **stimmt** in Richtung und asymptotischen Exponenten (D = 4: -1/2; D = 5: -1 mit
log-Korrektur; D = 6: -2), sofern die Form auf grossen Skalen quasi-statisch ist (Argument in Punkt 2). Sie legt
Vorfaktoren und die Exponenten bei L <= 64 nicht fest und gilt fuer die Rate, nicht fuer P. Literaturzuschreibung
ungenau (Punkt 4).

**Kopplung FD1 und FD2 [M].** Folgt die Rate zwischen L = 32 und 64 lambda(L) = lambda32 (L/32)^b und ist
P = 1 - exp(-lambda), dann ist die Zwei-Punkt-Steigung von ln P gleich ln[(1 - exp(-lambda32 2^b)) /
(1 - exp(-lambda32))] / ln 2. Mit P(32) ~ 0,67 (FADEN-DIM-1, Knickdichte 0,58): b = -0,4 gibt -0,24; b = -0,5 gibt
-0,30; b = -0,6 gibt -0,37. FD2 (Steigung unter -0,25) verlangt also etwa einen lokalen Raten-Exponenten unter
-0,42. FD1 und FD2 sind nicht unabhaengig.

**Meine Erwartung vor der Rechnung [H]:** Raten-Exponent bei D = 4 ueber L = 16 bis 64 etwa -0,5 bis -0,65 (FD1 im
Band), Steigung von ln P zwischen 32 und 64 etwa -0,3 (FD2 knapp eingetroffen). FD0 sicher (ableitbar, Abschnitt 1c).

### 1b. Rohdatenprobe FADEN-DIM-1 (lauf-69, jq 'keys')

- Alle sechs .jsonl haben je Zelle dieselben Schluessel: D, J, L, T, abgebrochen, akzeptanz_lokal, c, dyn, kappa,
  laufzeit_s, n, n_neu_gezogen_start, p, p_end_rest, p_start, schritte_gerechnet, t_treffen, treffer, zelle.
- Es gibt nur Zellsummen und Treffzeiten, keine Knickzahl je Paar. Eine Umgewichtung auf konstante Rauheit ist
  daher nicht moeglich.
- RP bei D = 4 reicht nur bis L = 32; Start-Knickdichte p = 0,6: 0,511 / 0,550 / 0,560 / 0,573 / 0,580 (L = 8 bis
  32), also keine Zelle im Band 0,59 bis 0,61. L = 48 und 64 fehlen.
- Die Treffzeiten geben P(t) fuer t < T bei festem L, aber nicht die Abhaengigkeit von L bei T = 4 L^2.
- **Urteil:** Die Rohdaten beantworten die Frage nicht. Rechnung noetig.

### 1c. FD0 ist ableitbar (Kontrolle K0) [M, L]

- Glatt: Der Querabstand ist eine einfache Irrfahrt auf Z_L^3 mit 2 Schritten je Schritt; E[tau] ~ G_3(0) L^3,
  G_3(0) = 1,516 [L]. P = 1 - exp(-8 L^2/(1,516 L^3)) = 1 - exp(-5,28/L): L = 32: 0,152; 48: 0,104; 64: 0,079.
  P L = 4,9 / 5,0 / 5,1, Faktor ~ 1,04. FD0 ist damit vorab entschieden; es prueft nur den Code bei groesserem L.

### 1d. Projekt-grep

- grep (mit allen Ausschluessen) nach "Kapazitaet der Spur", "capacity of the range", Jain-Orey, Asselah,
  FADEN-DIM-2 ueber coordination/ und model-lab/: nur Rundenprotokolle, Journal-Quelle, Dashboard und diese Karte.
  Keine fruehere Rechnung dazu.

## 2. Modell und Code [F]

- **code/faden.py**: unveraenderte Kopie aus FADEN-DIM-1 (sha256 a03a9ceb...f1d, gleich dem Original und dessen
  eingefrorener Kopie). Daraus unveraendert: Startlage (exakte Gleichgewichtsprobe der geschlossenen RSOS-Bruecke,
  Neuziehen von B bei Start-Ueberlappung), RP-Dynamik (je Schritt starre Verschiebung von A und B, dann ein Sweep
  lokaler Metropolis-Zuege in Halbsweeps, Treffpruefung nach jedem Teilzug), G-Dynamik, T = 4 L^2, Zeitgrenze 560 s
  je Prozess, Wilson-Intervall, Steigungsfit fit_steigung.
- **code/fd2.py** (neu): Kalibrierung, Saat mit Blockindex, Auswertung FD0 bis FD2, Bild. Ruft nur Funktionen aus
  faden.py auf.
- **code/kette.sh** (neu): einmalige Laufkette je Spur mit Schlusszeit, jeder Lauf ueber kleintest.sh.
- Nur RP (Plan-Modell aus FADEN-DIM-1) und G; die Karte verlangt kein RL.

## 3. Kalibrierung der Rauheit [F, E]

- **Methode.** Die geschlossene Kette mit Gewicht exp(-J K) hat die Knickzahlverteilung w(K) x^K mit
  w(K) = C(L, K) N_(D-1)(K), x = exp(-J); N_d(K) = Zahl geschlossener Wege aus K Einheitsschritten auf Z^d (exakt mit
  ganzen Zahlen). p_nom folgt per Bisektion aus <K>/L = 0,6; J = ln(2 (D-1)(1 - p_nom)/p_nom) wie in faden.run_R,
  kappa = J/2. Dieselbe Verteilung zieht faden.sample_bridges, und die Metropolis-Dynamik haelt sie (detailed
  balance auf geschlossenen Konfigurationen).
- **Gegenprobe der Formel an FADEN-DIM-1** (dort p_nom = 0,6) [E, kalib.log]: exakt 0,5080 / 0,5427 / 0,5588 /
  0,5735 / 0,5804 (D = 4, L = 8 bis 32) gegen dort gemessen 0,5114 / 0,5502 / 0,5599 / 0,5732 / 0,5798.
- **Kalibrierlauf** [E, kalib-69/kalib.log, .69 cpu, 17,5 s; Ausgabe nur Knickdichte und kappa]:

| D | L | p_nom | J | kappa | rho exakt | rho Stichprobe (4096 Bruecken) | rho nach 200 Sweeps (512 Bruecken) |
|---|---|---|---|---|---|---|---|
| 4 | 16 | 0,637093 | 1,2290 | 0,6145 | 0,60000 | 0,6021 | 0,5906 |
| 4 | 24 | 0,624774 | 1,2819 | 0,6409 | 0,60000 | 0,6014 | 0,5975 |
| 4 | 32 | 0,618615 | 1,3081 | 0,6540 | 0,60000 | 0,5994 | 0,6019 |
| 4 | 48 | 0,612438 | 1,3342 | 0,6671 | 0,60000 | 0,6015 | 0,6015 |
| 4 | 64 | 0,609339 | 1,3472 | 0,6736 | 0,60000 | 0,5999 | 0,5965 |
| 5 | 8 | 0,694680 | 1,2574 | 0,6287 | 0,60000 | 0,6022 | 0,5947 |
| 5 | 12 | 0,665759 | 1,3904 | 0,6952 | 0,60000 | 0,6005 | 0,6149 |
| 5 | 16 | 0,649599 | 1,4622 | 0,7311 | 0,60000 | 0,5954 | 0,6006 |
| 5 | 24 | 0,633042 | 1,5342 | 0,7671 | 0,60000 | 0,5999 | 0,6034 |

- Zum Vergleich FADEN-DIM-1: kappa 0,6931 (D = 4) und 0,8370 (D = 5) fuer alle L.
- Die Dynamikprobe bei D = 5, L = 12 liegt 0,015 neben 0,6. Bei 512 x 12 Spalten ist der Zufallsfehler ~ 0,006
  (2,4 Fehlerbreiten); ich werte das als Zufall, die Laeufe pruefen es mit grosser Zahl (Start und Ende).
- **Toleranz [F]:** Eine Zelle hat konstante Rauheit, wenn ihre gemessene Start-Knickdichte (alle 2 n Faeden)
  |rho_start - 0,6| <= 0,01 erfuellt. Knickdichte am Ende (ueberlebende Paare) wird berichtet, nicht bewertet.
- Die Laeufe rechnen p_nom selbst mit derselben Funktion (Zelle "kal"); der Wert steht im Datensatz.

## 4. Zellen, Paare, Saaten [F]

| Serie | L | Paare je L | Bloecke |
|---|---|---|---|
| RP, rho = 0,6, D = 4 | 16, 24, 32 | 3072 | 1 |
| RP, rho = 0,6, D = 4 | 48, 64 | 3072 | 3 x 1024 |
| G, D = 4 | 32, 48, 64 | 8192 | 1 |
| RP, rho = 0,6, D = 5 (beschreibend) | 8, 12, 16, 24 | 4096 | 1 |

- T = 4 L^2 (faden.C_T). Saat: numpy default_rng([20261004, 2, Dynamikcode (G 1, RP 3), D, L, n_Block, Block]).
  Bootstrap-Saat [20261004, 2, 99].
- Bloecke einer Zelle werden in der Auswertung addiert (Treffer und Paare); verschiedene p_nom oder doppelte Bloecke
  brechen die Auswertung ab.

## 5. Auswertung und Urteilsregeln [F]

- **P** = Treffer/Paare, Wilson-95-%. **Rate** = -ln(1 - P~), P~ = (Treffer + 0,5)/(Paare + 1).
- **Steigung von ln P:** faden.fit_steigung unveraendert (gewichtete Gerade ln P~ gegen ln L, Gewicht n P~/(1 - P~)).
- **Exponent der Rate:** gewichtete Gerade ln(-ln(1 - P~)) gegen ln L, Gewicht n (1 - P~) ln(1 - P~)^2 / P~
  (Kehrwert der Varianz nach Deltamethode).
- **Zwei-Punkt-Steigung:** ln(P~64/P~32)/ln 2.
- **Bootstrap:** je Fit 2000 parametrische Ziehungen (Treffer ~ Bin(n, Treffer/n) je Zelle), Perzentile 2,5/97,5.
- Abgebrochene Zellen zaehlen nirgends. "Im Band" = |rho_start - 0,6| <= 0,01.

| Nr | Karte | nach Plan | nach Kartenwortlaut |
|---|---|---|---|
| FD0 | G, D = 4: P L zwischen L = 32 und 64 konstant bis Faktor 1,5 (85 %) | Faktor aus Wilson-Grenzen max(PL_hi)/min(PL_lo) ueber L = 32, 48, 64 <= 1,5: eingetroffen; Punktfaktor > 1,5: nicht eingetroffen; sonst uneindeutig | Punktfaktor max(PL)/min(PL) ueber L = 32, 48, 64 <= 1,5: eingetroffen, sonst nicht |
| FD1 | RP, Rauheit 0,6, D = 4: Exponent der Rate ueber L = 16 bis 64 in [-0,75; -0,35] (60 %) | Fit ueber alle fuenf L, alle im Band (sonst nicht auswertbar). Bootstrap-95-% ganz im Band: eingetroffen; ganz ausserhalb: nicht eingetroffen; sonst uneindeutig | Punktwert des Fits ueber alle nicht abgebrochenen Zellen L = 16 bis 64 im Band: eingetroffen, sonst nicht |
| FD2 | RP, Rauheit 0,6, D = 4: lokale Steigung von P zwischen L = 32 und 64 unter -0,25, Schwellregel, Grenze 3 (75 %) | Schwellregel FADEN-DIM-1 auf den Fit von ln P ueber L = 32, 48, 64 (alle im Band, sonst nicht auswertbar): Steigung < -0,25 und obere 95-%-Grenze < 0: eingetroffen (Grenze 3), sonst nicht eingetroffen | Zwei-Punkt-Steigung zwischen L = 32 und 64 < -0,25: eingetroffen, sonst nicht |

- Zusatz zu FD2 (beschreibend, kein Urteil): ob das ganze 95-%-Intervall unter -0,25 liegt. "Grenze 3" setzt
  voraus, dass auch D >= 5 faellt; D = 5 ist hier nur beschreibend (FADEN-DIM-1: D = 5 und 6 fallen deutlich).
- Beschreibend [D]: lokale Steigungen und Raten-Exponenten je Nachbarpaar von L (RP D = 4, G D = 4, RP D = 5);
  Steigung von ln P ueber L = 16 bis 64; D = 5: Steigung und Raten-Exponent ueber L = 8 bis 24; Treffzeit-Median/L^2;
  Knickdichte Start/Ende; Annahmerate; Bloecke einzeln (Treffer je Block als Konsistenzprobe).
- Die Urteile rechnet der eingefrorene Code (fd2.py auswertung); ich pruefe sie von Hand gegen die Tabelle.

## 6. Abbruchregeln [F]

- Je Lauf: faden-interne Zeitgrenze 560 s ab Prozessstart (Zelle "abgebrochen", Rest des Laufs entfaellt);
  kleintest.sh RuntimeMaxSec 600.
- Kette: kein neuer Lauf nach 22:45:00 CEST (SCHLUSS in kette.sh); nach dem Zeitbox-Ende 22:59:20 startet nichts.
- Fehlt eine noetige Zelle oder liegt sie ausserhalb des Rauheitsbands, ist das Plan-Urteil "nicht auswertbar";
  das Kartenwortlaut-Urteil nimmt alle nicht abgebrochenen Zellen (gekennzeichnet).
- Kein Nachrechnen mit geaendertem Code oder geaenderter Saat. Wiederholung mit identischem Code und gleicher Saat
  nur bei aeusserem Abbruch (Lock, Speicher, ssh), dokumentiert.
- Nach dem Einfrieren keine Aenderung an Plan, Urteilsregeln oder Code. Alles nach Sicht steht als gekennzeichneter
  Nachtrag in neuen Dateien.

## 7. Laufzeitschaetzung [E aus Rauchtest, rauch.log]

- Rauchtest (nur Laufzeiten): RP D = 4, L = 64: 213 ns, L = 48: 215 ns, RP D = 5, L = 24: 222 ns je Paar, Schritt
  und Spalte; G D = 4, L = 64: 85 ns je Paar, Schritt und Querrichtung.
- Schlechtester Fall (kein Paar trifft) je Block: RP D = 4, L = 64, 1024 Paare: 229 s; L = 48, 1024 Paare: 97 s;
  L = 32, 3072: 86 s; L = 24, 3072: 36 s; L = 16, 3072: 10 s; G (alle drei L, 8192): 62 s; RP D = 5 (alle vier L,
  4096): 73 s.
- Spur cpu: fd2a (L = 64 Block 0, L = 48 Block 0) <= 331 s; fd2b (L = 64 Block 1, L = 16, 24) <= 278 s.
- Spur cpu10: fd2c (L = 64 Block 2, L = 48 Block 1) <= 331 s; fd2d (L = 48 Block 2, L = 32, G, D = 5) <= 320 s.
- Je Spur hoechstens ~ 11 min, erwartet ~ 7 bis 9 min (getroffene Paare fallen heraus). Danach Auswertung und Bild
  (cpu, je < 1 min).

## 8. Einfrieren

- Kopien PLAN.md.eingefroren-<Stempel>, code/faden.py.eingefroren-<Stempel>, code/fd2.py.eingefroren-<Stempel>,
  code/kette.sh.eingefroren-<Stempel>; sha256 in EINGEFROREN-SHA256.txt; auf der .69 dieselben Pruefsummen.
- Die Laeufe benutzen code/fd2.py, code/faden.py und code/kette.sh, bytegleich mit den eingefrorenen Kopien.
