# PRISMA-MAXWELL-1: Ergebnis (Rechen-Agent fuer die Leitung claude-primary, Runde 52)

- Karte KARTE.md unveraendert (sha256 435e93ba..., geprueft 18:59:05 CEST). VORAB.md eingefroren 19:11:33 CEST
  (EINGEFROREN-SHA256.txt). Text ab 19:18:37 CEST (date). Die .69 laeuft in UTC (CEST = UTC + 2).
- Synthetische Rechnung an einem gedachten periodischen Netz. **Keine Messdaten, keine Naturbestaetigung.**
- Kennzeichen: [E] hier gerechnet, [M] Schreibtisch, [L] Gedaechtnis-Literatur (nicht nachgelesen), [H] Hypothese,
  [H, nach Sicht] Lesart nach den Laeufen.

## Ergebnis zuerst

| Nr | Erwartung (Karte) | Urteil nach Wortlaut | Kernzahl |
|---|---|---|---|
| PR0 | alle Sterne auf V x Z > 0 | **eingetroffen** (vorab ableitbar) | 8 Sternarten, 504 Werte je Zelle, keiner <= 0; min \*2 = 0,088 (Zeitflaechen), min \*1 = 0,0071, min \*0 = 0,00086 [E] |
| PRk | d1 d0 = 0 (< 1e-12) auf V x Z und Z^4; Nullzahl = Eckenzahl je Zelle | **eingetroffen** (vorab ableitbar) | d1 d0 <= 1,3e-15 (V x Z), 0 (Z^4); 200 von 200 Zufalls-q mit genau 10 (V x Z) bzw. 1 (Z^4) Nullen [E] |
| PR1 | 12^4: kleinster Nicht-Eich-Eigenwert > 0 **und** Lipschitz-Schranke schliesst jede Zelle (bis 24^4 lokal), Kugel mit Vorfaktor > 0 in 26 Richtungen | **nicht eingetroffen: "nicht zertifiziert"** | Eigenwerte: alle > 0 (min 0,185 ausserhalb der Kugel). Schranke: 0 von 10352 Zellen, nach Verfeinerung 0 von 165268 Teilzellen zertifiziert (B(24) = 9,85 gegen lambda_max = 14,4). Kugel: 26 von 26 Vorfaktoren = 0,02900055 > 0 [E] |
| PR1b | beschreibend: Zeltnetz QUANT-2 | -- | kein negativer Nicht-Eich-Eigenwert an 15379 Ecken (min 0,0117; ausserhalb der Kugel 0,088), Vorfaktor 0,01427 bis 0,01450 (0,8 % Richtungsspreizung); Schranke schliesst keine Zelle [E] |

- **Das Scheitern von PR1 liegt an der Schranke, nicht an der Form.**
  - Die Form ist an allen 15378 Ecken q != 0 positiv; an den Punkten des 24er-Gitters ausserhalb der Kugel ist das
    Minimum 0,157.
  - Das Vorzeichen war vorab entschieden (VORAB Abschn. 2) [M]. W > 0 und die verschwindende Kohomologie des
    verdrehten Bloch-Komplexes fuer q != 0 [L] geben Kern Q = Bild d0. Fuer q != 0 gibt es also keine Nicht-Eich-Nullmode.
  - Das gilt fuer **alle** q, nicht nur fuer die Gitterpunkte. Das ist ein Schreibtischargument, kein Gitterzertifikat.
- **Die Schranke der Karte (Operator-Norm-Lipschitz) taugt fuer diese Frage nicht, schon nicht am Hyperkubus [E].**
  - Am Hyperkubus Z^4 bleiben nach 24^4 noch 29432 Teilzellen offen, bei V x Z alle.
  - Fuer V x Z waere ein Gleichgitter N ~ 1300 noetig. Grund: Die Lipschitz-Konstante misst die ganze Matrix
    (lambda_max = 14,4), die Luecke aber ist der kleinste Ast (0,16 bis 0,19 am Kugelrand).

## 1. Aufbau (wie VORAB, Abweichungen in Abschn. 6)

- **Raum:** V mit einer Zelle (10 Ecken, 68 Kanten, 116 Dreiecke, 58 Tetraeder). Gewichte am Hand-Optimum
  (x, y) = (-23/7, -32/7) (a/8)^2. Sterne mit rv.sterne aus REGULAER-V-1, unveraendert.
- **Zeit:** Schritt tau = 0,348006576329167 a (QUANT-2-Wert; die Karte legt tau nicht fest).
- **V x Z:** 78 Kanten, 184 Flaechen je Zelle. Die Sterne sind Produkte: \*2(f x pt) = \*2s tau, \*2(e x I) = \*1s / tau
  usw. (Herleitung in VORAB Abschn. 1).
- **Bloch:** in reduzierten Koordinaten q_i = k . a_i. Q(q) = Summe_Delta C_Delta e^{i q . Delta}, mit 55 Verschiebungen
  Delta. Q aus C stimmt mit D^+ W D direkt auf 3,6e-15 ueberein (R1).
- **Z^4:** Z^3 von Hand mal Z mit tau = 1, gleicher Produkt- und Bloch-Code.
- **Zelt:** gw.Vorlage (QUANT-2), w aus gwp.npz (tau = 0,348; 3 von 484 Gewichten negativ, min -0,0089). Aus den
  omega-Werten nachgerechnet: Abweichung 0.

## 2. PR0 und PRk im Einzelnen [E] (Lauf H1)

| Stern auf V x Z | min | max | Anzahl |
|---|---|---|---|
| \*0 (v x pt) | 8,56e-4 | 0,0180 | 10 |
| \*1 (e x pt) | 0,01065 | 0,0949 | 68 |
| \*1 (v x I) | 0,00707 | 0,149 | 10 |
| \*2 (f x pt) | 0,636 | 1,710 | 116 |
| \*2 (e x I) | 0,0880 | 0,784 | 68 |
| \*3 (t x pt) | 53,5 | 89,1 | 58 |
| \*3 (f x I) | 5,25 | 14,1 | 116 |
| \*4 (t x I) | 441 | 736 | 58 |

- **3D-Kontrollen aus rv:**
  - Alle 3D-Sterne sind positiv; min \*1 = 0,0306, min \*0 = 0,00246.
  - sign(\*2) = sign(g) an allen Flaechen; |g - delta H| = 1e-16.
  - Volumen- und Tensoridentitaet stimmen auf 2e-16.
- **Maxwell-Normierung auf V x Z:** Summe W S S^T = Vol4 I_6 auf 9,6e-16 relativ.

| Netz | d1 d0 max | Nullen (200 q) | Nullen bei q = 0 | Projektion gegen lambda_nV | sigma_min(d0) | min lambda_nV / lambda_max |
|---|---|---|---|---|---|---|
| V x Z, tau = 0,348 | 1,3e-15 | 10 bis 10 | 13 | 2,2e-14 | 0,71 | 0,0064 |
| V x Z, tau = 0,2924 | 1,3e-15 | 10 bis 10 | 13 | 1,9e-14 | 0,71 | 0,0079 |
| V x Z, tau = 1 | 1,3e-15 | 10 bis 10 | 13 | 4,6e-14 | 0,71 | 0,0013 |
| Z^4 | 0 | 1 bis 1 | 4 | 1,2e-14 | 0,71 | 1,0 |
| Zelt (beschreibend, 40 q) | 1,4e-15 | 10 bis 10 | -- | -- | -- | Projektion min 0,012, kein q negativ |

- **Spektrum Z^4:** {0, S, S, S} mit S = 4 Summe sin^2(q_mu / 2), Abweichung 1,8e-14.
- Q(-q) hat dasselbe Spektrum wie Q(q) (Abweichung 0). Damit ist die halbe Zone in q_t gerechtfertigt.
- Bei q = 0 gibt es 13 Nullen, wie in VORAB vorhergesagt (9 Eichnullen und 4 harmonische).

## 3. PR1 im Einzelnen [E] (Lauf H2, Kontrolle H3)

- **Kleinster Nicht-Eich-Eigenwert lambda_nV:**

| Ort | V x Z | Z^4 (H3) |
|---|---|---|
| alle Ecken q != 0 (12^4, halbe Zone) | **0,02376** bei q = (0, 0, -pi/6, 0), also k = (-0,52; -0,52; 0,52; 0) / a, |k| = 0,91 (in der Kugel) | 0,268 |
| Ecken ausserhalb der Kugel | **0,1850** bei q = (-pi/3, pi/6, pi/6, 0), also k = (2,09; -1,05; -1,05; 0) / a, |k| = 2,57 (am Kugelrand) | 1,268 |
| 24er-Punkte ausserhalb der Kugel | 0,1568 | 1,136 |
| Zahl der Ecken q != 0 mit lambda_nV <= 0 | 0 von 15378 | 0 |

- Die Kreuzkontrolle per Projektion auf das Komplement von Bild(d0) stimmt an allen 15378 Ecken auf 2,6e-14 mit
  lambda_nV ueberein. Kein negativer Wert; min sigma(d0) = 0,49 (d0 injektiv).
- Die Eichnullen bleiben unter 8e-15. lambda_max = 14,39.
- **Schranke (Kartenwortlaut, Weyl mit L_i >= sup ||dQ/dq_i||):**

| Groesse | V x Z | Z^4 |
|---|---|---|
| L_i (a) Summe ||C_Delta|| abs(Delta_i) | 32,6 / 31,5 / 28,1 / 18,5 | 10 / 10 / 10 / 10 |
| L_i (b) Gitter-Max ||dQ/dq_i|| + Hesse h/2 | 21,1 / 21,3 / 19,0 / 13,9 (genommen) | 17,2 (a genommen) |
| Gitter-Max ||dQ/dq_i|| allein | 4,0 / 4,5 / 3,5 / 3,2 | 4,6 |
| B(12) = Summe L_i h/2 | **19,70** | 9,21 |
| B(24) | **9,85** | 4,60 |
| Zellen 12^4: in Kugel / zertifiziert / offen | 16 / **0** / 10352 | 8 / 1872 / 8488 |
| Teilzellen 24^4: in Kugel / zertifiziert / offen | 364 / **0** / 165268 | 128 / 106248 / **29432** |
| noetiges Gleichgitter N (beschreibend) | ~1280 | ~87 |

- **Status:** Nach Wortlaut "nicht zertifiziert", fuer V x Z ohne eine einzige zertifizierte Zelle. Ein Gegenbeispiel
  (negativer Eigenwert) gibt es nicht.
- **Kugel |k| < k0 = 2,4 / a** (0,9 % des Zonenvolumens; nimmt die 16 Zellen um q = 0 heraus):
  - Vorfaktor lambda_nV / k^2 bei t = 1e-3 k0: **0,02900055 in allen 26 Richtungen**; Spanne 0,029000546 bis
    0,029000548.
  - Gegen t = 1e-2 k0 gleich auf 1e-5.
  - Reine Zeitrichtung (27.): 0,02900054.
  - Alle 26 + 1 Strahlen sind auf 22 Punkten bis k0 positiv.
  - Die zwei kleinsten Aeste sind entartet (0,0290; 0,0290). Der dritte liegt raeumlich bei 0,0718 und in den
    Raumzeitrichtungen bei 0,0504, rein zeitlich ebenfalls bei 0,0290.
  - Z^4: Vorfaktor 1,0000 (Soll 1).
- **Beschreibend, nicht Kartenwortlaut (Wurzel-Variante, sqrt(lambda) Lipschitz ueber Singulaerwerte von W^{1/2} d1):**
  - L_M = 8,8 / 8,8 / 8,4 / 0,89, B_M(24) = 3,52 gegen sqrt(0,157) = 0,40.
  - Auch so: 0 Zellen zertifiziert; noetig waeren N ~ 200.
  - Am Hyperkubus schliesst diese Variante bei 24^4 alle Teilzellen ausserhalb der Kugel (135680 von 135680).

## 4. PR1b, Zeltnetz QUANT-2 (beschreibend) [E] (Lauf H4)

- Gleiches Gitter 12^4 (halbe Zone), k0 = 2,4, ohne Verfeinerung und ohne Gitter-dQ-Normen (VORAB).
- **Nicht-Eich-Eigenwerte (Projektion, massgeblich, weil W dort das Vorzeichen wechselt):**
  - An allen 15378 Ecken q != 0 sind sie positiv. Minimum 0,01165 bei q = (0, 0, -pi/6, 0), wie bei V x Z.
  - Ausserhalb der Kugel liegt das Minimum bei 0,0884 an k = (-2,09; -1,05; 1,05; 0) / a.
  - lambda_nV und Projektion stimmen auf 2,5e-14 ueberein, es gibt also keinen negativen Eigenwert unter den Eichnullen.
- **Vorfaktoren in der Kugel:**
  - Raumrichtungen 0,014268 bis 0,014384, Zeitrichtung 0,014500. Die Spreizung betraegt 0,8 % gegen 2e-8 bei V x Z
    (bei V x Z Rauschen am numerischen Boden).
  - Alle 27 Strahlen sind positiv.
- **Schranke:** Nur L (a) = 38,7 / 36,6 / 34,2 / 42,9; B(12) = 39,9. Keine Zelle zertifiziert (0 von 10352).
- **Vergleich (gleiche Normierung W wie im jeweiligen Netz; lambda_max 12,1 Zelt gegen 14,4 V x Z):**
  - Die Luecke am Kugelrand ist beim Zelt etwa halb so gross (0,088 gegen 0,185).
  - Ebenso der Vorfaktor: 0,0143 gegen 0,0290.
  - QUANT-2 fand +2,3e-3 (relativ zum groessten Eigenwert je q) an 96 q. Hier ist an 15378 Ecken nichts negativ; das
    kleinste Verhaeltnis zum globalen lambda_max ist 0,0117 / 12,1 = 9,6e-4 [Kopfrechnung, andere Normierung] an der
    kleinsten Ecke in der Kugel.

## 5. Lesarten

- [H, nach Sicht] V x Z ist fuer die Positivitaet der Maxwell-Form das sichere Netz. Das liegt nicht an den Zahlen hier,
  sondern an PR0 plus Kohomologie: Jede positive Gewichtung gibt Q > 0 auf dem Nicht-Eich-Raum fuer alle q != 0. Beim
  Zelt mit 3 negativen Gewichten fehlt dieses Argument. Dort steht nur der Befund an den Gitterpunkten.
- [H, nach Sicht] Der Vorfaktor von V x Z ist in Raum **und** Zeit bis 2e-8 gleich (0,0290055), bei tau = 0,348. Ob das
  an tau haengt, habe ich nicht geprueft (PRk bei tau = 0,29 und 1 misst nur Nullzahl und Luecke). Fuer die
  verallgemeinerte Frequenz (mit Kantenmasse \*1) habe ich nichts gerechnet.
- [M] Um ueber die volle 4D-Zone wirklich zu zertifizieren, braucht man eine Schranke, die nur auf den unteren Ast wirkt.
  Moeglich waeren Kato-Temple oder eine Schur-Komplement-Schranke nach Ausprojizieren der oberen Baender. Oder man
  nimmt das Kohomologie-Argument als Beweis und rechnet nur die Groesse der Luecke beschreibend.

## 6. Regelabweichungen und Selbstanzeigen

1. **Vorschau im Rauchtest:** R3 (scan VZ mit Gitter 6, Verfeinerung auf 12) hat vor dem Einfrieren das 12^4-Eckgitter
   ausgewertet. Bekannt waren: kleinstes lambda_nV ausserhalb der Kugel 0,185, keine Zelle zertifiziert.
   - In VORAB Abschn. 7 offen vermerkt.
   - Die Erwartungen zu PR1 kannten damit das Ergebnis. Sie waren aber auch ohne R3 ableitbar (VORAB Abschn. 2) bzw.
     aus R1/R2 abschaetzbar.
2. **VORAB-Zahl B(12) = 29 war zu hoch:** Sie stammte aus R3 mit h = pi/3, wo der Hesse-Term groesser ist. Im Hauptlauf
   ist B(12) = 19,7 und B(24) = 9,85 (L nach Variante b). Am Urteil aendert das nichts.
3. **tau** fuer V x Z ist meine Wahl (QUANT-2-Wert), in VORAB vermerkt. Gescannt habe ich nur dieses tau.
4. **Halber Gitterabstand** ist komponentenweise h/2 umgesetzt (VORAB Abschn. 3). Das ist die gueltige Lesart; mit
   der euklidischen halben Diagonale waere B nur groesser.
5. **26 Richtungen** in 4D sind meine Festlegung (13 Raumachsen mal 2 Raumzeit-Neigungen), in VORAB vor dem Lauf.
6. **Laeufe:** 3 Rauchtests (R1 5,5 s, R2 0,6 s, R3 30 s) und 4 Hauptlaeufe (H1 8 s, H2 367 s, H3 25 s, H4 250 s),
   Spuren cpu2, cpu3, cpu4, alle rc = 0. Kein Lauf ueber 600 s, keine GPU, kein Lauf nach Sicht.
7. Lokal habe ich kein python, awk oder perl gestartet. Ausgewertet habe ich mit grep, tr und sed auf den JSON-Dateien;
   alle Zahlen stammen aus den Laeufen. Kein /tmp, kein /dev/null. Auf der .69 wurde pm.py einmal per .neu + mv ersetzt
   (vor dem Einfrieren). Fremde Ordner sind unveraendert, nur kopiert.
8. Die Kohomologie-Aussage (verschwindende Kohomologie mit nichttrivialem flachem Linienbuendel auf T^4) ist [L], nicht
   nachgelesen.
9. Die Hodge-Stern-Formel in rv.sterne ist laut REGULAER-V-1 aus dem Gedaechtnis (Glickenstein) [L]. Hier ist sie ueber
   die Identitaeten (Volumen, Tensor, Maxwell-Normierung 9,6e-16) geprueft.

## 7. Grenzen

- **Reflexionspositivitaet ist nicht geprueft.** Positivitaet der quadratischen Form ist nicht Reflexionspositivitaet
  des Masses. Fuer V x Z verweist die Karte auf Osterwalder/Seiler [L]; ob der Satz ungleiche positive raeumliche
  Gewichte abdeckt, bleibt an der Quelle zu pruefen (IDEE-07).
- Nur ein Gewichtspunkt (Kammermitte) und nur ein tau sind gescannt.
- Nur die freie (quadratische) Form ist geprueft, kein kompaktes U(1), kein Monte Carlo (PR2 ist nicht Teil der Karte).
- Das Gitterergebnis ist kein Zertifikat zwischen den Stuetzstellen. Fuer V x Z ersetzt das Schreibtischargument es
  [M/L]; fuer das Zelt gibt es keinen Ersatz.
- Die Euklid-Eigenwerte von Q sind nicht die physikalischen Frequenzen; die verallgemeinerte Aufgabe mit \*1 ist nicht
  gerechnet.

## 8. Dateien (sha256)

| Datei | sha256 |
|---|---|
| KARTE.md | 435e93ba7ebd55d3cada10813feea355b5b1992dcd74db289f24dc654b32f14e |
| VORAB.md (= VORAB.md.eingefroren-20261009-191133) | 9cae178e63ced5244d01790e4ec619b3cd16f7942b1086c8eee91798fb901151 |
| code/pm.py (eingefroren, alle Hauptlaeufe) | f57df3f9adbcc8a892059ad671293dbff4369fed95fb2fc70b8f29209441271f |
| code/KOPIEN-SHA256.txt (Kopien rv, ew, tp, danzer_naeherung, licht_netz, qu2, gw, rk, rk2, pt, gwp.npz) | 904ade421f2ff464283f4daa830a70f01e6ebd48da1cbd71d5bfc32ffd4c7c52 |
| PRUEFSUMMEN-69.txt (alle Lauf- und Rauchdateien, auf der .69 erzeugt; lokal alle OK) | 1ed4da27698ff4dee9281d2468af7ba82c00c825469ab51123fb5a92cec71101 |
| lauf-69/h1.json (PR0, PRk) | 5a7f2c11b4f3267767b8c8578b9897f53126ec3a96fa557281b32af3ba383c63 |
| lauf-69/h2.json (PR1, V x Z) | 403111187c05c90f7e4b3a38f0aeddb157fe65cb7e36c779470cb5efd0cfc046 |
| lauf-69/h3.json (Z^4-Scan) | e60c2e32ec78772bc9a4e53547e92f722e6f82d6f6d74976cc5ee7ea831c52d6 |
| lauf-69/h4.json (PR1b, Zelt) | 43b1c16588e145db26ce68ac555a7956959e747d100728cf484ccfcb40396d6c |

- Auf der .69: .69:fmhc-physics-remote/prisma-maxwell-1/ (code/, daten/, lauf/, rauch/, VORAB.md, PRUEFSUMMEN-69.txt).
- Zeiten: Rauchtests 17:07:34 bis 17:10:06 UTC; Hauptlaeufe 17:11:38 bis 17:17:45 UTC.

## 9. Einfach gesagt

Wir haben geprueft, ob Licht auf Finns Netz stabil ist, wenn man die Zeit in gleichen Schritten wie bei einem Stapel
Prismen dazunimmt. An zehntausenden Pruefpunkten gab es keine einzige "verbotene" Schwingung, und nahe bei null verhaelt
sich das Licht in allen Richtungen gleich. Dass es so kommen muss, folgt schon daraus, dass alle Gewichte positiv sind.
Die strenge Methode aus der Karte, die auch zwischen den Pruefpunkten garantieren sollte, war aber zu grob. Sie scheitert
sogar beim einfachsten Wuerfelgitter. Das Zeltnetz aus QUANT-2 ist ebenfalls an allen Punkten stabil, hat aber eine
etwa halb so grosse Sicherheitsreserve.

---
Abgabe ERGEBNIS.md: siehe naechste Zeile (date).
Abgabe ERGEBNIS.md: 2026-10-09 19:20:11 CEST (date).
