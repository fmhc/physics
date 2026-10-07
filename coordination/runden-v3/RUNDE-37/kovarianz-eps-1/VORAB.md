# KOVARIANZ-EPS-1: Vorab-Datei (Vorhersagen vor jeder Messung)

- Code-Agent fuer die Leitung claude-primary. Geschrieben ab 2026-10-04 17:33:33 CEST (date), vor den Hauptlaeufen und
  ohne Kenntnis eines Gamma-Werts dieser Karte. Die Zahlen stammen aus `kovarianz_eps.py vorab` (.69, 15:24:56 bis
  15:25:03 UTC, rc 0; rauch-69/vorab.json): eindimensionale Quadraturen, keine Gitterrechnung. Die Umklappzahlen in
  Abschnitt 5 stammen aus der Kontrolle (reine Geometrie, kein Gamma).
- Kennzeichen: [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [E-v] numerische Auswertung einer
  Kontinuumsformel (keine Messung), [E-g] Geometrie aus Kontrolle oder Rauchlauf (kein Gamma), [H] Hypothese,
  [P] Projektdatei.
- Konvention wie KOVARIANZ-KUGEL-1: y = Delta Gamma/sqrt(N), Delta Gamma = Gamma_QI(verformt) - Gamma_Q(rund), gepaart je
  Saat und N. Einstein: y_E = beta_Q Delta S_1/(32 pi^2), beta_Q = -1,613 +- 0,052 (INDUZIERT-KUGEL-2) [P]; y_E haengt
  nicht von N ab. Gerader Anteil G(e) = (y(+e) + y(-e))/2, ungerader U(e) = (y(+e) - y(-e))/2.

## 1. Einstein-Vorhersage je Amplitude [E-v]

Konform l = 2: sigma = eps (1 - 5 cos^2 theta) + c, auf Volumen N normiert. Delta S_1 = Int sqrt(g) R - 32 pi^2 auf der
Einheitskugel, exakte Quadratur (keine Entwicklung).

| eps | baubar (Profil) | Delta S_1 | zweite Ordnung 36 <Y^2> V0 eps^2 | y_E (beta_Q) |
|---|---|---|---|---|
| -0,1 | ja (profil_min -4e-16) | 10,857 | 10,828 | -0,05545 +- 0,00179 |
| -0,05 | ja | 2,7412 | 2,7071 | -0,01400 +- 0,00045 |
| -0,025 | ja | 0,6827 | 0,6768 | -0,003487 +- 0,000112 |
| -0,0125 | ja | 0,17004 | 0,16919 | -0,000868 +- 0,000028 |
| +0,0125 | ja | 0,16816 | 0,16919 | -0,000859 +- 0,000028 |
| +0,025 | ja | 0,6679 | 0,6768 | -0,003411 +- 0,000110 |
| +0,05 | ja (profil_min 0, Grenzfall: R = 0 am Pol) | 2,6263 | 2,7071 | -0,01341 +- 0,00043 |
| **+0,1** | **nein (profil_min -0,114)** | (10,059) | 10,828 | (-0,0514), nicht baubar |

- **eps = +0,1 ist nicht baubar [M, E-v]:** Die Einbettung als Rotationshyperflaeche verlangt
  abs(sigma' sin theta + cos theta) <= 1, hier cos theta (1 + 10 eps sin^2 theta) <= 1, also eps <= 0,05 (am Pol
  R a^2 = e^(-2 sigma)(12 - 6 Laplace sigma) = e^(-2 sigma)(12 - 240 eps): fuer eps > 0,05 negative Kruemmung). Das
  stand schon in KOVARIANZ-KUGEL-1 PLAN Abschnitt 2 [P]. Regel QI braucht die Einbettung; also gibt es weder in (a) noch
  in (b) einen Wert bei eps = +0,1.
- Gerade und ungerade Einstein-Anteile:

| e | y_E gerade | y_E ungerade | ungerade/gerade |
|---|---|---|---|
| 0,0125 | -0,000864 +- 0,000028 | +0,0000048 | -0,6 % |
| 0,025 | -0,003449 +- 0,000111 | +0,000038 | -1,1 % |
| 0,05 | **-0,013706 +- 0,000442** | +0,000293 | -2,1 % |

- Einstein-Steigung des geraden Anteils zwischen 0,025 und 0,05: 1,991 (quadratisch).
- Probe: Delta S_1/eps^2 bei eps = 0,001: 1082,35 gegen 1082,84 (dritte Ordnung).

## 2. Was die Bauweise (a) im Mittel misst [M]

- **Die Paarung bestimmt nur die Streuung, nicht den Erwartungswert.** Die Ausgangspunkte sind gleichverteilt auf der
  runden Kugel; der Transport bildet das runde Volumen auf das g-Volumen ab. Die verschobenen Punkte sind daher exakt
  eine frische Stichprobe der Dichte 1 auf (S^4, g). Huelle in der Karte und Regel QI sind feste Funktionen dieser
  Punkte. Also gilt E[Delta Gamma_a] = E_frisch[Gamma(S^4, g)] - E_frisch[Gamma(S^4, g0)].
- Folge: Die Umschaltspruenge der Neuvernetzung (je Saat) koennen den Mittelwert nicht verschieben; sie erhoehen nur das
  Rauschen. Das erklaert auch die Nachtraege von KOVARIANZ-KUGEL-1 (Drehung mit Neuvernetzung: null im Mittel), die
  danach vorab feststanden.
- **Der Erwartungswert ist glatt in eps:** Fuer feste Kartenpunkte haengt die Huelle nicht von eps ab, und die Laengen
  sind glatt in eps (fuer eps < 0,05). Die Dichte der Punkte ist glatt in eps. Also ist E[Delta Gamma_a](eps) glatt.
- **Die erste Ableitung bei eps = 0 verschwindet [M]:** In erster Ordnung ist die Einbettung der radiale Graph
  r = 1 + sigma_1 und der Transport der Gradientenfluss xi = (4/10) grad sigma_1. Beides ist SO(5)-kovariant. Der Kern
  der ersten Variation ist dann SO(5)-invariant, also konstant, und das Integral von Y_2 ist null.
- Folge: E[Delta Gamma_a] = c2 eps^2 + c3 eps^3 + ... In genuegend kleinem eps ist die Antwort quadratisch und gerade;
  ein gleiches Vorzeichen bei +eps und -eps folgt daraus von selbst. Ob 0,025 bis 0,1 schon in diesem Bereich liegt,
  ist nicht ableitbar. Die Amplitudenreihe von KOVARIANZ-KUGEL-1 (nur negative eps; Verhaeltnisse 0,2 : 0,48 : 1) passt
  zu c2 eps^2 + c3 eps^3 mit c3/c2 etwa 6,5 knapp (1,3 SE Rest bei -0,025) und besser zu einer Antwort in abs(eps)
  [von Hand, beschreibend].
- **Bedeutung fuer KE1 [K1]:** "Gleiches Vorzeichen" allein zeigt keine Nicht-Glaette; auch c2 eps^2 hat es. Das
  Unterscheidungsmerkmal ist die Steigung des geraden Anteils: 2 bei glatter Antwort, um 1 bei einer Antwort in abs(eps).
  Ein grosser ungerader Anteil spraeche fuer ein grosses c3.

## 3. Was die Bauweise (b) messen sollte [M, H]

- In (b) bleibt das runde Netz. Die neuen Laengen sind (bis auf die QI-Skalierung) die Laengen der Rueckholung
  phi*g = e^H g0. Der Transport ist massstreu, also tr H = 0: **(b) ist das feste, im runden Mass isotrope Netz mit einer
  reinen Scherung H** (die Geometrie von g steckt im Verlauf von H).
- **Scherprognose [M, H]:** Fuer ein festes Netz und eine konstante spurfreie Scherung gilt
  Gamma(H) - Gamma(0) = c N tr(H^2) + O(H^3).
  - Erste Ordnung im Mittel null (Isotropie).
  - Schranken [M]: Mit K0 = A^T A, K1 = A^T H^ A, K2 = A^T H^2 A ist K1 K0^-1 K1 <= K2 (Projektion). Daraus folgt
    0 <= c <= 1/(4n) = 1/16.
  - Ebene-Wellen-Schaetzung (isotroper Schnitt): c = 1/(4(n+2)) = 1/24.
  - Das Vorzeichen ist positiv, also entgegengesetzt zu Einstein (B < 0). Die Groesse waechst wie N, also y wie sqrt(N).
  - Das hat KOVARIANZ-KUGEL-1 PLAN S4 schon so geschaetzt ("etwa 1,4 N eps^2") [P]; meine Zahl unten stimmt damit.
- **<tr H^2> des Transports [E-v]:** H = 2 diag(ln lambda_r, ln lambda_a (dreifach)) mit lambda_r = e^sigma(theta')
  dtheta'/dtheta, lambda_a = e^sigma(theta') sin theta'/sin theta. Erste Ordnung [M]: theta' = theta + 2 eps sin 2 theta,
  ln lambda_r = -3 eps sin^2 theta, ln lambda_a = eps sin^2 theta, tr H^2 = 48 eps^2 sin^4 theta, S^4-Mittel
  48 (96/140) eps^2 = 32,9 eps^2. Numerisch exakt: Probe 32,86 eps^2.

| e | <tr H^2> gerade | ungerade/gerade | y_Scher gerade, N-Mittel (c = 1/24) | Spanne (c = 0 bis 1/16) |
|---|---|---|---|---|
| 0,0125 | 0,005140 | -2,2 % | +0,0100 | 0 bis +0,0150 |
| 0,025 | 0,02052 | -4,4 % | +0,0398 | 0 bis +0,0597 |
| 0,05 | 0,08144 | -8,7 % | **+0,158** | 0 bis +0,237 |

  - N-Mittel heisst Mittel ueber N = 1000, 2000, 4000 (mittleres sqrt(N) = 46,53). Je N bei e = 0,05 (c = 1/24):
    +0,107 / +0,152 / +0,215.
  - Steigung des Scheranteils zwischen 0,025 und 0,05: 1,989.
- **Vorhersage fuer (b) [H]:** G_b(e) etwa y_E gerade + y_Scher gerade. Bei e = 0,05 im N-Mittel etwa +0,144
  (Spanne -0,014 bis +0,223). Das heisst: glatt (Steigung etwa 2, ungerader Anteil etwa 9 %), mit N wachsend (Faktor 2
  von 1000 auf 4000) und mit dem falschen Vorzeichen. Erwartung dann: KE2 trifft ein, KE3 und KE4 nicht.
- **Scherkontrolle D [M, H]:** sigma = 0, Punkte mit der Faserdrehung um kappa theta verschoben. Die Geometrie bleibt
  rund (y_E = 0); nur das feste Netz wird geschert. Block [[1 + g^2, g], [g, 1]], g = kappa rho sin theta, rho^2
  gleichverteilt auf [0, 1]: <tr H^2> = 0,0499 (kappa = 0,25) und 0,1977 (kappa = 0,5). Vorhersage im N-Mittel
  (c = 1/24): +0,097 und +0,383 (Spanne 0 bis 1,5-fach). Damit laesst sich c direkt messen; der Vergleich
  G_b(K) gegen y_D mal <tr H^2>_K/<tr H^2>_D trennt Scherung und Rest (beschreibend).

## 4. Moebius-Nullprobe [M, P]

- Der Moebius-Schub bildet das runde Delaunay-Netz auf sich ab (KOVARIANZ-KUGEL-1: 120 von 120 Netzen gleich). In (a)
  wird also genau das runde Netz gebaut, in (b) bleibt es: **(a) und (b) geben fuer M dasselbe Gamma** (Kontrolle C2:
  Abweichung -4,1e-12).
- **KE0 Teil 2 ist damit vorab bestimmt [K2]:** KOVARIANZ-KUGEL-1 hat genau diese Groesse gemessen: b_M = -0,00166 +-
  0,00019 (120 Saaten, -8,9 SE), Std je Saat 0,0020. Mit 40 Saaten erwarte ich etwa -0,0017 +- 0,0003, also etwa
  -5 SE: "nicht innerhalb 3 SE". Die Ursache ist die Volumenzuordnung je Simplex (CI waere exakt null).
- KE0 Teil 1 ist eine Codepruefung: (a) bei eps = -0,1 ist mit dem Code von KOVARIANZ-KUGEL-1 bitgleich (Kontrolle C3,
  Saat 0, N = 1000; live und gegen dessen Laufdatei).

## 5. Umklappen in (b) [E-g, aus Kontrolle und Rauchlauf; kein Gamma]

| | K-0,1 | K-0,05 | K-0,025 bis K+0,05 | D 0,25 | D 0,5 |
|---|---|---|---|---|---|
| N = 1000 (Saaten 991, 900 bis 902) | 0 bis 1 | 0 | 0 | 8 bis 13 | 36 bis 52 |
| N = 2000 (991, 900, 901) | 1 bis 2 | 0 | 0 | 9 bis 15 | 52 bis 63 |
| N = 4000 (900, 901) | 1 bis 4 | 0 bis 1 | 0 | 22 bis 31 | 103 bis 107 |

- In (b) bleiben die Netze fuer abs(eps) <= 0,025 ohne Umklappen; bei -0,05 und -0,1 klappen einzelne Simplizes von
  etwa 27 000 bis 118 000 um. Die Scherkontrolle D klappt deutlich mehr um.
- Keine entarteten Sehnen-Simplizes; alle Netze gueltig.

## 6. Zusammenfassung der Erwartungen (fuer die Urteile)

- (a): Erwartungswert glatt und fuer kleine eps gerade [M]; ob 0,025 bis 0,05 schon quadratisch ist, ist offen [H].
- (b): glatt, Steigung etwa 2, ungerader Anteil unter 10 %, positiv und mit sqrt(N) wachsend (Scherterm) [H]. Die
  Einstein-Antwort (-0,0137 bei e = 0,05) liegt etwa eine Groessenordnung unter dem Scherterm (+0,158).
- M: -0,0017 (bekannt), gleich in (a) und (b).
