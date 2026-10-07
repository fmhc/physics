# VORAB-S4B-AUSWERTUNG: Festlegungen und Erwartungen vor der Auswertung der L = 6-Laeufe

- Geschrieben von claude (Auswerte-Agent der Leitung claude-primary) am 2026-10-06 20:30:03 CEST (per date), vor jeder Auswertung von chi_L (m5-n6t4) und der Korrelatoren (s4b-n6t8, -t10, -t12).
- Bis hierher gesehen: nur die Logzeilen der Laeufe (Plaketten-Mittel, Mittel von |L|; m5: |L| je Stufe laut NOTIZ-S4B-L6.md) und die Lauf-Metadaten. Nicht gesehen: chi_L, Binder-Kumulante, Korrelatoren S(D), E, sigma.
- Gilt zusaetzlich zu VORAB-S4B.md (Gemini, 19:38); dort Festgelegtes wird nicht geaendert. Die Erwartung S4 der KARTE bleibt unveraendert: T_c/Wurzel(sigma) auf Finns Netz innerhalb von 20 % an 0,709 (35 %). Das Fenster ist 0,567 bis 0,851.
- Laufpruefung vorab (aus den json-Dateien auf der .69): m5-n6t4 und s4b-n6t8/-t10/-t12 mit rc = 0, kein Abbruch, kein CUDA-Graph; nmess = 400 je Stufe und Replika (m5, R = 2, S = 8) bzw. 800 (s4b, R = 1, 20 Bins zu je 40 Messungen, ntherm 200); Waermebad ohne Annahme: 18 (m5), 4, 5, 8 (s4b). Alle vier mit L = 6, tau = 0,348006576329167, Gewichte gwp.npz, su2b.py (sha256 eafc7ed2...).

## Festlegungen (Ergaenzung zu VORAB-S4B.md)

**A. beta_c (m5-n6t4, L = 6, Nt = 4)**
1. Werkzeug: `ana.py tab --nbin 20` (chi_L = nS (<L^2> - <|L|>^2) aus der rohen Polyakov-Schleife, Jackknife ueber 20 Bins). Neues Skript ana_s4b.py (neue Datei, importiert ana.py) bildet die Teilmengen heiss, kalt und beide.
2. Hauptwert: Teilmenge "beide" (gewichtetes Mittel von heiss und kalt bei gleichem beta, wie in ana.py). Parabel durch den Gitterpunkt des Maximums und seine zwei Nachbarn. Das sind die drei hoechsten Punkte, falls das Maximum eine einzige Spitze ist; sonst wird die Variante "drei hoechste Punkte" zusaetzlich genannt.
3. "Signifikant" heisst: In mindestens 95 % von 4000 Ziehungen (Gauss mit den Jackknife-Fehlern von chi_L, Seed 1) oeffnet die Parabel nach unten, und der Scheitel liegt zwischen kleinstem und groesstem beta der drei Punkte. Sonst gibt es kein beta_c aus chi_L: genannt wird nur das Gitterpunkt-Maximum, und beta = 3,30 bleibt unbelegt.
4. Fehler: Standardabweichung der Scheitel der Ziehungen, quadratisch mit (beta_c,heiss - beta_c,kalt)/2, wenn beide Teilmengen signifikant sind.
5. Querproben, nicht Teil des Hauptwerts: 5-Punkt-Parabel (ana.py-Standard); heiss und kalt getrennt; die Heissstart-Reihen a2-n6t4 (Nt = 4, beta 3,1 bis 3,7) und b2-n6t6 (Nt = 6) mit derselben Regel.

**B. sigma (s4b-n6t8, -t10, -t12, beta = 3,30)**
1. `ana.py korr --dmin 1`, nur Familie 111, Fenster D = 1, 2, 3 (cosh-Fit, relative Abweichungen), E = fit_m/d, sigma aus Nambu-Goto (D = 4, E^2 = sigma^2 L_t^2 - (2 pi/3) sigma) mit L_t = Nt tau.
2. Fehler von sigma: Fehlerfortpflanzung aus dem Jackknife-Fehler von E (|d sigma/dE| mal E_err, d sigma/dE = 2E/Wurzel((2 pi/3)^2 + 4 L_t^2 E^2)), wie in VORAB-S4B.md. Gegenprobe: direkter Jackknife von sigma_NG ueber die 20 Bins.
3. Ausfaelle: Ist im Vollsample ein S(D) mit D = 1..3 nicht positiv, ist der Fit fuer diesen Lauf nicht bestimmbar; er geht nicht in den Mittelwert ein und wird so gemeldet. Faellt der Fit nur in einzelnen Jackknife-Proben aus, wird der Fehler ueber die gueltigen Proben gerechnet und das gekennzeichnet.
4. Zusammenfassung ueber Nt = 8, 10, 12: gewichtetes Mittel der sigma(Nt) mit Gewicht 1/Fehler^2; Konsistenz als chi^2 je Freiheitsgrad; ist es groesser als 1, wird der Fehler mit dessen Wurzel skaliert.
5. Nur berichtet, nicht verwendet: Familie 100; effektive Masse aus S(2)/S(3) (ohne D = 1). Sie aendern das Ergebnis nicht.
6. Diagnosen: Lag-1-Autokorrelation der Bin-Mittel von S(D); Unabhaengigkeit der Laeufe (Pearson-Koeffizient der Plaketten-Zeitreihen; alle Laeufe haben denselben Seed 20261005).

**C. Quotient und beta-Abweichung**
1. Q = T_c/Wurzel(sigma) mit T_c = 1/(4 tau) in Einheiten 1/a. Hauptwert aus dem gewichteten Mittel von sigma bei beta = 3,30, Fehler aus sigma.
2. Fehlerquelle beta: relative Aenderung von Q durch Dbeta = beta_c - 3,30 ist (1/2) |s| Dbeta mit s = d ln(sigma a^2)/d beta. Zwei Steigungen: (i) Zwei-Schleifen-Skalierung SU(2) bei beta = 3,3, s = -5,1 [L, aus dem Gedaechtnis, auf Finns Netz nicht geprueft]; (ii) aus den Uebergangsorten dieses Netzes, wenn beide mit Regel A.3 signifikant sind (am Uebergang gilt a proportional 1/Nt, also s = 2 ln(Nt1/Nt2)/(beta_c(Nt2) - beta_c(Nt1)); nimmt eine feste Anisotropie tau an). Verwendet wird der groessere Betrag, die andere Steigung wird als Band genannt. Dbeta geht als Wurzel((beta_c - 3,30)^2 + err_beta_c^2) ein. Die Quelle steht neben dem statistischen Fehler; der Hauptwert wird nicht verschoben.
3. Abgleich mit S4: nur beschreibend. Zentralwert gegen das Fenster 0,567 bis 0,851, dazu getrennt, ob das Fehlerband ueberlappt.

## Meine Erwartungen (Hypothesen, vor der Auswertung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| E1 | beta_c(L = 6, Nt = 4) aus chi_L liegt zwischen 3,25 und 3,35 | 70 % |
| E2 | Die Parabel-Regel A.3 ist fuer "beide" erfuellt (grobes Gitter, 400 Messungen je Punkt) | 50 % |
| E3 | Fuer alle drei Nt ist der Fit D = 1..3 bestimmbar; fuer Nt = 12 am ehesten nicht | 55 % |
| E4 | sigma a^2 (gewichtetes Mittel) liegt zwischen 0,5 und 1,0 | 65 % |
| E5 | Q liegt zwischen 0,70 und 1,00; Zentralwert um 0,85 | 65 % |
| E6 | Der Zentralwert von Q liegt im Fenster 0,567 bis 0,851 | 40 % |
| E7 | Relativer Fehler von Q (Jackknife) liegt zwischen 8 % und 20 % | 55 % |
| E8 | Die drei sigma(Nt) sind innerhalb von 2 Fehlern vertraeglich (chi^2/dof <= 2) | 50 % |
| E9 | Die beta-Abweichung traegt weniger als 5 % zu Q bei | 60 % |

Fest vor der Rechnung: Die Zahlen werden berichtet, wie sie herauskommen; Fenster, Richtung, Fit-Bereich und Kriterien werden nicht nach Sicht geaendert. Alles Zusaetzliche wird als "Zusatz" gekennzeichnet.

## Nachtrag vom 2026-10-06 20:37:14 CEST (per date; nach Sicht, Anlass: das Vorab-Verfahren liefert keinen Fit)

Bis hierher gesehen (nach der Festlegung oben):
- `ana.py korr --dmin 1`: Familie 111, Fenster D = 1..3: Der Fit ist fuer alle drei Laeufe nicht bestimmbar. Nt = 8: S(3) < 0; Nt = 10 und 12: S(2) < 0 (und S(3) < 0 bei Nt = 12). Familie 100 liefert nur bei Nt = 8 einen Fit (E = 2,94 +- 1,06); sie ist laut VORAB-S4B.md nicht zu verwenden.
- `ana_s4b.py beta` (m5-n6t4, L = 6, Nt = 4): Regel A.2 bis A.4 ergibt beta_c = 3,2893 +- 0,0013 (Teilmenge beide, drei Nachbarn). Die Variante "drei hoechste Punkte" (3,30; 3,35; 3,375) ist nicht konkav (kein beta_c); die kalte Teilmenge ist nicht signifikant. Der Regelfehler 0,0013 ist deutlich kleiner als die Streuung der Teilergebnisse (heiss 3,2902; kalt 3,3057 nicht signifikant; Heissstart-Reihe a2-n6t4 3,3051); das wird im Bericht so genannt.

Festlegung dazu, vor weiteren Rechnungen:
1. Ergebnis des Auftrags nach Regel B.3: sigma und T_c/Wurzel(sigma) sind aus der Vorab-Festlegung auf L = 6 nicht bestimmbar. Daran aendert nichts Weiteres; es wird so berichtet.
2. Zusatzauswertung, nach Sicht gewaehlt und ausdruecklich kein S4-Ergebnis (Information fuer die Leitung):
   - Z1: gemeinsamer Nambu-Goto-Fit der Familie 111 (D = 1..3, alle drei Nt zugleich): S_Nt(D) = A_Nt cosh(E_Nt d (D - 3)), E_Nt aus Nambu-Goto mit L_t = Nt tau, A_Nt je Nt frei (analytisch), Gewichte 1/S_err^2 (Jackknife-Fehler der Bin-Mittel), sigma auf dem Gitter 0,30 bis 6,00 (Schritt 0,005). Negative S(D) sind zugelassen. Fehler: Delta chi^2 = 1 und Jackknife (je ein Bin weglassen, Gewichte fest). Dazu Einzelfits je Nt mit derselben Methode und die Wirkung auf Q.
   - Z2: Signal zu Rausch von S(D), D = 1..3, je Nt und Familie (aus der Ausgabe).
   - Die Zahlen aus Z1 werden nur als "Zusatz" mit dem Hinweis "nach Sicht gewaehlt" genannt und zaehlen nicht fuer die Erwartung S4.
3. Zur Fehlerquelle beta: Steigung (ii) ist nicht bestimmbar (b2-n6t6 hat kein signifikantes Maximum; a3-n6t8 reicht nur bis beta = 3,5). Es gilt die Zwei-Schleifen-Steigung (i); der Dbeta-Wert geht mit dem Regelfehler und zusaetzlich mit einem Fehler von 0,01 (Streuung der Teilergebnisse) ein; beides wird genannt.

## Nachtrag 2 vom 2026-10-06 20:41:28 CEST (per date; Diagnose der Methode, nach Sicht)

- Gesehen bis hierher: die Ausgabe von `ana_s4b.py sigma` (VORAB-Ergebnis: sigma und Q nicht bestimmbar; Z1- und Z2-Zahlen; beta-Quelle ca. 3 bis 4 %).
- Z4 (nur Diagnose, kein Ergebnis): Wie gross ist die Verschmierung der Scheiben-Korrelatoren in ana.py korr? Dort bekommt jeder der 10 Punkte einer Zelle den Ebenenindex m . n (Zellindex); die Lage des Punktes in der Zelle wird ignoriert. Neues Skript ana_s4b_scheiben.py gibt je Familie die Ebenenkoordinaten u_b der 10 Punkte (in Einheiten des Ebenenabstands) und die Paar-Abweichungen u_b' - u_b aus. Es wird nichts an der Auswertung geaendert.

## Nachtrag 3 vom 2026-10-06 20:48:01 CEST (per date; Diagnose, nach Sicht)

- Anlass: In der Ausgabe von `ana_s4b.py sigma` ist S(0) von Nt = 8 nach 10 und von 10 nach 12 jeweils um denselben Faktor gefallen (ln-Verhaeltnisse 1,2008 und 1,2006), obwohl die Fehler 5 bis 8 % betragen. Das koennte Zufall sein oder ein gemeinsames Rauschen der drei Laeufe (alle mit Seed 20261005) anzeigen.
- Z5 (Diagnose, aendert nichts am Ergebnis): Neues Skript ana_s4b_kreuz.py rechnet fuer die Familie 111 und D = 0..3 den Pearson-Koeffizienten der 20 Bin-Werte S(D) zwischen je zwei Laeufen und Mittel und Streuung des ln-Verhaeltnisses je Bin.
- Meine Erwartung vorab: unabhaengiges Rauschen, also Pearson-Koeffizienten um 0 mit Streuung etwa 0,22 (Schwelle fuer Auffaelliges: Betrag ueber 0,6); Streuung des ln-Verhaeltnisses je Bin etwa 0,2 bis 0,4 (60 %). Gemeinsames Rauschen (Koeffizienten ueber 0,6, ln-Streuung unter 0,05) ist die Gegenhypothese (20 %); der Rest ist gemischt.
- Folge, falls auffaellig: Die Annahme "drei unabhaengige Laeufe" in der Zusammenfassung ueber Nt und im Z1-Fit wird im Bericht als verletzt gemeldet.

## Nachtrag 4 vom 2026-10-06 20:50:23 CEST (per date; Robustheitsprobe, nach Sicht)

- Anlass: tau_int(|L|) liegt bei beta = 3,30 bis 3,35 bis 8,4 Messungen, die Bins der Hauptauswertung haben 20 Messungen; die Jackknife-Fehler von chi_L koennten zu klein sein.
- Z6 (Robustheitsprobe, aendert nichts am Hauptwert): `ana.py tab --nbin 10` (Bins zu 40 Messungen) fuer m5-n6t4, danach `ana_s4b.py beta` mit denselben Regeln A.2 bis A.4.
- Erwartung vorab: Die Fehler von chi_L bei 3,30 bis 3,35 wachsen um bis zu den Faktor 1,5; der Regelwert der Teilmenge beide verschiebt sich um weniger als 0,02; heiss und kalt bleiben bei 3,30 bis 3,35 verschieden (60 %).
