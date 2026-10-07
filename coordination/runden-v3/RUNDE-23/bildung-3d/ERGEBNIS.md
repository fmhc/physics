# BILDUNG-3D (Runde 23): Ergebnis

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary.
  - Beginn 2026-10-02 21:48:38 CEST (date).
  - Rauchlauf 22:00:49 bis 22:04:12 CEST.
  - Plan eingefroren 22:05:32 CEST (PLAN.md.eingefroren-20261002-220532), vor jedem echten Lauf.
- Laeufe auf der .69 (Uhr dort UTC):
  - 20:05:48 bis 20:13:56 UTC (= 22:05:48 bis 22:13:56 CEST): 9 Aufrufe in Ketten auf cpu, cpu2, cpu3, cpu4, cpu6,
    alle rc = 0.
  - Auswertung 20:14:06 UTC. Nachtrag (nicht gewertet) 20:16:03 UTC.
- Ergebnis geschrieben ab 22:19:22 CEST (date), Ende in der letzten Zeile.
- Explorativ (v3), Deutungen [H, im Modell M1, 3D, nur l = 0].
- Zahlen in den Tabellen stammen aus jq und haben Dezimalpunkte.

## 1. Ergebnis zuerst

1. **B3D-1 eingetroffen: Der passende Klumpen (i) wird in 3D ein Q-Ball.**
   - Er ist zu allen drei Zeiten "auf": Abweichung +0,59 / -0,40 / -0,67 % bei T = 250 / 500 / 1000.
   - Er behaelt 86,9 % der Ladung. E/Q liegt bei T = 1000 nur 0,05 % ueber der Familie.
   - Die Zentraldichte schwingt noch, aber abnehmend: Spanne 10,4 / 7,5 / 4,2 %.
2. **B3D-2 nicht eingetroffen.** Der breite Klumpen (ii) ist bei T = 1000 "auf" (-0,75 %, 82,9 % Ladung), der
   schmale (iii) nicht.
   - (iii) verliert 98 % seiner Ladung (Anteil 2,0 %).
   - Uebrig bleibt ein kompakter, stark schwingender Rest. Er hat Q = 58, E/Q = 2,93 und omega 0,903; die Familie hat
     bei dieser Frequenz Q_F = 167,5 (Abweichung -65 %).
   - Zum Vergleich in 2D (BILDUNG-1): (iii) behielt 63 % und wurde ein kleinerer Q-Ball.
   - [H] Grund: Der schmale 3D-Klumpen startet mit E/Q = 3,10 (2D: 1,16), also weit ueber 1. Er kann fast alles als
     freie Quanten abgeben.
3. **B3D-3 eingetroffen: (iv) ist bei T = 1000 nicht "auf" (-71 %) und atmet stark (Spanne 53 %).**
   - Seine Ladung bleibt ab T = 500 stabil (77,4 % auf 77,3 %), es ist also ein gebundenes Objekt.
   - Die Atmung bei 0,157 liegt unter der Schwelle 1 - omega ~ 0,26 (omega + 0,157 = 0,90 < 1). Linear kann sie also
     nicht abstrahlen [H].
   - Sie verbiegt die Phase am Zentrum so stark, dass die 50er-Fenster-Frequenz zwischen 0,728 und 0,755 springt
     (Nachtrag). Am steilen Ast der Familie macht das aus Q_F(omega_mess) 6751 bzw. 52317.
4. **B3D-0 eingetroffen, Numerik sauber.**
   - K0: Die Zentraldichte weicht bis T = 1000 um hoechstens 4,6e-12 (0,60) bzw. 1,3e-11 (0,55) ab; Schranke 1e-8.
   - Die beiden Gitter geben in 18 von 18 Paaren (Reihe x Zeit) dasselbe Urteil, |Delta omega| <= 3,3e-4.
5. **Bedeutung nach Karte:**
   - Es gilt nur die Zeile zu B3D-3: "Wie in 2D behalten grosse Klumpen eine langlebige Atmung."
   - Die Zeile "M1 ist auch in 3D fuer einzelne kugelsymmetrische Klumpen bildungsfaehig" verlangt B3D-1 **und** B3D-2.
     Sie ist nicht erreicht.
   - Die Zeile "3D verhaelt sich anders als 2D" ist an B3D-1 gebunden, das eingetroffen ist; sie gilt deshalb nicht.
   - Den Fall "B3D-1 ja, B3D-2 nein" deckt die Karte nicht ab. Beschreibend [H]: Passende und breite Klumpen werden auch
     in 3D Q-Baelle, ein zu kompakter, energiereicher zerstrahlt fast ganz.

## 2. K0, Box-Pruefung und Familie

**K0** (Reihe "exakt", diskretes Familienprofil, T = 1000):

| omega^2 | Gitter | max rel. Abweichung Zentraldichte | omega_mess | Abw. Q_Ball gegen Q_F(omega_mess) | E/Q gegen Familie |
|---|---|---|---|---|---|
| 0,60 | dr 0,02 (gewertet) | 4,6e-12 | 0,7745966692414775 (sqrt 0,6: ...4834) | -4,8e-6 | +2,2e-7 |
| 0,55 | dr 0,02 (gewertet) | 1,3e-11 | 0,7416198487095381 | -4,4e-6 | +1,1e-7 |
| 0,60 | dr 0,04 | 1,8e-12 | 0,7745966692414862 | -1,9e-5 | +8,8e-7 |
| 0,55 | dr 0,04 | 4,9e-12 | 0,7416198487095729 | -1,8e-5 | +4,3e-7 |

- Alle K0-Fenster sind "auf".
- Die kleine Q-Abweichung ist der Unterschied zwischen der Leapfrog-Ladung (v aus phi(t +- dt)) und der Formel
  2 omega Integral f^2, Ordnung dt^2.
- Die Ladung in r < 60 ist bis T = 1000 erhalten: 2873,130199016287 auf 2873,130199016024 (dr 0,02, 0,60).

**Box-Pruefung** (r_sd = 60, r_max = 120, Begruendung im Plan, Abschn. 3):

- **Vorab:**
  - Familienschwanz am Absorberbeginn S(60)/S0 = 1,5e-31 (0,60) bzw. 1,5e-28 (0,55); Ladung jenseits r_sd 3e-30
    bzw. 4e-28.
  - Gauss-Starts S(60)/S(0): (iv) 1,1e-18, (ii) 8,8e-38, (i) 2,4e-63, (iii) 1,6e-128.
- **Nachher** (nur berichtet, Nachtrag Abschn. 6): Die Baelle bleiben kompakt.
  - Bei T = 1000 ist r_halb der Dichte 6,8 (i), 6,6 (ii), 3,0 (iii) und 13,3 (iv).
  - Der Anteil von Q(r < 60) in r < 20 betraegt 99,996 % (i), 96,7 % (ii), 98,1 % (iii) und 99,65 % (iv).
  - Der Rest ist auslaufende Strahlung.
  - Ballladung erreicht den Absorber also nicht. **Box-Pruefung bestanden.**
- **Langsame Strahlung bleibt lange im Messvolumen:** Bei (ii) liegen zu T = 250 / 500 noch 10,0 / 8,5 % von Q_Ball
  ausserhalb r < 30 (Abschn. 3).

**Familie M1 in 3D** (dr 0,02, r_max 120; 39 Punkte, alle "ok", bei dr 0,04 ebenso):
- Newton-Rest 4e-13 bis 2,5e-12, Virialrest -1,65e-5 bis -1,93e-5.
- dr 0,04 gibt Q_F um 4e-5 bis 9e-5 relativ kleiner und E/Q um <= 5,5e-6 anders (hilfs/familie.jq).

| omega^2 | Q_F | E_F/Q_F | R_rms | S0 |
|---|---|---|---|---|
| 0.52 | 280332.4 | 0.72836 | 27.743 | 1.0194 |
| 0.53 | 85855.1 | 0.73899 | 18.654 | 1.0288 |
| 0.54 | 37412.5 | 0.74959 | 14.127 | 1.0379 |
| 0.55 | 19773.1 | 0.76015 | 11.425 | 1.0467 |
| 0.56 | 11804.7 | 0.77065 | 9.635 | 1.0554 |
| 0.57 | 7664.7 | 0.78109 | 8.365 | 1.0639 |
| 0.58 | 5291.5 | 0.79144 | 7.422 | 1.0722 |
| 0.59 | 3828 | 0.8017 | 6.695 | 1.0803 |
| 0.6 | 2873.1 | 0.81185 | 6.119 | 1.0881 |
| 0.61 | 2221.6 | 0.82189 | 5.655 | 1.0957 |
| 0.62 | 1760.5 | 0.8318 | 5.273 | 1.103 |
| 0.63 | 1424.1 | 0.84158 | 4.955 | 1.1097 |
| 0.64 | 1172.3 | 0.85121 | 4.687 | 1.116 |
| 0.65 | 979.8 | 0.86069 | 4.46 | 1.1215 |
| 0.66 | 829.7 | 0.87 | 4.266 | 1.1263 |
| 0.67 | 710.8 | 0.87914 | 4.099 | 1.1302 |
| 0.68 | 615.2 | 0.8881 | 3.956 | 1.133 |
| 0.69 | 537.4 | 0.89687 | 3.831 | 1.1347 |
| 0.7 | 473.4 | 0.90543 | 3.724 | 1.1351 |
| 0.71 | 420.2 | 0.91378 | 3.632 | 1.1341 |
| 0.72 | 375.5 | 0.9219 | 3.552 | 1.1316 |
| 0.73 | 337.7 | 0.92979 | 3.485 | 1.1275 |
| 0.74 | 305.5 | 0.93744 | 3.428 | 1.1216 |
| 0.75 | 277.9 | 0.94482 | 3.38 | 1.114 |
| 0.76 | 254.1 | 0.95194 | 3.342 | 1.1044 |
| 0.77 | 233.5 | 0.95877 | 3.313 | 1.0928 |
| 0.78 | 215.5 | 0.96531 | 3.291 | 1.079 |
| 0.79 | 199.9 | 0.97154 | 3.278 | 1.063 |
| 0.8 | 186.1 | 0.97745 | 3.272 | 1.0446 |
| 0.81 | 174 | 0.98301 | 3.275 | 1.0237 |
| 0.82 | 163.4 | 0.98823 | 3.286 | 1.0003 |
| 0.83 | 154.1 | 0.99308 | 3.305 | 0.9742 |
| 0.84 | 145.9 | 0.99754 | 3.334 | 0.9453 |
| 0.85 | 138.7 | 1.00159 | 3.372 | 0.9135 |
| 0.86 | 132.4 | 1.00523 | 3.421 | 0.8787 |
| 0.87 | 127 | 1.00843 | 3.483 | 0.8407 |
| 0.88 | 122.5 | 1.01117 | 3.559 | 0.7995 |
| 0.89 | 118.7 | 1.01343 | 3.653 | 0.7549 |
| 0.9 | 115.6 | 1.01519 | 3.767 | 0.7067 |

- **Q_F faellt im ganzen Bereich monoton** (dQ/d omega < 0, also der Vakhitov-Kolokolov-stabile Ast [L]). Ein Minimum
  von Q_F laege, falls es eines gibt, jenseits 0,90; das ist nicht gerechnet.
- **E_F/Q_F ueberschreitet 1** zwischen omega^2 = 0,84 und 0,85. Darueber haben die Baelle mehr Energie als freie
  ruhende Quanten derselben Ladung.
- **Startwerte** (dr 0,02):

| Klumpen | s | A^2 = S(0) | Q(t = 0) | E/Q(t = 0) | Familie E/Q |
|---|---|---|---|---|---|
| (i) | 4,9965 | 2,670 | 2873,14 = Q_F | 0,9050 | 0,8118 |
| (ii) | 6,4955 | 1,215 | 2873,14 | 0,8701 | 0,8118 |
| (iii) | 3,4976 | 7,785 | 2873,14 | **3,0993** | 0,8118 |
| (iv) | 9,3283 | 2,949 | 19773,07 | 0,9179 | 0,7601 |

## 3. Tabelle je Klumpen, Gitter und Zeit

Legende:
- Fenster [T - 50, T].
- **Q-Anteil** = Q_Ball / Q(t = 0), mit Q_Ball = mittlere Ladung in r < 60.
- **Kern r<30** = Q(r < 30) / Q_Ball.
- **Abw.** = (Q_Ball - Q_F(omega_mess)) / Q_F(omega_mess).
- **E/Q** in r < 60, dahinter die Familie bei omega_mess.
- **S0 Mittel** = mittlere Zentraldichte, dahinter S0 der Familie bei omega_mess.
- **Spanne rel** = (max - min)/Mittel der Zentraldichte (Atmungsamplitude).
- **Atmung omega** = Gipfel des Periodogramms der Zentraldichte in [T - 200, T]. Bei K0 ist das Rauschen (Spanne
  ~1e-11).
- **R_rms r<30** aus dem Schnappschuss bei T (Abstand 0,2), dahinter die Familie.
- Erzeugt mit hilfs/tabelle.jq aus lauf-69/aus/gesamt.json.

| Reihe | dr | T | Q-Anteil | Kern r<30 | omega_mess | omega^2 | Q_Ball | Q_F(omega_mess) | Abw. | E/Q (Familie) | S0 Mittel (Familie) | Spanne rel | Atmung omega | R_rms r<30 (Familie) | Urteil |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K0-0.60 | 0.02 | 250.0 | 1 | 1 | 0.774597 | 0.6 | 2873.1 | 2873.1 | -0 % | 0.8118 (0.8118) | 1.0881 (1.0881) | 0 % | 2.373 | 6.119 (6.119) | auf |
| K0-0.60 | 0.02 | 500.0 | 1 | 1 | 0.774597 | 0.6 | 2873.1 | 2873.1 | -0 % | 0.8118 (0.8118) | 1.0881 (1.0881) | 0 % | 7.717 | 6.119 (6.119) | auf |
| K0-0.60 | 0.02 | 1000.0 | 1 | 1 | 0.774597 | 0.6 | 2873.1 | 2873.1 | -0 % | 0.8118 (0.8118) | 1.0881 (1.0881) | 0 % | 10.224 | 6.119 (6.119) | auf |
| i | 0.02 | 250.0 | 0.8776 | 0.9909 | 0.77793 | 0.60518 | 2521.6 | 2506.7 | 0.59 % | 0.8203 (0.8171) | 1.0926 (1.0921) | 10.42 % | 1.632 | 5.835 (5.867) | auf |
| i | 0.02 | 500.0 | 0.8693 | 0.9999 | 0.77792 | 0.60516 | 2497.7 | 2507.7 | -0.4 % | 0.8178 (0.817) | 1.0924 (1.0921) | 7.5 % | 1.636 | 5.835 (5.868) | auf |
| i | 0.02 | 1000.0 | 0.8691 | 1 | 0.777857 | 0.60506 | 2497.1 | 2514 | -0.67 % | 0.8174 (0.8169) | 1.0922 (1.092) | 4.15 % | 1.636 | 5.841 (5.872) | auf |
| ii | 0.02 | 250.0 | 0.9839 | 0.8995 | 0.78189 | 0.61135 | 2826.8 | 2149.9 | 31.49 % | 0.8586 (0.8232) | 1.098 (1.0967) | 7.85 % | 0.224 | 7.886 (5.599) | nicht auf |
| ii | 0.02 | 500.0 | 0.8855 | 0.9149 | 0.780686 | 0.60947 | 2544.2 | 2250.6 | 13.05 % | 0.8397 (0.8214) | 1.0955 (1.0953) | 2.87 % | 0.22 | 6.135 (5.677) | nicht auf |
| ii | 0.02 | 1000.0 | 0.8291 | 0.9676 | 0.779028 | 0.60688 | 2382 | 2400.1 | -0.75 % | 0.8278 (0.8188) | 1.0932 (1.0934) | 3.75 % | 0.231 | 5.698 (5.79) | auf |
| iii | 0.02 | 250.0 | 0.0327 | 0.6444 | 0.903495 | 0.8163 | 94.1 | 167.2 | -43.74 % | 2.404 (0.9863) | 0.6291 (1.0093) | 238.66 % | 1.773 | 4.636 (3.281) | nicht auf |
| iii | 0.02 | 500.0 | 0.0212 | 0.9437 | 0.902274 | 0.8141 | 60.9 | 169.5 | -64.05 % | 2.8905 (0.9852) | 0.6231 (1.0144) | 240.11 % | 1.773 | 3.593 (3.278) | nicht auf |
| iii | 0.02 | 1000.0 | 0.0203 | 0.9831 | 0.903327 | 0.816 | 58.3 | 167.5 | -65.21 % | 2.9339 (0.9862) | 0.6245 (1.01) | 240.05 % | 1.773 | 3.534 (3.28) | nicht auf |
| K0-0.55 | 0.02 | 250.0 | 1 | 1 | 0.74162 | 0.55 | 19773 | 19773.1 | -0 % | 0.7601 (0.7601) | 1.0467 (1.0467) | 0 % | 7.23 | 11.425 (11.425) | auf |
| K0-0.55 | 0.02 | 500.0 | 1 | 1 | 0.74162 | 0.55 | 19773 | 19773.1 | -0 % | 0.7601 (0.7601) | 1.0467 (1.0467) | 0 % | 0.231 | 11.425 (11.425) | auf |
| K0-0.55 | 0.02 | 1000.0 | 1 | 1 | 0.74162 | 0.55 | 19773 | 19773.1 | -0 % | 0.7601 (0.7601) | 1.0467 (1.0467) | 0 % | 0.734 | 11.425 (11.425) | auf |
| iv | 0.02 | 250.0 | 0.8988 | 0.8694 | 0.748922 | 0.56088 | 17772.4 | 11329.1 | 56.87 % | 0.8162 (0.7716) | 0.9859 (1.0562) | 87.67 % | 0.275 | 11.302 (9.506) | nicht auf |
| iv | 0.02 | 500.0 | 0.7738 | 0.9972 | 0.757144 | 0.57327 | 15300.9 | 6750.7 | 126.65 % | 0.7764 (0.7845) | 0.9606 (1.0666) | 65.75 % | 0.157 | 10.745 (8.027) | nicht auf |
| iv | 0.02 | 1000.0 | 0.773 | 0.9979 | 0.731833 | 0.53558 | 15283.7 | 52317.4 | -70.79 % | 0.7745 (0.7449) | 1.0473 (1.0339) | 53.3 % | 0.157 | 10.684 (15.77) | nicht auf |
| K0-0.60 | 0.04 | 250.0 | 1 | 1 | 0.774597 | 0.6 | 2873 | 2873 | -0 % | 0.8119 (0.8118) | 1.0881 (1.0881) | 0 % | 15.342 | 6.119 (6.119) | auf |
| K0-0.60 | 0.04 | 500.0 | 1 | 1 | 0.774597 | 0.6 | 2873 | 2873 | -0 % | 0.8119 (0.8118) | 1.0881 (1.0881) | 0 % | 15.95 | 6.119 (6.119) | auf |
| K0-0.60 | 0.04 | 1000.0 | 1 | 1 | 0.774597 | 0.6 | 2873 | 2873 | -0 % | 0.8119 (0.8118) | 1.0881 (1.0881) | 0 % | 5.896 | 6.119 (6.119) | auf |
| K0-0.55 | 0.04 | 250.0 | 1 | 1 | 0.74162 | 0.55 | 19772 | 19772.3 | -0 % | 0.7601 (0.7601) | 1.0467 (1.0467) | 0 % | 16.107 | 11.425 (11.425) | auf |
| K0-0.55 | 0.04 | 500.0 | 1 | 1 | 0.74162 | 0.55 | 19772 | 19772.3 | -0 % | 0.7601 (0.7601) | 1.0467 (1.0467) | 0 % | 14.882 | 11.425 (11.425) | auf |
| K0-0.55 | 0.04 | 1000.0 | 1 | 1 | 0.74162 | 0.55 | 19772 | 19772.3 | -0 % | 0.7601 (0.7601) | 1.0467 (1.0467) | 0 % | 14.286 | 11.425 (11.425) | auf |
| i | 0.04 | 250.0 | 0.8776 | 0.9909 | 0.777926 | 0.60517 | 2521.4 | 2507 | 0.57 % | 0.8203 (0.8171) | 1.0926 (1.0921) | 10.47 % | 1.633 | 5.835 (5.867) | auf |
| i | 0.04 | 500.0 | 0.8694 | 0.9999 | 0.777917 | 0.60516 | 2497.6 | 2507.9 | -0.41 % | 0.8178 (0.817) | 1.0923 (1.0921) | 7.52 % | 1.633 | 5.835 (5.868) | auf |
| i | 0.04 | 1000.0 | 0.8691 | 1 | 0.777856 | 0.60506 | 2497 | 2514 | -0.68 % | 0.8174 (0.8169) | 1.0922 (1.092) | 4.18 % | 1.633 | 5.841 (5.872) | auf |
| ii | 0.04 | 250.0 | 0.9839 | 0.8994 | 0.781874 | 0.61133 | 2826.6 | 2151.1 | 31.4 % | 0.8586 (0.8232) | 1.0981 (1.0967) | 7.85 % | 0.224 | 7.886 (5.6) | nicht auf |
| ii | 0.04 | 500.0 | 0.8855 | 0.915 | 0.780687 | 0.60947 | 2543.9 | 2250.4 | 13.04 % | 0.8397 (0.8214) | 1.0955 (1.0953) | 2.85 % | 0.22 | 6.135 (5.677) | nicht auf |
| ii | 0.04 | 1000.0 | 0.8291 | 0.9676 | 0.779027 | 0.60688 | 2381.9 | 2400.1 | -0.76 % | 0.8278 (0.8188) | 1.0932 (1.0934) | 3.75 % | 0.232 | 5.698 (5.79) | auf |
| iii | 0.04 | 250.0 | 0.033 | 0.6449 | 0.903545 | 0.81639 | 94.7 | 167.1 | -43.3 % | 2.391 (0.9864) | 0.629 (1.0091) | 238.49 % | 1.771 | 4.596 (3.281) | nicht auf |
| iii | 0.04 | 500.0 | 0.0214 | 0.9439 | 0.902168 | 0.81391 | 61.4 | 169.7 | -63.81 % | 2.8708 (0.9851) | 0.6236 (1.0149) | 240 % | 1.771 | 3.602 (3.278) | nicht auf |
| iii | 0.04 | 1000.0 | 0.0204 | 0.9831 | 0.903 | 0.81541 | 58.7 | 168.1 | -65.06 % | 2.913 (0.9859) | 0.6239 (1.0114) | 240.16 % | 1.774 | 3.541 (3.28) | nicht auf |
| iv | 0.04 | 250.0 | 0.8988 | 0.8696 | 0.749201 | 0.5613 | 17770.4 | 11112.3 | 59.92 % | 0.8162 (0.772) | 0.9856 (1.0565) | 87.85 % | 0.275 | 11.303 (9.446) | nicht auf |
| iv | 0.04 | 500.0 | 0.7739 | 0.9972 | 0.757397 | 0.57365 | 15302.3 | 6653.4 | 129.99 % | 0.7764 (0.7849) | 0.9606 (1.0669) | 65.86 % | 0.157 | 10.746 (7.99) | nicht auf |
| iv | 0.04 | 1000.0 | 0.7731 | 0.9979 | 0.731563 | 0.53518 | 15285.2 | 54021.7 | -71.71 % | 0.7745 (0.7445) | 1.0474 (1.0335) | 53.28 % | 0.157 | 10.682 (15.939) | nicht auf |

- **Abwicklung der Phase:** In keinem Fenster trat die Regel "Phase unsicher" ein. Der groesste Phasensprung je
  Messpunkt im Fenster war 0,82 rad bei (iii), die Grenze ist pi/2. Groessere Spruenge (bis 2,94 rad) lagen nur
  ausserhalb der Fenster, bei (iii) und (iv).
- **(i):**
  - Ladungsverlust fast ganz vor T = 250 (87,8 % bei 250, 86,9 % ab 500).
  - Die Frequenz passt zur Ladung: Das Familienmitglied mit Q = 2497,1 hat omega ~ 0,77811 (aus der Tabelle in ln Q
    interpoliert), gemessen sind 0,77786.
- **(ii):**
  - Bei T = 250 und 500 "nicht auf" (+31,5 / +13,0 %). Q_Ball enthaelt dort noch langsame Strahlung zwischen r = 30
    und 60 (Kern 0,90 / 0,91).
  - Nachtraeglich gerechnet, nicht gewertet: Mit Q(r < 30) waere die Abweichung bei T = 500 +3,4 %, bei T = 250
    +18,3 %.
- **(iii):**
  - Die Zentraldichte schwingt zwischen 0,031 und 1,53 mit omega 1,773.
  - Ladung in r < 30: 60,6 (T 250), 57,5 (500), 57,3 (1000). Der Rest ist also langlebig.
- **(iv):**
  - Spanne 88 / 66 / 53 %, also langsam fallend. E/Q 0,7745 bei T = 1000.
  - Das Familienmitglied mit gleicher Ladung (omega^2 ~ 0,555, aus der Tabelle interpoliert, nachtraeglich) hat
    E/Q ~ 0,7654. (iv) liegt also ~1,2 % darueber; diese Energie steckt in der Atmung [H].

## 4. B3D-0 bis B3D-3

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang (dr 0,02) | Zahlen | dr 0,04 (berichtet) |
|---|---|---|---|---|---|
| B3D-0 | K0 bestanden | 90 % | **eingetroffen** | 4,6e-12 (0,60) und 1,3e-11 (0,55) < 1e-8 | eingetroffen (1,8e-12 / 4,9e-12) |
| B3D-1 | (i) bei T = 500 "auf" | 60 % | **eingetroffen** | Q_Ball 2497,7, omega_mess 0,777920, Q_F(omega_mess) 2507,7, Abw. -0,40 % | eingetroffen (-0,41 %) |
| B3D-2 | (ii) und (iii) bei T = 1000 beide "auf" | 45 % | **nicht eingetroffen** | (ii) "auf", Abw. -0,75 %; (iii) "nicht auf", Abw. -65,2 % (Q_Ball 58,3 gegen Q_F 167,5, Ladungsanteil 2,0 %) | nicht eingetroffen (-0,76 % / -65,1 %) |
| B3D-3 | (iv) bei T = 1000 nicht "auf", weil er weiter deutlich atmet (Spanne > 5 %) | 55 % | **eingetroffen** (beide Teile) | "nicht auf", Abw. -70,8 % (Q_Ball 15284 gegen Q_F 52317); Spanne 53,3 % > 5 % | eingetroffen (-71,7 %, 53,3 %) |

- Jede Vorhersage hatte vorab einen moeglichen Fehlausgang, und B3D-2 ist gescheitert.
- **Lesart zu B3D-3** [H]: Das "nicht auf" kommt von der Atmung, nicht von Ladungsverlust.
  - Die Ladung ist ab T = 500 konstant (15301 auf 15284).
  - Die Phase am Zentrum ist so stark moduliert (Restfehler des Phasenfits 1,3 bis 1,5 rad), dass die
    50er-Fensterfrequenz um +-0,01 streut.
  - Auch gemittelt ueber [500; 1000] (Nachtrag) liegt omega mit 0,7426 noch ~0,0024 unter dem Familienmitglied gleicher
    Ladung (~0,745), das sind -16 % in Q. Der stark atmende Ball sitzt also auch im Mittel nicht genau auf der
    stationaeren Familie.

## 5. Latten, Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Latten (v3):**
- **L1 kann scheitern:** ja.
  - B3D-2 ist gescheitert.
  - B3D-1 haette schon an einer Frequenzabweichung von ~0,002 scheitern koennen (das sind 10 % in Q).
  - (ii) war bei T = 250 und 500 tatsaechlich "nicht auf", vor allem wegen noch nicht abgeflossener Strahlung in
    r < 60.
  - B3D-3 haette an "auf" oder an einer Spanne <= 5 % scheitern koennen.
- **L2 Gegenprobe:** ja.
  - K0 im selben Aufbau: "auf" zu allen Zeiten, omega auf 1e-14, Q auf 5e-6, E/Q auf 2e-7.
  - Zwei Ladungsradien (r < 30 gegen r < 60).
  - E/Q als energetische Gegenprobe: (i) +0,05 % gegen die Familie.
  - Langer Phasenfit (Nachtrag, nicht gewertet): bestaetigt (i) mit -0,04 % und (iii) mit -65 %.
- **L3 Numerik:** bestanden.
  - Zwei Gitter mit gleichem Urteil in 18 von 18 Paaren.
  - |Delta omega_mess| <= 3,3e-4, |Delta Q-Anteil| <= 2,4e-4, |Delta Abw.| <= 3,3 Prozentpunkte ((iv) bei T = 500, wo
    die Abweichung ueber 100 % liegt).
  - Familie: Q_F zwischen den Gittern auf 4e-5 bis 9e-5; Virialrest -7e-5 (dr 0,04) gegen -1,8e-5 (dr 0,02), also
    zweite Ordnung.
  - Abschnitte bis=/weiter im Rauchlauf bitgleich (in den echten Laeufen nicht gebraucht).
- **L4 schon bekannt** [L, nicht nachgeprueft, keine Literaturabfrage]: Allgemein bekannt aus der Literatur zu
  Q-Baellen und Oszillonen sind:
  - Angeregte Klumpen relaxieren unter Abstrahlung zu Q-Baellen.
  - Energiereiche Klumpen (E/Q > 1) koennen weitgehend zerstrahlen.
  - Gebundene Atmungsmoden unter der Schwelle 1 - omega sind langlebig.
  - Potentiale mit anziehendem quartischem Term tragen Oszillonen.
  - Neu sind nur die Zahlen fuer M1 in 3D mit diesem Kriterium.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter, nur l = 0).

**Grenzen:**
- **Nur l = 0.** Nichtradiale Instabilitaeten (z. B. Zerfall in mehrere Baelle) sind nicht erfasst.
- **Ein Familienpunkt je Reihe:** (i) bis (iii) bei Q 2873 (omega^2 0,60), (iv) bei Q 19773 (0,55). Starts sind
  zentriert, ruhend und rauschfrei, im Vakuum mit Absorber.
- **Das "auf"-Kriterium ist sehr frequenzempfindlich.**
  - Bei omega^2 0,55 bis 0,60 entsprechen 10 % in Q nur 0,15 bis 0,3 % in omega (Plan, Abschn. 3).
  - Ein stark atmender, aber gebundener und ladungsstabiler Ball wie (iv) kann es im 50er-Fenster nicht erfuellen.
  - "nicht auf" heisst hier "nicht als stationaeres Familienmitglied messbar", nicht "zerfallen".
- **Langsame Strahlung zaehlt in r < 60 mit** ((ii) bei T = 250 und 500).
- **(iii):** Der Rest (Q 58) liegt unter dem kleinsten Q_F der Tabelle (115,6 bei 0,90). Ob es fuer omega^2 > 0,90 ein
  Familienmitglied mit Q ~ 58 gibt, ist nicht gerechnet. Fuer das Urteil spielt das keine Rolle: omega_mess^2 = 0,816
  liegt in der Tabelle.
- Zweite Ordnung in Raum und Zeit; Reflexion am Absorber nicht gemessen (nur die Ladungsbilanz).

**Selbstanzeigen:**
1. **Box nach dem ersten Rauchlauf geaendert, vor dem Einfrieren:** Der erste Familien-Rauchlauf lief mit r_sd 50 und
   r_max 110. Wegen des Gauss-Schwanzes von (iv) bei r = 50 (S(50)/S(0) ~ 3e-13 nach Formel) habe ich 60/120
   gewaehlt (1e-18).
   Im Plan, Abschn. 3, dokumentiert.
2. **Code vor dem Einfrieren geaendert:** Nach dem ersten Rauchlauf kam die Regel "Phase unsicher" dazu (Anlass:
   Phasensprung 3,08 rad bei (iii) bis t = 20). Die Rauch-Auswertung wurde danach wiederholt. Im gewerteten Code
   (c614c1e6...) ist sie enthalten; in den Fenstern griff sie nie.
3. **hilfs/tabelle.jq:** Nach der Auswertung habe ich nur die Sortierung geaendert (dr 0,02 zuerst), reine
   Darstellung.
4. **Nachtrag hilfs/nachtrag.py:** erst nach Kenntnis der gewerteten Ergebnisse entstanden, nicht gewertet
   (Abschn. 6).
   - Seine "Linien" bei (i) und (ii) liegen in der Hauptkeule des Hann-Fensters, Abstand 0,02. Das sind keine eigenen
     Linien. Echt getrennt sind nur die Linien bei (iii) und (iv).
5. **Auf der .69:** py_compile hat im eigenen Rechenordner __pycache__ angelegt (nicht entfernt). Die Rohdateien (.pt,
   zusammen 8,3 MB) liegen nur dort in /home/fmh/fmhc-physics-remote/runde23-bildung-3d/aus/. Ihre sha256 stehen in
   gesamt.json.
6. **fam02-c:** Der Aufruf wartete ~3,7 min auf den Lock von cpu6 (fremder Lauf). Im Log steht eine ssh-Meldung
   "mux_client_request_session ... refused", danach baute ssh eine eigene Verbindung auf. Ohne Folgen.
7. **Scratchpad:** Die Hintergrundaufrufe des Werkzeugs (Bash im Hintergrund, Monitor) legen dort automatisch
   Ausgabedateien an. Alle Ausgaben habe ich nach lauf-69/*.log umgeleitet und selbst nichts dorthin geschrieben.
8. **Doppelte Tabellen:** hilfs/tabelle-ausgabe.md und hilfs/familie-ausgabe.md waren Zwischenausgaben der jq-Skripte.
   Sie sind jetzt nur noch Verweise auf dieses Dokument (lokal kein rm).
9. **Sonst keine Abweichung vom eingefrorenen Plan.**
   - Ketten und Spuren wie geplant.
   - Kein Aufruf brauchte Abschnitte.
   - bic2_2d_praez_v2.py wurde nur importiert (sha256 lokal = .69).

**Laufzeiten** (kleintest.sh, CPU, 1 Thread; Dienstlaufzeit):
- **Zeitlaeufe T = 1000:**
  - dr 0,02 mit 2 Reihen: 3:41 / 3:42 / 3:44 min (Schleife 208 bis 209 s, 1,66 bis 1,67 ms je Schritt, Profil 9 bis
    11 s)
  - dr 0,04 mit 6 Reihen: 2:30 min (Schleife 133 s, 2,13 ms je Schritt)
- **Familie:**
  - dr 0,02: 2:20 / 1:55 / 2:06 min (je 13 Punkte, 8,6 bis 10,4 s je Punkt)
  - dr 0,04: 2:00 / 1:56 min (19 / 20 Punkte, ~6 s je Punkt)
- **Sonst:** Auswertung 3,5 s, Nachtrag 3,3 s, Rauchlaeufe 3 bis 35 s.

**sha256:**
- **Code und Plan** (lokal = .69, geprueft):
  - code/zeit3d.py `c614c1e6498379c9a2ae21e5fa6e87008842447b63ca5bbd77a38d5b24119a3e` (auch in jeder Ausgabe-JSON)
  - RUNDE-22/bildung-leiter/code/bic2_2d_praez_v2.py `042ba893129ac3971dc53bf2c42b313f95f35e0f420149b274b7fd6a5be4ef00`
  - PLAN.md.eingefroren-20261002-220532 `334977f98bb59dead023e4c15b25e4e81a0fd1a7980de14dc28b7b7130883b72`
  - KARTE.md `1111fff639951d07e0e9b6e576e938df61b823ec3c1d0471d7ccd069b9301eab`
- **Hilfsdateien:**
  - hilfs/vergleich.py `8070d1d7f76e15c467481195269b22222a7bb1f82caa719ccc87cae4a311e1cd`
  - hilfs/nachtrag.py `4e1be04dcbae55384f85e189dd62f0328be8ad5d89e3292fe87248db3b7e00f8`
  - hilfs/familie.jq `11d1882f8d5ad2560caaabbfc61aa470193ba886fb6e59a3c94d502af49a083a`
  - hilfs/tabelle.jq: siehe letzte Zeile dieses Abschnitts
- **Ausgaben** (lauf-69/aus/, Kopien ohne .pt):
  - gesamt.json `3622340571fa47aace947c0a6197a9657ebfe2ab77b1a0dcb065d7196a22e98a` (Auswertung und Wertung)
  - l02-a.json `b4aa72891e2fdc12399fcf97d90869aebf21d8a25ae6d6e779ab3148395ebe36`
  - l02-b.json `350f6f28eb966cbc022d5fb492f6d9537a361167e8bc65561aae307517928ca2`
  - l02-c.json `29a959784e3babe00480c202115dc8bac01012b5a47ad556cad47e71f43c95c1`
  - l04.json `bec1046e382c691e7cafe4e944590b9e4b4e88b84b64236481a0a99f56ec258a`
  - fam02-a.json `261eb9e66533d9e8173a5f6794563d152903bb360e3830d13a5a7578b7fff96a`
  - fam02-b.json `1d0725957162ec8e61a6622f6df772c765010cc1808ef6d21f90d1954adb2830`
  - fam02-c.json `b775b0aae4d44696d930b2fcd91d265316ae8f491edbb40a68e3f9a249a68f30`
  - fam04-a.json `121fed215e22a9e647126909a4cfdf08330fcd0c8b6a29f58dee8b24d65f2ece`
  - fam04-b.json `15bf283235238dab725de9bc2541bdc100856cb48079dd85851ed8b751bd315b`
  - nachtrag.json `e2f8bec65745446b098047e19821216e682e7498eae4595d6edc2ada3dd7890c` (nicht gewertet)
- **Logs** (lauf-69/):
  - l02-a `b571eb32be1afdffe33d25d9abc3167305680ea816c7f45a3724d35be144829c`
  - l02-b `e1e34452d24a5d4a4a58500d17a139d94c064fb99ab55702b5e0041b476964aa`
  - l02-c `784cc818abd820b10b7ae802bec44465d6c7facd6ac557ff1a1f986fad50658f`
  - l04 `661ad9cc8deb7a3254fe2de9f97f026042adfadf42e70410bd7ef53c35d4f48c`
  - fam02-a `e2d56e303f491bcf86fe7a2d93860fc6fd98c9ce19701af8763d1e180a99a2cc`
  - fam02-b `d25636d397e3d8bf0ac51cdf66551e9dc14106cfadf56f831fb1c9cd3c0adbd3`
  - fam02-c `aedf53a7f1384dbaa1622cd74bcb2ea048ed2bf65e73228f1556cbed944c4f48`
  - fam04-a `1176997c24ba844161c2d28dbb0e559f7004375a690fdc2ad421e120c152ddf8`
  - fam04-b `9f7851482834dca432466165170bab43ddcd1e1ae8faa1185b7df62224e2e7d0`
  - auswerten `e006bb76f46f6f358955e750842f87691e6593261ebed23c04fb747a8c6e8532`
  - nachtrag `ad920d4b7f57015de7838929eec8d0e3d39551997f159c2ef2957340f156d764`
  - ketten-ende `c6b0144e187a9e2a5237b837300daa20578ee5cedac27a2b835787f9db2b3318`
- Rauchlauf: lauf-69/rauch/ (JSON und Logs).
- hilfs/tabelle.jq `eb83c427e3e48be5978cd90ceaa4d16615d8aacf2298f8181b2d457028f42129` (Fassung nach der Sortieraenderung)

## 6. Nachtrag (nach Kenntnis der gewerteten Ergebnisse, NICHT gewertet)

hilfs/nachtrag.py, .69 cpu, 20:16:03 bis 20:16:06 UTC, rc 0; lauf-69/aus/nachtrag.json. Werte fuer dr 0,02.

| Reihe | omega aus Fit [500; 1000] | Q_F dazu | Q_Ball [950; 1000] | Abw. | 50er-Fenster-omega in [500; 1000]: min / max / Streuung |
|---|---|---|---|---|---|
| i | 0,778017 | 2498,0 | 2497,1 | -0,04 % | 0,77785 / 0,77815 / 1,0e-4 |
| ii | 0,780160 | 2296,6 | 2382,0 | +3,7 % | 0,77903 / 0,78153 / 7,4e-4 |
| iii | 0,903051 | 168,0 | 58,3 | -65,3 % | 0,90180 / 0,90422 / 8,1e-4 |
| iv | 0,742592 | 18235,9 | 15283,7 | -16,2 % | 0,72778 / 0,75504 / 1,1e-2 |

- **Rest von (iii) bei T = 1000:**
  - kompakt: r_halb 3,0; 97 % seiner Ladung und 98,5 % seiner Energie (in r < 60) liegen in r < 10, dort Q = 56,8 und
    E = 168,5
  - Das Zentralfeld in [500; 1000] hat zwei gegenlaeufige Anteile: omega = +0,903 mit 65,5 % der Leistung und
    omega = -0,870 mit 34,5 %.
  - Ihre Summe 1,773 ist die Schwingfrequenz der Zentraldichte.
  - [H] Das ist ein oszillonartiges Objekt mit kleiner Nettoladung, kein Q-Ball der Familie. Beide Frequenzen liegen
    unter 1; das passt zur Langlebigkeit.
- **(iv):**
  - Das Zentralfeld hat die Traegerlinie 0,7427 und Seitenlinien bei 0,8997 und 0,5841 (Traeger +- 0,157) mit 63 % und
    34 % der Traegerleistung. Das ist die starke Atmung.
  - Die Dichte ist bei T = 1000 bis r = 10 flach (S 1,01 bis 1,04, r_halb 13,3). Es ist also ein duennwandiger Ball,
    dessen Wand atmet [H].
- **(i), (ii):** Das Zentralfeld liegt zu > 99,99 % bei positiver Frequenz. Eine gegenlaeufige Komponente wie bei
  (iii) gibt es nicht.

## 7. Einfach gesagt

Wir haben vier Wolken in 3D hingelegt, jede mit genau der Ladung eines echten Q-Balls, und zugeschaut, ob sie von
allein zu so einem Ball werden. Die passend breite und die zu breite Wolke schaffen es: Sie geben 13 bis 17 Prozent
ihrer Ladung als Wellen ab und sitzen dann genau auf der Q-Ball-Familie. Die zu schmale Wolke ist dagegen viel zu
energiereich, dreimal so viel Energie je Ladung wie ein ruhendes freies Teilchen. Sie zerstrahlt fast vollstaendig, und
uebrig bleibt nur ein kleines, wild pulsierendes Kluempchen, das kein Q-Ball ist. In 2D wurde aus derselben Art Wolke
noch ein kleinerer Q-Ball. Die grosse Wolke wird nach einem anfaenglichen Verlust ein Ball, der seine Ladung haelt. Er
"atmet" aber so heftig, dass man ihm die Familienfrequenz nicht ablesen kann, genau wie vorhergesagt.

---
Letzte Aenderung dieser Datei: 2026-10-02 22:24:37 CEST (date). Zeitbox 90 min ab 21:48:38 CEST eingehalten.
