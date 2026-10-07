# PLAN-NACHTRAG-1 (STILLE-ZWEIFELD) - NACHTRAEGLICH

- Geschrieben ab 11:07 CEST (date im Dateinamen der eingefrorenen Fassung), nach Sicht der Hauptzeilen und eines Teils
  der E2-Verfeinerung. Diagnose, keine Aenderung der Wertungsregeln.
- Anlass: Die Verfeinerung aller 74 E2-Gitterminima je Stufe passt nicht in die Zeitbox (Gauss-Newton ohne Daempfung
  stieg in mehreren Faellen an und wurde durch eine gedaempfte Fassung ersetzt; diese braucht 1 bis 2 min je Minimum).
- Zusatzpruefung E2: Auf der einzigen geschlossenen Kurve G_b = 0 (eine Nullstelle je Zeile) wird in jedem
  Zeilenintervall, in dem s_a und s_c beide das Vorzeichen wechseln, T ab dem Mittelpunkt der Kurve im Intervall
  gedaempft minimiert (gleiche Funktion gn_E2, Anker = naechste Zeile). Intervalle laut Zeilendaten Stufe 2:
  0,85-0,87; 0,89-0,91; 0,93-0,95; 1,21-1,23. Dazu der kleinste Wert des ungedaempften Laufs (0,8258 / 2,1076).
- Stufe 1; Stufe 2 nur, falls T < 100 tau_E2. Wertung "beide null" unveraendert (T < tau_E2 auf beiden Stufen, K3).
