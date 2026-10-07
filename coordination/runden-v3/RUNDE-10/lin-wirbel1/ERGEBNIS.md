# LIN-WIRBEL-1: Ergebnis. Lineare Stabilitaet drehender 2D-Q-Baelle, NLS-Form gegen KG-Form

- Autor: Beweis-Agent der Leitung claude-primary. Plan vorab: PLAN.md (2026-09-30 11:25:18 CEST, vor dem ersten Lauf).
- Rechnungen: .69, kleintest.sh, Spur cpu5, ein Kern, je Aufruf unter 10 min. Lokal kein python, kein awk.
- Karte GEN-02/G2-01/KARTE.md nur gelesen, nicht geaendert.

## Kurz

1. **Die NLS-Form trifft Pego und Warchall.** Schwellen omega_c^2 = 0,60378 / 0,56839 / 0,54662 fuer m = 1, 2, 3.
   Umgerechnet ist das Omega_cr = 0,14858 / 0,16185 / 0,17002; die Quelle hat 0,1487 / 0,1619 / 0,1700.
   Kollisionsfrequenzen in NLS-Einheiten: 0,04785 / 0,02715 / 0,01365 (Quelle 0,0478 / 0,0271 / 0,0136).
   Kritisch ist jedes Mal J = 2.
2. **KG und NLS haben verschiedene Schwellen.** KG wird frueher instabil: omega_c^2 = 0,60013 / 0,56492 / 0,54297.
   Die Verschiebung ist -0,00365 / -0,00347 / -0,00365 und haengt kaum von m ab. Grund: Der Umschlag ist eine
   Krein-Kollision bei nu ungleich 0 (nu_c = 0,073 / 0,044 / 0,022 in KG-Einheiten), kein Austritt durch null. Dort
   wirkt der lambda^2-Term; bei lambda = 0 sind beide Formen gleich.
3. **Die Verschiebung schrumpft nicht mit m.** Das widerlegt die Hypothese der Leitung und meinen Teil E2
   ("schrumpft etwa wie nu_c^2"). nu_c^2 faellt von m = 1 bis m = 3 um den Faktor 11, die Verschiebung bleibt.
   Warum, ist offen.
4. **Die Zeitentwicklung passt zu KG, nicht zu NLS.**
   - m = 2 bei 0,57: gamma_KG = 0,00928, G1-03 hat 0,0098, gamma_NLS nur 0,0056.
   - m = 2 bei 0,59: gamma_KG = 0,0257, G1-03 hat 0,0265.
   - m = 1: Die KG-Schwelle 0,60013 liegt 0,00013 ueber dem Teilungspunkt 0,60 der Zeitentwicklung. NLS laege 0,0038
     darueber. Mein E3-Teil "gamma(0,60) etwa 0,004" ist damit knapp verfehlt: linear ist 0,60 gerade noch stabil.
5. **Numerisch sauber.** Zwischen h = 0,1 und h = 0,05 aendern sich die Schwellen um hoechstens 2e-5. Die groessere
   Box (R + 10) gibt dieselben Bisektionsgrenzen; gamma am oberen Ende aendert sich um weniger als 3e-12 (so gross ist
   das Rauschen der Eigenwertsuche bei gleicher Eingabe). Die
   Verschiebung KG - NLS ist auf 3e-6 gitterunabhaengig.
   Keine Boxmoden-Instabilitaet, die Nullmoden (J = 1) bleiben stabil. Im Fenster ist sonst nur J = 3 bei m = 2 instabil
   (KG ab 0,5994).

## 1. Quelle (an der Quelle gelesen)

- Pego und Warchall, arXiv nlin/0108009 (lokal: quellen/pego-warchall-nlin0108009.pdf).
- Normierung: -i u_t - Laplace u = g(u), g = |u|^2 u - |u|^4 u, Welle e^{i omega t} e^{i m theta} w(r), omega_* = 3/16.
  Das ist die NLS der Karte mit Omega = omega_PW.
- Tabelle 1 (PDF-Seite 20): omega_cr = 0,1487 / 0,1619 / 0,1700, lambda_cr = 0,0478i / 0,0271i / 0,0136i.
  Mechanismus (ebenda): Ein Paar rein imaginaerer Lueckeneigenwerte, "always with index j = 2", stoesst bei lambda_cr
  zusammen.
- Die Zahlen 0,1487 / 0,1619 / 0,1700 stehen also dort, in der Normierung der Karte.
- Umrechnung: omega_c^2 = 1 - (8/3) Omega_cr, lambda_NLS = (3 omega/4) lambda. Die 4-stelligen Werte haben +-0,00013
  Rundungsbreite in omega^2.

## 2. Warum die Schwellen verschieden sind (exakt)

- Mit lambda = i nu ist die KG-Gleichung (K - 2 omega nu sigma_3 - nu^2) v = 0. Die NLS-Form ist dieselbe Gleichung
  ohne -nu^2. K ist in beiden Faellen derselbe selbstadjungierte Operator, und K(omega) = (8/3) K_NLS(Omega) exakt.
- Also gilt P_KG(nu) = P_NLS(nu) - nu^2 * 1. Die Eigenwertaeste mu_k(nu) des selbstadjungierten Buendels verschieben
  sich um genau -nu^2, die Eigenvektoren bleiben.
- NLS-Schwelle: Das Maximum eines Astes beruehrt 0 (bei nu_c). KG-Schwelle: Dasselbe Maximum beruehrt nu_c^2.
- Weil das Maximum mit omega^2 faellt, ist KG frueher instabil. Das zeigt der Scan direkt, etwa m = 1 bei omega^2 = 0,60:
  - NLS-Paar 0,0558 und 0,1017, weit auseinander
  - KG-Paar 0,0680 und 0,0769, kurz vor dem Zusammenstoss
- Bei einem Austritt durch null (nu_c = 0) waeren die Schwellen gleich. Das kommt hier nicht vor.
- Beobachtet: Die Verschiebung ist fast konstant (-0,0035 bis -0,0037).
  - Das Verhaeltnis |Verschiebung| / nu_c^2 steigt von 0,7 (m = 1) ueber 1,8 auf 7,6 (m = 3).
  - Die Steigung des Astmaximums mit omega^2 faellt also mit m so schnell wie nu_c^2.
  - Eine Erklaerung dafuer habe ich nicht. Hypothese: Die KG-Korrektur wirkt ueber die Dynamik des Rings (Traegheit
    gegen Spannung) und nicht ueber das Verhaeltnis nu/(2 omega). Ungeprueft.

## 3. Schwellentabelle (omega^2, unsere Einheiten; kritischer Index J = 2)

| m | Literatur Evans (PW, umgerechnet) | Literatur 2D-NLS-Simulation (Karte) | NLS-Form h=0,1 / h=0,05 / R+10 / h->0 | KG h=0,1 / h=0,05 / R+10 / h->0 | KG - NLS (h->0) | Zeitentwicklung (unser KG) |
|---|---|---|---|---|---|---|
| 1 | 0,60347 (Omega 0,1487) | 0,608 bis 0,611 | 0,603804 / 0,603786 / 0,603804 / **0,603780** | 0,600153 / 0,600137 / 0,600153 / **0,600132** | **-0,003648** | 0,59 ruhig bis T = 3000, 0,60 geteilt (gamma 0,0041) |
| 2 | 0,56827 (Omega 0,1619) | 0,568 bis 0,571 | 0,568392 / 0,568389 / 0,568392 / **0,568388** | 0,564921 / 0,564918 / 0,564921 / **0,564916** | **-0,003472** | 0,57 geteilt (gamma 0,0098), 0,59 (gamma 0,0265); Sehnen-Nullpunkt gamma^2: 0,567 |
| 3 | 0,54667 (Omega 0,1700) | 0,544 bis 0,547 | 0,546644 / 0,546629 / 0,546644 / **0,546624** | 0,542989 / 0,542974 / 0,542989 / **0,542969** | **-0,003655** | nicht gerechnet |

- **Zeilen- und Spaltenerklaerung:**
  - h -> 0 ist die Richardson-Extrapolation aus h = 0,1 und 0,05 (FD 2. Ordnung).
  - R = 40 (m = 1, 2) bzw. 48 (m = 3). "R+10" ist die Boxprobe bei h = 0,1.
  - Bisektion bis 1,2e-6 Breite, instabil heisst |Im nu| > 1e-8 im Fenster um nu_c.
- **In Omega (NLS-Einheiten):**
  - NLS-Form: 0,148583 / 0,161854 / 0,170016. PW: 0,1487 / 0,1619 / 0,1700.
  - Nur m = 1 liegt eine Einheit der vierten Stelle neben PW.
  - Mit h -> 0 und Box ist unser Wert auf etwa 1e-5 stabil. Die Differenz von 1,2e-4 in Omega kommt vermutlich aus der
    Schrittweite ihrer omega-Suche. Das ist geraten, nicht geprueft.
  - KG: 0,149950 / 0,163156 / 0,171387.
- **Kollisionsfrequenz nu_c (KG-Einheiten, h = 0,05):**
  - NLS-Form: 0,08211 / 0,04801 / 0,02461. In NLS-Einheiten sind das 0,04785 / 0,02715 / 0,01365; PW hat
    0,0478 / 0,0271 / 0,0136.
  - KG: 0,07257 / 0,04356 / 0,02192.
- **Karte G2-01 (nur zur Information, keine Bewertung):**
  - Ihr Test ist die Zeitentwicklung. Der lineare KG-Wert fuer m = 3 (0,54297) liegt in ihrem Band [0,540; 0,548].
  - Die m = 3-Profile bei 0,53 bis 0,54 haben S_max bis 1,0048 > 1 (siehe Abschnitt 8, Lauf m3 09:42:41).

## 4. Groesste Wachstumsrate gamma(omega^2) je m und J (dichter Scan, h = 0,1)

- Box des dichten Scans: R = 32 (m = 1, 2) bzw. 36 (m = 3). Nur lokalisierte Eigenwerte zaehlen (Normanteil in
  r > 0,75 R unter 1e-3; gefunden: hoechstens 2e-5).
- **Stabil im ganzen Fenster:**
  - J = 1, 4, 5, 6 fuer alle drei m in beiden Formen
  - J = 3 bei m = 1 und m = 3, bei m = 2 in der NLS-Form
- **Die Nullmoden bei J = 1** spalten auf dem Gitter in ein reelles Paar nu = +-0,0017. Sie bleiben stabil
  (null_max_im = 0).

| m | omega^2 | gamma NLS-Form, J = 2 | gamma KG, J = 2 | sonst instabil |
|---|---|---|---|---|
| 1 | 0,57 / 0,58 / 0,59 / 0,595 / 0,60 | 0 | 0 | - |
| 1 | 0,605 | 0,01324 | 0,02569 | - |
| 1 | 0,61 | 0,03090 | 0,03760 | - |
| 1 | 0,62 | 0,05190 | 0,05561 | - |
| 2 | 0,55 / 0,56 | 0 | 0 | - |
| 2 | 0,565 | 0 | 0,00107 | - |
| 2 | 0,57 | 0,00561 | 0,00928 | - |
| 2 | 0,575 | 0,01225 | 0,01400 | - |
| 2 | 0,58 | 0,01733 | 0,01817 | - |
| 2 | 0,59 | 0,02624 | 0,02575 | - |
| 2 | 0,60 | 0,03428 | 0,03254 | KG J = 3: 0,00894 (Schwelle 0,59937 bei h = 0,1) |
| 3 | 0,53 / 0,535 / 0,54 | 0 | 0 | - |
| 3 | 0,545 | 0 | 0,00209 | - |
| 3 | 0,55 | 0,00311 | 0,00429 | - |
| 3 | 0,555 | 0,00547 | 0,00617 | - |
| 3 | 0,56 | 0,00768 | 0,00806 | - |
| 3 | 0,57 | 0,01234 | 0,01205 | - |

- **Kreuzung der Kurven:** Knapp ueber der Schwelle waechst KG schneller, weiter oben die NLS-Form (Kreuzung bei
  m = 2 um 0,585, bei m = 3 um 0,565). KG setzt also frueher ein, steigt aber flacher.

## 5. Vergleich mit unserer Zeitentwicklung

- **m = 2 (G1-03):**
  - Linear KG bei h = 0,05, R = 40: gamma(0,57) = 0,00928 (G1-03: 0,0098, -5 %) und gamma(0,59) = 0,02575
    (G1-03: 0,0265, -3 %).
  - Die NLS-Form liegt bei 0,57 um 43 % daneben (0,0056).
  - Die Sehne durch die linearen KG-Werte bei 0,57 und 0,59 hat ihren gamma^2-Nullpunkt bei 0,5670, wie die
    Zeitentwicklung. Die wahre lineare Schwelle 0,56492 liegt 0,002 darunter, weil gamma^2 nach oben gekruemmt ist.
    Die Karte hatte das so vermutet.
- **m = 1 (RING-T):**
  - Linear KG ist 0,59 stabil, passt.
  - 0,60 ist linear ebenfalls stabil, denn die Schwelle liegt 0,00013 darueber. Die Zeitentwicklung teilte bei 0,60
    mit gamma = 0,0041.
  - Die Sehnensteigung gamma^2 / Abstand ist 0,136 (m = 1, KG, von der Schwelle bis 0,605). Damit entspricht
    gamma = 0,0041 einer Schwelle bei hoechstens 0,59988; wegen der Kruemmung nach oben eher noch tiefer.
  - Die Zeitentwicklung (dx = 0,3, nichtlinear, endliche Stoerung) liegt also mindestens 0,00025 unter der linearen
    Kontinuumsschwelle.
  - Das ist klein, aber ein Rest, den ich nicht erklaeren kann, ohne die Zeitentwicklung feiner zu rechnen.
  - Die NLS-Schwelle (0,6038) wuerde 0,60 mit Abstand 0,0038 stabil nennen und passt deutlich schlechter.

## 6. Erwartung vorab gegen Ergebnis

- **E1 (NLS-Form gegen PW) erfuellt.** Abweichung in omega^2: +0,00031 / +0,00012 / -0,00004, erlaubt waren +-0,0005.
  J = 2 kritisch. Kollisionsfrequenz innerhalb der Rundung der Quelle (Abweichung hoechstens 0,35 %).
- **E2 (KG gegen NLS) teils erfuellt, teils widerlegt.**
  - Erfuellt: nicht gleich; Vorzeichen tiefer; Grund Krein-Kollision bei nu ungleich 0 (bestaetigt); kritisch J = 2.
  - Erwartete KG-Schwellen: m = 1 (0,594 bis 0,602) getroffen mit 0,60013; m = 2 (0,564 bis 0,568) getroffen mit
    0,56492.
  - **Verfehlt:**
    - m = 3: 0,54297 liegt ausserhalb 0,5455 bis 0,5467.
    - Die Groessenordnung fuer m = 3 (0,0002 bis 0,0012) ist verfehlt, gemessen 0,0037.
    - "Schrumpft etwa wie nu_c^2" ist widerlegt.
- **E3 (Zeitentwicklung) teils erfuellt.**
  - m = 2 erfuellt (-5 % und -3 %, erlaubt 25 %). m = 1 bei 0,59 erfuellt.
  - m = 1 bei 0,60 verfehlt (erwartet etwa 0,004, linear 0).
- **Hypothese der Leitung ("Verschiebung schrumpft mit m") widerlegt:** -0,00365 / -0,00347 / -0,00365.

## 7. Grenzen

- **Nur linear.** Aussagen gelten fuer das Spektrum der Linearisierung. Die Zeitentwicklung vergleiche ich nur ueber
  gamma und die Schwellenlage.
- **Fenster:** omega^2 = 0,57 bis 0,62 (m = 1), 0,55 bis 0,60 (m = 2), 0,53 bis 0,57 (m = 3); J = 1 bis 6.
  Instabilitaeten ausserhalb des Fensters sind nicht gesucht.
- **Dichter Scan bei m = 3, omega^2 = 0,53 und 0,535:** Der Rand liegt knapp (Profilanteil am Rand 7e-3 bzw. 1,5e-3
  bei R = 36). Beide Punkte sind in beiden Formen stabil. Die Schwellen selbst sind bei R = 48 und 58 gerechnet.
- **Eine Software, ein Verfahren (FD 2. Ordnung).** Kein zweites Programm und kein Fremdhaus. Die Gegenprobe ist
  die Quelle (PW) fuer die NLS-Form und G1-03 fuer die KG-Form.
- **Die Umrechnung auf PW-Einheiten** nimmt die exakte Abbildung f = sqrt(4/3) g, r = sqrt(3/8) rho an. Die
  Deckung von E1 bestaetigt sie mit.

## 8. Laeufe, Abweichungen und Dateien

| Lauf (UTC) | Zweck | Ergebnis | Dauer |
|---|---|---|---|
| probe 09:32:21 | Form- und Zeitprobe m = 1, J = 1, 2 (Skript fb8918d0) | laeuft; KG dicht 6 s je Matrix -> Scan-Box R = 32 | 64 s |
| m1 09:34:18 | erster Scan (Skript f746e08a) | **von mir abgebrochen:** Newton-Fortsetzung 0,57 -> 0,58 sprang auf das Plateau f = f_2 (Q = 2227, Rand 0,99). Behoben mit Schritten <= 0,002 und Profilpruefung | 68 s |
| m1 09:36:33, m2 09:39:36 | Scan und Schwellen (Skript 3e6b2f87) | Tabelle oben | 183 s / 185 s |
| m3 09:42:41 | Scan (Skript 3e6b2f87) | Abbruch durch meine eigene Probe S_max < 1 (0,53: S_max = 1,0048). Die Probe war physikalisch falsch; ersetzt durch S_max < S_h = (2 + sqrt(6 omega^2 - 2))/3, dieselbe Grenze wie im Hinweis der Leitung | 10 s |
| m3 09:43:44 | Scan und Schwellen (Skript 0bdad7c8) | Tabelle oben | 357 s |
| Nachlauf m1 09:50:41, m2 09:53:26 | Reproduktion mit Endfassung 0bdad7c8 | Schwellen, Scan und Profile bitgleich zum Erstlauf; gamma am Bisektionsende und nu_c auf unter 3e-12 gleich (ARPACK-Startvektor). Die kanonischen Dateien LIN-WIRBEL-m1/m2.json stammen aus dem Nachlauf, die Erstlaeufe liegen als *-erstlauf.* daneben | 165 s / 164 s |

- **Weitere Vermerke:**
  - Der Hinweis der Leitung kam vor dem Schreiben von PLAN.md; das steht dort.
  - Laufende Skripte habe ich nie ueberschrieben (Kopie als .neu, dann mv).
  - Die abgebrochene Unit habe ich mit systemctl --user stop beendet, nicht mit pkill.
- **Dateien:**
  - lin_wirbel.py (Endfassung)
  - laeufe/ mit LAUF-*.log, LIN-WIRBEL-m*.json, PROBE.json und den Erstlaeufen
  - SHA256SUMS.txt
  - Kopie auf der .69: /home/fmh/fmhc-physics-remote/runde10-lin-wirbel1/

## Einfach gesagt

Ein kreiselnder Q-Ball zerfaellt ab einer bestimmten Groesse in Stuecke. Fuer eine vereinfachte Gleichung (NLS)
kennt man diese Grenze aus einem Fachartikel; unser Programm trifft sie auf drei bis vier Stellen. Unsere eigentliche
Gleichung (Klein-Gordon) hat einen Zusatzterm, der nur bei schwingenden Stoerungen wirkt. Weil der Zerfall hier genau
durch so eine langsame Schwingung ausgeloest wird, zerfaellt unser Ball etwas frueher, und zwar fuer eine, zwei und
drei Umdrehungen um fast denselben Betrag. Unsere Zeitsimulationen zeigen dasselbe fruehere Zerfallen, die
vereinfachte Gleichung nicht.
