# LEITER-BETA: Gibt es die stille Leiter in 3D auch bei beta = 1? (Runde 24, Fast Lane nach WAND-BETA)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 01:23:22 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - WAND-BETA (RUNDE-24/wand-beta/ERGEBNIS.md): Die ebene Wand hat bei beta = 1 genau eine stille Frequenz,
    rho_z(1) = 1,7734530718, mit k_in = 2,39943.
  - Daraus folgt der Duennwand-Abstand der Sprossen in 3D: b_inf(1) = 2 sqrt(beta) pi/k_in = 2,6186 in 1/eps, mit
    eps = omega^2 - 3/4.
  - Der Durchlaessigkeits-Einbruch der ebenen Wand ist bei beta = 1 nur ~1e-5 breit, bei beta = 1/2 deutlich breiter.
- **Offene Projektfrage:** RUNDE-10/nls-leiter/ERGEBNIS.md, Abschnitt 7: "Gibt es die Leiter im Klein-Gordon-Modell auch
  bei beta = 1 und 2?"
  - Ein aufgeloestes Rechteck bei beta = 1 (omega^2 0,808 bis 0,822, rho 1,805 bis 1,845) gab auf zwei Gitterstufen
    Umlauf 0.
- **Schreibtisch der Leitung [H]:**
  - Das Rechteck umfasst 1/eps von 13,9 bis 17,4, also 3,5 > b_inf(1) = 2,62. Es kann zwei Sprossen mit
    entgegengesetztem Umlauf (+1, -1) enthalten, deren Summe 0 ist.
  - Bei beta = 1/2 lagen die 3D-Sprossen bei (rho_n - rho_z)/eps ~ 1,10 bis 1,13, also oberhalb der ebenen Frequenz.
    Bei beta = 1 erwarte ich die Sprossen deshalb nahe rho ~ 1,7735 + c eps mit c ~ 1. Das liegt im Rechteck.
  - Wegen des schmalen Fano-Fensters braucht die rho-Abtastung nahe der Sprosse eine Aufloesung weit unter 1e-5. Siehe die
    Lehre aus RUNDE-12: Eine zu grobe rho-Abtastung verliert Sprossen.
- Projekt-grep (fuenfte Probe) nach "beta" in den Leiter-Runden:
  - RUNDE-07/bic2: Die erste Nullstelle wandert stetig mit beta in [0,40; 0,60].
  - RUNDE-08/gf-bic: beta_eff-Familie.
  - RUNDE-10: Rauchscan mit unzuverlaessigen Eck-Umlaeufen.
  - Radiale Sprossen bei beta = 1 sind nicht aufgeloest.

## Test

- 3D radial, l = 0, Modell U = S - S^2 + beta S^3 mit beta = 1. Code RUNDE-13/leiter3d-praez/bic2_3d_praez.py (Option
  --beta), Verfahren wie RUNDE-12/13: W-Abbildung, aufgeloeste Umlaeufe in Rechtecken, Vorzeichenwechsel, Kernwachstum.
- **Suchbereich:** eps in [0,03; 0,08] (1/eps 12,5 bis 33, erwartet etwa 7 bis 8 Sprossen); rho entlang
  1,7735 + c eps mit c in [0,5; 2].
  - Fein abtasten, mindestens so fein wie in RUNDE-12 fuer n >= 7 (4000 rho-Punkte), lokal um Kandidaten feiner.
  - Rechtecke um Einzelkandidaten so klein waehlen, dass sie nur eine Sprosse enthalten.
- **K0:** Derselbe Code reproduziert bei beta = 1/2 die 3D-Sprosse n = 10 aus RUNDE-13 (omega^2 = 0,5423644,
  rho = 1,57218) auf 1e-5 in omega^2 und 1e-4 in rho.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LB0 | K0 bestanden | 85 % |
| LB1 | Bei beta = 1 mindestens vier aufeinanderfolgende Sprossen mit aufgeloestem Umlauf +-1 (abwechselnd) in eps [0,03; 0,08] | 55 % |
| LB2 | Alle Schritte 1/eps_(n+1) - 1/eps_n der gefundenen Folge liegen in [2,45; 2,80], die letzten zwei innerhalb +-3 % von 2,6186 | 50 % |
| LB3 | Alle gefundenen rho_n liegen in (rho_z(1), rho_z(1) + 1,5 eps_n) | 60 % |

**Bedeutung (vorab):**
- LB1 und LB2 treffen ein: Die ebene Wandnullstelle sagt die radiale Leiter bei beta = 1 ohne Eichung voraus. Damit ist
  RUNDE-10s offene Frage beantwortet: Die Leiter gibt es auch bei beta = 1 [H, 3D, l = 0].
- LB1 trifft nicht ein: Im Bereich ist keine aufgeloeste Sprossenfolge gefunden.
  - Entweder gibt es sie radial nicht (die Kruemmung zerstoert sie), oder das schmale Fano-Fenster macht sie numerisch
    unzugaenglich.
  - Beschreiben, mit dem besten Hinweis, welches von beiden zutrifft.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min, 4 GB).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt, mit Parametern, die in keinem echten Lauf
  vorkommen.
- Zeitbox 120 min.
