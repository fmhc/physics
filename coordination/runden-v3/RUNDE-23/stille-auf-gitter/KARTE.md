# STILLE-AUF-GITTER: Bleibt die stille Mode auf einem Gitter still? (Runde 23, Bruecke Raum -> Teilchen)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 22:33:01 CEST (date), vor jeder Rechnung.
- Herkunft: Finn, 22:2x: "ideate mal rum was wir weiter untersuchen sollten und was zu basic verbindung logik ->
  teilchenmodell wird". Einordnung in RUNDE-23/IDEEN-LOGIK-TEILCHEN.md, Glied R -> T.
  - Wenn der Raum aus diskreten Beziehungen besteht (Gitter, Graph), ist die exakte Stille unserer Moden dann nur eine
    Eigenschaft des Kontinuums?
  - Die Stille ist das Hauptergebnis des Papiers.
- **Schreibtisch-Vorhersage der Leitung [H]:**
  - Der Gitter-Laplace mit 5 Punkten ist Delta + (h^2/12)(d_x^4 + d_y^4) + O(h^4).
    - Wegen d_x^4 + d_y^4 = k^4 (3 + cos 4theta)/4 hat er einen Anteil (h^2/48) k^4 cos 4theta. Dieser koppelt l = 0 an
      l = 4.
    - An der (durch den isotropen Anteil verschobenen) Sprosse verschwindet die l = 0-Breite weiter, der l = 4-Kanal ist aber
      offen.
    - Die Kopplung ist proportional zu h^2, also bleibt eine Restbreite Gamma_min proportional zu h^4.
  - Der isotrope 9-Punkt-Stern hat die Gewichte 4/6 (Achse), 1/6 (Diagonale) und -20/6 (Mitte), geteilt durch h^2.
    - Er hebt cos 4theta in Ordnung h^2 auf (nachgerechnet: Summe der vierten Momente = 2 k^4, isotrop).
    - Die Anisotropie kommt erst mit h^4 (sechste Momente: 5/2 - (1/2) cos 4theta), also ist Gamma_min proportional zu h^8.
  - Regel [H]: Der Breiten-Exponent ist zweimal die Ordnung der niedrigsten Gitter-Anisotropie.
    - Je isotroper die oertliche Struktur, desto stiller das Teilchen.
    - In 3D sind die 12 Ikosaeder-Richtungen bis zur 5. Ordnung isotrop (Finns "12"); das ist nicht Teil dieses Tests.
- **Ableitbarkeitspruefung:**
  - Im Projekt gibt es keine Rechnung der 2D-Mode auf einem kartesischen Gitter. RUNDE-12/leiter2d-praez und
    RUNDE-22/bildung-leiter sind radial, und radiale Gitter erhalten die Drehsymmetrie exakt.
  - Die Exponenten folgen aus dem Schreibtisch-Argument. Offen bleiben der Vorfaktor, ob die Sprosse auf dem Gitter
    ueberhaupt bestehen bleibt, und ob die Verformung des Hintergrunds oder ein Rechenboden die Restbreite bestimmt.
- Explorativ (v3), Hypothesen [H]. Literatur erst nach den Laeufen [L?]:
  - symmetriegeschuetzte BICs und ihre Brechung, z. B. die Uebersicht von Hsu u. a. 2016
  - isotrope Laplace-Sterne, z. B. Patra und Karttunen 2006

## Test

- Modell M1 in 2D (U = S - S^2 + S^3/2, S = |phi|^2, Masse 1).
- Hintergrund: Q-Ball an der Sprosse n = 7. Kontinuum (RUNDE-12/leiter2d-praez/ERGEBNIS.md):
  - omega_r^2 = 0,529266, stille Mode rho ~ 1,556
  - |Im rho| ~ (57 Delta omega^2)^2 neben der Sprosse, Rechenboden dort 8,4e-7
- Quadratgitter mit Abstand h, zwei Sterne: A (5 Punkte) und B (isotroper 9-Punkt-Stern).
- Je (Stern, h):
  - Gitter-Q-Ball per Newton bei festem omega. Die A1-Symmetrie von C4v (Achtel-Gebiet) darf genutzt werden; l = 0 und
    l = 4 liegen beide in A1.
  - Linearisierung (zwei Komponenten), auslaufender Rand durch komplexe Koordinatenstreckung (PML). PML-Probe mit zwei
    Einstellungen.
  - Eigenwert nahe rho ~ 1,556 per Shift-Invert.
- omega^2-Abtastung um die verschobene Sprosse. Fit Gamma(omega^2) = Gamma_min + a (omega^2 - omega_r^2(h))^2 ergibt
  Gamma_min(h) und omega_r^2(h).
- h aus {0,5; 0,4; 0,3; 0,25; 0,2}. Der Plan darf 0,15 dazunehmen, wenn es billig ist.
- Fernfeld des Eigenvektors am Minimum: Anteil des auslaufenden Flusses in cos 4theta.
- K0 (Kontrolle):
  - Die Extrapolation h -> 0 trifft das radiale Kontinuum.
  - Der Rechenboden der Gitterrechnung wird dokumentiert (PML-Probe, Doppelrechnung).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SG0 | omega_r^2(h) = omega_r^2(0) + c h^2 fuer beide Sterne (Exponent 2 +- 0,4); Extrapolation innerhalb +-3e-5 um 0,529266 | 70 % |
| SG1 | Stern A: Gamma_min proportional zu h^p mit p = 4 +- 0,8, aus mindestens drei h ueber dem Rechenboden | 55 % |
| SG2 | Stern B: p = 8 +- 2, oder Gamma_min liegt fuer alle h <= 0,3 unter dem Rechenboden; und bei h = 0,3 gilt Gamma_min(B) < Gamma_min(A)/30 | 50 % |
| SG3 | Stern A: am Minimum liegen >= 80 % des abgestrahlten Flusses in cos 4theta (l = 4) | 60 % |

**Bedeutung (vorab):**
- SG1 und SG2 treffen ein (SG3 stuetzt):
  - Die Stille des Teilchens misst die Anisotropie des Raums. Der Breiten-Exponent ist zweimal die Anisotropie-Ordnung
    [H, 2D, M1].
  - Auf Gittern bleiben stille Moden "fast still", in einem genuegend isotropen diskreten Raum praktisch exakt.
- SG1 trifft nicht ein mit p ~ 2: Die Anisotropie geht linear in die Breite ein, etwa ueber die Verformung des
  Hintergrunds. Beschreiben.
- SG0 trifft nicht ein: Das Gitter veraendert die Leiter staerker als die h^2-Regel, die Sprosse koennte verschwinden.
  Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh:
  - CPU-Spuren cpu, cpu2, cpu3, cpu4, cpu6
  - je Lauf <= 10 min und <= 4 GB
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt, mit Parametern, die in keinem echten Lauf
  vorkommen.
- Zeitbox 120 min:
  - zuerst Stern A vollstaendig
  - dann Stern B
- Literatur nach den Laeufen (L4).
