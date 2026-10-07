# BILDUNG-1 (Runde 22): Ergebnis

Code-Agent (Claude, Anthropic), Auftrag der Leitung claude-primary. Beginn 2026-10-02 19:02:26 CEST (date).
Rauchlauf 19:12:49 bis 19:13:27 CEST. Plan eingefroren 19:15:21 CEST (PLAN.md.eingefroren-20261002-191521), vor jedem
echten Lauf. Laeufe 19:15:30 bis 19:25:03 CEST auf der .69 (Uhr dort UTC). Ergebnis geschrieben ab 19:26:13 CEST, Ende
der Bearbeitung in der letzten Zeile. Explorativ (v3), Deutungen [H, im Modell].

## 1. Ergebnis zuerst

1. **B1 und B2 eingetroffen: Alle drei Gauss-Klumpen laufen von selbst auf die Familie, auf beiden Gittern.**
   - (i), Breite passend: schon im ersten Fenster (T = 50) "auf" und rund, bis T = 1000 durchgehend. Der Ball behaelt
     99,3 % der Ladung.
   - (ii), 30 % breiter: zu T = 50 "unentschieden" (starkes Atmen, u = 0,019), ab T = 100 "auf". Er behaelt 92,2 %.
   - (iii), 30 % schmaler: zu T = 50 "gestoert" (Q-Schwankung 33 %), zu T = 100 "unentschieden", ab T = 200 "auf".
     Er behaelt nur 62,6 % und landet auf einem anderen Familienpunkt: omega 0,7956 statt 0,7746, Q = 41,7 statt 66,6.
2. **B3 nicht eingetroffen.** Am Fall (iii) scheitert die 80-%-Grenze.
   - Er verliert 37 % seiner Ladung, fast alles zwischen t = 10 und 60. Q(r <= 12) faellt dort von 0,9999 auf 0,65.
   - Das passt zum Start: Der schmale Klumpen hat E/Q = 1,158, mehr Energie je Ladung als freie ruhende Quanten (1).
3. **B0 eingetroffen, Box-Pruefung bestanden.**
   - K0: Der exakte Familienball ist im selben Aufbau zu allen sechs Zeiten "auf" und rund, auf beiden Gittern. Seine
     Ladung driftet bis T = 1000 um hoechstens 8e-9.
   - Box: Der dichte Kern (S >= 0,6) bleibt in allen acht Laeufen innerhalb max(|x|, |y|) <= 3,1, Grenze 24. Abgegeben
     wird nur Strahlung: 0,7 / 7,5 / 37 % der Ladung (i / ii / iii) erreichen den Absorber.
4. **Nachtraeglich bemerkt [H]: "auf" ist hier mehr als "Q passt zu omega".**
   - Auch E/Q liegt am Ende auf der Familie. Bei (i) und (ii) liegt der E/Q-Abstand ab T = 100 zwischen -0,02 und
     0 %, so nah wie beim exakten K0 (-0,02 %).
   - Bei (iii) laeuft die Energie langsamer nach: +1,3 % (T 200), +0,3 % (T 500), +0,01 % (T 1000). Die
     Klassifikation "auf" (ab 200) kommt also vor der energetischen Ruhe.
5. **Bedeutung nach Karte (B1 und B2 eingetroffen):** Einzelne Klumpen laufen auf die Familie zu. M1 ist in 2D fuer
   isolierte Klumpen bildungsfaehig (Stufe 5, im Modell) [H]. Das "nie auf" in KF-5 lag dann am Verschmelzen bzw. an
   der Zeit.
   - Grenze: nur Q = Q_F bei omega^2 = 0,60 (Q 66,6), radialsymmetrisch, im Vakuum mit Absorber. Die KF-5-Tropfen
     lagen bei Q 1300 bis 2100 und omega 0,72, in einem Wellenbad.
   - [H, nachtraeglich] "An der Zeit" traegt hier wenig. Die Klumpen brauchten 50 bis 200 Zeiteinheiten, KF-5 lief bis
     800 bzw. 2000. Naeher liegt das Verschmelzen bzw. die Umgebung (Bad, Nachbarn); geprueft ist das nicht.

## 2. K0 und Box-Pruefung

**Setzen und K-Pruefung bei t = 0** (beide Gitter; Abweichungen relativ):

| Fall | s | A | S_max | Q gegen Q_F | r_rms auf dem Gitter | E/Q (Familie 0,84855) | K (1e-3) |
|---|---|---|---|---|---|---|---|
| K0 (Familienball, Profil aus kf_eich) | - | f(0) | 1,06119 | +7,1e-8 | 3,074145, gegen r_ladung -3,5e-7 | 0,84855 (E +6,6e-8; omega Gittergleichung -5e-11 grob / -2e-11 fein) | bestanden |
| (i) | 3,074146 | 1,203476 | 1,44835 | 0 | = s (Abweichung 0) | 0,85932 | bestanden |
| (ii) | 3,996390 | 0,925751 | 0,85701 | -2,2e-16 | = s (2,2e-16) | 0,87563 | bestanden |
| (iii) | 2,151903 | 1,719251 | 2,95582 | 0 | = s (2,2e-16) | 1,15814 | bestanden |

- **Ladungsradius (Plan, Abschnitt 3):**
  - r_ladung der Familiendatei ist der rms-Ladungsradius. Am Profil gerechnet 3,074146, rel -1,9e-7. Die Kandidaten
    "mittel" (2,780) und "halb" (2,692) passen nicht.
  - Fuer den Gauss ist r_rms = s, also s(i) = R_F.
  - Der Radius des Klassifikators (Maske S >= 0,6) ist fuer (i) nicht erreichbar, siehe Plan.
- **K0** (exakter Familienball im Absorberaufbau): 12 von 12 Fenstern "auf" und rund (T 50, 100, 200, 250, 500,
  1000; grob und fein). Entscheidend sind T 50 / 100 / 200, 6 von 6.
  - rmax/R_A 0,998 grob / 0,997 fein.
  - Q-Anteil 0,9997.
  - dQ* +0,04 % grob / -0,01 % fein.
  - omega 0,77462 / 0,77460 (Soll 0,774597), u hoechstens 2,2e-6.
  - E/Q-Abstand -0,02 %. Das ist die Grundlinie der Scheibenbilanz und wie in Runde 21.
- **Box-Pruefung** (Regel: Maske S >= 0,6 zu allen Diagnosezeiten 0, 10, ..., 1000 innerhalb max(|x|, |y|) <= 24):

| Lauf | Maske 0,6: max-Norm max | Maske 0,2: max | Q_box(1000)/Q0 | Ladung im Rahmen, max | Q(r <= 12)/Q0 bei 1000 | Urteil |
|---|---|---|---|---|---|---|
| grob K0 | 3 | 4,25 | 1,000000 (Drift max 7,6e-9) | 1,1e-9 | 1,0000 | bestanden |
| fein K0 | 3,125 | 4,25 | 1,000000 (Drift max 2,7e-9) | 3,1e-10 | 1,0000 | bestanden |
| grob (i) | 3 | 4,25 | 0,99323 | 2,6e-3 | 0,9932 | bestanden |
| fein (i) | 3,125 | 4,25 | 0,99323 | 2,7e-3 | 0,9932 | bestanden |
| grob (ii) | 3 | 4,75 | 0,92513 | 1,2e-2 | 0,9226 | bestanden |
| fein (ii) | 3 | 4,75 | 0,92512 | 1,2e-2 | 0,9226 | bestanden |
| grob (iii) | 2,75 | 5 | 0,63109 | 5,1e-2 | 0,6266 | bestanden |
| fein (iii) | 2,75 | 5,125 | 0,63050 | 5,2e-2 | 0,6260 | bestanden |

- Was der Box fehlt, ist abgestrahlte Ladung. Sie lief als Welle nach aussen (Front S >= 1e-4 mit etwa 0,75 je
  Zeiteinheit, Rauchlauf) und wurde im Rahmen geschluckt.
- Die Ballladung blieb im Zentrum. Q_net des Balls und Q(r <= 12) stimmen am Ende auf 0,0005 ueberein.

## 3. Tabelle je Klumpen, Gitter und Zeit (S0 = 0,3, Hauptauswertung)

Legende:
- Werte aus dem Messfenster [T - 40, T] des Runde-6-Klassifikators.
- **Q-Anteil** = Q_net / Q0 (Q0 = Q_F = 66,616). **Q(r<=12)** ist Q im Kreis r <= 12 am Fensterbeginn, ebenfalls / Q0.
- **omega** = omega_ruhe +- u. **E/Q** = E_ruhe_net / Q_net, in Klammern der Familienwert beim selben Q.
- **dQ*** = Q / Q_fam(omega) - 1. **E/Q-Abst.** = (E/Q) / (E/Q)_fam(Q) - 1. **omega-Abst.** = omega - omega_fam(Q).
- **rund** heisst rmax/R_A <= 1,3 am Fensterbeginn. **S_max** = S_max des Balls am Fensterbeginn.
- Kein Lauf hatte "verloren" oder "Stoss". v gemessen ist ueberall 0,0000.
- Zahlenformat: Dezimalpunkte aus jq, gerundet auf 4 bis 5 Stellen. Nullen am Ende fallen weg ("0.7746" = 0,77460),
  "+- 0" heisst u < 5e-6.
- Erzeugt mit hilfs/tabelle.jq aus den Ergebnis-JSON; hilfs/tabelle-s0-0.3.md ist danach nur noch ein Verweis.

| Fall | Gitter | T | Urteil | rund, rmax/R_A | Q-Anteil | Q(r<=12) | omega +- u | E/Q (fam) | dQ* | E/Q-Abst. | omega-Abst. | Q-Schwankung | S_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K0 | grob | 50 | auf | ja 0.998 | 0.9997 | 1 | 0.77462 +- 0 | 0.8484 (0.8486) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| K0 | fein | 50 | auf | ja 0.997 | 0.9997 | 1 | 0.7746 +- 0 | 0.8484 (0.8486) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| K0 | grob | 100 | auf | ja 0.998 | 0.9997 | 1 | 0.77462 +- 0 | 0.8484 (0.8486) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| K0 | fein | 100 | auf | ja 0.997 | 0.9997 | 1 | 0.7746 +- 0 | 0.8484 (0.8486) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| K0 | grob | 200 | auf | ja 0.998 | 0.9997 | 1 | 0.77462 +- 0 | 0.8484 (0.8486) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| K0 | fein | 200 | auf | ja 0.997 | 0.9997 | 1 | 0.7746 +- 0 | 0.8484 (0.8486) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| K0 | grob | 250 | auf | ja 0.998 | 0.9997 | 1 | 0.77462 +- 0 | 0.8484 (0.8486) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| K0 | fein | 250 | auf | ja 0.997 | 0.9997 | 1 | 0.7746 +- 0 | 0.8484 (0.8486) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| K0 | grob | 500 | auf | ja 0.998 | 0.9997 | 1 | 0.77462 +- 0 | 0.8484 (0.8486) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| K0 | fein | 500 | auf | ja 0.997 | 0.9997 | 1 | 0.7746 +- 0 | 0.8484 (0.8486) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| K0 | grob | 1000 | auf | ja 0.998 | 0.9997 | 1 | 0.77462 +- 0 | 0.8484 (0.8486) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| K0 | fein | 1000 | auf | ja 0.997 | 0.9997 | 1 | 0.7746 +- 0 | 0.8484 (0.8486) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| i | grob | 50 | auf | ja 0.986 | 0.9933 | 0.9995 | 0.77477 +- 0.00038 | 0.8496 (0.849) | -0.2 % | 0.06 % | -0.0001 | 0.5 % | 1.088 |
| i | fein | 50 | auf | ja 1 | 0.9933 | 0.9995 | 0.77475 +- 0.00038 | 0.8495 (0.849) | -0.3 % | 0.06 % | -0.0001 | 0.5 % | 1.088 |
| i | grob | 100 | auf | ja 0.996 | 0.9929 | 0.9932 | 0.77487 +- 3e-05 | 0.8489 (0.8491) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| i | fein | 100 | auf | ja 0.998 | 0.9929 | 0.9933 | 0.77485 +- 3e-05 | 0.8489 (0.8491) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| i | grob | 200 | auf | ja 0.998 | 0.9929 | 0.9932 | 0.77488 +- 1e-05 | 0.8489 (0.8491) | 0.1 % | -0.02 % | 0 | 0 % | 1.062 |
| i | fein | 200 | auf | ja 0.997 | 0.9929 | 0.9932 | 0.77486 +- 1e-05 | 0.8489 (0.8491) | -0 % | -0.02 % | -0 | 0 % | 1.062 |
| i | grob | 250 | auf | ja 0.998 | 0.9929 | 0.9932 | 0.77487 +- 2e-05 | 0.8489 (0.8491) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| i | fein | 250 | auf | ja 0.997 | 0.9929 | 0.9932 | 0.77485 +- 2e-05 | 0.8489 (0.8491) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| i | grob | 500 | auf | ja 0.998 | 0.9929 | 0.9932 | 0.77488 +- 1e-05 | 0.8489 (0.8491) | 0.1 % | -0.02 % | 0 | 0 % | 1.061 |
| i | fein | 500 | auf | ja 0.997 | 0.9929 | 0.9932 | 0.77486 +- 1e-05 | 0.8489 (0.8491) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| i | grob | 1000 | auf | ja 0.998 | 0.9929 | 0.9932 | 0.77488 +- 0 | 0.8489 (0.8491) | 0 % | -0.02 % | 0 | 0 % | 1.061 |
| i | fein | 1000 | auf | ja 0.997 | 0.9929 | 0.9932 | 0.77486 +- 0 | 0.8489 (0.8491) | -0 % | -0.02 % | -0 | 0 % | 1.061 |
| ii | grob | 50 | unentschieden | ja 0.998 | 0.9504 | 0.9984 | 0.77503 +- 0.01929 | 0.8611 (0.8523) | -3.8 % | 1.03 % | -0.0015 | 6.6 % | 1.23 |
| ii | fein | 50 | unentschieden | ja 0.998 | 0.9505 | 0.9984 | 0.77502 +- 0.01929 | 0.8611 (0.8523) | -3.9 % | 1.03 % | -0.0015 | 6.6 % | 1.23 |
| ii | grob | 100 | auf | ja 0.993 | 0.9231 | 0.9299 | 0.77756 +- 0.00284 | 0.8546 (0.8546) | -0.2 % | 0 % | -0.0001 | 0.6 % | 1.065 |
| ii | fein | 100 | auf | ja 0.996 | 0.9231 | 0.93 | 0.77754 +- 0.00284 | 0.8546 (0.8546) | -0.3 % | 0 % | -0.0001 | 0.6 % | 1.065 |
| ii | grob | 200 | auf | ja 1.013 | 0.922 | 0.9229 | 0.77783 +- 0.00082 | 0.8545 (0.8547) | 0.3 % | -0.02 % | 0.0001 | 0.1 % | 1.056 |
| ii | fein | 200 | auf | ja 1.001 | 0.922 | 0.9229 | 0.77781 +- 0.00081 | 0.8545 (0.8547) | 0.3 % | -0.02 % | 0.0001 | 0.1 % | 1.056 |
| ii | grob | 250 | auf | ja 0.993 | 0.9224 | 0.9231 | 0.77752 +- 0.00091 | 0.8545 (0.8546) | -0.4 % | -0.01 % | -0.0002 | 0.1 % | 1.066 |
| ii | fein | 250 | auf | ja 0.995 | 0.9224 | 0.9231 | 0.7775 +- 0.00093 | 0.8545 (0.8546) | -0.5 % | -0.01 % | -0.0002 | 0.1 % | 1.066 |
| ii | grob | 500 | auf | ja 0.993 | 0.9224 | 0.9228 | 0.77774 +- 0.0003 | 0.8545 (0.8546) | 0.1 % | -0.01 % | 0.0001 | 0.1 % | 1.059 |
| ii | fein | 500 | auf | ja 0.996 | 0.9224 | 0.9228 | 0.77772 +- 0.00028 | 0.8545 (0.8546) | 0.1 % | -0.01 % | 0 | 0.1 % | 1.059 |
| ii | grob | 1000 | auf | ja 0.993 | 0.9223 | 0.9228 | 0.77767 +- 0.00059 | 0.8545 (0.8546) | -0.1 % | -0.02 % | -0 | 0.1 % | 1.06 |
| ii | fein | 1000 | auf | ja 0.996 | 0.9223 | 0.9227 | 0.77765 +- 0.00061 | 0.8545 (0.8546) | -0.1 % | -0.02 % | -0 | 0.1 % | 1.06 |
| iii | grob | 50 | gestoert | ja 0.98 | 0.6802 | 0.9999 | 0.80163 +- 0.03151 | 0.9238 (0.8799) | 20.9 % | 4.99 % | 0.0104 | 33 % | 0.667 |
| iii | fein | 50 | gestoert | ja 0.991 | 0.6793 | 0.9999 | 0.80167 +- 0.03148 | 0.9239 (0.88) | 20.8 % | 4.99 % | 0.0104 | 32.8 % | 0.667 |
| iii | grob | 100 | unentschieden | ja 0.983 | 0.6306 | 0.6489 | 0.79476 +- 0.00603 | 0.9039 (0.8867) | -0.8 % | 1.94 % | -0.0004 | 1.4 % | 0.918 |
| iii | fein | 100 | unentschieden | ja 0.999 | 0.63 | 0.6484 | 0.79479 +- 0.00605 | 0.9041 (0.8867) | -0.8 % | 1.96 % | -0.0004 | 1.4 % | 0.918 |
| iii | grob | 200 | auf | ja 0.982 | 0.6301 | 0.6321 | 0.79557 +- 0.00018 | 0.8985 (0.8867) | 0.6 % | 1.32 % | 0.0003 | 0.3 % | 1.07 |
| iii | fein | 200 | auf | ja 1.002 | 0.6295 | 0.6315 | 0.7956 +- 0.00017 | 0.8987 (0.8868) | 0.6 % | 1.33 % | 0.0003 | 0.3 % | 1.072 |
| iii | grob | 250 | auf | ja 0.988 | 0.6302 | 0.6316 | 0.79543 +- 0.00291 | 0.8963 (0.8867) | 0.4 % | 1.08 % | 0.0002 | 0.3 % | 1.113 |
| iii | fein | 250 | auf | ja 0.993 | 0.6296 | 0.631 | 0.79546 +- 0.00288 | 0.8965 (0.8868) | 0.4 % | 1.09 % | 0.0002 | 0.3 % | 1.112 |
| iii | grob | 500 | auf | ja 0.982 | 0.6273 | 0.6279 | 0.79544 +- 0.00032 | 0.8898 (0.8871) | -0 % | 0.3 % | -0 | 0.2 % | 1.07 |
| iii | fein | 500 | auf | ja 0.993 | 0.6267 | 0.6273 | 0.79546 +- 0.00025 | 0.89 (0.8872) | -0.1 % | 0.31 % | -0 | 0.2 % | 1.069 |
| iii | grob | 1000 | auf | ja 0.99 | 0.6262 | 0.6267 | 0.79556 +- 0.00023 | 0.8873 (0.8873) | 0 % | 0.01 % | 0 | 0.1 % | 1.039 |
| iii | fein | 1000 | auf | ja 1.001 | 0.6256 | 0.6261 | 0.79559 +- 0.00031 | 0.8874 (0.8874) | -0 % | 0.01 % | -0 | 0.1 % | 1.039 |

- T 50 und 200 sind fuer die Klumpen nur beschreibend; die Karte entscheidet an 100, 250, 500, 1000.
- **Zusatz S0 = 0,1** (Schwelle 0,2, dieselben Laeufe): Alle 48 Klassen sind gleich wie bei S0 = 0,3.
  - Bei T = 1000 sind die Q-Anteile 0,9932 / 0,9225 / 0,6265 (grob) bzw. 0,6259 (fein, iii).
  - Zeilen in hilfs/tabelle-s0-0.1.md.

## 4. B0 bis B3

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| B0 | K0 bestanden | 90 % | **eingetroffen** | 6 von 6 "auf" und rund (T 50 / 100 / 200, grob und fein); auch zu 250, 500, 1000. rmax/R_A 0,997 bis 0,998, dQ* -0,01 bis +0,04 %, u <= 2,2e-6, Q-Drift der Box <= 8e-9 |
| B1 | (i) bei T = 500 "auf" und "rund", beide Gitter | 65 % | **eingetroffen** | 2 von 2. Q-Anteil 0,9929, omega 0,77488 / 0,77486 +- 1e-5 (Familie bei diesem Q 0,77486), dQ* +0,05 / -0,00 %, E/Q-Abstand -0,02 %, rmax/R_A 0,998 / 0,997. "auf" schon ab T = 50 |
| B2 | (ii) und (iii) bei T = 1000 beide "auf" und "rund", beide Gitter | 50 % | **eingetroffen** | 4 von 4. (ii): omega 0,77767 / 0,77765, dQ* -0,06 / -0,11 %, rmax/R_A 0,993 / 0,996. (iii): omega 0,79556 / 0,79559, dQ* +0,01 / -0,02 %, rmax/R_A 0,990 / 1,001 |
| B3 | Alle drei behalten bei T = 1000 >= 80 % der Anfangsladung | 60 % | **nicht eingetroffen** | Q-Anteil (S0 0,3, Fenster [960, 1000]) grob / fein: (i) 0,9929 / 0,9929; (ii) 0,9223 / 0,9223; (iii) **0,6262 / 0,6256** |

- Die Box-Pruefung ist fuer alle acht Laeufe bestanden. Kein B ist deshalb "offen".
- Die Bedeutung folgt mechanisch aus B1 und B2 (Abschnitt 1, Punkt 5). B3 aendert sie nach der Karte nicht.
  - B3 zeigt aber: Ein zu kompakter Klumpen wird nicht zum Ball seiner eigenen Ladung. Er wirft gut ein Drittel ab und
    wird zum Familienball einer kleineren Ladung [H].

## 5. Latten, Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Latten (v3):**
- **L1 kann scheitern:** ja. B3 ist gescheitert. B1 und B2 konnten an Atmen (u), Rundheit oder Zerfliessen scheitern.
  Zu T = 50 bzw. 100 waren (ii) und (iii) tatsaechlich noch nicht "auf".
- **L2 Gegenprobe:** ja.
  - K0 im selben Aufbau: "auf" zu allen Zeiten, Q-Drift <= 8e-9.
  - r_rms des K0-Balls auf dem Gitter gegen r_ladung: -3,5e-7.
  - Zwei Ladungsmasse: Q_net (Scheibe) gegen Q(r <= 12), am Ende auf 0,0005 gleich.
  - Zwei Schwellen mit 48 von 48 gleichen Klassen.
  - E/Q-Abstand als energetische Gegenprobe zu "Q passt zu omega" (Abschnitt 1, Punkt 4).
- **L3 Numerik:** bestanden.
  - Grob und fein geben in allen 48 Paaren (Fall x T x S0) dieselbe Klasse.
  - |Delta omega| <= 4,0e-5, |Delta Q-Anteil| <= 9,1e-4 (ab T = 100: 6,2e-4).
- **L4 schon bekannt:** Dass angeregte Klumpen durch Abstrahlung zu Q-Baellen relaxieren und zu kompakte einen Teil
  ihrer Ladung abwerfen, ist allgemein aus der Literatur zu Q-Baellen und Oszillonen bekannt [L, nicht nachgeprueft,
  keine Literaturabfrage]. Neu ist nur der Befund fuer M1 in 2D mit diesem Klassifikator.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter).

**Grenzen:**
- **Ein Familienpunkt, ein Q.** Alle Klumpen tragen Q_F bei omega^2 = 0,60 (Q 66,6, dicke Wand). Die KF-5-Tropfen lagen
  bei Q 1300 bis 2100 nahe omega^2 = 0,52, also anders. Die Uebertragung auf KF-5 ist [H].
- **Symmetrie.** Die Starts sind radialsymmetrisch, zentriert, ruhend und rauschfrei. Gebrochen wird die Symmetrie nur
  durch Rundungsfehler. Nicht geprueft: elliptische Klumpen, Rauschen, Drehimpuls.
- **Vakuum mit Absorber**, kein Bad. Die Reflexion am Rahmen ist nicht gemessen, nur die Rahmenladung (max 5,2 % von
  Q0 bei iii).
- **"auf" heisst nur Q passt zu omega (Runde 21).** Fuer (iii) zeigt E/Q, dass die Ruhe spaeter kommt als das "auf".
- **Ladungsradius.** Gewaehlt ist die rms-Definition (= r_ladung, Plan). Mit "halb" oder "mittel" waeren die Klumpen
  breiter (s(i) 3,69 bzw. 3,47). Das ist nicht gerechnet.

**Selbstanzeigen:**
- **Vorzeichen:** psi_t = -i w0 psi statt "i w0 psi" der Karte, damit Q = +Q_F ist. Vorab im Plan begruendet; wegen der
  Ladungskonjugation physikalisch gleichwertig.
- **Ladungsradius:** Der Hinweis "Radiusgroesse, die der Klassifikator fuer R_F verwendet" war woertlich nicht
  umsetzbar. Der Klassifikator liest r_ladung nicht, und sein eigenes R_A ist fuer (i) unerreichbar. Geloest per
  Planregel, die Wahl rms ist auf 1,9e-7 bestaetigt.
- **Rauchlauf:** Er zeigte vor dem Einfrieren fruehe Ladungsverluste bis t = 60 (im Plan vermerkt). Vorhersagen und
  Regeln blieben unveraendert.
- **Spuren:** Im Plan standen Platzhalter "p4000x/y". Tatsaechlich lief Gruppe a (mit grob) auf p4000a und Gruppe b
  auf p4000b. zusammen wartete etwa 94 s auf den Lock von p4000a.
- **Dateien auf der .69:** py_compile hat runde22-bildung-1/__pycache__ angelegt (Vorgabe "-m py_compile").
  - torch.load gab eine FutureWarning (weights_only), ohne Wirkung; die Dateien sind eigene.
  - Die Zwischenspeicher (.pt, 2 x 37,8 MB echt, 37,8 + 18,9 MB Rauch) liegen nur auf der .69. Lokal sind
    lauf-69/zwischen/ und lauf-69/rauch-zwischen/ deshalb leer.
- **Scratchpad:** Die Hintergrundaufrufe des Werkzeugs legen dort automatisch Ausgabedateien an. Ich habe alle
  Ausgaben in lauf-69/ umgeleitet und selbst nichts dorthin geschrieben.
- **Sonst keine Abweichung vom eingefrorenen Plan.** kf5_geburt.py und kf_eich.py wurden nur importiert.

**Laufzeiten** (kleintest.sh, rc = 0 ueberall; Dienstlaufzeit):
- Rauch: 7,4 s, 6,4 s, 7,4 s.
- grob alle vier Faelle 0 bis 1000: 97,6 s (3,04 ms je Schritt bei B = 4, GPU 103 MB).
- fein, je B = 2 und 6,4 bis 7,4 ms je Schritt, GPU 234 MB:
  - a 0 bis 500: 183,1 s; a 500 bis 1000: 190,9 s.
  - b 0 bis 500: 174,5 s; b 500 bis 1000: 174,1 s.
- zusammen: 2,7 s. Summe der Rechenaufrufe etwa 845 s.

**sha256:**
- bildung1.py `0ef60ef1f8f1dd209808c5b1dbce044d8238f1f9ceedbe64405c2879f6a0ff64` (lokal = .69 = in allen Ergebnis-JSON)
- PLAN.md.eingefroren-20261002-191521 `b5a3f8b562e31521e7dfc71fa34b96b7aec6de383a44b7b88588b2489e9b3ba4`
- Importiert:
  - kf5_geburt.py `9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0`
  - familie_2d_m0.json `f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806`
  - kf_eich.py `332f3293a94448848beeb1c90a58ba9128d14e4f5029983832a8ea7a77eacb59`
  - torch 2.5.1+cu121, Quadro P4000
- lauf-69/ausgabe:
  - grob_alle_0-1000_ergebnis.json `247a429fd41b9dc49dc455ea0480678c5deed34f67bc80edd27c0b791ca765a3`
  - fein_a_0-500_ergebnis.json `0733969d5fda71cfa6c0e96c5fa90bfaf62b040c171ecfe3a76290a51eaead81`
  - fein_a_500-1000_ergebnis.json `d12094b2f6990cf4475943dc20105ff5c64e9941620d1836e994b265d88fdcc8`
  - fein_b_0-500_ergebnis.json `e71a37e0a451b2aac038ca8829723c4348bec33fce188ea3276d1fcf9c406c24`
  - fein_b_500-1000_ergebnis.json `cba7274fbdf26f0a2431d08cc9176320ce02ce93d995c4d2fe0fb8fb8b6e59a5`
  - zusammen.json `0521008aaaf5b1910f95c779e7cf403e33bcece8640b2a5da747100aa62776ee` (lokal = .69)
  - zusammen.txt `fa91557585f4f52c010d86131b82e3aeaf75b920f00c8a310d57e58a5efe8e69`
  - Berichte: grob `7dc91d9b24cb2e9ff6373bcecb04d5871be036516fdfeee9658e8b0d6ee2e15e`, fein_a_0-500
    `e438734653369f3a6eb8e8d0e07f22ef7b60d916daa0d84be300b956ed8b9ab2`, fein_a_500-1000
    `a02a85cbc439b112ee82c62a381b74880195816a6e4eb9e40b5e27cc4d7943fc`, fein_b_0-500
    `72d34cb26fa6b344104a5c5a462ea2a813bf62f97e4b4555d4ff2b0abbc2f1ae`, fein_b_500-1000
    `6406d5e81492f1fea13e570514c38cca6a071d1a5c8ea573ac585dbbaef487db`
- Zwischenspeicher (nur .69; sha256 im Abschnitt-1-JSON = im Abschnitt-2-JSON):
  - fein_a_t500.pt `f75e01989a90cb4be283022edbaae13b7681ed4ddd7134cf029a025645fe4405`
  - fein_b_t500.pt `b07b0c82465a968e1eb74cc4cd0dd877b1020c088eb031198d5e0046c3961511`
- Logs:
  - LAUF-grob `f692709295d648fd3b12e74f71596683ce31de9776eac8f0755b1ed9a0ab03de`
  - LAUF-fein-a1 `0861cd8a2efcab6bf9a3521ee556b6dbcfa6d7288f70246f448915bcecdb9c28`
  - LAUF-fein-a2 `928a055f0a3754780f0bc2426bd50d5b5e5d82e06c776c2815cc3c4c4e4e9229`
  - LAUF-fein-b1 `98114be651a8aa672178d6689beb5b059e4598a4b68f5b1ddde1c066aa19122d`
  - LAUF-fein-b2 `666d8ba02ce81e46cf6115fea0d11c4cda6c692794baa8809aecb0407ea226a5`
  - LAUF-zusammen `663e23b38d322525bed8c5abe04aa95b0a32f6707cd1657f62f1b152ae3d2e81`
  - RAUCH-grob `8dcd72a608eff830a299d7368868b14365322c91a641acb28541f819463f85a4`
  - RAUCH-fein `bcc1aec3476bb5c9a3bff41e17b8923e0d456c0d1de6c69c16b95ed01b9530e3`
- Rauch-JSON:
  - grob_alle_0-30 `42ffb9caa1c5d8caf587f32b5de2de1ede691a1fa4f5962d8593c79fe27515df`
  - grob_alle_30-60 `fa4fb30555185490ede0b35d25182bfff212d447fd6831bc025b840b77e84627`
  - fein_a_0-10 `7b7e718671f3281ecda6b580d12d005b9c29bc421d5a243feb0a4baa9e740a74`
- hilfs/tabelle.jq `03226aa8c3552dd9d9a9d9c7f35bc3b34bb38eeceebf4fa223d5bf9f0a9b1206` (nur Darstellung)

**Dateien:**
- Kartenordner: KARTE.md, PLAN.md (+ eingefrorene Fassung), bildung1.py, ERGEBNIS.md.
- hilfs/: tabelle.jq, tabelle-s0-0.1.md (48 Zeilen Zusatz), tabelle-s0-0.3.md (nur Verweis).
- lauf-69/ (Spiegel von /home/fmh/fmhc-physics-remote/runde22-bildung-1/lauf-69 ohne .pt): ausgabe/, rauch/, LAUF-*.log,
  RAUCH-*.log, LAUF-spur-a/b.zeiten.

## 6. Einfach gesagt

Wir haben drei Wolken mit genau der Ladung eines echten Q-Balls hingelegt: eine passend breite, eine zu breite und eine
zu schmale. Dann haben wir zugeschaut, ob sie von allein zu einem echten Q-Ball werden. Alle drei schaffen das, und zwar
schnell, in wenigen hundert Zeiteinheiten. Die passende Wolke verliert fast nichts, die breite knapp ein Zehntel. Die
schmale ist zu energiereich: Sie schleudert gut ein Drittel ihrer Ladung als Wellen weg und wird dann ein kleinerer,
aber echter Q-Ball. Ein einzelner Klumpen findet also von selbst zur Familie, zumindest in diesem einfachen,
symmetrischen Fall. Dass die Tropfen frueher nie ankamen, lag vermutlich eher am Verschmelzen und an ihrer Umgebung als
am Modell; das ist noch nicht geprueft.

Ende der Bearbeitung: 2026-10-02 19:29:03 CEST (date).
