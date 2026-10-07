# VORAB-S4B: Festlegung der Auswertung für L=6

Um Bias durch "Auswertung nach Sicht" zu vermeiden, lege ich hiermit *vor* dem Start der L=6 Produktionsläufe die Fit-Parameter für den Polyakov-Korrelator fest:

1. **Richtung:** Es wird ausschließlich die Ebenenfamilie `111` verwendet.
   *Begründung:* Diese Diagonale zeigte bei den vorherigen L=4-Läufen das stabilste Signal. Die 100-Richtung ist durch Gitterartefakte stärker beeinträchtigt.
2. **Abstände (Fit-Fenster):** Der Fit der effektiven Masse $E$ aus dem Korrelator (cosh-Fit) erfolgt im Fenster $D \in [1, L/2]$, d.h. bei $L=6$ werden die Abstände $D=1, 2, 3$ einbezogen (`--dmin 1`).
   *Begründung:* Bei starker Dämpfung fallen Korrelatoren bei größeren Abständen sehr schnell ins Rauschen. Da die Statistik limitiert ist (max 10 Minuten Laufzeit), wird auch der kleinste Abstand $D=1$ mitgenommen.
3. **Auswertungsverfahren:** Es wird die Nambu-Goto-Formel $\sigma_{NG}$ aus dem von `ana.py korr` ermittelten `fit_E` berechnet. Der statistische Fehler von $\sigma_{NG}$ wird über Fehlerfortpflanzung aus dem Jackknife-Fehler von $E$ geschätzt.
4. **Bestimmung von $\beta_c$:** Der Wert für $\beta_c(N_t=4)$ wird aus dem Maximum der Polyakov-Suszeptibilität $\chi_L$ bei $L=6$ (aus dem Scan) ermittelt. Parabel-Fit durch die drei höchsten Punkte, sofern signifikant.

Diese Festlegungen gelten verbindlich für die Auswertung der S4B-Läufe.
