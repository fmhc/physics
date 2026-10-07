# PLAN-NACHTRAG-3 (HUELLEN-LEITER) - NACHTRAEGLICH

- Geschrieben ab 14:23 CEST (date), nach Laufbeginn. Nur Ablauf, wie Nachtrag 2.
- Gemessene Kosten mit Nachtrag 1: Stufe 2 bei R ~ 81 etwa 47 s je Zeile ohne Paar, Stufe 1 bei R ~ 39 etwa 13 s.
  Auch der Bereich bis Zeile 210 passt nicht mehr in die Zeitbox.
- Zusaetzlich nicht gestartet (vorbelegt): Stufe 1 170-190, 190-205, 205-220; Stufe 2 203-213.
- Bereits beanspruchte oder wartende Auftraege laufen weiter (keine Prozesse beendet).
- Am Ende werden Lueckenfueller fuer nie gestartete Bloecke ueber Stoppdateien (aus/stopp-stX-i0-i1) beendet:
  cmd_block kehrt dann sofort zurueck. Das ist nur Ablaufsteuerung.
- Gewertet bleibt nach Nachtrag 2 der zusammenhaengende Bereich ab omega^2 = 1,40 auf beiden Stufen.
