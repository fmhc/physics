# BILDUNG-2 (Runde 22): Ergebnis

Code-Agent (Claude, Anthropic), Auftrag der Leitung claude-primary. Beginn 2026-10-02 19:30:35 CEST (date).
Rauchlauf 19:42:44 bis 19:44:00 CEST. Plan eingefroren 19:46:44 CEST (PLAN.md.eingefroren-20261002-194644), vor jedem
echten Lauf. Laeufe 19:46:52 bis 20:01:39 CEST auf der .69 (Uhr dort UTC). Ergebnis geschrieben ab 20:02:52 CEST, Ende
der Bearbeitung in der letzten Zeile. Explorativ (v3), Deutungen [H, im Modell].

## 1. Ergebnis zuerst

1. **Arm A (Groesse): C1 nicht eingetroffen.** Der grosse Klumpen (omega^2 0,52, Q 1421) ist bei T = 500 auf
   keinem Gitter "auf", auch nicht bei T = 1000.
   - Der Ball behaelt 90,5 % der Ladung; 8,9 % verlassen die Box als Strahlung. E/Q liegt am Ende nur 0,5 % ueber der
     Familie.
   - Er atmet aber bis T = 1000 stark (u 0,02 bis 0,05). Die gemessene omega von 0,696 bis 0,703 liegt unter dem
     Familienwert 0,722. Das Urteil lautet deshalb "ausserhalb" (omega^2 unter dem Tabellenbeginn 0,51).
   - Der exakte Familienball KA ist im selben Aufbau zu allen 12 Zeiten "auf" (u <= 5e-5). Der Klassifikator kann
     es dort also.
2. **Arm C (Verschmelzen): C3 eingetroffen, C4 nicht eingetroffen.**
   - Die beiden Klumpen trennen sich nie. Die Gebietszahl ist in allen 191 Proben 1, auf beiden Schwellen und Gittern;
     schon bei t = 0 verbindet sie eine Bruecke (S 0,611).
   - Kein Fenster zeigt zwei Tropfen, keiner war also einzeln "auf".
   - Das Gebilde (Q 2,11 Q_F) bleibt bis T = 1000 "unentschieden" bzw. "nicht rund", mit u 0,01 bis 0,05 und einer
     Formschwingung (rmax/R_A 1,00 bis 1,53). Bei T = 1000 liegt es 0,9 % (E/Q) bzw. -25 % (dQ*) neben der Familie.
3. **Arm B (Bad): C0 nicht eingetroffen (8 von 12), C2 deshalb offen.** Grund ist eine Drift, nicht der Klassifikator.
   - Das Bad stoesst die Baelle an. B0 und B laufen mit v = 0,021 in -x und sind bei T = 500 und 1000 weiter als 5 vom
     Start entfernt (x = -9,5 bzw. -20). Die eingefrorene Ballsuche (Radius 5) meldet dort "kein Tropfen".
   - **Nachtraeglich, entscheidet nichts:** Der Klassifikator selbst nennt genau diese Tropfen zu T = 500 und 1000
     "auf" und rund, mit u <= 5e-5. Zu T = 50 bis 250 sind B0 und B ohnehin "auf". Mit "naechster Tropfen" statt
     "Radius 5" waeren C0 und C2 eingetroffen.
   - Das Bad ist schwach und durch den Absorber fluechtig (Plan, Abschnitt 4). Im Kreis r <= 32 ist bei t = 100 noch
     5 % der Badladung, bei t = 200 noch 0,4 %.
4. **Bedeutung nach Karte (mechanisch, beide Zeilen gelten):**
   - C1 nicht eingetroffen: Grosse, duennwandige Klumpen erreichen die Familie langsamer oder gar nicht.
   - C0 nicht eingetroffen: Der Klassifikator taugt im Bad nicht; Arm B bleibt offen.
   - Die zweite Zeile trifft den Grund nicht (Punkt 3). Wie das zu werten ist, entscheidet die Leitung.
   - Die Zeile "C1 und C2 eingetroffen, C4 nicht: lag am Verschmelzen" gilt nicht, weil C1 gescheitert ist.
5. **Beschreibend [H, nicht Karte]:** Groesse und Verschmelzen fuehren beide zu langlebigen Schwingungszustaenden, die
   bis T = 1000 nicht "auf" sind. Das schwache, kurze Bad stoert die Bildung nicht erkennbar; es stoesst den Ball nur
   an. Fuer das "nie auf" in KF-5 bleiben damit Groesse und Verschmelzen als Kandidaten, nicht nur das Verschmelzen.
   - Pruefungen: Box bestanden in allen 12 Laeufen, B0 knapp (24,0 bei Grenze 24). L3: 72 von 72 Klassen gleich.

## 2. Box- und K-Pruefungen (B0)

**K-Pruefung bei t = 0** (Gate; alle bestanden, beide Gitter):

| Teil | Q (rel) | weitere Werte | Urteil |
|---|---|---|---|
| Klumpen (i) 0,60 (wie BILDUNG-1, fuer B und C) | 66,616119 (0 bis 2e-16) | r_rms = s = 3,074146 (rel <= 2e-16), E/Q 0,85932, S_max 1,448 | bestanden |
| Klumpen (i) 0,52 (Arm A) | 1421,452286 (-1e-12) | r_rms = s = 12,532245 (rel -1e-11), E/Q 0,82694 (Familie 0,73583), S_max 1,998 | bestanden |
| Ball 0,60 (B0) | 66,616124 (+7,1e-8) | E rel +6,6e-8, omega_gitter rel -5e-11 / -2e-11, r_rms gegen r_ladung -3,5e-7 | bestanden |
| Ball 0,52 (KA) | 1421,456420 (+2,9e-6) | E rel +2,9e-6, omega_gitter rel -6e-11 / -3e-11, r_rms gegen r_ladung +1,4e-6 | bestanden |
| Bad (B, B0, BAD) | 13,323224 = 0,2 Q_F (rel -1e-16) | 696 Moden, E/Q 1,2439, S_max 0,00483 | bestanden |
| C, Summe beider Klumpen | 147,274813 = 2 Q_F (1 + e^{-9/4}) (rel 0) | S in der Mitte 0,61062 (= analytisch) | bestanden |

- Kreuzterm Ball/Bad bei t = 0: Q_box(B0) 80,4951, Q_box(B) 80,4933 statt 79,9393 (+0,55, rel +6,9e-3).
- Absorber Box 96: in allen vier bc-Laeufen bitgleich mit bildung1.absorber (Pruefung im Lauf, sonst Abbruch).

**K-Arm B0 (Karte; exakter Ball 0,60 im Bad):**
- Zu T = 50, 100, 200, 250 auf beiden Gittern "auf" und rund.
  - rmax/R_A 1,02 bis 1,04; dQ* -0,7 bis -0,3 %; E/Q-Abstand +0,28 % (T 50) bis 0; u 1,3e-4 bis 8,4e-4.
  - Q/Q_F 1,016 (T 50) bis 1,010: Der Ball nimmt etwa 1 % Ladung aus dem Bad auf.
- Zu T = 500 und 1000 "kein Tropfen" nach der eingefrorenen Ballsuche (Radius 5 um den Start). Der Ball ist bei
  x0 = -9,51 / -19,97 (grob und fein gleich auf 0,01).
- Er driftet von Anfang an: v gemessen 0,0201 bis 0,0213 in den Fenstern T = 50 bis 250 (danach ohne Ball-Eintrag;
  der Ort waechst weiter linear). Ohne Bad war v = 0 (BILDUNG-1).
- Nachtraeglich: Die Klassenliste aller Fenstertropfen nennt diesen Ball zu T = 500 und 1000 "auf" und rund.
  - omega 0,77414 bis 0,77419, u 2,7e-5 bis 4,8e-5, Q-Schwankung <= 7e-5, Q_net 67,28 (beide Gitter, T = 500 und 1000).
  - Dasselbe gilt fuer B (x0 -9,46 / -19,86, omega 0,77439 bis 0,77443, u <= 3,9e-5).

**Box-Pruefung** (Maske S >= 0,6 zu allen Diagnosezeiten innerhalb max(|x|, |y|) <= innen - 8):

| Lauf | Maske 0,6: max-Norm max (Grenze) | Maske 0,2 max | Q_box(1000)/Q0 | Rahmen max / Q0 | Urteil |
|---|---|---|---|---|---|
| grob / fein A | 21,25 / 21,25 (40) | 22,25 / 22,375 | 0,9112 / 0,9114 | 1,3e-2 | bestanden |
| grob / fein KA | 17 / 17,125 (40) | 18,25 / 18,375 | 1,000000 | 1,7e-10 | bestanden |
| grob / fein B0 | **24 / 24 (24)** | 25 / 25,125 | 0,8361 | 9,7e-2 (Bad bei t = 0) | bestanden, genau an der Grenze |
| grob / fein B | 23,75 / 23,875 (24) | 25 | 0,8302 | 9,7e-2 | bestanden |
| grob / fein BAD | keine Maske | keine Maske | 0,00005 | 0,58 (t = 0) | bestanden |
| grob / fein C | 7,5 / 7,5 (24) | 9 / 9,125 | 0,9579 | 3,7e-3 | bestanden |

- B0 und B erreichen die Grenze nur wegen der Drift. Bei t = 1000 liegt der Maskenrand von B0 bei max-Norm 24,0.
- **Bad allein (BAD, grob):**

  | t | 0 | 50 | 100 | 150 | 200 | 300 | 500 | 1000 |
  |---|---|---|---|---|---|---|---|---|
  | Q_box | 1 | 0,297 | 0,108 | 0,024 | 0,008 | 0,003 | 0,001 | 0,0000 |
  | im Kreis r <= 32 | 0,322 | 0,216 | 0,050 | 0,011 | 0,004 | 0,002 | 0,0004 | 0 |

  Anteile der Anfangsladung des Bads. Fein gleich (Q_box Ende 5,2e-5).

## 3. Tabelle je Arm, Gitter und Zeit (S0 = 0,3, Hauptauswertung)

Legende:
- Werte aus dem Messfenster [T - 40, T] des Runde-6-Klassifikators.
- **N** = Zahl der Fenstertropfen.
- **Q/Q_F** = Q_net des Balls / Q_F des Familienpunkts (Arm A, KA: 1421,45; B, B0, C: 66,616).
- **Ring/Q_F** = Q(r <= 12, bei Box 128 r <= 24) am Fensterbeginn / Q_F.
- **E/Q** mit dem Familienwert beim selben Q in Klammern.
- **dQ*** = Q / Q_fam(omega) - 1. **E/Q-Abst.** = (E/Q) / (E/Q)_fam(Q) - 1. **omega-Abst.** = omega - omega_fam(Q).
- "-" bei dQ* heisst, omega liegt ausserhalb der Familientabelle.
- Zahlen per jq gerundet (hilfs/tabelle.jq); Dezimalpunkte aus jq.
- BAD hat zu allen Zeiten "kein Tropfen" (N = 0) und fehlt in der Tabelle.

| Fall | Gitter | T | Urteil | N | rund, rmax/R_A | Q/Q_F | Ring/Q_F | omega +- u | E/Q (fam) | dQ* | E/Q-Abst. | omega-Abst. | Q-Schwankung | v |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | grob | 50 | ausserhalb | 1 | ja 1 | 0.9517 | 0.9779 | 0.67017 +- 0.08312 | 0.8085 (0.7365) | - | 9.78 % | -0.0513 | 2.9 % | 0 |
| A | fein | 50 | ausserhalb | 1 | ja 1 | 0.9515 | 0.978 | 0.67016 +- 0.08318 | 0.8085 (0.7365) | - | 9.78 % | -0.0513 | 2.9 % | 0 |
| A | grob | 100 | gestoert | 2 | ja 1.244 | 0.3437 | 0.9802 | 0.72011 +- 0.01281 | 0.7971 (0.7567) | -70.8 % | 5.34 % | -0.0109 | 193.6 % | 0.0223 |
| A | fein | 100 | gestoert | 2 | ja 0.998 | 0.1627 | 0.9802 | 0.79201 +- 0.04325 | 0.8934 (0.7807) | 418.1 % | 14.44 % | 0.0499 | 131.1 % | 0.0538 |
| A | grob | 200 | unentschieden | 1 | ja 1 | 0.9036 | 0.9081 | 0.73312 +- 0.04598 | 0.7395 (0.7372) | 208.2 % | 0.31 % | 0.0113 | 0.4 % | 0 |
| A | fein | 200 | unentschieden | 1 | ja 1 | 0.9037 | 0.9082 | 0.73296 +- 0.04651 | 0.7395 (0.7372) | 204.4 % | 0.31 % | 0.0112 | 0.4 % | 0 |
| A | grob | 250 | ausserhalb | 1 | ja 1 | 0.9048 | 0.9073 | 0.70252 +- 0.04596 | 0.7412 (0.7372) | - | 0.54 % | -0.0192 | 0.2 % | 0 |
| A | fein | 250 | ausserhalb | 1 | ja 1 | 0.9049 | 0.9074 | 0.70231 +- 0.04579 | 0.7412 (0.7372) | - | 0.54 % | -0.0195 | 0.2 % | 0 |
| A | grob | 500 | ausserhalb | 1 | ja 1 | 0.9053 | 0.9059 | 0.69603 +- 0.0212 | 0.741 (0.7372) | - | 0.52 % | -0.0257 | 0.1 % | 0 |
| A | fein | 500 | ausserhalb | 1 | ja 1.001 | 0.9055 | 0.906 | 0.69587 +- 0.02051 | 0.741 (0.7372) | - | 0.52 % | -0.0259 | 0.1 % | 0 |
| A | grob | 1000 | ausserhalb | 1 | ja 1.002 | 0.9051 | 0.9057 | 0.7031 +- 0.03965 | 0.7406 (0.7372) | - | 0.47 % | -0.0187 | 0.1 % | 0 |
| A | fein | 1000 | ausserhalb | 1 | ja 1.004 | 0.9053 | 0.9058 | 0.70345 +- 0.04102 | 0.7406 (0.7372) | - | 0.47 % | -0.0183 | 0.1 % | 0 |
| KA | grob | 50 | auf | 1 | ja 1 | 1 | 1 | 0.72112 +- 1e-05 | 0.7358 (0.7358) | 0.1 % | -0 % | 0 | 0 % | 0 |
| KA | fein | 50 | auf | 1 | ja 1 | 1 | 1 | 0.72111 +- 0 | 0.7358 (0.7358) | 0 % | -0 % | 0 | 0 % | 0 |
| KA | grob | 100 | auf | 1 | ja 1 | 1 | 1 | 0.72114 +- 4e-05 | 0.7358 (0.7358) | 0.5 % | -0 % | 0 | 0 % | 0 |
| KA | fein | 100 | auf | 1 | ja 1 | 1 | 1 | 0.72112 +- 1e-05 | 0.7358 (0.7358) | 0.1 % | -0 % | 0 | 0 % | 0 |
| KA | grob | 200 | auf | 1 | ja 1 | 1 | 1 | 0.72113 +- 4e-05 | 0.7358 (0.7358) | 0.3 % | -0 % | 0 | 0 % | 0 |
| KA | fein | 200 | auf | 1 | ja 1 | 1 | 1 | 0.72111 +- 1e-05 | 0.7358 (0.7358) | 0.1 % | -0 % | 0 | 0 % | 0 |
| KA | grob | 250 | auf | 1 | ja 1 | 1 | 1 | 0.72112 +- 1e-05 | 0.7358 (0.7358) | 0.1 % | -0 % | 0 | 0 % | 0 |
| KA | fein | 250 | auf | 1 | ja 1 | 1 | 1 | 0.72111 +- 0 | 0.7358 (0.7358) | 0 % | -0 % | 0 | 0 % | 0 |
| KA | grob | 500 | auf | 1 | ja 1 | 1 | 1 | 0.72114 +- 4e-05 | 0.7358 (0.7358) | 0.4 % | -0 % | 0 | 0 % | 0 |
| KA | fein | 500 | auf | 1 | ja 1 | 1 | 1 | 0.72112 +- 1e-05 | 0.7358 (0.7358) | 0.1 % | -0 % | 0 | 0 % | 0 |
| KA | grob | 1000 | auf | 1 | ja 1 | 1 | 1 | 0.72113 +- 5e-05 | 0.7358 (0.7358) | 0.4 % | -0 % | 0 | 0 % | 0 |
| KA | fein | 1000 | auf | 1 | ja 1 | 1 | 1 | 0.72112 +- 1e-05 | 0.7358 (0.7358) | 0.1 % | -0 % | 0 | 0 % | 0 |
| B0 | grob | 50 | auf | 1 | ja 1.034 | 1.0155 | 1.0182 | 0.77381 +- 0.00084 | 0.8498 (0.8474) | -0.6 % | 0.28 % | -0.0002 | 0.2 % | 0.0201 |
| B0 | fein | 50 | auf | 1 | ja 1.037 | 1.0155 | 1.0182 | 0.77379 +- 0.00083 | 0.8498 (0.8474) | -0.7 % | 0.28 % | -0.0002 | 0.2 % | 0.0202 |
| B0 | grob | 100 | auf | 1 | ja 1.036 | 1.0117 | 1.0171 | 0.77405 +- 0.00013 | 0.8482 (0.8477) | -0.3 % | 0.06 % | -0.0001 | 0.3 % | 0.0213 |
| B0 | fein | 100 | auf | 1 | ja 1.042 | 1.0117 | 1.0171 | 0.77403 +- 0.00013 | 0.8482 (0.8477) | -0.4 % | 0.06 % | -0.0001 | 0.3 % | 0.0212 |
| B0 | grob | 200 | auf | 1 | ja 1.025 | 1.0101 | 1.0105 | 0.77411 +- 0.00059 | 0.8478 (0.8478) | -0.3 % | -0 % | -0.0001 | 0 % | 0.0207 |
| B0 | fein | 200 | auf | 1 | ja 1.029 | 1.0101 | 1.0105 | 0.77409 +- 0.00059 | 0.8478 (0.8478) | -0.4 % | -0 % | -0.0001 | 0 % | 0.0207 |
| B0 | grob | 250 | auf | 1 | ja 1.02 | 1.0101 | 1.0102 | 0.77413 +- 0.00048 | 0.8478 (0.8478) | -0.3 % | -0 % | -0.0001 | 0 % | 0.0207 |
| B0 | fein | 250 | auf | 1 | ja 1.025 | 1.0101 | 1.0102 | 0.77411 +- 0.00048 | 0.8478 (0.8478) | -0.3 % | -0 % | -0.0001 | 0 % | 0.0207 |
| B0 | grob | 500 | kein Tropfen | 1 | - - | - | 0.848 | - +- - | - (-) | - | - | - | - | - |
| B0 | fein | 500 | kein Tropfen | 1 | - - | - | 0.8506 | - +- - | - (-) | - | - | - | - | - |
| B0 | grob | 1000 | kein Tropfen | 1 | - - | - | 0.0001 | - +- - | - (-) | - | - | - | - | - |
| B0 | fein | 1000 | kein Tropfen | 1 | - - | - | 0.0001 | - +- - | - (-) | - | - | - | - | - |
| B | grob | 50 | auf | 1 | ja 1.033 | 1.0086 | 1.018 | 0.77396 +- 0.00046 | 0.8508 (0.8479) | -0.9 % | 0.34 % | -0.0003 | 0.5 % | 0.0201 |
| B | fein | 50 | auf | 1 | ja 1.036 | 1.0086 | 1.018 | 0.77394 +- 0.00047 | 0.8508 (0.8479) | -0.9 % | 0.34 % | -0.0003 | 0.5 % | 0.0201 |
| B | grob | 100 | auf | 1 | ja 1.04 | 1.0046 | 1.01 | 0.77429 +- 0.00012 | 0.8488 (0.8482) | -0.4 % | 0.06 % | -0.0001 | 0.3 % | 0.0209 |
| B | fein | 100 | auf | 1 | ja 1.041 | 1.0047 | 1.01 | 0.77426 +- 9e-05 | 0.8487 (0.8482) | -0.4 % | 0.06 % | -0.0002 | 0.3 % | 0.0212 |
| B | grob | 200 | auf | 1 | ja 1.026 | 1.003 | 1.0034 | 0.77437 +- 0.00058 | 0.8483 (0.8483) | -0.3 % | 0 % | -0.0001 | 0 % | 0.0206 |
| B | fein | 200 | auf | 1 | ja 1.028 | 1.003 | 1.0034 | 0.77435 +- 0.00059 | 0.8483 (0.8483) | -0.4 % | 0 % | -0.0001 | 0 % | 0.0206 |
| B | grob | 250 | auf | 1 | ja 1.023 | 1.003 | 1.0031 | 0.77438 +- 0.00052 | 0.8483 (0.8483) | -0.3 % | 0 % | -0.0001 | 0 % | 0.0207 |
| B | fein | 250 | auf | 1 | ja 1.032 | 1.003 | 1.0031 | 0.77437 +- 0.00051 | 0.8483 (0.8483) | -0.3 % | 0 % | -0.0001 | 0 % | 0.0206 |
| B | grob | 500 | kein Tropfen | 1 | - - | - | 0.85 | - +- - | - (-) | - | - | - | - | - |
| B | fein | 500 | kein Tropfen | 1 | - - | - | 0.8526 | - +- - | - (-) | - | - | - | - | - |
| B | grob | 1000 | kein Tropfen | 1 | - - | - | 0.0002 | - +- - | - (-) | - | - | - | - | - |
| B | fein | 1000 | kein Tropfen | 1 | - - | - | 0.0002 | - +- - | - (-) | - | - | - | - | - |
| C | grob | 50 | nicht rund | 1 | nein 1.445 | 2.17 | 2.2067 | 0.74493 +- 0.04696 | 0.8197 (0.8013) | -27.4 % | 2.3 % | -0.0069 | 2.5 % | 0 |
| C | fein | 50 | nicht rund | 1 | nein 1.446 | 2.1699 | 2.2068 | 0.74491 +- 0.04703 | 0.8197 (0.8013) | -27.4 % | 2.3 % | -0.0069 | 2.5 % | 0 |
| C | grob | 100 | unentschieden | 1 | ja 1.126 | 2.1437 | 2.155 | 0.74117 +- 0.02485 | 0.8146 (0.8019) | -41.7 % | 1.59 % | -0.0109 | 0.8 % | 0 |
| C | fein | 100 | unentschieden | 1 | ja 1.129 | 2.1437 | 2.155 | 0.74114 +- 0.02481 | 0.8146 (0.8019) | -41.7 % | 1.59 % | -0.0109 | 0.8 % | 0 |
| C | grob | 200 | nicht rund | 1 | nein 1.338 | 2.1355 | 2.1381 | 0.743 +- 0.03691 | 0.8135 (0.8021) | -35.5 % | 1.42 % | -0.0092 | 0.4 % | 0 |
| C | fein | 200 | nicht rund | 1 | nein 1.354 | 2.1355 | 2.1381 | 0.74299 +- 0.03685 | 0.8135 (0.8021) | -35.6 % | 1.42 % | -0.0092 | 0.4 % | 0 |
| C | grob | 250 | unentschieden | 1 | ja 1.178 | 2.1327 | 2.1354 | 0.74203 +- 0.03321 | 0.8131 (0.8022) | -39 % | 1.36 % | -0.0102 | 0.3 % | 0 |
| C | fein | 250 | unentschieden | 1 | ja 1.177 | 2.1328 | 2.1355 | 0.742 +- 0.03313 | 0.8131 (0.8022) | -39.1 % | 1.36 % | -0.0102 | 0.2 % | 0 |
| C | grob | 500 | unentschieden | 1 | ja 1.013 | 2.1232 | 2.1262 | 0.74217 +- 0.0106 | 0.8118 (0.8024) | -38.8 % | 1.17 % | -0.0101 | 0.3 % | 0 |
| C | fein | 500 | unentschieden | 1 | ja 1.014 | 2.1232 | 2.1262 | 0.74217 +- 0.01041 | 0.8118 (0.8024) | -38.8 % | 1.17 % | -0.0101 | 0.3 % | 0 |
| C | grob | 1000 | unentschieden | 1 | ja 1.088 | 2.1057 | 2.1077 | 0.74636 +- 0.02545 | 0.8098 (0.8028) | -24.5 % | 0.88 % | -0.0061 | 0.2 % | 0 |
| C | fein | 1000 | unentschieden | 1 | ja 1.102 | 2.1056 | 2.1076 | 0.74634 +- 0.02541 | 0.8098 (0.8028) | -24.6 % | 0.88 % | -0.0062 | 0.2 % | 0 |

- T 50 und 200 sind fuer A, B und C beschreibend; die Karte entscheidet an 100, 250, 500, 1000 (C0 und C3: alle sechs).
- **Arm A im Verlauf** (Gebietszahl, Diagnose grob):
  - Zwischen t = 8 und 110 zerfaellt die Maske in Kern und konzentrische Ringe. Die Gebietszahl ist dann bis 3, in 79
    von 191 Proben ungleich 1; ab t = 120 immer 1. Daher kommen "gestoert" und N = 2 bei T = 100.
  - Q_box/Q0 0,997 (t 100), 0,937 (200), 0,918 (300), 0,911 (1000). Die Ladung geht als Strahlung zwischen t = 100
    und 300 weg.
  - S_max schwingt zwischen 1,0 und 1,4 (Familienball 1,019).
- **Arm C: Gebietszahl ueber die Zeit** (alle 1 bis t = 100, danach alle 10):
  - Hauptmaske 0,6 und Zusatzmaske 0,2: in allen 191 Proben genau 1 Gebiet, auf beiden Gittern. Nie 2, nie 0.
  - Das eine Gebiet ist zuerst laenglich (Doppellappen): rmax/R_A 1,64 / 1,65 bei t = 0, dann 1,30 bis 1,58. Erstmals
    rund (<= 1,3) ist es bei t = 16 (grob) bzw. 17 (fein).
  - Danach schwingt die Form zwischen rmax/R_A 1,00 und 1,53, auch nach t = 500 noch (1,00 bis 1,39 bzw. 1,41; 23
    von 51 Proben ueber 1,3).
  - "verschmolzen" (Planregel: ein Gebiet, rund, Mitte) gilt dauerhaft erst ab t_m = 990 (beide Gitter). Die letzten
    nicht runden Proben liegen bei t = 970 und 980. Siehe Selbstanzeige.
  - Schwerpunkt immer in (0, 0); v = 0.
- **Zusatz S0 = 0,1** (Schwelle 0,2, dieselben Laeufe): 70 von 72 Klassen wie bei S0 = 0,3.
  - Abweichung nur bei C, T = 200: "unentschieden" statt "nicht rund", beide Gitter.
  - Zeilen in hilfs/tabelle-s0-0.1.md.

## 4. C0 bis C4

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| C0 | K-Arm B0: exakter Ball im Bad bleibt bis T = 1000 "auf" | 60 % | **nicht eingetroffen** | 8 von 12 "auf": T 50 / 100 / 200 / 250 ja, T 500 / 1000 "kein Tropfen" auf beiden Gittern (Ball bei x0 -9,5 / -20 ausserhalb der Ballsuche, Drift v 0,021). Nachtraeglich: diese Tropfen selbst "auf", u <= 5e-5 |
| C1 | A: "auf" und rund bei T = 500, beide Gitter | 55 % | **nicht eingetroffen** | 0 von 2: "ausserhalb", omega 0,69603 / 0,69587 +- 0,021 (Familie bei diesem Q 0,7218), rund (1,000 / 1,001), Q/Q_F 0,905, E/Q-Abstand +0,52 % |
| C2 | B: "auf" und rund bei T = 500, beide Gitter (nur wertbar bei C0) | 50 % | **offen** (C0 nicht eingetroffen) | Rohausgang nicht eingetroffen: 0 von 2, "kein Tropfen" wegen der Drift (x0 -9,46). Nachtraeglich: der Tropfen selbst "auf", omega 0,77439 / 0,77441 (fein / grob), u <= 2,7e-5 |
| C3 | C: Klumpen verschmelzen (Gebietszahl 1), bevor einer "auf" ist | 55 % | **eingetroffen** | Beide Gitter: t_m = 990 nach Planregel; Gebietszahl 1 ab t = 0 (191 von 191 Proben); kein Fenster mit 2 Tropfen, kein Einzelklumpen je "auf" |
| C4 | C: verschmolzenes Gebilde bei T = 1000 "auf" und rund | 35 % | **nicht eingetroffen** | Beide Gitter "unentschieden", rund (1,088 / 1,102), omega 0,74636 / 0,74634 +- 0,025 (Familie 0,7525), dQ* -24,5 %, E/Q-Abstand +0,88 %, Q/Q_F 2,106 |

- Box-Pruefung fuer alle beteiligten Laeufe bestanden, keine Vorhersage ist deshalb "offen (Box)".
- Bedeutung mechanisch: siehe Abschnitt 1, Punkt 4.

## 5. Latten, Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Latten (v3):**
- **L1 kann scheitern:** ja. C0 und C1 sind gescheitert, C4 auch; C3 ist eingetroffen.
- **L2 Gegenprobe:** ja.
  - KA: exakter Ball bei 0,52 im A-Aufbau, 12 von 12 "auf", u <= 5e-5. Das Scheitern von A liegt am Klumpen, nicht am
    Klassifikator oder an der Box 128.
  - B0: Klassifikator im Bad "auf", solange der Ball gefunden wird. BAD: Das Bad allein erzeugt nie einen Tropfen.
  - K-Pruefungen, Absorber bitgleich mit BILDUNG-1, zwei Schwellen, zweites Ladungsmass Q(r <= R).
- **L3 Numerik:** bestanden. Grob und fein geben in 72 von 72 Paaren (Fall x T x S0) dieselbe Klasse.
  - Einzige grosse Abweichung: A bei T = 100 mit S0 = 0,3. Die Klasse ist gleich ("gestoert"), aber als Ball gilt auf
    den Gittern je ein anderes Bruchstueck der Ringphase: |Delta omega| 0,072, |Delta Q/Q_F| 0,18.
  - Alle anderen Paare: |Delta omega| <= 3,5e-4, |Delta Q/Q_F| <= 1,3e-4.
- **L4 schon bekannt:** Q-Ball-Relaxation, langsame Atemmoden grosser Q-Baelle, Verschmelzen gleichphasiger Q-Baelle
  und Brownsche Bewegung im Bad sind allgemein bekannte Phaenomene [L, nicht nachgeprueft, keine Literaturabfrage].
  Neu ist nur der Befund fuer M1 in 2D mit diesem Klassifikator.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter).

**Grenzen:**
- Je Arm ein Startzustand, ein Familienpunkt, eine Saat.
- Arm A: "auf" haengt an der omega-Messung. Bei 0,52 entsprechen 10 % in Q nur etwa 6e-4 in omega; das Atmen
  (u 0,02 bis 0,05) ist 30- bis 80-mal groesser.
  - Energetisch liegt A nahe an der Familie (E/Q +0,5 %). "Nicht auf" heisst hier "atmet noch", nicht "weit weg".
  - Ob das Atmen nach T = 1000 abklingt, ist nicht gerechnet.
- Arm B: Das Bad ist schwach (0,2 Q_F in der ganzen Box, Amplitude etwa 2,5 % des Kerns) und nach t = 150 fast weg.
  Ein dauerndes, dichtes Bad wie in KF-5 ist nicht geprueft.
- Arm C: Die Klumpen ueberlappen schon beim Start (Bruecke S 0,611, Interferenzladung +10,5 %). Ein Start mit
  getrennten Masken (groesserer Abstand) ist nicht gerechnet.
- "auf" heisst nur "Q passt zu omega" (Runde 21).

**Selbstanzeigen:**
- **Ballsuche bei Drift (C0, C2):** Die Regel "naechster Tropfen hoechstens 5 vom Start" habe ich aus BILDUNG-1
  uebernommen, ohne an einen Stoss durch das Bad zu denken.
  - Sie macht aus einem "auf"-Ball "kein Tropfen", sobald er mehr als 5 gewandert ist. Das bestimmt die Ausgaenge von
    C0 und C2.
  - Nach dem Ergebnis nicht geaendert; die Klassen der gewanderten Tropfen stehen oben nur als nachtraegliche
    Beschreibung.
- **Ursache der Drift:** Woher der Stoss kommt, ist nicht getrennt geprueft [H]. Vermutlich stammt er aus dem
  Kreuzterm von Ball und Bad beim Start (Ueberlagerung bei t = 0, Q-Kreuzterm +0,55). B0 und B laufen fast gleich
  (v 0,0201 bis 0,0213).
- **Verschmelzungsregel (C3):** Das Rund-Kriterium sollte die Startbruecke vom echten Verschmelzen trennen. Es reagiert
  aber auch auf die Formschwingung des verschmolzenen Gebildes.
  - t_m = 990 ist deshalb ein Zufall der Schwingungsphase. Waeren die Proben 990 oder 1000 nicht rund gewesen, haette
    es kein t_m gegeben; C3 waere "nicht eingetroffen" und C4 "offen" gewesen.
  - Der Ausgang von C3 stimmt mit der woertlichen Kartenfassung ueberein: Gebietszahl 1 von Anfang an, nie ein
    Einzelklumpen "auf". Die Zahl 990 hat aber keine physikalische Bedeutung.
- **Box B0 genau an der Grenze** (24,0 bei <= 24, beide Gitter). Eine Rasterzelle weiter, und C0 und C2 waeren
  "offen (Box)" gewesen.
- **Rauchlauf:** Die Diagnosereihe bis t = 60 (Q_box je Fall, Bad im Kreis r <= 32) habe ich vor dem Einfrieren
  gesehen und den Badverlust im Plan vermerkt. Vorhersagen und Regeln stammen aus der Karte bzw. waren vor dem
  Rauchlauf im Code; sie blieben unveraendert.
- **Spuren:** p4000b war beim Start etwa 1 min belegt (Lock), dann liefen fein bc 0 -> 500 -> 1000 dort wie geplant.
- **Dateien auf der .69:** py_compile hat runde22-bildung-2/__pycache__ angelegt (Vorgabe "-m py_compile").
  - torch.load gab eine FutureWarning (weights_only), ohne Wirkung; die Dateien sind eigene.
  - Die Zwischenspeicher (.pt) liegen nur auf der .69: zwischen/ 2 Dateien, 67 und 75 MB; rauch-zwischen/ 4 Dateien.
    Lokal sind beide Ordner leer.
- **Scratchpad:** Die Hintergrundaufrufe des Werkzeugs legen dort automatisch Ausgabedateien an. Ich habe alle
  Ausgaben in lauf-69/ umgeleitet und selbst nichts dorthin geschrieben.
- **Sonst keine Abweichung vom eingefrorenen Plan.** bildung1.py, kf5_geburt.py und kf_eich.py wurden nur importiert.

**Laufzeiten** (kleintest.sh, rc = 0 ueberall; Dienstlaufzeit):
- Rauch: 9,5 s, 8,3 s, 11,5 s, 12,4 s, 5,3 s.
- grob bc 0 -> 1000: 104,8 s (3,04 ms je Schritt, B 4). grob a 0 -> 1000: 88,5 s (2,52 ms, B 2).
- fein a 0 -> 500: 345,2 s (12,0 ms, B 2). fein a 500 -> 1000: 336,7 s (12,8 ms).
- fein bc 0 -> 500: 364,0 s (13,3 ms, B 4). fein bc 500 -> 1000: 359,7 s (13,9 ms).
- zusammen: 2,9 s. Summe der Rechenaufrufe etwa 1650 s.
- GPU: grob 126 / 138 MB, fein 424 bis 531 MB.

**sha256:**
- bildung2.py `f1bc80b4d86743e4190a5d719089a180ada8bc4de1a51a52465ae0d97bfb8f90` (lokal = .69 = in allen Ergebnis-JSON)
- PLAN.md.eingefroren-20261002-194644 `e464e1fa625396845c842505b730ab3f03e7a318e58584cf5b12e00b97a639ba`
- Importiert (in allen Ergebnis-JSON so vermerkt):
  - bildung1.py `0ef60ef1f8f1dd209808c5b1dbce044d8238f1f9ceedbe64405c2879f6a0ff64`
  - kf5_geburt.py `9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0`
  - familie_2d_m0.json `f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806`
  - kf_eich.py `332f3293a94448848beeb1c90a58ba9128d14e4f5029983832a8ea7a77eacb59`
  - torch 2.5.1+cu121, Quadro P4000
- lauf-69/ausgabe:
  - grob_bc_0-1000_ergebnis.json `8c7a117655092b44c4d07346c53aaeed81fb2920be3c78ab3107489b3a9d3f97`
  - grob_a_0-1000_ergebnis.json `d51d20f99ffe18b611f649a83ddbb36c604df5baa0fb31e92fb7186b24d9faaf`
  - fein_a_0-500_ergebnis.json `e7094aaee8b81274f98536baa1f5bcd21bb412c01c8f253d1084c781bbae6af0`
  - fein_a_500-1000_ergebnis.json `fb8ee7fa2906edb76a66eedd14c2b1687ed2d536c3f7c9a6ce3d9c9c25592fab`
  - fein_bc_0-500_ergebnis.json `66844d85f8b87ef1d99cc8d7e2398fc5b546e67ec2ec2aff3c3cc4a1fbeebe56`
  - fein_bc_500-1000_ergebnis.json `b2d77fa137299c4c0b266e32e26f3aaea6583e81f65d2082608002265f1af551`
  - zusammen.json `47560b884f31056d499802835a3427655c8613c331feede9a5085b24589f2e57` (lokal = .69)
  - zusammen.txt `a2c108624ee9bf56d99389bcb0b56b41f7c8b8a0c00e69da3ba180d6b0fb7f7c`
  - Berichte: grob_bc `9feac967cafe1ab47c012e3b5ec71450b4916a6a9158bab2061bb2221552bd8c`, grob_a
    `9888165fc87f2be9b79b69eb396747979dc9c15a90448be3ad422b87a73dbe24`, fein_a_0-500
    `fa7c2a4e7103b850e992537b814f5bc093e736b38f84a45b60cbc52f5180b9d5`, fein_a_500-1000
    `6dc0df5d4b2f7f662584702e16798d39a7c58ae68b36f4674e9ff68ed6c5161b`, fein_bc_0-500
    `f24242bac0da67d3e2f692ab527cd1665419b0cb2b90f0fcf087eb179a21f994`, fein_bc_500-1000
    `86b22b216c7ac62300937ad1c67ea7f96dd262c3e976ff7f133ff9205c000100`
- Zwischenspeicher (nur .69; sha256 im Abschnitt-1-JSON = im Abschnitt-2-JSON):
  - fein_a_t500.pt `e4eb42e581076514d098ddf1272bf62641e17afdf249bac6f3702387a653de3e`
  - fein_bc_t500.pt `747937199571fc8d72275f6d416c465e69c10af1afce7e05dd8d7189d3b6bc7a`
- Logs:
  - LAUF-grob-bc `550526d0a6a480e7c5afa62832f8e6eb5c1f4f58cac288a15be631f17561c780`
  - LAUF-grob-a `813bb3814fc528246e09b5b50bdd44e464349ff53a75579055971c755e94339f`
  - LAUF-fein-a1 `8fe306603070b5c7ea1f32be290c1320db3279a04093d0724e712fd239d6756a`
  - LAUF-fein-a2 `31245ecb9184082ab32417fb70f4a9cebdede0a934d7d01993d37356a7ee4ec2`
  - LAUF-fein-bc1 `89d33c5b1e050313aa32a0b7a8ac73a0c4fbe882250e99c1ec8e9af6ce1f7611`
  - LAUF-fein-bc2 `6980dc9e782a15708958569755bfea7a411f9609ee3a1e0db1cabfb9612c2ed6`
  - LAUF-zusammen `5f6d18baa0651681e0df17ba7815b975a3dce37dcf8d780826f63a08faaa3b15`
  - RAUCH-grob-bc-1 `a5b1577d68f9567e73c9ea59e58b201f720010101ad25d780951230dd28178f2`, RAUCH-grob-bc-2
    `973a67a28a65a701bc631b1932f83b6ab569c041cc0fa5263e292b98a63bc706`, RAUCH-fein-a
    `a3010bd0a7516d67c9f5690c73101e6b13afb87a23bc41cb4a58d84a8fdf9f04`, RAUCH-fein-bc
    `2adc4624f710067e2660e931cdea35db48d39e3e58aa0d9b94df1632c44b772f`, RAUCH-grob-a
    `c41c46037edde88d6d87da5df26544e26dfa05c099093f1f3dc6426099beb222`
- Rauch-JSON: grob_bc_0-30 `80d815dc0ffd797fe3f407f9dd779316187165c84978d5b9534d460ce1f37e9b`, grob_bc_30-60
  `4b6268037999a352f3dfbd28e784ba03acc0873885661609a97140e73578414f`, fein_a_0-10
  `4bd91f795acd171476b194eb6bf6b717630816865b421c43b0a9f24c5f51c4df`, fein_bc_0-10
  `fae1fc4e75d7b84dc1b84160fbd85a42755ad5033015d5942e078b52009aa8b9`, grob_a_0-10
  `1ed9fdc37ce8577b259dae1e2584d16b02e9fc6240cd22cba452e0697e229672`
- hilfs/tabelle.jq `a7d8b5bdd06b5499611b791701c01791af5d13a8e056c472566021e02b7bc3f7` (nur Darstellung)

**Dateien:**
- Kartenordner: KARTE.md, PLAN.md (+ eingefrorene Fassung), bildung2.py, ERGEBNIS.md.
- hilfs/: tabelle.jq, tabelle-s0-0.1.md (60 Zeilen Zusatz), tabelle-s0-0.3.md (nur Verweis auf Abschnitt 3).
- lauf-69/ (Spiegel von /home/fmh/fmhc-physics-remote/runde22-bildung-2/lauf-69 ohne .pt): ausgabe/, rauch/, LAUF-*.log,
  RAUCH-*.log, LAUF-spur-a/b.zeiten.

## 6. Einfach gesagt

Wir wollten wissen, warum die Tropfen aus frueheren Versuchen nie zu echten Q-Baellen wurden, und haben drei
Verdaechtige einzeln geprueft. Ein grosser Klumpen kommt energetisch fast an, wackelt aber bis zum Schluss so stark,
dass seine Frequenz nicht zur Familie passt. Zwei nahe Klumpen kleben sofort zusammen und schwingen danach als ein
verbeultes Gebilde, ebenfalls ohne anzukommen. Im schwachen Wellenbad wird der Ball dagegen ganz normal; das Bad schubst
ihn nur an, sodass er langsam wegwandert und unsere Suchregel ihn spaeter nicht mehr findet. Nach den vorher
festgelegten Regeln zaehlt das als Fehlschlag, obwohl der Ball selbst in Ordnung ist. Als Erklaerung fuer die alten
Fehlschlaege bleiben damit vor allem die Groesse und das Verschmelzen, nicht das Bad.

Ende der Bearbeitung: 2026-10-02 20:07:26 CEST (date).
