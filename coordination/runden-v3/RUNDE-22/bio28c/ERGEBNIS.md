# Runde 22, bio28c: Ergebnis

Code-Agent (Opus 5.5) fuer claude-primary. Karte KARTE.md, Plan PLAN.md.eingefroren-20261002-194815 (eingefroren
19:48:15 CEST, vor dem Hauptlauf; davor nur der dokumentierte Rauchlauf). Hauptlauf auf der .69 von 17:53:59 bis
17:55:29 UTC (19:53:59 bis 19:55:29 CEST), rc 0. Bericht begonnen 19:57:54 CEST (date). Explorativ (v3), [H].

## 1. Ergebnis

1. **J0 eingetroffen.**
   - Ein exakter Drehball m = 1 allein ergibt L_z/Q = 1 - 7e-16 (w60 und w75).
   - L_box bleibt in allen vier Laeufen bis T = 90 auf hoechstens 8e-14 relativ erhalten. Nichts erreicht den Rand.
2. **J1 eingetroffen (4 von 4 Laeufen).** Bei T = 60 tragen die Toechter als Bahndrehimpuls (a) 0,63 / 0,84 / 0,62 /
   0,52 des Anfangsdrehimpulses (w60_nachbarn1 / w60_nachbarn2 / w75_nachbarn1 / w75_nachbarn2).
3. **J2 nicht eingetroffen, nach der vorab eingefrorenen Lesart "alle vier Laeufe".**
   - |b|/L0 bei T = 60: 0,036 / 0,166 / 0,019 / 0,044.
   - Die Toechter von w60_nachbarn2 tragen Eigendrehimpuls gegen den Anfangsdrall (b = -0,166). Sie tragen dafuer
     mehr Bahn (0,84).
   - Die Karte nennt fuer J2 keine Laufzahl; die Lesart "alle vier" ist meine Festlegung (PLAN 4.2). Mit "3 von 4"
     wie bei J1 waere J2 eingetroffen. Ich aendere nichts; die Leitung entscheidet.
   - **Bedeutung nach Karte:** Fuer "J1 ja, J2 nein" ordnet die Karte keine Bedeutung zu. Die Ausgaenge stehen ohne
     Deutung.
4. **(c) ist in der Maskenzerlegung zum grossen Teil Schwanz, nicht Abstrahlung.**
   - (c) liegt schon bei t = 0 bei 0,31 bis 0,35. Das ist der Teil der Baelle unter der Maskenschwelle.
   - Bei T = 60 ist (c) 0,33 bis 0,43. Die Zusatz-Zerlegung mit Zonen (Radius 12 um die Toechter) gibt dort einen
     Fernanteil von -0,08 bis +0,24. Am groessten ist er in w75_nachbarn2 (0,24 von 0,43; Bahn in Zonen 0,67).
   - Kontrolle: Die Maske erfasst 81 bis 83 % eines reinen Eigendrehimpulses und 56 bis 64 % eines reinen
     Bahndrehimpulses; die Zonen erfassen beides zu ueber 99,9 %.
5. **Ableitbarkeit: J1 und J2 waren aus den Bio-28b-Rohdaten vorab ableitbar.**
   - Die Karte sagt "nicht ausgegeben". bio28b.py speichert aber je Gebiet E, v, Schwerpunkt und Jspin/Q, dazu
     J_box_start.
   - Nachgerechnet mit jq: (a) und (b) stimmen mit bio28c bis auf 1,3e-4 ueberein (bei T = 60 bis auf 5e-5). Die
     Gebiete sind bis auf die Rundung gleich; es ist dieselbe Rechnung.

## 2. K0 (Normierung, Erhaltung)

**Konvention** (PLAN 2, vor jedem Lauf; r5.dichten unveraendert):
- rho = 2 Im(psi conj psi_t), P_i = -2 Re(conj(psi_t) d_i psi), L_z = Int (x P_y - y P_x).
- Fuer f(r) e^{i m theta - i omega t} gilt punktweise x P_y - y P_x = m rho, also L_z = m Q.

**Kontrollen bei t = 0** (grob, Box L = 115,2, eigene Maskenschwelle je Feld):

| Feld | L_z/Q | (a)/L | (b)/L | (c)/L | Zonen (a) / (b) / (c) | bestanden |
|---|---|---|---|---|---|---|
| m1_w60 (Drehball m = 1, Q 138,757) | 0,9999999999999993 | 0 | 0,832 | 0,168 | - / 0,9999 / - | K0a ja |
| m1_w75 (Drehball m = 1, Q 66,234) | 0,9999999999999993 | 0 | 0,808 | 0,192 | - / 0,9997 / - | K0a ja |
| m0_w60_ruhend bei (10, -7) | 3e-17 | - | - | - | - | K0b ja |
| paar_w60 (L = -276,9) | - | 0,635 | -6e-9 | 0,365 | 1,0000 / -7e-6 / 8e-6 | Vorzeichen ja |
| paar_w75 (L = -90,1) | - | 0,558 | -1e-8 | 0,442 | 1,0000 / -2e-5 / 3e-5 | Vorzeichen ja |

- Das Paar (Ball bei +y laeuft nach +x) hat L < 0, wie fuer eine Bahn im Uhrzeigersinn erwartet. (a)/L ist positiv,
  (b) praktisch null.
- Q_box der Drehballkontrollen stimmt mit dem Profil-Q auf 2e-12 relativ ueberein.

**K0c, Erhaltung bis T = 90** (Messtakt 0,5):

| Lauf | L0 | Q_m1 | L0/Q_m1 | max abs(L/L0 - 1) | E_Rand max / E0 | Q(90)/Q0 | E(90)/E0 |
|---|---|---|---|---|---|---|---|
| w60_nachbarn1 | 146,194 | 138,757 | 1,054 | 8,7e-15 | 4e-17 | 1,0000000 | 0,999987 |
| w60_nachbarn2 | 153,632 | 138,757 | 1,107 | 4,2e-15 | 6e-17 | 1,0000000 | 0,999990 |
| w75_nachbarn1 | 72,529 | 66,234 | 1,095 | 2,1e-14 | 1e-16 | 1,0000000 | 0,999993 |
| w75_nachbarn2 | 78,823 | 66,234 | 1,190 | 7,7e-14 | 2e-16 | 1,0000000 | 0,999988 |

- K0 = K0a und K0b und K0c in allen vier Laeufen: **bestanden**. Vorzeichenprobe bestanden.
- Die Erhaltung auf Maschinengenauigkeit passt zum Verfahren [S]: Velocity-Verlet erhaelt eine quadratische
  Erhaltungsgroesse einer linearen Symmetrie exakt. Die spektralen Ableitungen machen das Gitter fuer diese glatten
  Felder praktisch drehsymmetrisch. Die Energie schwankt dagegen um 1e-5.
- **L0 ist 5 bis 19 % groesser als Q_m1.** Grund ist der Ueberlapp der Anfangsfelder: Wo Drehball und Nachbar
  ueberlappen, entsteht Impulsdichte. Die Zonen-Zerlegung zeigt diesen Teil bei t = 0 als Bahn (0,04 bis 0,20).
  Alle Anteile beziehen sich auf L0 (Karte: "Anfangsdrehimpuls").

## 3. Tabelle je Lauf und Zeit

Legende:
- Alle Werte sind Anteile von L0 = L_box(t = 0) des Laufs.
- (a) Bahn um X0, (b) Eigen um den eigenen Schwerpunkt, (c) Rest ausserhalb der Maskengebiete.
- s = X0 x Sum P_k ist das Schliessglied, damit L = a + b + c + s exakt gilt (Rest der Summe hoechstens 2e-16).
- Zonen sind die Zusatz-Zerlegung (kein Kriterium): naechster Gebietsschwerpunkt, hoechstens 12 entfernt.
- n ist die Zahl der Gebiete.

| Lauf | t | n | L/L0 | (a) Bahn | (b) Eigen | (c) Rest | s | Zonen (a) / (b) / (c) |
|---|---|---|---|---|---|---|---|---|
| w60_nachbarn1 | 0 | 2 | 1 | -0,012 | 0,685 | 0,308 | 0,019 | 0,036 / 0,947 / 0,000 |
| w60_nachbarn1 | 20 | 2 | 1 | 0,583 | -0,056 | 0,346 | 0,127 | 0,915 / 0,064 / 0,001 |
| w60_nachbarn1 | 40 | 2 | 1 | 0,557 | -0,034 | 0,504 | -0,028 | 0,921 / 0,059 / 0,007 |
| w60_nachbarn1 | 60 | 2 | 1 | 0,625 | -0,036 | 0,368 | 0,042 | 0,991 / -0,040 / 0,031 |
| w60_nachbarn1 | 90 | 2 | 1 | 0,642 | -0,044 | 0,337 | 0,066 | 0,970 / -0,038 / 0,034 |
| w60_nachbarn2 | 0 | 3 | 1 | 0,012 | 0,675 | 0,313 | 0 | 0,101 / 0,899 / 0,000 |
| w60_nachbarn2 | 20 | 2 | 1 | 1,027 | -0,134 | 0,107 | 0 | 1,303 / -0,302 / -0,000 |
| w60_nachbarn2 | 40 | 2 | 1 | 0,749 | -0,181 | 0,432 | 0 | 1,320 / -0,301 / -0,019 |
| w60_nachbarn2 | 60 | 2 | 1 | 0,839 | -0,166 | 0,328 | 0 | 1,382 / -0,305 / -0,077 |
| w60_nachbarn2 | 90 | 2 | 1 | 0,769 | -0,155 | 0,386 | 0 | 1,303 / -0,283 / -0,020 |
| w75_nachbarn1 | 0 | 2 | 1 | -0,007 | 0,634 | 0,350 | 0,023 | 0,087 / 0,891 / 0,000 |
| w75_nachbarn1 | 20 | 2 | 1 | 0,512 | -0,041 | 0,403 | 0,126 | 0,704 / 0,264 / 0,001 |
| w75_nachbarn1 | 40 | 2 | 1 | 0,663 | -0,022 | 0,324 | 0,035 | 0,823 / -0,041 / 0,158 |
| w75_nachbarn1 | 60 | 2 | 1 | 0,623 | -0,019 | 0,341 | 0,055 | 0,885 / -0,056 / 0,145 |
| w75_nachbarn1 | 90 | 2 | 1 | 0,626 | -0,017 | 0,341 | 0,049 | 0,889 / -0,049 / 0,146 |
| w75_nachbarn2 | 0 | 3 | 1 | 0,024 | 0,624 | 0,352 | 0 | 0,201 / 0,799 / 0,000 |
| w75_nachbarn2 | 20 | 2 | 1 | 0,969 | -0,052 | 0,083 | 0 | 1,186 / -0,181 / -0,004 |
| w75_nachbarn2 | 40 | 2 | 1 | 0,423 | 0,033 | 0,544 | 0 | 1,009 / -0,069 / 0,061 |
| w75_nachbarn2 | 60 | 2 | 1 | 0,525 | 0,044 | 0,431 | 0 | 0,668 / 0,090 / 0,242 |
| w75_nachbarn2 | 90 | 2 | 1 | 0,501 | 0,055 | 0,444 | 0 | 0,627 / 0,139 / 0,235 |

- Erzeugt mit hilfs/tabelle.jq aus lauf-69/ausgabe/bio28c_auswertung.json (Rohfassung hilfs/tabelle.md).
- L/L0 ist zu jeder Zeit 1 auf 1e-13.
- Je Gebiet (Q, Lage, Bahn, Eigen, Jspin/Q, Windung): lauf-69/ausgabe/bio28c_auswertung.txt.
  - t = 0: Der Drehball hat Jspin/Q 0,992 bis 0,998 und Windung 1.
  - Ab t = 20 gibt es zwei Toechter mit Windung 0. Jspin/Q liegt dann zwischen -0,13 und +0,09.
- In den Laeufen mit einem Nachbarn ist s bei t = 20 gross (0,13). Dort liegt X0 nicht im Ursprung (x = 2,6 bis 7,5),
  und der Impuls in den Maskengebieten ist nicht null. Mit X0 im Ursprung waere (a) um s groesser; J1 bleibt bei beiden
  Wahlen erfuellt.
- Die Toechter in w60_nachbarn2 tragen in beiden Zerlegungen Gegendrall (Maske -0,17, Zonen -0,31). Die Bahn liegt in
  den Zonen dafuer bei 1,38. Bio 28b fand diese Toechter bei T = 100 bis 300 "nicht rund" (rmax/R_A 1,31 bis 1,42).
  Dass laengliche Toechter ohne Windung Eigendrehimpuls tragen koennen, ist eine Hypothese [H], hier nicht geprueft.

## 4. J0 bis J2

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| J0 | K0 bestanden | 80 % | **eingetroffen** | L/Q = 1 - 7e-16 (m1_w60, m1_w75); ruhender m = 0-Ball L/Q = 3e-17; Erhaltung bis 90 auf <= 8e-14 in 4 von 4 Laeufen |
| J1 | Bei T = 60 tragen die Toechter als Bahndrehimpuls (a) mindestens 50 % des Anfangsdrehimpulses, in mindestens 3 der 4 Laeufe | 55 % | **eingetroffen** | (a)/L0 = 0,625 / 0,839 / 0,623 / 0,525, also 4 von 4. Knappster Lauf w75_nachbarn2 (+0,025); auch ohne ihn bleiben 3 von 4 |
| J2 | Der Eigendrehimpuls (b) der Toechter ist bei T = 60 kleiner als 10 % des Anfangsdrehimpulses | 70 % | **nicht eingetroffen** (Lesart PLAN 4.2: alle vier Laeufe, Betrag) | abs(b)/L0 = 0,036 / 0,166 / 0,019 / 0,044; w60_nachbarn2 liegt 0,066 ueber der Schwelle (b negativ) |

- Die Lesart von J2 habe ich vor dem Lauf festgelegt und als Festlegung der Bearbeitung markiert (PLAN 4.2). Die
  Karte selbst nennt keine Laufzahl.
- **Bedeutung nach Karte:** Fuer "J1 ja, J2 nein" ist keine Bedeutung vorgesehen.
- **Zusatz, kein Kriterium (Zonen):** (a_Z)/L0 bei T = 60 = 0,99 / 1,38 / 0,89 / 0,67; abs(b_Z)/L0 = 0,04 / 0,31 /
  0,06 / 0,09. Die Zonen geben fuer beide Fragen dieselben Ja/Nein-Antworten je Lauf wie die Maske.

## 5. Latten, Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Latten (v3):**
- **L1 (kann scheitern): formal ja, in der Sache nein.**
  - J2 ist in einem Lauf gescheitert.
  - Beide Ausgaenge waren aber aus den Bio-28b-Rohdaten ableitbar (PLAN 1 und 4.6): (a) und (b) bis 1,3e-4, L0 exakt.
  - K0a ist analytisch vorab bekannt (punktweise x P_y - y P_x = m rho).
- **L2 (Gegenprobe): ja.**
  - Drehball m = 1, ruhender Ball und bewegtes Paar mit richtigem Vorzeichen.
  - Summenprobe der Zerlegung (a + b + c + s = L) auf 2e-16.
  - Rechenprobe gegen Bio 28b: dieselben Gebiete (Q auf 4, Lage auf 3 Stellen), (a) und (b) bis 1,3e-4 gleich.
  - Zweite Zerlegung (Zonen) mit denselben Antworten je Lauf.
- **L3 (Numerik): nur teilweise.** Gerechnet wurde nach Karte nur grob. Erhaltung: L 8e-14, Q exakt, E 1e-5. Einen
  Vergleich grob gegen fein gibt es fuer die Drehimpulsanteile nicht.
- **L4 (schon bekannt): weitgehend.** Dass der Drehimpuls eines zerfallenden Drehballs in die Bahn der Bruchstuecke
  geht, ist bekannte Physik [L, nicht nachgelesen]. Mit Erhaltung und Toechtern ohne Windung lag es nahe. Neu, nur im
  Modell: der Gegendrall der Toechter in w60_nachbarn2 (in Bio 28b "nicht rund").
- **L5 (Messbezug): nein.**

**Grenzen:**
- **Maske:** Die Maske laesst die Schwaenze aus. (c) enthaelt deshalb einen grossen Schwanzanteil (bei t = 0 schon
  0,31 bis 0,35), und (a) wird unterschaetzt: Die Maske erfasst nur 56 bis 64 % einer reinen Bahn. Die Zonen trennen
  den Fernanteil, sind aber kein Kriterium. Der Fernanteil ausserhalb 12 ist Abstrahlung oder Kleinteile; das trennt
  hier nichts.
- **X0:** X0 (Ladungsschwerpunkt der Gebiete) und X_k (Schwerpunkt mit Gewicht S, wie Bio 28b) sind verschieden
  definiert. Das Schliessglied s zeigt die Wirkung: bei T = 60 hoechstens 0,055.
- **L0:** L0 enthaelt den Ueberlapp-Anteil (5 bis 19 % ueber Q_m1).
- **Rest:** 2D, ein Feld, Futter statt Bad (R5-Modell). Nur bis T = 90.

**Selbstanzeigen:**
- Vor dem Lauf kannte ich aus dem Bio-28b-ERGEBNIS Zahl, Windung, Lage und Geschwindigkeit der Toechter. Die
  gespeicherten Drehimpulswerte (Jspin_Q, v, E, J_box_start) habe ich vor dem Lauf nicht angesehen, nur gezaehlt.
- Die Konvention stand im Skriptkopf, bevor der Rauchlauf startete. Der Plan wurde waehrend des Rauchlaufs fertig
  geschrieben und danach eingefroren.
- Die Angabe "ab 19:44 CEST" im eingefrorenen Plan (Skript geschrieben) ist geschaetzt. Gemessen sind nur 19:43:53
  (davor) und 19:46:13 (danach).
- Der Rauchlauf zeigte die Wahrheitswerte K0a, K0b und Vorzeichenprobe (alle true), keine Zahlen (PLAN 5.1).
- Nach dem Lauf habe ich die Rechenprobe gegen Bio 28b mit jq gerechnet. Sie war vorab festgelegt (PLAN 4.6), ist kein
  Kriterium und hat nichts geaendert.
- Weder am Skript noch an der Auswertung habe ich nach dem Einfrieren etwas geaendert. Alle Aufrufe liefen mit
  bio28c.py e6461359...
- py_compile hat auf der .69 einen Ordner __pycache__ in meinem Ordner angelegt.
- Die Hintergrundaufrufe meiner Umgebung haben Statusdateien unter /tmp/claude-1000/... angelegt. Projektdateien habe
  ich dort nicht geschrieben.
- Der Hauptlauf wartete etwa 5,6 min auf den Lock von p4000b. Dort und auf p4000a liefen fremde bildung2-Laeufe.

**Laufzeiten** (.69, kleintest.sh, rc 0; UTC):

| Aufruf | Spur | Zeit (UTC) | Dauer | Details | GPU max |
|---|---|---|---|---|---|
| Rauch (T = 6) | p4000b | 17:46:45 bis 17:47:53 | Unit 68 s | Schiessen 63,0 s; 14,63 ms je Schritt | 573 MB |
| grob (Haupt) | p4000b | 17:48:19 bis 17:55:30 | Unit 93 s, davor etwa 5,6 min Lock | Schiessen 62,5 s; Entwicklung 27,0 s (19 Analysen 1,8 s); 14,02 ms je Schritt; Waechter-Prognose 91 s | 573 MB |
| auswerten | cpu | 17:55:41 bis 17:55:43 | Unit 2,7 s | - | - |

**sha256** (lokal und .69 gleich, voll in hilfs/sha256-lokal.txt und hilfs/sha256-69.txt):
- bio28c.py e64613596ef52382ea311dc943503592f58af83d70c4b2437292f88cceb5aff9
- r5_2d_a.py 4b7a00b22e427ab9889056057437fc2199ca0fe6fff0ccf4847c11f62892bc7b (wie R5/R21/Bio 28b)
- PLAN.md.eingefroren-20261002-194815 f7fcb546e5d558444702b9729c86f09494b76da3d8e95f68d28f4f983ab91ff7
- lauf-69/ausgabe:
  - bio28c_roh.json ea89d1665cfb8e4d9bdc13950f4fe3363ef2dce5fa3d2f608ccb4ab59da2db9c
  - bio28c_auswertung.json 809c7de0e9f9b2eb19495445bd00832c801d60e9e506391d72acb623dfb6a815
  - bio28c_auswertung.txt a5d45d37302926e4926ac0ee60416fe9b69363c934db538dca48601d253861c6
- lauf-69/rauch/rauch_roh.json ff0ea86029968de47c57343d756d3cbfefc4654300831267c032eb1c65748885
- Logs: RAUCH 9d277cd8..., HAUPT-grob a5853312..., AUSWERTEN ae2d7e2f...

**Dateien:**
- Kartenordner: KARTE.md, PLAN.md und die eingefrorene Fassung, bio28c.py, ERGEBNIS.md.
- hilfs/: tabelle.jq, tabelle.md, bio28b_probe.jq, bio28b_probe.txt (Rechenprobe), sha256-69.txt,
  sha256-lokal.txt, einfrierzeit.txt.
- lauf-69/: Spiegel von /home/fmh/fmhc-physics-remote/runde22-bio28c/lauf-69 mit ausgabe/, rauch/ und den Logs.

## 6. Einfach gesagt

Der Drehball dreht sich am Anfang und hat deshalb Drehimpuls, eine Groesse, die nie verloren geht. Wir haben
nachgerechnet, wo dieser Drehimpuls landet, wenn der Ball in zwei Toechter zerfaellt. Die Rechnung haelt ihn bis auf
die letzte Kommastelle fest. Der groesste Teil steckt danach darin, dass die zwei Toechter versetzt aneinander
vorbeifliegen, wie zwei Eiskunstlaeufer, die sich loslassen. In einem von vier Laeufen drehen sich die Toechter selbst
ein wenig rueckwaerts. Die Vorhersage "die Toechter drehen sich kaum noch selbst" sollte fuer alle vier Laeufe gelten,
deshalb gilt sie als nicht eingetroffen. Ausserdem haetten wir das alles schon aus den Daten des letzten Versuchs
ausrechnen koennen.

Ende der Bearbeitung: 2026-10-02 20:01:26 CEST (date). Beginn 2026-10-02 19:37:36 CEST.
