# DREIECK-LINSE-1: Ergebnis (Code-Agent fuer claude-primary, Runde 36, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh, nur Spur p4000a (CUDA, Quadro P4000, float64), jeder Lauf einzeln.
  Die .69-Uhr laeuft in UTC; CEST = UTC + 2.
  - Rauchlaeufe 23:40:42 bis 23:47:09 UTC (01:40:42 bis 01:47:09 CEST), vor dem Einfrieren.
  - Plan-Laeufe:
    - li-K 23:47:33 bis 23:52:02 UTC
    - li-F 23:52:34 bis 23:58:03 UTC
    - li-K-dt 23:58:34 bis 00:07:12 UTC
    - li-K-h 00:07:24 bis 00:15:56 UTC
  - Alle rc = 0, jeder Lauf in einem Abschnitt (laengster 516 s, Grenze 600 s); keine Fortsetzung noetig.
  - Vorlaeufige Auswertung 23:58:15 UTC (nach li-K und li-F, Selbstanzeige 4); endgueltige Auswertung und Bilder
    00:16:05 bis 00:16:08 UTC.
- **Eingefroren** um 01:47:26 CEST, vor der ersten echten Rechnung:
  - PLAN.md.eingefroren-20261004-014726 (sha256 beginnt mit 850bbf082a710f25)
  - code/linse.py.eingefroren-20261004-014726 (sha256 beginnt mit a00ed51a2d0e79ec; auf der .69 dieselbe Datei)
  - code/kegel_q.py unveraendert (sha256 beginnt mit 4de64b080729204c)
  - Pruefsummen in EINGEFROREN-20261004-014726.sha256. Code und Plan wurden danach nicht mehr geaendert.
- **Rohdaten** in lauf-69/:
  - li-K.json, li-F.json, li-K-dt.json, li-K-h.json: Bahnen (Schwerpunkt alle 2 Zeiteinheiten) und Bilanzen je Bahn
  - Logs, auswertung.json (mechanische Urteile), auswertung-vorlaeufig.json
  - Bilder: bahnen.png (Bahnen in der abgerollten Ebene, Kegel und flach), winkel.png (Winkel gegen b, Zusatzablenkung,
    Endschnelle)
  - Rauchlaeufe in rauch-69/. Die Feldzustaende wurden nicht gespeichert.
- Geschrieben ab 02:08:37 CEST (date).
- **Einheiten:** Modell M1 in 2D, Masse 1, c = 1.
  - Q = 200: Ruheenergie 157,288 (Netz h = 0,3), R_half = 6,26, kappa = 0,667.
  - v0 = 0,05, gemessen v_ein = 0,049967; Bewegungsenergie K = 0,197.

## Ergebnis zuerst

1. **Die Fuenfer-Spitze wirkt auf vorbeilaufende Q-Baelle wie eine Punktmasse in der 2+1-Gravitation.**
   - Zwei Baelle starten parallel und laufen links und rechts an der Spitze vorbei. Danach laufen sie unter
     60,0003 / 60,0002 / 60,0001 Grad aufeinander zu (b = 20 / 30 / 40). Die Spannweite ueber b ist 0,0002 Grad.
   - Endschnelle gleich Startschnelle auf 5e-7. Jeder Ball laeuft fuer sich gerade weiter: Zusatzablenkung hoechstens
     0,0004 Grad. Es wirkt keine Kraft; der Knick steckt allein in der Geometrie.
   - D1 und D3 sind eingetroffen.
2. **Bei b = 10 kommt die Mulde der Spitze dazu: 70,88 Grad statt 60 (D2 eingetroffen).**
   - Jede Bahn wird zusaetzlich um 5,44 Grad zur Spitze hin gebogen; der kleinste Abstand ist 9,91 statt 10.
   - Der Ball wird dabei nicht langsamer (v_aus/v_ein - 1 = -9e-7) und nicht angeregt: Atmung und Ballenergie wie auf
     dem flachen Netz.
   - Nachgerechnet [H, nachtraeglich]: Die statische Mulde aus KEGEL-Q gibt in Impulsnaeherung 4,6 Grad bei Abstand 10
     und etwa 5,2 Grad bei Abstand 9,91. Die Ablenkung ist also im Wesentlichen die statische Anziehung der Mulde.
3. **Kontrolle flaches Netz (D0 eingetroffen):** Winkel hoechstens 1,2e-5 Grad, Schnelle konstant auf 1,6e-7.
4. **Konvergenz:** Mit halbem Zeitschritt (alle b) und mit h = 0,2 (b = +-10) bleiben alle Urteile gleich; kein
   Vermerk.
   - Winkel bei b = 10: 70,884 / 70,858 / 70,828 Grad (h = 0,3 und dt = 0,1 / dt = 0,05 / h = 0,2 und dt = 0,05). Die
     Zusatzablenkung je Bahn aendert sich dabei um 0,2 bzw. 0,5 %.
   - Bei b = 20, 30, 40 gleich auf 3e-6 Grad.
5. **Ableitbarkeit:** Die 60 Grad sind die Winkelsumme der Netz-Ecke (5 x 60 Grad), von Hand ins Netz gelegt.
   - Gemessen ist, dass Q-Baelle fern der Spitze den Geodaeten des Netzes folgen. Weil das Netz dort eben ist, war das
     praktisch vorab klar; D0, D1 und D3 waren nahezu ableitbar.
   - Offen war D2 (Mulde bei b = 10).

## Vorab gegen Ausgang

| Nr | Vorhersage (Karte) | Ausgang (mechanisch nach PLAN.md, lauf-69/auswertung.json) |
|---|---|---|
| D0 | Flaches Netz: Winkel +b/-b < 0,5 Grad fuer alle b; Schnelle konstant auf 1 % (85 %) | **eingetroffen**: Winkel -2,7e-8 / 1,4e-7 / 3,3e-7 / 1,2e-5 Grad (b = 10 / 20 / 30 / 40); \|v_aus/v_ein - 1\| <= 1,6e-7 in allen 8 Bahnen |
| D1 | Fuenfer-Spitze, b = 20, 30, 40: 60 +- 2 Grad, Streuung ueber b < 2 Grad (70 %) | **eingetroffen**: 60,00030 / 60,00018 / 60,00011 Grad, Spannweite 0,00019 Grad; Probe dt = 0,05: gleiches Urteil |
| D2 | [H] b = 10: mindestens 3 Grad ueber 60 Grad (50 %) | **eingetroffen**: 70,884 Grad, also 10,88 Grad ueber 60; je Bahn 5,442 Grad zur Spitze; Proben dt = 0,05 und h = 0,2: gleiches Urteil (70,858 bzw. 70,828 Grad) |
| D3 | Endschnelle = Startschnelle auf 2 % fuer b >= 20 (75 %) | **eingetroffen**: \|v_aus/v_ein - 1\| <= 5,1e-7 in allen 6 Bahnen b = +-20, +-30, +-40; Probe dt = 0,05: gleiches Urteil |

- **Winkel** = Richtung des Auslaufs von +b minus Richtung des Auslaufs von -b in der Auslaufkarte (abgerollte Dreiecke,
  Schnitt vor der Spitze; PLAN.md 3.2). Ausgleichsgeraden ueber 15 <= d <= 56, mindestens 294 Punkte je Fenster.
- **Ableitbarkeit:**
  - D0: Auf dem flachen Netz laeuft ein Ball geradeaus; der Rauchlauf zeigte -0,0001 Grad (Selbstanzeige 1).
  - D1: Die 60 Grad folgen aus der Winkelsumme der Spitze, sobald der Ball einer Geodaete folgt. Ausserhalb der Spitze
    ist das Netz exakt eben. Der Ball sieht dort dasselbe Gitter wie auf dem flachen Netz: Energie und Ort stimmen in
    rauch1/rauch2 auf alle gedruckten Stellen ueberein, ebenso die Abstaende fuer b >= 20 in li-K und li-F. Die Mulde
    ist schon bei d = 18 auf 4e-8 abgeklungen (KEGEL-Q, h = 0,3). Der Rauchlauf zeigte 60,0015 Grad.
  - D3: Ohne Spitzennaehe gibt es nichts, was bremst; ableitbar wie D0.
  - D2 war offen. Die Schwelle 3 Grad hing an der Staerke der Mulde bei d ~ 10; die Karte nannte 50 %.

**Bedeutung (nach Karte):**
- **D1 und D3 treffen ein:** "Eine Ecke mit fuenf Dreiecken wirkt auf Q-Baelle wie eine Masse in der
  2+1-Gravitation. Keine Kraft in der Ferne, aber ein fester Knick in den Bahnen, wie ein kosmischer String, der
  Doppelbilder macht." Finns "Masse = Fehlwinkel" bekommt damit eine sichtbare Wirkung: Linsen statt Anziehung.
- **D2 trifft ein:** "In der Naehe kommt die kurzreichweitige Mulde dazu. Das ist der Unterschied zwischen einem endlich
  grossen Q-Ball und einem Punktteilchen." Sie wirkt in dieselbe Richtung wie der Kegel (zur Spitze hin) und faellt
  steil ab: 5,44 Grad je Bahn bei b = 10, unter 0,0004 Grad ab b = 20.
- **Einschraenkungen dieser Lesart:**
  - Der Fehlwinkel ist hier von Hand ins Netz gelegt (Zahl der Dreiecke). In der 2+1-Gravitation erzeugt die Masse
    ihren Fehlwinkel (delta = 8 pi G M). Ob ein Q-Ball sich seine Spitze selbst schafft, ist nicht getestet.
  - Gerechnet sind nur Q = 200, v0 = 0,05, Bahnen parallel zu einer Gitterrichtung und ein Netztyp.
  - [H] Die Linsenwirkung ist die Holonomie des Kegels: Sie haengt nur davon ab, dass die beiden Bahnen die Spitze
    zwischen sich haben, nicht vom Ball.

## Tabellen

**Fuenfer-Spitze (li-K, h = 0,3, dt = 0,1)**

- Winkel: Auslaeufe +b gegen -b (gewertet). Einlaufwinkel: dieselbe Groesse fuer die Einlaeufe; 60 Grad sind dort
  der Schnitt der Karte, die Baelle starten parallel.
- Zusatzablenkung je Bahn: Auslauf- minus Einlaufrichtung, positiv zur Spitze hin. +b und -b sind spiegelgleich auf
  8e-9 Grad.

| b | Winkel [Grad] | Einlaufwinkel [Grad] | Zusatzablenkung je Bahn [Grad] | kleinster Abstand | v_aus/v_ein - 1 | Punkte ein / aus |
|---|---|---|---|---|---|---|
| 10 | **70,8839** | 59,9996 | **+5,4422** | 9,906 | -9,3e-7 | 294 / 440 |
| 20 | **60,0003** | 59,9996 | +0,00035 | 20,0003 | +5,1e-7 | 405 / 523 |
| 30 | **60,0002** | 59,9998 | +0,00020 | 30,0002 | +1,9e-7 | 405 / 473 |
| 40 | **60,0001** | 59,9999 | +0,00012 | 40,0001 | -1,7e-7 | 391 / 392 |

**Flaches Netz (li-F, gleiche Parameter)**

| b | Winkel [Grad] | Zusatzablenkung je Bahn [Grad] | kleinster Abstand zur Mitte | v_aus/v_ein - 1 |
|---|---|---|---|---|
| 10 | -2,7e-8 | 0,0000 | 10,00004 | -4,4e-8 |
| 20 | 1,4e-7 | 0,0000 | 20,00002 | -1,6e-7 |
| 30 | 3,3e-7 | 0,0000 | 30,00001 | -1,1e-7 |
| 40 | 1,2e-5 | 0,0000 | 39,99999 | -4,5e-8 |

**b = 10 im Einzelnen** (li-K gegen li-F, Mittel ueber die Fenster):

| Groesse | Kegel | flach |
|---|---|---|
| Ablenkung je Bahn | 5,442 Grad zur Spitze | 0,0000 Grad |
| Fenster ein / aus | t = 30 bis 616 / 1082 bis 1960 | t = 30 bis 616 / 1066 bis 1942 |
| Geradheit Auslauf (Richtung 1. gegen 2. Fensterhaelfte) | 35,44206 / 35,44189 Grad | - |
| E_ball aus minus ein | -6,4e-6 | -5,7e-6 |
| Q_ball aus minus ein | -4,3e-6 | -3,3e-6 |
| max \|phi\|^2 ein / aus (Atmung) | 1,05002 bis 1,05075 / 1,05008 bis 1,05068 | 1,05002 bis 1,05075 / 1,05008 bis 1,05068 |

- Die Ablenkung ist zwischen den Fenstern abgeschlossen: Die beiden Haelften des Auslauffensters unterscheiden sich um
  0,0002 Grad, die des Einlauffensters um 0,0004 Grad.
- Die Atmung (halbe Spanne von max |phi|^2: 0,035 % im Einlauf, 0,029 % im Auslauf) ist auf beiden Netzen gleich. Der
  Vorbeiflug regt den Ball nicht an.

**Konvergenzproben**

| Groesse | li-K (h = 0,3, dt = 0,1) | li-K-dt (h = 0,3, dt = 0,05) | li-K-h (h = 0,2, dt = 0,05) |
|---|---|---|---|
| Winkel b = 10 [Grad] | **70,8839** | **70,8580** | **70,8275** |
| Zusatzablenkung je Bahn b = 10 [Grad] | 5,4422 | 5,4292 | 5,4140 |
| kleinster Abstand b = 10 | 9,9059 | 9,9060 | 9,9064 |
| v_aus/v_ein - 1 (b = 10) | -9,3e-7 | -9,0e-7 | -8,6e-7 |
| Winkel b = 20 / 30 / 40 [Grad] | 60,00030 / 60,00018 / 60,00011 | 60,00030 / 60,00018 / 60,00011 | nicht gerechnet |
| \|v_aus/v_ein - 1\| bei b >= 20 | <= 5,1e-7 | <= 5,9e-7 | nicht gerechnet |
| v_ein | 0,049967 | 0,049937 | 0,049976 |
| Atmung (halbe Spanne max \|phi\|^2 im Auslauf, b = 10) | 0,029 % | 0,002 % | 0,002 % |
| Urteile | D0 bis D3 eingetroffen | D1, D2, D3 eingetroffen | D2 eingetroffen (D1, D3 nicht gerechnet) |

- Die Zusatzablenkung bei b = 10 faellt mit dt und h leicht und gleichsinnig (-0,013 bzw. -0,015 Grad je Bahn). Der
  Ueberschuss bei D2 (10,8 Grad gegen die Schwelle 3 Grad) ist mehr als hundertmal groesser als diese Aenderung.
- v_ein haengt am Start (Boost ohne Lorentz-Kontraktion) und am Zeitschritt um bis zu 8e-4 relativ; bei dt = 0,05 ist
  K damit 0,12 % kleiner. Nicht weiter untersucht.
- Die Atmung bei dt = 0,1 ist die Startabweichung durch den Zeitschritt (wie EINFANG-1); bei dt = 0,05 ist sie mehr als
  zehnmal kleiner.

## Kontrollen

- **Netz:** 242 701 Ecken (n = 5) bzw. 291 241 (n = 6) bei h = 0,3; 546 001 bei h = 0,2.
  - Grad der Spitze 5, Defekt pi/3 auf 1e-15, Euler 1.
  - Kartenpruefung: Alle Kanten haben in beiden Entwicklungskarten die Laenge h (auf 1,5e-13), ausser 653 bzw. 565
    Kanten am Schnitt. Diese haben nach dem Kleben mit der Winkelsumme der Spitze (5 pi/3 auf 9e-16) wieder die Laenge h
    (auf 1,3e-13).
- **Schnittprobe:** Die Einlaufkarte (Schnitt hinter der Spitze) mit eigener Abwicklung je Bahn und Kleben ueber den
  Gegenstrahl gibt denselben Winkel auf 2e-13 Grad. Das ist eine Probe der Buchhaltung, keine unabhaengige Messung.
  Beim flachen Netz ist das Kleben die Identitaet (Abweichung 9e-14 Grad).
- **Spiegelprobe:** Zusatzablenkung +b gegen -b gleich auf 8e-9 Grad, Schnellen auf 1e-12. Die 8 Felder eines Laufs
  rechnen also unabhaengig und spiegelrichtig.
- **Schwellen-Schwerpunkt** (harte Schwelle |phi|^2 > 0,01 wie EINFANG-1) statt glattem Fenster: Winkel gleich auf
  1,8e-4 Grad (Kegel) bzw. 1,5e-4 Grad (flach).
- **Geradheit:** senkrechte Abweichung von den Ausgleichsgeraden 2e-5 bis 6e-5 (rms); Richtungen der Fensterhaelften
  gleich auf 4e-4 Grad.
- **Energie- und Ladungsbilanz** (E_tot + E_damp, je Bahn):
  - Bis t = 1650 (deckt alle Fenster) auf 1,27e-4 in allen Bahnen (nachtraeglich mit jq, Selbstanzeige 6).
  - Ueber den ganzen Lauf bis 0,032 bei b = 40: Am Laufende (t > 1700) laufen die Baelle b = 30 und 40 in den Schwamm
    und werden dort aufgezehrt (b = 40: E_damp = 43,9 bei t = 2000).
  - Ladung auf 2,3e-12 (Rundung).
  - Im Bild bahnen.png knicken die Bahnen b = +-40 (Kegel und flach) am Ende ab. Dort laeuft der Ball in den Schwamm,
    nach dem Auslauffenster; die dicken Fensterstuecke enden vorher.
- **Start:** Laborladung 200,000000; K_eff = 0,19671 gegen Nennwert 0,19698 (-0,14 %, fehlende Lorentz-Kontraktion wie
  EINFANG-1). v_ein/0,05 - 1 = -6,6e-4 in allen Bahnen.
- **Statische Baelle:** Nebenbedingungen auf 2e-11, Restgradient <= 3,7e-7.

## Latten (v3)

- **L1: teilweise.** D2 konnte scheitern (50 %) und ist eingetroffen. D0, D1 und D3 waren nahezu ableitbar (siehe
  Ableitbarkeit); der Rauchlauf zeigte ihre Tendenz.
- **L2: ja.** Flaches Netz als Gegenprobe, Spiegelprobe, Schnittprobe, zweites Schwerpunktmass, Kartenpruefung,
  Konvergenzproben dt und h.
- **L3: ja.** Zeitschritt halbiert und Gitter verfeinert: Zusatzablenkung bei b = 10 5,442 / 5,429 / 5,414 Grad je
  Bahn (0,5 %), Winkel bei b >= 20 gleich auf 3e-6 Grad. Energie in den Fenstern auf 1,3e-4 (dt = 0,1) bzw. 8,5e-6
  (dt = 0,05), Ladung auf Rundung.
- **L4: ja, fuer den Kern.**
  - Geodaeten auf dem Kegel und das Doppelbild hinter einer konischen Spitze sind elementar.
  - [L, aus der Karte, nicht nachgelesen] 2+1-Gravitation: Punktmassen sind Kegel mit delta = 8 pi G M
    (Deser/Jackiw/'t Hooft 1984). Kosmische Strings machen Doppelbilder unter delta (Vilenkin 1981).
  - Neu ist hier nur, dass ein ausgedehntes Feld-Soliton auf einem triangulierten Kegel diese Geodaeten bis auf
    4e-4 Grad einhaelt, und die Groesse der Zusatzablenkung durch die Mulde. Ob das fuer Q-Baelle auf Kegeln bekannt
    ist, wurde nicht gesucht.
- **L5: nein.** Moegliche Analogien [H]: Linsenwirkung von Disklinationen (Fuenfer-Ringe in Graphen-Kegeln) auf
  Elektronen- oder Phononenwellen; Suche nach Doppelbildern kosmischer Strings. Kein Messbezug in diesem Test.

## Selbstanzeigen

1. **Rauchlaeufe vor dem Einfrieren** zeigten die Tendenzen von D0 und D1 (rauch1: 60,0015 Grad bei b = 16, Q = 150,
   v = 0,1; rauch2 flach: -0,0001 Grad). Offengelegt im Plan, Abschnitt 7. Schwellen sind die der Karte, unveraendert.
2. **Code zwischen Rauchlauf und Einfrieren geaendert:** Option --b-liste fuer die Auswertung der Rauchdaten, robuster
   Zugriff in den Urteilsfunktionen, Markierungen im Bild. Regeln, Fenster und Schwellen standen schon in der ersten
   Fassung vor rauch1.
3. **Abweichung vom Hinweis der Leitung zur Schnittwahl** (Plan 3.2, als [Festlegung] vor dem Einfrieren):
   - Gemessen in der Auslaufkarte (Schnitt vor der Spitze) statt mit dem Schnitt hinter der Spitze.
   - Grund: Mit dem Schnitt hinter der Spitze umrundet jeder schnittfreie Verbindungsweg der Auslaeufe die Spitze. Er
     gaebe 0 bzw. 120 Grad statt delta.
   - Die Schnittprobe zeigt, dass beide Karten denselben Winkel geben, wenn man ueber den Gegenstrahl klebt.
4. **Vorlaeufige Auswertung** um 23:58:15 UTC nach li-K und li-F, vor den Konvergenzproben. Danach wurde nichts an
   Plan, Code oder Laufliste geaendert; die endgueltige Auswertung lief mit demselben Code ueber alle Laeufe
   (lauf-69/auswertung-vorlaeufig.json bleibt zum Vergleich).
5. **Restablenkung bei b >= 20** von 1,2e-4 bis 3,5e-4 Grad je Bahn, auf dem flachen Netz nicht vorhanden. Sie faellt
   langsam (etwa wie b^-1,5), nicht wie die Mulde (exponentiell).
   - [H, nicht geprueft] Erklaerung: Der bewegte Ball ist leicht abgeplattet. Sein Quadrupol trifft die Kruemmung von
     w = z^s (s = 1,2) im harmonischen Schwerpunkt, beim flachen Netz ist s = 1 und der Effekt null.
   - Dazu passt, dass der kleinste Abstand um etwa 0,0054/b zu gross gemessen wird (2,7e-4 / 1,8e-4 / 1,2e-4).
   - Fuer die Urteile ist das 4 Groessenordnungen unter den Schwellen.
6. **Nachtraeglich mit jq gerechnet** (nicht im Plan): Energiebilanz bis t = 1650; die Nachrechnung der Ablenkung bei
   b = 10 aus dem statischen Potential (KEGEL-Q, Impulsnaeherung mit V ~ exp(-1,42 d) zwischen d = 9,6 und 13,2; von
   Hand). Beide gehen in kein Urteil ein.
7. **Mehrere Baelle in einem Lauf:** Die 8 Bahnen eines Laufs sind 8 getrennte Felder auf demselben Netz (Stapel auf
   der GPU). Sie koennen sich nicht beeinflussen; die Spiegelprobe und die gleichen Zahlen fuer b >= 20 auf Kegel und
   flachem Netz bestaetigen das.
8. **Uhrzeiten** der Laeufe stammen aus den Logs der .69 (UTC); CEST ist umgerechnet.

## Einfach gesagt

Wir haben Q-Baelle, kleine Feldtropfen, ueber ein Netz aus gleichseitigen Dreiecken rollen lassen, in dem an einer Ecke
nur fuenf statt sechs Dreiecke zusammenstossen; dort ist das Netz zu einer flachen Tuete gefaltet. Zwei Baelle, die
parallel links und rechts an dieser Ecke vorbeirollen, laufen danach genau unter 60 Grad aufeinander zu, egal wie weit
sie an der Ecke vorbeigehen, obwohl jeder fuer sich schnurgerade weiterrollt und keine Kraft spuert. So lenkt in einer
Welt mit nur zwei Raumrichtungen eine Masse Licht ab: Eine Ecke mit fuenf Dreiecken wirkt also wie eine Masse, nur ohne
Anziehung aus der Ferne. Wer sehr nah an der Ecke vorbeirollt (Abstand 10), spuert zusaetzlich die Mulde an der Spitze
und wird um gut 5 Grad mehr zur Ecke hingezogen, ohne langsamer zu werden; wie gross der Knick ist, bestimmt aber die
Zahl der Dreiecke, nicht der Ball.
