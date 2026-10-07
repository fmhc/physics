# KEGEL-Q: Plan (Code-Agent fuer claude-primary, Runde 26)

- Geschrieben ab 2026-10-03 04:30:07 CEST (date). Wird vor der ersten echten Rechnung eingefroren
  (PLAN.md.eingefroren-<datum-uhrzeit>, dazu code/kegel_q.py.eingefroren-<datum-uhrzeit>).
- Karte: KARTE.md (Vorhersagen KQ0 bis KQ3 unveraendert). Code: code/kegel_q.py. Rechnen nur auf der .69 ueber
  kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6), Ordner /home/fmh/fmhc-physics-remote/runde26-kegel-q/lauf/.

## 1. Methode

1. **Ebene radiale Familie** (Befehl `radial`):
   - FV-Gitter r_j = (j + 1/2) dr mit dr = 0,01 (Probe dr = 0,005), r_max = 60, Dirichlet.
   - Newton bei festem omega^2, Familie omega^2 = 0,530 bis 0,900. Die diskrete Energie hat genau die diskreten
     Feldgleichungen als Euler-Lagrange-Gleichungen, daher gilt dE/dQ = omega auch im Diskreten.
   - Probe dE/dQ = omega an jedem Ziel-Q per zentraler Differenz (Q +- 0,1 %).
   - Fuer jedes Ziel-Q: omega(Q) per brentq auf dem VK-stabilen Ast (Q faellt mit omega), E_eben(Q), E_eben(sQ) mit
     s = 6/5 (Fuenfer-Ecke) und s = 6/7 (Siebener-Ecke), B_exakt = E_eben(Q) - E_eben(sQ)/s.
   - R_half = Radius, bei dem S = f^2 auf die Haelfte des Zentralwerts faellt; kappa = sqrt(1 - omega^2). Beide gehoeren
     zum ebenen Ball mit Ladung Q.
2. **Netz** (Befehl `netz` und in jedem Ball-Lauf mitgeschrieben):
   - n Sektoren zu 60 Grad (n = 5, 6, 7) aus dem gleichseitigen Dreiecksgitter, an den Strahlen verklebt. Alle
     Dreiecke sind gleichseitig mit Kante h.
   - Abgeschnitten bei geodaetischem Radius R = 40, Dirichlet f = 0 auf den Randecken.
   - Pruefung: genau eine Innenecke vom Grad 5 bzw. 7 (alle anderen 6), Winkeldefekt +-pi/3 an der Spitze und 0 sonst,
     Euler V - E + F = 1, Kotangens-Gewichte w = 1/sqrt(3), A_Spitze = (n/6) A_regulaer.
3. **Ball bei festem Q und festem Ort** (Befehl `ball`):
   - Minimiert wird E[f] = Q^2/(4 Sum A f^2) + Sum w (f_i - f_j)^2 + Sum A U(f^2) mit L-BFGS (scipy L-BFGS-B ohne
     Schranken; f bleibt positiv).
   - **Ort = harmonischer Schwerpunkt** W = Sum A f^2 r^s e^{i s phi} / Sum A f^2, s = 6/n, phi = Abwicklungswinkel gegen
     die Laufrichtung theta0 = 0 (eine Gitterrichtung). Begruendung:
     - z^s bildet den Kegel konform und eindeutig auf die Ebene ab (kein Schnittproblem).
     - Fuer den zentrierten Ball gilt W = 0.
     - W = d^s gilt exakt fuer jeden rotationssymmetrischen Ball im geodaetischen Abstand d, der die Spitze nicht
       ueberdeckt (Mittelwerteigenschaft holomorpher Funktionen). Abstand d = |W|^(1/s).
     - Der Ladungsschwerpunkt im aufgeschnittenen Kegel (X_karte) ist fuer den zentrierten Ball nicht null (etwa
       0,19 <r> bei n = 5) und haengt am Schnitt. Er wird nur mitgeschrieben.
   - Nebenbedingungen Re W = d^s, Im W = 0 (im flachen Flicken W = x0 + i y0) sind linear in f^2. Sie werden per
     Augmented Lagrangian erzwungen (mu = 5, hoechstens 12 Aussenschritte, Ziel |c| < 1e-9).
   - Gemeldet wird E ohne Straf- und Multiplikatorterm. Ausgewertet wird E_korr = E + m1 c1 + m2 c2, die Energie am
     exakten Ort in erster Ordnung des Nebenbedingungsrests (Unterschied im Rauchlauf <= 1e-8).
   - Gegenprobe aus dem Multiplikator: dE/dd = -m1 (N/N0) s d^(s-1).
   - Startprofil: radiales ebenes Profil zur Ladung Q um den Zielort (geodaetischer Abstand). Auf der Spitze (d = 0,
     n = 5/7) das ebene Profil zur Ladung sQ, also das exakte Kontinuumsprofil des Kegels.
   - Ein Thread je Lauf (OMP/OPENBLAS/MKL_NUM_THREADS = 1 im Skript).
4. **Auswertung** (Befehl `auswertung --h-fein 0.2 --Q-kraft 200`): mechanisch, Urteile in lauf-69/auswertung.json.

## 2. Parameter (fest)

- **Ladungen** Q = 50, 100, 200, 400 (R_half etwa 3,0 / 4,3 / 6,3 / 9,0; mittel bis duennwandig).
  - sQ fuer n = 5: 60 / 120 / 240 / 480; fuer n = 7: 42,9 / 85,7 / 171,4 / 342,9.
  - Alle liegen auf dem VK-stabilen Ast (in der Familie faellt Q monoton bis omega^2 = 0,9).
- **Gitter:** h = 0,4, 0,3 und 0,2; Urteile bei h_fein = 0,2. Scheibenradius R = 40.
- **Laufrichtung** theta0 = 0 (Gitterrichtung). d = 1,2 m mit m = 0 bis 16 (0 bis 19,2). Alle d sind fuer alle drei h
  Gitterecken auf dem Strahl.
- **Q_kraft** = 200 (R_half ~ 6,3, kappa ~ 0,668, R_half + 4/kappa ~ 12,3).

## 3. Laeufe

| Rolle | n | h | Q | Orte |
|---|---|---|---|---|
| radial | - | - | 50, 100, 200, 400 | dr = 0,01 und 0,005 |
| netz | 5, 6, 7 | 0,4 / 0,3 / 0,2 | - | - |
| bindung | 6 | alle h | alle Q | d = 0 |
| bindung | 5, 7 | alle h | alle Q | d = 0 und d = 19,2 (fern) |
| kraft | 5, 7 | alle h | 200 | d = 0; 1,2; ...; 19,2 (h = 0,2 in zwei Haelften) |
| kraft (beschreibend) | 5, 7 | 0,3 | 100 und 400 | wie oben |
| kq0 | 6 | alle h | alle Q | xy = (0, 0), (h/2, 0), (h/2, h/(2 sqrt3)), (0,37, 0,23), (3, -2), (-5,5, 4,1) |
| rand | 5, 6, 7 | 0,4 | 400 | R = 48; d = 0 (n = 5/7 auch 19,2) |
| dEdQ | 5, 6 | 0,3 | 199,8 und 200,2 | d = 0 |

## 4. Urteile (mechanisch, vorab festgelegt)

- **KQ0:** In jeder kq0-Datei (alle h, alle Q) gilt (max E - min E)/mittel E < 1e-4.
- **KQ1:** Fuenfer-Ecke bei h = 0,2.
  - B_gitter(Q) = E_flach(Q) - E_Spitze(Q); beide Baelle sind auf einer Ecke zentriert (Rolle bindung).
  - Vergleich mit B_exakt(Q) aus radial (dr = 0,01).
  - Eingetroffen, wenn |B_gitter - B_exakt|/|B_exakt| < 0,05 bei mindestens drei der vier Q.
- **KQ2:** h = 0,2, Q = 200.
  - Fuenfer-Ecke: E(d) - E(0) > 0 fuer alle d > 0 der Liste, und jede Stufe E(d_k+1) - E(d_k) >= -tol.
  - Siebener-Ecke: E(d) - E(0) < 0 fuer alle d > 0, und jede Stufe <= +tol.
  - tol = 1e-4 |B_exakt(200)|. Eingetroffen, wenn beide Netze erfuellen.
- **KQ3:** h = 0,2, Q = 200, je Netz 5 und 7.
  - Fuer alle d der Liste mit d > R_half(200) + 4/kappa(200) gilt |E(d) - E_flach(200)| < 0,01 |B_gitter| (B_gitter des
    jeweiligen Netzes). Es muss mindestens zwei solche d geben.
  - E(unendlich) := E_flach (Ball im flachen Flicken auf einer Ecke zentriert, gleiches h und R).
  - Eingetroffen, wenn beide Netze erfuellen.
- **Fallback:** Fehlen die h = 0,2-Daten einer Vorhersage bis 05:40 CEST, gilt fuer sie h = 0,3. Fehlen auch diese,
  lautet das Urteil "nicht entscheidbar". Ein abgebrochener Lauf zaehlt nur mit den Punkten, die er geschrieben hat.
- **Bedeutung:** nach der Karte (KQ1 bis KQ3 eingetroffen, bzw. KQ2 nicht eingetroffen).

## 5. Beschreibend (nicht gewertet)

- B bei h = 0,4 und 0,3; Richardson h -> 0 aus 0,3 und 0,2 (Ansatz h^2).
- B aus dem fernen Ball (d = 19,2) auf demselben Kegelnetz.
- Kraftgesetz bei h = 0,4 und 0,3 nach denselben Regeln (Gegenprobe), bei Q = 100 und 400 (Reichweite gegen R).
- Schwanz: Abklingrate von |E(d) - E_flach| fuer d >= R_half + 2/kappa (|dE| > 1e-9) gegen 2 kappa ([H] der Karte).
- Multiplikator-Kraft (Trapez) gegen die Energiestufen.
- Duennwand-Vergleich B/(sigma 2 pi R_half) gegen 8,7 % bzw. -8,0 %.

## 6. Kontrollen

- KQ0 (Ortsunabhaengigkeit im flachen Flicken), drei Gitterweiten, dE/dQ = omega (radial und auf dem Gitter),
  Randabstand (R = 40 gegen 48), Netzpruefung, Restgradient und Nebenbedingungsrest je Punkt.

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt)

- **radial** mit Q = 123,5 / 201,3 / 333,3, dr = 0,02 und 0,01.
  - Daraus Familie und R_half(Q); die Q-Liste ist danach gewaehlt.
  - Gesehen: B_exakt bei diesen Q, B5 und B7 etwa +-10 % der Duennwand-Oberflaechenenergie.
- **netz** h = 0,5, R = 20 (alle Pruefungen erfuellt).
- **ball** h = 0,5 bzw. 0,45, R = 25 bzw. 30, Q = 123,5 und 201,3 (n = 5, 6, 7; d bis 13,5; Pipeline-Probe rauch3 mit
  Auswertung). Gesehen:
  - B_gitter(h = 0,5) liegt -0,3 % neben B_exakt.
  - Der flache Ball ist ortsunabhaengig auf 5e-11.
  - An der Fuenfer-Ecke steigt E mit d, an der Siebener-Ecke faellt es.
  - **Damit waren KQ0 bis KQ2 in der Tendenz vor dem Einfrieren sichtbar (Selbstanzeige).**
  - KQ3 war bei R = 25 vom Rand ueberdeckt (E_fern - E_flach bis 1,8e-3); daher R = 40 und d <= 19,2.
- **Technik:** Mehrfaedige BLAS unter CPUQuota = 100 % bremste etwa 20-fach; behoben im Skript (ein Thread).
- **Selbstanzeige (04:27):** Lokal ist versehentlich ein Befehl mit `python3 -` und leerer Eingabe gelaufen (Tippfehler
  in einem grep-Aufruf). Er hat nichts gerechnet, verstoesst aber gegen die Regel.
