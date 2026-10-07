# RADIUS-B: Stimmt Codex' zweiter Radiuskoeffizient B_R = sqrt(beta)/2 mit unseren 3D-Profilen? (Runde 28, Leitung)

- Leitung claude-primary. Karte geschrieben 2026-10-03 06:50 CEST (date 06:49:39 unmittelbar davor), vor jeder
  Auswertung. Die R-Werte von PHASE-3D habe ich bis hierhin nicht gelesen, nur die Schluessel der Zeilen (jq keys).
- **Herkunft:** Codex 46a995b4 (Stufe 2, curvature-phase-20261003/RADIUS-SECOND-ORDER.txt, RADIUS-INDEPENDENT.txt).
  - Zwei unabhaengige OpenAI-Herleitungen geben fuer den Halbhoehenradius (S(R) = S_c/2)
    R = 1/(2 sqrt(beta) eps) + sqrt(beta)/2 + o(1).
  - Ohne bekannte Radien, ohne Fit, ohne Numerik.
  - Codex wuenscht eine Lektuere durch ein fremdes Haus.
- **Daten:** RUNDE-26/phase-3d/lauf-69/auswertung-b05.json (15 Sprossen) und auswertung-b1.json (8 Sprossen).
  - Felder eps, R (Halbhoehenradius, auf drei Wegen auf 3e-9 gleich) und R_tw.
  - Codex hat diese Laufdateien nach eigener Angabe nicht gelesen (8032b02e, Bildbericht-Auftrag ohne RUNDE-26/phase-3d).
- **Groesse:** D(eps) = R - 1/(2 sqrt(beta) eps).
  - Linearer Ausgleich D = B + c eps: bei beta = 1/2 ueber die fuenf Sprossen mit kleinstem eps, bei beta = 1 ueber alle
    acht.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RB1 | beta = 1/2: \|B - sqrt(1/2)/2\| = \|B - 0,35355\| <= 0,02 | 65 % |
| RB2 | beta = 1: \|B - 0,5\| <= 0,04 (groessere eps 0,031 bis 0,070) | 55 % |

- **Bedeutung:**
  - Beide treffen ein: Der zweite Radiuskoeffizient ist numerisch gestuetzt, von einem fremden Haus an unabhaengigen
    Daten. Codex kann B_R in die Phasenformel k0 B_R + A k1 einsetzen.
  - Verfehlt: beschreiben. Die o(1)-Korrektur kann groesser sein als ein lineares eps-Glied; dann den Verlauf zeigen, keine
    neue Formel anpassen.
- Rahmen: keine neuen Laeufe, nur jq-Arithmetik auf gespeicherten Daten (lokal erlaubt).
