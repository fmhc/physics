# TAKT-UMKLAPP-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 47, Finn-Auftrag "Zellen umklappen")

- Start 2026-10-05 07:21:17 CEST (date). Plantext ab 07:42:44 CEST (date), vor jeder Hauptrechnung. Zeitbox 150 min,
  also bis 09:51:17 CEST.
- Grundlage: KARTE.md (HT0, HT1', HT2, HT3, TU1; Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Kennzeichen: [M] vorab ableitbar (eigene Mathematik), [E] hier gerechnet, [P] Projektdatei, [S] Quelle (ueber
  HODGE-L), [F] eigene Festlegung, [H] Hypothese, [L] Gedaechtnis. Alles ist synthetische Gitterrechnung, keine
  Messdaten.
- Code: code/tu.py (neu). Unveraendert kopiert und importiert: tg.py, tg_auswertung.py, tp.py, uk.py, ew.py,
  nachtrag_v.py (aus umklapp-1/code; sha256 ec48a258..., 88cbd2ce..., 419d7da6..., f52df743..., fa7b6417...,
  a5dff790...) und mn.py (aus materie-netz-1/code, b36984d3...). Die Originale sind unveraendert.

## 0. Zusatz der Leitung 07:27 (woertlich)

> TAKT-UMKLAPP-1 hat jetzt Vorrang: Finn (07:26) will die Karte sofort.
> - Zusatz der Leitung: Du darfst zusaetzlich die Spuren cpu8, cpu9 und cpu10 ueber kleintest.sh nutzen (eigener Lock je Spur). Dann musst du nicht auf p4000a/p4000b (TT-GLAS-2) oder cpu3/cpu4 (DANZER-NAEHERUNG-1) warten. Steht der Lock einer Spur schon, nimm die naechste freie und belege keine doppelt.
> - Sonst bleibt alles wie in der Karte: Plan und Code vor den Hauptlaeufen einfrieren, je Lauf hoechstens 10 Minuten, keine Aenderung an Vorhersagen und Bedeutung.
> - Bitte einen Zwischenstand: Sobald HT0 und HT1' entschieden sind, schreib ZWISCHENSTAND-A.md in deinen Kartenordner (Zeiten per date, Urteile nach Kartenwortlaut). Danach Teil B wie geplant.
> - Diese Nachricht nimmst du woertlich als "Zusatz der Leitung 07:27" in PLAN.md auf.

- Umsetzung: Spuren cpu8, cpu9, cpu10 (um 07:35 alle frei; p4000a und p4000b belegt). ZWISCHENSTAND-A.md nach dem
  ersten Lauf (A1: V, S, V_D, S_D).

## 1. Ableitbarkeitsprobe und Projektsuche

- **Projektsuche** (07:39:38 bis 07:40:16 CEST, grep mit allen vorgeschriebenen Ausschluessen ueber coordination/ und
  model-lab/, Suchwoerter Glickenstein, Hodge-Laplace, umkreisbasiert, circumcentric, zug32, 3-2-Zug,
  Delaunay-gesteuert, Delaunay-wiederherstell, "W^H B W", Takt-Operator). Ergebnis:
  - **PUMPE-NETZ-1 ERGEBNIS 4.4 [P]:** P1-Gewichte je Tetraeder (= 3D-Kotangens = umkreisbasierter Stern *1 [M dort])
    auf V: "alle 68 Kantengewichte positiv (1/60 bis 1/2)", P1-Laplace an 300 Zufalls-k positiv (kleinster Eigenwert
    0,0144).
  - **UMKLAPP-1 Nachtrag 4.4 [P]:** V verletzt an genau 12 von 116 Flaechen je Zelle die Delaunay-Bedingung
    (mu = -16/41); nach 12 2-3-Zuegen je Zelle ist V Delaunay (kleinster Randabstand 0,220), regulaer, Spanne 15,4 %.
  - **MATERIE-NETZ-1 [P]:** P = -W^H B W an allen Gitter-k (L = 16, 24, 32) positiv definit ausser k = 0.
  - **DANZER-NAEHERUNG-1 4.4 [P]:** *1 und *2 (umkreisbasiert) auf Danzer-Naeherungen (Delaunay) ohne negative Eintraege.
  - **OKTA-SCHATTEN-1 (laeuft, nur PLAN) [P]:** rechnet P(k)/L(k) fuer Wabennetze (R12, D1z, H3), nicht V oder S.
  - Keine Datei rechnet P gegen c d0^H *1 d0 auf V oder S, Hodge-Sterne nach zufaelligen Zuegen oder
    Delaunay-gesteuerte Zuege nach Eckverschiebung mit TT-Auswertung.
- **HT0 ist vorab ableitbar [M, S]** (Karte). Eigene Skizze: Je Tetraeder gilt mit G_t = sum_e l_e theta_e
  (Schlaefli dG_t = sum theta dl) und a_e = phi_i + phi_j: die Matrix -sum_{e an v} l_e d theta_e / d phi_w ist
  symmetrisch mit Zeilensumme 0, und ueber alle Tetraeder summiert ist P = Hesse-Matrix der Regge-Wirkung nach phi
  am flachen Netz. Dass sie je Tetraeder gleich c mal dem *1-Laplace ist, ist Glickensteins Satz [S ueber HODGE-L],
  hier nicht selbst bewiesen. Die Rechnung prueft das als Kontrolle, auch je Tetraeder (takt_je_tet). c ist vorab
  nicht bekannt (Dossier: Erwartung 8 [H]) und geht in kein Urteil ein.
- **HT1' ist im Wesentlichen schon gerechnet [P]:** *1 > 0 auf V (PUMPE-NETZ-1, falls P1 = umkreisbasiert; das
  prueft diese Rechnung mit, siehe Kontrolle K6), negative *2 auf V (12 je Zelle; aus mu < 0 und HKV "lokal Delaunay
  <=> *2 > 0" [S]) und V_D Delaunay (UMKLAPP-1 Nachtrag). Ein "eingetroffen" waere eine Wiederholung mit einem
  zweiten Code (Sterne direkt aus Umkreismitten statt P1 bzw. mu), keine neue Messung. Neu sind nur S und S_D.
- **HT2:** Dass zufaellige 2-3-Zuege nicht-Delaunay-Flaechen und damit negative *2 erzeugen, ist so gut wie sicher
  [M, nicht bewiesen: die Zuege waehlen gleichverteilt unter allen konvexen Flaechen]. Ob P positiv semidefinit bleibt,
  ist nicht ableitbar (HKV sichert nur Delaunay; Doehrman/Glickenstein "in many cases" [S Abstract]).
- **HT3 ist vorab ableitbar [M]** (Karte): Mit c = -B W ist ker c^H das B-orthogonale Komplement von Bild W. Ist
  B auf Bild W (also -P) nicht entartet, zerfaellt der Kantenraum B-orthogonal, und nach Sylvester gilt
  n_-(B) = n_+(P) + n_-(B auf ker c^H). Weil B M = 0 und c^H M = 0, ist n_-(B auf ker c^H) = n_-(B_red) mit B_red wie
  tg.punkt. Daraus: n_-(B_red) = n_-(B) - V + n_-(P) + n_0(P). Die Rechnung prueft die Identitaet als Kontrolle des
  Codes an allen gerechneten Punkten.
- **TU1 ist nicht ableitbar, aber weitgehend aus Projektdaten erwartbar [P]:** Der D-Arm endet im Delaunay-Netz der
  verschobenen Punkte, also wieder in einem Poisson-Delaunay-Netz; TT-GLAS-1 fand 48 von 48 solchen Netzen regulaer.
  Der Z-Arm: UMKLAPP-1 fand etwa eine negative Richtung je fuenf zufaellige 2-3-Zuege. Bei a = 1e-3 sind es wenige
  Zuege je Netz (UMKLAPP-1: im Mittel 7,5e-3 der Tetraeder), dann bleiben viele Z-Netze stabil; bei a = 1e-2 und auf
  V (96 Zuege je 2 x 2 x 2) erwarte ich fast nur instabile Z-Netze. Neu sind die zufaelligen 3-2-Zuege (in UMKLAPP-1
  nicht gerechnet) und die genauen Anteile.

## 2. Konstruktionen [F]

- **Netze.** Allgemeine Form wie tg.py: Gittervektoren LV (Zeilen), Lagen, Tetraeder G (T, 4), Bildversaetze O.
  - V: tg.netz_V() (unveraendert; gleich der eigenen Umformung von ew.geometrie('V'), wird geprueft). S: dieselbe
    Umformung von ew.geometrie('S'). Beide primitive fcc-Zellen (ew.AV), 10 bzw. 6 Ecken, 58 bzw. 34 Tetraeder.
  - V_D, S_D: Delaunay-Reparatur (Abschnitt 4) ohne Verschiebung auf V bzw. S.
  - Glasnetze: tg.zufallsnetz(128, s), s = 1 bis 12 (TT-GLAS-1).
  - UMKLAPP-1-Netze: tg.zufallsnetz(N, s), dann uk.zugfolge mit derselben Saat (default_rng([4538, N, s])) bis
    round(f F0) Zuege: N = 128, s = 1 bis 4, f = 0,05 und 0,2; N = 256, s = 1 bis 3, f = 0,2; N = 256, s = 1,
    f = 0,05. Probe: Zugzahlen gleich UMKLAPP-1 4.2 und 4.3 (345/347/349/340, 86/87/87/85, 696/692/681, 174).
  - Teil B: D- und Z-Netze (Abschnitt 4); V2 = 2 x 2 x 2-Superzelle von V (80 Ecken, 464 Tetraeder).
- **Hodge-Sterne (umkreisbasiert, vorzeichenbehaftet wie HKV 2013).** Je Tetraeder t mit Umkugelmitte c_t:
  - Kante ij mit Gegenecken k, l: duale Teilflaeche A*_ij,t = 1/2 (h_ij,k h_ijk,l + h_ij,l h_ijl,k). h_ij,k =
    Abstand Kantenmitte -> Umkreismitte von ijk, positiv zur Seite von k; h_ijk,l = Abstand Umkreismitte von ijk ->
    c_t, positiv zur Seite von l. *1_e = sum_t A*_e,t / l_e.
  - Flaeche f zwischen t1 und t2: duale Laenge L*_f = h_f(t1) + h_f(t2) (Umkreismitte von f -> c_t, positiv zur
    Gegenecke von t); *2_f = L*_f / |f|.
  - *0_v = sum_t sum_{e an v} (l_e / 6) A*_e,t.
  - Negativ: *1 < -1e-12 max|*1|, ebenso *2; null: |.| <= 1e-12 max.
- **Takt-Operator und Hodge-Laplace bei Bloch-k** (Konvention tg.ops = mn.W_of):
  - W (E x V): Zeile e hat 1 an der Anfangsecke und e^{i k T_e} an der Endecke (a_e = phi_s + e^{ik.T} phi_s2).
    B aus tg.ops_BA (unveraendert). P = -W^H B W (hermitesch gemacht).
  - d0 (E x V): -1 an der Anfangsecke, e^{i k T_e} an der Endecke. L1 = d0^H diag(*1) d0.
  - Gegenprobe der Bauweise auf V und S: P aus ew.ops + mn.W_of (MATERIE-NETZ-1, unveraendert) gegen P aus tg.
  - c(k) = Re<L1, P>_F / <L1, L1>_F; c = Median ueber k; Rest(k) = max|P - c L1| / max|P|.
  - Je Tetraeder bei k = 0: P_t = -W_t^T (l D l)_t W_t gegen L_t = d0_t^T diag(A*_t / l_t) d0_t (4 x 4), ein c fuer alle
    Tetraeder, Rest je Tetraeder.
- **k-Saetze.** "klein": 13 Wuerfelrichtungen bei |k| = 1e-2 und [100], [110], [111] bei 2e-2 (wie tg.spektrum).
  "Gitter": m/n_g @ reziproke Basis, m in {0..n_g-1}^3 (n_g = 6 fuer V, S, V_D, S_D: 216 Punkte; n_g = 4 fuer Glas-
  und UMKLAPP-1-Netze: 64 Punkte), dazu 20 Zufalls-k in der reziproken Zelle (default_rng([4542, 1 bzw. 2])).
  Teil B: 16 kleine und 8 Zufalls-k (default_rng([4542, 3])).
- **P positiv semidefinit** an einem k: lambda_min(P) >= -1e-10 max|lambda(P)|; "an allen k" = an allen gerechneten k.
- **Traegheit (HT3):** n_-, n_0, n_+ von B (dicht, E x E), P (V x V) und B_red (wie tg.punkt: Komplement von
  Bild[M, c] per QR bzw. SVD) mit Schwelle 1e-9 max|lambda| (wie tg.punkt). Ausgegeben werden auch der groesste als
  null gezaehlte und der kleinste als nicht null gezaehlte |lambda(B)| (Abstand der Schwelle). Punkte: V, S, V_D, S_D
  an allen k != 0 der Saetze; Glas- und N = 128-Netze an "klein-100-1" und zwei Zufalls-k; N = 256 an "klein-100-1"
  und einem Zufalls-k; Teil B je Arm an "klein-100-1".

## 3. Kontrollen (vorab ableitbar; keine Messung)

- K1 (HT0): P = c L1 an allen k auf V und S (Rest <= 1e-10); dazu auf allen anderen Netzen beschreibend.
- K2 (HT3): n_-(B) = n_+(P) + n_-(B_red) an allen Punkten mit n_0(P) = 0.
- K3: sum_e l_e A*_e = 3 V_ges, sum_v *0_v = V_ges, sum_f |f| L*_f = 3 V_ges (je auf 1e-12).
- K4: Vorzeichen von *2 gleich dem von mu (uk.raender) an allen Flaechen mit |mu| > 1e-9 (HKV, Lemma 2 [S]).
- K5: P aus MATERIE-NETZ-1 (ew + mn.W_of) gleich P aus tg (relativ <= 1e-10).
- K6: *1 auf V zwischen 1/60 und 1/2 wie die P1-Gewichte von PUMPE-NETZ-1 [P] (beschreibend; zeigt P1 = umkreisbasiert).
- K7: Delaunay-Netze (Glas, D-Arm) ohne negative *1, *2 (HKV [S]); UMKLAPP-1-Zugzahlen reproduziert; V_D mit genau 12
  2-3-Zuegen je Zelle; D-Arm-Ergebnis gleich scipy-Delaunay der verschobenen Punkte (nur kubische Kaesten).

## 4. Teil B: Verschiebung, Delaunay-Wiederherstellung, Zufallszuege gleicher Zahl [F]

- **Faelle:** Glasnetze N = 128, Saaten 1 bis 12, und V2; je a = 1e-3 und 1e-2; zusammen 26 Faelle.
- **Verschiebung:** delta_i = a lbar / sqrt(3) xi_i, xi_i standardnormal (default_rng([4540, N, s]); V2: [4540, 0, 2]),
  fuer beide a dieselben xi (gemeinsame Zufallszahlen); lbar = mittlere Kantenlaenge; Lagen nicht zurueckgefaltet.
- **D-Arm (M-B waehlt):** Die Ecken laufen in 10 gleichen Teilschritten von x nach x + delta. Nach jedem Teilschritt
  Reparatur: Solange eine Flaeche mu < -1e-9 hat, wird die staerkste Verletzung zuerst behandelt, an der ein Zug
  moeglich ist:
  - 2-3, wenn die Strecke d-e das Innere des Dreiecks trifft (alle drei Volumina gleiches Vorzeichen, je > 1e-10 des
    mittleren Volumens, neue Kante noch nicht vorhanden; uk.zug23 unveraendert);
  - 3-2, wenn d-e hinter genau einer Kante PQ liegt und das dritte Tetraeder PQDE existiert (Kante vom Grad 3); neue
    Tetraeder PRDE, QRDE; Volumensumme gleich auf 1e-9, jedes neue Volumen > 1e-10 des Mittels.
  - Kein moeglicher Zug: "stecken", ausgewiesen. Gezaehlt werden ausgefuehrte 2-3- und 3-2-Zuege (n23, n32), dazu die
    Netto-Aenderung gegenueber dem Ausgangsnetz (uk.cluster), umgeklappte Tetraeder (Vorzeichenwechsel des Volumens
    zwischen Teilschritten) und, bei kubischem Kasten, der Vergleich mit uk.delaunay_periodisch der Endlagen.
  - Grund fuer Teilschritte: Bei a = 1e-2 koennten flache Tetraeder in einem Schritt umklappen; der stetige Weg
    entspricht "die Verbindungen folgen den Ecken" (M-B).
- **Z-Arm (gleich viele zufaellige Zuege):** auf dem unverschobenen Ausgangsnetz (Lagen x) genau n23 2-3- und n32
  3-2-Zuege in zufaelliger Typenreihenfolge (default_rng([4541, N, s, ia]), ia = 0 fuer 1e-3, 1 fuer 1e-2); je Schritt
  gleichverteilt unter allen erlaubten Zuegen des Typs: 2-3 wie UMKLAPP-1 (uk.kandidaten, Volumenschwelle 1e-3 des
  mittleren Ausgangsvolumens, keine doppelte Kante), 3-2 je Kante vom Grad 3 mit konvexer Huelle und beiden neuen
  Volumina ueber derselben Schwelle. Fehlt ein erlaubter Zug, wird er ausgelassen und gezaehlt.
  - Grund fuer unverschobene Lagen: Die alte Verbindung kann bei a = 1e-2 auf den verschobenen Lagen umgeklappte
    Tetraeder haben, ist dann kein gueltiges Netz. Eine Verschiebung um 1e-3 bis 1e-2 der Kantenlaenge allein aendert
    an einem flachen Netz nichts Qualitatives [H].
- **Auswertung je Arm:** tg.modell, Hodge-Sterne, P psd (24 k), c und Rest, Traegheit an klein-100-1, TT-Spektrum
  tg.spektrum (13 Richtungen, 16 Punkte, unveraendert), Kennzahlen tg_auswertung.netz_kennzahlen (unveraendert).
- **"stabil"** (Karte: "keine wachsenden Moden") = n_wachsend = 0 an allen 16 Punkten (n_wachsend_max = 0).
  Beschreibend: "regulaer" (TT-GLAS-1), B_red negativ (max ueber k), A_red positiv definit, Spanne, mittleres
  omega^2/k^2.

## 5. Urteilsregeln (mechanisch in code/tu.py, Funktion auswertung)

- **HT0** (V und S, alle k der Saetze, 252 je Netz):
  - Wortlaut: je Netz Rest(k) <= 1e-10 an allen k mit dem festen c des Netzes (Median ueber k).
  - Plan: Wortlaut und c_V = c_S (relativ <= 1e-10) und c(k) an allen k gleich dem Median (relativ <= 1e-10) und K5.
- **HT1'** (V, V_D):
  - Wortlaut: V hat negative *2 ("trotz") und alle *1 auf V > 0 (kein negativer, kein Null-Eintrag); V_D hat keinen
    negativen und keinen Null-Eintrag *2 und keine Flaeche mit mu < -1e-9.
  - Plan: Wortlaut und V_D entsteht mit genau 12 2-3-Zuegen je Zelle (keine 3-2-Zuege, nicht stecken).
  - S und S_D: beschreibend (Karte: "S: offen").
- **HT2** (UMKLAPP-1-Netze bei f = 0,2: N = 128 Saaten 1 bis 4, N = 256 Saaten 1 bis 3):
  - Wortlaut: In den Netzen gibt es negative *2 (mindestens ein Netz), und P ist in jedem Netz an allen gerechneten k
    psd.
  - Plan: jedes Netz hat negative *2, und P ist in jedem Netz an allen gerechneten k psd.
  - Fehlt ein Netz, steht das als Vermerk dabei.
- **HT3** (alle Traegheitspunkte aus Teil A und Teil B):
  - Plan: Identitaet n_-(B) = n_+(P) + n_-(B_red) an allen Punkten mit n_0(P) = 0.
  - Wortlaut: An allen Punkten, an denen P eine negative Richtung hat, ist n_-(B_red) - (n_-(B) - V) = n_-(P)
    ("genau so viele negative Moden mehr"). Gibt es keinen solchen Punkt: "nicht entscheidbar (Praemisse in keinem
    Netz eingetreten)".
- **TU1** (26 Faelle):
  - Wortlaut: Anteil stabiler D-Netze >= 0,9 und Anteil stabiler Z-Netze < 0,9 (alle Faelle).
  - Plan: nur Faelle mit mindestens einem D-Zug; D-Anteil >= 0,9 und Z-Anteil <= 0,5.
  - Fehlen Faelle (Laufzeit), werden die vorhandenen gewertet und die Zahl vermerkt.

## 6. Agenten-Vorhersagen (vorab; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B1 | P bleibt in allen Netzen nach zufaelligen Zuegen (UMKLAPP-1 und Z-Arm) an allen gerechneten k psd | 55 % |
| B2 | D-Arm stabil in 26 von 26 Faellen | 80 % |
| B3 | In den instabilen Z-Netzen kommen die negativen Richtungen von B_red aus B selbst (n_-(P) = 0 ueberall) | 55 % |
| B4 | Negative *1 gibt es nach zufaelligen Zuegen seltener als negative *2 (Anteil an E bzw. F) | 65 % |

## 7. Laeufe auf der .69 (kleintest.sh, Spuren cpu8, cpu9, cpu10, je 1 Thread, <= 600 s)

- Arbeitsordner /home/fmh/fmhc-physics-remote/takt-umklapp-1/ (code/ eingefroren, lauf/). Laufketten code/kette-cpu8.sh,
  code/kette-cpu9.sh, code/kette-cpu10.sh, einmalig per ssh gestartet (kein Dienst, kein Timer). Schlusszeit: nach
  09:30 CEST (07:30 UTC) startet kein neuer Lauf. Danach Auswertung und Bild (code/tu.py auswertung, bild) auf cpu8.
- Schaetzungen aus den Rauchtests (Abschnitt 8): A1 (V, S, V_D, S_D) ~15 s; Glas N = 128 ~8 s je Netz; UMKLAPP-1-Netze
  N = 128 ~13 s, N = 256 ~2 min je Netz; Teil B ~170 s je Glasnetz (beide a, beide Arme, 13 Richtungen), V2 ~1 min.
- cpu8: A1 (V, S, VD, SD) -> A2a (Glas s1-6) -> B1 (Glas s1, s2) -> B4 (s7, s8) -> B7 (V2).
- cpu9: A3 (UMKLAPP-1 N = 128, s1-4, f = 0,05 und 0,2) -> A2b (Glas s7-12) -> B2 (s3, s4) -> B5 (s9, s10).
- cpu10: A4 (N = 256 s1, s2, f = 0,2) -> A5 (N = 256 s3 f = 0,2; s1 f = 0,05) -> B3 (s5, s6) -> B6 (s11, s12).
- Geschaetzt 14 bis 18 min je Spur.

## 8. Rauchtests vor diesem Plantext (.69 in UTC)

- r1 (05:39:30 bis 05:39:36, cpu8): teilA V, S, VD, SD --rauch. r2 (05:39:30 bis 05:39:53, cpu9): teilB
  glas-N128-s901, a = 1e-2, nur Richtung 0, --rauch. r3 (05:39:30 bis 05:39:47, cpu10): teilA glas-N128-s901,
  uk-N128-s901-f0.2 --rauch. r4 (05:41:18, cpu8): teilB V2 --rauch, Absturz (superzelle-Aufruf mit 6 Argumenten);
  behoben, r4b (05:41:31 bis 05:41:39) rc = 0. r5 (05:41:18 bis 05:41:38, cpu9): ohne --rauch auf Rauchnetzen
  (teilA V, S, VD, SD, glas-N32-s901, uk-N32-s901-f0.2; teilB glas-N32-s901; auswertung; bild) als Absturzprobe.
- Gelesen: Rueckgabewerte (alle 0 ausser r4), Laufzeiten, Speicher, Schluessel. Sichtbar waren ausserdem die
  Zugzahlen in den Logzeilen: D-Arm 20 2-3- und 14 3-2-Zuege (Rauchsaat 901, N = 128, a = 1e-2) und 96/0 auf V2
  (a = 1e-3; erwartet: 12 je Zelle [P]). r5 hat V und S schon voll gerechnet; deren Werte habe ich nicht gelesen.
- Regeln (Abschnitte 2 bis 6) danach unveraendert.
