# GUERTEL-FINN-NETZ-1: Plan (Runde 43; Guertel-Trick auf Finns Tetraeder-Netz)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 19:38:15 CEST (date). Plantext ab 19:46:13 CEST (date),
  vor Code und Rauchlauf. Zeitbox 120 min, also bis 21:38:15 CEST.
- **Unterbrechung (Sitzungslimit):** letzte Dateiaenderung davor 19:53:00 CEST (mtime code/auswertung_fn.py);
  Wiederaufnahme 21:35:55 CEST (date). Verbraucht waren 14 min 45 s; nach Vorgabe der Leitung [Zusatz Leitung] gilt die
  Restzeit von 105 min 15 s ab Wiederaufnahme, also bis 23:21:10 CEST. Auf der .69 lief in der Pause nichts von mir.
- Karte: KARTE.md (K0, Teile A bis C, GF0 bis GF2, Bedeutung). Daran aendert dieser Plan nichts. Festlegungen [F]
  machen die Karte rechenbar; Zusaetze sind als **Zusatz** markiert und nicht urteilsbildend.
- Kennzeichen: [M] Mathematik; [E] Rechnung im Modell; [L] Literatur oder Gedaechtnis; [H] Hypothese; [F] Festlegung
  dieses Plans; [R] im Rauchlauf gesehen. Alles ist eine synthetische Modellrechnung, keine Messdatenbestaetigung.
- Vorwissen aus veroeffentlichten Ergebnissen (nur Z^3): GUERTEL-FELD-STAB-1 (GFS1) und GUERTEL-2 N1. Auf Z^3 (12, 24)
  kam im 10-Grad-Protokoll der erste Gittersprung bei 540 Grad (GFS1 ERGEBNIS, Punkt 3) [E, fremd]. Diamant-Werte
  kenne ich keine.

## 0. Ableitbarkeit und Dimensionen (vorab)

1. **Symmetrie [M]:** Die Energie haengt nur von q_a . q_b ab. Die Spiegelung q -> q quer ist orthogonal auf R^4 und
   laesst jeden Graphen unveraendert. Also ist die umgekehrte Verdrillung bei theta (Kern q_z(theta) = q_z(theta - 720))
   das Spiegelbild der Vorwaertsverdrillung bei 720 - theta: E_um(theta) = E(720 - theta), auf jedem Graphen exakt.
   Die Gleichheit "E auf E(720 - theta)" ist daher eine Konsistenzpruefung, sobald der Stoss ohne Sprung im richtigen
   Tal endet. Gemessen wird, **ob** er dort endet.
2. **Ebene Verdrillung = SO(2) [M]:** Liegt das Feld in der (1, z)-Ebene, q = cos(phi/2) + z sin(phi/2), dann gilt
   4(1 - (q_a . q_b)^2) = 2(1 - cos(phi_a - phi_b)), und q_a . q_b <= 0 genau dann, wenn |phi_a - phi_b| >= pi. Der
   SO(3)-Vorwaertsast ist also bis auf das Rauschen ausserhalb der Ebene dasselbe Problem wie das SO(2)-Feld, und sein
   Gittersprung ist derselbe Phasensprung. Die Sprunggrenze theta_max ist fuer SO(2) und SO(3) im ebenen Ast gleich;
   Unterschiede kommen nur aus der Instabilitaet ausserhalb der Ebene jenseits von 360 Grad.
3. **Kontinuum [M, aus GFS1 PLAN Abschnitt 0]:** Fuer theta > 360 Grad ist der radiale Ast ein Sattel (konjugierter
   Punkt), in d = 1, 2, 3 gleich. Fuer SO(2) gibt es keine Kipprichtung; pi_1(SO(2)) = Z schuetzt die Windung. Ohne
   Phasensprung kann das SO(2)-Feld nicht entdrillen.
4. **Netzvergleich [M]:** Diamant mit kubischer Zellkante a = 2 hat die Knotendichte 8/a^3 = 1 wie Z^3, Bindungslaenge
   sqrt(3)/2 = 0,866 und Summe der Bindungsvektoren b b^T = Einheitsmatrix je Knoten mit 4 Bindungen. Im Kontinuum ist
   die Diamant-Energie daher halb so gross wie auf Z^3 (2 statt 3 Bindungen je Knoten). Energien beider Netze sind
   deshalb nicht direkt vergleichbar; verglichen werden theta_max, Sonde und Ausgang.
5. **Nicht ableitbar [E, Gegenstand der Rechnung]:**
   - wo auf dem Diamant-Netz die Verdrillung lokalisiert (die Bindungsenergie 2(1 - cos omega) wird ab omega = pi/2
     weich) und damit theta_max;
   - ob der Stoss dort ohne Gittersprung in die umgekehrte Verdrillung laeuft.
   - [H] Naive Erwartung: kuerzere Bindungen (0,866) geben kleinere Bindungswinkel, also theta_max eher groesser als auf
     Z^3; die geringere Vernetzung (4 statt 6) kann das Gegenteil bewirken. Keine Zahl vorab.
6. **Dimensionen (AGENTS.md):**
   - **Innere Symmetrie:** SO(3) (Teile A, B, K0) und SO(2) (Teil C) getrennt gerechnet und getrennt ausgewiesen.
   - **Raum:** Beide Netze sind 3D-Graphen; verglichen wird Diamant gegen Z^3 bei (fast) gleicher Knotenzahl. Nichts
     davon wird auf 1D oder 2D uebertragen. Ein radialer Stoss in eine Richtung ist kein voller Stabilitaetsnachweis.

## 1. Netz [F]

- **Finns Netz:** Knoten = Tetraedermitten, Nachbarn ueber die geteilten Ecken, 4 je Knoten. Das ist das Diamant-Gitter
  (ideales beta-Cristobalit: Mitten = Diamant, Ecken = Pyrochlor; Geometrie wie RUNDE-37/iso-atem-1).
- **Koordinaten:** kubische Zellkante a = 2. Untergitter A: ganzzahlige Punkte p mit gerader Koordinatensumme;
  Untergitter B: p + (1/2, 1/2, 1/2). A-Knoten p ist mit p + (1, 1, 1)/2, p + (1, -1, -1)/2, p + (-1, 1, -1)/2 und
  p + (-1, -1, 1)/2 verbunden. Zentrum auf einem A-Knoten (wie Z^3 auf einem Gitterpunkt).
- **Kugel wie Z^3:** alle Knoten mit r <= R + 1; Kern r <= r0, Rand r > R, frei dazwischen; r0 = 12, R = 24. Jeder freie
  Knoten hat alle 4 Nachbarn in der Menge (0,866 < 1).
- **Begruendung der Radien:** Bei gleicher Knotendichte (a = 2) haben Kern, freie Knoten und Rand bis auf
  Oberflaecheneffekte dieselbe Zahl wie auf Z^3 (12, 24): N = 65267, frei 50624, Kern 7153, Rand 7490 (GFS1 prot.json).
  Der Graph haengt nur von r0/a und R/a ab; gleiche Knotenzahl legt ihn also fest (gleichwertig: Bindungslaenge 1 mit
  r0 = 13,86, R = 27,71).
- **Pruefung [F]:** Weicht die Zahl der freien Knoten um mehr als 2 % von 50624 ab, passe ich R vor dem Einfrieren an
  (im Rauchlauf). Die Zahlen werden im Rauchlauf gezeigt und hier nachgetragen.
- **Profil h:** harmonisch in 3D wie GFS1, h = (1/max(r, r0) - 1/R)/(1/r0 - 1/R), Kern 1, Rand 0, auf beiden Netzen und
  fuer beide Feldtypen.

## 2. Code [F]

- code/guertel2.py, code/guertel.py und code/stab.py: unveraenderte Kopien aus GFS1 (sha256 c9374a98..., 795f474d...,
  b7093e59...). In den Quellordnern aendere ich nichts.
- code/finn.py (neu): Klasse Netz auf einem allgemeinen Nachbargraphen (Knotenorte, Bindungslisten a, b). Energie,
  Gradient, Sonde, tang, norm, setze, null, praediktor und rauschen sind Kopien aus g2.Feld; der Feldtyp (so3, so2) ist
  vom Raum getrennt, h immer 3D.
  - **Z^3:** Bindungen und Platzliste werden aus g2.Feld(3, 12, 24) uebernommen (gleiche Reihenfolge), damit K0 mit
    derselben Arithmetik rechnet.
  - **Diamant:** Bau wie in Abschnitt 1.
  - FIRE (fire_feld, fire_log), Protokoll, Kipp-Stoss, Struktur und Kipp-Amplitude: Kopien aus g2 bzw. stab.py, nur auf
    Netz umgestellt; SO(2): Sonde max |phi_a - phi_b| (laufendes Maximum), Sprung bei >= pi.
- code/auswertung_fn.py (neu): mechanische Urteile und Bilder.

## 3. Teil A: Vorwaertsast und theta_max [F]

- **Protokoll P10 (Plan):** wie GUERTEL-2 N1 und GFS1: 10-Grad-Schritte; je Schritt Praediktor, Kern setzen, Rauschen
  1e-3, FIRE 30; an jedem Vielfachen von 90 Grad (auch 0) zusaetzlich FIRE 150; ftol 1e-5, dtmax 0,1. Bis 720 Grad.
  - Saaten: Z^3 default_rng([42, 3, 120, 24]) (wie N1, fuer K0); Diamant [42, 3, 120, 24, 4].
- **Protokoll P30 (Kartenwortlaut "in 30-Grad-Schritten"):** gleiche Parameter, aber Schritt 30 Grad (FIRE 30 je
  Schritt, FIRE 150 an Vielfachen von 90). Bis 720 Grad, beide Netze, gleiche Saaten.
  - **Begruendung der Doppelung:** Die Karte laesst offen, ob "in 30-Grad-Schritten" die Schrittweite des Protokolls
    oder das Raster der Auswertung meint. P10 ist das Protokoll von GFS1 (dessen Zustaende Teil B "wie GFS1" braucht,
    und K0 ist nur damit pruefbar); P30 ist die woertliche Lesart. Plan-Urteile nutzen P10, Wortlaut-Urteile P30.
- **Je Schritt aufgezeichnet:** E, Sonde am Schrittende, laufende Sonde (Minimum ueber alle FIRE-Schritte seit Start),
  fmax; an jedem 30-Grad-Rasterwinkel zusaetzlich qz_mittel_aussen, qz_mittel_innen, q0_min_frei und Kipp-Amplitude P
  (Definitionen wie GFS1).
- **theta_max** := kleinster Winkel im 30-Grad-Raster (30, 60, ..., 720), an dessen Ende die laufende Sonde <= 0 ist
  (erster Gittersprung). Ohne Sprung: "> 720".
  - Nach Plan aus P10; nach Wortlaut aus P30. Beschreibend: Sprungwinkel auf 10 Grad genau (P10).
- **Vorwaertsast gueltig bei theta (nur Plan):** laufende Sonde > 0 an allen Rasterwinkeln bis theta und
  qz_mittel_aussen > 0 an allen Rasterwinkeln 30 <= t <= theta (bei 0 Grad gibt es keine Verdrillung; Korrektur nach
  dem Rauchlauf, siehe unten). Damit wird ein Zerfall in die umgekehrte Verdrillung ohne Sprung nicht als Vorwaertsast
  gezaehlt. Nach Wortlaut zaehlt nur die Sonde.
- **Gespeichert** (Zustand nach allen Relaxationen des Winkels): 270, 300, 330, 360, 390, 420, 450 Grad (P10).

## 4. K0 [F]

- Z^3 (12, 24), P10 mit finn.py. Bezugswerte aus GFS1 lauf-69/prot.json (Kopie in eingaben-gfs1/, mechanisch gelesen),
  **Teil des Urteils:** E_schritt(420) = 14642,446583942661; E_schritt(450) = 16725,58389579176;
  E_gitter(450) = 16722,374712425655.
- Nach Plan: alle drei auf 1e-6 relativ und Sonde an allen drei > 0. Nach Wortlaut ("bei 450 Grad"): E_schritt(450) und
  E_gitter(450) auf 1e-6 relativ.

## 5. Teil B: Stoss auf dem Diamant-Netz (SO(3)) [F]

- **Winkelwahl (mechanisch, Modus wahl):**
  - Plan: theta_max(P10) > 450 und Vorwaertsast gueltig bei 450 -> {420, 450}. Sonst der groesste gueltige Rasterwinkel
    in {390, 420}. Gibt es keinen, entfaellt der Stoss nach Plan.
  - Wortlaut: dieselbe Regel mit theta_max(P30) und nur der Sonde.
  - Gerechnet wird die Vereinigung beider Winkelmengen. Die Zustaende stammen immer aus P10 (wie GFS1, dessen Zustaende
    aus dem 10-Grad-Protokoll stammen).
  - Liegt kein Rasterwinkel ueber 360 gueltig vor, gibt es keinen Stoss; GF2 gilt dann als nicht eingetroffen ("kein
    gueltiger Ast ueber 360").
- **Stoss:** wortgleich GFS1 (stab.kipp auf Netz umgestellt): innere Haelfte h >= 1/2, delta = eps sin(pi f_i),
  f_i = clip(2h - 1, 0, 1), q -> q_s q_y(delta) q_s^-1 q q_y(-delta), q_s = q_z(theta/2); eps = 0,01, 0,1, 0,3.
- **Relaxation:** FIRE bis 3000 Schritte wie GFS1 (fire_log), Sonde an jedem Schritt.
- **Referenzen (urteilsbildend):** FIRE 3000 ab dem P10-Zustand bei 720 - theta ohne Stoss; E_ref := E am Ende. Gueltig
  nur mit Sonde im Lauf > 0.
- **Zusatz (beschreibend):** Kontrolle eps = 0 je Stosswinkel (zerfaellt der Ast von selbst?).

## 6. Teil C: SO(2)-Kontrolle auf dem Diamant-Netz [F]

- SO(2)-Feld phi (Werte in R), P10 bis 720 Grad, Saat [42, 2, 120, 24, 4]; Rauschen wie g2 (Normalverteilung 1e-3).
- Bei 420 und 450 Grad (fest, wie die Karte) der einzige moegliche Stoss: phi -> phi + delta auf den freien Knoten der
  inneren Haelfte, delta wie in Teil B (eps = 0,01, 0,1, 0,3); eine Kipprichtung gibt es nicht [M]. Dann FIRE 3000.
- **Zusatz (beschreibend):** eps = 0 je Winkel; SO(2) P10 auf Z^3 (Saat [42, 2, 120, 24]) fuer den Vergleich der
  Sprunggrenzen.

## 7. Urteilsregeln [F] (mechanisch in code/auswertung_fn.py)

**Klassen je SO(3)-Stoss (Teil B):** rho := (E_end - E_ref)/(E_Ast - E_ref), E_Ast = E des P10-Zustands vor dem Stoss.

| Klasse | nach Plan | nach Kartenwortlaut |
|---|---|---|
| sprung | Sonde im Lauf <= 0 (einschliesslich Zustand nach dem Stoss) oder P10-Ast bei theta nicht gueltig | Sonde im Lauf <= 0 oder laufende P10-Sonde bis theta <= 0 |
| umgekehrt | kein Sprung, rho <= 0,10 und qz_mittel_aussen am Ende < 0 | kein Sprung und abs(E_end - E_ref) <= 1e-6 E_ref (Karte GF2) |
| ast | kein Sprung, rho >= 0,90 und P_end <= P_0 | (keine eigene Klasse) |
| sonst | dazwischen | nicht umgekehrt |

**Klassen je SO(2)-Stoss (Teil C):**

| Klasse | nach Plan | nach Kartenwortlaut |
|---|---|---|
| sprung | laufende Protokoll-Sonde bis theta >= pi oder Sonde im Lauf >= pi | (keine eigene Klasse) |
| bleibt | kein Sprung und E_end >= 0,90 E_vor | E_end >= 0,90 E_vor |
| entdrillt | kein Sprung und E_end < 0,90 E_vor | E_end < 0,90 E_vor |

**Vorhersagen:**

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| GF0 | eingetroffen: K0 nach Plan eingetroffen und alle sechs SO(2)-Stoesse "bleibt"; sonst nicht eingetroffen | K0 nach Wortlaut und kein SO(2)-Stoss "entdrillt" |
| GF1 | eingetroffen: theta_max(P10) > 450 und Vorwaertsast gueltig bei 450; sonst nicht eingetroffen | theta_max(P30) > 450 |
| GF2 | eingetroffen: an jedem Plan-Winkel mindestens 2 von 3 Stoessen "umgekehrt"; nicht eingetroffen: sonst oder kein Plan-Winkel | dasselbe mit Wortlaut-Winkeln und Wortlaut-Klassen |

- Fehlt eine Datei oder eine gueltige Referenz, lautet das betroffene Urteil "nicht auswertbar".
- **Beschreibend:** theta_max auf 10 Grad genau; E und Sonde ueber theta (beide Netze, P10 und P30, SO(2));
  E_Diamant/E_Z3 bei 90 Grad gegen den Kontinuumswert 1/2 [M]; je Stoss E bei den Schritten 0, 250, 500, ..., 3000,
  erster Sprungschritt, P_max mit Schritt; Kontrollen eps = 0.
- **Bilder:** lauf/energie-verlauf.png (E, Sonde, P ueber die FIRE-Schritte je Stosswinkel, Diamant) und
  lauf/vorwaertsast.png (E und Sonde ueber theta, Diamant gegen Z^3, P10 und P30, SO(3) und SO(2)).

## 8. Laufplan [F]

- Nur .69, ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu6 und cpu7. Je Lauf <= 10 min
  (RuntimeMaxSec 600), 1 Thread, Logs mit absolutem Pfad. Ordner /home/fmh/fmhc-physics-remote/guertel-finn-netz-1/
  (code/, rauch/, lauf/, eingaben-gfs1/).
- **Rauchlauf:** Protokolle bis 60 Grad (P10 Diamant und Z^3, P30 Diamant, SO(2) Diamant), Stoss und Referenz bei 30
  und 60 Grad mit 100 FIRE-Schritten, Wahl und Auswertung mit Testparametern. Kein Wert ueber 60 Grad wird dabei erzeugt
  oder angesehen. Gemessen werden Laufzeit je FIRE-Schritt und Knotenzahlen.
- **Hauptlaeufe** (eingefrorener Code, je genau einmal):
  - cpu7: P30 Diamant; K0 (P10 Z^3); P30 Z^3; SO(2) P10 Diamant; SO(2)-Stoesse 420 und 450 (eps 0,01, 0,1, 0,3, 0);
    Zusatz SO(2) P10 Z^3.
  - cpu6: P10 Diamant; wartet auf P30 Diamant; Wahl; SO(3)-Stoesse je Winkel und eps; Referenzen; Kontrollen eps = 0.
  - Danach die Auswertung auf cpu6.
- Bricht ein Lauf ab (Zeit, Absturz), wird er mit Grund als Nachtrag wiederholt; seine Werte sehe ich vorher nicht an.

## Rauchlauf und Festlegungen vor dem Einfrieren [R]

- **Laeufe (.69, UTC):** Rauchlauf 1 von 19:37:47 bis 19:38:21 auf cpu6 und cpu7, 16 Units, alle rc = 0 (ketten/
  rauch-cpu6.sh, rauch-cpu7.sh). Rauchlauf 2 (nur Wahl und Auswertung nach der Korrektur) 19:40:26 bis 19:40:29 auf
  cpu6, rc = 0 (ketten/rauch2-cpu6.sh). Gesehen habe ich nur Knotenzahlen, Laufzeiten, Codepfade und Werte bis 60 Grad.
- **Netz:**
  - Diamant: N = 65441, frei 50632, Kern 7193, Rand 7616, 127508 Bindungen; jeder freie Knoten hat Grad 4,
    Bindungslaenge 0,866 (sqrt(3)/2). Innere Haelfte (h >= 1/2): 10024 freie Knoten.
  - Z^3 aus finn.py: N = 65267, frei 50624, Kern 7153, Rand 7490 (wie GFS1); Platz- und Bindungsaufbau gleich g2.Feld
    (z3_gleich_g2 = true). Innere Haelfte 9924.
  - Freie Knoten weichen um 8 von 50624 ab, weit unter 2 %. R bleibt 24.
- **Laufzeit (Rauchlauf):** Protokoll P10 bis 60 Grad (480 FIRE-Schritte) 9,4 s Diamant, 10,6 s Z^3, also etwa 20 ms je
  Schritt. P30 bis 60 Grad 2,8 s bzw. 3,6 s; SO(2) 1,7 s bzw. 2,1 s; Stoss mit 100 Schritten 4,5 s einschliesslich
  Aufbau. Erwartet fuer die Hauptlaeufe: P10 bis 720 Grad (etwa 3660 Schritte) 1,5 bis 4 min je nach Last (GFS1 hatte
  60 ms je Schritt), Stoss hoechstens 3000 Schritte, also unter 3 min. Alles unter 10 min.
- **Werte bis 60 Grad:** E(60) im P10-Protokoll 155,8 (Diamant) gegen 307,9 (Z^3), passend zur Kontinuumsabschaetzung 1/2
  in Abschnitt 0.4. Stoss eps = 0,3 bei 30 und 60 Grad: Klasse "ast" (zurueck auf den Ast, wie unterhalb 360 Grad
  erwartet); SO(2) bei 60 Grad: "bleibt".
- **Korrektur nach Rauchlauf 1 (Code):**
  - finn.gueltig_plan prueft den Drehsinn aussen nur noch fuer Rasterwinkel > 0. Vorher fiel jeder Vorwaertsast am
    Rasterwinkel 0 durch (qz_mittel_aussen = 0), und alle Plan-Gueltigkeiten waren falsch. Abschnitt 3 ist entsprechend
    ergaenzt.
  - auswertung_fn.py: Fehlt P10 bzw. P30, lautet GF2 nach Plan bzw. Wortlaut "nicht auswertbar" statt "nicht
    eingetroffen". Diese Aenderung lag vor der Auswertung von Rauchlauf 1 auf der .69 noch nicht vor; geprueft in
    Rauchlauf 2.
- **Bilder:** Aufbau wie geplant. Die SO(2)-Kurven liegen unter den SO(3)-Kurven (Abschnitt 0.2).
- **Hauptketten:** ketten/lauf-cpu6.sh und ketten/lauf-cpu7.sh setzen Abschnitt 8 um. Stossnamen tragen eps als Index
  (e1, e2, e3), weil Punkte in Unit-Namen stoeren koennen.
- Sonst keine Aenderung an Plan oder Code nach dem Rauchlauf.
