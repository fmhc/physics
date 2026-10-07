# REGIME-K-1: Ist die linearisierte 4D-Regge-Wirkung auf Finns Netz mit Zeltstangen fuer lange Wellen richtungsunabhaengig, ohne Abstimmung? (Runde 48, ausgeloest durch LUND-REGGE-MASSE-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 11:40:07 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - LUND-REGGE-MASSE-1 (RUNDE-48): Im Regime H (stetige Zeit, gesetzte Bewegungsenergie) gibt keine gerechnete Paarung ohne Abstimmung zugleich isotrope und stabile Schwerewellen. Die vorab festgelegte Folge "Regime K (kovariante 4D-Zeit)" ist ausgeloest.
  - GRUNDGLEICHUNG-SKIZZE-v2, Abschnitt 2.3, Ausweg (ii): In Regime K wird keine Bewegungsenergie gesetzt; sie folgt aus der 4D-Regge-Wirkung.
- **Projektbefunde [P]:**
  - PACHNER-TAKT-1 (RUNDE-42; Code RUNDE-37/pachner-takt-1/code/pt.py):
    - Euklidisches linearisiertes 4D-Regge nach Hoehn auf einer B1-Kopie (fcc-Stabnetz, Oktaeder mit Diagonale) mit Zeltstangen (Takt je Ecke).
    - Flach auf 1,8e-15, alle 4-Volumen positiv.
    - Durch einen Takt propagieren E - G Groessen (3 je Zelle plus 4 global).
    - Eine Dispersion bzw. Isotropie ist dort nicht gerechnet.
  - REGGE-KINETIK-L:
    - Feinberg/Friedberg/Lee/Ren 1984: Kontinuumslimes auf "any lattice, regular or irregular", Korrekturen in l^2, mit dem Graviton-Propagator als Beispiel [S Abstract].
    - Christiansen 2011: Eigenpaarkonvergenz des statischen linearisierten Regge-Operators auf quasi-uniformen Netzen (Satz 4.7) [S].
  - TT-ISO-1, SKALAR-MISCH-1, HODGE-MASSE-1, LUND-REGGE-MASSE-1: Im Regime H ist die TT-Spanne auf V ohne Abstimmung 6 bis 11 %.
- Kennzeichen: [M], [E], [P], [S], [L], [H], [ES].

## Ableitbarkeitsprobe (Leitung, verkettet)

- **Kette [S Abstract + M]:**
  - Haelt FFLR auch fuer unser Gitter, naehert sich die linearisierte Regge-Wirkung fuer kl -> 0 der linearisierten Einstein-Hilbert-Wirkung (Fierz-Pauli) zur Hintergrundmetrik, die die Kantenlaengen festlegen.
  - Diese ist bezueglich der Hintergrundmetrik rotationsinvariant.
  - **Folge:** Der O(k^2)-Teil ist richtungsunabhaengig ohne Abstimmung; Richtungsabhaengigkeit erst ab O((kl)^2) relativ.
  - Auf LIGO-Wellenlaengen mit l ~ Planck-Laenge waere das (kl)^2 ~ 1e-76, also fuer GW170817 bedeutungslos.
- **Bedingungen der Kette (nicht ableitbar):**
  - ob unser Zeltstangen-Gitter (V bzw. B1 mal Zeit) ein Gitter im Sinn von FFLR ist (Abstract, nicht Volltext)
  - Groesse des (kl)^2-Koeffizienten
  - Rolle der Zeltstangenhoehe (Lapse): Geht sie nur ueber die Hintergrundmetrik ein (effektiver Lichtkegel)?
- **Euklidisch statt Lorentz [M]:** Die Karte rechnet die euklidische Bloch-Hesse-Matrix in allen vier Richtungen. Rotationsinvarianz im Euklidischen heisst nach Wick-Drehung Lorentz-Invarianz des Kontinuumsteils. Die echte Zeitentwicklung (Lorentz-Signatur, Stabilitaet) ist **nicht** Teil dieser Karte.
- **Kennzahlen-Abgleich:** Im Projekt ist keine Bloch-Dispersion einer 4D-Regge-Wirkung gerechnet (grep nach "Fierz", "Bloch" in pachner-takt-1 und regge-kinetik-l ohne Treffer zur Sache; vom Agenten vor dem Plan zu wiederholen).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RK0 | Kontrolle [M, P]: Das periodische 4D-Zeltstangen-Gitter ist flach (Innen-Fehlwinkel <= 1e-12). Die Bloch-Hesse-Matrix H(k) hat an jedem gerechneten k ungleich 0 genau 4 Nullmoden je Ecke der Grundzelle (Eckverschiebungen in 4D) | 85 % |
| RK1 | [S-Kette] Fuer kl -> 0 naehert sich der Nicht-Null-Teil von H(k) dem Fierz-Pauli-Symbol der Hintergrundmetrik: Die auf k^2 normierten physikalischen (TT-)Eigenwerte haben ueber mindestens 50 Richtungen in 4D eine Spanne, die extrapoliert unter 1e-6 liegt | 75 % |
| RK2 | [H] Die fuehrende Richtungsabhaengigkeit ist O((kl)^2): Die Spanne waechst zwischen kl = 0,05 und 0,2 mit einem Exponenten 1,8 bis 2,2 | 60 % |
| RK3 | [H] Die Zeltstangenhoehe wirkt nur ueber die Hintergrundmetrik: Wird sie um den Faktor 1,5 geaendert, bleibt die extrapolierte raeumliche Spanne unter 1e-6, und das Verhaeltnis der zeitlichen zur raeumlichen Steifigkeit folgt der Metrik auf 1e-6 | 65 % |

**Bedeutung (vorab):**
- **RK1 trifft ein:** Im Regime K sind lange Schwerewellen auf Finns Netz ohne Abstimmung richtungsgleich. Das Isotropie-Problem des Regimes H ist dann eine Folge der gesetzten Bewegungsenergie, nicht des Netzes. Regime K wird der Hauptweg der Grundgleichung.
  - Licht auf demselben 4D-Gitter saehe dieselbe Hintergrundmetrik. c_T = c waere dann eine Folge, keine Abstimmung [L-Kette, ungeprueft].
- **RK1 verfehlt:** FFLR gilt fuer unser Gitter nicht, oder die Zeltstangen brechen die Isotropie. Dann ist zu klaeren, welche Gitterbedingung fehlt.
- **RK3 verfehlt:** Der Takt (Zeltstangenhoehe) ist mehr als eine Eichwahl. Das waere fuer Finns Takt-Bild wichtig.
- **Ausdruecklich nicht gezeigt, auch wenn alles eintrifft:** Lorentz-Zeitentwicklung, Stabilitaet, Kausalitaet, Umklappen.

## Rahmen

- Code-Agent. Code aus RUNDE-37/pachner-takt-1/code (pt.py: Geometrie, Fehlwinkel, Hesse) kopieren, dort nichts aendern.
- Periodisches 4D-Gitter: raeumlich V (bzw. die B1-Kopie aus PACHNER-TAKT-1, im Plan begruenden), zeitlich periodisch mit Zeltstangen. Bloch-Phasen in allen vier Richtungen.
- Zerlegung von H(k) in Eich-, Spur- und TT-Anteil gegen das Fierz-Pauli-Symbol im Plan festlegen; Normierung und Richtungsraster (mindestens 50 Richtungen in 4D) vorab.
- Lesen, falls erreichbar: Volltext FFLR 1984 (NPB 245, 343) und Rocek/Williams (linearisiertes Regge auf dem Wuerfelgitter) [L]; nur als Hintergrund, kein Urteil haengt daran.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu2, cpu3 und cpu4. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
