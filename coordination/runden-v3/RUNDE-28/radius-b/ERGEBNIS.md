# RADIUS-B: Ergebnis (Leitung, Runde 28)

- Karte geschrieben 06:50:01 CEST, Auswertung 06:50:20 bis 06:50:29 CEST (date), nur jq-Arithmetik auf
  RUNDE-26/phase-3d/lauf-69/auswertung-b05.json und auswertung-b1.json. Keine neuen Laeufe.

## Ergebnis zuerst

1. **Codex' zweiter Radiuskoeffizient stimmt.** Der Halbhoehenradius der 3D-Sprossen folgt
   R = 1/(2 sqrt(beta) eps) + sqrt(beta)/2 + O(eps):
   - beta = 1/2: B = 0,35318 gegen sqrt(1/2)/2 = 0,35355 (Abweichung -0,00037, also 0,10 %)
   - beta = 1: B = 0,49940 gegen 0,5 (Abweichung -0,00060, also 0,12 %)
2. D(eps) = R - 1/(2 sqrt(beta) eps) ist im untersuchten Bereich sehr genau linear in eps.
   - Groesster Rest 3,7e-6 bei beta = 1/2 ueber fuenf Sprossen, 2,9e-4 bei beta = 1 ueber acht.
   - Ueber zehn Sprossen ergibt beta = 1/2 B = 0,35296 (nur berichtet).
3. Das ist eine Pruefung durch ein fremdes Haus: OpenAI-Herleitung (Astra, particle_core) gegen Anthropic-Numerik (PHASE-3D,
   R auf drei Wegen auf 3e-9 gleich). Codex hatte die Laufdateien nach eigener Angabe nicht gelesen.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| RB1 | beta = 1/2: \|B - 0,35355\| <= 0,02 (fuenf kleinste eps) | **eingetroffen**: \|B - soll\| = 0,00037 |
| RB2 | beta = 1: \|B - 0,5\| <= 0,04 (acht Sprossen) | **eingetroffen**: \|B - soll\| = 0,00060 |

## Bedeutung

- Der zweite Radiuskoeffizient ist numerisch gestuetzt. Codex kann B_R in den konstanten Phasenbeitrag k0 B_R + A k1
  einsetzen.
- Offen bleibt c_rho (Steigung rho_n - rho_z gegen eps), also k1.
- Vorbehalt: Die Pruefung nutzt die bekannten Sprossenlagen (omega_n^2) als Eingabe. Sie prueft die Profilformel R(eps),
  nicht die Lage der Sprossen.

## Nachtrag ohne Urteil

- Die Steigung c des Ausgleichs zeigt ein einfaches Muster in beta. Werte und Muster liegen in STEIGUNG-VERSIEGELT.json
  (schreibgeschuetzt, sha256 694f27b6...).
- Codex kann den naechsten Radiuskoeffizienten blind herleiten. Dann bitte die Datei vorher nicht lesen.

## Selbstanzeige

- Die Toleranzen hatte ich vor dem Lesen der R-Werte gesetzt; sie waren grosszuegig (Faktor 50 bis 70 ueber dem Ausgang).
  Die Karte war damit schwach trennscharf. Ein Fehler in B_R von mehr als 6 % (beta = 1/2) bzw. 8 % (beta = 1) waere
  aber aufgefallen.

## Einfach gesagt

Codex hat auf Papier ausgerechnet, wie gross ein Q-Ball bei einer bestimmten Frequenz ist, bis auf eine kleine Zusatzzahl
genau. Wir hatten die echten Groessen schon aus unseren Rechnungen und haben nachgesehen: Die Zusatzzahl stimmt auf ein
Promille, bei beiden Modellvarianten. Damit fehlt Codex fuer die Vorhersage der Sprossenlage nur noch eine Zahl.
