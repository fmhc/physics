# LEITER-BETA: Ergebnis (Code-Agent, Runde 24, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 01:24:10 CEST (date).
- Rauchlaeufe (Parameter in keinem echten Lauf): .69, 23:28:45 bis 23:30:40 UTC, beide rc = 0.
- Plan eingefroren 01:39:06 CEST (PLAN.md.eingefroren-20261003-013906), nach den Rauchlaeufen und vor jedem echten Lauf.
  PLAN.md, Code und Skripte sind seither unveraendert (gleiche sha256, Abschnitt Kontrollen).
- **K0 und Phase 1** (Grobsuche): .69, 23:39:14 bis 23:48:19 UTC, sieben Aufrufe, alle rc = 0.
- **Phase 2** (8 Kandidaten auf zwei Stufen): .69, 23:48:41 bis 00:15:08 UTC, 16 Aufrufe, alle rc = 0.
- Mechanische Auswertung (auswertung.sh, jq lokal) 02:15:26 CEST: lauf-69/auswertung/. Geschrieben ab 02:18:01 CEST
  (date); Ende in der letzten Zeile.
- Markierungen: [A] Festlegung des Code-Agenten (vor den Laeufen im Plan), [H] Deutung/Hypothese. Alles gilt im linearen,
  radialen Zweikanalmodell (l = 0, abgeschnittener Rand): numerische Evidenz im Modell, keine Messung.

## Ergebnis zuerst

1. **Die stille Leiter gibt es in 3D auch bei beta = 1.** Im Bereich eps = omega^2 - 3/4 in [0,03; 0,08] liegen acht
   aufeinanderfolgende Sprossen, von eps = 0,0309 bis 0,0696.
   - Jede hat auf beiden Stufen (h = 0,04 und 0,02) einen Vorzeichenwechsel von s und einen aufgeloesten Umlauf.
   - Die Umlaeufe wechseln ab: +1, -1, +1, -1, +1, -1, +1, -1 (nach eps aufsteigend).
   - Die Stufen stimmen auf hoechstens 5,4e-8 in omega^2 und 3,6e-8 in rho ueberein. LB1 ist eingetroffen.
2. **Der Abstand passt zur ebenen Wand.**
   - Die Schritte 1/eps_(n+1) - 1/eps_n sind 2,5393 bis 2,5964 und steigen mit fallendem eps gleichmaessig an.
   - Die zwei Schritte bei kleinstem eps (2,5964 und 2,5922) liegen 0,85 % und 1,01 % unter b_inf = 2,6186. LB2 ist
     eingetroffen.
   - Aber: In der Gegenlesart "die zwei Schritte bei groesstem eps" laege 2,5393 mit -3,03 % knapp ausserhalb
     (Selbstanzeige 2).
3. **Die Sprossen liegen knapp ueber der ebenen Nullstelle:** rho_n = rho_z(1) + c eps_n mit c = 0,95 (eps 0,031) bis
   0,85 (eps 0,070). LB3 ist eingetroffen.
4. **K0 bestanden, bitgleich:** n = 10 bei beta = 1/2 kommt auf beiden Stufen ziffergleich wie in RUNDE-13 heraus
   (omega*^2 = 0,54236441 / 0,54236442, rho* = 1,5721765, Umlauf +1). LB0 ist eingetroffen.
5. **Das schmale Fano-Fenster stoert die Rechnung nicht.**
   - Am Kandidaten ist das Kernwachstum hoechstens 1,2e5. Bei beta = 1/2 waren es bis 4e7.
   - Die Rechtecke sind nach 10 bis 18 Halbierungsrunden aufgeloest.
   - Schmal sind die Polbreiten: 1,8e-6 bis 2,8e-5 in 9e-4 Abstand zur Sprosse, bei beta = 1/2 waren es 6,5e-4 bis
     2,7e-3 in 1e-3 Abstand (Zusatz).
   - Das Rechteck aus RUNDE-10 (Umlauf 0) enthaelt genau zwei Sprossen, k = 7 (+1) und k = 8 (-1). Ihre Summe ist 0,
     wie die Leitung am Schreibtisch vermutet hatte.

## Vorab gegen Ausgang

Mechanisch nach PLAN.md Abschnitt 3 und 7 (k0.jq, auswertung.jq; lauf-69/auswertung/k0.json und auswertung.json).

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| LB0 | K0 bestanden | 85 % | **eingetroffen**: beide Stufen; Abstand zu 0,5423644 +5,9e-9 / +2,0e-8, zu 1,57218 -3,5e-6; Umlauf +1, groesster Sprung 0,300 / 0,275 rad |
| LB1 | Bei beta = 1 mindestens vier aufeinanderfolgende Sprossen mit aufgeloestem Umlauf +-1 (abwechselnd) in eps [0,03; 0,08] | 55 % | **eingetroffen**: acht (k = 1 bis 8), alle Phase-1-Kandidaten, Umlauf abwechselnd |
| LB2 | Alle Schritte 1/eps_(n+1) - 1/eps_n der gefundenen Folge liegen in [2,45; 2,80], die letzten zwei innerhalb +-3 % von 2,6186 | 50 % | **eingetroffen**: sieben Schritte 2,5393 bis 2,5964; die letzten zwei (kleinste eps) 2,5964 (-0,85 %) und 2,5922 (-1,01 %) |
| LB3 | Alle gefundenen rho_n liegen in (rho_z(1), rho_z(1) + 1,5 eps_n) | 60 % | **eingetroffen**: (rho_n - rho_z)/eps_n = 0,848 bis 0,949 |

- "Die letzten zwei" ist im Plan vor den Laeufen festgelegt [A]: die zwei Schritte mit den kleinsten eps (groesste n). Das
  folgt der Zaehlung der Karte, in der eps_(n+1) < eps_n ist.
- Gegenlesart (nicht gewertet): die zwei Schritte mit den groessten eps, 2,5584 (-2,30 %) und 2,5393 (-3,03 %). Dann
  waere LB2 knapp nicht eingetroffen.

**Bedeutung (nach Karte):**
- LB1 und LB2 treffen ein: "Die ebene Wandnullstelle sagt die radiale Leiter bei beta = 1 ohne Eichung voraus. Damit ist
  RUNDE-10s offene Frage beantwortet: Die Leiter gibt es auch bei beta = 1 [H, 3D, l = 0]."
- **Einschraenkungen:**
  - "Ohne Eichung" gilt fuer den Abstand b_inf. Die Lage der Sprossen (Phase theta) und c sind nicht vorhergesagt.
  - Die gemessenen Schritte liegen 0,85 bis 3,0 % unter b_inf. Dass sie gegen b_inf laufen, ist nur eine
    nachtraegliche Ausgleichsrechnung (Nebenbefunde).
  - Nur 3D, l = 0, ein beta (1), linear, ein Code (bic2). beta = 2 ist nicht gerechnet.

## Sprossen (Phase 2; Lage aus h = 0,02)

rho_z(1) = 1,7734530718; c = (rho* - rho_z)/eps. Die Spalte "Schritt" ist 1/eps_k - 1/eps_(k+1); k zaehlt nach eps
aufsteigend, die Leiternummer n faellt also mit k. Paare stehen als h = 0,04 / h = 0,02.

| k | omega*^2 (h = 0,02) | eps | 1/eps | rho* | c | Umlauf | Schritt zum naechsten k | Stufen-Diff. omega^2 / rho | Kernwachstum am Kandidaten | Halbierungsrunden | groesster Sprung (rad) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0,78087929 | 0,030879 | 32,3842 | 1,8027610 | 0,9491 | +1 / +1 | 2,5964 | 2,2e-8 / 1,8e-8 | 1,1e5 / 1,1e5 | 18 / 18 | 0,299 / 0,294 |
| 2 | 0,78357085 | 0,033571 | 29,7877 | 1,8050552 | 0,9414 | -1 / -1 | 2,5922 | 2,4e-8 / 2,0e-8 | 4,6e4 / 4,6e4 | 16 / 16 | 0,297 / 0,292 |
| 3 | 0,78677077 | 0,036771 | 27,1955 | 1,8077352 | 0,9323 | +1 / +1 | 2,5872 | 2,6e-8 / 2,1e-8 | 1,8e4 / 1,8e4 | 15 / 15 | 0,296 / 0,296 |
| 4 | 0,79063674 | 0,040637 | 24,6083 | 1,8109062 | 0,9217 | -1 / -1 | 2,5805 | 2,9e-8 / 2,3e-8 | 7,2e3 / 7,2e3 | 14 / 14 | 0,298 / 0,299 |
| 5 | 0,79539722 | 0,045397 | 22,0278 | 1,8147134 | 0,9089 | +1 / +1 | 2,5714 | 3,3e-8 / 2,6e-8 | 2,8e3 / 2,8e3 | 13 / 13 | 0,298 / 0,296 |
| 6 | 0,80139691 | 0,051397 | 19,4564 | 1,8193633 | 0,8932 | -1 / -1 | 2,5584 | 3,8e-8 / 2,9e-8 | 1,1e3 / 1,1e3 | 12 / 12 | 0,293 / 0,290 |
| 7 | 0,80917854 | 0,059179 | 16,8980 | 1,8251555 | 0,8737 | +1 / +1 | 2,5393 | 4,5e-8 / 3,2e-8 | 4,1e2 / 4,1e2 | 11 / 11 | 0,299 / 0,297 |
| 8 | 0,81964422 | 0,069644 | 14,3587 | 1,8325332 | 0,8483 | -1 / -1 | - | 5,4e-8 / 3,6e-8 | 1,5e2 / 1,5e2 | 10 / 10 | 0,297 / 0,294 |

- **Umlauf:** aus der Phasenaufloesung, die Kreuzungszaehlung gibt ueberall dasselbe.
- **Stufen-Diff.:** h = 0,02 minus h = 0,04. Beide sind positiv und wachsen mit eps.
- **Zeilen je Kandidat:** 7 Zeilen im Abstand 3e-4 um die grobe Lage. Das Rechteck reicht ueber alle 7 Zeilen
  (1,8e-3) und rho* +- 0,01. Die Nachbarsprossen liegen mindestens 2,7e-3 entfernt.
- **s an den zwei Zeilen um den Wechsel (h = 0,02):** |s| = 1,5e-7 bis 2,4e-5. Die Stufen unterscheiden sich in s um
  2,0e-10 (k = 1) bis 4,7e-9 (k = 8).
- **Lage gegen Grobsuche:** Die Phase-2-Lage liegt 1,2e-5 bis 2,9e-5 ueber der linear interpolierten Phase-1-Lage. Die
  Zeilen der Grobsuche lagen 5,5e-4 bis 2,9e-3 auseinander.

### Grobsuche (Phase 1, h = 0,04)

| Fenster | Zeilen (Abstand) | eps-Bereich | R / r_m | Wechsel von s (zwischen den Zeilen) | Umlauf grob (Sprung) | Kernwachstum Kandidat / Fenster-Max | Laufzeit |
|---|---|---|---|---|---|---|---|
| g1 | 10 (5,5e-4) | 0,0300 .. 0,0350 | 54,5 / 15,8 | k1 0,78055/0,7811; k2 0,7833/0,78385 | +1 (0,293); -1 (0,274) | 1,0e5, 5,3e4 / 9,1e7 | 344 s |
| g2 | 10 (7,5e-4) | 0,0350 .. 0,0417 | 52,3 / 13,4 | k3 0,78645/0,7872; k4 0,7902/0,79095 | +1 (0,299); -1 (0,283) | 1,7e4, 8,4e3 / 5,6e6 | 322 s |
| g3 | 10 (1,1e-3) | 0,0417 .. 0,0516 | 50,3 / 11,0 | k5 0,795/0,7961; k6 0,8005/0,8016 | +1 (0,298); -1 (0,297) | 2,8e3, 1,3e3 / 3,4e5 | 304 s |
| g4 | 10 (1,7e-3) | 0,0516 .. 0,0669 | 48,6 / 8,7 | k7 0,8084/0,8101 | +1 (0,296) | 4,5e2 / 2,2e4 | 268 s |
| g5 | 7 (2,9e-3) | 0,0669 .. 0,0843 | 47,4 / 6,6 | k8 0,8169/0,8198 | -1 (0,300) | 1,3e2 / 1,7e3 | 186 s |

- 43 verschiedene Zeilen; benachbarte Fenster teilen ihre Randzeile.
- In jeder Zeile hat L(y_b) im ganzen rho-Fenster genau eine Nullstelle, bei 5000 + 2001 Abtastpunkten. Der Zielast ist
  ueberall durchgehend gepaart; Wechsel auf anderen Aesten gibt es nicht.
- s auf dem Ast laeuft glatt wie eine Schwingung mit wachsender Amplitude: Betrag bis 1,6e-5 bei eps 0,030 bis 0,035,
  bis 4,2e-4 bei eps um 0,08. Die Vorzeichen folgen dem Muster der acht Wechsel.
- Bei eps = 0,0843, der letzten Zeile, ist s = -8,7e-6. Die naechste Sprosse liegt also knapp jenseits von 0,08 und ist
  nicht gerechnet.

## Kontrollen

- **K0** (wie RUNDE-13, Spuren cpu und cpu6):
  - Gegen RUNDE-13 lauf-69/n10-h004 und -h002 verglichen (jq): Zielast, Wechsel, Rechteck (ohne Laufzeit), Pole, Zeilen,
    R, r_m, rho_ref und Fenstermaximum sind bitgleich.
  - Laufzeit 166 s und 290 s.
- **Numerik, alle 23 gewerteten Laeufe:**
  - Alle Profile da, nichts "entfallen", alle Illinois-Suchen konvergiert.
  - Rest |L(y_b)| an der Nullstelle hoechstens 7,8e-11; Phase 2 brauchte hoechstens 26 Schritte.
  - Phase 2: In jeder Zeile genau eine Nullstelle von L(y_b), genau ein Wechsel auf dem Zielast, keine Nebenaeste.
- **Kernwachstum:**
  - Am Kandidaten: 1,5e2 (k = 8) bis 1,15e5 (k = 1), weit unter der Grenze 1e8.
  - Das Fenstermaximum ueber das ganze rho-Fenster erreicht bei k = 1 1,67e8. Es liegt weit weg vom Ast und ist nicht
    Teil der Regel.
  - Ausloeschung am Kandidaten hoechstens 9,3e6; der Rundungsfehler von s ist damit ~1e-9 relativ.
- **Randzeilen doppelt gerechnet:** Wo zwei Fenster eine Zeile teilen (anderes R, anderes r_m), stimmt s auf 1,2e-12
  ueberein (relativ 7e-8).
- **Interpolationsfehler der Lage** (nachtraeglich geschaetzt, nicht im Plan):
  - Die Lage ist zwischen zwei Zeilen im Abstand 3e-4 linear interpoliert. Die quadratische Korrektur aus den
    Nachbarzeilen ist +1,9e-7 bis +3,7e-7 in omega^2.
  - In 1/eps sind das hoechstens 3,9e-4 (k = 1). Die Schritte aendern sich dadurch um hoechstens ~2e-4, weit unter den
    Bandbreiten von LB2 (+-7,9e-2).
  - Die Stufen-Differenz (<= 5,4e-8) misst diesen Fehler nicht, weil beide Stufen dieselben Zeilen haben.
- **Rauchlauf gegen Phase 2:** Die Rauch-Sprosse bei 0,81964213 liegt 2,1e-6 neben k = 8. Dort waren es nur 3 Zeilen im
  Abstand 7e-4.
- **Polbreiten Gamma = -Im rho am Zielast** (Pluecker-Newton, Zusatz, nicht Regel; alle konvergiert):

| k | Gamma bei -9e-4 / -6e-4 / -3e-4 | mittlere Zeile (h = 0,02 / 0,04) | Gamma bei +3e-4 / +6e-4 / +9e-4 |
|---|---|---|---|
| 1 | 2,78e-5 / 1,65e-5 / 5,02e-6 | 1,3e-8 / -4,1e-8 | 3,93e-6 / 1,43e-5 / 2,56e-5 |
| 2 | 2,35e-5 / 1,27e-5 / 3,63e-6 | 3,9e-9 / -5,0e-8 | 3,01e-6 / 1,12e-5 / 2,14e-5 |
| 3 | 1,87e-5 / 9,57e-6 / 2,69e-6 | 5,4e-9 / -4,9e-8 | 2,12e-6 / 8,26e-6 / 1,67e-5 |
| 4 | 1,40e-5 / 6,83e-6 / 1,87e-6 | 3,1e-9 / -5,2e-8 | 1,47e-6 / 5,89e-6 / 1,23e-5 |
| 5 | 9,82e-6 / 4,65e-6 / 1,26e-6 | 2,0e-9 / -5,4e-8 | 9,74e-7 / 3,98e-6 / 8,61e-6 |
| 6 | 6,42e-6 / 2,98e-6 / 7,93e-7 | 4,5e-10 / -5,7e-8 | 6,18e-7 / 2,56e-6 / 5,64e-6 |
| 7 | 3,98e-6 / 1,84e-6 / 5,06e-7 | 2,2e-9 / -5,7e-8 | 3,33e-7 / 1,46e-6 / 3,32e-6 |
| 8 | 2,16e-6 / 9,92e-7 / 2,69e-7 | 4,5e-11 / -6,1e-8 | 1,80e-7 / 7,95e-7 / 1,82e-6 |

  - Die aeusseren Spalten sind h = 0,02. Die mittlere Zeile liegt 1,2e-5 bis 3,0e-5 neben der Sprosse.
  - Die Breite faellt V-foermig zur Sprosse. Ihr Minimum liegt in der mittleren Zeile und auf h = 0,02 unter 1,3e-8.
    - Bei k = 1 erwartet man dort aus den Nachbarzeilen a d^2 = 1,3e-8, gerechnet sind 1,3e-8.
  - Auf h = 0,04 ist die mittlere Breite leicht negativ (-4e-8 bis -6e-8). Das ist der Diskretisierungsfehler dieser
    Stufe; auf h = 0,02 ist er mehr als zehnmal kleiner.
  - Die Breiten sind klein. Bei beta = 1/2 waren es in 1e-3 Abstand 6,5e-4 bis 2,7e-3 (RUNDE-13); hier in 9e-4 Abstand
    1,8e-6 bis 2,8e-5. [H] Das ist das schmale Fano-Fenster der Wand, als schwache Abstrahlung des Wandzustands entlang
    des ganzen Astes.
- **Unveraendert seit dem Einfrieren (sha256):**
  - PLAN.md = PLAN.md.eingefroren-20261003-013906: 4ab1b22b6ec5190f95beb8d55fd89853870bd20d8278f98fa6f1c40ebbbccb88
  - bic2_3d_praez.py (lokal = .69 = RUNDE-13): ba86ae6a61eb31b3afbbefcd630771ae627dfcaaa33b9bd7903b768d44838e9b
  - start1.sh f0b6f626..., gen2.sh 38b5a369..., phase1.jq c6fffe78..., k0.jq 2b91cce6..., auswertung.jq 1a820dbc...,
    auswertung.sh d01de028... (volle Werte in PLAN.md Abschnitt 9)
  - start2.sh, mechanisch erzeugt (lokal = .69): 8783ed65c705cc411dc86d59908b68515ea4caa7b380ee4c46b49634d9cb4a6d
  - kandidaten.json 7a001b58457865b9c239d31f7674e3bdc3c76dd115e94917d9533d991dcae461
  - auswertung.json 63c07a3028665cd086ce918499c1946a6e80af5087673a755ce63002584e90ef
  - k0.json c2f227f6d5f361ceeb8930566429f2e88a18a9b1268bca0dd1b2daf4718b7d93
- **Laufzeiten** (.69, Python-Start bis Ende, UTC):
  - Phase 2, h = 0,04: 189 bis 259 s; h = 0,02: 315 bis 417 s. Keiner kam an 480 s oder 600 s.
  - Wartezeiten auf Spur-Sperren bis 8,6 min (Selbstanzeige 3).
  - Einzelzeiten in lauf-69/LAUF-*.log.

**Nebenbefunde (nachtraeglich, ohne Wertung):**
- **Schritte gegen eps** (Ausgleich mit jq ueber die sieben Schritte, eps = Mittel der zwei Sprossen):
  - quadratisch: 2,6243 - 0,416 eps - 14,03 eps^2, Reste <= 1,2e-4
  - linear: Achsenabschnitt 2,655, Reste bis 2e-3, passt schlecht
  - [H] Die Folge laeuft von unten gegen ~2,62, also gegen b_inf = 2,6186 (+0,2 %). Bei beta = 1/2 liefen die Schritte
    ebenso von unten gegen 2,3100 (Papier: 2,3043 / 2,3053 / 2,3068). Die Form der Korrektur ist nicht bekannt; der
    Achsenabschnitt ist keine Messung von b_inf.
- **Nummer und Umlaufsinn [H]:**
  - Zaehlt man wie bei beta = 1/2 n = floor((1/eps)/b_inf), so sind die Sprossen n = 12 (k = 1) bis n = 5 (k = 8). Bei
    beta = 1/2 trifft dieselbe Zaehlung n = 7 bis 10.
  - Die Umlaeufe folgen dann der Regel von RUNDE-08: n gerade +1, n ungerade -1.
  - Ob das die absolute Nummer ist, ist nicht geprueft. Sprossen mit eps > 0,084 sind nicht gesucht.
  - Der Bruchteil (1/eps)/b_inf - n faellt von 0,48 (k = 8) auf 0,37 (k = 1); bei beta = 1/2 war er ~0,22.
- **Warum das Kernwachstum klein ist [H, Schreibtisch]:**
  - Die abklingende Innenwelle hat nach der Innenmatrix des Papiers (D_c = 1 + 1/(4 beta), C_c = 1/(2 beta)) bei k = 1
    die Rate kappa_in = 0,667; bei beta = 1/2, n = 10 sind es 1,004.
  - e^(kappa_in r_m) ist 5,9e4 (r_m = 16,5) bzw. 2,4e7 (r_m = 16,9), gemessen 1,15e5 bzw. 4,1e7. Bis auf einen Faktor
    ~2 erklaert das den Unterschied.
- **RUNDE-10:** Das dort aufgeloeste Rechteck (beta = 1, omega^2 0,808 bis 0,822, rho 1,805 bis 1,845, Umlauf 0)
  enthaelt k = 7 (0,80918 / 1,82516, +1) und k = 8 (0,81964 / 1,83253, -1). Sonst liegt keine Sprosse darin. Nicht
  nachgerechnet, nur aus den Lagen gelesen.

## Latten (v3)

- **L1 (kann scheitern): ja.** Vier Vorhersagen mit Zahlengrenzen standen vor jeder Rechnung, die Regeln waren vor dem
  ersten echten Lauf eingefroren. LB2 lag am Ende nahe an der Grenze: 3,03 % in der Gegenlesart.
- **L2 (Gegenprobe): teilweise.**
  - Je Sprosse zwei Kriterien (Vorzeichenwechsel von s, aufgeloester Umlauf) auf zwei Stufen.
  - Grob- und Feinsuche liefen mit eigenen Zeilen und trafen dieselben acht Stellen (1,2e-5 bis 2,9e-5).
  - Polbreiten als drittes Zeichen (Zusatz); K0 ist bitgleich.
  - Es fehlt ein unabhaengiges Programm. Alles laeuft in bic2; es gibt keine Zeitentwicklung und kein Schiessen auf
    anderem Weg.
- **L3 (Numerik): ja, mit Grenzen.**
  - Stufen-Differenz <= 5,4e-8; Interpolationsfehler <= 3,7e-7 (geschaetzt); Kernwachstum am Kandidaten <= 1,2e5.
  - Nur die Stufen h = 0,04 / 0,02; eine Stufe h = 0,01 fehlt, wie in RUNDE-13.
  - Die Breiten auf h = 0,04 haben einen Fehler ~6e-8 (Zusatz, nicht Regel).
- **L4 (schon bekannt): teilweise.**
  - Projekt: RUNDE-13 (beta = 1/2, dieselbe Methode), WAND-BETA (b_inf(1), rho_z(1)), Papierabschnitt "thin-wall
    phase-matching" (Abstandsformel).
  - Literatur zur beta-Abhaengigkeit nicht gesucht (Websuch-Kontingent erschoepft).
- **L5 (Messbezug): nein.** Modellinterne Aussage: linear, radial, l = 0.

## Selbstanzeigen

1. **Rauchlaeufe vor dem Einfrieren** (rauch.sh, 3 Zeilen, Parameter in keinem echten Lauf):
   - rauch-b zeigte die Sprosse k = 8 schon (0,819642, Umlauf -1), dazu den Ast L(y_b) = 0 bei c ~ 0,85 bis 0,94 mit
     einer Nullstelle je Zeile.
   - Fenster, Band und Zeilenabstand des Plans sind danach gewaehlt. Die Vorhersagen LB0 bis LB3 standen vorher.
     Eigene Vorhersagen habe ich nicht abgegeben.
2. **Auslegungen [A]**, im Plan vor den Laeufen festgelegt, nicht von der Leitung:
   - "die letzten zwei" Schritte = die zwei bei kleinstem eps. In der Gegenlesart (groesstes eps) waere LB2 mit -3,03 %
     nicht eingetroffen; das ist die einzige Auslegung, an der ein Urteil haengt.
   - K0 verlangt zusaetzlich Umlauf +-1.
   - Sprosse: beide Stufen, Lage auf 1e-4 gleich, Kernwachstum <= 1e8 (strenge Lesart). "Aufeinanderfolgend" heisst:
     kein Phase-1-Kandidat dazwischen.
   - Phase 2 mit 7 Zeilen im Abstand 3e-4 statt 9 im Abstand 2,5e-4 (Laufzeit bei h = 0,02).
   - rho-Abtastung 5000 Punkte im Fenster plus 2001 im Band, Phase 2 im Band 2e-6 dicht.
3. **Gemeinsame Spuren:**
   - Ein anderer Agent (runde24-tetra-stab, Einheiten r24ts-/r24tk-) nutzte zur selben Zeit cpu2, cpu3, cpu4 und cpu6.
   - Acht meiner Phase-2-Aufrufe warteten 2,0 bis 8,6 min auf die Sperre (Start von kleintest.sh bis Start von Python).
     Die Ergebnisse beruehrt das nicht (je ein Kern, eigene Einheit).
4. **Nach dem Einfrieren geschrieben, nur Darstellung:**
   - bericht.jq (Tabellenformat; einmal per sed null-fest gemacht)
   - der Ausgleich der Schritte, die Schaetzung des Interpolationsfehlers, die Polbreiten-Tabelle und der Vergleich mit
     RUNDE-13 (alles jq)
   - Keines davon geht in ein Urteil ein.
5. **Zwischenauswertungen waehrend Phase 2:**
   - Zweimal habe ich auswertung.sh auf Teilkopien im Scratchpad laufen lassen (Test der Berichtsskripte).
   - Die erste zeigte k = 2 als "Rechteck nicht aufgeloest", weil der Lauf beim Kopieren noch rechnete; die Endauswertung
     lief auf den vollstaendigen Dateien.
   - Es war nichts mehr zu entscheiden; start2.sh lief da schon unveraendert.
6. **Startbefehle:** Der ssh-Aufruf, der die Rauchlaeufe startete, kehrte nicht zurueck und wurde lokal nach 20 s
   (timeout) mit rc = 124 beendet; die Laeufe auf der .69 liefen normal zu Ende. Die spaeteren Starts kehrten zurueck.
7. **Lokal:**
   - kein Interpreter
   - nur bash, jq, ssh, scp, rsync, sha256sum, date sowie cp, mkdir, chmod, sed, cat, ls, grep, cut, head, tail, sort,
     wc, basename, dirname
   - Die jq-Skripte habe ich vor dem Einfrieren an synthetischen Daten und an RUNDE-13 n10 geprueft (Scratchpad).
8. **Sonst:**
   - kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Dienste, Timer oder Hooks
   - nur die Spuren cpu, cpu2, cpu3, cpu4 und cpu6; jeder Aufruf unter 10 min
   - auf der .69 nichts in place ueberschrieben
   - Dateien nur in RUNDE-24/leiter-beta/ und runde24-leiter-beta/
   - Plan, Code und Regeln nicht geaendert, keine Abweichung vom Plan

## Einfach gesagt

Ein Q-Ball kann bei bestimmten Frequenzen schwingen, ohne Wellen abzustrahlen; wir nennen diese Frequenzen stille
Sprossen einer Leiter. Bisher kannten wir die Leiter nur fuer eine Modellvariante. Jetzt haben wir eine zweite (beta = 1)
gerechnet und im gesuchten Bereich acht Sprossen hintereinander gefunden. Jede ist doppelt belegt, durch einen
Vorzeichenwechsel und einen vollen Umlauf, abwechselnd links- und rechtsherum, und zwei verschieden feine Rechengitter
stimmen fast vollstaendig ueberein. Der Abstand der Sprossen liegt nur 1 bis 3 % neben dem Wert, den wir vorher allein aus
einer flachen Wand berechnet hatten, und kommt ihm mit wachsendem Ball naeher. Die Sorge, die Stellen seien hier zu
schmal zum Rechnen, hat sich nicht bestaetigt; das alles gilt aber nur im Rechenmodell, nicht im Labor.

---
Letzte Aenderung dieser Datei: 2026-10-03 02:21:04 CEST (date). Zeitbox 120 min ab 01:24:10 eingehalten.
