# Runde 6, Ernte C: M1 (Medium 1D), M2 (Medium 2D), Paket 2D-B (Kollektiv und Kristall)

- **Beginn:** 2026-09-30 04:08:19 CEST (gemessen mit date)
- **Ende:** 2026-09-30 04:33:33 CEST (gemessen mit date nach dem Schreiben)
- **Bearbeiter:** Anthropic-Agent (Opus 5.5), reine Lese- und Schreibaufgabe, explorativ (v3). Kein Programm gestartet;
  gelesen mit Read, grep, sed, jq.
- **Quellen** (Pfade unter coordination/runden-v3/):
  - M1: RUNDE-06/medium1d/PLAN.md; lauf-69/<test>/medium1d_<test>_bericht.txt (9 Tests); lauf-69/LAUF1.log
  - M2: RUNDE-06/medium2d/PLAN.md; lauf-69/ausgabe/{magnus,kielwasser,wirbel,brechung}*_bericht.txt; lauf-69/LAUF1.log
  - 2D-B: RUNDE-05/r5-2d-b/PLAN.md; lauf-69/ausgabe/*_bericht.txt (8 Karten); lauf-69/LAUF1.log, LAUF2.log
  - Gegenlesen: RUNDE-06.md Z. 33-34 und 337-350; Chat-Aussage der Leitung zu "ringe"; RUNDE-07.md Z. 23
- **Kennzeichen:**
  - "HR": von Hand aus Berichtszahlen gerechnet (kein Programm).
  - "(JSON)": aus der ergebnis.json desselben Laufs; steht nicht im Berichtstext.
  - "(Code)": im Skript nachgelesen.
- **Logs:** In allen drei Paketen sind die "ende ... rc="-Zeilen vollstaendig, alle rc=0.
  - M1: 10 von 10 (Rauchtest plus 9), p4000a, 01:47:23 bis 02:05:21 UTC
  - M2: 9 von 9 (Rauchtest plus 8), p4000b, 01:35:06 bis 02:07:43 UTC
  - 2D-B: LAUF1 5 von 5 (p4000a), LAUF2 4 von 4 (p4000b)
  - Der Fehler "Startskript ueberschrieben" trifft hier nicht zu.

## 1. Je Test

Latten je ein Wort: L1 kann scheitern, L2 Gegenprobe, L3 Numerik, L4 schon bekannt, L5 Messbezug. L4 und L5 folgen den
Vorschlaegen in den PLAN-Tabellen.

### 1.1 M1 Medium-Karten 1D (C0 = 0,1, g4 = 0,5, lam = 0,1; c_s = 0,2085; F_MIN = 2e-6)

#### M1-W5 landau (Landau-Schwelle)

- **Vorhersage (PLAN 2.1):**
  - V5a: "|F| < F_MIN bei u <= 0,05 (C0 = 0,1) und u <= 0,15 (C0 = 0,3)"
  - V5b: "u_c/c_s = 0,55 +- 0,2 bei C0 = 0,1 ... und 0,75 +- 0,15 bei C0 = 0,3"; Schwelle waechst mit C0 um "Faktor
    1,5 bis 2,5 statt 1,54"
  - V5c: "Ueber der Schwelle ist F > 0 ..., bei u = 0,30 und C0 = 0,1 zwischen 5e-4 und 2e-3. Zwischen v_c und c_s
    schwankt F stark (Dunkelsolitonen, F_std gross)"
  - V5d: "u = 0,10 (0,48 c_s): |F| < F_MIN"
- **Ergebnis** (grob; fein gleich auf 2 bis 3 Stellen):
  - C0 = 0,1, F_med bei u/c_s: 1,62e-7 (0,24), 1,41e-6 (0,38), 5,77e-6 (0,48), 2,32e-5 (0,58), 9,11e-5 (0,67),
    3,27e-4 (0,77), 8,54e-4 (0,86), 1,28e-3 (1,01), 1,18e-3 (1,20), 1,33e-3 (1,44), 7,36e-4 (1,92)
  - C0 = 0,3: -9,15e-9 (0,31), 1,51e-8 (0,47), 9,60e-7 (0,59), 2,99e-5 (0,72), 1,15e-3 (0,84), 3,04e-3 (0,96),
    2,82e-3 (1,12), 1,88e-3 (1,40)
  - Schwelle nach Code-Regel (Uebergang ueber F_MIN): u_c = 0,090, u_c/c_s = 0,43 (Klammer 0,38 bis 0,48) bei C0 = 0,1;
    u_c = 0,210, u_c/c_s = 0,65 (Klammer 0,59 bis 0,72) bei C0 = 0,3
  - Verhaeltnis u_c(0,3)/u_c(0,1) = 2,33 (HR), mit den Klammergrenzen mindestens 1,9 (HR); c_s-Verhaeltnis 1,54
  - Kontrollen:
    - u = 0: -3,66e-19
    - lam = 0 und Medium allein: 0,00e+00
    - Spiegel u = -0,25: -1,18e-3, gegengleich zu +0,25
    - langsame Rampe bei u = 0,10: 7,06e-6 gegen 5,77e-6; Differenz 1,3e-6 < F_MIN (E3 formal erfuellt)
  - **Plateau E1** (PLAN 1.3: Fensterhaelften auf 10 %, unter F_MIN auf F_MIN; HR aus den Haelftenwerten):
    - An allen vier Klammerpunkten nicht erfuellt: u = 0,08: 3,32e-6 / 3,88e-7; u = 0,10: 1,10e-5 / 2,43e-6;
      C0 = 0,3, u = 0,19: 3,17e-6 / 8,62e-8; u = 0,23: 5,47e-5 / 1,36e-5.
    - Insgesamt erfuellen 7 von 20 Hauptpunkten E1.
- **Urteil: teilweise.**
  - V5a getroffen.
  - V5b getroffen: Beide Werte liegen im Band, Faktor 2,33 im Band 1,5 bis 2,5.
  - V5c getroffen: 1,33e-3. F_std/F betraegt zwischen u_c und c_s 13 bis 100 %, darueber 2,5 bis 24 % (HR).
    "Dunkelsolitonen" steht nicht im Bericht.
  - V5d verfehlt: 5,77e-6 ist 2,9 F_MIN. Damit greift die L1-Regel des PLAN ("stationaere Kraft >= F_MIN bei
    0,48 c_s"), aber die Kraft ist dort nicht stationaer (E1).
- **L3:** 22 von 22 bestanden; Plateau E1 an der Schwelle nicht bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 teilweise, L4 ja, L5 nein.
- **Vorschlag: weiter.** Alle Klammerpunkte fallen im Fenster noch ab. Ein laengeres Messfenster entscheidet, ob bei
  0,4 bis 0,5 c_s eine Kraft bleibt.

#### M1-EIN einschwingen (Klaerung "kreuzen")

- **Vorhersage (PLAN 2.3):**
  - V-E1: "ploetzlich n = 10 gibt x(300) = 1,27 +- 0,05 und v[100, 300] = 5,2e-3 +- 5 % wie r5d"
  - V-E2: "adiabatisch u = 0,0994: nach dem Hochfahren gleichfoermig, |a| < 1e-7 auf [370, 570] ..., und
    v_b = (0,07 bis 0,21) u"
  - V-E3: "ploetzlich u = 0,0994 spaet ebenfalls |a| < 1e-6 ...; ploetzlich gehalten: F_med spaet < F_MIN"
  - V-E4: "u = 0,3044 (1,46 c_s): a > 1e-4 in beiden Faellen"
  - V-E5: "u = 0,1578 (0,76 c_s) folgt landau: ist dort u_c < 0,16, beschleunigt auch der adiabatische Ball"
- **Ergebnis:**
  - ploetzlich, frei, u = 0,0994: x(300) = +1,2728; v, a auf [100, 300] = 5,22e-3, 4,04e-6; auf [370, 570] =
    5,45e-3, 2,51e-8; F_med spaet 5,81e-8
  - adiabatisch, frei, u = 0,0994: x(300) = +0,1114; [100, 300]: 4,47e-4, 1,02e-5; [370, 570]: 3,43e-3, 1,69e-6;
    F_med spaet 3,82e-6; v_b/u = 0,035 (HR)
  - ploetzlich, gehalten: F_med spaet 5,35e-7
  - u = 0,1578: a spaet 4,85e-5 (adiabatisch), 9,30e-6 (ploetzlich)
  - u = 0,3044: a spaet 3,06e-4 (ploetzlich), 3,77e-4 (adiabatisch)
  - Kontrollen: lam = 0: v = -1,32e-8 (grob), 0 (fein); Medium allein: C-Spanne 6,63e-15 bzw. 8,83e-15
- **Urteil: teilweise.**
  - V-E1, V-E3, V-E4 und V-E5 getroffen; der Nachbau trifft r5d auf alle gedruckten Stellen.
  - V-E2 verfehlt: a = 1,69e-6 liegt 17-mal ueber 1e-7, und v_b/u = 0,035 liegt unter 0,07.
- **L3:** 14 von 14 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: weiter**, zusammen mit landau. Der ploetzliche Nachbau ist spaet unter F_MIN, der adiabatisch
  aufgebaute Ball nicht. Welcher Zustand der stationaere ist, zeigt erst ein laengerer Lauf.

#### M1-W6 gleiten

- **Vorhersage (PLAN 2.2):**
  - V6a: "Maximum der Kraft bei u = 0,25 bis 0,45 (lam = 0,1)"
  - V6b: "F(0,9)/F_max < 0,1 bei lam = 0,1 und < 0,2 bei lam = 0,3"
  - V6c: "Das Maximum bei lam = 0,3 liegt nicht unter dem bei lam = 0,1"
- **Ergebnis:**
  - lam = 0,1, F bei u: 1,18e-3 (0,25), 1,33e-3 (0,30, groesste), 1,06e-3 (0,35), 7,36e-4 (0,40), 2,23e-4 (0,50),
    3,92e-5 (0,60), 2,82e-6 (0,70), 2,44e-7 (0,80), 4,60e-9 (0,90); Bericht "F(0,9)/F_max = 0.000"
  - lam = 0,3: 7,86e-3 (0,30, groesste und zugleich kleinster Rasterwert), 3,02e-3 (0,50), 9,18e-5 (0,70),
    3,25e-7 (0,90)
  - landau ergaenzt F(0,21) = 1,28e-3. Zwischen 0,21 und 0,30 ist der Verlauf flach (1,28 / 1,18 / 1,33 e-3).
  - Spiegel u = -0,50: -2,23e-4, gegengleich
  - **Fallenbilanz** F_med + F_Falle = 0 ab u = 0,6 verletzt:
    - lam = 0,1, u = 0,8: 2,44e-7 gegen -1,82e-5; u = 0,9: 4,60e-9 gegen -6,76e-6
    - lam = 0,3, u = 0,7: 9,18e-5 gegen -4,68e-6; u = 0,9: 3,25e-7 gegen -9,45e-5
    - "S gehalten" 0,9273 (lam 0,3, u 0,5) und 1,0434 (u 0,7) verletzt E2 (1 %).
- **Urteil: getroffen, V6c offen.**
  - V6a und V6b getroffen; bei u = 0,9 liegt F unter F_MIN (Minimum, obere Schranke).
  - V6c ist nicht entscheidbar, weil das Maximum bei lam = 0,3 am unteren Rasterrand 0,30 liegt.
- **L3:** 13 von 13 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 teilweise (Fallenbilanz), L4 ja, L5 nein.
- **Vorschlag: parken.** Der Verlauf ist wie vorhergesagt und als 1D-Hindernisphysik bekannt; offen ist nur die Lage
  des Maximums bei lam = 0,3.

#### M1-W7 windschatten

- **Vorhersage (PLAN 2.4):**
  - V7a: "u = 0,05: alle dF < F_MIN"
  - V7b: "u = 0,35, d >= 10: hinten/allein = 1,00 +- 0,15"
  - V7c: "vorn/allein weicht bei mindestens zwei der vier Abstaende um mehr als 0,2 von 1 ab und folgt dem Vorzeichen
    von cos(k' d) oder seinem Gegenteil (Korrelation |r| > 0,7)"
- **Ergebnis** (u = 0,35 grob, fein in Klammern wo abweichend):
  - hinten/allein: 5,579 (d = 6), 2,464 (2,489) (d = 10), 1,266 (d = 16), 0,954 (d = 24)
  - vorn/allein: 0,143, 0,217 (0,115), -0,142, -0,125; cos(k_w d): -0,75, +0,99, -0,64, -0,97
  - u = 0,05: dF an 6 von 8 Stellen ueber F_MIN; d = 16 und 24 vorn 4,19e-6 und 5,71e-6, grob gleich fein
  - statische Referenz u = 0, d = 10: grob +7,58e-5 / -1,03e-4, fein +1,89e-4 / -1,30e-4 (nicht gegengleich, nicht
    gitterstabil); dF vorn bei u = 0,05, d = 10 wechselt das Vorzeichen (3,36e-5 grob, -8,26e-5 fein)
- **Urteil: verfehlt.**
  - V7a verfehlt.
  - V7b verfehlt bei d = 10 und 16, getroffen bei d = 24.
  - V7c teilweise: Abweichung > 0,2 an allen vier Abstaenden; Vorzeichen passt an 3 von 4 (nicht d = 6). Die
    Korrelation steht nicht im Bericht; HR (Pearson ueber die vier Werte): r = 0,71 grob, 0,53 fein.
  - In Zahlen: Bei kleinem d spuert der hintere Ball das 1,3- bis 5,6-fache der Einzelkraft, der vordere 0,1 bis 0,2
    davon oder eine kleine Gegenkraft.
- **L3:** 7 von 8. Welche Kenngroesse fehlt, steht nicht im Bericht; nach den Werten am ehesten d = 10 vorn
  (2,30e-4 grob gegen 1,21e-4 fein).
- **Latten:** L1 ja, L2 teilweise (d = 10-Referenz), L3 teilweise, L4 teilweise, L5 nein.
- **Vorschlag: weiter.** Das Ergebnis widerspricht dem Vorhersagebild deutlich. Vor jeder Deutung muessen die
  d = 10-Referenz und die Stationaritaet (Fensterhaelften fehlen im Bericht) nachgerechnet werden.

#### M1-W11 fahrtwind (Lorentz-Codeprobe)

- **Vorhersage (PLAN 2.5):**
  - V11a: "|F_B - F_A| <= max(0,05 |F_A|, 5e-7) bei allen drei u"
  - V11b: "F_C - F_A ist bei 0,35 und 0,60 deutlich (> 10 % von F_A) und hat das Vorzeichen der Steigung von F(u) aus
    gleiten zwischen u_G und u. Bei 0,05 sind alle ~0."
- **Ergebnis:**
  - u = 0,05: F_A 3,46e-8, F_B 1,00e-7, F_B - F_A = 6,57e-8
  - u = 0,35: F_A 1,12e-3, F_B 1,04e-3, F_B - F_A = -8,41e-5 (grob), -8,57e-5 (fein), also 7,5 % von F_A (HR)
  - u = 0,60: F_A 3,91e-5, F_B 4,00e-5, Differenz 9,24e-7 (2,4 %, HR)
  - F_C - F_A: -1,90e-10 (0,05), +7,73e-5 (0,35; 6,9 % von F_A, HR), +1,36e-4 (0,60; das 3,5-fache von F_A, HR)
  - Spiegel A(-0,35) = -1,12e-3, gegengleich
  - Messfenster [420, 620] (JSON t_mess). gleiten misst auf [370, 570] und gibt bei 0,35 F = 1,06e-3; das sind 6 %
    Fensterunterschied (HR).
  - Fallenbilanz bei 0,60 offen: A 3,91e-5 gegen -3,10e-5, B 4,00e-5 gegen -2,32e-5
- **Urteil: teilweise.**
  - V11a: bei 0,05 und 0,60 getroffen, bei 0,35 verfehlt (7,5 % > 5 %).
  - V11b: bei 0,05 und 0,60 getroffen, bei 0,35 verfehlt (6,9 % < 10 %). F_C > F_A passt dazu, dass F in gleiten
    zwischen 0,30 und 0,35 faellt; der Wortlaut "Vorzeichen der Steigung" ist dafuer mehrdeutig.
- **L3:** 3 von 3 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 ja, L5 nein.
- **Vorschlag: weiter als Codeprobe.** Die 7,5 % bei 0,35 liegen in der Groesse der Fensterabhaengigkeit (6 %).
  Ein laengeres, gleiches Fenster fuer A und B trennt beides.

#### M1-W3 stokes

- **Vorhersage (PLAN 2.6):**
  - V3a: "Exponent aus v_Ende und aus x nach Durchgang (a = 0,2 gegen 0,05): 2,0 +- 0,3; Richtung +x"
  - V3b: "Welle auf dem Ball: Verschiebung ~ a (Verhaeltnis a = 0,2/0,1 zwischen 1,7 und 2,3)"
  - V3c: "Spiegel kehrt das Vorzeichen um; lam = 0 gibt 0 exakt"
- **Ergebnis** (a = 0,05 / 0,1 / 0,2):
  - x nach Durchgang +3,509e-3 / +1,384e-2 / +5,542e-2
  - x Ende +3,140e-4 / +1,270e-3 / +5,397e-3
  - v Ende -1,39e-5 / -5,61e-5 / -2,31e-4
  - Exponent v, x: 2,03, 1,99
  - Welle auf dem Ball: x nach Durchgang -0,8321 (a = 0,1) und -1,624 (a = 0,2), Verhaeltnis 1,95 (HR); v Ende
    -1,55e-3 und -3,00e-3
  - Kontrollen: Spiegel gegengleich; lam = 0: x = -3,061e-6 (grob), -1,526e-6 (fein); ohne Welle -3,093e-6 /
    +1,549e-6; Medium allein 0
- **Urteil: teilweise.**
  - V3a: Exponent getroffen. Die Richtung +x gilt nur fuer x nach Durchgang: v Ende zeigt nach -x, und x Ende ist
    etwa ein Zehntel von x nach Durchgang.
  - V3b getroffen (1,95).
  - V3c: Spiegel getroffen. lam = 0 ist nicht exakt 0, liegt aber auf dem Niveau des Laufs ohne Welle.
- **L3:** 10 von 10 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: weiter (klein).** a^2 ist getroffen. Zu klaeren ist, warum der freie Ball nach dem Durchgang mit
  negativer Geschwindigkeit zuruecklaeuft (laengeres T, Impulsbilanz Ball plus Medium).

#### M1-B2 osmose

- **Vorhersage (PLAN 2.7):**
  - V2a: "Vorzeichenwechsel der Rate zwischen C = 0,15 und 0,25 ..., mit C_iso = 0,20 +- 0,03. Darunter verliert der
    Ball Ladung, darueber waechst er."
  - V2b: "C = 0: Rate/Formel zwischen 0,67 und 1,5"
  - V2c: "Rate(eps = 0,02)/Rate(eps = 0,01) zwischen 3 und 5 bei C = 0,10 und 0,30"
  - V2d: "Das isotone Gleichgewicht ist instabil"
- **Ergebnis** (grob):
  - Rate (psi plus chi) bei C = 0 / 0,10 / 0,15 / 0,20 / 0,25 / 0,30 / 0,35: -4,00e-4 / -7,18e-4 / -1,09e-3 /
    +5,26e-4 / -7,59e-4 / +6,46e-4 / +8,44e-4
  - nur psi: -3,89e-4 / -6,71e-4 / -1,02e-3 / -4,03e-4 / -3,53e-4 / +8,41e-4 / +8,77e-4
  - Code: "Vorzeichenwechsel der Rate (isoton) bei C = 0.184" (fein 0,185)
  - omega Ball am Ende: 0,923 / 0,941 / 0,835 / 0,977 / 0,773 / 0,793 (C = 0,10 bis 0,35); Start 0,837
  - dQ gesamt bis -2,48 (C = 0,25) und -3,51 (eps 0,02, C 0,30); Start-Q laut PLAN 2,441
  - Vakuum: Rate -4,00e-4 gegen Formel -7,441e-4, Verhaeltnis 0,54 (HR)
  - eps = 0,02: -9,24e-4 bei C 0,10 (Verhaeltnis 1,29, HR); -1,25e-3 bei C 0,30 (Vorzeichen gegen eps 0,01
    umgekehrt)
  - Das Vorzeichen der Rate folgt in allen 7 Laeufen mit |mu-Differenz| > 0,01 der mu-Differenz am Ende (HR).
  - Kontrollen: eps = 0 grob -2,09e-11, **fein 3,10e-5**; Medium allein etwa 0; Q_psi + Q_chi auf 1e-14 erhalten
- **Urteil: teilweise.**
  - V2a nur formal getroffen: Der erste Wechsel liegt bei 0,184, im Band. Die Rate wechselt aber dreimal das
    Vorzeichen (C = 0,25 negativ), und die reine psi-Rate wechselt erst zwischen 0,25 und 0,30.
  - V2b verfehlt (0,54).
  - V2c verfehlt (1,29 bzw. Vorzeichenwechsel).
  - V2d teilweise: Alle nicht-isotonen Baelle driften weit weg. Bei C = 0,20 bleibt der Ball bis T = 800 nahe am Start;
    Instabilitaet ist dort nicht gesehen.
- **L3:** 9 von 9 bestanden.
- **Latten:** L1 ja, L2 teilweise (eps = 0 fein gerissen), L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: weiter.** Die Raten stammen von fast aufgeloesten Baellen. Noetig sind eine Messung vor der grossen
  Ladungsaenderung und die Klaerung der eps = 0-Kontrolle fein.

#### M1-C9 massenwirkung

- **Vorhersage (PLAN 2.8):**
  - VC9a: "Bei allen 6 nicht-isotonen Baellen (|mu - omega| > 0,01) hat die Rate das Vorzeichen von mu - omega"
  - VC9b: "Kein Massenwirkungsgesetz mit stabilem Verhaeltnis, sondern Reifung: Der Abstand der Ladungen waechst mit der
    Zeit, bei C = 0,2 auseinander"
  - VC9c: "Vakuum: alle drei verlieren Ladung"
- **Ergebnis:**
  - Code "Vorzeichen passt: 7 von 7", gezaehlt mit omega am Ende. Der beim Start isotone Ball omega^2 = 0,6 bei
    C = 0,1 zaehlt dabei mit. Nach Start-omega 6 von 6 (HR).
  - C = 0,2: dQ +1,201 (grosser Ball), +0,571 (mittlerer), -0,853 (kleiner); Raten am Ende +1,34e-3, +1,03e-3,
    -4,19e-4
  - Beim Start isotone Baelle: -2,03e-3 (C 0,1), +1,03e-3 (C 0,2), +3,20e-4 (C 0,3)
  - Vakuum: -7,92e-4, -5,35e-4, -3,94e-5
  - eps = 0: Raten hoechstens 1,4e-10; dQ gesamt je Ball +3,35e-2 (grob), +1,67e-2 (fein)
- **Urteil: getroffen.** VC9a, VC9b (bei C = 0,2 laufen die Ladungen bis T = 800 auseinander; ein stabiles Verhaeltnis
  ist nicht gesehen) und VC9c.
- **L3:** 8 von 9. Welche fehlt, steht nicht im Bericht; nach den Werten am ehesten C = 0,3, omega^2 = 0,8 (3,20e-4
  gegen 2,56e-4).
- **Latten:** L1 ja, L2 bestanden, L3 teilweise, L4 ja, L5 nein.
- **Vorschlag: parken.** Vorzeichen und Reifung wie erwartet (Ostwald, PLAN L4).

#### M1-B21 nische

- **Vorhersage (PLAN 2.9):**
  - V21a: "lam = +0,1 sanft: Umkehr bei x = -15 +- 2, Halbperiode 500 +- 150, zweiter Ausschlag >= 0,9 x der erste. Er
    bleibt nicht stehen"
  - V21b: "lam = -0,1 sanft: dasselbe Bild zum Buckel (+x); Spiegel: nach +x"
  - V21c: "lam = +0,2 steil: gedaempft, zweiter Ausschlag <= 0,7 x der erste. Der Ball bleibt bei der Delle x = -15 +- 5
    liegen"
  - V21d: "lam = 0: Ball bleibt auf 1e-6; Medium allein: Profil bleibt nach dem Einschalten stehen"
- **Ergebnis:**
  - lam +0,1: Umkehr (t = 792, x = -14,93); x Ende -0,389 bei T = 1300. Halbperiode und Amplitudenverhaeltnis "nan"
    (nur ein Umkehrpunkt). Von der Freigabe [200, 250] bis t = 792 vergehen 542 bis 592 (HR).
  - lam -0,1: Umkehr (763, +14,92), x Ende +0,092. Spiegel: (792, +14,93), x Ende +0,389.
  - lam +0,2 steil: Umkehr (748, -30,64) und (1254, +1,04); Halbperiode 507,0; Amplitudenverhaeltnis 1,044
  - lam = 0: x min..max 0,000 auf drei Stellen. Der Umkehrpunkt-Detektor meldet vier "Umkehrpunkte" mit Halbperiode
    15,0 (grob) bzw. 19,0 (fein).
- **Urteil: teilweise.**
  - V21a und V21b getroffen.
  - V21c verfehlt: ungedaempft (1,044), der Ball bleibt nicht liegen.
  - V21d: lam = 0 nur auf 5e-4 pruefbar (drei Nachkommastellen); Medium allein nicht im Bericht.
- **L3:** 6 von 6 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: parken.** Der Ball pendelt ungedaempft um die Nische, auch im steilen Fall.

### 1.2 M2 Medium-Karten 2D (C0 = 0,1, g4 = 0,5, lam = 0,1; c_s = 0,2085)

#### M2-W8/9 magnus

- **Vorhersage (PLAN 3.1):**
  - V-M1: "|dY - dY_Moeller| < 0,05 und |v_y| < 1e-4 (p = 0,8) ... Befund-Kandidat bei |dY - dY_Moeller| > 0,15 oder
    |v_y| > 3e-4"
  - V-M2: "fester Querversatz dY = m (Q/E) v_x, gleiches Vorzeichen wie m"
  - V-M3: "Nach der Rampe laeuft der freie Ball mit fester Geschwindigkeit v_x weiter (a_x etwa 0) ... m = 1: 0,05 bis
    0,17 und m = 0: 0,04 bis 0,12"
  - V-M4: "Bei 0,8 c_s entstehen chi-Wirbel mit p = 0,5 (m = +-1) bzw. p = 0,3 (m = 0)"
  - Stabilitaet: "Der m = 1-Ball bleibt heil (Windung 1, c2 < 0,05) ueber T = 400 mit p = 0,7"
- **Ergebnis:**
  - m = +-1, 0,4 c_s: dY +-4,417e-3, Moeller +-3,779e-3; v_y +-1,1e-6; v_x/u 0,040; a_x -2,86e-6 (JSON)
  - m = +-1, 0,8 c_s: dY +-3,628e-2, Moeller +-3,005e-2; v_y +-9,87e-5 (grob und fein); v_x/u 0,161; a_x +1,02e-4
    (JSON); F_x_mittel 1,20e-2 (JSON)
  - m = 0, 0,8 c_s: |Y| 2,4e-13; v_x/u 0,095; a_x +2,41e-5 (JSON)
  - chi-Zirkulation 0 und freie chi-Wirbel 0 in allen Laeufen; Windung von psi erhalten; c2 hoechstens 0,020
  - m = +1 in Ruhe: Windung 1, c2 0,000
  - Kontrollen:
    - Spiegel |Y(+1) + Y(-1)|: 1,20e-10 und 1,19e-10 (grob), 1,54e-9 (fein) gegen PLAN "< 1e-10"
    - m = 0: |Y| 2,3e-13; lam = 0: |dX| 1,8e-10, |Y| 1,8e-8; Medium allein: Spanne 0, Q_chi 1,000000
- **Urteil: teilweise.**
  - V-M1 getroffen (Code "V-M1 getragen"). Bei 0,8 c_s liegt v_y = 9,87e-5 aber nur 1,3 % unter der Schwelle 1e-4.
  - V-M2 im Vorzeichen getroffen; dY liegt 17 bis 21 % ueber m Q v_x/E (HR).
  - V-M3 verfehlt: Bei 0,8 c_s beschleunigt der Ball am Laufende noch (a_x 1,0e-4 bzw. 2,4e-5). Bei 0,4 c_s liegt
    v_x/u = 0,040 unter 0,05, und v_x/u ist nicht fest (0,040 gegen 0,161).
  - V-M4 nicht eingetreten (keine Wirbel; p = 0,5 bzw. 0,3 angesetzt).
  - Stabilitaet getroffen.
- **L3:** 9 von 9 bestanden (fein nur bei 0,8 c_s).
- **Latten:** L1 ja, L2 teilweise (Spiegel ueber 1e-10), L3 ja, L4 ja, L5 nein.
- **Vorschlag: Magnus parken, Laengskraft weiter.** Ohne Zirkulation gibt es keine Querdrift, wie erwartet. Die
  Laengsbeschleunigung bei 0,8 c_s ist die 2D-Seite der Landau-Frage.

#### M2-W4 kielwasser

- **Vorhersage (PLAN 3.2):**
  - V-K1: "RMS-Spitze ... innerhalb 6 Grad von a' = 49,2 / 31,9 / 20,8 Grad (u = 1,3 / 1,8 / 2,5 c_s)"
  - V-K2: "Bei 0,5 c_s ist die RMS-Amplitude im Ring kleiner als 10 % der Amplitude bei 1,3 c_s"
  - V-K3: "Widerstand F_x(0,5 c_s) kleiner als 10 % von F_x(1,3 c_s)"; dazu "Der Widerstand steigt ueber c_s mit u"
- **Ergebnis:**
  - Winkel gemessen 33,0 / 73,0 / 50,0 Grad (Abweichung -16,2 / +41,1 / +29,2); 50-%-Kante 87 / 87 / 86 bei einem
    Suchbereich von 8 bis 87 Grad
  - Amplitude 0,5 c_s / 1,3 c_s = 0,046; |F_x| 0,5 / 1,3 = 0,007; F_x(0,5 c_s) = -2,33e-4
  - F_x: 3,50e-2 (1,3), 4,52e-2 (1,8), 2,40e-2 (2,5)
  - Kontrollen: lam = 0 Amplitude 0, der Schaetzer gibt dabei trotzdem 87 / -8 Grad aus; Medium allein max|dC| 0;
    oben und unten symmetrisch
- **Urteil: teilweise.**
  - V-K1 verfehlt, alle drei (Code "verfehlt").
  - V-K2 und V-K3 getroffen.
  - "Steigt mit u" verfehlt: F_x ist bei 2,5 c_s kleiner als bei 1,8 c_s.
- **L3:** 9 von 9 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 ja, L5 nein.
- **Vorschlag: weiter, zuerst als Messmethode.** Die 50-%-Kante sitzt immer am Suchrand, und der Schaetzer liefert auch
  ohne Signal einen Winkel. So ist nicht entscheidbar, ob der Machkegel fehlt oder nur nicht gemessen wird.

#### M2-W18 wirbel

- **Vorhersage (PLAN 3.3):**
  - V-W1: "Bei 0,4 c_s kein Wirbel. Die Schwelle liegt zwischen 0,55 und 0,85 c_s (p = 0,6)"
  - V-W2: "Wirbel entstehen paarweise (Gesamtwindung 0). Oben mit negativer, unten mit positiver Windung (p = 0,8)"
  - V-W3: "Die Abloesefrequenz steigt mit u; St zwischen 0,05 und 0,3 (p = 0,6)"; "Symmetrische Paarabloesung:
    p = 0,5"
  - V-W4: "lam = 0: kein Wirbel, keine Kraft"
- **Ergebnis:**
  - Ereignisse: 0 (0,4 c_s), 0 (0,55), 2 (0,7; erste Zeit 351 grob, 352 fein), 4 (0,85; 253 / 252), 10 (1,0; 208).
    Code: "Schwelle zwischen u/c_s = 0.55 und 0.7".
  - Oben minus, unten plus, paarweise gleichzeitig auf eine Zeiteinheit (einmal drei: 656 / 659 bei 1,0 c_s).
    Ausnahme bei 1,0 c_s: Bei t = 644 treten auf beiden Seiten beide Vorzeichen auf.
  - mittlerer Abstand 283,0 (0,85; St 0,276) und 112,8 (1,0; St 0,591)
  - St aus dem Auftrieb 0,621 / 0,612 / 0,325 (Perioden 152,5 / 127,7 / 204,6); F_y RMS 3,5e-6 bis 1,2e-5
  - F_x: 3,84e-4 (0,4), 5,02e-3 (0,55), 4,03e-2, 6,20e-2, 8,64e-2
  - lam = 0: 0 Ereignisse, F = 0
- **Urteil: teilweise.**
  - V-W1, V-W2 und V-W4 getroffen; bei 1,0 c_s haben 2 von 10 Ereignissen das Gegenvorzeichen.
  - V-W3 teilweise: Die Frequenz steigt von 0,85 auf 1,0 c_s, und die Abloesung ist symmetrisch. St = 0,276 liegt im
    Band; 0,591 und alle St aus dem Auftrieb liegen ausserhalb.
- **L3:** 6 von 6 bestanden. Das fein-Urteil "Schwelle zwischen 0.0 und 0.7" ist ein Artefakt, weil fein nur 0,7 und
  0,85 gerechnet sind.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 ja, L5 nein.
- **Vorschlag: parken.** Schwelle und Paarbild passen zur BEC-Literatur (PLAN L4). Offen bleibt die Kraft ohne Wirbel
  bei 0,55 c_s (5,02e-3); sie gehoert zur Landau-Frage.

#### M2-W14 brechung

- **Vorhersage (PLAN 3.4):**
  - V-B1: "P1 haelt fuer alle sechs Stufenlaeufe (1 Grad, 2 %, Ausgang); p = 0,35"
  - V-B2: "Die Ausgaenge stimmen, einschliesslich der Reflexion bei abst50 (p = 0,8)"
  - V-B3: "m_a/M zwischen 0,02 und 0,15. Kontrolle: bei lam = 0 ist M*/(gamma M) = 1 auf 1e-3"
  - V-B4: "Kein Ladungsverlust (< 1e-3)"
  - V-B5: "Kein Wirbel"
- **Ergebnis** (grob; fein fuer abst20, abst40 und anz40 gleich auf 0,01 Grad):
  - th2 gemessen gegen P1: abst20 24,83 / 24,91; abst40 52,01 / 52,34; anz20 17,24 / 17,21; anz40 33,86 / 33,79;
    senkrecht 0,00 / 0,00
  - v2/P1 0,9863 bis 1,0056; P2 weicht hoechstens 0,03 Grad ab
  - abst50 (Reflexion erwartet): Ausgang "unklar", kein th2
  - Code-Urteil "P1 getragen (1 Grad, 2 Prozent, Ausgang)". In das Urteil gehen nur Laeufe mit gemessenem th2 ein
    (Code Z. 1355); abst50 ist damit nicht bewertet.
  - m mitgef. 0,216 bis 0,324 bei M_eff 22,755, also m_a/M 0,009 bis 0,014 (HR); lam = 0: -0,006, also M*/(gamma M)
    etwa 1 - 3e-4 (HR)
  - Q-Verlust (relativ, Code Z. 1352): anz20 2,1e-1; sonst 1,3e-7 bis 1,8e-4
  - Wirbel: nicht im Bericht; wirbel_max 0 in allen Laeufen (JSON)
  - Kontrollen: ohne Stufe +0,01 Grad; lam = 0 gerade; M_eff(lam = 0) gegen Vakuum -8,40e-6
- **Urteil: teilweise.**
  - V-B1 fuer 5 von 6 getroffen (abst50 unklar).
  - V-B2 teilweise: fuenf Durchlaeufe richtig, die Reflexion ist nicht gezeigt.
  - V-B3 verfehlt (m_a/M unter 0,02); die lam = 0-Kontrolle ist getroffen.
  - V-B4 bei anz20 verfehlt (21 %).
  - V-B5 getroffen (JSON).
- **L3:** 6 von 6 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: weiter.** Beide Pruefsteine sind offen: der Reflexionsfall abst50 (laengeres T) und der Ladungsverlust
  von anz20. Fuer anz20 die Zeitreihen Q_psi(t) und X(t) gegen den Beginn der Randschicht legen.

#### M2-W15 Linse und M2-W17 Kelvin-Helmholtz

- Nur Papier (PLAN 3.5, 3.6), nicht gerechnet. Keine Latten-Wertung.
- Vorschlag laut PLAN: Linse erst nach brechung; Kelvin-Helmholtz parken.

### 1.3 Paket 2D-B (Ein-Feld-Modell 2D; Ball omega^2 = 0,70, Q 24,0, d = 7,83)

#### 2DB-P paare (Grundlage)

- **Vorhersage (PLAN 2.3):**
  - Statik: "E_bind(d, 0) monoton, ohne Minimum (p = 0,9)"; "kappa_fit innerhalb 5 % von 0,548"
  - "gleich_s4, s5, s7: verschmolzen, p = 0,85. Erste Verschmelzung bei 5 bis 30, 10 bis 60 bzw. 20 bis 200"
  - "gegen_s4, s5: auseinander, p = 0,9. Die Phasendifferenz bleibt bei pi"
  - "quer_s4: Anfangsstrom |dQ_1/dt| / |B(Spalt 4)| in [0,7; 1,3] ... Danach Verschmelzen"
  - "einzel: ruhig, Q-Verlust < 1e-3"
  - Starrkoerper: "gleichphasig > 1,5 (p = 0,6) ..., gegenphasig in [0,7; 2]"
  - Abstandsgesetz: "d''(s4)/d''(s5) etwa e^kappa = 1,73 und d''(s5)/d''(s7) etwa e^{2 kappa} = 2,99, je innerhalb
    30 % (p = 0,5)"
- **Ergebnis:**
  - E_bind(dphi = 0) steigt monoton von -3,370 (Spalt 1) bis -0,0165 (Spalt 10); kappa_fit 0,5374, 1,9 % unter 0,5477
    (HR)
  - Erste Verschmelzung bei t = 5 / 10 / 35
  - gegen_s4 und gegen_s5 auseinander, Phase -3,142 am Start und am Ende
  - quer_s4: Strom/B = 0,864, danach verschmolzen (t = 15; max|dQ|/Q 0,925)
  - einzel: Q-Verlust 1,3e-8
  - dyn/statik gleichphasig 5,84 / 1,79 / 1,09 (s4 / s5 / s7), gegenphasig 1,22 / 1,28
  - Abstandsgesetz: 6,28 und 6,22
- **Urteil: teilweise.**
  - Statik, Klassen, Josephson-Strom und die gegenphasige Starrkoerperprobe getroffen.
  - Gleichphasig > 1,5 bei s4 und s5 getroffen, bei s7 nicht (1,09).
  - Abstandsgesetz verfehlt (6,28 statt 1,73; 6,22 statt 2,99).
  - Ein gebundenes gleichphasiges Paar ist nicht gesehen.
- **L3: nicht bestanden** (Bericht "bestanden": false; bei quer_s4 aendert sich d'' um 11,7 % > 10 %).
- **Latten:** L1 ja, L2 bestanden, L3 nein, L4 ja, L5 nein.
- **Vorschlag: weiter als Grundlage.** Die Paarbeschleunigung weicht um den Faktor 2 bis 4 vom e^(-kappa d)-Bild ab,
  und L3 fehlt. Beides sollte geklaert sein, bevor Paarkraefte fuer Vielball-Vorhersagen dienen.

#### 2DB-B25/42 und C13 gitter

- **Vorhersage (PLAN 3.3):**
  - alle "gleich": "verschmolzen, p = 0,9; erste Verschmelzung 5 bis 30 (Spalt 4) bzw. 20 bis 150 (Spalt 7); am Ende
    1 bis 3 Klumpen"
  - Q3_wechsel, Q4_wechsel: "auseinander, p = 0,8"; Q4_wechsel_s7: "auseinander p = 0,6"
  - D16_streifen: "verschmolzen (teilweise), Reihen zu Staeben ..., p = 0,6"
  - D16_drei: "auseinander p = 0,55; teilweise verschmolzen ... p = 0,35"
  - Q4_windung, D16_windung: "verschmolzen, p = 0,8; groesster Klumpen mit Windung +-1 ... p = 0,4"
  - Q4_zufall: "verschmolzen (teilweise) ..., p = 0,7"
  - Chemie 13: "kein Lauf mit gemischten Phasen haelt (p = 0,85)"; Bio 25/42: "kein Gitter haelt (p = 0,9)"
- **Ergebnis:**
  - gleich: Q3, Q4, D16 verschmolzen (ganz) bei t = 5; Q4_s7 bei t = 40; je 1 Klumpen am Ende
  - Q3_wechsel verschmolzen (teilweise, 4 von 9; t = 20); Q4_wechsel 4 von 16 (t = 30); Q4_wechsel_s7 auseinander
    (Rg bis 2,35)
  - D16_streifen 6 von 16; D16_drei 9 von 16; D16_windung 2 von 16; Q4_windung ganz; Q4_zufall 6 von 16
  - "halten_gefunden": [], "gemischte_phasen_halten": []
- **Urteil: teilweise.**
  - Kernaussagen getroffen: Kein Gitter und keine gemischte Anordnung haelt; gleichphasige verschmelzen in der
    vorhergesagten Zeit.
  - Verfehlt: Q3_wechsel und Q4_wechsel (teilweise verschmolzen statt auseinander) und D16_drei (Nebenausgang
    p = 0,35).
  - Die Windung des groessten Klumpens steht nicht im Bericht.
- **L3:** 5 von 5 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: verwerfen** (im Ein-Feld-Modell ohne Daempfung). In 12 Laeufen haelt kein Gitter, wie auf dem Papier
  erwartet.

#### 2DB-B46 und C19 ringe

- **Vorhersage (PLAN 4.3):**
  - N6_k0: "verschmolzen (ganz), kompakter Ball, Windung 0, p = 0,9"
  - N6_k3: "auseinander als symmetrische Halskette (alle 6 Klumpen bleiben), p = 0,9"; N6_k2: "auseinander, p = 0,7"
  - N5/N6/N7/N8_k1: "verschmolzen, p = 0,8. Am Ende Windung 1 im groessten Klumpen p = 0,35; kompakt mit Windung 0 ...
    p = 0,45"
  - N6_k1_dreh+: "ein Klumpen mit Windung +1 und J/Q etwa 1 (Ring schliesst sich zum drehenden Ball) p = 0,45"
  - N8_k1_dreh+: "wie N6_k1_dreh+, p = 0,45"; N6_k1_dreh-: "auseinander ..., p = 0,6"; N6_k0_dreh+: "verschmolzen,
    Windung 0, p = 0,7"
  - Kapsid: halten fuer ein N mit k = 1 "p = 0,15"; Chemie 19: "keiner (p = 0,8). Keine Sonderrolle von N = 6"
- **Ergebnis:**
  - N6_k0 ganz, W [0], R_Ring min 0,02; N6_k3 auseinander 6 -> 6 (Rg bis 4,76); N6_k2 auseinander
  - k = 1 ruhend: N5 teilweise 2 von 5, N6 teilweise 2 von 6 (beide W []: am Laufende kein Klumpen mehr, Q-Verlust
    94 bzw. 97 %; Code: Windung aus der letzten Analyse), N7 teilweise 3 von 7 (W [0, 0, 0]), N8 ganz mit W [1]
  - N6_k1_dreh+: ganz (6 -> 1, t = 5), W [1] grob und fein; J 181,6 -> 159,1; Q-Verlust 5,3 %; J/Q Start 1,042;
    R_Ring min 2,72
  - N8_k1_dreh+: ganz (8 -> 1, t = 5), W [1], nur grob; J 242,1 -> 214,4; Q-Verlust 8,5 %; J/Q Start 1,029
  - N6_k1_dreh-: auseinander (6 -> 6), alle W 0, J -48,3 -> -47,7
  - N6_k0_dreh+: ganz, W [0], J 78,6 -> 0,015, abgestrahlt 0,362
  - halten: keiner
- **Urteil: getroffen.**
  - Alle Klassen wie vorhergesagt; beim mitdrehenden Ring der p = 0,45-Ausgang "ein Klumpen mit Windung +1".
  - "J/Q etwa 1" am Ende steht nicht im Bericht, nur J/Q am Start.
  - In der ruhenden k = 1-Reihe gibt es Windung 1 nur bei N = 8.
- **L3:** 5 von 5 bestanden (N8_k1_dreh+ nur grob gerechnet).
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 mittelbar.
- **Vorschlag: weiter** (laeuft als Karte RING in RUNDE-07).
  - Zu pruefen: Profil und omega des Endklumpens gegen die m = 1-Familie, J des Klumpens statt J der Box, laengeres T.
  - Die Klumpenladung schwankt bis zum Ende zwischen 121,8 und 157,6 (JSON, N6_k1_dreh+).

#### 2DB-B11 gluehwurm

- **Vorhersage (PLAN 5.3):**
  - "Keine Phasen- und keine Frequenzsynchronisation in keinem Lauf (p = 0,9)"
  - "nah_gleich_atem: verschmolzen (ganz), p = 0,9"; "nah_zufall(_atem): teilweise verschmolzen, p = 0,6";
    "nah_wechsel_atem: auseinander, p = 0,8"
  - "Atmung: Die Amplitude faellt bis zum Endfenster auf unter die Haelfte (p = 0,6) ... Atemsynchron in keinem Lauf
    (p = 0,95)"
- **Ergebnis:**
  - phasensynchron, frequenzsynchron, atemsynchron: keiner
  - nah_gleich_atem ganz; nah_zufall_atem 4 von 8; nah_zufall 7 von 8; nah_wechsel_atem 7 von 8; mittel 6 von 8
  - weit (Kontrolle) "halten": r 0,241 -> 0,540, sigma_om 9,53e-3 -> 9,50e-3
  - Atem-Amplitude steigt in 4 von 6 Laeufen (z. B. 4,44e-2 -> 7,12e-2). Unter die Haelfte faellt sie nur bei
    nah_gleich_atem (2,99e-2 -> 1,23e-2).
  - Omega_Atem 0,006 (nah, mittel) und 0,013 (weit). JSON: 0,006280 und 0,012560, also 1 und 2 mal 2 pi/1000,5 (HR).
    Das ist der erste und der zweite Frequenzschritt der Laufzeit.
- **Urteil: teilweise.**
  - Keine Synchronisation: getroffen.
  - Klassen getroffen ausser nah_wechsel_atem (verschmolzen statt auseinander).
  - Amplitudenabfall verfehlt.
- **L3:** 1 von 1 bestanden (nah_zufall_atem; Differenz r_Ende 5e-4).
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 ja, L5 nein.
- **Vorschlag: verwerfen** (im Ein-Feld-Modell). Keine Synchronisation, alle nahen Ringe verschmelzen. Die
  Atem-Kennzahlen liegen auf dem ersten Frequenzschritt und muessen vor einer Neuauflage repariert werden.

#### 2DB-B47 haendigkeit

- **Vorhersage (PLAN 6.3):**
  - "plus9 (und Spiegel): auseinander, p = 0,7"
  - "Spiegelprobe bis t_rand unter 1e-6: p = 0,8 bei plus9, p = 0,6 bei misch_a"
  - "misch_a, misch_b: teilweise verschmolzen. +1/-1-Paare verlieren die Windung, +1/+1-Paare geben Windung 2"
  - "eta-Drift in zufaelliger Richtung. Keine Bevorzugung"; "einzel_plus: ruhig, Windung 1 bleibt, p = 0,85"
- **Ergebnis:**
  - plus9 und Spiegel auseinander (Rg bis 1,876), W je 9 mal +-1, J +3250 -> +2081 und gegengleich
  - Spiegelprobe max|J_a + J_b|/max|J_a|: plus9 8,4e-16; misch_a 1,08e-4
  - misch_a 5 von 9, misch_b 6 von 9; alle Endklumpen W 0; eta +0,111 -> 0 (Spiegel -0,111 -> 0), misch_b
    +0,114 -> 0
  - einzel_plus ruhig, W [1], Q-Verlust 6,7e-9
  - misch_b: J +523 -> -1441
- **Urteil: teilweise.**
  - plus9, einzel_plus und "keine Bevorzugung" getroffen.
  - Spiegelprobe misch_a verfehlt (1,08e-4 > 1e-6; Zeitpunkt nicht im Bericht).
  - Windung 2 nicht gesehen (alle Endklumpen W 0).
- **L3:** 2 von 2 bestanden.
- **Latten:** L1 schwach, L2 teilweise, L3 ja, L4 ja, L5 nein.
- **Vorschlag: parken.** Keine Haendigkeit, wie die Symmetrie verlangt. Die Spiegelabweichung bei misch_a mit
  Zeitverlauf pruefen; frueh hiesse laut PLAN 13 Codefehler.

#### 2DB-C5 isomere

- **Vorhersage (PLAN 7.2):**
  - "E(Dreieck) - E(Kette) < 0 fuer gleiche Phasen ... die Formprobe gab -1,03, also etwa 16 % Dreikoerperanteil"
  - "(0, pi, 0): Formprobe -0,56. Auf dem Messgitter muss das Vorzeichen bleiben (p = 0,9)"
  - "Alle gleichphasigen verschmelzen (p = 0,9), das Dreieck zuerst (p = 0,6)"
  - "kette_wechsel und knick_wechsel: auseinander (p = 0,75)"
  - "dreieck_wechsel: verschmolzen (teilweise, 2 von 3); der pi-Ball wird ausgestossen (p = 0,6)"
  - "Umwandlung Kette -> Dreieck (Winkel <= 75 Grad ohne Verschmelzen): p = 0,05"
- **Ergebnis:**
  - E(Dreieck) - E(Kette) = -1,027 (gleich) und -0,562 (wechsel); Dreikoerperanteil Dreieck gleich -0,163, Dreieck
    wechsel +1,747
  - Alle drei gleichphasigen verschmolzen bei t = 5,0, also gleichzeitig
  - kette_wechsel und knick_wechsel auseinander; dreieck_wechsel 2 von 3 (t = 10)
  - Code: "umwandlung_kette_zu_dreieck": ["knick_wechsel"] (Winkel min 42,7 Grad), obwohl der Lauf "auseinander" ist
    (dNN bis 4,45)
- **Urteil: teilweise.**
  - Energie, Vorzeichen und Klassen getroffen.
  - "Dreieck zuerst" ist nicht entscheidbar (alle bei t = 5, Analyse alle 5).
  - "pi-Ball ausgestossen" steht nicht im Bericht.
  - Umwandlung: Das Kriterium spricht an, aber in einer auseinanderlaufenden Anordnung, also ohne gebundenes Dreieck.
- **L3:** 6 von 6 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: parken.** Isomere mit Barriere sind nicht gesehen. Das Umwandlungskriterium braucht eine
  Abstandsbedingung, bevor es wieder zaehlt.

#### 2DB-B26/40 kollektiv

- **Vorhersage (PLAN 8.3):**
  - "schleim_gleich aggregiert p = 0,5, vergroebert p = 0,45; schleim_zufall vergroebert p = 0,7"
  - "kein Schwarm (p = 0,9). schwarm_gleich vergroebert p = 0,8, schwarm_zufall vergroebert p = 0,6"
- **Ergebnis:**
  - schleim_gleich vergroebert (5 von 12, groesster Anteil 0,662); schleim_zufall vergroebert (6 von 12)
  - schwarm_zufall vergroebert (7 von 12; Polarisation 0,661 -> 0,548)
  - schwarm_gleich aggregiert (4 von 12, Anteil 0,733; Polarisation 0,457 -> 0,392)
  - Phasenordnung schwarm_zufall 0,114 -> 0,833 (grob und fein)
- **Urteil: teilweise.**
  - Kein Schwarm getroffen; schleim_zufall und schwarm_zufall getroffen; schleim_gleich mit dem Nebenausgang
    (p = 0,45).
  - schwarm_gleich verfehlt (aggregiert statt vergroebert).
- **L3:** 2 von 2 bestanden.
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: parken.** Nur lokales Verschmelzen, kein Schwarm. Der Anstieg der Phasenordnung auf 0,833 hat im PLAN
  kein Kriterium und bleibt eine Notiz.

#### 2DB-W19 profile (Auge des Tornados)

- **Vorhersage (PLAN 9.2):** "Meine Erwartung vorher: Saettigung, p = 0,6" (Regel |s| <= 0,1); "Erwartung: naeher am
  Kapillarloch, p = 0,65"
- **Ergebnis:**
  - Alle 7 m = 1-Profile gueltig, auch 0,52; Virialrest hoechstens 6,8e-11
  - R_kern_halb 2,951 / 2,544 / 2,131 / 2,012 / 2,021 / 2,109 / 2,275 (omega^2 0,52 bis 0,80; Q 1798 bis 60)
  - s (4 groesste Q) = 0,131; s (alle) = 0,104
  - mittlere Abweichung Kapillarloch 0,31, Heilungslaenge 1,18
  - Code: "Kern haengt schwach von Q ab (Zwischenbereich); naeher am Kapillarloch"
- **Urteil: teilweise.**
  - Saettigung knapp verfehlt (0,131 > 0,1; Klasse "schwach").
  - "Naeher am Kapillarloch" getroffen.
  - R_kern ist nicht monoton in Q (Minimum 2,012 bei omega^2 = 0,65).
- **L3:** nicht grob gegen fein; die PLAN-Latte "Klammer, Virialrest" ist bestanden (Klammer 4,4e-16).
- **Latten:** L1 ja, L2 bestanden, L3 ja, L4 teilweise, L5 nein.
- **Vorschlag: parken.** Der Kern waechst nur schwach mit Q und hat ein Minimum; ohne Messbezug bleibt das eine
  Profilnotiz.

## 2. Drei Kernfragen (nur aus den Berichten)

### 2.1 Gibt es eine Landau-Schwelle im stabilen Medium, und wo liegt sie relativ zu c_s?

- **Nach der Code-Regel ja:** Die Schwelle ist der Uebergang der Kraft ueber F_MIN = 2e-6.
  - C0 = 0,1: u_c/c_s = 0,43 (Klammer 0,38 bis 0,48).
  - C0 = 0,3: u_c/c_s = 0,65 (Klammer 0,59 bis 0,72).
  - Beide liegen unter c_s. Die Schwelle waechst mit der Dichte staerker als c_s: Faktor 2,33, ueber die Klammer
    mindestens 1,9, gegen 1,54.
- **Eine scharfe Kante ist nicht gesehen:**
  - Bei C0 = 0,1 steigt F stetig ueber fast vier Groessenordnungen: 1,62e-7 (0,24 c_s), 5,77e-6 (0,48 c_s), 8,54e-4
    (0,86 c_s).
  - Unter der Schwelle ist die Kraft kleiner als F_MIN (Minimum), nicht null.
  - An allen vier Klammerpunkten faellt die Kraft im Messfenster noch ab (E1 nicht erfuellt).
- **In 2D (M2)** gibt es ebenfalls Kraft unter c_s: wirbel F_x = 5,02e-3 bei 0,55 c_s ohne Wirbel; magnus a_x = 1,0e-4
  bei 0,8 c_s (JSON). Eine Schwelle ist dort nicht vermessen.

### 2.2 War das "kreuzen"-Rutschen aus Runde 5 ein Anfangsstoss, eine echte Kraft oder beides?

- **Die Verschiebung +1,27 war im Nachbau ein Anfangsstoss.**
  - Der ploetzlich gestartete Ball (r5d-Start) erreicht x(300) = +1,2728 bei v = 5,22e-3 und laeuft spaet mit
    5,45e-3 weiter.
  - Spaet ist a = 2,51e-8 und F_med = 5,81e-8, also unter F_MIN. Gehalten sieht er spaet 5,35e-7, ebenfalls unter
    F_MIN.
- **Nach adiabatischem Aufbau bleibt bei derselben Stroemung eine kleine Kraft ueber F_MIN.**
  - frei: 3,82e-6 (a = 1,69e-6); gehalten (landau u = 0,10): 5,77e-6, im Fenster abfallend (1,10e-5 auf 2,43e-6)
  - Ob sie stationaer bleibt, zeigen die Laeufe nicht.
- **Kurz:** Die kreuzen-Verschiebung war ein Anfangsstoss. Eine Dauerkraft bei 0,48 c_s ist nur nach adiabatischem
  Aufbau zu sehen und nicht als stationaer belegt; im Nachbau des kreuzen-Laufs selbst liegt sie spaet unter F_MIN.

### 2.3 Entsteht aus dem mitdrehenden Ring ein Ball mit Windung 1?

- **Im Sinn der Berichtskennzahlen ja.** N6_k1_dreh+ und N8_k1_dreh+ verschmelzen ganz zu einem Klumpen mit sicherer
  Windung 1 am Ende (W [1]). N6 ist grob und fein gerechnet, N8 nur grob.
- **Nicht belegt** ist, dass der Klumpen ein ruhiger m = 1-Q-Ball ist. Profil und omega fehlen im Bericht, und die
  Klumpenladung schwankt bis zum Ende zwischen 121,8 und 157,6 (JSON).
- Auch der ruhende Ring N8_k1 endet mit Windung 1. Bei N = 8 ist das Drehen dafuer nicht noetig.

## 3. Auffaelligkeiten

### 3.1 Widersprueche zur Vorhersage (die wichtigsten)

- M1 landau V5d und einschwingen V-E2: Kraft bzw. Beschleunigung bei 0,48 c_s ueber der Schwelle des PLAN (5,77e-6;
  1,69e-6).
- M1 windschatten: Der hintere Ball spuert bei d = 6 bis 16 das 1,3- bis 5,6-fache der Einzelkraft (Vorhersage 1,00 +-
  0,15); bei u = 0,05 liegt dF an 6 von 8 Stellen ueber F_MIN.
- M1 stokes: v Ende zeigt nach -x, obwohl die Verschiebung beim Durchgang nach +x geht.
- M1 osmose: Rate nicht monoton in C (Vorzeichen - / + / - / + bei 0,15 / 0,20 / 0,25 / 0,30); Vakuumrate 0,54 der
  Formel; eps-Skalierung 1,29 statt 3 bis 5.
- M1 nische steil: ungedaempft (Amplitudenverhaeltnis 1,044) statt gedaempft.
- M2 magnus V-M3: Der freie Ball behaelt keine feste Geschwindigkeit; bei 0,8 c_s a_x = 1,0e-4 (JSON).
- M2 kielwasser: Winkel 33 / 73 / 50 Grad statt 49 / 32 / 21; F_x faellt von 1,8 auf 2,5 c_s.
- M2 brechung: m_a/M 0,009 bis 0,014 statt 0,02 bis 0,15; anz20 verliert 21 % Ladung.
- 2D-B paare: Abstandsgesetz 6,28 / 6,22 statt 1,73 / 2,99.
- 2D-B gitter: Schachbrett-Gitter verschmelzen teilweise statt auseinanderzulaufen.

### 3.2 Gerissene Kontrollen

- M1 osmose eps = 0 fein: Rate 3,10e-5 gegen Schwelle 1e-7 (grob -2,09e-11).
- M1 landau E1-Plateau: an allen vier Schwellen-Klammerpunkten nicht erfuellt; insgesamt 7 von 20 Punkten.
- M1 gleiten:
  - Fallenbilanz ab u = 0,6 verletzt (bis Faktor 290 bei lam = 0,3, u = 0,9: 3,25e-7 gegen -9,45e-5; HR)
  - S gehalten 7,3 % bzw. 4,3 % daneben (E2 1 %)
  - C fern 0,0985 bei lam = 0,3, u = 0,9 (E7 1e-3 knapp verfehlt)
- M1 windschatten: statische Referenz d = 10 nicht gegengleich und grob/fein verschieden.
- M1 stokes und einschwingen: lam = 0 nicht "exakt 0" (x = -3,06e-6; v = -1,32e-8 grob), aber auf dem Niveau der Laeufe
  ohne Welle.
- M2 magnus Spiegel: 1,20e-10 / 1,19e-10 (grob) und 1,54e-9 (fein) gegen < 1e-10; physikalisch klein.
- M2 kielwasser: Winkelschaetzer liefert bei Amplitude 0 (lam = 0) Winkel 87 / -8 Grad.
- 2D-B haendigkeit: Spiegelprobe misch_a 1,08e-4 > 1e-6.

### 3.3 L3 nicht oder nicht voll bestanden

- 2D-B paare: nicht bestanden (quer_s4, d'' 11,7 % > 10 %).
- M1 windschatten 7 von 8, massenwirkung 8 von 9 (fehlende Kenngroesse jeweils nicht benannt).
- 2D-B ringe: N8_k1_dreh+ nur grob; die Aussage "aus 6 oder 8" hat fuer N = 8 keine L3.
- M2 wirbel: fein-Urteil "Schwelle zwischen 0.0 und 0.7" ist ein Artefakt der fehlenden feinen Laeufe.

### 3.4 Unplausible oder nicht belastbare Werte

- **J_Box ist keine geschlossene Bilanz.**
  - Laeufe mit J = 0 am Start: gitter D16_gleich 0 -> +22,1, D16_drei 0 -> +50,7, D16_streifen 0 -> -18,0; kollektiv
    schleim_gleich 0 -> -49,2.
  - Sonst: gitter Q4_windung +295,9 -> +399,5; ringe N8_k1 +136,7 -> +200,5 und N5_k1 +64,0 -> -52,3; haendigkeit
    misch_b +523 -> -1441.
  - Drehimpulsaussagen aus J_Box (auch bei den Ringen) sind damit nur eingeschraenkt belastbar.
- **ringe, Startladung** (JSON, HR): Q_Box(0) weicht von N mal Q_1 ab. N6_k1_dreh+ 174,3 statt 144,0 (+21 %),
  N8_k1_dreh+ 235,3 statt 192,0 (+23 %), N6_k1_dreh- 132,7 (-8 %). J/Q am Start haengt damit an der Ueberlagerung.
- **ringe, "Drehwinkel Ball 0":** -8,40 rad bei positivem J (N6_k1_dreh+); N6_k0 grob +0,00, fein -4,68. Nach dem
  Verschmelzen ist der Wert laut PLAN 14 nicht einem Ball zuzuordnen.
- **gluehwurm:**
  - Omega_Atem liegt auf dem ersten bzw. zweiten Frequenzschritt; die Atmung ist nicht aufgeloest.
  - r_Atem >= 0,95 nur in verschmolzenen Laeufen, auch ohne Atemanregung (nah_zufall 0,981).
  - Die weite Kontrolle hat am Start die Atem-Amplitude 2,93e-3, die nahen Laeufe mit Atmung 3,0e-2 bis 5,9e-2, bei
    gleicher Anregung laut PLAN.
- **osmose:** Die Baelle loesen sich fast auf (omega Ende bis 0,989, dQ bis -3,5 bei Start-Q 2,441). Die Raten gelten
  fuer stark veraenderte Baelle.
- **massenwirkung:** gleicher Ball im Vakuum -5,35e-4 (mit zwei Nachbarn) gegen -4,00e-4 (osmose, allein); dQ gesamt
  bei eps = 0 +3,35e-2 (grob) bzw. +1,67e-2 (fein), ein Messversatz, der sich mit dx halbiert.
- **nische lam = 0:** Der Umkehrpunkt-Detektor meldet auf einem Nullsignal Halbperiode 15 bzw. 19.
- **brechung:** Das Code-Urteil laesst abst50 aus (Code Z. 1355 bis 1362). anz20 verliert 21 % Ladung bei passendem
  Winkel.
- **isomere:** Das Umwandlungs-Flag steht in einem auseinanderlaufenden Lauf.
- **wirbel:** Auftriebsperioden 127,7 bis 204,6; der PLAN nennt die Halter-Eigenperiode etwa 214 als moegliche
  Stoerquelle. Der Bericht trennt das nicht.

## 4. Abgleich

### 4.1 RUNDE-06.md, Abschnitt "M1 Medium-Karten 1D" (Z. 337 bis 350)

| Fundstelle | Aussage der Leitung | Bericht | Befund |
|---|---|---|---|
| Z. 337 | ".69, p4000a" | LAUF1.log spur=p4000a, alle rc=0 | stimmt |
| Z. 339 | "Landau-Schwelle (L3 22/22)" | "22 von 22 Kenngroessen bestanden" | stimmt |
| Z. 340 | "Unter einer Grenzgeschwindigkeit bremst das stabile chi-Medium den Ball nicht." | 1,62e-7 (0,24 c_s), 1,41e-6 (0,38 c_s); stetiger Anstieg | zu stark. Belegt ist: Die Kraft liegt dort unter der Messschwelle F_MIN = 2e-6 (Minimum, nicht null); an 0,38 c_s ist E1 nicht erfuellt. |
| Z. 341 | "u_c/c_s = 0,43 bei C0 = 0,1 und 0,65 bei C0 = 0,3" | 0,43 und 0,65 | Zahlen stimmen. Es fehlen: Klammer 0,38 bis 0,48 bzw. 0,59 bis 0,72; Definition "Uebergang ueber F_MIN"; E1 an den Klammerpunkten nicht erfuellt. |
| Z. 341-342 | "Sie waechst also mit der Dichte staerker als c_s." | 0,090 -> 0,210 gegen c_s 0,2085 -> 0,3216 | stimmt (2,33, ueber die Klammer mindestens 1,9, gegen 1,54) |
| Z. 343 | "Vorhersage war 0,55 bzw. 0,75: Richtung getroffen, Werte niedriger." | PLAN V5b: 0,55 +- 0,2 und 0,75 +- 0,15 | untertreibt: Beide Werte liegen im Band, V5b ist getroffen. Nicht genannt: V5d (keine Kraft bei 0,48 c_s) ist verfehlt. |
| Z. 344 | "Damit war das Rutschen bei 0,48 c_s ('kreuzen', Runde 5) zum Teil eine echte Kraft." | einschwingen: Nachbau spaet a = 2,51e-8, F_med 5,81e-8; gehalten 5,35e-7; nur adiabatisch 3,82e-6 bzw. 5,77e-6, abfallend | nicht gedeckt. Die Aussage folgt der PLAN-Regel V5d, nicht dem einschwingen-Bericht. Belegt ist: Die kreuzen-Verschiebung war ein Anfangsstoss; nach adiabatischem Aufbau bleibt im Fenster eine kleine, abfallende Kraft ueber F_MIN, deren Stationaritaet offen ist. |
| Z. 345 | "Stokes-Drift im Medium (L3 10/10)" | "10 von 10" | stimmt |
| Z. 346 | "Start 130 vom Ball entfernt" | "x = -130 (130 vom Ball)" | stimmt |
| Z. 346-347 | "Exponent 1,99 fuer x, 2,03 fuer v (Vorhersage 2 +- 0,3; getroffen)" | "2.03, 1.99" | Zahlen stimmen. V3a verlangte auch "Richtung +x": v Ende ist negativ (-1,39e-5 bis -2,31e-4), x Ende etwa ein Zehntel von x nach Durchgang. "getroffen" gilt nur fuer den Exponenten. |
| Z. 348-349 | "(-0,83 bei a = 0,1, -1,62 bei a = 0,2)", "etwa linear" | -0,8321 / -1,624, Verhaeltnis 1,95 (HR) | stimmt |
| Z. 349 | "Das erklaert den verfehlten Runde-4-Test als Starteffekt." | nur Zwei-Feld-Medium gerechnet; Runde 4 war Ein-Feld (AUFTRAG Z. 66) | Deutung ueber das Gerechnete hinaus. Belegt ist: Im Zwei-Feld-Modell skaliert ein Start auf dem Ball linear mit a; das passt zur Vermutung aus dem Auftrag, der Runde-4-Lauf selbst ist nicht nachgerechnet. |
| Z. 350 | "Gegenproben (ohne Welle, lam = 0, Spiegel, Medium allein) bestanden." | lam = 0: -3,06e-6 (grob), -1,53e-6 (fein) | im Kern stimmt es; V3c verlangte "0 exakt", erreicht ist das Niveau des Laufs ohne Welle. |

### 4.2 RUNDE-06.md, Kartentabelle

- Z. 33 (M1 "alle 9 Aufrufe rc 0"): stimmt (LAUF1.log).
- Z. 34 (M2 "Wellen 4, 8/9, 14, 15, 17, 18 ... gerechnet ..., alle 8 Aufrufe rc 0"): rc stimmt. Wellen 15 (Linse) und
  17 (Kelvin-Helmholtz) sind aber nur Papier (M2-PLAN 3.5 und 3.6), nicht gerechnet.

### 4.3 Chat-Aussage der Leitung zu "ringe"

Wortlaut: "ein mitdrehender Ring aus 6 oder 8 Q-Baellen mit einer Phasenwindung verschmilzt ganz zu einem einzigen Ball,
behaelt fast seinen ganzen Drehimpuls (J/Q ~ 1,03 bis 1,04), das sieht nach einem drehenden Wirbelball aus; der
gegenlaeufig drehende fliegt auseinander".

| Teil | ringe_bericht.txt | Befund |
|---|---|---|
| "verschmilzt ganz zu einem einzigen Ball" | N6_k1_dreh+ und N8_k1_dreh+: "verschmolzen (ganz)", n 6 -> 1 bzw. 8 -> 1, t = 5 | stimmt |
| "behaelt fast seinen ganzen Drehimpuls (J/Q ~ 1,03 bis 1,04)" | Spaltenkopf "J/Q Start": +1,042 bzw. +1,029. J 181,6 -> 159,1 und 242,1 -> 214,4 | Abweichung: 1,03 bis 1,04 sind Startwerte, per Aufbau gesetzt (PLAN 4.1 "J_Bahn = Q"). J faellt um 12 % bzw. 11 % (HR). J/Q am Ende steht nicht im Bericht; HR aus J-Endwert, J/Q Start und Q-Verlust ergibt fuer die Box etwa 0,96 (N6) und 1,00 (N8). J_Box ist in diesen Boxen keine geschlossene Bilanz (Abschnitt 3.4). |
| "sieht nach einem drehenden Wirbelball aus" | "Windungen Ende" W [1] (N6 grob und fein, N8 grob); "windung_1_am_ende" nennt beide | Windungszahl stimmt: ein Klumpen mit sicherer Windung 1. Belegebene: "ein Klumpen mit Windung 1". Stationaer oder m = 1-Profil nicht im Bericht; die Klumpenladung schwankt bis zum Ende 121,8 bis 157,6 (JSON). |
| "aus 6 oder 8" | N8_k1_dreh+ nur grob | fuer N = 8 ohne L3 |
| "der gegenlaeufig drehende fliegt auseinander" | N6_k1_dreh-: "auseinander", 6 -> 6, W alle 0 | stimmt |
| nicht erwaehnt | N8_k1 ruhend: ganz, W [1]; N6_k0_dreh+: J 78,6 -> 0,015, W [0] | Bei N = 8 entsteht Windung 1 auch ohne Drehung. Ohne Windung verliert der drehende Ring seinen Drehimpuls fast ganz. |

- Dieselbe Angabe "J/Q ~ 1,03" steht auch in RUNDE-07.md Z. 23 (Karte RING) und ist dort ebenso ein Startwert.

## 5. Zusammenfassungstabelle

| Karte | Ergebnis kurz | Urteil | L3 | L1 / L2 / L3 / L4 / L5 | Vorschlag |
|---|---|---|---|---|---|
| M1-W5 landau | u_c/c_s 0,43 und 0,65 (F_MIN-Regel); bei 0,48 c_s F = 5,77e-6, abfallend | teilweise | 22/22, E1 nein | ja / bestanden / teilweise / ja / nein | weiter |
| M1-EIN einschwingen | Nachbau exakt, spaet unter F_MIN; adiabatisch a = 1,69e-6 | teilweise | 14/14 | ja / bestanden / ja / teilweise / nein | weiter |
| M1-W6 gleiten | Maximum 1,33e-3 bei 0,30; F(0,9) unter F_MIN | getroffen (V6c offen) | 13/13 | ja / bestanden / teilweise / ja / nein | parken |
| M1-W7 windschatten | hinten 1,3- bis 5,6-fach, vorn 0,1 bis 0,2 | verfehlt | 7/8 | ja / teilweise / teilweise / teilweise / nein | weiter |
| M1-W11 fahrtwind | F_B - F_A 7,5 % bei 0,35; sonst unter 5 % | teilweise | 3/3 | ja / bestanden / ja / ja / nein | weiter (Codeprobe) |
| M1-W3 stokes | Exponent 1,99 / 2,03; v Ende negativ; Start auf Ball linear (1,95) | teilweise | 10/10 | ja / bestanden / ja / teilweise / nein | weiter (klein) |
| M1-B2 osmose | erster Wechsel 0,184, dann nicht monoton; Vakuum 0,54 | teilweise | 9/9 | ja / teilweise / ja / teilweise / nein | weiter |
| M1-C9 massenwirkung | Vorzeichen 6 von 6, Reifung bei C = 0,2 | getroffen | 8/9 | ja / bestanden / teilweise / ja / nein | parken |
| M1-B21 nische | Pendel sanft wie vorhergesagt; steil ungedaempft (1,044) | teilweise | 6/6 | ja / bestanden / ja / teilweise / nein | parken |
| M2-W8/9 magnus | keine Querdrift; v_y 9,87e-5 knapp unter 1e-4; a_x 1,0e-4 bei 0,8 c_s | teilweise | 9/9 | ja / teilweise / ja / ja / nein | Magnus parken, Laengskraft weiter |
| M2-W4 kielwasser | Winkel 33 / 73 / 50 statt 49 / 32 / 21; unter c_s kaum Welle | teilweise | 9/9 | ja / bestanden / ja / ja / nein | weiter (Methode) |
| M2-W18 wirbel | Schwelle 0,55 bis 0,7 c_s; Paare oben minus, unten plus | teilweise | 6/6 | ja / bestanden / ja / ja / nein | parken |
| M2-W14 brechung | P1 in 5 von 6 auf hoechstens 0,34 Grad; abst50 unklar; anz20 21 % Verlust | teilweise | 6/6 | ja / bestanden / ja / teilweise / nein | weiter |
| M2-W15, W17 | nur Papier | - | - | - | Linse nach brechung; KH parken |
| 2DB-P paare | Statik und Klassen wie vorhergesagt; Abstandsgesetz 6,3 statt 1,7 / 3,0 | teilweise | nein | ja / bestanden / nein / ja / nein | weiter (Grundlage) |
| 2DB gitter | kein Gitter haelt; Schachbrett verschmilzt teilweise | teilweise | 5/5 | ja / bestanden / ja / teilweise / nein | verwerfen |
| 2DB ringe | mitdrehend: ein Klumpen mit Windung 1; gegendrehend auseinander | getroffen | 5/5 | ja / bestanden / ja / teilweise / mittelbar | weiter (RING) |
| 2DB gluehwurm | keine Synchronisation; Atem-Kennzahlen auf erstem Frequenzschritt | teilweise | 1/1 | ja / bestanden / ja / ja / nein | verwerfen |
| 2DB haendigkeit | keine Haendigkeit; Spiegel misch_a 1,1e-4 | teilweise | 2/2 | schwach / teilweise / ja / ja / nein | parken |
| 2DB isomere | Dreieck 1,03 tiefer; keine Isomere; Umwandlungs-Flag in auseinanderlaufendem Lauf | teilweise | 6/6 | ja / bestanden / ja / teilweise / nein | parken |
| 2DB kollektiv | nur Vergroebern, kein Schwarm; schwarm_gleich aggregiert | teilweise | 2/2 | ja / bestanden / ja / teilweise / nein | parken |
| 2DB profile | s = 0,131 (schwach), Minimum bei 0,65 | teilweise | Klammer ok | ja / bestanden / ja / teilweise / nein | parken |

## 6. Einfach gesagt

Wir haben nachgesehen, was die Rechnungen der Nacht wirklich zeigen. Ein Q-Ball in der ruhigen "Suppe" wird schon
unterhalb der Schallgeschwindigkeit ein wenig gebremst, aber die Bremskraft waechst langsam und stetig; eine harte Grenze
sieht man nicht, und die Kraft hatte sich beim Messen noch nicht beruhigt. Das Rutschen aus Runde 5 war ein Schubs beim
ploetzlichen Start, keine gemessene Dauerkraft. Ein Ring aus sechs oder acht Baellen, der sich mitdreht, wird zu einem
einzigen Ball mit einem Wirbel in der Mitte; die Zahl 1,04 fuer den Drehimpuls gilt aber fuer den Start, nicht fuer das
Ende. Viele Kontrollen haben gehalten, einige Messwerkzeuge (Winkel, Atmung, Drehimpuls in der Box) muessen vor der
naechsten Runde repariert werden.
