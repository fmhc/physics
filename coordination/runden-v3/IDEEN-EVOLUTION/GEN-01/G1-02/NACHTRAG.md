# G1-02 Nachtrag (nach dem Stempel 07:52:18, vor jedem echten Lauf)

- 2026-09-30 07:58:39 CEST, T-1: Die Plausibilitaetspruefung "q_durch + q_zurueck + q_frei = 1 +- 0,01" schlaegt per Konstruktion bei jedem
  Lauf der Klasse "haengt" an (Ladung in der Stufenzone zaehlt in keine der drei Groessen; Formprobe zeigte das).
  Der Code prueft wie die Karte; urteil meldet dann "kein Ausgang". Die Leitung entscheidet vor dem Lauf, ob das so
  bleibt. Nichts daran ist nach einem Ergebnis gelockert.
- Papiertest kann scheitern (V4 gegen Pi/(1 + Pi)); kein "L1 schwach".
- Formprobe: v_cl exakt 0,1030 / 0,2254 / 0,3108 / 0,4192 (Karte grob 0,105 / 0,23 / 0,32 / 0,44).
- 2026-09-30 08:06:14 CEST, Leitung (Entscheidung vor jedem echten Lauf, ohne Ergebnis): Die Summenregel bleibt, wie sie
  in der Karte steht und wie der Code sie prueft.
  - Grund: So lautet die Karte, und es ist der einfachste Weg.
  - Ein Lauf der Klasse "haengt" erscheint in der Tabelle sichtbar als Klasse; das Urteil lautet dann "kein Ausgang".
  - Eine Wiederholung mit laengerem T waere ein neuer Test (neue Karte), keine Rettung dieses Tests.
  - Kein Zusatz der Leitung zu den Messregeln.
