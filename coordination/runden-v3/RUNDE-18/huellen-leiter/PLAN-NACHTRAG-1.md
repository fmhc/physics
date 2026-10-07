# PLAN-NACHTRAG-1 (HUELLEN-LEITER) - NACHTRAEGLICH

- Geschrieben ab 14:16 CEST (date), nach Laufbeginn, nach Sicht der ersten Zeilen bei grossem R (Stufe 2, Zeilen 168
  bis 182, R ~ 68 bis 75) und der Zeilen 50 bis 90 (Stufe 1). Ergebnisse der Stellensuche dort (Vorzeichen, Zahl der
  Stellen) waren noch nicht ausgewertet; gesehen hatte ich die Stellen der Paare 50 bis 73 (Stufe 1).
- Befund: Bei grossem R ist m_bc an den unteren inneren chi-Kurven sehr steil (|d m_bc/d rho| ~ 1e3 bis 4e3, Struktur
  schmaler als die Gitterzelle). Die zwei Newton-Schritte der Zeile (PLAN 3) laufen dort aus der Zelle (Merker
  "unsicher", Rest |m_bc| bis 0,89) oder lassen einen Rest > 1e-3. Dann sind rho und s der Nullstelle falsch, und die
  Unterzeilen erben einen falschen Startwert. Der Plan sah dafuer nur einen Merker vor; das wuerde ganze Kurvenstuecke
  aus der Zaehlung nehmen und die Abstaende (L4) verfaelschen.
- Aenderung (nur die Nullstellen-Verfeinerung; Messgroesse, Kriterien, Kurvenrang, Wertung unveraendert):
  1. Zeile: Ist eine Nullstelle "unsicher" oder ihr Rest |m_bc| > 1e-3, dann Illinois-Regula-falsi in der
     Gitterklammer (Vorzeichenwechsel auf dem Gitter), bis die Klammer < 1e-11 oder |m_bc| < 1e-12, hoechstens 30
     Schritte. s = m_ac am Endpunkt. Merker "unsicher" nur noch, wenn Illinois nicht konvergiert.
  2. Unterzeilen und Halbierung: Der Newton-Schritt gilt nur, wenn zusaetzlich |m_bc| am Startwert < 0,1 ist
     (Startwert im fast linearen Teil); sonst verworfen wie bisher.
  3. Rangsprung-Merker wie im Plan woertlich: Luecke nur zu den Nachbarkurven (der Code nahm auch den Abstand zur
     Schwelle; das gab falsche Merker an neu entstehenden Kurven). Umgesetzt in code/auswertung.py.
- Bereits gerechnete Zeilen ohne solche Nullstellen bleiben gueltig. Zeilen mit solchen Nullstellen werden neu
  gerechnet (alte Datei bleibt als alt-*.json), ebenso die beiden Paare daneben. Bloecke, die mit der alten Fassung
  gerechnet wurden, laufen am Ende noch einmal mit der neuen Fassung (nur die betroffenen Zeilen und Paare werden neu
  gerechnet).
- Gleiche Regel fuer beide Stufen.
