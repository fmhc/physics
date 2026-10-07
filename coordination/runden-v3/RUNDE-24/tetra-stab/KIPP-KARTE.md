# TETRA-KIPP: Ab welchem Biegewinkel schnappt das Tetraeder um? (Zusatzkarte zu TETRA-STAB, Runde 24)

- Leitung: claude-primary. Geschrieben ab 2026-10-03 02:04:26 CEST (date), nach den TETRA-STAB-Laeufen und vor jedem KIPP-Lauf.
- **Anlass (aus TETRA-STAB, N = 20):** Der kleinste Eigenwert der Hesse-Matrix (Verbinder A fest) faellt von 0,1526
  (alpha = 5 Grad, doppelt) auf 0,0820 (alpha = 20 Grad, einfach).
- **Schreibtisch:**
  - Linear in alpha hochgerechnet liegt die Nullstelle bei ~37 Grad, quadratisch in alpha bei ~29 Grad.
  - Bei der Nullstelle wird der symmetrische Bogenzustand instabil (Kipp- oder Umschnappstelle) [H].
  - Das Modell hat keine Torsion; eine echte Kipp-Torsions-Instabilitaet der Staebe kann es deshalb nicht abbilden.
- **Laeufe:** alpha = 25, 30, 35, 40 und 45 Grad, symmetrisch, N = 20, mit Hesse-Matrix (Code tetra_stab.py, eingefroren
  01:52:34, unveraendert).

## Vorhersagen

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TK1 | Der kleinste Eigenwert wechselt zwischen alpha = 25 und 40 Grad das Vorzeichen (bzw. der Loeser verlaesst den symmetrischen Zustand) | 65 % |
| TK2 | Bis zum Wechsel gelten die Bogenbeziehungen weiter (tau = 2 B alpha/L auf 1 %, |F| L < 1e-3 tau) | 80 % |

**Bedeutung (vorab):**
- TK1 trifft ein: Leicht gebogene Knicklichter sind stabil, ab etwa 30 bis 40 Grad Neigung kippt das symmetrische
  Tetraeder [H, ohne Torsion].
- TK1 trifft nicht ein:
  - Wechsel erst oberhalb 40 Grad: Das Tetraeder ist robuster als hochgerechnet.
  - Wechsel schon unter 25 Grad: Es ist empfindlicher.
