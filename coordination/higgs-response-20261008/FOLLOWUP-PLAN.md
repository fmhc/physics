# Folgetest N2 – nach abgeschlossenem Erstvergleich

08.10.2026. Erstvergleich: N bei g=.001 brauchbar, bei g=.005
unzureichend nach unverändertem 5%-Kriterium; keine Änderung der Erstresultate.
Neue vorher festgelegte Frage: Reicht eine störungstheoretische Korrektur
zweiter Ordnung in b bei festgehaltenem Singulettprofil für beide Kopplungen?

Mit chi=y-y0 und K=-Delta+6.25 gilt exakt:
K chi + b*y0*S + b*S*chi + 3*a*y0*chi² + a*chi³ = 0.
chi1=-K^-1(b*y0*S).
chi2=-K^-1(b*S*chi1 + 3*a*y0*chi1²).
N2=chi1+chi2. In radialen Variablen z2=-K_r^-1(b*S*z1+3*a*y0*z1²/r).
Keine freien Fitparameter, keine Optimierung, keine dritte/weitere Ordnung.
Die Entwicklung hält S fest; es ist keine Störungstheorie der kompletten
selbstkonsistenten Singulettlösung.

Alle 24 Profile; alle bisherigen Kriterien und Gitter-/Boxregeln unverändert.
Neue Quelldatei followup.py und neues Ausgabeverzeichnis results-second-order.
Alte Methoden als exakte Reproduktionskontrolle mitführen; ihre Werte sollen
mit Erstlauf auf 1e-12 absolut übereinstimmen, sonst Folgetest stoppen.
QA des Erstlaufs wiederholt; Ergebnis unabhängig von Erfolg veröffentlichen.
Selbes Ressourcenbudget und vorhandene GPU-Pacht. Keine neuen Relaxationen.
