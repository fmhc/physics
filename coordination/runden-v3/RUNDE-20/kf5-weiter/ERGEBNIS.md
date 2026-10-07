# KF-5 weiter (Runde 20, Zufallskarte): Ergebnis

Code-Agent (Claude, Anthropic), Auftrag der Leitung claude-primary. Beginn 2026-10-02 17:47:58 CEST (date).
Rauchlauf 17:59:46 bis 18:00:42 CEST. Plan eingefroren 18:02:35 CEST (PLAN.md.eingefroren-20261002-180235), vor K0 und
vor jeder Fortsetzung. Laeufe 18:02:39 bis 18:10:31 CEST auf der .69 (Uhr dort UTC), Ende der Bearbeitung in der
letzten Zeile.
Explorativ (v3), alle Deutungen [H, im Modell].

## 1. Ergebnis zuerst

1. **K0 bestanden, Z0 eingetroffen.**
   - Der unveraenderte Runde-6-Klassifikator gibt die T = 800-Urteile auf beiden Gittern exakt wieder: Tropfenzahl,
     rund / nicht rund, Klasse und E/Q gleich auf alle sieben ausgegebenen Stellen.
   - Das gilt auch fuer die Fensterurteile. Sie wurden ueber Rueckwaertsrechnung 800 -> 760 und Neulauf rekonstruiert;
     der Rueckkehrfehler betraegt im Feld hoechstens 1e-14, in der Zeitableitung hoechstens 1,6e-13.
2. **Kein Tropfen landet bis T = 2000 auf der Familie; die Tropfen verschmelzen (der kleinste auf fein erlischt).**
   - Auf beiden Gittern laufen die Tropfen von s03 zu einer einzigen Komponente der unteren Schwelle zusammen: grob bei
     t = 1550 (1650 bis 1740 noch einmal getrennt, ab 1750 wieder eine), fein bei t = 1520.
   - Diese Komponente traegt 84 bis 85 % der Ladung, ist nicht rund (rmax/R_A 1,49 fein, 1,79 grob am Fensterbeginn)
     und schwingt stark.
   - Bei 2000 gibt es auf jedem Gitter genau einen Fenstertropfen, Klasse "nicht rund". Kein "auf", kein "neben".
3. **Vorhersagen:** Z1 (>= 2 runde Tropfen) und Z2 (>= 1 "auf") nicht eingetroffen. Z4 (grob = fein) eingetroffen,
   aber nur im schwachen Sinn: je ein nicht runder Klumpen.
   - Z3 ist **offen**: Von den sechs T = 800-Tropfen bleibt keiner ohne Verschmelzung (fuenf verschmolzen, einer
     erloschen). Die Grundmenge der Regel ist leer.
4. **Bedeutung nach Karte: parken mit Grund.** Z3 ist weder eingetroffen noch nicht eingetroffen. Grund:
   - In der Box 96 mit S0 = 0,3 ist die Vergroeberung (Verschmelzen) schneller als das Abrunden.
   - Die Frage "laufen einzelne Tropfen auf die Familie zu?" laesst sich mit dieser Anordnung nicht stellen: Es bleibt
     kein einzelner Tropfen lange genug uebrig.
   - Stufe 5 ist damit weder gezeigt noch widerlegt.
5. **Zusatz s01 fein (beschreibend, nicht in Z0 bis Z4):** 13 Fenstertropfen bei 800, 3 bei 2000.
   - Die entscheidbaren Tropfen (runde, ungestoerte mit Q etwa 70 bis 420) kommen als **"neben"** heraus (je einer bei
     1200 und 2000, zwei bei 1600), nie als "auf".
   - Ihr omega liegt 0,006 bis 0,010 unter dem Familienwert fuer ihr Q, ihr E/Q 0,8 bis 2,2 % ueber der Familie.
   - Ein Tropfen ohne Verschmelzung bis 1600 (w0) zeigt die beiden Masse gegenlaeufig:
     - E/Q-Abstand faellt von +2,0 auf +1,0 %.
     - |dQ*| steigt von 0,09 auf 0,53.
   - Das ist nachtraeglich bemerkt und nicht vorregistriert.

## 2. K0 im Detail

| Gitter | K0a (Schnappschuss t = 800) | K0b (Fenster 760 -> 800, rekonstruiert) | Rueckkehrfehler psi / vel |
|---|---|---|---|
| grob s03 | N_tropfen 3 / N_komp 3 (2 S0), N_tropfen 6 (3 S0); alle Zahlen je Tropfen gleich, max. rel. Abweichung 0,0 (bei 7 Stellen) | Zeilen 760 bis 800 gleich; 3 Fenstertropfen, rund F / W / W, Klasse nicht rund / unentschieden / unentschieden, E/Q 0,7273494 / 0,8551535 / 0,7291311 (= Runde 6), Urteil "nicht entscheidbar"; max. rel. Abweichung 0,0 | 5,5e-15 / 5,5e-14 |
| fein s03 | N_tropfen 3 / N_komp 3, N_tropfen 2 (3 S0); max. rel. Abweichung 0,0 | Zeilen gleich; rund F / F / W, nicht rund / nicht rund / unentschieden, E/Q 0,7292778 / 0,9393655 / 0,7287145 (= Runde 6); max. rel. Abweichung 0,0 | 9,5e-15 / 1,6e-13 |
| fein s01 (Zusatz) | gleich (12 Tropfen bei 800) | 13 Fenstertropfen, alle Klassen, rund und E/Q gleich | 5,6e-15 / 1,3e-13 |

- **Weg:** derselbe Velocity-Verlet mit -dt von 800 nach 760, dann vorwaerts 760 -> 800 mit analyse_arm alle 10 und
  Messfenster wie Runde 6 (PLAN.md, Abschnitt 4).
- Verglichen wurden die Fensterzahlen Q, E, E/Q, omega_rot, omega_ruhe, u, v, Q-Schwankung und dQ. Toleranz relativ
  1e-4; gemessen 0,0 bei sieben Stellen.
- Das Gate (K0a) war vor jeder Fortsetzung erfuellt.

## 3. Tabelle je Tropfen und Gitter (s03)

Spalten:
- Werte aus dem Messfenster [T - 40, T] des Runde-6-Klassifikators. Bei T = 800 sind es die Runde-6-Werte, von K0b
  reproduziert.
- E ist E_ruhe_net. "fam" ist der Familienwert bei gleichem Q.
- rmax/R_A gilt am Fensterbeginn; danach richtet sich "rund".
- dQ* = Q_net / Q_fam(omega_ruhe) - 1 ist das Hauptmass "Abstand zur Familie" fuer Z3.
- Status: "rein" heisst, der Fenstertropfen traegt nur die Wurzel dieses Tropfens; "verschmolzen" heisst, er traegt
  dazu fremde Wurzeln.

| Gitter | Tropfen (Wurzel) | T | Q | E | E/Q (fam) | omega_ruhe +- u (fam(Q)) | rmax/R_A | Urteil | dQ* | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| grob | R6-k0 (w0) | 800 | 2128,9 | 1548,5 | 0,7273 (0,7309) | 0,7205 +- 0,0037 (0,7187) | 1,389 | nicht rund | +0,35 | Runde 6 |
| grob | R6-k0 (w0) | 1200 | 2198,3 | 1586,0 | 0,7215 (0,7305) | 0,7239 +- 0,0177 (0,7186) | 1,276 | unentschieden | +1,299 | rein |
| grob | R6-k0 (w0) | 1600 | - | - | - | - | - | kein Tropfen im Fenster | - | Komponente umspannend (s. u.) |
| grob | R6-k0 (w0) | 2000 | 3433,7 | 2452,7 | 0,7143 (0,7259) | 0,7251 +- 0,0160 (0,7163) | 1,787 | nicht rund | +2,929 | verschmolzen mit w1, w2 |
| grob | R6-k1 (w1) | 800 | 60,8 | 52,0 | 0,8552 (0,8554) | 0,7724 +- 0,0102 (0,7781) | 1,192 | unentschieden | -0,141 | Runde 6 |
| grob | R6-k1 (w1) | 1200 | 1499,7 | 1110,4 | 0,7404 (0,7351) | 0,7194 +- 0,0195 (0,7208) | 1,169 | unentschieden | -0,205 | verschmolzen mit w2 |
| grob | R6-k1 (w1) | 1600 | - | - | - | - | - | kein Tropfen im Fenster | - | |
| grob | R6-k1 (w1) | 2000 | wie w0 | | | | | nicht rund | +2,929 | verschmolzen mit w0, w2 |
| grob | R6-k2 (w2) | 800 | 1347,3 | 982,4 | 0,7291 (0,7366) | 0,7142 +- 0,0053 (0,7215) | 1,277 | unentschieden | -0,757 | Runde 6 |
| grob | R6-k2 (w2) | 1200 | wie w1 | | | | | unentschieden | -0,205 | verschmolzen mit w1 |
| grob | R6-k2 (w2) | 1600 | - | - | - | - | - | kein Tropfen im Fenster | - | |
| grob | R6-k2 (w2) | 2000 | wie w0 | | | | | nicht rund | +2,929 | verschmolzen mit w0, w1 |
| fein | R6-k0 (w0) | 800 | 2046,3 | 1492,3 | 0,7293 (0,7313) | 0,7262 +- 0,0111 (0,7190) | 1,350 | nicht rund | +1,662 | Runde 6 |
| fein | R6-k0 (w0) | 1200 | 2168,4 | 1546,0 | 0,7130 (0,7307) | 0,7258 +- 0,0163 (0,7186) | 1,415 | nicht rund | +1,677 | rein |
| fein | R6-k0 (w0) | 1600 | 2329,9 | 1683,6 | 0,7226 (0,7299) | 0,7130 +- 0,0121 (0,7183) | 1,886 | nicht rund | - (omega unter Tabelle) | verschmolzen mit w2 |
| fein | R6-k0 (w0) | 2000 | 3409,4 | 2255,1 | 0,6614 (0,7260) | 0,7773 +- 0,0353 (0,7164) | 1,487 | nicht rund | +53,9 | verschmolzen mit w2 |
| fein | R6-k1 (w1) | 800 | 26,5 | 24,9 | 0,9394 (0,9324) | 0,8218 +- 0,0165 (0,8270) | 1,472 | nicht rund | -0,059 | Runde 6 |
| fein | R6-k1 (w1) | 1200 bis 2000 | - | - | - | - | - | kein Tropfen im Fenster | - | erloschen bei 860 |
| fein | R6-k2 (w2) | 800 | 1324,9 | 965,5 | 0,7287 (0,7368) | 0,7186 +- 0,0153 (0,7216) | 1,281 | unentschieden | -0,398 | Runde 6 |
| fein | R6-k2 (w2) | 1200 | 1424,6 | 1043,2 | 0,7323 (0,7358) | 0,7202 +- 0,0184 (0,7211) | 1,336 | nicht rund | -0,137 | rein |
| fein | R6-k2 (w2) | 1600 | wie w0 | | | | | nicht rund | - | verschmolzen mit w0 |
| fein | R6-k2 (w2) | 2000 | wie w0 | | | | | nicht rund | +53,9 | verschmolzen mit w0 |

Neue Fenstertropfen ohne Runde-6-Wurzel: keine (s03, beide Gitter).

**Verschmelzungen und Verlauf (Abstammung ueber Maskenueberlapp alle 10, untere Schwelle):**
- **grob:**
  - w1 + w2 verschmelzen bei 960 (N_tropfen 3 -> 2).
  - w0 + (w1 w2) verschmelzen bei 1550. Von 1550 bis 1640 gibt es nur eine Komponente, und sie gilt meist als
    "umspannend": ihre Projektion deckt alle Zeilen oder Spalten, Maskenanteil 0,28.
  - Bei 1650 teilt sie sich wieder in zwei Tropfen, bei 1750 vereinigt sie sich erneut. Ab dann gibt es eine
    Komponente (bei 1770 kurz nicht kompakt).
  - Maskendiagnose je Abschnitt (Verschmelzungen / Teilungen): 1 / 0, 1 / 0, 2 / 2.
- **fein:**
  - w1 (Q 26,5) erlischt bei 860.
    - Bei 850 ist er noch ein Tropfen mit Flaeche 5,4, periodisch gerechnet etwa 4 Laengeneinheiten vom Maskenrand von
      w2 entfernt.
    - Bei 860 ueberlappt keine Komponente >= A_MIN seine Maske; es bleibt ein Kleinteil unter A_MIN. Nach der Regel heisst
      das "erloschen", nicht "verschmolzen".
    - Ob er abgestrahlt oder von w2 aufgenommen wurde, entscheidet die Maske nicht. Q_net von w2 springt 850 -> 860 von
      1270 auf 1411, zum Teil durch die Scheibenzuordnung.
  - w0 + w2 verschmelzen bei 1520, danach bleibt eine grosse Komponente. Zeitweise kommt ein zweiter kleiner Tropfen dazu
    (Q 17 bis 18, z. B. bei 1540, 1850, 1950).
  - Maskendiagnose: 0 / 0, 1 / 0, 0 / 0.
- **Endklumpen bei 2000:**
  - grob: Q_net 3434 bzw. 3409 fein, bei Q_box 4045. Das sind 85 bzw. 84 % der Ladung.
  - Er schwingt stark: rmax/R_A springt von Auswertung zu Auswertung zwischen etwa 1,35 und 1,9. Q in der Scheibe
    schwankt im Fenster um 39 % (grob) bzw. 14 % (fein). Der Schwerpunkt springt ("verloren").
  - fein bei 2000: An der oberen Schwelle (3 S0) liegen 11 Komponenten >= A_MIN, davon 10 Tropfen, alle in der einen
    Komponente der unteren Schwelle. Zu anderen Zeiten sind es 0 bis 2.
- **Erhaltung je Abschnitt:**
  - Q-Drift hoechstens 6,7e-16.
  - E-Drift grob 2,4e-5 bis 2,9e-5, fein 5,8e-6 bis 7,9e-6. Das ist dieselbe Groessenordnung wie in Runde 6 (0 bis
    800).

## 4. Z0 bis Z4

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| Z0 | K0 reproduziert die T = 800-Urteile | 85 % | **eingetroffen** | K0a und K0b auf grob und fein bestanden, Abweichung 0 bei 7 Stellen, Rueckkehrfehler <= 9,5e-15 |
| Z1 | T = 2000: >= 2 Tropfen "rund", beide Gitter | 55 % | **nicht eingetroffen** | je 1 Fenstertropfen; runde: grob 0 (rmax/R_A 1,787), fein 0 (1,487) |
| Z2 | T = 2000: >= 1 Tropfen "auf", beide Gitter | 35 % | **nicht eingetroffen** | "auf" grob 0, fein 0 (je 1 x "nicht rund") |
| Z3 | Abstand zur Familie bei 2000 kleiner als bei 800, jeder Tropfen ohne Verschmelzung | 65 % | **offen** | Grundmenge leer: grob k0 verschmolzen 1550, k1 und k2 960; fein k0 und k2 verschmolzen 1520, k1 erloschen 860 |
| Z4 | L3: grob und fein gleich in Tropfenzahl und Urteil je Tropfen | 60 % | **eingetroffen** (schwach) | 1 / 1 Fenstertropfen, Klassen ["nicht rund"] / ["nicht rund"]; N_tropfen(2000) untere Schwelle 1 / 1, obere 1 / 10 (nicht Teil der Regel) |

- **Zu Z3, nur berichtet:** Die ausgeschlossenen Tropfen bewegen sich vom Familienwert weg.
  - dQ*: grob von +0,35 / -0,14 / -0,76 auf +2,93; fein von +1,66 / -0,40 auf +53,9.
  - E/Q-Abstand: grob von -0,5 / -0,03 / -1,0 % auf -1,6 %; fein von -0,3 / -1,1 % auf -8,9 %.
  - Das betrifft verschmolzene Klumpen und entscheidet nach der Regel nichts.
- **Bei 1200 (beschreibend):** Die reinen Tropfen sind fein w2 (|dQ*| 0,40 -> 0,14) und fein w0 (1,66 -> 1,68)
  sowie grob w0 (0,35 -> 1,30).
- **Bedeutung (Karte, mechanisch):** Z3 nicht "nicht eingetroffen", Z2 nicht eingetroffen, also "sonst: parken mit
  Grund". Der Grund steht in Abschnitt 1, Punkt 4.

## 5. Latten (v3)

- **L1 kann scheitern:** ja.
  - Z1 und Z2 sind gescheitert.
  - Z3 haette die Karte verwerfen koennen. Das ist nicht geschehen, weil die Grundmenge leer blieb.
- **L2 Gegenprobe:** teilweise.
  - K0a und K0b exakt, Erhaltung von Q und E gut.
  - Es fehlt eine Eichprobe des Klassifikators an einem bekannten Familienmitglied (siehe Abschnitt 6).
- **L3 Numerik:** ja, qualitativ.
  - Beide Gitter vergroebern gleich: Verschmelzung zu einer Komponente bei 1550 bzw. 1520, Endurteil gleich.
  - Die Einzelwege unterscheiden sich, wie nach der Saettigung erwartet (grob: w1 + w2 bei 960; fein: w1 erlischt).
- **L4 schon bekannt:** Bildung und Verschmelzen von Q-Baellen in Gitterlaeufen ist Literatur (Runde-6-Plan: Kusenko und
  Shaposhnikov 1998, Kasuya und Kawasaki 2000 [L, hier nicht nachgeprueft]). Neu ist nur der Familientest dieses
  Klassifikators im Modell M1.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter).

## 6. Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Grenzen:**
- **Box:** In der periodischen Box 96 bei S0 = 0,3 bleibt ab etwa t = 1550 nur ein Klumpen.
  - Fuer Z3 braucht es Tropfen, die lange getrennt bleiben.
  - Ob eine groessere Box, eine geringere Dichte oder ein einzeln gesetzter Tropfen im Bad das leistet, ist eine
    Hypothese fuer eine neue Karte, kein Befund.
- **Verschmelzungsregel:** Sie ist streng; jede fremde Wurzel zaehlt, auch eine kurze Beruehrung.
  - Fuer s03 sind die Verschmelzungen keine kurzen Beruehrungen.
    - grob: w1 + w2 ab 960 bleibend; w0 mit (w1 w2) von 1550 bis 1640 eine Komponente, 1650 bis 1740 wieder zwei,
      ab 1750 bis 2000 eine.
    - fein: w0 + w2 ab 1520 bleibend.
    - Auch eine mildere Regel, die nur bleibende Verschmelzungen zaehlt, liesse keinen s03-Tropfen in Z3 uebrig.
  - Bei s01 sind einige nur kurze Beruehrungen (z. B. w1/w2 bei 790, getrennt bei 800). Dort ueberzeichnet der Status
    die Verschmelzungen.
- **"Verschmolzen" ist eine Maskenaussage.** Ob die Kerne des Endklumpens zu einem Q-Ball verschmolzen sind oder zwei
  Kerne aneinander haften, zeigen die Masken nicht. rmax/R_A 1,5 bis 1,9 und 10 Teile an der oberen Schwelle lassen
  beides offen. Bilder wurden nicht ausgewertet; ein S-Bild je Abschnittsende liegt im Zwischenspeicher.
- **Geschwindigkeitskorrektur** (nachtraeglich bemerkt, aendert kein Urteil): Beim Endklumpen fein ist v = 0,40. Das
  ist ein Schwerpunktfit eines sich verformenden Klumpens, mit Merker "verloren".
  - Daher omega_ruhe = 0,7773 statt omega_rot 0,7111 bzw. omega_geo 0,7158. Der Familienwert bei Q = 3409 ist 0,7164.
  - E_ruhe wird durch gamma 1,09 verkleinert, daher E/Q -8,9 % unter der Familie.
  - Fuer verformte Klumpen ist die Runde-6-Korrektur also unzuverlaessig. Runde 6 hatte die V11-Gegenprobe ebenfalls
    verfehlt.
- **E/Q unter der Familie:** Auch bei kleinem v liegen grosse Tropfen unter (E/Q)_fam.
  - Beispiele: grob k2 bei 800 (v 0,024) -1,0 %; fein k2 bei 800 (v 0,028) -1,1 %.
  - Mit groesserem v sind es bis -2,4 % (fein w0 bei 1200, v 0,20).
  - Die Familie sollte bei festem Q die kleinste Energie haben (Coleman-Argument [L, nicht nachgeprueft]). Das deutet
    auf einen Bilanzfehler der Scheibenmessung von etwa 1 bis 2 % hin [H].
- **Hauptmass dQ*:** Es ist bei duennwandigen Tropfen sehr steil in omega, wie vorab vermerkt (fein 1600: omega unter
  Tabelle, dQ* nicht definiert).
- **Fehlende Eichprobe:** Der Klassifikator wurde nie an einem Objekt geprueft, das sicher "auf" liegt (stationaerer
  Familien-Q-Ball im selben Bad). Das systematische "neben" bei s01 (omega 0,006 bis 0,010 zu tief) kann Physik oder
  Messfehler sein. Vorschlag fuer eine Folgekarte, nicht gerechnet.

**Selbstanzeigen:**
- **Spur:** s01 fein (K0 und drei Abschnitte) lief auf Spur p4000b, parallel zu s03 fein auf p4000a. Der eingefrorene
  Plan nennt fuer die Aufrufe p4000a.
  - Der Auftrag erlaubt beide Spuren. Vor dem Start lief keine WM-1-MB-Unit (systemctl geprueft), kleintest.sh prueft
    das zusaetzlich.
  - Gleiches Kartenmodell (Quadro P4000), ohne Einfluss auf die Zahlen von s03.
- **Unsinnige Zeilen bei s01:** zusammen gibt fuer s01 generisch Z1 bis Z4 und "Bedeutung" aus (zusammen_s01.txt).
  Fuer s01 sind diese Zeilen ohne Sinn; s01 ist nur beschreibend.
- **Nachtraegliche Beobachtungen:** Folgende Punkte sind nach dem Ergebnis bemerkt und nicht vorregistriert:
  - s01: "neben" und der Gegenlauf der Masse (Abschnitt 1, Punkt 5).
  - Geschwindigkeitskorrektur und E/Q unter der Familie (Abschnitt 6).
  - Sie aendern keine Regel und kein Urteil.
- **Ordner:**
  - Lokal wurde der zuerst verschachtelt kopierte Ordner lauf-69/lauf-69 per mv flach gezogen.
  - Eine doppelte Spiegelkopie liegt in hilfs/doppelte-spiegelkopie-1810/. Sie ist ein Spiegel des .69-Ordners von etwa
    18:10, ohne .pt, mit damaligem Stand der Logs; massgeblich ist lauf-69/.
  - rm gehoert nicht zu den erlaubten Befehlen; die Kopie kann geloescht werden.
- **Rauchlauf:** Er lief vor dem Einfrieren und ist im Plan dokumentiert. Die Ausgabe enthielt nur Dauern.
- **Keine weiteren Abweichungen vom Plan.** Insbesondere wurden Regeln, Schwellen und Funktionen nicht veraendert.

**Laufzeiten** (kleintest.sh, Gesamtdauer je Aufruf; Rechenanteil "entwicklung"):
- Rauch: 2,0 bis 12,6 s.
- K0: grob 7,5 s, fein 37,6 s, s01 fein 16,1 s.
- grob s03: 18,6 / 14,6 / 19,9 s.
- fein s03: 86,2 / 94,9 / 101,2 s. Entwicklung 62,6 / 67,5 / 69,9 s, also 3,1 bis 3,5 ms je Schritt.
- s01 fein: 70,4 / 76,1 / 81,4 s.
- zusammen: je etwa 3 s.
- Summe aller Rechenaufrufe etwa 650 s (knapp 11 min). Alle Aufrufe liegen weit unter 600 s, rc = 0.

**sha256:**
- Code und Plan:
  - kf5_weiter.py `9dce1fad28cfda51699f3fb3e103bf0fe50d9615e191ea7c72a6dbf473e47e11` (lokal = .69)
  - PLAN.md.eingefroren-20261002-180235 `1690c0cade1a2a4bb84700921b2477613b7a880d7b078278ac6c7e87fa0a8d51`
  - kf5_geburt.py (Runde 6, importiert) `9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0`
  - familie_2d_m0.json `f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806`
- Startzustaende (Runde 6, nur gelesen):
  - grob `6e0599b09e6a30394c3d32f00d84bfefd1aaf1645e0498d13c264231eea78285`
  - fein s03 `c23dd6f05b79f1700da25bbb60cd062fdbe65378dd89fdbaa16a7202a2a7a579`
  - fein s01 `5d0284240a79fbd8b9fe56806b19258e86d165671928b9e5ebf935d39f3c26ef`
- Ergebnisse (lokal in lauf-69/):
  - k0/k0_grob_s03.json `59213697d88cc6027cf31c7d46e300e2df2e426fd6ade5e5c1c8c36aae508ef2`
  - k0/k0_fein_s03.json `adac314e2ca47c515f3ba0abc168164c086eeb2fe55bdca0668ac76e3c8ba6a9`
  - k0/k0_fein_s01.json `3842815318e073caa78635d0e32c0bbc67177328178321c4c039abdb4be55ead`
  - abschnitte/weiter_grob_s03_*:
    - `122eec8eb710bf6cd47ae3054a26e3b17a430d44f85a06aa3b745f010c4b160a` (800-1200)
    - `0de64ab856cb9471954643dc640f8082d93b68d4f4b404f494990bbc6acfcef3` (1200-1600)
    - `f93cfba579b329dc8332b94458f98f8d1cf2069176134ed13cbe3aeb77c15038` (1600-2000)
  - abschnitte/weiter_fein_s03_*:
    - `18363823d4cc1d3fe3d9da08fadfacdc1ed98ed82abdb8853375c02e9eceff3e` (800-1200)
    - `19613a51fbd59616ee91a4ab803290a57b0d8e9d171bc64500d1b652cae2ad72` (1200-1600)
    - `1445fb0039606d66ace5899de0ac90a63e0911c95e0cc631ee01c5f3591197aa` (1600-2000)
  - abschnitte/weiter_fein_s01_*:
    - `5fd9622a7f60798179524ec49e03da3bf47f367f10921fc2fba938411509f5a4` (800-1200)
    - `bdc4c30d319a8fd130a52ac7b025969b4d35de95e5b689639c1396b78935a5ed` (1200-1600)
    - `d569ac8298350bb1b4c45a8b2d898b6b5c0d8563e7f197113197478843ebfe5a` (1600-2000)
  - zusammen_s03.json `99442eefef194ddcd39f1890417b0f1a0b02f0f01d989f889799aeb1db433c17`, zusammen_s03.txt
    `22b407e573b916b1092c544d2ea283a8e3851f4b933ad05df60eb432410e3f8a`
  - zusammen_s01.json `d94a5d44dab1d004963ef2762b3beda2dc1f1571a8c492a7aa92e93f36e664c6`
- Zwischenspeicher (nur auf der .69, runde20-kf5-weiter/lauf-69/zwischen/, complex128 psi und vel, Etiketten, S-Bild):
  - grob t1200 / t1600 / t2000:
    - `df454aa58a38afa3ca8c2283f91f2e5623db760a41bf855ba3db5eb086bef5b3`
    - `b6bdaea897150ed835d6866bc3472e6c7d7e945b62a495765bdb4c29b6006b57`
    - `3768e8ec0726dcbba46240bdef2ec45f7ea4a089fe897548a3775b992a9070b5`
  - fein s03 t1200 / t1600 / t2000:
    - `c4c822dc394f3c3b712094ec27ce07357dff9753fa2cadd660bddf38a7eb23ff`
    - `697a2c105fbcc341f24449029fbc99ae7fd0e4ad6c1ff25af81768be4fe7f27d`
    - `e3599b0afb4e1970e5c0915370ff11ea79019e0c42d3abd0cbe049538792185d`
  - fein s01 t1200 / t1600 / t2000:
    - `7afca3f8187afd349944e1286342ed105e90cab5b983784700b5b0d82a647eab`
    - `a6b606b4af4b612c51f02dcfa0ed856ba5058346c841246de7a6f366348efe11`
    - `863f1e409f7b8a39a99c78887df61795094397c86f122dd75c196b8686fb3c13`

**Dateien:**
- Kartenordner: KARTE.md, PLAN.md (+ eingefrorene Fassung), kf5_weiter.py, ERGEBNIS.md, hilfs/tabelle.jq (nur
  Darstellung).
- lauf-69/: k0/, abschnitte/, rauch/, zwischen/*_linie.json, zusammen_*.json/.txt, LAUF.log, LAUF-s01.log, RAUCH.log.
- Auf der .69: /home/fmh/fmhc-physics-remote/runde20-kf5-weiter/ (dazu die .pt-Zwischenspeicher und k0/*_linie.pt).

## 7. Einfach gesagt

Wir haben die Kiste mit den Feldtropfen aus Runde 6 weiterlaufen lassen, von Zeit 800 bis 2000. Wir wollten sehen, ob
die Tropfen sich beruhigen und zu "echten", ruhigen Q-Baellen werden. Zuerst haben wir geprueft, dass unser Messgeraet
genau dasselbe sagt wie damals, und das tut es Ziffer fuer Ziffer. Dann zeigte sich aber etwas anderes: Bevor die
Tropfen sich beruhigen koennen, stossen sie zusammen und verschmelzen zu einem einzigen grossen, wackelnden Klumpen. So
bleibt kein einzelner Tropfen uebrig, an dem man die Frage pruefen koennte. Darum wird die Karte geparkt, nicht
verworfen: Man braucht einen Versuch, in dem die Tropfen sich nicht so schnell treffen.

Ende der Bearbeitung: 2026-10-02 18:17:42 CEST (date).
