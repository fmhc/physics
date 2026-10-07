# VERSCHRAENK-DIM-1: Gibt es ein Verschraenkungsmaximum ueber die Dimensionszahl? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 18:46:54 CEST (date), vor jeder
  Rechnung.
- **Finn (04.10., zwischen 18:33 und 18:36), woertlich:** "... gibts ein verschränkungsmaximum oder eine abklingende
  wahrscheinlichkeit oder uniformität in der dimensionsanzahl die berechnet wird? ..." (voller Wortlaut in
  RUNDE-37/dim-leiter-qball-1/KARTE.md).
- Kennzeichen: [M] Mathematik, [E] Rechnung, [L] Literatur, [H] Hypothese.

## Schreibtisch der Leitung [M, nicht gegengelesen]

- **Modell:** freies massives Skalarfeld (Masse m in Gittereinheiten) auf dem hyperkubischen Gitter Z^D,
  Grundzustand, Schnitt durch einen Halbraum (x_1 < 0 gegen x_1 >= 0).
- **Zerlegung:** Weil der Schnitt in den D-1 Querrichtungen verschiebungsgleich ist, zerfaellt das Problem in
  unabhaengige 1D-Ketten je Querimpuls k mit
  m_eff^2(k) = m^2 + Summe_(i=2..D) 4 sin^2(k_i/2).
  - Verschraenkung je Randplatz: S_D(m) = Mittel ueber k von S_1(m_eff(k)), wobei S_1 die Halbketten-Verschraenkung der
    1D-Kette ist [M; Standardzerlegung, L].
  - **Das ist eine zusammengesetzte Formel aus einem 1D-Term und D-1 gleichen Quertermen** (Finns Wunsch). Jeder
    Querterm hat Mittel 2 und Varianz 2. Fuer grosse D wird m_eff^2 also scharf um m^2 + 2(D-1): Gleichfoermigkeit.
- **Feste Punktzahl N** (Finns "groesseres System"): Wuerfel mit N = L^D Punkten, Halbschnitt mit L^(D-1) = N^((D-1)/D)
  Randplaetzen, also S_tot(D) = N^((D-1)/D) S_D(m).
  - Der erste Faktor waechst mit D, der zweite faellt. Grobe Schaetzung: Maximum bei D* ~ (ln N)/2 [M, grob].

## Ableitbarkeitsprobe

**Vorab ableitbar:**
- S_D faellt mit D, weil S_1 mit wachsender Masse faellt und m_eff mit D waechst. Das ist eine Kontrolle, kein Befund.
- D = 1, kleine Masse: S_1 ~ -(1/6) ln m (c = 1) [L].

**Nicht ableitbar:**
- Die genaue Kurve S_D(m) fuer D = 1 bis 12 (und 12 + n bis 24).
- Lage und Schaerfe des Maximums D*(N, m) von S_tot, und ob D* einem einfachen Gesetz in ln N folgt.

## Auftrag (Code-Agent)

1. **S_1(M):**
   - Halbketten-Verschraenkung der harmonischen Kette per Korrelationsmatrix (Peschel), Kettenlaenge >> 1/M.
   - Konvergenzprobe in der Laenge.
2. **S_D(m) fuer D = 1 bis 24 und m = 0,01, 0,1 und 1:**
   - Mittel ueber k als 1D-Integral ueber die Verteilung der Summe der Querterme (Faltung) oder Monte Carlo mit
     Fehlerangabe.
3. **Kontrolle der Zerlegung:**
   - direkte Rechnung auf einem kleinen 2D- und 3D-Gitter mit periodischen Querrichtungen
   - Abweichung zur Zerlegung < 1 %
4. **S_tot(D) = N^((D-1)/D) S_D(m):**
   - fuer N = 10^3, 10^6, 10^9, 10^12 und 10^80
   - Maximum D*(N, m)

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| VD0 | Kontrollen: Zerlegung gegen direkte 2D- und 3D-Rechnung < 1 %; D = 1 Steigung -1/6 gegen ln m auf 5 %; S_D faellt monoton mit D (ableitbar) | 85 % |
| VD1 | [H, Finns Einpendeln] Fuer N = 10^6 und m = 0,1 liegt das Maximum D* bei 3 oder 4 | 15 % |
| VD2 | [H] D*(N) waechst linear in ln N (Anpassung ueber die fuenf N auf 10 %) | 50 % |

**Bedeutung (vorab):**
- **VD1 trifft ein:** Bei realistischer Punktzahl und Masse liegt das Verschraenkungsmaximum bei 3 bis 4 Dimensionen
  [H].
- **VD1 verfehlt:** Das Maximum liegt woanders, vermutlich hoeher. Dann waehlt Verschraenkung allein keine 3 aus.
- **VD2:** Eine einfache Formel fuer die "beste" Dimension bei gegebener Punktzahl [H].

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu6 und cpu7 (frei, sobald ATEM-NETZ-1 sie nicht nutzt; sonst cpu
  und cpu2). Je Lauf <= 10 min, 1 Thread. Zeitbox 75 min.
