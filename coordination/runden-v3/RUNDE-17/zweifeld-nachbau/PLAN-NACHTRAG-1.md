# PLAN-NACHTRAG-1 (ZWEIFELD-NACHBAU) - NACHTRAEGLICH

- Verfasst 2026-10-02 12:00:04 CEST (date), nach L1 und dem Abbruch von L2, vor jedem weiteren Lauf.
- Anlass: L2 (profile M2) brach mit "Newton Stufe 2 w2=0.8420" ab. Stufe 1 und alle Zeilen 0,830 bis 0,840 auf
  Stufe 2 waren konvergiert. Ursache vermutlich: Die Abbruchschranke 1e-13 (relativ) des Hintergrund-Newton liegt auf
  Stufe 2 (20 000 Unbekannte) unter der Rundungsgrenze des Schritts.
- Aenderung (nur Abbruchregel des Hintergrund-Newton, kein anderes Verfahren):
  - weiterhin konvergiert bei Schritt < 1e-13 relativ;
  - zusaetzlich konvergiert an der Rauschgrenze: ab der 7. Iteration, Schritt < 1e-9 relativ und Schritt > 0,5 mal
    Vorschritt (keine Abnahme mehr).
  - Der letzte Schritt wird je Zeile als newton_schritt berichtet.
- L1 (profile M1) bleibt gueltig (alle Zeilen mit der strengen Schranke konvergiert). L2 wird wiederholt (L2b).
- Alle weiteren Laeufe nutzen den Code mit dieser Regel.
