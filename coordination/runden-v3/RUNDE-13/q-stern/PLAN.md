# Q-STERN: Plan (Runde 13, Code-Agent)

- Auftrag der Leitung claude-primary; Start 2026-10-01 20:13:46 CEST (date), Zeitbox 75 min (bis ~21:28).
- Bindend: KARTE.md (Modell, Kontrollen, Regel, Vorhersage). Zusatz der Leitung: nur Spuren cpu und cpu2.
- Grundlage: RUNDE-13/bball-leiter/bball2.py, kopiert als qstern.py; Diff qstern.diff (wird vor dem Einfrieren
  erzeugt, sha256 im Ergebnis).

## 1 Herleitungsstand (Einzelheiten HERLEITUNG.md)

- Wirkung bis erste Ordnung in Phi: sqrt(-g) = 1 - 2 Phi, g^tt = -(1 - 2 Phi), g^ij = (1 + 2 Phi) delta_ij. Daraus
  L = (1 - 4 Phi)|d_t phi|^2 - |grad phi|^2 - (1 - 2 Phi) U. Stimmt mit der Karte ueberein.
- Feldgleichung (statisches Phi): lap phi = (1 - 4 Phi) d_t^2 phi + (1 - 2 Phi) U'(|phi|^2) phi. Mit
  phi = f e^{-i omega t}: f'' + (2/r) f' = (1 - 2 Phi) U' f - (1 - 4 Phi) omega^2 f. Stimmt mit der Karte.
- Poisson: Phi'' + (2/r) Phi' = alpha rho_E, rho_E = omega^2 f^2 + f'^2 + U, wie Karte (bindend). Vermerk: Eine
  Variation derselben Wirkung nach einem einzigen Phi gaebe die Quelle rho + 3 p = 4 omega^2 f^2 - 2 U (linearisierte
  ART: g_00-Potential aus rho + 3 p, g_ij-Potential aus rho). Die Karte waehlt den Newton-Grenzfall mit rho_E; das
  bleibt die Regelfassung. Keine Abweichung in der Herleitung der Karte selbst; die Quellenwahl wird als Grenze
  gefuehrt. Ein Nebenlauf mit rho + 3 p ist NICHT geplant (Zeit).
- Linearisierung (Cowling, delta Phi = 0), phi = e^{-i omega t}(f + a e^{-i rho t} + b* e^{i rho t}), l = 0, y = r w:
  - offener Kanal a (omega + rho): y_a'' = [(1 - 2 Phi) dp - (1 - 4 Phi)(rho + omega)^2] y_a + (1 - 2 Phi) sp y_b
  - geschlossener Kanal b (omega - rho): y_b'' = [(1 - 2 Phi) dp - (1 - 4 Phi)(rho - omega)^2] y_b + (1 - 2 Phi) sp y_a
  - dp = U' + S U'', sp = S U''. Im Code: A = (1 - 2 Phi) dp - (1 - 4 Phi) omega^2, B = 2 omega (1 - 4 Phi),
    C = (1 - 2 Phi) sp, D = 1 - 4 Phi; Kanal 1 (geschlossen): A + B rho - D rho^2, Kanal 2 (offen): A - B rho - D rho^2.
    Neu gegenueber bball2: D vor rho^2. Schwellen 1 -+ omega (Phi(inf) = 0).
- Langreichweite / Coulomb-Phase: W = L(y_a) + i L(y_b) mit z = Loesung, die bei R im geschlossenen Kanal abklingt
  und im offenen Kanal exakt null ist (z2 = z2' = 0). Ausserhalb des Balls ist C ~ f^2 < 1e-12; Phi ist diagonal und
  koppelt die Kanaele nicht. Darum ist z2 fuer r >= R exakt null, und W = 0 heisst: es gibt eine regulaere Loesung
  ohne jeden offenen Anteil. Die Coulomb-Phase des offenen Kanals geht nicht ein (Weg "Groesse ohne Phase"). Nur der
  Start von z1 haengt von Phi ab: z1'/z1 = -kappa_c + eta_c/R, eta_c = c (4 (rho - omega)^2 - 2)/(2 kappa_c),
  c = alpha m (Phi ~ -c/r); ein Restfehler klingt nach innen mit e^{-2 kappa_c (R - r_m)} ab. Pruefung K3.
- Hintergrund: Schiessen in f bei festem Phi (Klammer wie bball2, mit Ausweiten), Phi aus dem Poisson-Integral
  Phi(r) = -alpha [m(r)/r + int_r^inf rho r' dr'] (Trapez plus Euler-Maclaurin-Korrektur, O(h^4)), Feingitter per
  kubischem Spline, ausserhalb -c/r. alpha-Rampe in 6 Iterationen, danach Anderson(1)-Mischung; konvergiert, wenn
  max |Phi_neu - Phi_alt| < 1e-9. Schwanz f ~ e^{-kappa r} r^(eta - 1), eta = c (4 omega^2 - 2)/(2 kappa).
- Q = 8 pi omega int (1 - 4 Phi) f^2 r^2 dr (Noether-Ladung), E = 4 pi int rho_E r^2 dr (Masse der Quelle).

## 2 Rauchtests und Hintergrundpruefungen vor dem Einfrieren (lokal, System-python3, 1 Thread, nice 19, timeout)

- rauch-k2-a0.1 (h = 0,04, x = 0,8): erste Fassung ohne Rampe; Phi-Iteration lief aus der Klammer (bei festem Phi aus
  dem flachen Profil ueberschiessen alle Amplituden). Daraus: alpha-Rampe. 7,2 s.
- dbg1 (Klammerverlauf), dbg2/dbg3 (Rampe ohne/mit Anderson-Mischung, alpha = 0,1, x = 0,8, Profilschritt 0,02):
  einfache Mischung schwingt mit Faktor ~ -0,87; mit Anderson(1) 16 Iterationen, 23 s.
  Ergebnis alpha = 0,1, x = 0,8: f0 = 0,697462 (flach 1,022043), Phi(0) = -0,191892, 2|Phi(0)| = 0,384, Q = 76,90,
  E = 54,05, R_w = 2,327, Phi(R_w) = -0,145, eta = 0,577.
- rauch-orient-a0.1 (h = 0,04; Zeilen 0,70/0,75/0,80/0,85/0,90; n_mid 1; ohne Lokalisierung), 78 s:
  - Kompaktheit 2|Phi(0)| = 0,513 / 0,446 / 0,384 / 0,317 / 0,221; Newton-Grenzfall fraglich.
  - Ast der Stelle (Richtung +1): rho 1,597 / 1,638 / 1,698 / 1,785 / 1,879; s/median -2,4e-2 / -1,8e-2 / -3,3e-3 /
    -4,7e-5 / -1,2e-9, also ueberall negativ (bei alpha = 0 ist s unterhalb 0,7977 positiv). [H] Der s-Wechsel liegt
    bei alpha = 0,1 unter 0,70, also ausserhalb des Fensters.
  - Neu: ein Paar Nullstellen dicht unter der geschlossenen Schwelle (rho 1,80 bis 1,94; |s|/median 1e-4 bis 1e-11).
    [H] gravitativ gebundene Zustaende des geschlossenen Kanals im -c/r-Schwanz (Rydberg-artig).
  - Streifen 0,70 .. 0,85 je Umlauf +1, aufgeloest; Streifen 0,85 .. 0,90 nicht aufgeloest (oberer Rand, |W| ~ 1e-9).
- rauch-orient-a0.03 (wie oben), 78 s:
  - Kompaktheit 0,262 / 0,222 / 0,189 / 0,161 / 0,135.
  - Ast der Stelle: rho 1,641 / 1,668 / 1,697 / 1,742 / 1,819; s/median -7,3e-5 / -1,6e-2 / -2,2e-2 / -9,0e-3 /
    -4,2e-4. [H] Der s-Wechsel liegt bei alpha = 0,03 knapp unter oder bei 0,70.
  - Zwei s-Wechsel im schwellennahen Paar zwischen 0,700 und 0,725 (rho 1,82 bis 1,85).
  - Streifen 0,70 .. 0,75 Umlauf -1, 0,75 .. 0,80 Umlauf +1, 0,80 .. 0,85 Umlauf 0 (27 neue Profile am oberen Rand).
- Folge fuer die Zeilen: Fenster 0,70 .. 0,90 voll abdecken (sonst ist "Nicht gesehen" nicht entscheidbar), dicht
  (0,005) dort, wo die Stelle nach der Orientierung liegt (unterer Fensterrand fuer 0,1 und 0,03; fuer 0,01 linear
  geschaetzt um 0,78), sonst 0,01.
- Zeitmessung fuer die Laufliste: h = 0,04, 5 Zeilen ~15 s Profile (12 bis 15 Iterationen); h = 0,02 kostet etwa das
  Doppelte je Zeile, h = 0,01 das Vierfache. Erwartung je Teil-Lauf 2 bis 6 min; harte Grenze 10 min, --budget 540.

## 3 Zeilen und Gitter

- Stufen: h = 0,02 (Profilschritt 0,01) und h = 0,01 (Profilschritt 0,005), wie bball. K3: h = 0,02 mit --r-fak 1,5.
- Zeilen (omega^2), Teile (benachbarte Teile teilen ihre Randzeile):
  - alpha = 0,1 und 0,03:
    - pa: 0,700 0,705 0,710 0,715 0,720 0,725 0,730 0,735 0,740 0,745 0,750 (Abstand 0,005)
    - pb: 0,75 0,76 0,77 0,78 0,79 0,80 0,81 0,82
    - pc: 0,82 0,83 0,84 0,85 0,86 0,87 0,88 0,89 0,90
    - bei h = 0,01 je Teil in zwei Haelften: pa1 0,700..0,725, pa2 0,725..0,750, pb1 0,75..0,79, pb2 0,79..0,82,
      pc1 0,82..0,86, pc2 0,86..0,90
  - alpha = 0,01:
    - pa: 0,70 0,71 0,72 0,73 0,74 0,75 0,76
    - pb: 0,760 0,765 ... 0,820 (13 Zeilen, Abstand 0,005)
    - pc wie oben
    - bei h = 0,01: pa (ganz), pb1 0,760..0,790, pb2 0,790..0,820, pc1, pc2
- Je Lauf: n1 4000, n2 2000 (dicht 1,5 .. 1,95), n_mid 1, n_zw 1500, max_kand 6, rdx 4e-4, rdrho 2e-3, r_nx 5,
  pole nein, budget 540. Rechteck-Aufloesung wie bball2 (Sprung < 0,4 rad).
- K1: alpha = 0, Zeilen 0,785 .. 0,815 (7, wie bball), n_mid 2, beide Stufen.
- K2: qstern.py k2 je alpha, x = 0,75 / 0,80 / 0,85, h = 0,02 (Profilschritte 0,01 und 0,005).
- K3 (bedingt, vorab festgelegt): fuer jeden h-0,02-Teil, dessen JSON mindestens einen Kandidaten mit Rechteck-Umlauf
  ungleich 0 hat, derselbe Teil mit --r-fak 1,5 (Pruefung per jq im Starter).
- Nebenlauf (nicht regelrelevant, nur "wohin wandert sie", niedrigste Prioritaet): alpha = 0,1 und 0,03, h = 0,02,
  Zeilen 0,60 0,61 ... 0,70 (unter dem Fenster).

## 4 Laufliste (.69, kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde13-q-stern, Ausgaben aus/, Logs logs/)

- Zwei Starter, je einmal per nohup, jeder arbeitet seine Liste der Reihe nach ab:
  - start-cpu.sh (Spur cpu): k1-h0.02; a0.1-h0.02-pa/pb/pc; a0.1-h0.01-pc1/pc2; K3 alpha 0,1 (bedingt);
    a0.03-h0.02-pa/pb/pc; a0.03-h0.01-pc1/pc2; K3 alpha 0,03 (bedingt); a0.01-h0.02-pa/pb/pc; a0.01-h0.01-pc1/pc2;
    K3 alpha 0,01 (bedingt); Nebenlaeufe
  - start-cpu2.sh (Spur cpu2): k1-h0.01; k2-a0.1; a0.1-h0.01-pa1/pa2/pb1/pb2; k2-a0.03; a0.03-h0.01-pa1/pa2/pb1/pb2;
    k2-a0.01; a0.01-h0.01-pa/pb1/pb2
- Gemessene Dauer: siehe Abschnitt 2 (Rauchtests); Erwartung 2 bis 6 min je Teil. Was bis zum Ende der Zeitbox nicht
  gelaufen ist, gilt als "nicht gerechnet". Keine Laeufe werden vorsorglich abgebrochen.
- Auswertung: qstern.py auswertung --aus aus (auf der .69, Spur cpu, nach den Laeufen; bei Zeitmangel auf dem Stand
  der fertigen Laeufe).

## 5 Auswertung (wortgleich zur Regel der Karte; Umsetzung in qstern.py cmd_auswertung)

Regel (bindend, je alpha in {0,01; 0,03; 0,1}):
- **Gesehen:**
  - aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen und ein Vorzeichenwechsel von s
  - Lage im Fenster 0,70 <= omega^2 <= 0,90, 1,6 <= rho <= 1,9
  - Lagen der Stufen auf 1e-4 gleich, K3 bestanden
- **Nicht gesehen:** im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
- **Unentschieden:** alles andere.
- alpha = 0,01 ist nur eine Stetigkeitskontrolle. Dort ist "gesehen" wegen der Stetigkeit fast erzwungen, es zaehlt
  nicht als Test. Echte Tests sind alpha = 0,03 und 0,1.
- Der Bericht nennt je alpha die Kompaktheit 2|Phi(0)| und Phi am Ballrand. Ab 2|Phi(0)| > 0,1 ist der
  Newton-Grenzfall fraglich; das wird vermerkt.
- Kontrollen: K1 alpha = 0 gibt die bewiesene Stelle auf 1e-4, Umlauf -1 auf beiden Stufen. K2 Hintergrund auf zwei
  Gittern, omega, Q, E und Phi(0) auf 1e-6 relativ. K3 Aussenrand R und 1,5 R, Lage einer gefundenen Stelle aendert
  sich um weniger als 1e-4. Verfehlt eine Kontrolle: nicht auswertbar fuer das betroffene alpha.

Umsetzung (Lesart, vor den Laeufen festgelegt):
- "Rechteck" einer Stelle = kleines Rechteck um die lokalisierte Stelle (omega*^2 +- 4e-4, rho* +- drho) wie bball2.
  "Umlauf +-1 auf beiden Stufen" und "Lagen auf 1e-4 gleich": Kandidat auf h = 0,02 und h = 0,01 mit
  |d omega^2| < 1e-4 und |d rho| < 1e-4, beide aufgeloest, |Umlauf| = 1, beide im Fenster.
- K3 bestanden: der K3-Lauf (r_fak 1,5) hat einen Kandidaten mit |d omega^2| < 1e-4 und |d rho| < 1e-4 zur
  h-0,02-Lage. K3-Lauf vorhanden, aber ohne solchen Kandidaten: K3 verfehlt -> nicht auswertbar (falls keine andere
  Stelle "gesehen" ist). K3-Lauf fehlt (Zeit): nicht bestanden -> hoechstens Unentschieden.
- "Nicht gesehen" verlangt: beide Stufen decken 0,70 .. 0,90 ab, alle Zeilen gueltig, kein s-Wechsel mit
  Mittelpunkt im Fenster, alle Streifen aufgeloest mit Umlauf 0.
- omega ist im Hintergrund Vorgabe (gleich auf beiden Gittern); K2 vergleicht Q, E und Phi(0).
- K2 gilt je alpha; K2 verfehlt -> nicht auswertbar fuer dieses alpha. K1 verfehlt -> alle alpha nicht auswertbar.
- Der Bericht nennt zu jeder gesehenen Stelle den Ast (Ast der bewiesenen Stelle, Richtung +1, rho ~ 1,6 .. 1,8, oder
  schwellennahes Paar), ohne dass das den Regel-Ausgang aendert.

## 6 Vorab (Agent, vor den Laeufen, nach den Rauchtests)

- E-1 K1 besteht auf beiden Stufen (alpha = 0 ist der bball2-Pfad): ~90 %.
- E-2 K2 besteht fuer alle drei alpha (Phi-Toleranz 1e-9, RK4 O(h^4)): ~75 %.
- E-3 alpha = 0,1: Ausgang "Gesehen" ~25 % (nur ueber das schwellennahe Paar), "Unentschieden" ~60 %, "Nicht
  gesehen" ~15 %. Begruendung: Der Ast der Stelle hat im ganzen Fenster s < 0 (Rauchtest); die Streifen haben aber
  Umlauf +1 aus dem schwellennahen Bereich.
- E-4 alpha = 0,03: "Gesehen" ~45 % (Stelle am unteren Fensterrand oder schwellennahes Paar), "Unentschieden" ~45 %.
- E-5 Richtung: omega*^2 sinkt mit alpha (Rauchtest) ~85 %; |Delta omega*^2| bei alpha = 0,1 > 0,05 ~80 %.
- E-6 Kompaktheit am Ort der Stelle > 0,1 fuer alpha = 0,03 und 0,1 ~95 %.

## 7 Letzte Pruefungen vor dem Einfrieren

- rauch-k1-a0 (alpha = 0, Zeilen 0,795/0,80, h = 0,04, budget 90): s-Wechsel zwischen 0,7975 (rho 1,74456, s +1,9e-4)
  und 0,80 (rho 1,74538, s -2,4e-3), Streifen Umlauf -1, aufgeloest; Lokalisierung wegen budget 90 entfallen
  (Reserve 90 s), 2,8 s. Pfad alpha = 0 laeuft.
- auswertung-rauch (Auswertungskommando auf lauf-lokal/): laeuft ohne Fehler (alle Ausgaenge "nicht gerechnet", da
  keine Regel-Laeufe vorhanden).
- Dateien fuer die .69: qstern.py, start-cpu.sh, start-cpu2.sh (sha256 im Ergebnis).
