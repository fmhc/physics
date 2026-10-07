# TT-GRUND-1: Gibt es eine natuerliche Massenregel fuer die Tetraederarten, die die Schwerewellen auf Finns gefuelltem Netz von selbst isotrop macht? (Runde 44, Fast Lane)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 22:44:39 CEST (date), vor jeder Rechnung.
- **Herkunft:** TT-ISO-1 (RUNDE-37/tt-iso-1/ERGEBNIS.md; Ernte RUNDE-44.md).
  - In A1R1 (Netz V) sinkt die TT-Spanne von 6,34 % (alle J = 1) auf 1,1e-5 bei Kegel-Tetraedern J = 0,090 und Sechseck-Tetraedern J = 1,00, relativ zu Finns Tetraedern.
  - J gewichtet den Hamilton-Term, ist also eine inverse Masse; die Kegel sind etwa elfmal so traege.
  - Die Steifigkeit ist schon isotrop; die Anisotropie sitzt in der effektiven Masse.
  - Bedeutung dort: "Das ist eine Abstimmung; fuer 1e-15 muesste sie extrem genau sitzen oder einen Grund haben."
- **Weiche an Finn (offen):** Kristall (regelmaessig, mit Grund fuer die Abstimmung) oder Glas (zufaellig, im Mittel isotrop)? Diese Karte prueft den Grund.
- Kennzeichen: [M], [E], [P], [H].

## Ableitbarkeitsprobe (vor der Karte)

- **Projektsuche:** Die Volumina stehen in eine-welt-loch-1/PLAN.md Z. 43: Finn 4/768, Kegel 5/768, Sechseck 3/768 (V).
  - Die volumengewichtete Variante A2 (J_t = V_Finn/V_t, also Kegel 4/5 und Sechseck 4/3) ist im EINE-WELT-LOCH-1-Nachtrag gerechnet und anisotrop (GAMMA-NETZ-L: 3,2 bis 10,6 % ueber die Varianten). Regel N2 unten ist also bekannt und dient als Kontrolle.
- **Schreibtisch der Leitung [M, ungeprueft]:** Kein einfaches Potenzgesetz der Volumina trifft 0,090. Das Volumenverhaeltnis Kegel/Finn ist 1,25, und 1,25^p = 1/0,090 verlangt p ~ 10,8.
- **Nicht ableitbar:**
  - die Form der isotropen Menge in der symmetrischen Ebene (J_Kegel, J_Sechseck): Punkt, Kurve oder Gebiet
  - die Spanne an den Regeln N3 bis N6

## Auftrag (Code-Agent)

1. Code aus tt-iso-1/code kopieren, dort nichts aendern. Paarung A1R1, Netz V; S beschreibend.
2. **Karte der Spanne** in der symmetrischen Ebene: log10 J_Kegel und log10 J_Sechseck je in [-2, 2], Raster im Plan festgelegt. Dazu der Verlauf der Menge mit Spanne < 1e-4: Punkt, Kurve oder Gebiet?
3. **Natuerliche Regeln** (vor der Rechnung festgelegt; J = 1/Masse, Finn-Tetraeder = 1):
   - N1: alle gleich (J = 1). Kontrolle 6,34 %.
   - N2: Masse proportional zum Volumen, also J_Kegel = 4/5 und J_Sechseck = 4/3. Bekannt, Kontrolle.
   - N3: Masse proportional zu 1/Volumen, also J_Kegel = 5/4 und J_Sechseck = 3/4.
   - N4: Masse proportional zum Volumen^2, also J_Kegel = 16/25 und J_Sechseck = 16/9.
   - N5: Masse proportional zur Zahl der Ecken, die auf Finns Netz liegen.
     - Im Plan aus der Geometrie abzaehlen: Finn 4; Kegel (C plus 3 Netzecken) 3; Sechseck-Tetraeder (C, H und 2 Netzecken) 2.
     - Also J = 4/n.
   - N6: Masse proportional zum Traegheitsmoment des Tetraeders um seinen Schwerpunkt bei gleicher Dichte. Im Plan aus den Koordinaten des Codes berechnet.
4. **Messgroesse:** TT-Spanne max/min - 1 wie in TT-ISO-1 (13 Richtungen, |k| = 1e-3 und 2e-3). Stabilitaet an den 511 k fuer jede Regel und fuer den besten Punkt.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TG0 | Kontrolle: N1 gibt 6,34 % und der TT-ISO-1-Punkt (0,090; 1,00) <= 2e-5, je auf 1e-3 relativ bzw. absolut | 90 % |
| TG1 | [H] Die Menge mit Spanne < 1e-4 ist in der symmetrischen Ebene eine Kurve, kein einzelner Punkt und kein Gebiet | 65 % |
| TG2 | [H] Keine der Regeln N2 bis N6 liegt unter 0,1 % Spanne | 75 % |

**Bedeutung (vorab):**
- **TG2 trifft ein:** Fuer das isotrope Massenverhaeltnis gibt es keinen der naheliegenden Gruende. Es bleibt eine Abstimmung, und die Kristall-Lesart braucht einen neuen Grund [H].
- **TG2 verfehlt:** Eine natuerliche Massenregel macht die Schwerewellen von selbst (fast) isotrop. Das waere ein starkes Argument fuer die Kristall-Lesart; danach muesste man pruefen, wie genau.
- **TG1 trifft ein:** Es gibt eine Ein-Parameter-Schar isotroper Massen; ein Grund muesste nur eine Bedingung erfuellen.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu10.
  - cpu3, cpu4 und p4000a nutzt claude-video, cpu2 haelt Codex.
- Je Lauf hoechstens 10 min, 1 Thread. Zeitbox 60 min.
