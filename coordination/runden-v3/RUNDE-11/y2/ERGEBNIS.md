# Y-2 (Runde 11): Quartik je Kanal mit nachgestimmtem U und Rabi-Arm, Ergebnis

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5) fuer die Leitung claude-primary. Explorativ (v3).
- **Das ist eine andere Theorie als unsere Gesamtformel:** + c sum_a |psi_a|^4 mit b_0 = 1 + c/3 (Arme A, B) bzw. ein
  Rabi-Term - eps sum_{a<b} Re(psi_a^* psi_b) (Arm C). Alles [H]: Vorbild, kein Proton, kein QCD, kein Eichfeld.
- Zeitkette (date, CEST; die .69 loggt UTC = CEST - 2 h):
  - Beginn 12:34:36; y2.py kopiert 12:41:52; PLAN.md ab 12:47:01, eingefroren 12:48:34
  - Rauchtest lokal 12:48:42 bis 12:50:38; Nachtrag 9 im Plan 12:50:43; y2.py auf der .69 12:51:02
  - Laeufe LAUF1 bis LAUF4 12:51:06 bis 13:01:43; dieser Bericht ab 13:03:16; Ende in der letzten Zeile
- Vorab vor der Ergebnisdatei: PLAN.md.eingefroren-20260930-124834 (mtime 12:48:33) und Nachtrag 9 (12:50:43) liegen vor
  der ersten Ergebnisdatei der .69 (y2a/y2b_ergebnis.json, 10:55:45 bzw. 10:56:21 UTC = 12:55/12:56 CEST).
- Belegstufen: [num] numerisch (eine Gitterstufe), [num+K] mit Kontrolle, [Bild] aus den PNG gelesen, [Hand] Herleitung,
  [H] Hypothese, [nachtr.] Deutung erst nach dem Ergebnis.
- Quellen: lauf-69/ausgabe/y2b, y2a, y2c_ergebnis.json und _bericht.txt, y2auswertung_bericht.txt (bindende Auswertung
  nach PLAN 1 und 3), PNG; Logs lauf-69/LAUF1 bis LAUF4.

## 0. Ergebnis in fuenf Punkten

1. **Ausgang nach der Scheiterregel (Wortlaut, Lesart PLAN Z3 bis Z6):** Arm B (c = 2, b_0 = 1,667): **"weder noch"**.
   Arm A (c = 1, b_0 = 1): **"weder noch"**. Arm C (eps = 0,3): **"Quartik traegt das Y nicht"** (Arm-Name ersetzt: der
   Rabi-Term traegt es nicht), ausgeloest durch Windung 0 bei r = 4,5 in 3 von 3 Dreiern. Kein Arm zeigt "Y" oder "Dreieck".
2. **In allen drei Armen dasselbe Bild: ein leerer "Beutel", kein Wandnetz** [num, Bild: 9 von 9 angesehen]. In allen 9 Dreier-Geometrien
   (je Arm gleichseitig 9 und 12, kollinear 8) liegt ein Loch mit S < 0,05 S_max ueber dem ganzen Dreieck (kollinear:
   Schlitz A-B-C); die drei Wirbel sitzen auf seinem Rand. Das Kopplungsdefizit ist nur am Lochrand nahe den Wirbeln
   von null verschieden; auf den Steiner-Armen und an den Kanten gibt es 0 Rippen (Kantenmitte AB: S/S_0 = 0,0003 bis 0,009).
   Beide Saaten (neutral, Y) enden in 9 von 9 Geometrien im selben Zustand (gleiche E auf allen gedruckten Stellen).
3. **Vorab: 1 von 7 getroffen.** Arm B: (i) getroffen (nach Wortlaut), (ii) (iii) (iv) (v) verfehlt; Erwartung Arm A
   verfehlt; Erwartung Arm C verfehlt. Knapp nur B (iii): 5,35 gegen 3 bis 5, innerhalb der Gitterunsicherheit +-0,6 aus
   Y-1; B (v) liegt mit 2,09 klar ueber 1.
4. **Auffaellig:** Die Energie des Beutels haengt kaum von c ab: Arm B gleichseitig 9/12 = 2166,795/2172,148 gegen
   Y-1 ohne c mit demselben Ring 2166,678/2172,060 (+0,12/+0,09; gleicher Ball b = 1,1667, Q = 3600). [Hand, nachtr.]
   Grund: Die Quartik bestraft Entmischung, ein ganz leeres Loch (S -> 0) aber nicht. Ein Loch kostet im Ball nur den
   Innendruck p = omega^2 S_0 - U(S_0) = 0,017 je Flaeche (B, C; A: 0,009) plus Rand; bei Nitta u. a. kostet Entleeren
   (lambda/4) v^4 = 0,5 je Flaeche. Die Annahme aus ALT-1 ("Entleeren eines Kerns teurer machen") trifft das Loch nicht [H].
5. **Kontrollen bestanden:** Reproduktion Y-1 (c = 0, b_0 = 1) bitgleich (2166,6778595004525, relativ 0); Ball in Arm C
   mit Q_C = 1142,5 exakt wie Arm B (S_0 1,1786, R_halb 29,025; omega 0,18329 gegen vorhergesagt 0,18330); dE1000 <= 1,6e-7,
   Schub <= 0,09 in allen 37 Konfigurationen. **Einschraenkung:** Die Windung bei r = 4,5 misst in diesen Zustaenden nicht
   sicher "Gegenwirbel", weil der Kreis das Loch schneidet (Abschnitt 4); die Arm-Unterschiede bei (i) sind deshalb
   nicht belastbar.

## 1. Tabelle je Arm (beste Saat; beide Saaten gleich)

Quelle: y2*_bericht.txt, y2auswertung_bericht.txt. E in Code-Einheiten; Arm C hat kleinere Ladung (Z1), deshalb
kleinere E. Vergleichbar sind nur Differenzen innerhalb eines Arms.

| Arm | gleich 9 | gleich 12 | kollinear 8 | (iii) E12 - E9 | (v) E_koll8 - E9 | Zustand [Bild] |
|---|---|---|---|---|---|---|
| B: c = 2, b_0 = 1,6667 | 2166,79485 | 2172,14813 | 2168,88533 | 5,353 | 2,090 | Beutel in 3/3 |
| A: c = 1, b_0 = 1 | 2978,34514 | 2981,01313 | 2979,39026 | 2,668 | 1,045 | Beutel in 3/3 |
| C: eps = 0,3, Q = 1142,5 | 298,39364 | 303,85887 | 300,35822 | 5,465 | 1,965 | Beutel in 3/3 |
| Y-1 ohne c, Ring r < 4 (Vergleich) | 2166,6779 | 2172,0604 | - | 5,383 | - | Beutel (Y-1 4.2) |

Meson (psi_1-Wirbel und -Gegenwirbel):

| Arm | Hauptreihe E(6 / 9 / 12), Ring 2,5 / 4 / 4 | Steigung 6->9 / 9->12 | Kontrollreihe Ring r < 2, E(6 / 9 / 12) | Steigung 6->9 / 9->12 |
|---|---|---|---|---|
| B | 2155,1914 / 2160,1952 / 2164,0607 | 1,668 / 1,289 | 2162,2493 / 2164,3412 / 2164,3916 | 0,697 / 0,017 |
| A | 2970,8831 / 2973,9630 / 2976,3173 | 1,027 / 0,785 | 2972,0630 / 2974,8999 / 2974,9910 | 0,946 / 0,030 |
| C | 297,0529 / 292,7872 / 296,7193 | -1,422 / 1,311 | 295,0887 / 297,5227 / 297,6651 | 0,811 / 0,047 |

- In allen 18 Mesonlaeufen entsteht ein Wirbel-Gegenwirbel-Paar knapp ausserhalb des Klammerrings (Wirbelzaehlung je
  Komponente: Gegenwirbel 4,0 bis 4,1 vom Klammerzentrum bei Ring 4, 2,5 bei Ring 2,5, 1,9 bis 2,0 bei Ring 2) [num]. Das Band
  reisst also auch hier durch Paarbildung, wie in Y-1.
- Kontrollreihe (einheitlicher Ring r < 2): in allen drei Armen flach ab d = 9 (9 -> 12: 0,017 / 0,030 / 0,047), wie Y-1
  meson und mesonc.
- Hauptreihe: nach Wortlaut nicht flach (9 -> 12 >= 0,3 x 6 -> 9 in B und A; in C ist 6 -> 9 negativ). Der Anstieg 9 -> 12
  bei Ring 4 passt zu Y-1 dreier_k4 (Meson dort linear bis ~12, flach ab 15) [nachtr.]; d = 6 hat einen anderen Ring
  (2,5, Z2) und in C einen anderen Zustand (S_loch 0,70 gegen 0,00 bei d = 9 und 12). Die Steigung 6 -> 9 der Hauptreihe
  mischt also Klammer und Zustand.

## 2. Vorab gegen Ausgang

Vorab: PLAN.md 1 (ALT-1 Zeilen 232 bis 237, woertlich) mit den Lesarten Z3, Z4, Z6; eingefroren 12:48:34.

| Nr. | Vorab (kurz) | Ausgang | Bewertung |
|---|---|---|---|
| B (i) | keine Gegenwirbel (Windung r = 2,5 und 4,5 gleich 1) in >= 4 von 5 (Lesart: Anteil >= 0,8) | 6 von 6 Windung 1 bei 2,5 und 4,5; r = 2,5 durch die Klammer erzwungen (Z3); r = 4,5 schneidet das Loch | getroffen nach Wortlaut, inhaltlich nicht belastbar |
| B (ii) | Rippe innerhalb 1,5 der Steiner-Arme, Knoten (P-Windung 2) innerhalb 1,5 von J | Knoten: P-Umlauf um J bei r = 1,5 = 2,00 in 3/3; Rippen: 0 von 8 Armen (D auf den Armen ~0, weil S ~ 0) | verfehlt |
| B (iii) | E(gleich 12) - E(gleich 9) = 3 bis 5 | 5,353 | verfehlt (knapp, innerhalb +-0,6 Gitterunsicherheit) |
| B (iv) | Meson linear bis 12, Steigung 0,6 bis 1,0 (beide Abschnitte, Z6) | 1,668 / 1,289; Paarbildung in allen drei | verfehlt |
| B (v) | E(kollinear 8) - E(gleich 9) < 1 | 2,090 (ALT-1 nennt fuer "Dreieck" +2,0) | verfehlt |
| A | (i) verfehlt in >= 2 von 5 (Lesart: Anteil >= 0,4) | 0 von 6 mit Windung != 1 | verfehlt |
| C | eine Rippe je Arm statt zwei (Mitte, >= 2/3 der Arme) | 0 Rippen an 8 von 8 Armen | verfehlt |

- Summe: 1 von 7 getroffen (B (i), nur nach Wortlaut).
- Die Vorab-Erwartungen gingen wie in Y-1 von Waenden auf den Armen aus. Es gibt in keinem Arm Waende; daher die
  Fehltreffer.
- Zaehl-Lesart (Z3) aendert nichts: B (i) 6 >= 4 getroffen, A 0 >= 2 verfehlt.

## 3. Scheiterregel je Arm (Wortlaut ALT-1 Zeilen 238 bis 244, Reihenfolge Z5)

| Arm | nicht auswertbar? | Gegenwirbel (Windung r 2,5/4,5) in Dreier-Geometrien | Meson flach (Hauptreihe) | "Dreieck": Kantenmitten n_a/S < 0,1 an >= 2 | "Y": (i), (ii), (iii) | Urteil |
|---|---|---|---|---|---|---|
| B | nein (dE1000 <= 8,4e-8, Schub <= 0,07) | 0 von 3 | nein (1,289 >= 0,500) | nein (0 von 3 je gleichseitige Geometrie) | (i) ja, (ii) nein, (iii) nein | **weder noch** |
| A | nein (dE1000 <= 6,9e-8, Schub <= 0,09) | 0 von 3 | nein (0,785 >= 0,308) | nein | (i) ja, (ii) nein, (iii) nein | **weder noch** |
| C | nein (dE1000 <= 9,0e-8, Schub <= 0,08) | 3 von 3 | nein (6 -> 9 negativ) | nein | (i) nein | **"Quartik traegt das Y nicht"** |

- Arm C: ausgeloest allein durch Windung 0 bei r = 4,5 (gleichseitig 9: Wirbel C; gleichseitig 12: alle drei; kollinear 8:
  A und C). Die Bilder zeigen in C denselben Beutel wie in A und B. Nach Wortlaut gilt das Urteil; dass die Windung dort
  durch das Loch gemessen wird, steht in 4.
- Die Kantenmitten-Bedingung "n_a/S < 0,1" greift nicht, weil an den Kantenmitten S/S_0 = 0,0003 bis 0,009 ist (Loch) und das
  Verhaeltnis n_a/S dort 0,25 bis 0,33 betraegt.

## 4. Kontrollen und Einschraenkungen

- **Reproduktion (Z7)** [num+K]: y2.py mit c = 0, b_0 = 1, eps = 0, Ring 4, gleichseitig 9, Y-Saat im Stapel von Arm A:
  E = 2166,6778595004525, Y-1 dreier_k4 2166,6778595004525, relativ 0. Die Codeaenderungen lassen die alte Physik bitgleich.
- **Ball in Arm C (Z1)** [num+K]: b 1,1667, m 0,7, Q 1142,5: omega 0,18329 (Hand 0,18330), S_0 1,1786, R_halb 29,025,
  Residuum 2,7e-11; Arm B: S_0 1,1786, R_halb 29,025. Die Abbildung m -> m - eps, omega^2 -> omega^2 - eps haelt.
- **Vorab-Probe** (PLAN 2): Ausgabe b = 1,1667 (B, C), 0,8333 (A), m = 0,7 (C), wie per Hand.
- **Energie:** statischer Gradientenfluss bei fester Ladung, keine Zeitentwicklung; eine Energieerhaltung gibt es hier
  nicht zu pruefen. Die Energiekontrolle ist die Konvergenz dE1000 (Aenderung von E ueber die letzten 1000 Iterationen),
  wie ALT-1 sie fuer "nicht auswertbar" verlangt.
- **Konvergenz und Schub:** dE1000 <= 1,6e-7 in allen 37 Konfigurationen (36 plus Reproduktion) (Schwelle 0,02); Schub <= 0,09 (Schwelle 30);
  ein Klumpen; Kreis um alle drei: 0 Wandwechsel in 9 von 9. Schleifen 269,6 bis 307,3 s, kein Budgetabbruch.
- **Zwei Saaten** [num+K]: neutral und Y gleich in 9 von 9 Dreiern (E auf 5 Stellen gleich).
- **Windungen [Messen die zwei Zahlen dasselbe? nachtr.]:**
  - r = 2,5 liegt im Klammerring (r < 4) und ist erzwungen (Z3, vorab benannt).
  - r = 4,5: In allen Beutel-Zustaenden schneidet der Kreis um jeden Wirbel das Loch (der Lochrand laeuft durch die Wirbel,
    das Loch fuellt den 60-Grad-Keil zwischen den Kanten). Dort ist die Phase eines fast verschwindenden Feldes
    gemessen. Die Wirbelzaehlung je Komponente findet in B gleichseitig 12 und kollinear 8 sowie in C Plaketten-
    Gegenwirbel 4,0 bis 5,1 vom Wirbel, in A keine; alle diese liegen im Loch. Y-1 hatte dieselbe Unsicherheit
    ("unsicher, wo der Kreis ein Loch schneidet").
  - Folge: Die Unterschiede zwischen den Armen bei (i) und das Urteil fuer C beruhen auf einer Groesse, die in diesen
    Zustaenden nicht "Gegenwirbel im dichten Feld" misst. Das Urteil bleibt nach Wortlaut; inhaltlich zeigen die drei
    Arme denselben Zustandstyp.
- **Gitterprobe:** von ALT-1 nicht verlangt, nicht gerechnet. Y-1 fand fuer Energiedifferenzen zwischen Geometrien +-0,6
  bei dx 0,3; B (iii) (5,35 gegen 5) liegt innerhalb dieser Spanne um die Grenze. In A (dort keine Vorab-Zeile zu (iii)
  und (v)) laegen 2,67 und 1,045 ebenso nahe an 3 bzw. 1.

## 5. Einordnung

- [num] Mit c = 2 (b_0 nachgestimmt), c = 1 oder eps = 0,3 bleibt der festgehaltene Dreier bis a = 12 ein Beutel. In Y-1
  ohne c war das mit Ring 4 ebenso (gleichseitig 9 und 12 Beutel), mit Ring 2 nur bis a = 9. Der Umbau aendert Zustand
  und Energie also kaum.
- [Hand, nachtr.] Warum: Im duennwandigen Q-Ball sind Inneres und Vakuum fast entartet. Ein Loch der Flaeche A kostet
  bei fester Ladung (omega^2 S_0 - U(S_0)) A = p A mit p = 0,33360 x 1,1786 - 0,37658 = 0,0166 (B, C) bzw. 0,0085 (A),
  dazu seinen Rand. Die Quartik verteuert nur Entmischung (Kern ohne die eigene, mit den anderen Komponenten; ALT-1 A4:
  0,51 je Flaeche), nicht das volle Loch. Dem System bleibt der billige Ausweg "alles leer". Bei Nitta u. a. ist das
  Vakuum das Kondensat selbst; dort kostet jedes Loch (lambda/4) v^4 = 0,5 je Flaeche, 30-mal mehr als hier.
- [H] Ein Y-Knoten wie bei Nitta u. a. braucht deshalb in der Ball-Fassung eine Groesse, die ein leeres Gebiet im Ball
  teuer macht (hoeherer Innendruck p, etwa kleinerer Ball oder weiter weg von der Duennwand-Grenze), nicht nur eine
  teure Entmischung. Nicht gerechnet.
- L1 ja (Test konnte in beide Richtungen ausgehen; 6 von 7 Vorab-Zeilen verfehlt). L2 ja (Reproduktion, Ball-Abbildung,
  zwei Saaten, zwei Mesonreihen). L3 teilweise (eine Gitterstufe). L4: Beutel und Stringbruch wie Y-1, Literatur-Y nur
  festgehalten und mit teurem Loch (ALT-1). L5 nein (modellintern).
- Vorschlag: Y-2 in dieser Form **verwerfen**; Quartik und Rabi-Term aendern den Beutel nicht. Wer weitergeht: zuerst
  per Hand pruefen, ob ein Ball mit p >> 0,02 je Flaeche und stabilem Vakuum in der Formelfamilie existiert
  (Ableitbarkeitsprobe vor jedem Lauf), und die Gegenwirbel-Pruefung auf Kreise legen, die das Loch nicht schneiden.

## 6. Abweichungen, Verstoesse (Selbstanzeige)

- Abweichungen vom Plan: keine an Arm, Geometrie, Schwelle oder Lesart. Zwei Programmfehler nach dem Einfrieren und vor
  jedem Lauf behoben (PLAN 9: Berichtszeile, Auswertung bei fehlenden Geometrien), offengelegt.
- LAUF3 wartete am Spur-Lock p4000a hinter LAUF1 (bewusst so gestartet): Aufruf 12:51:26 bis 13:01:27 = 10 min 01 s
  Wanduhr, davon Rechnung 4 min 57 s (Dienstzeit). Die 10-min-Grenze fuer die Rechnung (RuntimeMaxSec 600) ist
  eingehalten, die Aufrufdauer inklusive Warten um 1 s ueberschritten.
- Lokal: Python nur im Rauchtest (CPU, 1 Thread, nice 19, CUDA_VISIBLE_DEVICES leer): 3 Aufrufe mit Fehler (rc 1, 33 s),
  3 Aufrufe nach der Behebung (33 s), 1 Auswertungsaufruf auf den Rauchdaten (2 s); zusammen etwa 70 s. Kein awk, keine
  leeren Interpreteraufrufe.
- Ausserhalb der erlaubten Ordner geschrieben: eine Hilfsdatei scratchpad/sec8.txt (Hash-Zeile fuer den Plan) im
  Sitzungs-Scratchpad. Die Hintergrund-Ausgaben des Werkzeugs liegen ebenfalls dort.
- Auf der .69 nur ueber kleintest.sh (Spuren p4000a, p4000b); y2.py per neue Datei + mv; kein python ausserhalb von
  kleintest.sh. Kein git, kein Peerbus, keine Unteragenten, keine Dienste, keine gesperrten Pfade geoeffnet.

## 7. Dateien, Laufzeiten, Hashes

- y1.py (RUNDE-10/y1, unveraendert) sha256 d04cdfd861c1192888ba9829485fa8198c7289a4e28c04749eb7cffac8d1e986.
- y2.py sha256 e0f4559ace72d2c82b1004028cb04bdcf5457bff29a79490e1175f283682f5af (lokal = .69,
  /home/fmh/fmhc-physics-remote/runde11-y2/y2.py); beim Einfrieren 3de388e0... (vor den zwei Programmfehler-Behebungen).
- PLAN.md.eingefroren-20260930-124834 sha256 f79c87f082bd6864069d9c6a204228ed7e3d1cc7e4f327ac250710ec58119997.
- Ausgaben lauf-69/ausgabe/ (Berichte, JSON, PNG), Logs lauf-69/LAUF1 bis LAUF4; Rauchtest lauf-lokal/ (ungueltig).
- Wichtige Bilder: y2b_g+0.5_gleich9_Y_B.png, y2b_g+0.5_gleich12_Y_B.png, y2b_g+0.5_kollinear8_Y_B.png,
  y2a_g+0.5_gleich12_Y_A.png, y2c_g+0.5_gleich12_neutral_C.png (Beutel in allen).

| Lauf | Stapel | Spur | Start / Ende (UTC) | Schleife | Dienst |
|---|---|---|---|---|---|
| LAUF1 | y2b (Arm B, 12) | p4000a | 10:51:06 / 10:56:30 | 307,3 s | 5 min 25 s |
| LAUF2 | y2a (Arm A, 12 + Reproduktion) | p4000b | 10:51:07 / 10:55:56 | 269,6 s | 4 min 48 s |
| LAUF3 | y2c (Arm C, 12) | p4000a | 10:51:26 (Lock) / 10:56:33 Start / 11:01:27 | 269,6 s | 4 min 57 s |
| LAUF4 | y2auswertung | p4000a | 11:01:40 / 11:01:43 | - | 3 s |

- GPU-Zeit zusammen etwa 15 min (P4000). Alle Rechnungen rc = 0.

## Einfach gesagt

Wir haben die Regeln unseres Modells auf drei Arten umgebaut (zweimal wird das Entmischen der Felder teurer, einmal
werden die Felder direkt aneinander gekoppelt) und wieder drei Wirbel festgehalten, um einen Y-foermigen Faden zwischen
ihnen zu finden. In allen drei Faellen entstand kein Faden, sondern wieder ein leeres Loch zwischen den drei Wirbeln.
Der Grund: In unserem Feldklumpen kostet ein ganz leerer Fleck fast nichts, die Umbauten machen aber nur das halbe
Leeren teuer. Nach der vorab festgelegten Regel heisst das zweimal "weder Y noch Dreieck" und einmal "traegt nicht",
wobei dieses eine Urteil an einer Messung haengt, die im Loch unsicher ist.

- Ende (date): 2026-09-30 13:07:14 CEST. Dateien nur in RUNDE-11/y2/ und auf der .69 in runde11-y2/ (ausser scratchpad/sec8.txt, siehe 6).
