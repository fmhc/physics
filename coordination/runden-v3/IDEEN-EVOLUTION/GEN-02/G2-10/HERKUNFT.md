# G2-10 Herkunft (nicht an die Ernte geben)

- Operator: mutation (Operator-Agent "innen", Anthropic, Opus 5.5)
- Elter: 3D-RES (pool.jsonl), die stillen Atmungsstellen des 3D-Q-Balls, U = S - S^2 + beta S^3 (RUNDE-06/
  AUFTRAG-3D-RESONANZ.md; RUNDE-07.md bis RUNDE-09.md: BIC-2/3/4, SP-1, FORMEL-1 bis -3, MOD-2).
- Befund des Elters (Stand heute): eine Leiter von 15 Stellen bei beta = 0,5, blind vorhergesagt; dazu l = 1 und l = 2;
  Duennwandmodell (RUNDE-09/MODELL-DUENNWAND.md): Phasenbedingung k_c R_tw = pi (n + theta), Grenzschritt
  b_inf = 2 sqrt(beta) pi/k_inf (2,30; gemessen ~2,29 bis 2,305), wechselnde Umlaufzahl, C_n ~ (n + theta)^4; keine Stellen
  in 1D und im Log-Potential, weil die Innenbarriere fehlt.
- Geaenderte Annahme: **Dimension** d = 3 -> d = 2 (radial, l = 0). Alles andere wie beim Elter: dasselbe Potential
  (beta = 0,5), dieselbe Zwei-Kanal-Stoerung, dieselbe Suche (Breitenminima, signierte Wurzel).
- Warum diese Mutation (Hebel Innenbarriere, Hinweis der Leitung):
  - Das Duennwandmodell trennt, was von d abhaengt (Radius R ~ (d - 1)/eps, Phase der Innenwelle (3 - d) pi/4, Hoehe der
    Innenbarriere ueber S0) und was nicht (ebene Wand: Wandzustand, theta_inf, Niveauverschiebung). d = 2 prueft diese
    Trennung ohne freien Parameter: doppelter Schritt, Viertelphase, gleiche Wand.
  - d = 1 fehlt die Leiter (bekannt), d = 3 hat sie. d = 2 liegt dazwischen: Plateau waechst wie 1/eps (Duennwandgrenze
    existiert), aber S0 liegt bei gleichem omega tiefer. Die Barriere schneidet die Leiter oben ab (x_B(2D) < 0,878); das
    ist der scharfe, vorab festgelegte Teil V4.
  - MOD-1 nennt fuer die Dimensionsbruecke nur die topologische Hypothese (Nullstellenlinien in (d, omega^2) enden
    paarweise oder am Rand), keine Lagen.
- Verworfene Mutationen:
  - Randbedingung (reflektierende Kugelschale aussen): Eine echte stille Stelle ist aussen feldfrei, bleibt also bei jedem
    Schalenradius; der Test koennte kaum scheitern (L1 schwach).
  - Kopplung an ein Zwei-Feld-Medium: oeffnet einen masselosen Schallkanal; Restbreite ~ lam^2 waere erwartbar, braucht
    aber neuen radialen Zwei-Feld-Code (> 1 h).
  - Potential mit flachem Minimum von U/S (U = S(omega_c^2 + a (S - S_c)^4), dp_c = omega_c^2): wuerde die Barriere bei
    erhaltener Duennwand abschalten, ist aber auf Papier in 15 min nicht belastbar vorherzusagen (Wandzustand unbekannt).
- Nicht doppeln geprueft:
  - SP-1 (l > 0), SD-1 (Gegentakt), EVO-1 (Potentialfamilie beta, gamma), KREIN-1 (Krein-Signatur), MESS-1 (Troepfchen),
    MOD-2 (Duennwand n bis 15): alle in 3D oder in anderem Modell.
  - G1-10 (GEN-01, stille Atmung in H^3, geparkt): Kruemmung des Raums, nicht Dimension.
  - R6 Bruecke (RUNDE-06.md, V10): verfolgt einen Pol bei festem omega^2 = 0,7 von dim 1 bis 3; keine Leiter in 2D.
  - pool.jsonl: keine Karte zu stillen Stellen in 2D.
- Rechnung von Hand (Kontrolle der Methode): 3D, n = 3 bei gemessenem omega^2 = 0,631449 gibt Psi/pi = 3,7007 (MOD-1:
  3,7014). 2D-Lagen aus k_c(omega, omega + c(eps)) R_2D = pi (n + theta(eps) - 1/4) durch Einsetzen und lineare
  Interpolation: n = 2: 0,5971; n = 3: 0,5674; n = 4: 0,5515; n = 5: 0,5417 (Probe bei eps = 0,0417: n_eff = 4,997).
  n = 1: ~0,671.
- Quellen:
  - RUNDE-09/MODELL-DUENNWAND.md (ganz gelesen; M.2 bis M.7, Tabellen)
  - RUNDE-06/AUFTRAG-3D-RESONANZ.md (Kopf); RUNDE-06.md und RUNDE-06/ERGEBNISSE-R6-B.md (Bruecke, per grep)
  - RUNDE-09.md (MESS-1, SD-1, FORMEL, MOD-2 per grep); RUNDE-10.md (KREIN-1, EVO-1 per grep)
  - RUNDE-07/bic2/bic2_v2.py (Kopf: dim-Parameter, nu = l + (dim - 1)/2, profil(w2, dim, beta, ...), bruecke; per grep)
- Beginn (date): 2026-09-30 10:34:18 CEST (Beginn des Operator-Auftrags fuer alle vier Karten)
- Ende (date): 2026-09-30 10:58:47 CEST
- **Berichtigung vor jeder Vorhersagezeile (2026-09-30 11:02:48 CEST, date; Operator beim Gegenlesen):** Die Regel fuer
  x_B(2D) brauchte "Re rho vom verfolgten Pol" und widersprach damit "vor der Polsuche". Jetzt nur aus den Profilen:
  dp(S(r = 0)) > c(eps)^2 mit c(eps) = 0,826 + 0,24 eps aus der 3D-Leiter.
