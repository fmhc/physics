# G1-07 Herkunft (nicht an die Ernte geben)

- Operator: mutation (Operator-Agent "innen", Anthropic, Opus 5.5)
- Elter: Bio 4, Tod unter Q_min (pool.jsonl; Entscheidung "weiter (R7 R5F a)", danach R5F-a "parken")
- Befund des Elters:
  - 3D radial mit gleichmaessigem Abfluss: kein schlagartiger Tod; der Ball haelt bis 0,70 bis 0,83 Q_min
  - omega 1,007 > 1 kurz vor dem Ende (Phase); Aufloesung etwa 200 Zeiteinheiten, fast unabhaengig von gamma
  - Verzoegerung tau ~ gamma^(-0,15); R5F-a: kein Oszillon unter Q_min (nur radial); v_g-Dauerformel um mehr als Faktor 2
    verfehlt
- Geaenderte Annahme: **Dimension**, 3D radial -> 1D. Alles andere wie beim Elter: Potential U = S - S^2 + S^3/2,
  gleichmaessiger Abfluss -gamma psi_t mit gamma = 2e-3 / 1e-3 / 5e-4, Start omega^2 = 0,80, Stopp-Probe,
  t90/t50/t10 aus q_rel.
- Warum diese Mutation: In 1D fehlt die Mindestladung (die Familie reicht bis Q -> 0). Damit trennt der Test zwei
  Todesarten: am Faltpunkt Q_min (3D, gamma-unabhaengig) gegen den Adiabatik-Bruch (1D, Q_d ~ sqrt(gamma)). Die
  Mutation mit dem gemischten Ball der Gesamtformel (Vorschlag der Leitung in GEN-01.md) habe ich verworfen: Der
  symmetrische gemischte Ball ist exakt das beta_eff-Modell, sein Tod waere nur die bekannte Familie bei anderem beta
  (EVO-1-nah), und die Kopplungsachse nutzt schon G1-04.
- Quellen:
  - RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md, Idee 4
  - RUNDE-05.md; RUNDE-05/ERGEBNISSE-R5-AB.md (tod); RUNDE-05/r5a/PLAN.md (Abfluss, Q_erw, Klassen)
  - RUNDE-07.md (R5F-a); RUNDE-07/ERGEBNISSE-R7-A.md (R5F-a); RUNDE-07/r5f/PLAN.md, 3 (a) und 4 (a)
  - RUNDE-05/r5b/r5b.py (entwickeln mit gamma; 1D-Anker, Q(0,70) = 2,4415 laut pumpe)
  - Nicht doppeln geprueft: pool.jsonl (Bio 4, KF-3 Todesschwelle eps_c in 3D radial, Bio 48 Altern, Bio 45 Pumpe),
    RUNDE-07.md, RUNDE-09.md: keine 1D-Karte zum Tod unter Abfluss.
- Beginn (date): 2026-09-30 07:18:34 CEST (Beginn des Operator-Auftrags fuer alle vier Karten)
- Ende (date): 2026-09-30 07:41:22 CEST
