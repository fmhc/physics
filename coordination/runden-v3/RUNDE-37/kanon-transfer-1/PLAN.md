# KANON-TRANSFER-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 49)

- Start 2026-10-05 14:40:52 CEST (date). Plantext ab 2026-10-05 14:54:29 CEST (date), vor jeder Rechnung und vor jedem
  Rauchtest. Zeitbox 120 min, also bis 16:40:52 CEST. Die .69 laeuft in UTC (CEST = UTC + 2).
- Grundlage: KARTE.md (KT0 bis KT3, Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert; nicht geaendert).
- Kennzeichen: [M] vorab ableitbar (eigene Mathematik, nicht gegengelesen), [E] hier gerechnet, [P] Projektdatei,
  [F] eigene Festlegung, [H] Hypothese oder Lesart. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 1. Code [F]

- Unveraendert kopiert aus RUNDE-37/uebergabe-konfluenz-1/code (Summen gleich den dort eingefrorenen): konfluenz.py
  (56f9a6f0...), td.py (fbc02c48...), hm_td.py (c62c15ab...), tg.py (ec48a258...), uk.py (f52df743...), tu.py (6c5c3a95...),
  tp.py, ew.py, mn.py, tg_auswertung.py, kette.sh (nur Vorlage, nicht benutzt). Dort nichts geaendert.
- Neu (Erweiterung der Kopien): code/kanon.py importiert diese Module unveraendert; code/kette_kt.sh startet die Laeufe.
  Modulgroessen wie konfluenz.MU_ZIEL und hm_td.VREF werden nur zur Laufzeit gesetzt, die Dateien bleiben gleich.
- Eingabe: eingabe/konfluenz-s1..s4.json, Kopien von uebergabe-konfluenz-1/lauf-69 (sha256 gleich lauf-69/PRUEFSUMMEN.txt:
  65eb52ed..., 7219844..., e1c0b353..., d48ab365...). Gelesen werden nur Fallbeschreibungen (X, Y, Art, verschobene Ecken
  und Verschiebungen, gespeicherte erste Zuege), keine Energien oder Abstaende aus UEBERGABE-KONFLUENZ-1.

## 2. Ist *0 im kopierten Code das umkreisbasierte (Voronoi-)Dual? [M, P]

- Ja. konfluenz.skalar_ops bildet *0 je Ecke aus tu.hodge: A*_e,t = 1/2 Summe ueber die zwei Nachbarflaechen von
  (Kantenmitte -> Flaechenumkreismitte) x (Flaechenumkreismitte -> Umkugelmitte), vorzeichenbehaftet; *0_v = Summe
  l_e A*_e,t / 6 ueber die Kanten an v (Pyramiden ueber den Dualflaechen). Das ist das umkreisbasierte Dual (Hirani-Art);
  in einer Delaunay-Zerlegung ist es die Voronoi-Zelle.
- Folge [M]: Bei exakter Kosphaerizitaet der 5 Ecken haben alle Tetraeder der Doppelpyramide (2 alt, 3 neu) dieselbe
  Umkugelmitte. Die Beitraege innerer Flaechen heben sich paarweise weg (gegenlaeufige Normalen), es bleiben nur die
  6 Randflaechen und die 9 Randkanten, die in beiden Zerlegungen gleich sind. Also *0'_v = *0_v, D_v = 1. Der Satz der
  Karte gilt im Code; KT0 wird ohne Sonderregel geurteilt.
- Kontrolle [E]: *0 aus den Kantenlaengen (td.tet_X_aus_laengen + td.hodge_teile, dieselben Formeln) gleich *0 aus
  den Lagen auf 1e-10 relativ.

## 3. Faelle, mu-Raster und Zuege [F]

- Faelle: die 32 gespeicherten Faelle (11 D, 1 T, 20 K; Saaten 1 bis 4), Netze tg.zufallsnetz(128, s).
- **mu = -1e-3:** Hintergrundlagen = gespeicherte Lagen plus gespeicherte Verschiebung an den gespeicherten Ecken.
  Kontrolle: mu_X, mu_Y gleich den gespeicherten auf 1e-12 (absolut); genau X und Y verletzt.
- **mu = -1e-4:** dieselben Ecken und dasselbe Schema (eine gemeinsame Ecke mit beiden Gleichungen, oder je eine Ecke
  fuer X bzw. Y), konfluenz.newton mit MU_ZIEL = 1e-4 (Gauss-Newton, Mindestnorm, Start bei null Verschiebung, auf dem
  unverschobenen Netz). Gueltig, wenn wie in UEBERGABE-KONFLUENZ-1: genau X und Y verletzt (mu < -1e-9), kein
  Tetraeder kehrt sein Vorzeichen um, X und Y je als 2-3 ausfuehrbar, Verschiebung je Ecke <= 0,1 l. Ungueltige Faelle
  fallen bei -1e-4 heraus (Zahl ausgewiesen); ihre Werte bei -1e-3 bleiben.
- **Zuege:** X und Y je als erster Zug auf der Ausgangszerlegung des verschobenen Netzes (= die gespeicherten ersten
  Zuege von XY bzw. YX; alle 2-3). Ausfuehrung konfluenz.zug_waehlen -> td.zug_ausfuehren (unveraendert). Kontrolle:
  Typ 2-3 und Schluessel der neuen Kante gleich dem gespeicherten. Spaetere Zuege der Ketten (nur der T-Fall der Saat 1
  hat welche) werden nicht ausgewertet. Stichprobe je mu: 64 Zuege (32 X, 32 Y).
- Begruendung: Die Karte fragt nach dem Fehler "am Umklappzug"; die Zustaende sind "um den Zug" bzw. "an den
  Zug-Ecken" festgelegt. Ein Einzelzug mit kontrolliertem mu ist dafuer die kleinste saubere Einheit.

## 4. Zustaende [F]

- **Skalar auf den Ecken** (komplex = zwei reelle Felder; dphi/dt = pi / *0):
  H_phi = Summe_v |pi_v|^2 / (2 *0_v) + m^2/2 Summe_v *0_v |phi_v|^2 + Z_S/2 Summe_e *1_e |phi_b - phi_a|^2, Z_S = 8,
  *0 und *1 aus konfluenz.skalar_ops (Hintergrundlagen, aktuelle Zerlegung). Lokale Ladung Q_v = Im(conj(phi_v) pi_v).
  Testfeld; Rueckwirkung nur ueber den Rueckstoss von K (Abschnitt 5).
- **Z1 (KT1, masselos, reell):** m = 0. Welle wie UEBERGABE-KONFLUENZ-1: phi_v = A cos(k1 . r_v + p0),
  pi_v = *0_v A |k1| sin(k1 . r_v + p0), k1 = 2 pi (erste Zeile von LV^-T), A = 1e-3. Phase p0 je Zug so, dass
  k1 . r_c + p0 = pi/4 (r_c = Mittelpunkt der 5 Zug-Ecken, ungefaltet im Rahmen des ersten alten Tetraeders). Dann sind
  phi und pi an den Zug-Ecken im Allgemeinen beide ungleich null; min |cos| und min |sin| an den Zug-Ecken werden
  ausgewiesen.
- **Z2 (KT2, massiv, komplex):** m = 1, omega = 0,8 m, phi_v = A f_v exp(i k1 . r_v), pi_v = i omega *0_v phi_v
  (Zeitpunkt t = 0), A = 1e-3. Gauss-Profil f_v = exp(-d_v^2 / (2 sigma^2)), sigma = 3 l (l = mittlere Kantenlaenge des
  unverschobenen Netzes, wie konfluenz.lauf), d_v = Abstand zu r_c im naechsten Bild (Mindestbild im Kasten).
  - Hinweis [E aus tg.zufallsnetz, keine Kennzahl]: Kasten L = 128^(1/3) = 5,04, l etwa 1,28, also sigma etwa 0,76 L.
    Das Profil ist breit (in der Kastenecke f etwa 0,5) und hat an den Grenzen des Mindestbilds einen Knick. Der Knick
    liegt fern vom Zug und wirkt nur auf H_phi im Nenner, nicht auf den Sprung.
  - Re(conj(pi) phi) = 0 an jeder Ecke (exakt), also kein Rueckstoss [M].
- **Geometrie (KT3 und Rueckstossenergie):** Form A2 (hm_td, KIN = A2, RED = R1; VREF = Kastenvolumen / Tetraederzahl,
  je Fall und mu einmal gesetzt). TT-Mode wie UEBERGABE-KONFLUENZ-1: td.tt_mode mit TT-Amplitude A_Q = 1e-3,
  x0 = sin(1) x_Mode, y0 = A_red^-1 omega cos(1) x_Mode. H_geo = 1/2 y^T A_red y + 1/2 x^T B_red x (N.energie).
  A_red muss im Ausgangsnetz und nach dem Zug positiv definit sein (sonst Zug fuer KT3 nicht gewertet, ausgewiesen).
- **Skalar-Amplitude fuer KT3 (Regel):** je Zug, Zustand und mu A_s = A x Wurzel(H_geo,0 / H_phi,0(A)), also
  H_phi / H_geo = 1 im Anfangszustand (liegt in [0,3; 3]). Das Verhaeltnis wird ausgewiesen.

## 5. Transfers und Rueckstoss [F, M]

- D_v = *0'_v / *0_v je Ecke (*0' nach dem Zug). Ausserhalb der 5 Zug-Ecken ist D_v = 1 bis auf Rundung (Kontrolle).
- R: phi' = phi, pi' = D pi. P: phi' = phi, pi' = pi. K: phi' = D^(-1/2) phi, pi' = D^(1/2) pi.
- Rueckstoss bei K: dp_a = Summe_v (c_v / 2) d ln D_v / d a, c_v = Re(conj(pi_v) phi_v) (unter K unveraendert [M]),
  a_e = dl_e / l_e. **Konvention [F]:** Der Kovektor wird im Kantenraum der neuen Zerlegung gebildet (neue Kante d-e als
  eigene Koordinate; *0 der alten Zerlegung haengt nur von den alten Kanten ab) und nach dem geometrischen Transfer
  (Lesart R oder P, td.abbilden unveraendert) addiert: y' -> y' + S'^T dp_a. Rueckstossenergie
  E_rec = H_geo'(x', y' + S'^T dp_a) - H_geo'(x', y'). Die Variante "vor dem Transfer im alten Raum mit flacher
  Fortsetzung der neuen Kante" wird nicht gerechnet.
- **d ln D_v / d a [F]:** Ableitung der Beitraege je Tetraeder zu *0_v aus den 6 Laengen nach a_e = dl_e / l_e, fuer
  alte und neue Zerlegung, am Hintergrund (a = 0), fuer die 5 Zug-Ecken.
  - **Geaendert nach Rauchtest r1 (vor dem Einfrieren):** Zuerst geplant waren zentrale Differenzen in den Laengen
    (h = 1e-4 und 1e-5). r1 brach ab (LinAlgError "Singular matrix" in tu.umkreis_tet): Bei flachen Tetraedern
    (Splittern) sind die gestoerten Laengen nicht mehr einbettbar, td.tet_X_aus_laengen setzt dann z = 0.
  - **Jetzt:** komplexer Schritt (a_e -> a_e + i 1e-20) durch dieselben Formeln wie td.tet_X_aus_laengen und
    td.hodge_teile, nur komplex fortsetzbar geschrieben (Norm als Wurzel der Quadratsumme, Vorzeichen vom Realteil,
    kein np.maximum). Das ist die exakte Ableitung der Formel bis auf Rundung, ohne Differenzenfehler ("analytisch"
    im Sinne der Karte, algorithmisch gebildet).
  - Gegenprobe mit zwei Schrittweiten: Jede der 5 Zug-Ecken wird in einer festen Zufallsrichtung verschoben (Saat 4911);
    d *0_v / dt aus den Lagen (zentrale Differenzen, t = 1e-5 l und 1e-6 l) gegen die Kettenregel mit der Ableitung
    nach a, je in alter und neuer Zerlegung. Soll: Abweichung <= 1e-6 relativ, Schrittweiten untereinander <= 1e-6.
  - Homogenitaet Summe_e d ln *0_v / d a_e = 3 (Grad 3 in den Laengen) auf 1e-10; *0 aus Laengen gleich *0 aus Lagen auf
    1e-10.
- **Hinweis [M, nicht gegengelesen]:** D_v - 1 verschwindet auf der Kosphaerizitaetsflaeche, seine Ableitung quer dazu
  aber im Allgemeinen nicht. Der Rueckstoss von K bleibt also endlich, wenn mu -> 0 geht, waehrend die
  Feldblock-Unterschiede mit mu schrumpfen. Beschreibend gerechnet: |dp_a| bei -1e-3 und -1e-4. Das ist eine Lesehilfe
  fuer KT3, kein Urteil.

## 6. Messgroessen je Zug [F]

- D - 1 an den 5 Zug-Ecken, max |D - 1| je Zug; Volumenerhalt Summe_v (*0'_v - *0_v) (relativ zum Volumen der
  Doppelpyramide).
- Delta H_phi(T) = H_phi'(nach Transfer T, neue *0', *1') - H_phi(vorher), zerlegt in kinetisch, Masse, Gradient; der
  Gradient weiter in "*1-Teil" G(*1', phi) - G(*1, phi) (fuer R und P der ganze Gradiententeil) und "Umskalierung"
  G(*1', phi') - G(*1', phi) (nur K). Relativ: rel_T = |Delta H_phi(T)| / H_phi,0.
- Geometrie: Delta H_geo(L) = H_geo'(x', y') - H_geo(x0, y0) fuer L = R, P (Form A2).
- Gesamt fuer KT3 (Amplitude A_s): Delta H_ges(L, T) = Delta H_geo(L) + Delta H_phi(T) + [T = K] E_rec(L).
- Ladung (Z2): Gesamtladung vorher und nachher je Transfer (Quellenabweichung).
- Anteile im Anfangszustand: H_phi zerlegt (kinetisch, Masse, Gradient), Anteil der 5 Zug-Ecken samt anliegender Kanten;
  fuer KT3 zusaetzlich H_geo (kinetisch, potentiell) gegen H_phi.

## 7. Kontrollen [M]-Saetze (KT0) und weitere [F]

- Je Zug, mu, Transfer (fuer Z1 und Z2 dort, wo die Groesse ungleich null ist):
  - Feldblock: Jacobi-Matrizen des Transfercodes (angewandt auf Einheitsvektoren), Klammer {phi'_v, pi'_w} =
    J_phiphi J_pipi^T - J_phipi J_piphi^T gegen diag(D) (R) bzw. Einheit (P, K).
  - kinetisch je Ecke gegen D, 1/D, 1 mal vorher (R, P, K); Masse je Ecke (Z2) gegen D, D, 1; lokale Ladung (Z2) gegen
    D, 1, 1.
  - K: Wurzel(*0) phi und pi / Wurzel(*0) stetig.
  - Fehlermass: max |ist - soll| / |soll| ueber Ecken mit soll ungleich null; Eintraege mit soll = 0 absolut gegen das
    Maximum von |soll|.
- Weitere Kontrollen (kein Urteil): Wiedergabe von mu_X, mu_Y; *0 aus Laengen gegen Lagen; Ableitungs-Gegenproben
  (Abschnitt 5); D - 1 ausserhalb der Zug-Ecken; Volumenerhalt; H_phi/H_geo = 1 fuer KT3; A_red positiv definit;
  Rueckstoss fuer Z2 gleich null.

## 8. Urteilsregeln (mechanisch, code/kanon.py auswertung)

- Stichprobe nach Plan: alle gueltigen Zuege (X und Y) bei mu = -1e-3, n = 64 erwartet. Wortlaut-Pruefung von KT1 bis
  KT3: nur die X-Zuege (ein Zug je Fall, n = 32), sonst gleich. Fehlen Zuege, werden die vorhandenen gewertet und die
  Zahl vermerkt; ohne Zug "nicht entscheidbar".
- **KT0** (Plan = Wortlaut): eingetroffen, wenn (i) alle Fehler aus Abschnitt 7 (Feldblock, kinetisch, Masse, Ladung)
  ueber alle Zuege, beide mu, Z1 und Z2, R/P/K <= 1e-12 sind und (ii) r_D = max |D - 1| bei -1e-3 / max |D - 1| bei
  -1e-4 in [8; 12] liegt (Maximum ueber die 5 Zug-Ecken aller Zuege, die bei beiden mu gueltig sind). Sonst verfehlt.
  Kein gepaarter Zug: (ii) nicht entscheidbar, dann KT0 nicht entscheidbar, wenn (i) gilt, sonst verfehlt.
- **KT1** (Z1, mu = -1e-3): m_T = Median von rel_T. Eingetroffen, wenn m_K <= 0,5 x min(m_R, m_P), sonst verfehlt.
- **KT2** (Z2, mu = -1e-3): eingetroffen, wenn 10 x m_K <= min(m_R, m_P), sonst verfehlt.
- **KT3** (mu = -1e-3, Form A2, Amplitude A_s): M(L, T) = Median von |Delta H_ges(L, T)| (absolut). Basis wie
  UEBERGABE-KONFLUENZ-1 (Geometrie und Skalar in derselben Lesart): L* = die Lesart mit kleinerem M(L, L).
  Bedingung: M(L*, K) >= M(L*, L*) / 2 ("mit K hoechstens 2-mal kleiner"; auch erfuellt, wenn K groesser ist).
  - nach Plan: Zustand Z2 (Q-Ball-artig; der Fall, fuer den K gedacht ist und auf den die Grundgleichung v2.5 3.2 zielt).
    Bedingung erfuellt -> eingetroffen, sonst verfehlt.
  - nach Kartenwortlaut: Die Karte nennt keinen Zustand, also muss die Bedingung fuer Z1 und Z2 gelten -> eingetroffen,
    sonst verfehlt (X-Zuege, n = 32).
  - Beschreibend: M(L, K) auch mit der jeweils anderen Lesart der Geometrie; Werte fuer Z1 nach Plan-Stichprobe.
- Alle Urteile stehen in lauf-69/auswertung.json; Zahlen dort sind die Grundlage von ERGEBNIS.md.

## 9. Ableitbarkeit vorab (eigene Pruefung) [M, nicht gegengelesen]

- KT0 (i) ist vorab ableitbar (diagonale Faktoren); die Rechnung prueft nur die Umsetzung. KT0 (ii) folgt aus Abschnitt
  2 in erster Ordnung (D - 1 proportional zu mu bei fester Gestalt der Doppelpyramide); offen bleibt, ob die
  -1e-4-Netze dieselbe Gestalt behalten.
- Volumenerhalt: Summe_v (D_v - 1) *0_v = 0 [M] (gleiche Vereinigung der Tetraeder). Fuer Z2 mit fast gleichem |phi|^2
  an den 5 Ecken heben sich deshalb kinetischer und Massenteil bei R und P weitgehend weg; bei K ist der
  Umskalierungsteil des Gradienten nicht so gebunden. Die Rangfolge ist damit nicht ableitbar (wie die Karte sagt).
- Fuer Z2 gilt Re(conj(pi) phi) = 0, also E_rec = 0 [M]: KT3 nach Plan vergleicht nur den Feldblock-Teil.

## 10. Agenten-Erwartungen (vorab; gehen in kein Urteil ein)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| E1 | KT0 eingetroffen | 85 % |
| E2 | KT1 eingetroffen (K mindestens halbiert) | 20 % |
| E3 | KT2 eingetroffen (K mindestens 10-mal kleiner) | 20 % |
| E4 | KT3 nach Plan eingetroffen | 85 % |
| E5 | Median |dp_a|(-1e-3) / |dp_a|(-1e-4) fuer Z1 zwischen 0,5 und 2 | 80 % |
| E6 | Median |Delta H_geo(R)| > Median |Delta H_phi(T)| fuer alle T (KT3-Amplitude, Z1 und Z2) | 75 % |

## 11. Laeufe auf der .69 (kleintest.sh, nur Spuren cpu5 und cpu6, <= 600 s je Aufruf)

- Arbeitsordner /home/fmh/fmhc-physics-remote/kanon-transfer-1/ (code/, eingabe/, lauf/, rauch/).
- code/kette_kt.sh (einmal je Spur per ssh mit setsid nohup gestartet; kein Dienst, kein Timer):
  - cpu5: lauf Saat 1, dann Saat 3; cpu6: lauf Saat 2, dann Saat 4;
  - danach auf cpu5: auswertung und tabellen, Pruefsummen.
- Schlusszeit: nach 16:15 CEST (14:15 UTC) startet kein neuer Aufruf.

## 12. Rauchtests (nur Technik)

- r1: cpu5, Saat 1, --rauch (nur der erste Fall, beide mu, beide Zuege). Ausgabe nur Schluessel, Laufzeiten und
  technische Kontrollen (Wiedergabe mu_X, *0 Laengen gegen Lagen, Ableitungs-Gegenproben, Gueltigkeit bei -1e-4). Keine
  Energien, keine D-Werte, keine Urteilsgroessen.
- r2: cpu5, auswertung und tabellen auf einer Rauch-Ausgabe mit voller Ausgabe (Saat 901, 1 Fall, nach rauch/).
  Gelesen werden nur rc, Schluessel der Urteile und Zeilenzahl der Tabelle; die Werte nicht.
- Weitere Rauchtests nur nach Fehlern, mit derselben Lesebeschraenkung; alle werden in Abschnitt 13 nachgetragen
  (vor dem Einfrieren).

## 13. Rauchtests (Nachtrag vor dem Einfrieren; .69 in UTC)

- r1 (13:00:38 bis 13:00:43, cpu5, Saat 1, --rauch): rc = 1, LinAlgError in den zentralen Differenzen (Abschnitt 5).
  Gelesen: nur der Traceback.
- Danach geaendert: Ableitung per komplexem Schritt, Gegenprobe ueber Eckverschiebungen (Abschnitt 5).
- r1b (13:04:00 bis 13:04:09, cpu5, Saat 1, --rauch, erster Fall D, beide mu): rc = 0, 8,8 s. Gelesen nur die
  technischen Kontrollen: Wiedergabe mu 0,0; Fall bei -1e-4 gueltig; A2 positiv definit; neue Kante gleich; Lagen-Probe
  1,3e-9 bis 5,8e-9; Schrittweiten 5,2e-9 bis 4,9e-8; Homogenitaet <= 7,7e-13; *0 Laengen gegen Lagen <= 2,9e-14;
  Zeiten je Zug etwa 1,5 s. Keine Energien, keine D-Werte, keine Urteilsgroessen.
- r2a (13:04:21 bis 13:04:47, cpu5, Rauchsaat 901, alle 3 Faelle der Rauch-Eingabe aus UEBERGABE-KONFLUENZ-1, volle
  Ausgabe nach rauch/kanon-s901.json; Plan 12 nannte "1 Fall", es waren 3): rc = 0, 25,0 s. Nicht gelesen.
- r2b, r2c (13:04:47 bis 13:04:49, cpu5): auswertung und tabellen auf rauch/: rc = 0. Gelesen: nur die Schluessel der
  Urteile und der Zusammenfassung, die Zahl der Eintraege (12) und die Zeilenzahl der Tabelle (232).
- Danach geaendert: KT3 wertet nur Zuege, deren A_red(A2) auch nach dem Zug positiv definit ist (so in Abschnitt 4
  schon festgelegt, im Code nachgezogen).
- r3a, r3b (13:05:34 bis 13:05:35, cpu5): auswertung und tabellen auf rauch/ mit dem Endstand: rc = 0; gelesen nur rc
  und Zeilenzahl (232).
- Schaetzung: etwa 8,5 s je Fall (beide mu), also 1 bis 1,5 min je Saat.
