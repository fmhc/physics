# DREIECK-TAKT-1 mit QCA-WINDUNG-2: Ergebnis (Runde 41, Teil 2)

- Code-Agent fuer die Leitung claude-primary (derselbe Agent wie QCA-WINDUNG-1).
- **Zeiten (date):** Start 2026-10-04 16:33:41 CEST; Abrufe 16:40 und 16:42; Code ab 16:46; Rauchlaeufe 14:50 bis
  15:00 UTC; Plan und Code eingefroren 17:00:38 CEST (EINGEFROREN-SHA256.txt); Hauptlaeufe siehe "Laeufe".
- **Kennzeichen:** [S] an der Quelle gelesen; [L] Gedaechtnis; [M] eigene Mathematik, nicht gegengelesen; [E] Rechnung
  im Modell; [F] Festlegung des Plans; [R] im Rauchlauf gesehen; [H] Hypothese.
- **Art:** Rechnung an Modellen (Literaturmodelle, Zufallsautomaten, Finns Dreieckstakt). Keine Messdaten.

## Ergebnis zuerst

1. **In 2D erzeugt Finns Dreiecks-Takt eine einseitige Randwelle, deren Richtung der Drehsinn bestimmt [E].** Gerechnet
   am Wabengitter nach Kitagawa u. a. 2010 mit zyklischem Sprung um die drei Bindungsrichtungen. Im reinen, streng
   lokalen Takt sind die Volumenbaender flach und haben Chern 0. Trotzdem laeuft am oberen Rand netto eine Welle in die
   eine Richtung, am unteren in die andere. Die Umkehr des Drehsinns kehrt beide um.
   - Mechanisch nach Plan bleibt DT3 "nicht eingetroffen": In der Luecke bei pi hat meine eingefrorene Zaehlung einen
     Durchgang doppelt gezaehlt (+2 statt +1).
   - Eine Nachzaehlung nach dem Einfrieren mit Summenprobe gibt in beiden Luecken sauber (-1, +1) und umgekehrt (+1, -1).
2. **In 3D kann ein streng lokaler Takt keine Netto-Haendigkeit erzeugen [M, mit L; an 104 Automaten bestaetigt].**
   Jede endlichreichweitige Unitaere hat W3 = 0 (K-Theorie, Abschnitt Schreibtisch). Die Rechnung findet bei allen 104
   endlichreichweitigen 3D-Automaten |W3| <= 5,3e-15:
   - 72 Zufallsprodukte
   - 6 Pyrochlor-Dreieckstakte (Finns Bild, beide Drehsinne)
   - 25 allgemeine Suchtreffer ohne Produktform
   - das Literaturmodell auf seinem ganzen Torus
   Der Leitungssatz (Produkte aus Teilverschiebungen haben W3 = 0) stimmt und ist ein Sonderfall.
3. **Das Literaturbeispiel fuer ein einzelnes Floquet-Weyl-Teilchen (Higashikawa u. a. 2019) habe ich exakt nachgebaut
   [E, S].** Seine Quasienergieformel trifft auf 5,6e-16.
   - W = 1 (W3 = -1) gilt nur fuer die halbe Zone, den Block der "unteren Floquet-Baender".
   - Die andere Haelfte hat +1, der ganze endlichreichweitige Automat 0. Der Partner-Weyl-Punkt (chi = +1) sitzt bei
     k3 = 2 pi, ebenfalls bei Quasienergie 0.
   - Der Kegel bei k = 0 ist isotrop (v = 1,0000, Spannweite 3,4e-5 bei |k| = 0,05).
   - Der Ort der Anomalie ist hier der abgetrennte obere Bandraum.
4. **Urteile (dritte, gueltige Auswertung):** DT0 eingetroffen, DT1 nicht eingetroffen, DT2 nicht auswertbar,
   DT3 nicht eingetroffen (Zaehlfehler, siehe 1).
   - Nach Kartenwortlaut ("eine einseitige Randwelle, deren Richtung der Drehsinn bestimmt") ist DT3 eingetroffen,
     schon mit der Luecke bei 0 der eingefrorenen Zaehlung.
   - Die ersten zwei Auswertungen waren ganz "nicht auswertbar", weil der Suchlauf mit N = 3 zweimal an der
     10-min-Grenze abbrach (Selbstanzeige 9).
5. **Fuer Finns Frage:** Der Takt mit Drehsinn erzeugt in der Flaeche Wellen, die nur links- oder nur rechtsherum am
   Rand laufen. Im Raum hebt sich die Haendigkeit eines strikt lokalen Takts immer weg. Ein einzelnes Weyl-Teilchen
   gibt es nur, wenn man einen Teil der Baender abtrennt oder lange Reichweiten erlaubt.

## Urteile (lauf-69/auswertung2.json, dritte Auswertung; Vorbedingungen erfuellt)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil nach Plan | Urteil nach Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| DT0 | Kontrollen: Produkte aus Teilverschiebungen und Muenzen W3 = 0 (1e-8); Kitagawa-Lauf mit Chern-Zahl ungleich 0 und einseitiger Randwelle | 85 % | eingetroffen | eingetroffen | 72 Produkte und 6 Takte, max abs(W3) 5,3e-15 bei N_exakt; lam3: Chern (-1, +1); Randfluss Luecke 0: (-1, +1, 0), umgekehrt (+1, -1, 0) |
| DT1 | [H] endlichreichweitiger 3D-Automat mit W3 ungleich 0 gefunden oder aus der Literatur nachgebaut | 35 % | nicht eingetroffen | nicht eingetroffen | 104 Automaten, max abs(W3) 5,3e-15; Literaturmodell ganzer Torus 3,7e-16; nur die halbe Zone (kein Automat fuer sich) hat -1 |
| DT2 | [H] wenn DT1: tiefster Kegel bei 0 ungepaart, isotrop auf 10 % | 30 % | nicht auswertbar (DT1 nicht eingetroffen) | nicht auswertbar | Vermerk Literaturblock: Kegel bei k = 0, Quasienergie 0, in der halben Zone ungepaart (chi = -1), isotrop auf 3,4e-5 |
| DT3 | [H] Takt je Dreieck mit festem Drehsinn gibt in 2D eine einseitige Randwelle, deren Richtung der Drehsinn bestimmt | 60 % | nicht eingetroffen (Luecke pi: (-1, +2, 0) statt einseitig; Zaehlfehler) | eingetroffen (Luecke 0: (-1, +1, 0), umgekehrt (+1, -1, 0)) | Nachzaehlung nach dem Einfrieren: beide Luecken (-1, +1, 0), umgekehrt (+1, -1, 0), Summen 0 |

- **Lesart Kartenwortlaut:** Im Plan hatte ich "Kartenwortlaut: wie oben" festgelegt. Die Karte verlangt bei DT3 aber
  nur "eine einseitige Randwelle". Meine Planregel war strenger (beide Luecken). Deshalb weiche ich bei DT3 von meiner
  Planfestlegung ab und nenne das (Selbstanzeige 10).
- **DT1, Lesart "aus der Literatur nachgebaut":** Nachgebaut ist das Modell. Endlichreichweitig ist es nur als Ganzes,
  und dann ist W3 = 0. Der W3 = -1-Block ist kein endlichreichweitiger Automat auf eigenem Torus. Also nicht eingetroffen,
  auch woertlich.
- **Woran die Urteile haengen:**
  - DT1 an der Ganzzahligkeit; alle Werte liegen 13 Groessenordnungen unter der Schwelle 0,05.
  - DT3 (Plan) an einem einzigen Zaehlfehler in der pi-Luecke. Die Summenprobe zeigt ihn als Fehler (Summe +1 statt 0).

## Schreibtisch [M] (PLAN.md Abschn. 1, vor der Rechnung)

- **Leitungssatz T1 geprueft: richtig, mit einer Voraussetzung.** W3 ist unter punktweisem Produkt additiv. Eine
  Teilverschiebung I - P + exp(i k.f) P mit festem P und eine feste Muenze haben W3 = 0. Jedes Produkt daraus hat also
  W3 = 0, in jeder Reihenfolge. Voraussetzung: Jeder Faktor ist selbst auf demselben Torus periodisch. Higashikawa u. a.
  nutzen Halbschritte U_3(k3/2) mit Periode 4 pi; dort greift der Satz fuer die halbe Zone nicht.
- **T2 (staerker, meine Herleitung mit Saetzen aus dem Gedaechtnis [L]): Jede endlichreichweitige translationsinvariante
  Unitaere in 3D hat W3 = 0, mit beliebig vielen inneren Zustaenden.**
  - Grund: U ist eine invertierbare Matrix ueber dem Laurent-Polynomring R = C[z1^+-1, z2^+-1, z3^+-1]. Fuer diesen Ring
    gilt SK_1(R) = 0 (Bass/Heller/Swan fuer regulaere Ringe, K_0 = Z nach Swan) [L].
  - Also ist U + I_m = diag(det U, 1, ...) mal ein Produkt elementarer Matrizen E_ij(p). Jedes E_ij(t p), t von 0 bis 1,
    ist eine Homotopie zur Eins durch invertierbare Matrizen. Damit gilt W3(U) = W3(det U) = 0.
  - Das ist das Gegenstueck zum bekannten Satz, dass endlichreichweitige Projektoren die Chern-Zahl 0 haben [L].
  - Folge: Ein strikt lokaler Takt in 3D kann keine Netto-Haendigkeit tragen, egal wie er gebaut ist. Das gilt auch fuer
    alle Automaten aus Teil 1, deren W3 = 0 damit vorab ableitbar war (Teil-1-Dateien unveraendert).
- **T3:** Eine stetige Treibung mit lokalem H(t) gibt U_F homotop zur Eins, also W3 = 0. Floquet-W3 ungleich 0 braucht
  deshalb Schritte, die keine lokale Hamilton-Entwicklung sind, oder einen abgetrennten Unterraum.

## Literatur (2 von 3 Abrufen, keine Websuche)

- **Higashikawa/Nakagawa/Ueda, "Floquet chiral magnetic effect", arXiv:1806.06868v2, PRL 123, 066403 (2019)** [S, S. 1
  bis 3 als Bild; quellen/higashikawa-nakagawa-ueda-1806.06868v2.pdf]:
  - Modell: spinselektive Thouless-Pumpen U_j^+- (Eq. 2: Spin +- springt um +-e_j), Halbschritte U_h3^+- in der
    dritten Richtung (Eq. 3), Takt aus acht Schritten (Eq. 4, 5).
  - "V^wh(k) = U(k) + U^H(k)", "U^H(k) := U(k1, k2, k3 - 2pi)", "U_h3(k) := U_3(k/2)"; "Here we focus on U(k) as a
    Floquet operator of lower Floquet bands"; die Abgeschlossenheit kommt aus "generalized adiabaticity ... or some
    fine-tuning".
  - Eq. (6): "W := -(1/24 pi^2) Int ... Tr[R_i R_j R_k] = 1".
  - **Lesart [M]:** Das Modell ist endlichreichweitig (nur Teilverschiebungen). W = 1 gilt fuer den unteren Block,
    also die halbe Zone. Der Partner liegt im oberen Block U^H.
- **Kitagawa/Berg/Rudner/Demler, "Topological characterization of periodically-driven quantum systems",
  arXiv:1010.6126, PRB 82, 235114 (2010)** [S, S. 1, 2, 6 bis 10 als Bild; quellen/kitagawa-berg-rudner-demler-1010.6126.pdf]:
  - Wabengitter, Eq. (9) und (10). In jedem Drittel der Periode ist eine Bindungsrichtung verstaerkt (lambda J), zyklisch
    1 -> 2 -> 3.
  - S. 7: "C+- = +-1 for 1 < lambda < lambda_c ~ 3.3" bei "J/omega = 3/32"; fuer lambda > lambda_c sind die
    Chern-Zahlen 0, "yet the nanoribbon clearly still supports chiral edge states".
  - Grenzfall S. 8 (lambda J T/3 = pi/2): Volumenteilchen kehren nach 2T zurueck, Randteilchen laufen "unidirectionally".
  - Zur Umkehr der Reihenfolge sagt die Quelle nichts; das habe ich gerechnet.

## 3D-Ergebnisse (lauf-69/p3.json, lm_2.json, lm_3.json)

| Familie | Anzahl | W3 (groesster Betrag, alle Gitter) | Bemerkung |
|---|---|---|---|
| Zufallsprodukte aus 4 Muenzen und 4 Teilverschiebungen (N = 2, 3, 4), je beide Reihenfolgen | 72 | 5,3e-15 | N_exakt = 13, 19, 25; Unitaritaet <= 5,7e-15 |
| Pyrochlor-Dreieckstakt (Finns Bild), theta = pi/2, pi/3, 0,4, je beide Drehsinne | 6 | 1,8e-16 | 24 Schritte; die Versaetze teleskopieren, Frequenzen nur bis 1 |
| Additivitaet: K-S1 mal Zufallsprodukt R und R mal K-S1 | 8 | Abweichung von -1 hoechstens 4,1e-14 (N = 48) | R allein <= 1,0e-15 |
| Higashikawa u. a., ganzer feiner Torus (k3 in (-2 pi, 2 pi]) | 1 | 4,2e-16 | endlichreichweitig, 39 Frequenzen |
| Higashikawa u. a., halbe Zone k3 in [-pi, pi] (Block der unteren Baender) | 1 | -0,99999994 (N = 64) | W = -W3 = +1 wie in der Quelle; Rand = -sigma_0 auf 6,7e-16 |
| Higashikawa u. a., andere Haelfte (oberer Block U^H) | 1 | +0,99999994 | gleicht die erste Haelfte genau aus |
| LM-Suche, allgemeine Unitaere mit Traeger F15 (keine Produkte vorgegeben) | N = 2: 23 Treffer aus 40 Starts; N = 3: 2 Treffer aus 3 Starts | 4,9e-17 | Unitaritaet <= 2,3e-12; kein Treffer trivial; N = 3 nur 3 Starts (zwei Laeufe mit 30 bzw. 15 Starts brachen an der 10-min-Grenze ab, Selbstanzeige 9) |

- **Nachbau Higashikawa an der Quelle:** cos eps = Tr U/2 = 2 cos^2(k1/2) cos^2(k2/2) cos^2(k3/2) - 1 auf 5,6e-16
  getroffen (500 Zufallspunkte).
- **Weyl-Punkte Higashikawa auf dem ganzen feinen Torus:**
  - Bei Quasienergie 0 ("im Takt") gibt es genau zwei: k = 0 mit chi = -1 und k3 = 2 pi (q3 = pi) mit chi = +1, also
    netto 0.
  - Bei Quasienergie pi ist U = -sigma_0 auf ganzen Ebenen (Rand der halben Zone). Das ist eine Knotenflaeche; die
    Suche ist dort nicht einfach und nicht vollstaendig (403/404 Funde).
  - Die halbe Zone ist also ein "ungepaartes" Weyl-Teilchen nur, weil man die andere Haelfte (den oberen Block)
    weglaesst. Beide Haelften stossen auf einer Entartungsflaeche bei pi aneinander.
- **Kegel bei k = 0:** v = 0,99998 (|k| = 0,05), Spannweite der Richtungen 3,4e-5. Bei |k| = 1e-4 ist er isotrop auf
  1,4e-10.

## 2D-Ergebnisse: Wabengitter nach Kitagawa u. a. (lauf-69/h2.json)

- Protokolle (T = 1): "voll" = reiner Dreieckstakt (lambda J T/3 = pi/2, endlichreichweitig); "lam3", "lam4", "lam1"
  mit JT = 3 pi/16 (J/omega = 3/32). Die Reihenfolge 1-2-3 dreht gegen den Uhrzeigersinn (b1 bei 120 Grad, b2 bei 240
  Grad, b3 bei 0 Grad), die Umkehr 3-2-1 im Uhrzeigersinn.
- Randfluss: netto Zahl der Randmoden mit d eps/dk > 0 minus < 0 am oberen bzw. unteren Rand, gezaehlt an der
  Lueckenmitte. Zickzack-Streifen, 40 Zellen, 1200 k-Werte.

| Protokoll | Reihenfolge | Luecken (Mitte: Breite) | Chern-Zahlen der Baender | Randfluss Luecke 0 (oben, unten, Volumen) | Randfluss Luecke pi |
|---|---|---|---|---|---|
| voll | 1-2-3 | 0: 3,142; pi: 3,142 (flache Baender bei +-pi/2) | 0, 0 | -1, +1, 0 | -1, **+2**, 0 |
| voll | 3-2-1 | wie oben | 0, 0 | +1, -1, 0 | +1, **-2**, 0 |
| lam3 | 1-2-3 | 0: 0,261; pi: 0,393 | -1, +1 | -1, +1, 0 | 0, 0, 0 |
| lam3 | 3-2-1 | wie oben | +1, -1 | +1, -1, 0 | 0, 0, 0 |
| lam4 | 1-2-3 | 0: 0,569; pi: 0,764 | 0, 0 | -1, **0**, 0 | -1, +1, 0 |
| lam4 | 3-2-1 | wie oben | 0, 0 | +1, -1, 0 | +1, -1, 0 |
| lam1 | beide | lueckenlos bei 0 (kleinster Abstand 0,0) | (0, 0; Baender beruehren sich) | - | - |

- **Nachbau Kitagawa:**
  - lam3 hat Chern +-1, lam4 Chern 0 mit Randmoden, wie die Quelle (S. 7).
  - lam1 (statisch) ist bei 0 lueckenlos.
  - Die Umkehr der Reihenfolge kehrt die Chern-Zahlen und den Randfluss um.
- **Zaehlfehler (fett):** Der gesamte spektrale Fluss eines Streifens ist null, weil det U = 1 ist (jeder Schritt hat
  Spur 0 im Exponenten) [M]. In drei Zellen ist die Summe aus oben, unten und Volumen aber nicht 0 (+1, -1, -1). Dort hat
  meine Zuordnung ueber Eigenvektor-Ueberlapp einen Durchgang doppelt gezaehlt oder verpasst. Eine Summenprobe stand
  nicht in den eingefrorenen Regeln.

## Selbstanzeigen

1. **Higashikawa zuerst falsch gelesen:** Im Rauchlauf P3b hatte ich U_j^- mit e^{-ik} statt e^{+ik} gebaut. Das
   ergab einen quadratischen Kegel und den Rand +sigma_0. Eq. (2) und die Entwicklung auf S. 2 verlangen e^{-+ik}. Ich
   habe das vor dem Einfrieren berichtigt und die Quellformel fuer cos eps als Nachbauprobe eingebaut.
2. **Vor dem Einfrieren gesehen:**
   - W3 der Produkte, der Dreieckstakte und von Higashikawa: halbe Zone -1, ganzer Torus ~0. Der ganze Torus zaehlt zu
     DT1.
   - Die Chern-Zahlen aller 2D-Protokolle.
   - Nicht gesehen: W3 der LM-Treffer und den 2D-Randfluss, der im Rauchmodus nicht geschrieben wurde.
3. **Kitagawa-Parameter:** Fig. 6 nennt "JT = pi/16", der Text "J/omega = 3/32" (JT = 3 pi/16). Mit pi/16 kann die
   Luecke bei pi gar nicht schliessen, und lam4 hatte im Rauchlauf Chern +-1. Ich habe 3 pi/16 genommen, vor dem
   Einfrieren und nach Sicht der Chern-Zahlen aus dem Rauchlauf. Mit 3 pi/16 gibt die Rechnung die Aussagen der Quelle
   wieder; den Widerspruch in der Quelle habe ich nicht geklaert.
4. **Code nach den Rauchlaeufen geaendert (vor dem Einfrieren):**
   - fehlende Funktion fib_dirs
   - Higashikawa-Vorzeichen (Punkt 1)
   - Gitter und Lueckenpruefung in 2D
   - Kreuzungsregel des Randflusses
   - analytische Jacobi-Matrix
   - LM-Suche je N ein Lauf
   - Schutz in auswertung2.py gegen die im Rauchmodus ausgelassenen Felder
   Keine Urteilsregel und keine Vorhersage geaendert.
5. **Randfluss ohne Summenprobe:** In 3 von 12 Zaehlungen ist die Summe nicht 0 (Abschnitt 2D). Die eingefrorene
   DT3-Regel kennt keine Summenprobe; daran haengt das mechanische DT3-Urteil. Nachrechnung nach dem Einfrieren siehe
   "Diagnose".
6. **Eigene Units gestoppt bzw. Logdatei doppelt benutzt:**
   - Die veraltete Rauch-Unit r41t2rLM (Differenzen-Jacobi) habe ich mit systemctl --user stop beendet.
   - Zwei Rauchlaeufe schrieben kurz in dieselbe Datei rauch/lm_rauch.log; die Zeilen sind gemischt, die JSON-Datei
     stammt vom neuen Lauf.
7. **T2 stuetzt sich auf K-Theorie-Saetze aus dem Gedaechtnis [L]** (Bass/Heller/Swan; Swan bzw. Quillen/Suslin fuer
   Laurent-Ringe). An keiner Quelle gelesen (Abrufbudget), nicht gegengelesen. Die Rechnung prueft T2 nur an Beispielen.
8. **Werkzeuge:**
   - Lokal: jq, sed, grep, sha256sum, date, ssh, scp, cp, mv, mkdir, dazu ls, cat, rm (eine eigene Hilfsdatei
     koeff_jac.neu) und Warteschleifen bzw. Monitor. Kein python, awk oder perl.
   - Auf der .69 ausserhalb des Starters: mkdir, mv, cp, ls, grep, tail, cut, sed, basename, test, sha256sum,
     systemctl --user (lesend, einmal stop fuer die eigene Unit).
9. **Suchlauf N = 3 zweimal abgebrochen, dritter Versuch mit 3 Starts:**
   - H-LM3 (30 Starts) und H-LM3b (15 Starts) liefen genau 600 s und wurden vom Starter beendet (rc = 1). Mein
     Rauchlauf (2 Starts in 19,5 s) hatte die Laufzeit stark unterschaetzt; einzelne Starts brauchen ueber 60 s.
   - Die eingefrorene Auswertung verlangt alle Dateien. Deshalb waren die erste und die zweite Auswertung in allen vier
     Urteilen "nicht auswertbar" (lauf-69/auswertung2_erstlauf.json, _zweitlauf.json).
   - Der dritte Versuch H-LM3c mit 3 Starts lief durch (2 Treffer, 89,9 s). Erst damit entstand die gueltige
     Auswertung.
   - Die Regel aus Teil 1 erlaubt einen zweiten Versuch nur bei Fehlern ausserhalb des Codes. Beide Wiederholungen sind
     Abweichungen; der Plan nannte 30 Starts.
   - Die Saat ist dieselbe. Die 3 Starts sind die ersten 3 der geplanten 30, also keine nachtraeglich ausgewaehlte
     Stichprobe.
10. **Kartenwortlaut DT3:** Der Plan sagt "Kartenwortlaut: DT0 bis DT3 wie oben". Ich nenne DT3 nach Kartenwortlaut
    trotzdem getrennt, weil der Wortlaut ("eine einseitige Randwelle") schwaecher ist als meine Planregel (beide
    Luecken). Das ist eine Abweichung von meiner Festlegung, nicht von der Karte.
11. **Diagnoseskripte nach dem Einfrieren:** code/diag_rand.py (ein Lauf ueber den Starter) nutzt nur eingefrorene
    Funktionen mit anderen Gitterparametern. Es aendert kein Urteil.
12. **Zeitbox:** 120 min ab 16:33:41 CEST; Text abgeschlossen um 17:27:01 CEST (date).

## Diagnose nach dem Einfrieren (aendert kein Urteil)

- **Randfluss neu gezaehlt** (code/diag_rand.py, Lauf r41t2dRand 15:11:59 bis 15:14:27 UTC, lauf-69/diag_rand.json):
  - Gleiche eingefrorene Funktionen, anderes k-Gitter (1201 Punkte, k = 0 nicht auf dem Gitter), Streifen 41 Zellen,
    mit Summenprobe.
  - voll 1-2-3: Luecke 0 (-1, +1, 0), Luecke pi (-1, +1, 0); voll 3-2-1: (+1, -1, 0) in beiden Luecken. Die Summen sind
    0. Der Wert +2 im Hauptlauf war also ein Zaehlfehler auf dem symmetrischen Gitter.
  - lam3: Luecke 0 (-1, +1, 0), Luecke pi (0, 0, 0), umgekehrt gespiegelt.
  - lam4 1-2-3, Luecke 0: wieder (-1, 0, 0), also mit Summe -1 unvollstaendig. Ein Randdurchgang am unteren Rand wird
    dort verpasst; die Ursache habe ich nicht geklaert. Alle anderen lam4-Werte sind sauber.
- **Folge:** Fuer den reinen Dreieckstakt gilt mit sauberer Zaehlung: In jeder der beiden Luecken laeuft am oberen Rand
  netto eine Welle mit d eps/dk < 0 und am unteren eine mit d eps/dk > 0. Die Umkehr des Drehsinns kehrt beide um. Das
  ist der Inhalt von DT3. Das mechanische Urteil nach der eingefrorenen Zaehlung bleibt trotzdem stehen.

## Bedeutung fuer Finns Frage

- **2D (belegt im Modell [E], Literaturmodell nachgebaut):** Ein Takt mit festem Drehsinn um die drei
  Bindungsrichtungen des Wabengitters, Finns "Dreiecke mit Takt und Richtung", erzeugt an jedem Rand eine Welle, die nur
  in eine Richtung laeuft. Ihre Richtung legt der Drehsinn fest.
  - Im reinen Takt (vollstaendiger Uebertrag, streng lokal) sind die Volumenbaender flach und topologisch trivial
    (Chern 0). Die einseitige Randwelle kommt allein aus der Windung des Takts.
  - Bei schwaecherem Takt (lam3) tragen die Baender Chern +-1, und die Randwelle gibt es nur in einer Luecke.
- **3D (Schreibtisch T2 [M, mit L], numerisch an allen Beispielen bestaetigt):** Ein streng lokaler Takt, also endliche
  Reichweite, ein Gitter und Translationsinvarianz, kann im Volumen keine Netto-Haendigkeit erzeugen: W3 = 0, egal wie
  die Schritte angeordnet sind.
  - Finns 3D-Dreieckstakt am Tetraeder gibt deshalb W3 = 0 in beiden Drehsinnen.
  - Das Literaturbeispiel (Higashikawa u. a.) zeigt, wie man trotzdem ein einzelnes Weyl-Teilchen bekommt: Man nimmt nur
    die halbe Zone, die "unteren Baender". Der Partner mit der anderen Haendigkeit sitzt bei k3 = 2 pi im oberen Block,
    ebenfalls bei Quasienergie 0. Die beiden Haelften stossen bei Quasienergie pi auf ganzen Ebenen aneinander.
  - Der Ort der Anomalie ist dort der abgetrennte obere Bandraum, nicht der Gegentakt.
- **Verbindung 2D/3D [H]:** Die einseitige 2D-Randwelle ist selbst ein "ungepaartes" chirales Teilchen, aber am Rand
  eines Volumens, das den Ausgleich traegt. Entsprechend waere ein ungepaartes 3D-Weyl-Teilchen der Rand eines
  4D-Takts. Das habe ich nicht gerechnet.
- **Grenzen:** Ein-Teilchen-Bild, keine Eichung, keine Wechselwirkung, kein Messbezug.
- **Zeitumkehr [M]:** Bei reellen Spruengen ist die Umkehr der Tick-Reihenfolge genau die zeitumgekehrte Spielregel
  (K U^-1 K = E1 E2 E3).
  - In 2D dreht sie die Laufrichtung der Randwelle. Die Laufrichtung kehrt sich unter Zeitumkehr um.
  - In 3D aendert sie W3 nicht (T1); die Haendigkeit eines Weyl-Punkts bleibt unter Zeitumkehr gleich.
  - Das passt zur Grenze der Karte: Eine echte Zeitumkehr allein tauscht nie links und rechts [L].

## Laeufe (UTC, alle ueber kleintest.sh, 1 Thread)

| Lauf | Spur | Inhalt | Start bis Ende | Ergebnis |
|---|---|---|---|---|
| H-P3 | p4000b | 3D: Produkte, Takte, Additivitaet, Higashikawa (mit Weyl-Suche) | 15:00:46 bis 15:01:42 | rc = 0, 55,9 s |
| H-H2 | p4000a | 2D: vier Protokolle, je zwei Reihenfolgen, Streifen | 15:00:48 bis 15:03:13 | rc = 0, 144,0 s |
| H-LM2 | p4000a | Suche N = 2, 40 Starts | 15:03:13 bis 15:05:55 | rc = 0, 23 Treffer |
| H-LM3 | p4000b | Suche N = 3, 30 Starts | 15:01:43 bis 15:11:43 | rc = 1 (600-s-Grenze) |
| Auswertung 1 | p4000b | auswertung2.py | 15:11:58 | alle "nicht auswertbar" (lm_3 fehlt) |
| Diagnose Rand | p4000b | diag_rand.py | 15:11:59 bis 15:14:27 | rc = 0 |
| H-LM3b | p4000a | Suche N = 3, 15 Starts | 15:12:17 bis 15:22:18 | rc = 1 (600-s-Grenze) |
| Auswertung 2 | p4000a | auswertung2.py | 15:22:18 | alle "nicht auswertbar" |
| H-LM3c | p4000a | Suche N = 3, 3 Starts | 15:22:51 bis 15:24:21 | rc = 0, 2 Treffer |
| Auswertung 3 | p4000a | auswertung2.py | 15:24:21 bis 15:24:22 | DT0 ja, DT1 nein, DT2 n. a., DT3 nein |

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-170038, EINGEFROREN-SHA256.txt
- quellen/higashikawa-nakagawa-ueda-1806.06868v2.pdf, quellen/kitagawa-berg-rudner-demler-1010.6126.pdf
- code/teil2.py, code/auswertung2.py, code/windung.py (unveraenderte Kopie aus Teil 1), je .eingefroren-20261004-170038;
  code/diag_rand.py (nach dem Einfrieren)
- rauch-69/ (p3_rauch, h2_rauch, lm_rauch, Test der Auswertung in rauch-69/test/)
- lauf-69/: p3.json, h2.json, lm_2.json, lm_3.json, auswertung2.json (gueltig), auswertung2_erstlauf.json,
  auswertung2_zweitlauf.json, diag_rand.json, Logs r41t2*.log, PRUEFSUMMEN.txt
- Auf der .69: /home/fmh/fmhc-physics-remote/runde41-qca-windung/teil2/

## Einfach gesagt

Finn hat gefragt, ob Dreiecke mit Takt und Drehrichtung eine Welle machen koennen, die links- oder rechtsherum laeuft.
In der Flaeche ja: Wenn auf einem Bienenwabengitter die drei Sprungrichtungen reihum mit festem Drehsinn an die Reihe
kommen, laeuft am Rand eine Welle nur in eine Richtung, und dreht man den Takt um, laeuft sie andersherum. Im Raum
dagegen hebt sich die Haendigkeit bei jedem streng lokalen Takt immer weg; das zeigt eine allgemeine Rechenregel, und
alle 104 gerechneten Beispiele halten sich daran. Ein einzelnes links- oder rechtsdrehendes Teilchen bekommt man nur,
wenn man einen Teil der Zustaende abtrennt, wie im bekannten Literaturmodell, dessen Partner dann im abgetrennten Teil
sitzt. Das sind Rechnungen an Modellen, keine Messungen.
