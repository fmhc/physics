# PLAN BILDUNG-LEITER (Runde 22, v3 explorativ)

- Code-Agent im Auftrag der Leitung claude-primary (Finn: "ok mach den naechsten test"). Beginn 2026-10-02 20:22:32 CEST
  (date). Plan geschrieben ab 20:40:31 CEST (date), nach dem Rauchlauf und vor jedem echten Lauf.
- Grundlage: KARTE.md (ab 20:14:48) und DENKNOTIZ.md. Verbindlich und hier unveraendert: Arme M und G, K0, L0 bis L3,
  Bedeutung. Zeitbox 90 min, also bis 21:52:32 CEST.

## 1. Code

- Leitungsfassung code/zeit2d.py (sha256 e0010635041833379cbcdfa72c184187c9d882174d1bd7eadc6af39fea97fce5) bleibt
  unveraendert. Runde-12-Modul code/bic2_2d_praez_v2.py (042ba893129ac3971dc53bf2c42b313f95f35e0f420149b274b7fd6a5be4ef00)
  unveraendert.
- Ganz gelesen. Gerechnet wird mit **code/zeit2d_v2.py** (sha256 dbd1652ecf5f0c139376c9fb3368dfd6a1a5fe912b9dbdb83f8656665b58731e).
  Aenderungen, alle im Code mit "V2" markiert:
  - **V2-1 Start (Fehler):** Der Taylor-Start phi(-dt) = phi - dt vel + dt^2/2 a ist fuer das diskrete Profil nicht die
    exakte Leapfrog-Drehung. Der Startgeschwindigkeit fehlt relativ w2 dt^2/8: 1,7e-5 bei dr 0,04 und 4,2e-6 bei dr 0,02.
    Das regt Zentraldichte-Schwingungen ueber der K0-Schranke an.
    - Neu: Faktor q = sqrt(1 - w2 dt^2/4) vor dem Geschwindigkeitsterm. Damit ist die Loesung exakt f exp(-i w_d t) mit
      w_d = (2/dt) asin(w dt/2). Fuer andere Anfangszustaende aendert sich nur ein Term der Ordnung dt^3.
    - Vorab gerechnet, im Rauchlauf bestaetigt (Abschn. 2).
  - **V2-2 Drehfrequenz (Folgerichtigkeit):** Der lin-Arm nutzt exp(-2 i w_d t) als Hintergrundphase, die Messdrehung
    exp(+i w_d t). Er ist dann exakt die Linearisierung des diskreten nl-Schemas um dessen stationaere Loesung. Mit w
    blieb ein Rest O(w2 dt^2/12), der die Phasenmode bei rho = 0 stoert. Re rho verschiebt sich um w_d - w (dr 0,02:
    1,0e-6; dr 0,04: 4,1e-6).
  - **V2-3 Absturz (Fehler):** Im nl-Arm brach die Analyse bei leeren Fenstern ab (max() auf leerem Tensor). Das traf
    den vorgeschriebenen Rauchlauf T = 20 (Leitungsfassung rc = 1, Abschn. 2). Jetzt keine Rechnung auf leeren Fenstern.
  - **V2-4:** JSON mit nicht endlichen Zahlen als Text (m.jsonfest), damit jq liest.
  - **V2-5, nur Ausgaben:**
    - Laufzeiten
    - "band" je Pencil, also die Bandwahl der Leitung (unten)
    - Pencil K = 24 als Gegenprobe der Projektion
    - Rohsignale in <aus>.roh.pt und Teilaufruf "auswerten"
    - Option "start-taylor", nur fuer den A/B-Rauchlauf
  - **V2-6 Abschnitte:** Option bis=<t> sichert den Zustand, "weiter" setzt bitgleich fort. Das Profil wird neu gerechnet
    und bitgleich gegen das gesicherte geprueft. Grund: Grenze 600 s je Aufruf (kleintest.sh, RuntimeMaxSec).
- **Abweichung der Leitungsfassung vom Kartenwortlaut** (nur benannt, nicht geaendert): Arm M startet nicht mit dem
  Pol-Eigenvektor. Die Startstoerung ist der Gauss-Kick an r_halb (Reihe "kick", Breite 0,5); die stille Mode wird per
  Matrix-Pencil abgetrennt. Linearisiert, also im linearen Bereich fuer jede Amplitude.
- **Box:** Die "R ~ 31" der Auftragszeile sind der Integrationsrand von Runde 12 ("Rand R = 31,76"), nicht der Ball.
  Der Rauchlauf zeigt r_halb = 11,90, R_rms = 8,64, Q_F = 672,6, S0 = 1,028 bei 0,529266. Bis r_sd = 80 bleiben ~68
  Einheiten Abstand. Der Gauss (s = R_rms) hat jenseits r = 80 einen Ladungsanteil von exp(-(80/8,64)^2) ~ 1e-37.

## 2. Rauchlauf (vor diesem Plan; .69, 18:36:00 bis 18:40:09 UTC; alles in lauf-69/rauch/)

| Lauf | Ergebnis |
|---|---|
| Leitungsfassung lin, 0,529266, dr 0,04, T 20 | rc 0, 8,7 s |
| Leitungsfassung nl, dasselbe | **rc 1**: RuntimeError max() auf leerem Fenster (V2-3) |
| v2 nl dr 0,04 / 0,02, Start v2 | K0-Mass S_zentrum_rel_abw_max **1,4e-13 / 5,0e-13** bis T = 20 |
| v2 nl dr 0,04 / 0,02, start-taylor (q = 1) | **2,2e-5 / 5,5e-6**; vorab gerechnet 1,7e-5 / 4,2e-6 (Groessenordnung) |
| Newton (alle) | 30 Schritte, Residuum 4,3e-5 -> 3,7e-13 (dr 0,04) bzw. 1,1e-5 -> 9,7e-13 (dr 0,02), Rundungsboden; Schranke 1e-13 nicht erreichbar, unschaedlich |
| Ladung exakte Reihe | erhalten (672,57683 -> 672,57683) |
| Abschnitte bis=10 + weiter gegen Einmal-Lauf | nl und lin **bitgleich** (K0, Ladung, Summe der S-Reihe) |
| Zeit je Schritt (4 Laeufe parallel) | dr 0,04: 1,32 ms; dr 0,02: 1,81 ms; Profil 6,5 s bzw. 10,5 s |
| Pencil-Probe (synthetisch, hilfs/pencil_probe.py) | gamma 1e-6 / 1,5e-4 / 1e-2 / 3e-3 aus Signalen mit 10 Komponenten plus Drift **getroffen** (rel. < 1e-3), K = 12 und 24; 1,8 s (1751 Punkte) bis 3,7 s (9001 Punkte, erster Aufruf 7,7 s) |

- **Hochrechnung T = 2000:**
  - dr 0,04: Schleife ~165 s, mit Analyse (lin ~28 Pencils, ~90 s) ~260 s, ein Aufruf.
  - dr 0,02: Schleife ~452 s, mit Analyse ~550 s, zu knapp. Deshalb zwei Abschnitte: bis=1000 (~240 s), dann weiter mit
    Analyse (~330 s).
- Zeilen "lin rc = 2" in rauch-v2-lin-04-seg1.log/seg2.log: mein Shell-Fehler (falsches Arbeitsverzeichnis), keine
  Rechnung. Wiederholt als seg1b/seg2b.

## 3. Punkte und Laeufe (gewertet: dr 0,02)

- **Punkte (omega^2):**
  - 0,529266: Sprosse n = 7 (Runde 12, FEIN)
  - 0,52905 und 0,52950: daneben
  - 0,53139: zwischen den Sprossen. Mitte von n = 6 (0,533843, 1/eps 29,548) und n = 7 (1/eps 34,169) in 1/eps:
    31,859, also eps 0,031389. Leiterschritt 4,62.
- **Gitter:** dr 0,02 gewertet; dr 0,04 als Gittervergleich (Latte L3 Numerik).
- **Laufparameter:** T = 2000, r_sd = 80, r_max = 140, dt = 0,4 dr, Messabstand 0,2 (dr 0,04: 0,192).
- **Laeufe:**
  - Je Punkt: lin und nl auf beiden Gittern, zusammen 16 Laeufe.
  - Scan, nur berichtet: lin, dr 0,04, bei 0,52915 / 0,52920 / 0,52925 / 0,52930 / 0,52935 / 0,52940. Mit den drei
    Hauptpunkten bei dr 0,04 gibt das 9 Punkte fuer Lage und Kruemmung des V.
- **Aufrufe:**
  - dr 0,02: "bis=1000", dann "weiter" (mit Analyse).
  - dr 0,04: ein Aufruf.
  - Faellt ein Aufruf trotzdem an 600 s, wird er mit kuerzeren Abschnitten wiederholt (dokumentiert).
- **Spuren:** cpu, cpu2, cpu3, cpu4, je eine Kette, hoechstens 4 zugleich.
  - Je Kette: zuerst dr 0,02 (lin, nl), dann dr 0,04 (lin, nl) eines Punktes, dann Scanpunkte.
  - Zuordnung: cpu 0,529266; cpu2 0,52905; cpu3 0,52950; cpu4 0,53139.
  - Scan: cpu 0,52915 und 0,52935; cpu2 0,52920 und 0,52940; cpu3 0,52925; cpu4 0,52930.
- Rechenort .69: /home/fmh/fmhc-physics-remote/runde22-bildung-leiter/aus/; Kopie nach lauf-69/.

## 4. Auswertung (fest)

- **Abklingrate (L1, L2):** gamma = -Im rho der Komponente "band" im K = 12-Pencil der Projektion der Reihe "kick".
  - "band" ist die Komponente mit |Re rho| in [1,45; 1,65], deren |Re| am naechsten an 1,556 liegt.
  - Fenster [200; 2000] bei 0,52905, 0,529266 und 0,52950; Fenster [50; 400] bei 0,53139.
  - Re rho wird mitberichtet.
  - Kein Band-Treffer an einem Punkt heisst "offen" fuer diesen Punkt.
- **Vergleich Runde 12** (ERGEBNIS.md Abschn. 2c und 2a):
  - 0,52905: \|Im rho\| 1,5e-4, Re ~1,5552 (interpoliert)
  - 0,52950: 1,7e-4 (2a: 1,743e-4), Re 1,55781
  - Sprosse: theoretisch 0; Rechteck 2,6e-7 bei 0,529275; FEIN 8,4e-7 bei 0,52925; rho* 1,556457
- **L1** (dr 0,02):
  - **eingetroffen**, wenn alle drei gelten: gamma(0,52905)/1,5e-4 und gamma(0,52950)/1,7e-4 liegen je in [0,5; 2], und
    \|gamma(0,529266)\| < 1e-5
  - **nicht eingetroffen**, wenn ein gemessener Wert das verletzt
  - sonst **offen**
- **L2** (dr 0,02): gamma(0,53139) >= 3e-3 heisst eingetroffen, < 3e-3 nicht eingetroffen, kein Band-Treffer offen.
- **L3** (Arm G, dr 0,02, Reihe "gauss", Fenster [100; 600], "anteile" im Code; Amplitude^2 ohne |re| <= 0,01):
  - Je Punkt muss gelten: Anteil gebunden (0,01 < |re| < 1 - omega) > 0,5 und Anteil still (|re| in [1,45; 1,65]) < 0,01.
  - Alle vier Punkte erfuellen beides: **eingetroffen**.
  - Ein Punkt verletzt eines davon: **nicht eingetroffen**.
  - Sonst (Anteile None) **offen**.
- **L0 (K0):** S_zentrum_rel_abw_max der Reihe "exakt" < 1e-6 bis T = 2000 an allen vier Punkten mit dr 0,02. dr 0,04
  wird berichtet.
- **Nur berichtet, nicht gewertet:**
  - K = 24-Pencil
  - Pencils von Zentrum und Wand
  - Fenster [400; 1200] und [1200; 2000], also zeitliche Konstanz von gamma
  - dr 0,04 je Punkt (Gittervergleich, Verhaeltnis gamma(0,04)/gamma(0,02))
  - **V-Lage:**
    - dr 0,04: lineare Ausgleichsgerade durch die signierten Wurzeln +-sqrt(gamma) der 9 Punkte, ohne den Punkt mit
      kleinstem gamma; Vorzeichen minus links von diesem Punkt.
    - Daraus Nulldurchgang w*, Steigung (Runde 12: 57) und Kruemmung gamma ~ a^2 (w2 - w*)^2.
    - dr 0,02: Zwei-Punkt-Schaetzung w* = (x1 sqrt g2 + x2 sqrt g1)/(sqrt g1 + sqrt g2) aus 0,52905 und 0,52950.
- **Bedeutung:** wortgleich nach Karte.
- **Nach dem Einfrieren** aendere ich weder Code noch Regeln. Die Auswertung (hilfs/auswertung.py auf der .69 oder jq
  lokal) setzt nur diese Regeln um.
