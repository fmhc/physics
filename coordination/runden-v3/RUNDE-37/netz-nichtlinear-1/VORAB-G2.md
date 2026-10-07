# VORAB-G2: Voll nichtlineare Dynamik (Teil G2)

- **Begründung der Wahl (Nachführung in 1. Ordnung):**
  M_eff und B kontinuierlich exakt nachzuführen, würde pro Zeitschritt ca. 4,5 s dauern (14 Stunden für 10 Perioden). Führt man sie nur alle n Schritte sprungartig nach (stückweise konstant), entstehen exakt die in Teil B bewiesenen Energiesprünge beim Umschalten (virtuelle Arbeit), was die geforderte Energieerhaltung von 1e-8 zunichtemacht. 
  Daher wird M_eff in **erster Ordnung der Dehnung** nachgeführt: $A(x) = A_0 + \sum x_i A'_i$. Der Tensor $A'$ wird einmalig (bzw. nach jedem Zug) numerisch per finiter Differenz berechnet (Dauer ca. 10 Minuten). Dadurch entsteht ein geschlossener, glatter Hamilton-Operator $H = \frac{1}{2} p^T A(x) p + V(x)$, für den ein impliziter Midpoint-Integrator die Energie bis auf Integrationsfehler (1e-8) exakt erhält.

- **Erwartung N4 (ohne Züge):**
  Die Energieerhaltung mit dem impliziten Midpoint-Verfahren und dem Hamiltonoperator in 1. Ordnung von M_eff wird auf < 1e-8 relativ genau sein. Die Dynamik bleibt stabil.

- **Erwartung s2 (mit Ausnahmezug):**
  In Teil B haben wir gesehen, dass die Trägheit des Ausnahmezugs in s2 auch beim Rechnen am gedehnten Netz indefinit bleibt (130 negative Richtungen). Wenn M_eff nun stetig (in 1. Ordnung) mitgeführt wird, wird der Integrator diese Instabilität voll spüren. Ich erwarte, dass die Trägheit indefinit bleibt und die wachsende Mode nicht verschwindet, sondern die Energie/Trajektorie nach dem Zug explodiert (bzw. der Fixpunkt-Integrator divergiert).
