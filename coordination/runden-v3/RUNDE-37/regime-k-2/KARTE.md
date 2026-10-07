# REGIME-K-2: Laufen Schwerewellen in kovarianter 4D-Regge-Zeit auf Finns gefuelltem Netz V ohne Abstimmung richtungsgleich und stabil? (Runde 49, Fast Lane nach REGIME-K-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 12:47:03 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - REGIME-K-1 (RUNDE-37/regime-k-1/ERGEBNIS.md): Auf der B1-Kopie **ohne Fuellung** mit Zeltstangen ist die euklidische 4D-Regge-Wirkung langwellig genau die linearisierte Einstein-Wirkung (TT-Spanne extrapoliert 9,7e-10, konform/TT = -2). Die Anisotropie des Regimes H (6 bis 11 %) gehoerte aber zum **gefuellten** Netz V; ohne Fuellung war schon Regime H mit R1 isotrop (TT-ISO-1).
  - REGGE-4D-1 (RUNDE-36): Einsteins Form (1/4) k^2 (P2 - 2 P0) auf dem 4D-Kuhn-Gitter auf 0,04 %; fuenfte Nullmode (tote Hyperdiagonale).
  - REGGE-WELLE-1 (RUNDE-37): Wellen in echter Zeit ueber komplexes k_tau auf dem Kuhn-Gitter. Lange Schwerewellen laufen mit c (bei |k| = 0,05 v = 0,99979 bis 0,99986), genau zwei Polarisationen, keine Doppelbrechung, kein Anwachsen; Dispersion nach der Wuerfelgitter-Formel.
  - REGGE-4D-SCHIEF-1 (RUNDE-37): Im schiefen Netz verschwindet die tote Hyperdiagonale, aber die Diagonale wird eine Gittermode mit **negativer Steifigkeit** (-0,38 bei s = 0,1).
  - TT-ISO-1, SKALAR-MISCH-1, LUND-REGGE-MASSE-1: Regime H auf dem gefuellten V ohne Abstimmung 5,9 bis 10,6 %.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung, verkettet)

- **Kette [S Abstract + P]:** FFLR 1984 behaupten den Kontinuumslimes auf jedem Gitter. Auf Kuhn (REGGE-4D-1, REGGE-WELLE-1) und B1 ohne Fuellung (REGIME-K-1) hat sich das bestaetigt. Haelt es auch fuer das gefuellte V mal Zeit, ist die langwellige TT-Isotropie dort ohne Abstimmung zu erwarten.
- **Gegenzeichen [P]:** Das gefuellte V hat Oktaeder-Diagonalen. REGGE-4D-SCHIEF-1 zeigt, dass Diagonalen Gittermoden mit negativer Steifigkeit tragen koennen. V ist ausserdem nicht Delaunay (HODGE-L); fuer Regge spielt das keine Rolle, fuer die Gittermoden womoeglich schon.
- **Nicht ableitbar:**
  - ob die Kette auf dem gefuellten V gilt (Fuellung bzw. Diagonalwahl)
  - Zahl der Nullmoden (tote Kanten?)
  - Moden mit negativer Steifigkeit
  - laufende Moden und Geschwindigkeiten in echter Zeit
- **Kennzahlen-Abgleich:** Projekt-grep in den Rundentabellen (RUNDE-*.md) nach "4D", "Regge-Welle", "Zelt", "Kuhn", "gefuellt" vor dem Plan wiederholen; ein Ergebnis fuer das gefuellte V mal Zeit ist nach dem Stand der Leitung nicht bekannt.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RQ0 | Kontrolle [P]: Der Code gibt auf dem Kuhn-Gitter REGGE-WELLE-1 wieder (v bei |k| = 0,05 zwischen 0,9997 und 0,9999; zwei laufende Moden) und auf der B1-Kopie ohne Fuellung REGIME-K-1 (TT-Spanne extrapoliert < 1e-8) | 85 % |
| RQ1 | [S-Kette] Gefuelltes V mal Zeit, euklidisch: Die extrapolierte TT-Spanne ueber mindestens 50 Richtungen liegt unter 1e-6, und konform/TT = -2 auf 1e-4 | 60 % |
| RQ2 | [H] Gefuelltes V mal Zeit: genau 4 Nullmoden je Ecke der Grundzelle an jedem k ungleich 0 (keine tote Kante) | 55 % |
| RQ3 | [H] Gefuelltes V mal Zeit: keine Gittermode mit negativer Steifigkeit ausser der konformen Richtung (Vorzeichenzaehlung wie REGGE-4D-SCHIEF-1) | 45 % |
| RQ4 | [H] In echter Zeit (komplexes k_tau wie REGGE-WELLE-1): bei |k| = 0,05 in allen gerechneten Richtungen genau zwei laufende Moden mit v zwischen 0,999 und 1,001 | 50 % |

**Bedeutung (vorab):**
- **RQ1 und RQ4 treffen ein:** Im Regime K laufen lange Schwerewellen auch auf Finns gefuelltem Netz ohne Abstimmung richtungsgleich mit c. Die Richtungsabhaengigkeit des Regimes H ist dann eine Folge der gesetzten Bewegungsenergie, nicht des Netzes. Regime K wird der Hauptweg der Grundgleichung; GW170817 waere in der Isotropie ohne Abstimmung erfuellt (Gitterrest ~(kl)^2).
- **RQ1 verfehlt:** Die Fuellung bricht die FFLR-Kette; dann ist zu klaeren, welche Gitterbedingung fehlt.
- **RQ3 verfehlt:** Das gefuellte Netz hat in 4D eine instabile Gittermode (wie das schiefe Netz); Stabilitaet ist dann der naechste Engpass.
- **Ausdruecklich nicht gezeigt, auch wenn alles eintrifft:** Materie, Umklappen, nichtlineare Stabilitaet.

## Rahmen

- Code-Agent. Code aus RUNDE-37/regime-k-1/code/rk.py (Zeltstangen, euklidische Bloch-Hesse) und RUNDE-37/regge-welle-1/code (komplexes k_tau, laufende Moden) kopieren; Netz V (gefuellt) aus RUNDE-37/tt-iso-1/code. Dort nichts aendern.
- Die Fuellung (Oktaeder-Diagonalen) wie in TT-ISO-1 waehlen und im Plan begruenden; eine zweite Diagonalwahl als Kontrollarm, falls in 10 min machbar.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu2, cpu3 und cpu4. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
