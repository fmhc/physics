# DIM-LEITER-QBALL-1: Ergebnis (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:48:39 CEST; ERGEBNIS geschrieben ab 19:22:25 CEST
  (date).
- Plan und Code eingefroren 19:16:13 CEST (PLAN.md.eingefroren-20261004-191613, code/dim_leiter.py.eingefroren-...,
  Hashes in EINGEFROREN-SHA256.txt), vor jedem Hauptlauf und vor jeder Sicht auf Q-, E- oder W-Werte. Code danach
  unveraendert; Hash auf der .69 vor und nach den Laeufen gleich.
- Hauptlaeufe: .69, kleintest.sh, cpu11 (ungerade D) und cpu4 (gerade D), 17:16:20 bis 17:19:25 UTC (19:16 bis 19:19
  CEST), alle rc = 0, laengster Lauf 60 s (D = 12). Auswertung und Bilder mit dem eingefrorenen Code, 17:19:33 bis
  17:19:37 UTC.
- Kennzeichen: [E] gerechnet (.69), [M] eigene Mathematik oder Kopfrechnung (nicht gegengelesen), [P] Projektdatei,
  [L] Literatur aus dem Gedaechtnis, [H] Hypothese, [D] beschreibend nach dem Einfrieren (kein Urteil).
- **Radialer Ansatz, kein voller Stabilitaetsnachweis (AGENTS.md):** Kriterium ist VK plus E < m Q. Synthetische
  Rechnung im Modell, keine Messdatenbestaetigung.

## 1. Ergebnis zuerst

1. **Stabile Baelle gibt es in jeder Dimension D = 1 bis 12 [E]**, eine Grenzdimension zeigt die Rechnung nicht. Die
   kleinste Ladung mit E < Q waechst aber steil: Q_s = 141,5 (D = 3), 1705 (D = 4), 2,37e4 (D = 5) bis 2,61e13
   (D = 12). Der Faktor je Dimension steigt von 12,1 auf 23,5, also schneller als exponentiell.
2. **Dicke Wand: Der Exponent 2 - D gilt nur bis D = 3 [E].** D = 1: +1,000; D = 3: -0,995; **D = 4: -1,024 statt
   -2.** Ab D = 5 bleibt Q fuer omega -> 1 fast konstant (p = -0,08 bis +0,014). Das hatte ich vor dem Lauf hergeleitet
   (Plan Abschn. 2, [M]): Die kubische NLS hat ab D = 4 keinen Grundzustand. **DQ0 ist deshalb nicht eingetroffen**;
   alle anderen Kontrollen bestehen.
3. **Einen Wendepunkt (inneres Q-Minimum) gibt es nur fuer D = 3 bis 6 [E]**: omega_c = 0,9629; 0,9819; 0,9932;
   0,9984. Fuer D = 7 bis 12 faellt Q(omega) im ganzen Fenster, alle Baelle sind dort VK-stabil, und die kleinste
   Ladung liegt am Rand omega -> 1. **DQ1 nicht eingetroffen.**
4. **Kein einfaches Exponentialgesetz [E]:** Gegen den Fit ln Q_min = a + b D weicht Q_min bis 118 % ab (Plan). Nach
   Kartenwortlaut (Abweichung in ln) sind es 16,5 %; nur D = 3 liegt ueber 15 %, alle anderen D bei hoechstens 3,4 %.
   **DQ2 nicht eingetroffen.**
5. **W(D) ist bei D = 1 und 2 am groessten (= 1) [E].** Danach folgen 0,726 bei D = 3, und W steigt wieder bis 0,911
   bei D = 12, weil E < Q fast bis omega = 1 reicht (1 - omega_s ~ 0,3/D [M]). **DQ3 nicht eingetroffen.** Das war aus den
   Projektwerten fuer D = 1 und 2 vorab absehbar (Plan Abschn. 2).
6. **Zu Finns Frage:** In diesem Modell gibt es kein Einpendeln bei 3 bis 4 Dimensionen. D = 3 ist die erste Dimension
   mit Wendepunkt und instabilem Ast; D = 2 hat nur die untere Schranke Q > 11,70, ohne instabilen Ast. Mit jeder
   weiteren Dimension braucht ein stabiler Klumpen 12- bis 24-mal mehr
   Ladung [E]. Bis D = 12 gibt es keinen Bruch, der "partiell bis 12" stuetzen wuerde; ueber 12 ist nicht gerechnet.

## 2. Urteile

| Nr | Vorhersage (Karte, unveraendert) | Wahrsch. | nach Plan | nach Kartenwortlaut | Tragende Werte [E] |
|---|---|---|---|---|---|
| DQ0 | Kontrollen: Existenzgrenze 0,7071; Exponent 2 - D in D = 1, 3, 4 auf 10 %; 3D-Werte des Projekts auf 1e-3 | 85 % | **nicht eingetroffen** | **nicht eingetroffen** | Existenz ja: alle 102 Punkte auf beiden Gittern; omega_* = 0,70698 bis 0,70704 (D = 2 bis 12); D = 1 exakt auf 1,9e-6. Exponent nein: D = 4 p = -1,024 (Soll -2 +- 0,2); D = 1 +1,0001 und D = 3 -0,9954 ja. Projektwerte ja: D = 3 Q und E auf <= 9,4e-6, Q_min auf 1,3e-4; D = 2 auf <= 6,2e-7 |
| DQ1 | [H] Wendepunkt fuer D = 3 bis 12, Q_min(D) streng monoton steigend | 70 % | **nicht eingetroffen** | **nicht eingetroffen** | Wendepunkt D = 3 bis 6 ja, D = 7 bis 12 nein (kein Vorzeichenwechsel von dQ/domega bis omega^2 = 0,9999). Q_min(D) mit Randwerten streng steigend |
| DQ2 | [H] ln Q_min linear in D auf 15 % (D = 3 bis 12) | 35 % | **nicht eingetroffen** (max 118 % bei D = 3; 80 % bei D = 12) | **nicht eingetroffen** (max 16,5 % bei D = 3; sonst <= 3,4 %) | Fit: Faktor 16,7 je D. Q_min fuer D = 7 bis 12 sind Randwerte |
| DQ3 | [H] W(D) bei D = 3 oder 4 am groessten | 10 % | **nicht eingetroffen** | **nicht eingetroffen** (W und W2 gleich) | Maximum W = 1 bei D = 1 und 2; W(3) = 0,726, W(4) = 0,770 |

- Plan und Kartenwortlaut geben bei allen vier Vorhersagen denselben Ausgang.
- Vorab absehbar waren DQ0 (D = 4, Schreibtisch [M], Plan Abschn. 2) und DQ3 (Projektwerte [P] fuer D = 1, 2, 3).
  Neu sind die Zahlen ab D = 4, der fehlende Wendepunkt ab D = 7 und der Wiederanstieg von W.

## 3. Tabelle je D (feines Gitter h = 0,0125)

| D | omega_c | Q_min | omega_s (E = Q) | Q_s | W(D) in omega | W2 in omega^2 | p (dicke Wand) |
|---|---|---|---|---|---|---|---|
| 1 | - | -> 0 (Rand: 0,0400 bei omega^2 = 0,9999) | - | - | 1 | 1 | +1,000 |
| 2 | - | -> 11,70 (Rand: 11,7021) | - | - | 1 | 1 | +0,001 |
| 3 | 0,962900 | 111,858 | 0,919757 | 141,497 | 0,7260 | 0,6919 | -0,995 |
| 4 | 0,981880 | 1033,53 | 0,932568 | 1705,24 | 0,7698 | 0,7394 | -1,024 |
| 5 | 0,993212 | 11 747,5 | 0,943571 | 23 652,0 | 0,8073 | 0,7807 | -0,075 |
| 6 | 0,998397 | 158 910 | 0,951651 | 368 455 | 0,8349 | 0,8113 | -0,010 |
| 7 | - | 2,47197e6 (Rand) | 0,957729 | 6,31625e6 | 0,8557 | 0,8345 | +0,004 |
| 8 | - | 4,38525e7 (Rand) | 0,962451 | 1,17392e8 | 0,8718 | 0,8526 | +0,008 |
| 9 | - | 8,55399e8 (Rand) | 0,966224 | 2,33954e9 | 0,8847 | 0,8672 | +0,010 |
| 10 | - | 1,79365e10 (Rand) | 0,969308 | 4,95761e10 | 0,8952 | 0,8791 | +0,012 |
| 11 | - | 3,99362e11 (Rand) | 0,971876 | 1,10962e12 | 0,9040 | 0,8891 | +0,013 |
| 12 | - | 9,36754e12 (Rand) | 0,974048 | 2,60921e13 | 0,9114 | 0,8975 | +0,014 |

- **Rand** heisst: kein inneres Minimum im Fenster; Q_min ist der kleinste Gitterwert bei omega^2 = 0,9999, Q faellt
  bis dorthin. Der Grenzwert omega -> 1 liegt etwas tiefer. Unter der Annahme Q = Q_0 + a eps^2 waeren es etwa p/2,
  also hoechstens 0,7 % [M, Abschaetzung, nicht gerechnet].
- D = 1: Q -> 0 wie 4 omega eps, also keine untere Schranke. D = 2: Q faellt auf 11,70 zu, die Townes-Ladung [L];
  das ist eine untere Schranke, die nicht erreicht wird. In beiden Faellen gibt es keinen instabilen Ast.
- Fehler: grob gegen fein bei Q und E <= 1,2e-4 [E]; bei omega_c <= 7,4e-7, bei omega_s <= 3,5e-7, bei W <= 1,2e-6 [M,
  Kopfrechnung aus auswertung.json].
  Richardson-Werte [D]: Q_min(3) = 111,8597 und Q_s(3) = 141,4986 (code/beschreibung.py, lauf-69/beschreibung.log).
- W(D) enthaelt das Randstueck (omega_min, sqrt(0,53)), also 7,1 % des Fensters, als Annahme (Plan Nachtrag 2).
  Begruendung [M]: duenne Wand, dort dQ/domega < 0 und E/Q -> omega_min < 1.
- **Beschreibend [D], kein Urteil:**
  - Faktor Q_s(D)/Q_s(D-1): 12,05; 13,87; 15,58; 17,14; 18,59; 19,93; 21,19; 22,38; 23,51 (D = 4 bis 12).
  - Faktor Q_min(D)/Q_min(D-1): 9,24 (D = 4) bis 23,46 (D = 12).
  - 1 - omega_s: 0,080 (D = 3) bis 0,026 (D = 12). D (1 - omega_s) steigt von 0,24 auf 0,31 [M, Kopfrechnung].
  - Virial-Identitaet [M]: E/Q = omega + 2G/(D Q) mit G = Int |grad f|^2. Also gilt E < Q genau dann, wenn
    2G/(D Q) < 1 - omega. Am Gitter ist sie bis 6,5e-6 erfuellt [E].
  - Bei omega -> 1 und D >= 5 gilt nach derselben Identitaet E - Q -> (2/D) G > 0 [M]. E/Q bei omega^2 = 0,9999
    liegt bei 1,027 bis 1,040 (D = 5 bis 12) [E]. Der dicke Ast ist dort also nie absolut stabil.

## 4. Bilder

- BILD-Q-omega.png (= lauf-69/dim-leiter-qball-1-Q-omega.png): Q(omega) je D, logarithmisch. Punkt = Q_min bei
  omega_c, Kreuz = E = Q bei omega_s.
- BILD-Qmin-W.png (= lauf-69/dim-leiter-qball-1-Qmin-W.png): links Q_min(D) (gefuellt: inneres Minimum, offen:
  Randwert) und Q_s(D), logarithmisch, mit dem Exponentialfit von DQ2; rechts W(D) in omega und omega^2.

## 5. Kontrollen

| Kontrolle | Ergebnis [E] |
|---|---|
| Schuss-Genauigkeit (DOP853, Bisektion in f(0) bis 1e-12; omega^2 = 0,70 und 0,95, alle D) | f(0) fein gegen Schuss <= 6,0e-6; grob <= 2,4e-5; Verhaeltnis grob/fein ~ 4 (zweite Ordnung); Richardson gegen Schuss <= 1,3e-9 |
| Gitter grob (h = 0,025) gegen fein (0,0125) | Q, E <= 1,2e-4 an allen 102 Punkten und allen D |
| dE/dQ = omega (exakte Ableitung dQ/domega) | <= 1,7e-10 relativ |
| Residuum (relativ), Virial (Derrick), Anteil bei r > 1500 | <= 1,0e-10; <= 7,8e-7; <= 3e-13 |
| D = 1 gegen exakte Quadratur | f(0)^2 <= 1,9e-6 (Schwelle 1e-4); RUNDE-02-Anker Q und E <= 3,1e-6 |
| Existenzgrenze (quadratischer Fit 1/R_half, omega^2 = 0,53 bis 0,55) | omega_* = 0,70698 bis 0,70704 gegen 0,70711 (Schwelle 0,002) |
| D = 3 gegen RUNDE-02 tests1d (6 Stellen) | Q, E bei omega^2 = 0,55, 0,70, 0,80, 0,90 auf <= 9,4e-6; Q_min 111,858 gegen 111,8441 (+1,3e-4), 111,86 beutel-1 (-1,6e-5), 111,87733 FM-4 (-1,7e-4) |
| D = 2 gegen QB-BS-2D und KEGEL-Q | E bei Q = 13, 21, 100 und 50, 100, 200, 400 auf <= 6,2e-7; z. B. E(Q = 100) = 82,139685 gegen 82,139708 |
| Startloesung | Alle konvergierten Startprofile trafen je D dieselbe Loesung (ein f(0)-Wert); D = 10 und 12 per D-Fortsetzung, D = 7, 8, 11 per Schiessstart |
| Exponent | D = 1 und 3 auf 0,5 % am Sollwert; D = 4 bei -1,024 [Plan-Erwartung: nahe -1 mit Logarithmus] |

## 6. Was die Rechnung nicht zeigt

- Nur kugelsymmetrische Baelle und nur VK plus E < Q. Nicht-radiale Stoerungen (in hoeherem D gibt es mehr
  Drehimpulskanaele), Zerfall in mehrere Baelle, Dynamik und Quantenkorrekturen sind nicht geprueft.
- D ist Stellgroesse in einem festen Modell (gleiches U, m = 1 in jeder Dimension). Ueber echte Extradimensionen
  (Kompaktifizierung, Gravitation) sagt das nichts [H].
- Fenster nach oben bis 1 - omega^2 = 1e-4: Ob fuer D >= 7 noch naeher an omega = 1 ein Minimum liegt, ist nicht
  gerechnet. Die lokale Steigung p > 0 spricht dagegen [M].
- W ist ein Mass in der Frequenz und haengt an der Parametrisierung (omega gegen omega^2: bis 0,034 Unterschied). Die
  Ladungsskala sieht es nicht. Dass W ab D = 3 wieder steigt, heisst nicht, dass hohe Dimensionen "robuster" sind:
  Dort braucht jeder stabile Ball astronomisch viel Ladung.

## 7. Selbstanzeigen

1. **Rauchtest 1 vor dem Plan:** Er startete 17:04:47 UTC, also bevor PLAN.md geschrieben war (Plan ab 19:05:11 CEST).
   Offengelegt in Plan Abschn. 10. Gezeigt wurden keine Q- oder E-Werte.
2. **Plan und Code nach den Rauchtests geaendert (Nachtraege 1 und 2, vor dem Einfrieren):**
   - Residuum relativ, zusaetzliche Startwege (Schiessen, D-Fortsetzung).
   - Unteres Gitterende 0,53 statt 0,505, Existenzfit quadratisch statt linear.
   - Die Gitteraenderung war eine Laufzeitentscheidung. Sie verschiebt die Existenzprobe (a2) und macht 7,1 % des
     Fensters in W(D) zur Annahme.
3. **Vorab absehbare Ausgaenge:**
   - DQ0 (D = 4) war nach meiner Herleitung (Plan Abschn. 2) absehbar, DQ3 nach den Projektwerten fuer D = 1 und 2.
   - Die Ableitbarkeitsprobe der Karte nennt Dicke-Wand-Exponent und Wendepunkt fuer D >= 3 ableitbar; fuer D >= 4 ist
     beides nicht gedeckt.
   - Die Karte habe ich wie verlangt nicht geaendert.
4. **Zwei Rauchlaeufe per systemctl --user stop beendet** (rauch3, rauch4; kein pkill). In deren Logs steht dennoch
   rc = 0.
5. **Auf der .69 ausserhalb des Starters:**
   - "pip list" der Physik-venv; das startet python, ohne Rechnung.
   - Dazu mkdir, mv, ls, cat, grep, head, tail, sha256sum, uptime, top, systemctl --user status und stop, setsid und
     nohup.
6. **Lokal:**
   - Benutzt: date, ls, cat, grep, sed, head, tail, cp, mv, rm, mkdir, chmod, diff, sort, sha256sum, ssh, scp, jq
     (nur Anzeige).
   - Kein python, awk oder perl, keine Maschinenrechnung.
   - Ausserhalb der Liste (jq, sed, grep, ssh/scp, sha256sum) lagen ls, cat, head, tail, cp, mv, rm, mkdir, chmod, diff,
     sort (Dateiverwaltung und Vergleich).
   - Kopfrechnungen sind mit [M] gekennzeichnet: die Produkte D (1 - omega_s), die grob/fein-Abstaende von omega_c,
     omega_s, W und Q_min sowie die 0,7-%-Abschaetzung.
7. **Scratchpad und Werkzeugordner der Sitzung:**
   - Zwei Startskripte (start_rauch.sh, start_haupt.sh) lagen kurz im Scratchpad dieser Sitzung
     (/tmp/claude-1000/-home-fmh-fmhc-physics/76c41c65-.../scratchpad/). Laut Gedaechtnis ist das der Scratchpad der
     Leitung. Ich habe sie nach code/ kopiert und dort um 19:16 geloescht.
   - Eine Pruefsummenliste lag Sekunden lang in .../tasks/ und ist geloescht.
   - Die Hintergrund-Ausgaben in .../tasks/ legt das Werkzeug selbst an.
8. **Projekt-grep:**
   - Ausgeschlossen waren vertraege-20260925, ks-1-dk-lauf, ks-1-dk-laeufe sowie Ordner und Dateien mit VERSIEGELT,
     T8-SOLL, ks1, ks-1, KS-1 oder KS1 im Namen.
   - Angezeigt wurden Treffer aus vertraege-20260921 (FM-4 Q_min) und vertraege-20260916 (eine CSV-Zeile); diese
     Ordner sind nicht gesperrt.
9. **Nach dem Einfrieren:** code/beschreibung.py (Wachstumsfaktoren, Richardson, Virial-Probe) ist neu und nicht
   eingefroren. Es liefert nur beschreibende Zahlen [D], kein Urteil.
10. **ssh-Aufrufe:** Mehrere blieben haengen, weil der gestartete Hintergrundprozess die Verbindung hielt; sie liefen als
    Hintergrundaufgaben weiter. Auf die Rechnung hatte das keine Wirkung.

## 8. Laeufe (.69, kleintest.sh, 1 Thread; Zeiten UTC aus den Logs)

| Lauf | Spur | Inhalt | Start bis Ende | rc |
|---|---|---|---|---|
| dlq1rauch | cpu11 | Rauch 1 (D = 1, 4, 12; sechs omega^2) | 17:04:47 bis 17:05:09 | 1 (Start D = 12) |
| dlq1rauch2 | cpu11 | Rauch 2 nach Nachtrag 1 | 17:08:18 bis 17:08:40 | 1 (Start D = 12) |
| dlq1rauch3 | cpu11 | Rauch 3 (D-Fortsetzung, altes Gitter) | 17:09:55 bis 17:14:40 | von mir beendet |
| dlq1rauch4 | cpu4 | D = 12, volles altes Gitter, nur Fortschritt | 17:13:48 bis 17:14:40 | von mir beendet |
| dlq1rauch5 | cpu4 | D = 12, neues Gitter, grob | 17:15:05 bis 17:15:37 | 0 |
| dlq1rauch6 | cpu11 | D = 4 und 7, neues Gitter, grob | 17:15:05 bis 17:15:25 | 0 |
| dlq1d1 bis dlq1d12 | cpu11/cpu4 | Hauptlaeufe je D, eingefrorener Code | 17:16:20 bis 17:19:25 | alle 0 |
| dlq1ausw, dlq1bild | cpu11 | Auswertung, Bilder (eingefroren) | 17:19:33 bis 17:19:37 | 0 |
| dlq1beschr | cpu11 | beschreibung.py [D] | 17:21:03 bis 17:21:04 | 0 |

## 9. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-191613, EINGEFROREN-SHA256.txt.
- code/dim_leiter.py (+ .eingefroren-20261004-191613), code/beschreibung.py (nach dem Einfrieren),
  code/start_rauch.sh, code/start_haupt.sh, code/start_auswertung.sh.
- lauf-69/: d1.json bis d12.json mit Logs, auswertung.json/.log, bild.log, beschreibung.log, die zwei PNG,
  PRUEFSUMMEN.txt (lokal und .69 gleich); lauf-69/rauch/ (Rauchlogs).
- BILD-Q-omega.png, BILD-Qmin-W.png.
- .69: /home/fmh/fmhc-physics-remote/dim-leiter-qball-1/ (code/, rauch/, lauf/).

## 10. Einfach gesagt

Wir haben ausgerechnet, wie ein Klumpen aus unserem Feld (der Q-Ball aus Papier I) aussieht, wenn der Raum nicht drei,
sondern 1 bis 12 Richtungen hat. Stabile Klumpen gibt es in jeder dieser Dimensionen, eine Grenze bei 3, 4 oder 12 gibt
es also nicht. Aber mit jeder zusaetzlichen Richtung braucht ein stabiler Klumpen 12- bis 24-mal mehr Ladung: in drei
Dimensionen etwa 140 Einheiten, in zwoelf etwa 26 Billionen. In einer und zwei Dimensionen ist dagegen jeder Klumpen,
den es gibt, auch stabil (in einer Dimension in jeder Groesse, in zwei ab knapp 12 Einheiten). Ein Einpendeln bei 3 bis
4 Dimensionen zeigt dieses Modell nicht; die Drei ist nur die erste Dimension, in der kleine Klumpen zerfallen koennen.

## Zeitbox

- Start 2026-10-04 18:48:39 CEST; Abgabe 2026-10-04 19:24:37 CEST (date, beim Schreiben dieser Zeile gemessen), also innerhalb der 90 min.
- Danach drei Textkorrekturen (D = 2 hat die untere Schranke 11,70); letzte Aenderung 19:25:15 CEST (date).
