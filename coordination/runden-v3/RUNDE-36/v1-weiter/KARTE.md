# V-1-WEITER: Uebersteht die stille Wandfrequenz eine Aenderung bei kurzen Wellen (eps k^4)? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 23:51:15 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Idee B2 aus IDEEN-EVOLUTION/GEN-03.md (Eltern V-1 und STILLE-3D), Warteschlange Runde 36.
  - Bezug Papier I: Robustheit der stillen Stelle.
  - Bezug Finns Netzbild: Ein Gitter aendert die Dispersion bei kurzen Wellen, etwa -h^2 k^4/12 (QBALL-GITTER-1).
- **Vorlauf:**
  - WAND-BETA (RUNDE-24/wand-beta/): Die ebene Q-Ball-Wand hat bei jedem beta genau eine stille Frequenz rho_z (beta = 1:
    1,7734530718). Ausserhalb ist die Wand fast durchsichtig; der Einbruch ist sehr schmal.
  - STILLE-GITTER: Gitter brechen die Stille anisotrop ab h^4 (kubisch) bzw. h^8 (Dreieck).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Gleichung:** M1 in 1D (ebene Wand), mit Zusatzterm eps d^4/dx^4 in der Feldgleichung. Er gilt fuer Hintergrund und
  Schwankungen gleich (isotrope Aenderung der Dispersion).
  - Lineare Dispersion im Vakuum: omega^2 = 1 + k^2 + eps k^4 [M].
- **Kanalzaehlung** [M]: Fuer reelles omega und eps k^4 + k^2 - (omega^2 - 1) = 0 gibt es zwei Wurzeln k^2.
  - eps > 0 (Versteifung): eine laufende Wurzel (k^2 ~ omega^2 - 1) und eine abklingende (k^2 ~ -1/eps). Die Zahl der
    offenen Kanaele bleibt gleich.
  - eps < 0 (gitterartige Erweichung): auch die zweite Wurzel k^2 ~ 1/abs(eps) laeuft. Ein neuer offener Kanal bei hohem
    k entsteht.
- **Erwartung aus der Kanalzaehlung** [H]:
  - Eine stille Stelle in einem offenen Kanal ist eine Bedingung in einem Parameter (rho). Sie bleibt unter glatten
    Stoerungen bestehen und wandert nur. Fuer eps > 0 bleibt die Stille also exakt, mit rho_z(eps) - rho_z(0) ~ eps.
  - Fuer eps < 0 muss die Mode auch den neuen Kanal stillhalten, also zwei Bedingungen mit einem Parameter. Die Stille
    bricht. Die Restbreite sollte aber nur exponentiell klein sein, ~ exp(-c/sqrt(abs(eps))), weil die Wand glatt ist und
    k ~ 1/sqrt(abs(eps)) kaum ankoppelt.
- **Bedeutung fuer Finn [H]:** Ein Gitter (eps < 0) macht die Stille undicht, aber nur um einen Faktor, der mit feinerem
  Gitter extrem schnell verschwindet.

## Test (Code-Agent)

- **Code-Basis:** RUNDE-24/wand-beta/code/wand_beta.py (Wandprofil, Innen- und Aussenmoden, Kopplung c_in, Nullstelle).
  Ebenso die Nachproben in RUNDE-24/wand-beta/nach-69/ und das diskrete Schiessen dort.
- **Erweiterung auf 4. Ordnung:**
  - Hintergrund: ebene Wand bei omega_min, Randwertproblem 4. Ordnung.
  - Schwankungen: 4. Ordnung mit zwei zusaetzlichen Loesungen; Stabilisierung der abklingenden Anteile (Orthonormierung
    bzw. Riccati, wie bei PHASE-3D) offenlegen.
- **Werte:** beta = 1; eps = 0 (Kontrolle), +1e-3, +3e-3, +1e-2, -1e-3, -3e-3, -1e-2.
- **Gemessen:**
  - Lage rho_z(eps) der stillen Stelle: Nullstelle der Kopplung bzw. Minimum der Durchlaessigkeit, mit Aufloesung des
    sehr schmalen Einbruchs
  - kleinste Restgroesse dort
  - fuer eps < 0 die Restkopplung in den neuen Kanal
- Zwei Gitterweiten bzw. Toleranzen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| V0 | Kontrolle eps = 0: rho_z = 1,7734530718 (WAND-BETA) auf 1e-8 | 90 % |
| V1 | eps > 0: exakte stille Stelle bleibt (Restgroesse < 1e-10 relativ, beide Gitterweiten) fuer alle drei eps | 70 % |
| V2 | eps > 0: rho_z(eps) - rho_z(0) linear in eps (Verhaeltnis der Verschiebungen bei 3e-3 und 1e-3 zwischen 2,7 und 3,3) | 65 % |
| V3 | eps < 0: keine exakte Stille; Restkopplung in den neuen Kanal ungleich 0 und steigend mit abs(eps) | 60 % |
| V4 | eps < 0: Restkopplung faellt mit kleinerem abs(eps) schneller als jede Potenz (ln Rest ~ -c/sqrt(abs(eps))) | 45 % |

**Bedeutung (vorab):**
- V1 bis V3 treffen ein: Die stille Stelle ist robust gegen versteifende Aenderungen bei kurzen Wellen. Gitterartige
  Erweichung macht sie undicht, weil ein neuer Kanal aufgeht.
  - Fuer Papier I: Die Stille ist keine Feinabstimmung des Kontinuumsmodells, solange keine neuen Kanaele aufgehen.
  - Fuer Finns Netz: Ein Gitter macht die Stille nur winzig undicht.
- V1 verfehlt: Die Stille haengt an der genauen Dispersion; das schwaecht Papier I und muss offen gesagt werden.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (CPU- oder GPU-Skript; nicht cpu, cpu2, cpu3,
  cpu4, cpu5, cpu6, p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
