# G2-04 Herkunft (nicht an die Ernte geben)

- Operator: mutation (Operator-Agent "innen", Anthropic, Opus 5.5)
- Elter: Wel 6 "Gleiten ueber der Rumpfgeschwindigkeit" (pool.jsonl; RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md,
  Idee 6; Entscheidung "weiter (Medium), nicht geerntet").
- Befund des Elters:
  - R5-C (Papier, RUNDE-05/r5c/PLAN.md Abschnitt 2): im Ein-Feld-Modell nicht umsetzbar (bei S < 2/3 instabiles Medium mit
    v_c = 0, bei S > 2/3 kein Ball); mit zweitem Feld chi (abstossend |chi|^4, Kopplung lam |psi|^2 |chi|^2) wohlgestellt.
  - M1 gleiten (RUNDE-06/ERGEBNISSE-R6-C.md, "M1-W6 gleiten"; Plan RUNDE-06/medium1d/PLAN.md 2.2): lam = 0,1, C0 = 0,1,
    mc2 = 1; groesste Kraft 1,33e-3 bei u = 0,30, F(0,9) = 4,6e-9 (unter F_MIN); V6a und V6b getroffen, V6c offen;
    Fallenbilanz ab u = 0,6 verletzt; Vorschlag "parken" (bekannte 1D-Hindernisphysik).
- Geaenderte Annahme: **Medium** (Masse der Mediumsquanten mc2 = 1 -> 0,25 und 0). Alles andere wie beim Elter:
  C0 = 0,1, g4 = 0,5, lam = 0,1, Ball omega^2 = 0,7, Falle, Lorentz-Stroemung, Box, Messfenster, Gitter.
- Warum diese Mutation:
  - Das Papierbild des Elters (Kraft ~ Formfaktor bei k') macht eine Vorhersage, die der Elter nicht pruefen konnte: Der
    Einbruch muss mit k' wandern, nicht mit u. mc2 aendert k'(u) stark (k'(0,9) = 4,31 / 2,40 / 1,23 fuer
    mc2 = 1 / 0,25 / 0), laesst Ball, Kopplung und Code aber gleich.
  - Der Test trennt drei Bilder (k', u allein, u/c_s) mit weit auseinanderliegenden Zahlen (u_10 bei mc2 = 0:
    0,90 / 0,53 / kein Einbruch).
  - Grundlagenbezug [H]: Ein masseloses |chi|^4-Kondensat hat c_s^2 = 1/3 exakt (Strahlungsgas).
- Verworfene Mutationen:
  - Dimension 1D -> 2D: Papier sagt klar voraus (in 2D erfuellt ein ganzes Band 0 < k < k* die Cherenkov-Bedingung, die
    Kraft faellt dann nur wie 1/u^2), aber die vorhandene 2D-Box (medium2d.py, 76,8 periodisch) laesst die Nachlaufwelle
    zurueckkehren; eine groessere Box oder Randschicht mit Stroemung ist mehr als 1 h Code. Nach der Lehre aus Generation 1
    (drei ungetestete Innen-Karten) nicht gewaehlt.
  - Duennwandball in 1D (Nullstellen des Formfaktors, "Buckel und Taeler" wie beim Schiffswellenwiderstand): In 1D waechst
    das Plateau nur wie ln(1/eps)/(2 sqrt 2), bei eps = 0,02 etwa 2; die Nullstellen laegen in einem Bereich, den die
    Einhuellende schon unterdrueckt. Zudem Parameter statt Annahme.
  - Austauschkopplung eps: treibt psi ueberall (gleichfoermige Quelle), kein sauberer Ball-im-Medium-Zustand.
- Quellen:
  - RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md (Ideen 5, 6, 11)
  - RUNDE-05/r5c/PLAN.md (Abschnitt 2); RUNDE-05.md (Zeile R5-C); RUNDE-05/ERGEBNISSE-R5-CD.md
  - RUNDE-06/medium1d/PLAN.md (1.1 bis 2.2, 2.5); RUNDE-06/ERGEBNISSE-R6-C.md (M1-W5, M1-W6, M1-W11, 3.2, Tabelle 5)
  - RUNDE-06/medium1d/medium1d.py (Funktionen om0, schall, k_stroemung, c_start, bogoliubov, kielwelle, lauf; gelesen)
  - RUNDE-07/IDEATION-UEBERSICHT.md, Zeile Wel 6
  - Nicht doppeln geprueft: pool.jsonl (Wel 5, 6, 7, 11, Bio 48 "masseloser Kanal" betrifft den Zerfall des Balls, nicht
    das Medium), RUNDE-07.md bis RUNDE-10.md: keine Karte zur Mediumsmasse.
- k'-Werte und u_10 von Hand gerechnet (Formel wie kielwelle()); Probe: k'(0,35) = 0,644 und k'(0,9) = 4,31 bei mc2 = 1
  wie im PLAN.
- Beginn (date): 2026-09-30 10:34:18 CEST (Beginn des Operator-Auftrags fuer alle vier Karten)
- Ende (date): 2026-09-30 10:56:31 CEST
