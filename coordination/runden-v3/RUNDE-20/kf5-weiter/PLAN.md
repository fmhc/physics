# KF-5 weiter (Runde 20, Zufallskarte): Plan

Bearbeiter: Code-Agent (Claude, Anthropic), Auftrag der Leitung claude-primary. Beginn 2026-10-02 17:47:58 CEST (date).
Plan geschrieben ab 18:01:20 CEST (date), nach dem Rauchlauf (Abschnitt 8) und vor jedem echten Lauf. Explorativ (v3),
Hypothesen [H]. Karte: KARTE.md daneben (Vorhersagen Z0 bis Z4 und Bedeutung dort, hier nur umgesetzt).

## 1. Frage

Landen die Tropfen aus der 2D-Geburt (KF-5, Runde 6) bei laengerer Laufzeit auf der Q(omega)-Familie? Arm s03 (S0 = 0,3)
auf beiden Gittern von T = 800 bis T = 2000, Auswertung bei 1200, 1600, 2000; Klassifikator aus Runde 6 unveraendert.
Zusatz, falls Zeit: s01 fein, nur beschreibend (geht nicht in Z0 bis Z4 ein).

## 2. Original geprueft (kf5_geburt.py, sha256 9b895c9f...6bc0, auf der .69 identisch; familie_2d_m0.json f3446207...f806)

- Gleichung psi_tt = Lap psi - U'(S) psi, U = S - S^2 + S^3/2; Laplace spektral (FFT), Velocity-Verlet, complex128.
- Periodische Box 96 x 96 **ohne Randschicht oder Daempfung** (es gibt keinen Daempfungsrand, der fortzusetzen waere).
- grob dx 0,25 / dt 0,04 (n 384), fein dx 0,125 / dt 0,02 (n 768). Zeit t = Schritt * dt ab t = 0.
- Auswertung alle T_AUS = 10 (analyse_arm: Schwellen 2 S0 und 3 S0, A_MIN 2, KOMPAKT 2), Messfenster 40 am Ende,
  Abtastung 1 (fenster_start / fenster_probe / fenster_auswerten), rund = rmax/R_A <= 1,3 am Fensterbeginn, Familientest
  FAM_TOL 0,10, Q_SCHWANK 0,20, MIN_ENTSCHEIDBAR 5, Familie aus familie_2d_m0.json (quadratische Interpolation).
- Gespeicherte Zustaende bei T = 800 (lauf-69/ausgabe/*_felder.pt): psi, vel als (B, n, n) complex128, t 800, box, dx,
  stufe, Armliste. grob: Stapel s03, s01, s08, frei, s03b, s01b (s03 = Index 0); fein: je Arm eine Datei.

## 3. Umsetzung (kf5_weiter.py) und Abweichungen, die die Fortsetzung erzwingt

kf5_weiter.py importiert kf5_geburt.py unveraendert aus /home/fmh/fmhc-physics-remote/runde6-kf5 (nur gelesen, ohne
Bytecode) und ruft dessen Funktionen und Konstanten auf. Die Verlet-Schleife steckt in lauf() und ist nicht einzeln
aufrufbar; sie ist Zeile fuer Zeile nachgebaut (gleiche Operationen, gleiche Reihenfolge, gleiche Schrittzaehlung).

Abweichungen, alle vor dem Lauf festgelegt:
1. **Neustart:** F = kraft(psi) wird beim Laden neu berechnet (im Original aus dem letzten Schritt uebernommen). Gleiche
   Funktion, gleiche Eingabe.
2. **grob, Stapelgroesse:** Runde 6 rechnete s03 im Stapel mit sechs Armen (B = 6), die Fortsetzung nur s03 (B = 1).
   Die FFT-Rundung kann von der Stapelgroesse abhaengen (Groessenordnung 1e-16). Nach der Saettigung ist die Dynamik
   chaotisch: Die Fortsetzung ist dann eine gleichwertige Realisierung, aber nicht bitgleich zu einem gedachten
   durchgehenden Sechs-Arm-Lauf. fein s03: auch Runde 6 hatte B = 1.
3. **Abschnitte** 800 -> 1200 -> 1600 -> 2000 mit Zwischenspeicher (complex128, verlustfrei) in
   runde20-kf5-weiter/lauf-69/zwischen/. Jeder Abschnitt endet an einer Auswertezeit; das Messfenster [T_e - 40, T_e]
   liegt am Abschnittsende wie in Runde 6 am Laufende (fenster_auswerten mit t0 = T_e - 40).
4. **Auswertung bei t = von:** in jedem Abschnitt neu berechnet (gleicher Zustand, gleiche Zeile). Bei 800 gibt es kein
   Etikettenbild von 790 (Runde 6 hat es nicht gespeichert), also verknuepfung(None, .) = (0, 0); die Zaehlung 790 -> 800
   steht in Runde 6. Ab 1200 wird das gespeicherte Etikettenbild uebergeben.
5. **Ausgaben:** Bilder alle 50 entfallen (reine Ausgabe); je Abschnittsende ein S-Bild (dx 0,5) im Zwischenspeicher.
   Kontrastreihe alle T_KON wie im Original.
6. **Zeitgrenze:** eigene Prognose nach vier Auswertungen, sauberer Abbruch ueber 540 s (Original: 560 s, Prognose bei
   t = 40). Jeder Aufruf ist systemd-begrenzt auf 600 s.

**Zusatz, nicht Teil des Klassifikators (nur fuer Z3 und den Bericht):**
- **Abstammung:** Komponenten der unteren Schwelle (die Etiketten aus analyse_arm, Flaeche >= A_MIN) werden zwischen zwei
  Auswertungen ueber Maskenueberlapp verknuepft, dieselbe Regel wie verknuepfung(). Jede Komponente traegt die Menge ihrer
  Wurzeln. Wurzeln sind die Komponenten bei t = 760 (Beginn des Runde-6-Fensters); spaeter entstandene Komponenten
  bekommen eine neue Wurzel. Akte je Wurzel: erste Verschmelzung mit einer fremden Wurzel (auch einer neu entstandenen
  Komponente), erste Teilung, Erloeschen.
- **Fenstertropfen -> Wurzel:** am Fensterbeginn werden die Tropfenetiketten mit denselben Funktionen (komponenten,
  eigenschaften, gleiche Auswahl) bestimmt; die Positionen muessen die aus analyse_arm treffen (Pruefung im Code).
- **Abstaende je Fenstertropfen** (alle Tropfen, auch "nicht rund" und "gestoert"):
  - dQ* = Q_net / Q_fam(omega_ruhe) - 1. Das ist dieselbe Groesse wie delta im Familientest; dort wird sie nur fuer runde,
    ungestoerte Tropfen ausgegeben.
  - E/Q-Abstand = (E/Q) / (E/Q)_fam(Q) - 1.
  - omega-Abstand = omega_ruhe - omega_fam(Q).

## 4. K0 (vor jeder Fortsetzung, je Gitter)

- **K0a, Schnappschuss:** analyse_arm auf den gespeicherten T = 800-Zustand gegen die Runde-6-Zeile t = 800.
  - Gleich sein muessen: N_komp, N_klein, N_tropfen, N_netz, umspannt (beide Schwellen).
  - Bis auf die Rundung der Ausgabe (relativ 2e-6 plus absolut 1e-6) gleich sein muessen: Maskenanteile und je Tropfen
    x, y, A, S_max, Q_maske, Q_roh, Q_net, E_net, omega, dQ_familie, rmax/R_A.
- **K0b, Fensterurteile:** Die Runde-6-Urteile ("rund", "auf / neben / unentschieden", E/Q) stammen aus dem Messfenster
  [760, 800] mit Tropfen vom Fensterbeginn 760. Der Zustand bei 800 allein reicht dafuer nicht.
  - Deshalb rechnet derselbe Verlet mit -dt von 800 nach 760 zurueck (Velocity-Verlet ist zeitumkehrbar) und dann
    vorwaerts 760 -> 800 mit Auswertung alle 10 und Fenster wie Runde 6.
  - Pruefung: Zeilen 760 bis 800 wie bei K0a; Fenster: Tropfenzahl, rund, klasse, klasse_roh, verloren, stoss, Zaehlung
    und Urteil gleich; Zahlen (Q, E, E/Q, omega_rot, omega_ruhe, u, v, ...) relativ 1e-4.
  - Dazu der Rueckkehrfehler max|psi(800, zurueck und vor) - psi(800)| / max|psi(800)|.
- **Gate:** Fortsetzung nur, wenn K0a auf dem Gitter besteht; sonst Fehlersuche, keine Fortsetzung.
  - Scheitert K0b bei kleinem Rueckkehrfehler (<= 1e-8), ist der Fensterpfad verdaechtig: Stopp.
  - Scheitert K0b bei grossem Rueckkehrfehler, ist es eine Grenze der Rekonstruktion: Fortsetzung mit Vermerk.
- Z0 ist eingetroffen, wenn K0a und K0b auf beiden Gittern (s03) bestehen.

## 5. Vorhersagen der Karte, umgesetzt (Regeln fest vor dem Lauf, im Unterbefehl zusammen kodiert)

| Nr | Karte | Wahrsch. | Regel |
|---|---|---|---|
| Z0 | K0 reproduziert die T = 800-Urteile | 85 % | K0a und K0b bestanden, grob und fein |
| Z1 | T = 2000: mindestens 2 Tropfen "rund", beide Gitter | 55 % | Fenstertropfen bei 2000 (Tropfen am Fensterbeginn 1960) mit rund = wahr (rmax/R_A <= 1,3 bei 1960, Runde-6-Definition); Anzahl >= 2 auf grob und auf fein |
| Z2 | T = 2000: mindestens ein Tropfen "auf", beide Gitter | 35 % | klasse "auf" aus fenster_auswerten bei 2000; >= 1 auf grob und auf fein |
| Z3 | Abstand zur Familie bei 2000 kleiner als bei 800, jeder Tropfen ohne Verschmelzung | 65 % | siehe unten |
| Z4 | L3: grob und fein gleich in Tropfenzahl und Urteil je Tropfen | 60 % | bei T = 2000: Zahl der Fenstertropfen gleich und Liste der Klassen (Tropfen nach Q_net absteigend) gleich |

**Z3 im Einzelnen:**
- **Grundmenge:** die Runde-6-Fenstertropfen bei T = 800 (Tropfen bei 760), beide Gitter.
- **Abstand zur Familie, Hauptmass:** |dQ*|.
  - Werte bei 800: dQ* aus den Runde-6-Fensterwerten (Q_net, omega_ruhe aus der Runde-6-JSON).
  - Werte bei 2000: dQ* des Fenstertropfens, dessen Wurzelmenge genau die Wurzel des Tropfens ist ("rein"). Bei Teilung
    gilt der Teil mit dem groessten Q_net (vermerkt).
- **Ausgeschlossen:** Tropfen mit Verschmelzung (Akte: fremde Wurzel irgendwann in (760, 2000]) und erloschene Tropfen.
- **Einzelfall:** "kleiner", wenn |dQ*(2000)| < |dQ*(800)|, sonst "nicht kleiner".
  - "Offen" ist der Einzelfall, wenn bei 2000 kein reiner Fenstertropfen existiert, die Wurzel nicht eindeutig ist oder
    dQ* nicht definiert ist (omega ausserhalb der Tabelle).
- **Gesamturteil:**
  - eingetroffen: Die Restmenge ist nicht leer, und jeder Einzelfall ist "kleiner".
  - nicht eingetroffen: mindestens ein Einzelfall ist "nicht kleiner".
  - offen: sonst.
- **Nebenmasse** |E/Q-Abstand| und |omega-Abstand|: werden je Tropfen berichtet, entscheiden Z3 aber nicht.

**Bedeutung (Karte, mechanisch):**
- Z2 und Z3 eingetroffen: Tropfen laufen auf die Familie zu, M1 in 2D bildungsfaehig (Stufe 5) [H, im Modell].
- Z3 nicht eingetroffen: keine Annaeherung auf dieser Zeitskala, KF-5 verwerfen.
- Sonst parken mit Grund.

Bei T = 1200 und 1600 wird dasselbe berichtet (beschreibend). Die Urteile fallen nur bei 2000.

## 6. Aufrufe (alle ueber kleintest.sh, Spur p4000a; Ordner /home/fmh/fmhc-physics-remote/runde20-kf5-weiter)

```
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5w-k0-grob   kf5_weiter.py k0 --stufe grob --arm s03
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5w-k0-fein   kf5_weiter.py k0 --stufe fein --arm s03
bash ... p4000a kf5w-grob-1 kf5_weiter.py weiter --stufe grob --arm s03 --von 800 --bis 1200   (dann 1200-1600, 1600-2000)
bash ... p4000a kf5w-fein-1 kf5_weiter.py weiter --stufe fein --arm s03 --von 800 --bis 1200   (dann 1200-1600, 1600-2000)
bash ... cpu    kf5w-zus    kf5_weiter.py zusammen --arm s03 --stufen grob,fein --geraet cpu
Zusatz s01 fein: k0 --stufe fein --arm s01, drei Abschnitte, zusammen --arm s01 --stufen fein --geraet cpu
```

**Laufzeit aus dem Rauchlauf (Abschnitt 8), Hochrechnung je Abschnitt (400 Zeiteinheiten):**
- fein: 20 000 Schritte x 3,5 bis 5,9 ms = 70 bis 120 s; 41 Auswertungen x 0,4 bis 1,8 s = 16 bis 72 s; Fenster etwa
  5 s. Zusammen 90 bis 200 s.
- grob: 10 000 x 0,8 bis 1,3 ms = 8 bis 13 s plus 41 x 0,4 s, also etwa 30 s.
- K0 fein etwa 25 s, grob etwa 5 s. Alles weit unter 600 s je Aufruf. Ein einziger Aufruf 800 -> 2000 fein laege bei
  270 bis 590 s, daher die Abschnitte.

## 7. Latten (v3)

- **L1 kann scheitern:** ja. Z1 bis Z4 haben Ausgaenge in beide Richtungen; Z3 kann die Karte verwerfen.
- **L2 Gegenprobe:** K0a/K0b (Klassifikator und Fensterpfad gegen Runde 6), Rueckkehrfehler, Erhaltung von Q und E in der
  Box je Abschnitt.
- **L3 Numerik:** grob gegen fein (Z4). Nach der Saettigung chaotisch, also nur Statistik vergleichbar (wie Runde 6).
- **L4 schon bekannt:** Q-Ball-Bildung und Vergroeberung aus modulationsinstabilen Kondensaten ist Literatur (Runde-6-Plan,
  L4). Neu ist nur der Familientest mit diesem Klassifikator in diesem Modell.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter).

## 8. Rauchlauf (vor dem Einfrieren, Zahlen ungueltig, nur Durchlauf und Zeit)

- 2026-10-02 17:59:46 bis 18:00:42 CEST (Uhr der .69 in UTC, 15:59:46 bis 16:00:42), Spur p4000a, Quadro P4000.
- Gelaufen: k0 --rauch (10 zurueck, 10 vor, Fenster 10) und weiter --rauch (800 -> 820, Fenster 10), je grob und fein.
- Die Rauchausgabe enthaelt keine Tropfenzahlen oder -werte, nur Dauern (lauf-69/rauch/*.json, RAUCH.log).
- Gemessen:
  - k0 fein: 3,49 ms/Schritt vorwaerts, 3,51 rueckwaerts, gesamt 11,2 s.
  - weiter fein: 5,93 ms/Schritt (mit Anlaufkosten), 1,75 s je Auswertung, gesamt 12,6 s.
  - k0 grob: 0,82 / 0,77 ms, gesamt 2,0 s.
  - weiter grob: 1,32 ms/Schritt, 0,37 s je Auswertung, gesamt 2,2 s.
- Alle rc = 0.

## 9. Grenzen (vorab)

- **Hauptmass Z3:** Bei duennwandigen grossen Tropfen (omega^2 nahe 0,51) reagiert dQ* sehr stark auf omega. Dort aendert
  0,003 in omega Q_fam um Dutzende Prozent. Z3 kann also an Rauschen in omega haengen. Deshalb werden die Nebenmasse und
  u_omega mitberichtet, ohne die Regel zu aendern.
- **Klasse bei grossen Tropfen:** Liegt omega_ruhe - u unter sqrt(0,51) = 0,7141, gibt der Klassifikator dort immer
  "unentschieden" (Band ausserhalb der Tabelle). Fuer omega_ruhe nahe 0,72 braucht "auf" also u < etwa 0,005.
- **Periodische Box ohne Senke:** Das Wellenbad bleibt und stoesst die Tropfen weiter an.
- **Verschmelzung:** Sie ist eine Maskendiagnose im Takt 10. Kurze Beruehrungen zwischen zwei Auswertungen werden nicht
  gesehen.
- **Rekonstruktion K0b:** Der Rueckwaertslauf traegt Rundungsfehler, die das Chaos ueber 40 Zeiteinheiten verstaerkt; der
  Rueckkehrfehler wird berichtet.

## 10. Stand beim Einfrieren

- kf5_weiter.py sha256 9dce1fad28cfda51699f3fb3e103bf0fe50d9615e191ea7c72a6dbf473e47e11 (lokal und auf der .69 gleich, py_compile auf der .69 ok).
- Eingefroren 2026-10-02 18:02:35 CEST (date), vor K0 und vor jeder Fortsetzung.
