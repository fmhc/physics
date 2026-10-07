# PEITSCHE-1: Ergebnis (Runde 35)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-03 20:48:23 CEST, Plan eingefroren 21:09:56 CEST
  (PLAN.md.eingefroren-20261003-210956), Ende siehe Abschnitt 4 (date).
- Explorativ (v3). Alles synthetische Rechnung in zwei Modellen (reelles phi^4; M1). Keine Messdatenbestaetigung.
- Urteile mechanisch aus lauf-69/auswertung.json (code/auswertung.py nach PLAN.md A.4 und B.3). Kennzeichen: [M]
  Mathematik, [L]/[L?] Literatur aus dem Gedaechtnis, [H] Hypothese.

## 1. Ergebnis

1. **Die zusammenfallende Wand ist eine Peitsche, und ihre Energie bleibt unter c.** Die Wand folgt der
   Duennwand-Formel (Nambu-Goto) sehr genau: R0 = 80, d = 2, Schnelle bei R0/2, R0/4, R0/10 = 0,8660 / 0,9685 /
   0,9985 gegen 0,8660 / 0,9682 / 0,9950; Zusammenfallzeit 0,27 % frueher als (pi/2) R0. Der Energiefluss
   |T^0r|/T^00 ist ueberall und jederzeit hoechstens 1 (Rundung), im energietragenden Bereich hoechstens 0,99983.
   A0 bis A3 eingetroffen.
2. **Nicht vorhergesagt: Die Nullstelle wird schon vor dem Zusammenschlag schneller als Licht.** In d = 2 ab
   R ~ 7,3 (R0 = 80), 5,2 (R0 = 40), 3,7 (R0 = 20); in d = 3 ab R ~ 12,1 (R0 = 40) und ~ 7,7 (R0 = 20). Bei R = 2
   (R0 = 80) laeuft sie mit 1,025, waehrend der Energiefluss 0,9994 hat. Die "groesste Wandschnelle" von A3 (1,025)
   ist also schon eine Musterschnelle. Der Ueberschuss ueber die Duennwand-Formel betraegt in d = 2 bei R = 3 bis 8
   etwa (0,14 bis 0,24)/R^2, fast unabhaengig von R0; das ergibt die Schwelle R ~ 0,8 sqrt(R0) (7,2; 5,1; 3,6 gegen
   gemessen 7,3; 5,2; 3,7) [H, empirisch aus drei Laeufen]. In d = 3 ist der Ueberschuss zwei- bis dreimal so gross
   ((0,36 bis 0,66)/R^2 bei R = 3 bis 8).
3. **A4 eingetroffen:** Im Fenster t_c +- 1 springt die Nullstelle in allen fuenf Laeufen mit 29 bis 162 (Verschwinden
   und Wiederauftauchen beim Zusammenschlag und Rueckprall); die zentrale Differenz direkt vor t_c gibt 2,35 bis 3,13
   (bei R = 0,12 bis 0,19), die groesste Momentanschnelle -phi_t/phi_r im Fenster 3,7 bis 10,8. A0 gilt in jedem Lauf.
4. **A5 nicht eingetroffen:** d = 2, R0 = 20 hinterlaesst keinen Klumpen: bei t_c + 500 liegt nur 1,1e-5 der
   Anfangsenergie in r < 10; am Ursprung klingt nur noch eine Schwingung mit der Masse sqrt 2 nach (1,41416,
   Amplitude 0,0025). Beschreibend, d = 3, R0 = 20: Dort bleibt ein schwingender Klumpen mit etwa 1 % der Energie und
   Frequenz 1,30 < sqrt 2 (Oszillon).
5. **Teil B: Ein drehender Q-Ball hat nirgends Lichtgeschwindigkeit.** Das groesste v_E liegt je (m, omega) bei 0,365
   bis 0,498, hoechstens 61 % der Schranke (B1). B2 eingetroffen (0,498). B3 nicht eingetroffen: Das Maximum ueber r
   sitzt im fast leeren Kern bei r ~ m und steigt fuer jedes m monoton bis omega^2 = 0,99 (dort gilt
   v_E -> omega/sqrt(2(1 + omega^2)) [M]). Am Ring selbst trifft die Kartenschaetzung v_E = m/(R omega) auf 2,5 % und hat
   fuer m >= 3 ein inneres Maximum von 0,39 bis 0,40 bei omega^2 = 0,65 (beschreibend). B0 eingetroffen.

**Bedeutung (nach der Karte, vorab formuliert):** A1 bis A3 treffen ein: Eine Wand mit Zugspannung buendelt ihre
Energie wie eine Peitsche und kommt c beliebig nahe; ueberschritten wird c vom Energiefluss nie (A0). B1 und B2 treffen
ein: Ein drehender Q-Ball hat nirgends Lichtgeschwindigkeit, Energie fliesst in ihm hoechstens halb so schnell wie
Licht. Der Regge-Turm drehender Q-Baelle (RG-1) braucht also keine c-Enden, anders als der drehende String der
Maximum wie geschaetzt im Innern des omega-Bereichs. A4 trifft ein: Der "Knall" ist eine Musterschnelle ueber c ohne
Energietransport, und diese Musterschnelle beginnt schon vor dem Knall. [H] Der Mechanismus ist offen. Vermutlich
verschiebt die Kruemmung die Nullstelle gegen die Energiemitte der Wand, und dieser Versatz schrumpft beim
Zusammenziehen.

## 2. Urteile

Mechanisch aus lauf-69/auswertung.json (erstellt 2026-10-03T19:29:47Z); Urteilsgitter fein bzw. h0 = 0,005. Das grobe
Gitter (h0 = 0,01) gibt in allen zehn Faellen dasselbe Urteil; kein Vermerk "nicht konvergiert".

| Nr | Vorhersage (Karte, kurz) | Wahrsch. | gemessen | Urteil | Bemerkung |
|---|---|---|---|---|---|
| A0 | Energie bis t_c besser als 1e-4; \|T^0r\|/T^00 <= 1 + 1e-6 | 95 % | Energiefehler 4,3e-11 bis 9,4e-9; Verhaeltnis hoechstens 1,0 (fuenf Laeufe) | eingetroffen | Kontrolle; das Verhaeltnis ist eine Identitaet [M] |
| A1 | t_c innerhalb 2 % (d = 2: R0 = 40, 80; d = 3: R0 = 40) | 75 % | -0,66 %; -0,27 %; -1,03 % | eingetroffen | immer zu frueh; d = 2, R0 = 20: -1,65 %; d = 3, R0 = 20: -2,62 % (nicht gewertet) |
| A2 | v bei R0/2, R0/4, R0/10 innerhalb 2 % (d = 2, R0 = 80) | 70 % | +0,002 %; +0,026 %; +0,36 % | eingetroffen | bei kleinerem R0 groesser: R0 = 20 bei R0/10 +4,8 % (nicht gewertet) |
| A3 | groesste Wandschnelle mit R >= 2 ueber 0,99 (d = 2, R0 = 80) | 75 % | 1,0248 bei R = 2,03 | eingetroffen | Wert ueber 1: das ist schon Musterschnelle (Ergebnis 2) |
| A4 | [H] Nullstelle beim Zusammenschlag schneller als 1, A0 gilt | 40 % | 54,6; 54,4; 29,3; 162,5; 40,3 (alle fuenf Laeufe); A0 in jedem Lauf | eingetroffen | Sprungwerte per Definition, siehe Abschnitt 5 |
| A5 | [H] Klumpen mit >= 5 % in r < 10 bei t_c + 500, Frequenz < sqrt 2 (d = 2, R0 = 20) | 50 % | 1,1e-5 der Energie; Frequenz 1,41416 | nicht eingetroffen | Frequenz ist die Massenschwelle; d = 3 beschreibend: 1 %, 1,30 |
| B0 | J = m Q auf 1e-8; Q, E gegen RG-1 auf 1e-5 | 90 % | 6,7e-16; 4,4e-16; 4,4e-16 (20 bzw. 125 Zeilen) | eingetroffen | Nachbau mit demselben Code |
| B1 | v_E <= omega/sqrt(omega^2 + 1/2) ueberall | 99 % | hoechstens 61,1 % der Schranke | eingetroffen | Identitaet [M] |
| B2 | groesstes v_E in [0,35; 0,65] | 60 % | 0,4981 (m = 1, omega^2 = 0,99, r = 1,005) | eingetroffen | liegt im fast leeren Kern |
| B3 | m >= 3: Maximum im Innern des omega-Bereichs | 65 % | m = 3, 5, 8: Maximum bei omega^2 = 0,99 (Rand), monoton steigend | nicht eingetroffen | am Ring inneres Maximum bei 0,65 (beschreibend, Tabelle 3.5) |

## 3. Tabellen

### 3.1 Teil A, feines Gitter (in Klammern grobes, wo es abweicht)

| Lauf | t_c / duenn (Abw.) | v(R0/2) | v(R0/4) | v(R0/10) | Wand R >= 2 | Muster | vor t_c | erstes v > 1 | Energie | E-Fehler bis t_c fein / grob |
|---|---|---|---|---|---|---|---|---|---|---|
| d = 2, R0 = 80 | 125,330 / 125,664 (-0,27 %) | 0,8660 / 0,8660 | 0,9685 / 0,9682 | 0,9985 / 0,9950 (grob 0,9981) | 1,0248 bei R = 2,03 | 54,6 | 2,35 bei R = 0,12 | R = 7,31 (grob 7,47) | 0,99983 | 9,4e-9 / 1,4e-7 |
| d = 2, R0 = 40 | 62,416 / 62,832 (-0,66 %) | 0,8661 / 0,8660 | 0,9700 / 0,9682 | 1,0083 / 0,9950 | 1,0330 bei R = 2,03 (grob 1,0333) | 54,4 | 2,62 bei R = 0,14 | R = 5,21 | 0,99930 | 2,2e-9 / 3,5e-8 |
| d = 2, R0 = 20 | 30,898 / 31,416 (-1,65 %) | 0,8672 / 0,8660 | 0,9776 / 0,9682 | 1,0424 / 0,9950 (grob 1,0427) | 1,0409 bei R = 2,04 | 29,3 (grob 29,4) | 3,13 bei R = 0,16 | R = 3,72 | 0,99725 | 4,7e-10 / 7,6e-9 |
| d = 3, R0 = 40 | 51,900 / 52,441 (-1,03 %) | 0,9684 / 0,9682 | 1,0045 / 0,9980 | 1,0224 / 0,99995 | 1,0486 bei R = 2,04 | 162,5 (grob 162,7) | 2,89 bei R = 0,15 | R = 12,12 (grob 12,14) | 0,9999998 | 4,3e-10 / 6,9e-9 |
| d = 3, R0 = 20 | 25,535 / 26,221 (-2,62 %) | 0,9722 / 0,9682 | 1,0227 / 0,9980 | 1,0782 / 0,99995 | 1,0770 bei R = 2,02 | 40,3 | 3,12 bei R = 0,19 | R = 7,66 | 0,9999997 | 4,3e-11 / 6,9e-10 |

- v-Spalten: gemessen / Duennwand. "Wand R >= 2": groesste zentrale Differenz mit R >= 2 vor t_c (A3).
  "Muster": groesste Sprungschnelle im Fenster t_c +- 1 (A4). "vor t_c": groesste zentrale Differenz vor t_c ueberhaupt
  (beschreibend). "erstes v > 1": groesstes R, an dem die Nullstelle schneller als 1 wird (Nachauswertung,
  beschreibend). "Energie": max |T^0r|/T^00 im energietragenden Bereich bis t_c (beschreibend).

### 3.2 Teil A, Nachlauf bis t_c + 500 (Rest)

| Lauf | E(r < 10)/E0, Mittel t_c + 490 bis 500 | max E(r < 10)/E0 ab t_c + 100 | Gipfelfrequenz t_c + 400 bis 500 | fruehere Fenster (t_c + 10/100/200/300, je 100 lang) | phi_c Mittel / Amplitude | erstes phi_c < 0 nach t_c |
|---|---|---|---|---|---|---|
| d = 2, R0 = 20, fein | 1,08e-5 | 3,3e-4 | 1,41416 | 1,413; 1,415; 1,414; 1,414 | 1,00001 / 0,0025 | t_c + 0,74 |
| d = 2, R0 = 20, grob | 1,08e-5 | 3,3e-4 | 1,41416 | 1,413; 1,415; 1,414; 1,414 | 1,00001 / 0,0025 | t_c + 0,74 |
| d = 3, R0 = 20, grob | 1,01e-2 | 1,22e-2 | 1,299 | 1,217; 1,259; 1,279; 1,291 | 0,485 / 1,15 | t_c + 0,59 |
| d = 3, R0 = 20, fein | 1,01e-2 | 1,22e-2 | 1,299 | 1,217; 1,259; 1,279; 1,291 | 0,485 / 1,15 | t_c + 0,59 |

- sqrt 2 = 1,41421 ist die Masse der Kleinschwingungen. In d = 2 ist der Rest am Ursprung also nur noch eine
  abklingende Schwingung an der Massenschwelle (die Gipfelfrequenz liegt 5e-5 darunter, weit unter der Aufloesung
  0,063); A5 scheitert am Energieanteil.
- In d = 3 schwingt am Ursprung ein Klumpen mit grosser Amplitude um phi ~ 0,5 (er taucht also periodisch in die andere
  Mulde), Frequenz 1,22 bis 1,30 < sqrt 2 und langsam steigend, mit etwa 1 % der Anfangsenergie (E0 = 4747, also
  ~48) [L?: Gleiser 1994, Copeland/Gleiser/Mueller 1995: Oszillonen aus kugelfoermigen Blasen in phi^4; dort mit
  kleinen Anfangsradien].

### 3.3 Teil A, Nullstelle gegen Duennwand bei festen R (d = 2, R0 = 80, feines Gitter; beschreibend)

| R | 32 | 16 | 8 | 6 | 4 | 3 | 2 | 1,5 | 1 | 0,5 |
|---|---|---|---|---|---|---|---|---|---|---|
| v Nullstelle | 0,91654 | 0,98038 | 0,99853 | 1,00311 | 1,00955 | 1,01485 | 1,02493 | 1,03541 | 1,05711 | 1,13660 |
| v Duennwand | 0,91652 | 0,97980 | 0,99499 | 0,99718 | 0,99875 | 0,99930 | 0,99969 | 0,99982 | 0,99992 | 0,99998 |
| max \|T^0r\|/T^00 (Wand) | 0,96204 | 0,99973 | 0,99983 | 0,99981 | 0,99974 | 0,99965 | 0,99941 | 0,99909 | 0,99835 | 0,99780 |
| (v - v_duenn) R^2 | 0,026 | 0,149 | 0,227 | 0,213 | 0,173 | 0,140 | 0,101 | 0,080 | 0,057 | 0,034 |

Unter R ~ 1 ist die verkuerzte Wand (Dicke sqrt(2) R/80) auf dem feinen Gitter mit weniger als 5 Punkten aufgeloest;
grob und fein stimmen dort trotzdem auf 2e-3 ueberein. Bild: lauf-69/bild_a_v_gegen_R.png.

### 3.4 Teil B: groesstes v_E je m und omega^2 (h0 = 0,005, alle 125 Zeilen gueltig), Schranke omega/sqrt(omega^2 + 1/2)

| omega^2 | m = 1 | m = 2 | m = 3 | m = 5 | m = 8 | Schranke |
|---|---|---|---|---|---|---|
| 0,52 | 0,3926 | 0,3747 | 0,3707 | 0,367 | 0,3648 | 0,714 |
| 0,55 | 0,4092 | 0,3846 | 0,3806 | 0,3771 | 0,3749 | 0,7237 |
| 0,575 | 0,4228 | 0,3929 | 0,3887 | 0,3853 | 0,3831 | 0,7314 |
| 0,6 | 0,4332 | 0,403 | 0,3965 | 0,3932 | 0,3911 | 0,7385 |
| 0,625 | 0,4397 | 0,409 | 0,4043 | 0,4013 | 0,4 | 0,7454 |
| 0,65 | 0,4442 | 0,4159 | 0,4116 | 0,4085 | 0,4067 | 0,7518 |
| 0,675 | 0,4479 | 0,4229 | 0,4188 | 0,416 | 0,4142 | 0,7579 |
| 0,7 | 0,4514 | 0,4297 | 0,4259 | 0,4232 | 0,4215 | 0,7638 |
| 0,725 | 0,4549 | 0,4363 | 0,4328 | 0,4303 | 0,4287 | 0,7693 |
| 0,75 | 0,4584 | 0,4427 | 0,4396 | 0,4373 | 0,4358 | 0,7746 |
| 0,775 | 0,462 | 0,4489 | 0,4462 | 0,4441 | 0,4427 | 0,7796 |
| 0,8 | 0,4658 | 0,455 | 0,4527 | 0,4508 | 0,4496 | 0,7845 |
| 0,825 | 0,4697 | 0,461 | 0,459 | 0,4573 | 0,4562 | 0,7891 |
| 0,85 | 0,4737 | 0,4669 | 0,4652 | 0,4638 | 0,4628 | 0,7935 |
| 0,875 | 0,4778 | 0,4727 | 0,4713 | 0,4701 | 0,4693 | 0,7977 |
| 0,9 | 0,482 | 0,4783 | 0,4773 | 0,4763 | 0,4756 | 0,8018 |
| 0,92 | 0,4855 | 0,4828 | 0,482 | 0,4812 | 0,4806 | 0,8049 |
| 0,94 | 0,489 | 0,4872 | 0,4866 | 0,486 | 0,4856 | 0,8079 |
| 0,95 | 0,4908 | 0,4894 | 0,4889 | 0,4883 | 0,488 | 0,8094 |
| 0,96 | 0,4926 | 0,4915 | 0,4911 | 0,4907 | 0,4904 | 0,8109 |
| 0,97 | 0,4944 | 0,4937 | 0,4934 | 0,4931 | 0,4928 | 0,8123 |
| 0,975 | 0,4954 | 0,4947 | 0,4945 | 0,4942 | 0,4941 | 0,813 |
| 0,98 | 0,4963 | 0,4958 | 0,4956 | 0,4954 | 0,4952 | 0,8137 |
| 0,985 | 0,4972 | 0,4969 | 0,4967 | 0,4965 | 0,4964 | 0,8144 |
| 0,99 | 0,4981 | 0,4979 | 0,4978 | 0,4977 | 0,4976 | 0,8151 |

Lage des Maximums: r zwischen m und 1,45 m (im fast leeren Kern) fuer 120 von 125 Zeilen; nur m = 2 bei
omega^2 = 0,60 und 0,625 sowie m = 3, 5, 8 bei 0,625 haben es knapp innerhalb des Rings (r = 0,83 bis 0,99 R_max).
Bild: lauf-69/bild_b_vE.png (die waagrechten Linienstuecke links von r ~ 0,1 sind ein Zeichenartefakt der log-Achse
bei r = 0).

### 3.5 Teil B, beschreibend: v_E an der Ringmitte R_max / Maximum im energietragenden Bereich (T^00 >= 1 % des Maximums)

| omega^2 | m = 1 | m = 2 | m = 3 | m = 5 | m = 8 |
|---|---|---|---|---|---|
| 0,52 | 0,096 / 0,393 | 0,138 / 0,297 | 0,157 / 0,259 | 0,174 / 0,233 | 0,184 / 0,219 |
| 0,55 | 0,229 / 0,409 | 0,274 / 0,374 | 0,288 / 0,336 | 0,296 / 0,321 | 0,299 / 0,313 |
| 0,575 | 0,294 / 0,423 | 0,334 / 0,393 | 0,345 / 0,375 | 0,352 / 0,366 | 0,354 / 0,361 |
| 0,6 | 0,33 / 0,433 | 0,367 / 0,403 | 0,377 / 0,396 | 0,383 / 0,391 | 0,385 / 0,388 |
| 0,625 | 0,348 / 0,44 | 0,381 / 0,409 | 0,39 / 0,404 | 0,396 / 0,401 | 0,398 / 0,4 |
| 0,65 | 0,353 / 0,444 | 0,384 / 0,416 | 0,393 / 0,404 | 0,398 / 0,403 | 0,4 / 0,402 |
| 0,675 | 0,352 / 0,448 | 0,381 / 0,423 | 0,389 / 0,399 | 0,394 / 0,398 | 0,396 / 0,397 |
| 0,7 | 0,345 / 0,451 | 0,372 / 0,43 | 0,38 / 0,403 | 0,385 / 0,388 | 0,387 / 0,388 |
| 0,725 | 0,335 / 0,455 | 0,361 / 0,436 | 0,368 / 0,407 | 0,373 / 0,376 | 0,374 / 0,376 |
| 0,75 | 0,322 / 0,458 | 0,346 / 0,443 | 0,353 / 0,409 | 0,358 / 0,361 | 0,359 / 0,361 |
| 0,775 | 0,307 / 0,462 | 0,33 / 0,449 | 0,337 / 0,409 | 0,341 / 0,344 | 0,342 / 0,343 |
| 0,8 | 0,291 / 0,466 | 0,311 / 0,455 | 0,318 / 0,406 | 0,322 / 0,332 | 0,323 / 0,324 |
| 0,825 | 0,272 / 0,47 | 0,291 / 0,461 | 0,297 / 0,401 | 0,301 / 0,324 | 0,302 / 0,304 |
| 0,85 | 0,251 / 0,474 | 0,269 / 0,466 | 0,275 / 0,391 | 0,278 / 0,313 | 0,279 / 0,281 |
| 0,875 | 0,229 / 0,478 | 0,245 / 0,465 | 0,25 / 0,377 | 0,253 / 0,299 | 0,254 / 0,261 |
| 0,9 | 0,204 / 0,482 | 0,219 / 0,456 | 0,223 / 0,356 | 0,226 / 0,279 | 0,227 / 0,243 |
| 0,92 | 0,182 / 0,485 | 0,195 / 0,439 | 0,199 / 0,333 | 0,201 / 0,258 | 0,202 / 0,224 |
| 0,94 | 0,157 / 0,489 | 0,168 / 0,41 | 0,172 / 0,301 | 0,174 / 0,231 | 0,175 / 0,2 |
| 0,95 | 0,143 / 0,491 | 0,153 / 0,389 | 0,156 / 0,281 | 0,158 / 0,214 | 0,159 / 0,185 |
| 0,96 | 0,128 / 0,493 | 0,137 / 0,361 | 0,14 / 0,257 | 0,141 / 0,195 | 0,142 / 0,168 |
| 0,97 | 0,11 / 0,494 | 0,118 / 0,325 | 0,121 / 0,228 | 0,122 / 0,172 | 0,123 / 0,148 |
| 0,975 | 0,101 / 0,495 | 0,108 / 0,303 | 0,11 / 0,21 | 0,111 / 0,158 | 0,112 / 0,136 |
| 0,98 | 0,09 / 0,496 | 0,096 / 0,276 | 0,098 / 0,19 | 0,1 / 0,142 | 0,1 / 0,122 |
| 0,985 | 0,078 / 0,497 | 0,083 / 0,243 | 0,085 / 0,167 | 0,086 / 0,124 | 0,087 / 0,107 |
| 0,99 | 0,063 / 0,498 | 0,068 / 0,202 | 0,069 / 0,137 | 0,07 / 0,102 | 0,071 / 0,088 |

- Ringwert v_E(R_max) gegen Kartenschaetzung m/(R_max omega): Abweichung hoechstens 2,5 % ueber alle 125 Zeilen.
  Inneres Maximum am Ring je m bei omega^2 = 0,65: 0,353 (m = 1), 0,384 (2), 0,393 (3), 0,398 (5), 0,400 (8).
- Bei m = 1 ist der Kern selbst energietragend, daher sind dort beide Spalten des Maximums gleich dem unbeschraenkten
  Maximum.

## 4. Kontrollen

- **A0 je Lauf:** Energiefehler bis t_c (fein / grob) siehe Tabelle 3.1. Ueber den ganzen Lauf hoechstens 2,4e-8
  (fein). max |T^0r|/T^00 <= 1 in allen Laeufen. Die Werte 1,0 (d = 2, R0 = 40) bzw. 1 - 1e-11 entstehen im fast leeren
  Aussenfeld an der vordersten Strahlungsfront (T^00 ~ 1e-23 bis 1e-25), wo eine reine laufende Welle
  |T^0r| = T^00 hat. Die Ungleichung ist dort eine Rechenidentitaet
  (|ab| <= (a^2 + b^2)/2 bei V >= 0) [M]; die Kontrolle prueft also den Code, nicht die Physik.
- **Anfangsenergie gegen Duennwand:** d = 2, R0 = 80: 473,9074 gegen 2 pi sigma R0 = 473,9075. d = 3, R0 = 40:
  18 963,9 gegen 4 pi sigma R0^2 = 18 956,3 (+0,04 %, Kruemmung).
- **Konvergenz Teil A (fein gegen grob):** t_c auf 3e-6 gleich; v bei R0/2, R0/4, R0/10 auf hoechstens 4,4e-4; groesste
  Wandschnelle mit R >= 2 auf 4e-4; Musterschnelle auf 0,5 %; Nachlauf d = 2, R0 = 20: E(r < 10) und Frequenz auf
  2e-3 bzw. 6e-8; d = 3, R0 = 20: auf 5e-5 bzw. 1,5e-6. Kein Urteil aendert sich auf dem groben Gitter (auswertung.json, Feld "grob").
- **CUDA-Graph gegen direkte Rechnung** (Rauchlauf R0 = 10): Zusammenfassung bitgleich.
- **B0, RG-1-Anschluss:** Q und E aller 125 Zeilen gleich RG-1 bis 4,4e-16 (h0 = 0,005 gegen lauf-lokal/h0005 und
  h0 = 0,01 gegen lauf-lokal/h001). Das ist ein Nachbau mit demselben Code auf anderer Maschine, keine unabhaengige
  Rechnung.
- **B0, J = m Q auf dem kartesischen Gitter** (20 Zeilen): |J/(mQ) - 1| <= 6,7e-16; Q und E auf dem Gitter gegen
  radial <= 2,7e-13; Rest der 2D-Feldgleichung <= 1,2e-7.
- **v_E-Formel auf dem Gitter:** |T^0i|/T^00 aus spektralen Ableitungen gegen das radiale Maximum (beide nur wo
  |psi|^2 >= 1e-6 max): Abweichung hoechstens 2,2e-4 absolut (4,9e-4 relativ). Faktor 2 und m in der Formel stimmen.
- **Konvergenz Teil B (h0 = 0,01 gegen 0,005):** vE_max auf hoechstens 2,9e-5; Q auf 3,0e-7, E auf 2,9e-7. Kein Urteil
  aendert sich.
- **B1 ist eine Identitaet** [M]: v_E <= omega/sqrt(omega^2 + 1/2) gilt fuer jedes f, weil U(S) >= S/2. Gemessen:
  v_E hoechstens 61,1 % der Schranke (Abstand mindestens 0,305).
- **Hashes (sha256):**
  - PLAN.md und PLAN.md.eingefroren-20261003-210956: df11f3b628aadfc0a560a5702b83b2ab157ae84750fd8d1d30e936e078767529
  - code/peitsche_a.py: 4fdb87488e0034ce26f5aed58efed624b9c74dde5b4c6b7c6485590b92253e82
  - code/peitsche_b.py: 84f50ec4c46723800d36851a5a5d826134aebd9c73b015022a175531843eb7bd
  - code/auswertung.py: 3e71a05ec206e28ebe46c12c2e937cf74fc73959fa68a9b8b41e8d0c9d9af77c
  - code/regge2d.py (= RUNDE-06/regge/regge2d.py): 7e7f666793b956fe8a1b495ba254ee872d97f8780306f42a671dca0ebd892608
  - nach dem Einfrieren: code/nachauswertung.py: 2bea845cfb55f152a00e233f8fe19b93aa63e297d8291e835b7f15b2c918f306
  - Dieselben Hashes auf der .69 (/home/fmh/fmhc-physics-remote/runde35-peitsche/code/) vor der Auswertung geprueft.
- **Zeiten (date):** Start 20:48:23 CEST; Rauchlaeufe 18:59 bis 19:09 UTC; Plan eingefroren 21:09:56 CEST; Hauptlaeufe
  19:10:11 bis 19:29:39 UTC (21:10 bis 21:30 CEST); Auswertung 19:29:47 UTC; letzte inhaltliche Aenderung an ERGEBNIS.md vor 21:32:45 CEST (date).
  Zeitbox 120 min eingehalten (gut 45 min).

## 5. Selbstanzeigen

- **Plan nach den Rauchlaeufen.** Erlaubt; alles Gesehene steht in PLAN.md, Abschnitt R. Das A4-Fenster +-1 stand
  schon in der ersten, vor allen Rauchlaeufen hochgeladenen Fassung von peitsche_a.py. Nach den Rauchlaeufen festgelegt
  habe ich: A4 muss in allen fuenf Laeufen gelten; B3 heisst "Maximum strikt im Innern". Bei B3 war nach dem Rauchlauf
  schon sichtbar, dass das Kernmaximum fuer m = 3 und 8 bei 0,99 liegt; die Lesart "nur nicht am oberen Rand" gaebe
  dasselbe Urteil.
- **Code vor dem Einfrieren nach den Rauchlaeufen geaendert:** CUDA-Graph mit index_select statt Tensorindex (der
  erste Graph-Versuch brach ab), dazu beschreibende Spalten (Verhaeltnis im energietragenden Bereich, gewichtetes
  Mittel, v_E am Ring und im tragenden Bereich). Nach dem Einfrieren keine Aenderung an Plan, peitsche_a.py,
  peitsche_b.py, auswertung.py, regge2d.py (Hashes in Abschnitt 4).
- **Nach dem Einfrieren neu:** code/nachauswertung.py (Tabelle 3.3, "erstes v > 1", Bilder). Rein beschreibend, kein
  Urteil haengt daran.
- **Abweichungen von der Karte:**
  - Aufloesung in d = 3 mit der d = 3-Dicke sqrt(2) (R/R0)^2, strenger als die Kartenformel.
  - Nachlauf bis t_c + 500 nur fuer R0 = 20, nicht fuer R0 = 40 und 80.
  - "jederzeit" heisst an allen Ausgabezeiten (Abstand ~0,02), nicht nach jedem Zeitschritt.
  - A1 mit 1,3110288 R0 statt 1,311 R0 (Unterschied 2e-5).
  - Die Kartenzahl 0,814 fuer die Schranke bei omega^2 = 0,99 ist 0,8151; B1 nutzt die Formel.
- **Musterschnelle per Definition:** R = 0, sobald phi_0 >= 0. Die Fensterwerte 29 bis 162 sind daher Sprungschnellen
  beim Verschwinden und Wiederauftauchen der Nullstelle. Bei d = 3, R0 = 40 stammt 162 aus einem Paar nach t_c, in dem
  der Ursprung positiv wird, waehrend eine Schalen-Nullstelle bei R = 3,28 noch besteht. Das ist regelkonform, aber
  kein "Lauf" einer Nullstelle. Unabhaengig davon liegen die zentrale Differenz vor t_c (2,35 bis 3,13) und die
  Momentanschnelle (3,7 bis 10,8) ueber 1, und Tabelle 3.3 zeigt v > 1 schon ab R ~ 7.
- **A3 und die Karte:** Die Karte nennt die Nullstellenschnelle "Wandschnelle". Der A3-Wert 1,025 liegt ueber 1; er
  misst ab R ~ 7 (R0 = 80) das Muster, nicht die Wand. Das Urteil folgt der Regel (> 0,99).
- **Ablauf:**
  - Zweimal startete eine Kette nicht (cd lief in der Hintergrund-Subshell): beim Teil-B-Rauchlauf und bei der
    Teil-B-Hauptkette. Beide wurden sofort richtig neu gestartet; dabei wurde nichts gerechnet.
  - Einmal startete ich auf der .69 einen Interpreter ausserhalb des Starters: `python -c "import matplotlib"`
    (~19:14 UTC), nur eine Importprobe.
  - Lokal benutzte ich neben jq, ssh, scp, sha256sum und date auch cp, mkdir, rm, ls, du, cat, grep und head, dazu
    einmal sed (Dezimalpunkt zu Komma in Tabellen). Kein Interpreter.
- **Ablage:** Die Rauchausgaben liegen in peitsche-1/rauch-69/ (ohne den Codepfad-Test ausw_test), nicht in lauf-69/.
- **d = 3, R0 = 20, fein, in zwei Abschnitten:** Der Lauf hielt wie vorgesehen nach 480 s mit einem Zwischenstand an
  (checkpoint.npz bei t = 334,66). Ich setzte ihn mit --fortsetzen im selben Ordner fort; die Ausgabe des zweiten
  Abschnitts steht in a_d3_R20_fein_teil2.out. Der Zwischenstand wird verlustfrei in float64 gespeichert.

## 6. Einfach gesagt

Wenn ein Ring aus einer Feldwand in sich zusammenfaellt, wird er immer schneller, wie das Ende einer Peitsche, und
kommt der Lichtgeschwindigkeit sehr nahe; die Energie selbst ist dabei nie schneller als Licht. Der Punkt, an dem das
Feld durch null geht, ist dagegen nur ein Muster, wie der Kreuzungspunkt einer Schere: Er laeuft kurz vor dem Ende
sogar schneller als Licht, ohne dass etwas Echtes so schnell transportiert wird. Nach dem Knall bleibt in zwei
Dimensionen kein Klumpen uebrig, in drei Dimensionen ein kleiner schwingender Rest. In drehenden Q-Baellen fliesst
Energie hoechstens halb so schnell wie Licht, im eigentlichen Ring sogar nur mit etwa 40 Prozent der
Lichtgeschwindigkeit. Das alles sind Computerrechnungen in Modellen, keine Messungen.
