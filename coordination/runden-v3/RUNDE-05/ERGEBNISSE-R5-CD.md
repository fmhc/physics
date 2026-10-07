# Runde 5: Ergebnisse der Pakete R5-C und R5-D (explorativ, v3)

Auswertung: Anthropic-Agent (Opus) im Auftrag von claude-primary. Nur gelesen, nur diese Datei geschrieben.
Beginn 2026-09-30 02:53:17 CEST, Ende 2026-09-30 03:13:07 CEST (beide gemessen mit date).

## Grundlage und Lesehilfe

- **Quellen:**
  - r5c/PLAN.md, r5d/PLAN.md
  - Berichte r5c/lauf-69/<test>/r5c_bericht.txt und r5d/lauf-69/<test>/r5d_<test>_bericht.txt
  - Logs r5c/lauf-69/LAUF1.log, LAUF2.log, LAUF4.log, LAUF5.log sowie r5d/lauf-69/LAUF.log
  - Alle ausgewerteten Aufrufe enden mit rc = 0 und "Fehler in: keine".
- **bragg und anderson** sind nach dem Update der Leitung aus Version 2 ausgewertet (bragg-v2, anderson-v2). Die
  Rechnung ist wie in v1, nur die Auswertung ist behoben. lauf-69/bragg/, anderson/ und rauch-gpu/ sind v1-Reste und
  zaehlen nicht. Die Rauchtests (rauch-cpu, rauch-cuda) zaehlen ebenfalls nicht.
- **Zahlen:**
  - "grob / fein", wo beide stehen, sonst grob.
  - Eigene Ueberschlaege sind ausdruecklich markiert.
  - "nicht im Bericht" heisst: Der Bericht enthaelt die Groesse nicht.
- **Urteil** gegen die Vorhersage im jeweiligen PLAN: getroffen, teilweise oder verfehlt. Die Abschaetzung entscheidet
  die Leitung.
- **Latten, je ein Wort:**
  - L1 kann scheitern: ja / teilweise
  - L2 Gegenprobe: haelt / teilweise / gerissen / entfaellt
  - L3 Aufloesungsvergleich laut Bericht: bestanden / teilweise / fraglich / entfaellt
  - L4 schon bekannt: bekannt / teilweise / nein. Die Einstufung stammt aus dem PLAN; die Literatur ist dort aus dem
    Gedaechtnis und nicht nachgelesen.
  - L5 Messbezug

## 1. Je Test

### R5-C: 1D, mehrere Baelle und Hintergrund

**C1 osmose (Bio 2)**
- Vorhersage:
  - V-O1: "In allen vier Dichten faellt der Ueberschuss im Fenster bis T/4 unter 0,3 und liegt im Endfenster unter 0,3
    des Anfangs."
  - V-O2: "Kein Wachstum bei S = 1,2, obwohl dort omega_bg > omega ist."
  - V-O3: "Die Phase bei x = 0 dreht im Endfenster mit omega_bg +- 0,03."
- Ergebnis: Kondensat S = 0,8 / 1,0 / 1,1 / 1,2, also nur dichte, stabile Medien (PLAN Abschnitt 1; siehe C3). Ring
  L = 200, T = 200.
  - rel. Ueberschuss bei T/4: -0,01247 / -0,05395 / -0,07386 / -0,09753
  - rel. Ueberschuss am Ende: -0,02761 / -0,01892 / -0,02799 / -0,0445
  - "geloest" in allen vier Laeufen, "gewachsen" in keinem, auch nicht bei S = 1,2 (omega - omega_bg = -0,0351).
  - Drehfrequenz Mitte Ende 0,5999 / 0,7071 / 0,7843 / 0,8719 gegen omega_bg 0,6000 / 0,7071 / 0,7842 / 0,8718.
  - Anfangsrate (0 bis 30) -0,0403 bis -0,0924. Die Aufloesungszeit selbst ist nicht im Bericht.
  - Gegenproben: Beide Vorzeichen von omega - omega_bg sind gerechnet. Die Laeufe "Kondensat allein" und "Ball allein"
    stehen nicht einzeln im Bericht.
- Urteil: getroffen.
- L3 laut Bericht: 4 von 4.
- Latten: L1 ja, L2 teilweise, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken.
  - Im Ein-Feld-Modell ist nur die Aufloesung im dichten Kondensat pruefbar; das duenne Medium der Hypothese ist
    instabil (C3).
  - Die eigentliche Osmose-Frage braucht das Zwei-Feld-Medium mit Austausch eps (r5d/PLAN.md Abschnitt 6).

**C2 massenwirkung (Chemie 9)**
- Vorhersage:
  - V-M1: "Keine Mischung behaelt einen Ball. Der Ueberschuss im Endfenster liegt bei hoechstens 0,3."
  - V-M2: "omega = omega_bg wird erreicht (Drehfrequenz in der Mitte = 0,784 +- 0,03), aber durch Aufloesung. ... Der
    Ball mit omega < omega_bg (0,55) waechst nicht."
- Ergebnis: S = 1,1 (omega_bg = 0,7842), T = 800, Baelle omega^2 = 0,55 / 0,7 / 0,9.
  - rel. Ueberschuss Ende -0,03737 / 0,1204 / 0,04754; alle "geloest".
  - Buckel rel. Ende -0,06654 / 0,009409 / 0,009289.
  - Drehfrequenz Mitte Ende 0,7894 / 0,7863 / 0,7845.
  - Der 0,55-Ball (omega < omega_bg) waechst nicht.
  - Gegenproben: Das Vorzeichen von omega - omega_bg ist beidseitig gerechnet. "Kondensat allein" und "Baelle allein"
    stehen nicht einzeln im Bericht.
- Urteil: getroffen.
- L3: 3 von 3.
- Latten: L1 ja, L2 teilweise, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken; Grund wie bei osmose.

**C3 hintergrund (Papierprobe zu Wellen 6, 7, 11 und zum Fable-Review)**
- Vorhersage (PLAN Abschnitt 1):
  - "0 < S < 2/3 (M2 < 0): modulationsinstabil", gamma_max = |M2|/(4 omega_bg), "keine Landau-Schwelle (v_c = 0)"
  - "S > 2/3 (M2 > 0): linear stabil fuer alle k", mit c_s = 0,555 / 0,707 / 0,733 / 0,747 bei S = 0,8 / 1,0 / 1,1 /
    1,2
  - stationaer nur Dellen oder dunkle Solitonen, "keine Buckel"
  - S_krit(L) etwa 9,9e-4 (L = 100) und 1,1e-4 (L = 300)
- Ergebnis: 16 Dichten, exakte Dispersion auf 30000 k-Werten.
  - S von 1e-4 bis 0,6: instabil. gamma_max Formel / Scan 9,9995e-05 / 9,9993e-05 (S = 1e-4) bis 2,2558e-01 /
    2,2558e-01 (S = 0,3); Bandkante Formel und Scan gleich bis auf das Scanraster. Stationaere Form: "keine". Im Ring
    L = 100 und 300 ist davon nur S = 1e-4 stabil (Kasteneffekt, PLAN Abschnitt 1).
  - Ab S = 0,6667: gamma_max = 0.
    - c_s = v_c = 0,5547 / 0,7071 / 0,7332 / 0,7471 bei S = 0,8 / 1,0 / 1,1 / 1,2.
    - Stationaer "Delle (Blase)" bis S = 0,9, "dunkles Soliton (Knick)" ab S = 1.
  - S_krit: 9,884e-04 (L = 100), 2,468e-04 (L = 200), 1,097e-04 (L = 300).
- Urteil: getroffen.
  - Das bestaetigt den Fable-Befund: Ein duennes Medium ist im Ein-Feld-Modell fuer S < 2/3 modulationsinstabil.
  - Deshalb laufen osmose und massenwirkung nur auf dem dichten Kondensat.
  - Wellen 6 (Gleiten), 7 (Windschatten) und 11 (Fahrtwind) sind im Ein-Feld-Modell nicht umsetzbar (PLAN Abschnitt 2)
    und nicht gerechnet.
- L3: entfaellt (keine Zeitentwicklung, keine L3-Zeile im Bericht).
- Latten: L1 ja, L2 entfaellt, L3 entfaellt, L4 bekannt, L5 nein.
- Vorschlag: Wellen 6, 7 und 11 im Ein-Feld-Modell verwerfen und im Zwei-Feld-Medium (Aufbau von D6 kreuzen)
  weiterfuehren, weil das chi-Medium bei jeder Dichte stabil ist und eine Schallgeschwindigkeit hat (r5d/PLAN.md 1.3).

**C4 pendeln (Bio 12)**
- Vorhersage (Omega_p = 1,298 exp(-0,2739 D)):
  - V-P1: "Das Verhaeltnis gemessen/vorhergesagt liegt bei D = 10 und 12 in [0,5; 2], bei D = 7,5 in [0,3; 3]."
  - V-P2: "Die Steigung von ln Omega_p gegen D liegt in [-0,33; -0,22]."
  - V-P3: "D = 20 zeigt hoechstens eine halbe Schwingung. D = 30 bleibt eingefroren (Spanne q < 5 % von |q0|)."
  - V-P4: ohne Ungleichgewicht |q| < 1e-3; gleichphasig waechst |q| mindestens um den Faktor 3, oder die Baelle
    verschmelzen.
  - V-P5 (freie Paare, dphi = pi): "Die Baelle trennen sich (D_Ende > 2 D0), mit hoechstens zwei Nulldurchgaengen von
    q."
- Ergebnis:
  - Verhaeltnis gemessen/vorhergesagt 0,9479 (D = 7,5), 1,015 (10), 1,029 (12), 1,003 (15); fein 0,9477 / 1,015 /
    1,029 / 1,003.
  - Steigung ln Omega_p gegen D: -0,2669 / -0,2668 (Vorhersage -0,2739).
  - D = 20: Omega_p 0,01257, Verhaeltnis 2,315; Spanne q 0,0470. Ob hoechstens eine halbe Schwingung: nicht im Bericht.
  - D = 30: Spanne q 0,0002 / 0,0003 bei |q0| = 0,0236.
  - Kontrollen: ohne Ungleichgewicht max|q| 0,0000; gleichphasig max|q| 1,0870 / 0,9520 bei |q0| 0,0299 / 0,0294.
  - Freie Paare dphi = pi bei D0 = 7 / 8 / 10:
    - D_Ende 221,41 / 176,45 / 109,99, also getrennt
    - Nulldurchgaenge 82 / 3 / 1 (grob) und 58 / 1 / 1 (fein)
  - Freies Paar dphi = pi/2: Spanne q 0,8379, 3 Nulldurchgaenge, D_Ende 142,29, nicht verschmolzen.
  - "Harmonisch" (V-P1) und das Zeitskalenverhaeltnis 0,88 (V-P5): nicht im Bericht.
- Urteil: teilweise.
  - Getroffen: V-P1, V-P2, V-P4 und D = 30.
  - Verfehlt: V-P5 bei D0 = 7 (82 / 58 Nulldurchgaenge) und bei D0 = 8 grob (3).
  - D = 20 ist nicht entscheidbar.
- L3: 6 von 6.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken. Der Takt ist quantitativ getroffen, aber vorab von Hand ableitbar und als Josephson-Kontakt
  bekannt; es gibt keinen Messbezug.

**C5 ir (Chemie 4)**
- Vorhersage (Omega_vib = 1,473 exp(-0,2739 D)):
  - V-I1: "Das Verhaeltnis gemessen/vorhergesagt liegt in [0,5; 2] fuer D = 10, 12 und 15. Die Steigung von
    ln Omega_vib ist -0,274 +- 25 %."
  - V-I2: "Omega_vib/Omega_p = 1,135, fuer alle D gleich."
  - V-I3: Ladungsmode ruhig (max|q| < 1e-3); D = 30 bleibt bei u = s0 (Spanne < 5 %); Kontrolle s0 = 0 bleibt bei
    u ~ 0.
  - V-I4: "Spanne im letzten Viertel mindestens 0,7 x erstes Viertel."
- Ergebnis:
  - Verhaeltnis 1,066 (D = 10), 1,037 (12), 0,9901 (15); bei D = 7,5: 1,091. Fein 1,066 / 1,038 / 0,9906 / 1,092.
  - Steigung von ln Omega_vib: nicht im Bericht.
  - V-I2: Das Verhaeltnis ist nicht im Bericht. Rohwerte Omega_vib (ir) / Omega_p (pendeln): 0,2062 / 0,1578
    (D = 7,5), 0,1015 / 0,08521 (10), 0,05713 / 0,04994 (12), 0,02398 / 0,0214 (15).
  - max|q| hoechstens 1,74e-14 (Laeufe mit s0 = 0,3).
  - D = 30: Spanne u 0,0009 -> 0,0040 bei s0 = 0,3.
  - Kontrolle s0 = 0: Spanne u 0,0000.
  - Spanne erstes -> letztes Viertel: 0,5057 -> 0,5007 (D = 7,5), 0,5696 -> 0,5664 (10), 0,5889 -> 0,5879 (12),
    0,5974 -> 0,4873 (15). Alle liegen ueber 0,7 x Anfang.
- Urteil: getroffen (V-I1, V-I3, V-I4). V-I2 und die Steigung stehen nicht im Bericht.
- L3: 5 von 5.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken; Grund wie bei pendeln.

**C6 symbiose (Bio 16)**
- Vorhersage:
  - V-S1: "0,70/0,70, 0,71 und 0,72 verschmelzen. 0,74 liegt auf der Kippe. 0,78 verschmilzt nicht und trennt sich
    nicht (Abstand bleibt 7 bis 14). ... Gegenphasig: getrennt."
  - V-S2: "Nach dem Verschmelzen ist die abgestrahlte Energie 0,05 bis 0,45."
  - V-S3 (L1): "Es gibt keinen Lauf mit 'gebunden' UND einer Energie deutlich unter E1 + E2."
- Ergebnis: D0 = 10, T = 800, offene Box [-150, 150].
  - 0,70/0,70: verschmolzen bei t = 26; abgestrahlt 0,1943, Anregung 0,3855.
  - 0,71: verschmolzen bei t = 26,5; abgestrahlt 1,5119, Anregung 0,02873.
  - 0,72: getrennt (D min 4,94, D Ende 166,49); abgestrahlt 1,5085.
  - 0,74: getrennt (D min 6,09, D Ende 180,50); abgestrahlt 1,5282.
  - 0,78: getrennt (D min 7,46, D Ende 135,99); abgestrahlt 0,0104.
  - gegenphasig: getrennt (D Ende 144,28).
  - Kein Lauf ist "gebunden".
  - Bindung Start +0,19169 (gleichphasig 0,70/0,70) und -0,19718 (gegenphasig). Anker-Gewinn beim Verschmelzen
    -0,4484.
  - Einzelball: E Box 2,298462 -> 2,298462.
- Urteil: teilweise.
  - Getroffen: V-S3.
  - Verfehlt: V-S1 bei 0,72 (getrennt statt verschmolzen) und 0,78 (getrennt statt Abstand 7 bis 14); V-S2 bei 0,71
    (abgestrahlt 1,5119).
- L3: 6 von 6.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: verwerfen. Kein Lauf ist "gebunden", Symbiose ohne Verschmelzen gibt es hier also nicht; die offene
  Energiebilanz (Abschnitt 2) aendert die Klassen nicht.

**C7 quorum (Bio 39)**
- Vorhersage:
  - V-Q1: "Kein Quorum-Schalter: r_Ende < 0,6 bei allen drei Dichten, und r_Ende - r_Anfang < 0,3."
  - V-Q2: "Die Kohaerenz C bleibt unter 0,5."
  - V-Q3: "Gleiche Phase bleibt aus Symmetrie bei r nahe 1. Der entkoppelte Ring (K = 2) bleibt beim Anfangswert."
- Ergebnis: r und C in vier Zeitfenstern, T = 600.
  - K = 8 (D = 15): r 0,071 -> 0,102 / 0,068 -> 0,098; C hoechstens 0,121 / 0,116.
  - K = 12 (D = 10): r 0,912 -> 0,777 / 0,927 -> 0,595; C im ersten Fenster 0,689 / 0,732, im letzten 0,551 / 0,242.
  - K = 16 (D = 7,5): r 0,102 -> 0,635 / 0,203 -> 0,541; C hoechstens 0,315 / 0,196.
  - Gleiche Phase: r = 1,000 in allen Fenstern.
  - Entkoppelt (K = 2): r 0,995 / 0,388 / 0,605 / 0,611 (grob), 0,995 / 0,411 / 0,604 / 0,606 (fein).
  - Atemamplitude:
    - K = 12 zufall 6,91e-02 -> 4,13e-01
    - K = 16 1,29e-01 -> 2,95e-01
    - K = 8 1,64e-02 -> 2,73e-02
    - gleiche Phase 1,59e-02 -> 1,58e-02
    - K = 2 1,16e-02 -> 1,16e-02
- Urteil: verfehlt.
  - V-Q1 reisst bei K = 16 (Anstieg von r um mehr als 0,3 in beiden Stufen) und bei K = 12 grob (r_Ende 0,777).
  - V-Q2 reisst bei K = 12.
  - Die Kontrolle "entkoppelt" (V-Q3) reisst.
- L3: 4 von 5. Welcher Lauf fehlt, nennt der Bericht nicht; grob und fein liegen bei K = 12 zufall am weitesten
  auseinander (r_Ende 0,777 gegen 0,595).
- Latten: L1 ja, L2 gerissen, L3 teilweise, L4 nein, L5 nein.
- Vorschlag: parken. Solange die Kontrolle "entkoppelt" reisst, ist r keine belastbare Messgroesse; das Anwachsen der
  Atemamplitude ist nicht vorhergesagt und ungeklaert.

**C8 lawinen (Bio 50)**
- Vorhersage:
  - V-L1: "Lawinen sind groesser als ein Ball (mittlere Groesse > 1,5) ... am Ende gibt es eine Riesenlawine (aktiver
    Anteil am Ende > 0,5)."
  - V-L2: "Ohne Stoesse: keine Ereignisse. Entkoppelter Ring (D = 30 ...): nur Groesse 1, abgesehen von Zufallstreffern
    benachbarter Baelle."
- Ergebnis: K = 24, D = 10, 49 Stoesse, vier Seeds, T = 500.
  - Je Seed 7 bis 19 Lawinen (grob) bzw. 6 bis 19 (fein).
  - Mittlere Groesse 8,37 bis 17,43 (grob) bzw. 8,42 bis 20,17 (fein); groesste Lawine 24, also der ganze Ring.
  - Dauer max 491,0; aktiver Anteil am Ende 0,99 bis 1,00.
  - Ohne Stoesse: 200 / 198 Lawinen, alle der Groesse 24, Dauer hoechstens 4,0, aktiv am Ende 0,68 / 0,70.
  - Entkoppelter Ring K = 8: eine Lawine der Groesse 8, Dauer 490,5, aktiv am Ende 1,00.
- Urteil: teilweise. V-L1 ist getroffen, V-L2 in beiden Kontrollen verfehlt; damit ist auch V-L1 nicht belastbar.
- L3: 5 von 5.
- Latten: L1 ja, L2 gerissen, L3 bestanden, L4 nein, L5 nein.
- Vorschlag: verwerfen (Ein-Feld-Modell, ungedaempft).
  - Die Ereignisschwelle spricht schon ohne Stoesse an und fasst entkoppelte Baelle zu einer Lawine zusammen.
  - Der PLAN nennt das erwartete Bild selbst "Aufsummieren ungedaempfter Anregung, keine Kritikalitaet".

**C9 bragg (W21, Bragg-Kette; Version 2)**
- Vorhersage:
  - V-B1: "Das Transmissionsminimum liegt bei k0 = 0,31 +- 0,015 (d = 10) und 0,26 +- 0,015 (d = 12)."
  - V-B2: "Die Tiefe betraegt T_min 0,4 bis 0,85. ... Ausserhalb der Luecke gilt T >= 0,95."
  - V-B3: "Einzelball: T >= 0,95 ohne Minimum, R_1(k0) faellt mit k0. Die Kette ohne Paket ruht (max Verschiebung
    < 0,05)."
  - V-B4: Ein Minimum bei pi/(2d) liegt ausserhalb des Scans und bleibt offen.
- Ergebnis: Ring L = 480, T = 700.
  - Kette: T und R liegen weit ausserhalb [0, 1] und sind oft negativ.
    - d = 10: T von -14565,16 (k0 = 0,25) bis 14396,00 (k0 = 0,22); R bis 16457,53.
    - d = 12: T von -7,78 (k0 = 0,34) bis 94,67 (k0 = 0,38).
    - Der Code meldet das Minimum daher bei k0 = 0,25 (d = 10) und 0,34 (d = 12).
  - Nur je ein Kettenwert liegt zwischen 0 und 1, und zwar genau an k_Bragg 0,3142 bzw. 0,2618:
    - d = 10 bei k0 = 0,31: T 0,64127 / 0,61847
    - d = 12 bei k0 = 0,26: T 0,59904 / 0,59617
  - Die Kette bewegt sich mit Paket: max Verschiebung bis 14,0 (d = 10, k0 = 0,22) und 5,44 (k0 = 0,38); bei d = 12
    hoechstens 0,085. Die kleinste Verschiebung je Kette liegt an denselben zwei k0 (1,02e-02 und 8,80e-03).
  - Kette ohne Paket: max Verschiebung 2,362e-10 (d = 10) und 8,953e-13 (d = 12).
  - Einzelball bei k0 = 0,22 / 0,26 / 0,31 / 0,38:
    - T 0,94985 / 0,96252 / 0,97759 / 0,97943 (fein bei 0,22: 0,95442)
    - R 0,00482 / 0,01034 / 0,01502 / 0,00967
- Urteil: verfehlt; die Kettenwerte sind als Transmission nicht auswertbar.
  - V-B3: Die Kette ohne Paket ruht (getroffen).
  - Einzelball: T bei k0 = 0,22 grob knapp unter 0,95; R_1 faellt nicht mit k0, sondern steigt bis 0,31.
- L3: 19 von 22, obwohl die Werte ausserhalb [0, 1] liegen (Abschnitt 2).
- Latten: L1 ja, L2 teilweise, L3 fraglich, L4 bekannt, L5 nein.
- Vorschlag: parken. Zuerst klaeren, warum sich die Kette mit Paket bewegt (ohne Paket ruht sie); vorher ist keine
  Bragg-Aussage moeglich.

**C10 anderson (W22, Anderson-Gas; Version 2)**
- Vorhersage:
  - V-A1: "<-ln T> waechst linear mit N: etwa 0,03 / 0,07 / 0,13 fuer N = 4 / 8 / 16. Das Verhaeltnis zu N x (-ln T_1)
    liegt in [0,7; 1,4]."
  - V-A2: xi = d_mittel/R_1 "etwa 4000 Laengeneinheiten".
  - V-A3 (Gegenprobe): "Die periodische Kette im Durchlassband waechst nicht mit N: |ln T_per(16)| < 0,5 x
    <-ln T_zufall(16)>."
  - V-A4: "Die Kugeln ruhen (max Verschiebung < 0,5)."
- Ergebnis: Ring L = 1400, T = 2200, Seeds 21 bis 24.
  - Einzelball -ln T 0,009163 / 0,009016 (PLAN: etwa 0,008).
  - <ln T> zufall -0,01975 / -0,05106 / -0,1094 (grob) und -0,02024 / -0,05248 / -0,1137 (fein) bei N = 4 / 8 / 16.
  - Vorhersage N x Einzel -0,03665 / -0,07331 / -0,1466 (grob).
    - N = 4: in beiden Stufen unter dem 0,7-fachen.
    - N = 8: grob knapp darunter, fein darueber.
    - N = 16: im Band.
  - Steigung je Ball -0,007448 / -0,00777; Lokalisierungslaenge 4699 / 4505.
  - Periodisch -0,03279 / -0,05716 / -0,09274 (grob): Der Betrag waechst mit N; bei N = 16 ist er groesser als die
    Haelfte des Zufallswerts (0,09274 gegen 0,1094), bei N = 4 und 8 sogar groesser als der Zufallswert (fein ebenso).
  - max Verschiebung 0,1832.
- Urteil: teilweise.
  - Getroffen: V-A2, V-A4.
  - V-A1 nur bei N = 16 (N = 8 grenzwertig).
  - Die Gegenprobe V-A3 reisst.
- L3: 3 von 3.
- Latten: L1 ja, L2 gerissen, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken. xi hat die vorhergesagte Groessenordnung, aber die periodische Kette daempft fast so stark wie das
  Zufallsgas; damit trennt der Test die Zufallsaddition nicht von der periodischen Kette.

### R5-D: 1D, zwei Felder

**D1 zellkern (Bio 8)**
- Vorhersage:
  - V8a (lam = 0, Kontrolle): "Abstand bleibt 0,5, K = 1/m auf 0,01 ... m = 1 gemeinsam, m = 1,5 und 2,5
    verschachtelt."
  - V8b (lam = -0,4): "Abstand am Ende < 0,3 ... |dK| < 0,1, Loch < 0,05, Ladungen im Fenster >= 0,97. Klassen wie bei
    lam = 0."
  - V8c (lam = +0,4): "getrennt bei allen m, t_Trennung < 100."
  - V8d: "'Huelle mit Loch' in 0 von 9 Laeufen."
- Ergebnis: psi omega^2 = 0,6; chi mit m = 1 / 1,5 / 2,5; T = 400.
  - lam = 0: Abstand 0,500; K 1,000 / 0,666 / 0,399 (fein 1,000 / 0,667 / 0,400); Klassen gemeinsam / verschachtelt /
    verschachtelt; Ladungen 1,0000.
  - lam = -0,4:
    - Abstand 0,021 / 0,003 / 0,017
    - dK +0,001 / +0,193 / -0,054
    - Loch psi 0,011 / 0,006 / 0,008, Loch chi 0,011 / 0,020 / 0,067. Nach der PLAN-Definition zaehlt die breitere
      Komponente, bei m = 1,5 und 2,5 also psi.
    - Ladungen 0,9786 bis 0,9996
    - Klassen gemeinsam / gemeinsam / verschachtelt
  - lam = +0,4: bei allen m getrennt, t_Trennung 20,0 / 21,5 / 25,5. Die Relativgeschwindigkeit ist nicht im Bericht.
  - "Huelle mit Loch" in keinem der 9 Laeufe.
- Urteil: teilweise.
  - Getroffen: V8a, V8c, V8d.
  - Verfehlt: V8b bei m = 1,5 (dK +0,193; Klasse gemeinsam statt verschachtelt).
- L3: 9 von 9 Kenngroessen.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: parken. Die Verschachtelung folgt schon ohne Kopplung aus der Breite 1/m (V8a), und eine Huelle mit Loch
  entsteht nicht; der Aufbau liegt als Baustein fuer die Zwei-Feld-Idee bereit.

**D2 raeuber (Bio 15)**
- Vorhersage:
  - V15a (gleichphasig, z0 = 0,05): "pendelt um den Gleichstand, z zwischen -0,05 und +0,05, Periode 57 (40 bis 80)."
  - V15b (gleichphasig, z0 = 0,3): "pendelt, A ~ 0,3, Periode 60 bis 110."
  - V15c (gleichphasig, z0 = 0,6): "Selbstfang ... z bleibt zwischen etwa 0,44 und 0,6."
  - V15d (gegenphasig): "Selbstfang auf der Seite von z0 ... z zwischen 0,05 und ~0,43 bzw. zwischen 0,3 und ~0,52.
    Kein Pendeln um den Gleichstand."
  - V15e (rein): "ruhig, z > 0,98."
  - V15f (Kontrollen): "eps = 0: A < 1e-4; getrennt: A < 1e-3."
  - V15g (Box): pendelt, aber "keine einzelne saubere Periode".
  - L1: Pendeln in allen sechs Austauschlaeufen widerspraeche dem Josephson-Bild.
- Ergebnis: eps = 0,02, T = 500, Fenster [T/6, T].
  - gleichphasig z0 = 0,05: pendelt; z -0,1859 .. +0,1852 (A 0,1856); 15 Wechsel; Periode 56,3.
  - gleichphasig z0 = 0,3: pendelt; z -0,3797 .. +0,5502 (A 0,4650); 2 Wechsel; Periode 2483,2 / 2376,6.
  - gleichphasig z0 = 0,6: Selbstfang; z +0,4409 .. +0,6306.
  - gegenphasig z0 = 0,05: Selbstfang; z +0,2269 .. +0,5730; 0 Wechsel.
  - gegenphasig z0 = 0,3: Selbstfang; z +0,3386 .. +0,5952; 0 Wechsel.
  - rein: ruhig; z +0,9933 .. +0,9983.
  - Kontrollen: eps = 0: A 0,0000; getrennt 40: A 0,0075.
  - Box: pendelt, 7 Wechsel, Periode 108,9. Ob mehrere Perioden vorliegen: nicht im Bericht.
  - Korrelation psi/chi -0,943 bis -1,000 (ausser eps = 0: +0,972); "Summe rel." bis 3,9e-02.
- Urteil: teilweise.
  - Getroffen: alle Klassen. Gependelt wird nur gleichphasig bis z0 = 0,3, sonst gibt es Selbstfang; L1 im Sinne des
    Josephson-Bilds ist bestanden.
  - Verfehlt:
    - Amplitude bei z0 = 0,05 (0,1856 statt 0,05)
    - Periode bei z0 = 0,3 (2483,2 statt 60 bis 110)
    - Bereich gegenphasig z0 = 0,05 (bis 0,5730 statt bis ~0,43)
    - Kontrolle getrennt (A 0,0075 statt < 1e-3)
- L3: 12 von 12.
- Latten: L1 ja, L2 teilweise, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: verwerfen (als Raeuber-Beute-Karte). Der Lotka-Volterra-Versatz ist mit erhaltener Summe vorab
  ausgeschlossen (PLAN 2.2); gemessen ist das bekannte Josephson-Bild mit Selbstfang.

**D3 mitochondrium (Bio 35)**
- Vorhersage:
  - V35a (lam = -0,3): "v = 0: ruht innen. v = 0,2: gefangen (Anteil drin >= 0,9, mindestens 3 Mittendurchgaenge,
    Pendelperiode ~80 bis 100). v = 0,4: entkommen, t_raus < 60."
  - V35b (lam = 0): "v = 0 ruht; v = 0,2 und 0,4 fliegen frei durch (t_raus ~ 41 bzw. 20)."
  - V35c (lam = +0,3): "v = 0 ruht innen ... v = 0,2 und 0,4 entkommen frueher als bei lam = 0, mit
    Austrittsgeschwindigkeit ~0,39 bzw. ~0,5."
  - V35d: "Der Gast ueberlebt ueberall (Q_gast gehalten >= 0,9 ...); Q_wirt gehalten >= 0,98."
- Ergebnis: Wirt psi omega^2 = 0,500001; Gast chi mit m = 2; T = 400.
  - lam = -0,3:
    - v = 0 ruht innen.
    - v = 0,2 gefangen: drin-Anteil 1,000, 5 Durchgaenge.
    - v = 0,4 entkommen, t_raus 26,0 / 25,5.
  - lam = 0: v = 0 ruht; v = 0,2 und 0,4 entkommen, t_raus 41,0 und 20,5.
  - lam = +0,3: v = 0 ruht innen; v = 0,2 und 0,4 entkommen, t_raus 32,5 / 32,0 und 19,5.
  - Q_gast gehalten 0,9985 bis 1,0000; Q_wirt gehalten 0,9985 bis 1,0000.
  - Pendelperiode und Austrittsgeschwindigkeiten: nicht im Bericht.
- Urteil: getroffen (alle Vorhersagen, die der Bericht prueft).
- L3: 4 von 4.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: weiter. Alle pruefbaren Vorhersagen sind getroffen, Gast und Wirt behalten ihre Ladung, und die Karte ist
  der direkteste Baustein fuer Finns Zwei-Feld-Idee.

**D4 altern (Bio 48)**
- Vorhersage:
  - V48a: "Gamma_mess/Gamma_Formel liegt fuer alle 8 Groessen mit Gamma_Formel > 1e-5 zwischen 0,5 und 2. Die
    Grundlinie aus eps = 0 muss darunter liegen."
  - V48b: "Gamma ist nicht monoton in Q. Die kleinen Baelle (0,8; 0,9) verdampfen mindestens 20-mal langsamer als die bei
    0,55 bis 0,6. Die Lebensdauer waechst zu kleinen Baellen hin."
  - V48c: "Kanal m = 1,2: |Gamma| < 0,01 * Gamma_Formel desselben omega; eps = 0: |Gamma| < 1e-7."
- Ergebnis: eps = 0,05, T = 400.
  - Gamma_mess/Gamma_Formel je omega^2:
    - 0,500001: 0,687
    - 0,5001: 1,118
    - 0,51: 0,989
    - 0,55: 1,366
    - 0,6: 0,610
    - 0,7: 0,666
    - 0,8: 0,835
    - 0,9: 0,933 (Formel 6,969e-06, unter 1e-5)
  - Gamma ist nicht monoton in Q ("monoton wachsend: False").
  - Gamma(0,8) = 1,553e-04 gegen Gamma(0,6) = 1,854e-03: weniger als 20-mal kleiner. Gegen Gamma(0,55) = 6,774e-03:
    mehr als 20-mal. Gamma(0,9) = 6,500e-06.
  - Lebensdauer 531 (0,55), 1640 (0,6), 3747 (0,7), 1,214e+04 (0,8), 1,993e+05 (0,9); dazu 789 (0,51), 3880
    (0,500001) und 4,677e+04 (0,5001).
  - Gegenproben: Kanal m = 1,2: Gamma 1,008e-07 und 5,623e-08. eps = 0: 2,888e-10 / 1,804e-11.
  - Ladung im Fenster: bei 0,55 von 3,87755 auf -0,93194 / -0,94514; bei 0,51 von 5,43118 auf 2,75540.
- Urteil: teilweise.
  - Getroffen: V48a, V48c. Aus V48b: Gamma ist nicht monoton, und ab 0,55 waechst die Lebensdauer zu kleinen Baellen
    hin.
  - Verfehlt: der Faktor 20 zwischen 0,8 und 0,6.
- L3: 8 von 8.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: parken.
  - Die Formel traegt (Verhaeltnis 0,610 bis 1,366).
  - Vorher klaeren, was die negative Endladung bei 0,55 bedeutet.
  - Vorher die Quelle (Cohen, Coleman, Glashow, Georgi 1986) lesen, wie Fable-Review und PLAN verlangen.

**D5 tensid (Chemie 17)**
- In 1D ist nur der Wandteil pruefbar; Q_min und die Reifungsbremse brauchen 3D (PLAN 2.5).
- Vorhersage:
  - V17a: "Amphiphil (a = 1 und 2, beide A): Wandanteil >= 0,6; chi gehalten 0,3 bis 0,9."
  - V17b: "omega_chi bei a = 1: 0,90 bis 0,97; bei a = 2: 0,75 bis 0,92."
  - V17c: "E_ads < 0 und innerhalb 30 % von -(1 - omega_chi) Q_chi."
  - V17d: "|dOmega| < 0,3 |E_ads|."
  - V17e: "Die Wand wird breiter: dw > 0. dw(A = 0,15)/dw(A = 0,05) zwischen 4 und 12 ... dw(a = 2) > dw(a = 1)."
  - V17f (Gegenproben): "chi frei: Wandanteil < 0,2, dw = 0 auf 1e-6. Dichte: Innenanteil >= 0,5, Wandanteil < 0,4.
    anti: Wandanteil < 0,3."
  - Kontrolle nackt: "Omega = 0,7071 auf 1e-3, w = 2,83 auf 1e-2."
- Ergebnis: Wirt omega^2 = 0,500001, T = 400, Fenster [T/2, T]. Reihenfolge a = 1 (A = 0,05 / 0,15), dann a = 2
  (A = 0,05 / 0,15).
  - Wandanteil 0,574 / 0,574 und 0,738 / 0,737; chi gehalten 0,534 / 0,536 und 0,715 / 0,772.
  - omega_chi 0,96098 / 0,96059 und 0,89604 / 0,89400.
  - E_ads, in Klammern die lineare Erwartung: -3,513e-04 (-3,594e-04), -3,182e-03 (-3,260e-03), -1,218e-03
    (-1,244e-03), -1,127e-02 (-1,146e-02).
  - dOmega -1,05e-04 / -8,38e-04 und -1,43e-04 / -7,46e-04. Bei a = 1, A = 0,05 liegt |dOmega| genau auf der Grenze
    0,3 |E_ads|; bei der gedruckten Genauigkeit ist das nicht entscheidbar.
  - dw +1,55e-03 / +1,39e-02 und +5,89e-03 / +5,33e-02.
  - Gegenproben:
    - chi frei: Wandanteil 0,097, dw 0
    - anti: Wandanteil 0,049
    - Dichte (lam = -0,5): Wandanteil 0,449, Innenanteil 0,335
  - nackt: Omega 0,70649 / 0,70694; w 2,8067 / 2,8072 (Anker 2,8284).
- Urteil: teilweise.
  - Getroffen: V17b, V17c, V17e und V17d (bei a = 1, A = 0,05 an der Grenze).
  - Verfehlt:
    - V17a bei a = 1 (Wandanteil 0,574 statt >= 0,6)
    - Gegenprobe "Dichte" in beiden Schwellen
    - nackte Wandbreite 2,8067 gegen "2,83 auf 1e-2"
- L3: 18 von 18.
- Latten: L1 teilweise, L2 teilweise, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: weiter. Der Wandteil ist in 1D weitgehend getroffen; die eigentliche Frage (Q_min mit und ohne chi) geht
  nur 3D radial mit zwei Feldern (PLAN 2.5).

**D6 kreuzen (Wellen 10; 1D-Baustein "Segelkennlinie")**
- Kreuzen selbst ist in 1D nicht pruefbar, weil es keine Querrichtung gibt (PLAN 2.6). Gerechnet ist die Kraft eines
  stroemenden, stabilen chi-Mediums (c_s = 0,2085) auf einen ruhenden Ball.
- Vorhersage (Landau), Kernsatz: "Unter der Schallgeschwindigkeit des Mediums wirkt keine Kraft, darueber Mitnahme."
  - V10a: "n = 0: v = a = 0."
  - V10b: "n = +-5 (0,48 c_s): kraftfrei, |a| < 2e-5, |v| < 0,01; v(-5) = -v(+5)."
  - V10c: "n = 8 (0,76 c_s): unsicher. Erwartet kraftfrei bei lam = 0,1."
  - V10d: "n = 16 und 29 (ueber c_s): Mitnahme in +x, a > 5e-5, v_Ende > 0,01. Bei n = 16 ist die Mitnahme mit
    lam = 0,3 staerker als mit 0,1."
  - V10e: "lam = 0: v = a = 0 exakt."
  - V10f: Medium allein gleichfoermig (C_max - C_min < 1e-6).
- Ergebnis: T = 300, periodische Box. Angegeben sind Verschiebung, v Ende und a spaet (beide aus Fits auf [T/3, T]).

| Lauf | u/c_s | Verschiebung | v Ende | a spaet |
|---|---|---|---|---|
| n = 0 | 0 | 0,000 | 3,58e-16 | 1,15e-17 |
| n = +5 | 0,48 | +1,273 | 5,22e-03 | 4,04e-06 |
| n = -5 (Spiegel) | -0,48 | -1,273 | -5,22e-03 | -4,04e-06 |
| n = +8 | 0,76 | +3,742 | 1,65e-02 | 5,23e-05 |
| n = +16 | 1,46 | +18,300 | 8,51e-02 | 4,56e-04 |
| n = +29 | 2,40 | +3,142 | 1,36e-02 | 6,52e-05 |
| n = +16, lam = 0 | 1,46 | 0,000 | 2,33e-16 | 1,83e-17 |
| n = +16, lam = 0,3 | 1,46 | +61,595 | 2,74e-01 | -3,82e-06 |

  - Medium allein: C 0,100049 .. 0,100049 (grob) bzw. 0,100011 .. 0,100011 (fein).
  - Die Verschiebung bei n = +5 ist grob und fein gleich (1,273 / 1,273).
- Urteil: teilweise.
  - Getroffen: V10a, V10d, V10e, V10f.
  - V10b ist nach den Vorab-Schwellen getroffen (|a| 4,04e-06 < 2e-5, |v| 5,22e-03 < 0,01, Spiegel exakt). Der Ball
    verschiebt sich unter c_s aber um 1,273; "keine Kraft" im Wortlaut ist damit nicht erfuellt (Frage in Abschnitt 2).
  - V10c: Bei 0,76 c_s gibt es keine Kraftfreiheit (a 5,23e-05 und v 1,65e-02 liegen ueber den V10b-Schwellen). Die
    Vorhersage war als unsicher markiert.
- L3: 12 von 12.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: weiter. Die Bewegung unter c_s ist ungeklaert und haengt nicht von der Aufloesung ab; derselbe Aufbau traegt
  Wellen 5, 6, 7 und 11 (r5d/PLAN.md Abschnitt 6).

## 2. Auffaelligkeiten

### Kontrollen, die reissen

1. **lawinen:**
   - Ohne Stoesse zaehlt der Code 200 / 198 "Lawinen" der Groesse 24 (Dauer hoechstens 4,0).
   - Der entkoppelte Ring (K = 8, D = 30) bildet eine einzige Lawine aus allen 8 Baellen (Dauer 490,5), erwartet war
     nur Groesse 1.
   - Die Schwelle (1 % in S_max) trennt damit weder Stoss von Eigenbewegung noch gekoppelt von entkoppelt.
2. **quorum:** Der entkoppelte Ring (K = 2) faellt von r 0,995 auf 0,611 / 0,606, statt beim Anfangswert zu bleiben.
3. **anderson:** Die periodische Gegenprobe daempft mit N wachsend (-0,03279 / -0,05716 / -0,09274), bei N = 4 und 8
   staerker als das Zufallsgas; V-A3 reisst.
4. **raeuber:** Die Kontrolle "getrennt 40" hat A = 0,0075 statt < 1e-3 (z 0,3012 .. 0,3162).
5. **tensid:**
   - Gegenprobe "Dichte" (lam = -0,5): Innenanteil 0,335 (Soll >= 0,5), Wandanteil 0,449 (Soll < 0,4).
   - Nackte Wandbreite 2,8067 / 2,8072 gegen "2,83 auf 1e-2".
6. **pendeln, gleichphasige Kontrolle:** Das Kriterium (|q| mindestens mal 3) haelt, aber der Ausgang haengt von der
   Stufe ab. Grob: min Abstand Ende 8,29, max Verschiebung 2,805. Fein: 0,00 und 11,257.

### Unphysikalische Zahlen und Bilanzen

7. **bragg:**
   - Die Kettenwerte reichen bei d = 10 von T = -14565 bis 14396, R bis 16457,5; bei vielen k0 sind sie negativ.
   - Die Kette bewegt sich mit Paket um bis zu 14,0, ohne Paket nur um 2,4e-10.
   - L3 besteht trotzdem 19 von 22. L3 prueft hier Reproduzierbarkeit, nicht Plausibilitaet.
   - Frage an die Leitung: Nur an k_Bragg (k0 = 0,31 bzw. 0,26) liegt T zwischen 0 und 1, und dort ist die Verschiebung
     am kleinsten. Ueberdeckt der Fluss der bewegten Kette die Paketbilanz (Paket eps = 1e-3)? Ist die Kette nach einem
     Anstoss instabil?
   - Einzelball: T und R ergeben bei allen vier k0 zusammen weniger als 1, am deutlichsten bei k0 = 0,22 (0,94985 und
     0,00482). Ob ein Rest des Pakets bei T = 700 noch unterwegs ist, steht nicht im Bericht.
8. **altern:**
   - Bei omega^2 = 0,55 faellt die Fensterladung von 3,87755 auf -0,93194 / -0,94514. Der Ball verliert mehr als seine
     ganze Ladung, und im Fenster bleibt negative Ladung.
   - Die Rate 6,774e-03 (Verhaeltnis 1,366) stammt aus einer Geraden ueber diesen Verlauf.
   - Bei 0,51 halbiert sich die Ladung (5,43118 -> 2,75540).
   - Frage: Ist das noch "Verdampfung eines Balls" im Sinne der Formel?
9. **symbiose:**
   - "abgestrahlt E" betraegt 1,5119 / 1,5085 / 1,5282 bei 0,71 / 0,72 / 0,74, mehr als der Anker-Gewinn beim
     Verschmelzen (0,4413 / 0,4341 / 0,4191 im Betrag).
   - Bei 0,72 sinkt D von D max 182,16 auf D Ende 166,49.
   - Frage: Hat ein Ball oder ein Bruchstueck die Daempfungsschicht der offenen Box erreicht? Dann waere "abgestrahlt"
     keine Strahlung.
   - Dazu: "Bindung Start" ist +0,19169 (gleichphasig) bzw. -0,19718 (gegenphasig), der PLAN nennt -J(10) = -0,017.
     Frage: Messen beide dieselbe Groesse (Energie der ueberlagerten Anfangsfelder gegen Paarenergie aus der
     Auslaeuferformel)?
10. **quorum, Atemamplitude:**
    - Sie waechst bei K = 12 zufall von 6,91e-02 auf 4,13e-01 und bei K = 16 von 1,29e-01 auf 2,95e-01.
    - Bei gleicher Phase und bei K = 2 bleibt sie konstant.
    - Schon im ersten Fenster ist sie bei K = 12 zufall 6,91e-02 gegen 1,59e-02 bei K = 12 gleich, bei gleicher
      Stossstaerke eta = 0,02.
    - Das ist nicht vorhergesagt; die Ursache steht nicht im Bericht.

### Aufloesungsgrenzen und Zaehlweisen

11. **pendeln und ir, FFT und L3:**
    - Omega_p bei D = 20 (0,01257) und D = 30 (0,01057) liegt in der Groesse von 2 pi/T fuer T = 600, also an der
      kleinsten aufloesbaren FFT-Frequenz. Die Vorhersagen dort (0,0054 und 0,0004) liegen darunter.
    - ir, D = 30: Omega_vib 0,4172 (Verhaeltnis 1048) bei eingefrorenem u ist keine Schwingungsfrequenz.
    - "L3 6 von 6" bzw. "5 von 5" entspricht der Zahl aller angestossenen Laeufe. Gezaehlt werden also bei pendeln
      D = 20 und 30 mit, bei ir D = 30.
    - Frage: Sollen eingefrorene Laeufe aus der L3-Zaehlung heraus?
12. **pendeln, freie Paare:** Die Zahl der Nulldurchgaenge haengt von der Stufe ab: 82 gegen 58 bei D0 = 7, 3 gegen 1
    bei D0 = 8. L3 prueft sie nicht.
13. **raeuber:**
    - Die Periode bei gleichphasig z0 = 0,3 (2483,2 / 2376,6) ist laenger als das Auswertefenster [T/6, T] bei T = 500
      und damit keine gemessene Periode.
    - "Summe rel." (Q_psi + Q_chi im Fenster) aendert sich um bis zu 3,9e-02 (gegenphasig z0 = 0,05); der PLAN setzt
      die Summe als erhalten voraus.
14. **tensid:** Omega nackt aendert sich von grob nach fein (0,70649 -> 0,70694) um mehr als die kleinsten dOmega
    (1,05e-04). dOmega selbst ist in beiden Stufen gleich.
15. **zellkern und mitochondrium nach dem Austritt:**
    - zellkern lam = +0,4: Der abgewanderte Ball ist aus dem Fenster (Q gehalten 0,0062 bis 0,0122), und "Abstand
      Ende" ist kleiner als "Abstand max", zum Beispiel 30,966 gegen 115,71.
    - mitochondrium lam = +0,3, v = 0,4: Abstand Ende 110,04 (grob) gegen 120,07 (fein).
    - Nach dem Austritt sind diese Zahlen nicht als Abstand zu lesen; die Klassen haengen nicht davon ab.

### Frage an die Leitung: kreuzen unter c_s (kein Befund)

- **Spaete Beschleunigung, Berichtszahlen:**
  - 0,48 c_s: 4,04e-06; bei 1,46 c_s: 4,56e-04, also rund zwei Zehnerpotenzen mehr
  - 0,76 c_s: 5,23e-05; 2,40 c_s: 6,52e-05
  - Die spaete Beschleunigung unter c_s liegt unter der Vorab-Schwelle |a| < 2e-5.
- **Ueberschlag aus Berichtszahlen (nicht im Bericht; a als Beschleunigung gelesen):**
  - v und a stammen aus Fits auf [T/3, T] = [100, 300].
  - Mit a = 4,04e-06 aendert sich v in diesen 200 Zeiteinheiten um etwa 8e-04. Das ist wenig gegen v Ende = 5,22e-03.
  - v Ende mal 200 ergibt etwa 1,04 der gesamten Verschiebung 1,273.
  - Bei 1,46 c_s ergibt dieselbe Rechnung etwa 9e-02, also so viel wie v Ende (8,51e-02).
- **Frage:** Hatte der Ball unter c_s seine Geschwindigkeit also schon vor t = 100 weitgehend und glitt danach fast
  gleichfoermig, waehrend bei 1,46 c_s die Geschwindigkeit im Fenster noch stark waechst? Dann saehe die Verschiebung
  eher nach einem fruehen Stoss aus als nach einer dauernden Kraft. Als moegliche Quelle nennt der PLAN (Abschnitt 8),
  dass das Anfangsfeld keine Loesung des gekoppelten Systems ist.
- **Nebenbeobachtung:**
  - Die Mitnahme ist nicht monoton in u: Verschiebung 1,273 / 3,742 / 18,300 / 3,142 bei 0,48 / 0,76 / 1,46 / 2,40
    c_s.
  - Frage: Gehoert das zur Gleit-Frage von Wellen 6?

## 3. Zusammenfassung

| Paket | Test (Karte) | Ergebnis kurz | Urteil | L3 laut Bericht | L1 | L2 | L3 | L4 | L5 | Vorschlag |
|---|---|---|---|---|---|---|---|---|---|---|
| R5-C | osmose (Bio 2) | Ball loest sich bei S = 0,8 bis 1,2 auf, auch bei omega_bg > omega; Phase dreht mit omega_bg | getroffen | 4/4 | ja | teilweise | bestanden | bekannt | nein | parken |
| R5-C | massenwirkung (Chemie 9) | alle drei Mischungen aufgeloest; Drehfrequenz Mitte 0,7845 bis 0,7894 | getroffen | 3/3 | ja | teilweise | bestanden | bekannt | nein | parken |
| R5-C | hintergrund (Papierprobe, Wellen 6, 7, 11) | S < 2/3 instabil, Formel gleich Scan; c_s 0,5547 bis 0,7471 | getroffen | entfaellt | ja | entfaellt | entfaellt | bekannt | nein | W6/7/11: Ein-Feld verwerfen, Zwei-Feld weiter |
| R5-C | pendeln (Bio 12) | Omega_p/Vorhersage 0,9479 bis 1,029, Steigung -0,2669; freie Paare mit zu vielen Nulldurchgaengen | teilweise | 6/6 | ja | haelt | bestanden | bekannt | nein | parken |
| R5-C | ir (Chemie 4) | Omega_vib/Vorhersage 0,9901 bis 1,091, kaum gedaempft | getroffen | 5/5 | ja | haelt | bestanden | bekannt | nein | parken |
| R5-C | symbiose (Bio 16) | kein Lauf "gebunden"; 0,72 und 0,78 trennen sich | teilweise | 6/6 | ja | haelt | bestanden | teilweise | nein | verwerfen |
| R5-C | quorum (Bio 39) | r steigt bei K = 16 auf 0,635 / 0,541; Kontrolle K = 2 reisst | verfehlt | 4/5 | ja | gerissen | teilweise | nein | nein | parken |
| R5-C | lawinen (Bio 50) | Riesenlawinen wie vorhergesagt, aber auch ohne Stoesse | teilweise | 5/5 | ja | gerissen | bestanden | nein | nein | verwerfen |
| R5-C | bragg (W21, v2) | Ketten-T von -14565 bis 14396, Kette bewegt sich | verfehlt | 19/22 | ja | teilweise | fraglich | bekannt | nein | parken |
| R5-C | anderson (W22, v2) | xi 4699 / 4505; periodische Kette daempft fast wie das Zufallsgas | teilweise | 3/3 | ja | gerissen | bestanden | bekannt | nein | parken |
| R5-D | zellkern (Bio 8) | Verschachtelung schon aus 1/m, keine Huelle mit Loch; m = 1,5 bei lam = -0,4 abweichend | teilweise | 9/9 | ja | haelt | bestanden | teilweise | nein | parken |
| R5-D | raeuber (Bio 15) | Josephson-Klassen wie vorhergesagt; Amplitude, Periode und Kontrolle "getrennt" daneben | teilweise | 12/12 | ja | teilweise | bestanden | bekannt | nein | verwerfen |
| R5-D | mitochondrium (Bio 35) | Gast ruht, wird bei v = 0,2 gefangen, entkommt bei 0,4; Ladungen gehalten | getroffen | 4/4 | ja | haelt | bestanden | teilweise | nein | weiter |
| R5-D | altern (Bio 48) | Gamma/Formel 0,610 bis 1,366; negative Endladung bei 0,55 | teilweise | 8/8 | ja | haelt | bestanden | teilweise | nein | parken |
| R5-D | tensid (Chemie 17) | chi an der Wand (0,574 bis 0,738), Wand breiter, Omega fast gleich | teilweise | 18/18 | teilweise | teilweise | bestanden | teilweise | nein | weiter |
| R5-D | kreuzen (Wellen 10) | Mitnahme ueber c_s; unter c_s Verschiebung 1,273 | teilweise | 12/12 | ja | haelt | bestanden | bekannt | nein | weiter |

Zaehlung: 5 getroffen, 9 teilweise, 2 verfehlt. Vorschlaege: 3 weiter, 9 parken, 3 verwerfen; dazu hintergrund mit
Wellen 6, 7 und 11 (im Ein-Feld-Modell verwerfen, im Zwei-Feld-Medium weiter).

## 4. Finns Zwei-Feld-Idee (schwere und leichte Teile)

zellkern und mitochondrium zeigen: Ein schwererer zweiter Kanal (m = 1,5 bis 2,5) sitzt schon ohne Kopplung schmaler
im Ball des leichteren Feldes (K = 0,667 und 0,400 = 1/m), bleibt bei Anziehung beisammen (Abstand 0,003 bis 0,021)
bzw. als kleiner Gast gefangen (v = 0,2, fuenf Durchgaenge, alle Ladungen zu mindestens 0,9985 gehalten), trennt sich
bei Abstossung nach t = 20,0 bis 25,5 und entkommt bei v = 0,4; eine Huelle mit Loch entstand in keinem Lauf. tensid
zeigt, dass ein zweites Feld gleicher Masse mit Wandkopplung an der Wand des Balls sitzt (Wandanteil 0,574 bis 0,738),
die Wand verbreitert (dw bis 5,33e-02) und dabei die grosskanonische Wandenergie um hoechstens 8,38e-04 aendert.

## Einfach gesagt

Wir haben 16 kleine Computerversuche ausgewertet, in denen Q-Baelle als Zellen, Molekuele oder Boote gedacht werden.
Gut vorhergesagt war zum Beispiel, wie schnell Ladung und Abstand zwischen Nachbarbaellen hin- und herschwingen, dass
ein Ball in einem dichten Feldmeer einfach zerfliesst und dass ein kleiner Ball aus einem zweiten, schwereren Feld in
einem grossen Ball wohnen kann. Bei mehreren Versuchen haben die Kontrollen versagt: Der Lawinenzaehler zaehlt auch ohne
Stoesse Lawinen, und die Durchlaessigkeit der Ballkette kam mit unmoeglichen Werten heraus; diese Ergebnisse zaehlen
deshalb nicht. Offen ist, warum ein Ball in einer langsamen Stroemung doch ein Stueck mitrutscht, obwohl wir dort keine
Kraft erwartet hatten; ob das nur ein Schubs am Anfang war, prueft die Leitung.
