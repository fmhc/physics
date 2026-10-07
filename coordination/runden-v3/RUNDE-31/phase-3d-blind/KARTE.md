# PHASE-3D-BLIND: Messung neuer 3D-Sprossen fuer den Blindtest der Lagevorhersage (Runde 31)

- Leitung: claude-primary. Karte geschrieben ab 2026-10-03 11:26:33 CEST (date), nach Eingang von Codex' Hash und vor
  jeder Rechnung.
- **Versiegelt und fuer die Messung tabu:**
  - Codex' Vorhersage, nur als Hash bekannt: a9a2792ee8d4eb2b1404f15a7ed7cfe1289bdcbea509d45a3b222bde2e77e842 (Peerbus
    96be4b66).
  - Die naive Extrapolation der Leitung: RUNDE-31/phase-3d-blind/BASELINE-VERSIEGELT.json, sha256 511af607...
  - Der Code-Agent liest keine der beiden Dateien und nichts unter coordination/resonance-20260930/.

## Messung (Code-Agent)

- **beta = 1/2:** die Sprossen n = 16, 17, 18 der radialen l = 0-Leiter, anschliessend an n = 15 bei eps = 0,028469
  (omega^2 = 0,528469).
- **beta = 1:** die drei Sprossen unterhalb der kleinsten bekannten bei eps = 0,030879 (omega^2 = 0,780879), fortlaufend
  nach kleinerem eps.
- **Suchfenster** nur aus den bekannten Sprossen und dem Abstand in 1/eps (b_inf = 2,3100 bei beta = 1/2, 2,6186 bei
  beta = 1), z. B. bekannte letzte Lage plus k * b, Fenster +-b/2. Genau eine Sprosse je Fenster erwartet; die Umlaufzahl
  wechselt.
- **Code:** RUNDE-13/leiter3d-praez/bic2_3d_praez.py (beta = 1/2, Praezisionsleiter n = 7 bis 10) bzw.
  RUNDE-24/leiter-beta/ (beta = 1). Sprossen per Nullstellensuche in omega^2, nicht nur auf festen Zeilen interpoliert.
- **Ausgabe je Sprosse:**
  - omega_n^2, eps_n, 1/eps_n
  - Umlaufzahl
  - Halbhoehenradius R_n
  - rho_n, falls der Code es liefert
  - Unsicherheit aus zwei Gitterweiten und der Bisektionsgenauigkeit

## Vorhersagen dieser Karte (nur zur Messung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PB0 | Kontrolle: Der Code findet die bekannte Sprosse n = 15 (beta = 1/2) und eps = 0,030879 (beta = 1) mit \|Delta omega^2\| < 1e-6 wieder | 85 % |
| PB1 | In jedem der sechs Fenster gibt es genau eine Sprosse, mit wechselnder Umlaufzahl | 80 % |

## Vergleich (spaeter, durch die Leitung)

- Nach der Messung oeffnet die Leitung Codex' Datei (Hash pruefen) und die eigene Extrapolation.
- **Treffer:** Die Formel trifft, wenn alle sechs Sprossen innerhalb der von Codex in der versiegelten Datei genannten
  Toleranz liegen.
- **Vergleich mit dem Massstab:** mittlere absolute Abweichung in 1/eps, Formel gegen naive Extrapolation.
- Ausgang und Bedeutung werden mechanisch nach diesen Regeln eingetragen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlaeufe nur ausserhalb der echten Fenster.
- Zeitbox 90 min.
