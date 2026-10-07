# LEITER-2D-PRAEZ: Bricht die 2D-Leiter nach n = 6 ab, oder versagt der Vorzeichentest? (Runde 12, explorativ)

- Code-Agent im Auftrag der Leitung claude-primary. Neustart nach API-Limit-Abbruch am 30.09. (keine Datei entstanden).
- Beginn 2026-10-01 17:12:18 CEST (date). Plan geschrieben ab 17:23:30 CEST (date), vor jedem Lauf und vor dem Rauchtest.
- Arbeitsordner lokal: coordination/runden-v3/RUNDE-12/leiter2d-praez/; .69: /home/fmh/fmhc-physics-remote/runde12-leiter2d-praez/.
- Zeitbox 60 min (bis etwa 18:12 CEST).

## 1. Schreibtisch: Kernzuwachs der 3D-Laeufe n = 11 bis 15

Frage der Leitung: Fand derselbe Code in 3D bei vergleichbarem oder groesserem Kernzuwachs saubere Vorzeichenwechsel?

**Antwort: nein.** Die 3D-Stellen ab n = 7 kamen nicht aus dem Vorzeichentest, sondern aus Breitenminima der Polsuche.

- **n = 11 bis 15 (3D) wurden mit `pole` gefunden, nicht mit `kurve`.**
  - Fundstellen: RUNDE-09.md, FORMEL-1 (Z. 337 ff., "Test: pole bei 0,5381 ..."), FORMEL-2 und FORMEL-3/MOD-2 (Z. 359 bis 425).
    Die Laufordner sind RUNDE-09/daten-leiter/quellen-69/runde7-bic2/aus-pole-dw-n7 ... n15b.
  - Das Verfahren ist die Pluecker-Determinante. Die Lagen stammen aus der "signierten Wurzel" von |Im rho| auf drei
    Punkten, also aus Breitenminima ohne Umlauftest (RUNDE-09.md Z. 425 ff.; DATENPAKET.md Z. 222 bis 232).
  - **In keinem der zehn pole_bericht.txt steht ein Kernwachstum.** grep "wachstum" findet nichts, `pole` gibt es nicht aus.
  - Anschluss und Rand bei n = 15: r_m = 25,16 und R = 44,58 (aus-pole-dw-n15a/pole_bericht.txt).
  - Schaetzung, nicht gemessen [Hand]: Die 2D-Laeufe wachsen mit etwa 1,2 je Laengeneinheit
    (ln(1,2e5)/9,92 = 1,18 in R11-a; ln(1,9e6)/12,0 = 1,21 in R11-d). Bei r_m = 25 waeren das grob e^30, also etwa 1e13.
- **Der Vorzeichentest (`kurve`, direkte Vektoren wie in bic2_2d.py) versagte in 3D ab n = 7:**
  - RUNDE-08.md Z. 275 bis 282: n = 6 hat einen Vorzeichenwechsel. Bei n = 7 bleibt s negativ, Kernwachstum bis 1,1e7,
    und die Pol-Spur springt ("vermutlich mischen dort zwei Zweige"). Bei n = 8 und 9 gibt es keinen Wechsel; das
    Kernwachstum von 1,0e9 liegt ueber der Vorab-Grenze 1e8, der Lauf gilt als "nicht entscheidbar".
  - RUNDE-09.md Z. 139 und 154: "Der Vorzeichentest hatte hier versagt (Zweigmischung)." Die Polsuche fand danach die
    Breitenminima bei n = 7, 8 und 9 an den vorab fortgesetzten Stellen.
  - RUNDE-07.md Z. 80: Kernwachstum 9e6 bei vermuteter Pol-Zweigmischung.
- **Folgerung fuer die Lesarten:** Der 3D-Befund spricht nicht gegen (b). In 3D und in 2D bricht der Vorzeichentest an
  derselben Sprosse ab (n = 7), bei einem Kernwachstum von 1,1e7 (3D) bzw. 1,9e6 (2D). Die 3D-Leiter laeuft trotzdem
  bis n = 15 weiter, belegt durch Breitenminima.

### 1b. Nachtraegliche Lesung der R11-Polbreiten mit der 3D-Methode [H, nachtraeglich, kein Test]

- Die Methode wurde erst nach Kenntnis der R11-Daten gewaehlt. Sie ist dieselbe wie bei 3D n = 11 bis 15 (RUNDE-09).
- R11-d, Pluecker-Pole, |Im rho|: 0,5285: 1,972e-3; 0,5290: 2,346e-4; 0,5295: 1,743e-4; 0,5300: 1,610e-3.
  - Wurzeln: 4,441e-2 / 1,532e-2 / 1,320e-2 / 4,013e-2.
  - Nur die Vorzeichenwahl (+, +, -, -) gibt gleiche Steigungen: -58,2 / -57,0 / -53,9 je Einheit omega^2.
  - Nullstelle aus dem inneren Paar 0,529269; Ausgleichsgerade ueber alle vier Punkte 0,529278.
  - Schritt in 1/eps von n = 6 (29,546) zu 34,166 ist 4,620. Vorhersage V1 aus der R11-Karte: 0,52927 +- 0,0002.
- Die "kleinste Polbreite 1,75e-4" aus der R11-Karte ist nur der kleinste Rasterwert. Das Raster hat Abstand 5e-4, der
  naechste Rasterpunkt liegt 2,3e-4 von 0,52927 entfernt. Der Scheitel des V liegt bei extrapoliert |Im rho| < 1e-5.
- Der Realteil des Pols kreuzt die Linie L(y_b) = 0 zwischen 0,5290 und 0,5295, linear bei 0,52927. Bei n = 6 fiel
  dieser Kreuzungspunkt mit der stillen Stelle zusammen.
- n = 8 (R11-f, nur zwei Punkte, Vorzeichenwahl nicht pruefbar): Bei entgegengesetzten Vorzeichen folgt 0,525782,
  Steigung -72,4. V1 lag bei 0,52578 +- 0,0003.
- **Spannung [H]:**
  - Die Polbreiten sehen bei n = 7 wie eine stille Stelle aus, ein V mit Scheitel nahe 0 an der vorhergesagten Lage.
  - s = L(y_a) bleibt auf dem Ast dagegen bei etwa -1e-4, ohne Einbruch.
  - Ein reeller Pol ist nach dem Flussargument genau eine Nullstelle von W. Beides zugleich kann nur stimmen, wenn der
    Scheitel nicht ganz 0 erreicht (Quasi-BIC), oder wenn eine der beiden Rechnungen falsch ist.
  - Zwei Zahlen, die dasselbe messen sollen, widersprechen sich. Das ist eine Frage, kein Befund.

## 2. Vorhersage (vor jedem Lauf)

Wahrscheinlichkeiten fuer die Lesarten (was tatsaechlich zutrifft):

- **(a) Abbruch, nach n = 6 nur Quasi-BIC: 0,35.**
  - Dafuer spricht: s ist glatt und monoton, h = 0,02 und h = 0,01 stimmen auf 3 bis 4 Stellen ueberein.
  - L(y_a) haengt analytisch nicht von r_m ab (Omega ist fuer zwei Loesungen erhalten). Bei einem Kernwachstum <= 1e7
    reicht double-Genauigkeit rechnerisch aus: Rundung etwa 1e-16 * 1e7 = 1e-9 relativ.
- **(b) Verfahren oder Numerik verliert die Stelle: 0,65.**
  - Dafuer spricht das gleiche Versagensmuster in 3D (Abschnitt 1) und das V der Polbreiten an der vorhergesagten
    Lage mit Schritt 4,620 (Abschnitt 1b).
  - Aber nur ein Teil davon waere mit r_m sichtbar: **Ursache "Genauigkeit, mit r_m beweglich" 0,15**, Ursache
    "Verfahren (Ast oder Formulierung), mit r_m nicht beweglich" 0,50.

Vorhersage der Testausgaenge:

- **P1 r_m-Invarianz:** s bei 0,5285 bis 0,5300 stimmt fuer r_m = 9, 12 und 15 auf mindestens 2 Stellen ueberein und
  bleibt negativ. Wahrscheinlichkeit 0,8.
- **P2 Reproduktion:** r_m = 12 gibt die R11-d-Werte in allen gedruckten Stellen (gleicher Pfad, gleicher Rand R = 31,76).
  Wahrscheinlichkeit 0,95.
- **P3 Positivkontrolle:** Der Wechsel zwischen 0,533 und 0,535 bleibt bei jedem r_m erhalten. Die verfeinerten omega*^2
  liegen alle innerhalb +-2e-5 von 0,5338453. Wahrscheinlichkeit 0,85.
- **P4 Rechteck um (0,5292; 1,557):**
  - aufgeloest mit Umlauf 0: 0,45
  - aufgeloest mit Umlauf +-1: 0,25
  - nicht aufgeloest oder Fehler: 0,30
- **P5 Ausloeschungsmass** (groesster Einzelterm von Omega(y_a, z2) geteilt durch |s|): ueberall unter 1e8, erwartet 1e3
  bis 1e6. Dann ist Rundung als Ursache rechnerisch ausgeschlossen.
- Erwarteter Ausgang nach der Scheiterregel: "(a) Abbruch" 0,45, "(b) Numerik" 0,30, "unentschieden" 0,25.

## 3. Scheiterregel (Wortlaut der Leitung, Fundstelle: Auftrag LEITER-2D-PRAEZ, Punkt 2)

- **"(b) Numerik":** s wechselt bei 0,5285 bis 0,5300 unter geaendertem Anschlussradius r_m das Vorzeichen, oder ein
  aufgeloestes Rechteck zeigt Umlauf +-1.
- **"(a) Abbruch":** s bleibt fuer alle r_m negativ, und die Rechtecke zeigen Umlauf 0.
- Sonst **"unentschieden"**.

Auslegung, festgelegt vor dem Lauf (Zusatz des Code-Agenten, nicht von der Leitung):

- "Wechselt das Vorzeichen": Fuer irgendein r_m aus {9, 12, 15} ist s an einem der Punkte 0,5285/0,5290/0,5295/0,5300 >= 0,
  oder der Ast wechselt dort das Vorzeichen.
- "Aufgeloest" nach dem Code: groesster Phasensprung < 0,4 rad. Umlauf +-1 heisst |u -+ 1| < 0,1, Umlauf 0 heisst |u| < 0,1.
- Ist kein Rechteck aufgeloest, kann "(a)" nicht gelten. Der Ausgang ist dann "unentschieden", ausser "(b)" folgt schon
  aus s.
- Positivkontrolle: Faellt der Wechsel bei 0,533/0,535 fuer ein r_m weg, sind die s-Werte dieses r_m kein gueltiger
  Beleg fuer "(a)". Das wird vermerkt. Ein s >= 0 bei 0,5285 bis 0,5300 zaehlt trotzdem fuer "(b)".

## 4. Code

- bic2_2d_praez.py ist eine Kopie von GEN-02/G2-10/bic2_2d.py. Das Original bleibt unveraendert.
  - Original: sha256 e5f035c994922d357f0307b1acfea3edae5305396eb94c5e303760f9d7dcd2e1 (lokal und .69 runde11-leiter2d/ gleich).
  - Kopie: sha256 55f27ec8ae014f8f4db90346ef84355c668e0ca6a2b016385686f2f2908f3cfe.
  - Diff: bic2_2d_praez.diff (166 Zeilen), sha256 4e7d1c58bb14f2c40e462adc919471f4738fbb71e3a8c04be0273b3b37feca0a.
- **Aenderungen**, alle mit "PRAEZ" markiert:
  1. `--rm` (i): In `lin_multi` ersetzt ein fester Wert den Median der R_halb. Danach wie bisher Km = round(r_m/h),
     gerade gemacht, in [2, K-2]. Das wirkt fuer kurve und exakt.
  2. exakt mit `--dim` (ii): Die sieben festen `[1.0] * len(...)` (nu = 1, nur 3D) in exakt, umlauf_neu_gelegt und
     umlauf_rechteck sind jetzt `[g210_nu()] * len(...)`. Bei --dim 3 ist nu = 1 wie vorher. Die Profile hatten schon dim.
     Dauer der Aenderung: etwa 5 min.
  3. kurve gibt zusaetzlich aus:
     - `wachstum_je_x`: Kernwachstum je omega^2, das Maximum ueber die rho-Abtastung
     - je Kandidat das Kernwachstum, `terme_a` (groesster Einzelterm von Omega(y_a, z2) * |nz|) und
       `ausloeschung` = terme_a/|s|
     - Die Rechenwege fuer s, Pol und Verfeinerung sind unveraendert.
- Kern des Diffs (vollstaendig in bic2_2d_praez.diff):

```
@@ lin_multi
     rh = sorted(r_halb(p) for p in profs)[len(profs) // 2]
+    if PRAEZ_RM["r"] is not None:                                                             # PRAEZ: --rm
+        rh = PRAEZ_RM["r"]
     Km = max(2, min(K - 2, int(round(rh / h))))
@@ direkt_m
+    la_terme = torch.stack([(ya[0] * z2[2]).abs(), (ya[2] * z2[0]).abs(), (ya[1] * z2[3]).abs(),
+                            (ya[3] * z2[1]).abs()]).amax(0) * nz.abs()
-    return {"M": M, "la": ...
+    return {"M": M, "la_terme": la_terme, "la": ...
@@ exakt, umlauf_neu_gelegt, umlauf_rechteck (7 Stellen)
-        ... [1.0] * len(xs) ...
+        ... [g210_nu()] * len(xs) ...
@@ kurve
+    st["wachstum_je_x"] = [...]; je Kandidat "wachstum", "terme_a", "ausloeschung"; Tabellenzeile um zwei Spalten
@@ argumente / main
+    ap.add_argument("--rm", type=float, default=None, ...);  PRAEZ_RM["r"] = a.rm
```

## 5. Laeufe (nur .69, nur kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4, cpu6; je Aufruf <= 10 min, --budget 540)

Gemeinsam: `--dim 2 --beta 0.5 --h 0.02`.

| Lauf | Spur | Befehl |
|---|---|---|
| RM9 | cpu | kurve --omega2-liste 0.5285,0.5290,0.5295,0.5300,0.533,0.535 --rm 9 --n-wechsel-fein 2 |
| RM12 | cpu2 | dasselbe mit --rm 12 |
| RM15 | cpu3 | dasselbe mit --rm 15 |
| REC | cpu4 | exakt --x0 0.5292 --rho0 1.5561 --rc 1.557 --drho 5.5 --cgam 3000 --offsets 0,7.5e-5,-7.5e-5,1.5e-4,-1.5e-4,2.25e-4,-2.25e-4,3e-4,-3e-4 --w-dx 3e-4 --w-drho -1e-3,-3e-4,-1e-4,-3e-5,0,3e-5,1e-4,3e-4,1e-3 --u-dx 3e-4,1.5e-4 --u-drho 1.5e-3 --u-drho-ohne-fit 1.5e-3 --u-n 60 --neu-legen nein --rm 12 |
| FEIN (Zusatz) | cpu6 | kurve --omega2-liste 0.5292,0.52925,0.5293,0.52935 --rm 12 --n-wechsel-fein 0 |

- Die Positivkontrolle (0,533 und 0,535) laeuft in RM9/RM12/RM15 auf demselben Ast mit. Bei einem Wechsel verfeinert
  der Code in 4 Stufen.
- REC: Rechteckmitte (0,5292; 1,557) nach der Leitung, halbe Hoehe mindestens 1,5e-3.
  - Damit liegen die Linie L(y_b) = 0 (1,5560 bis 1,5567) und der Kreuzungspunkt des Pols (~1,5564) innen.
  - rho0 = 1,5561 und drho = 5,5 dienen nur als Newton-Keime der Pole (Realteil des Pols aus R11-d interpoliert).
- **FEIN ist ein Zusatz des Code-Agenten und nicht Teil der Scheiterregel.**
  - Frage: Faellt |Im Pol| bei 0,52925 und 0,5293 weiter (V bis nahe 0), oder bleibt ein Sockel?
  - Vorab: Bei einer echten Stelle bei 0,52927 +- 1e-5 ist min |Im Pol| auf diesen vier Punkten <= 3e-6, und die
    signierte Wurzel gibt 0,52927 +- 1,5e-5. Bei einem Quasi-BIC mit Sockel >= 1e-5 ist min |Im Pol| >= 1e-5.
  - s an diesen Punkten: erwartet glatt zwischen -8,8e-5 und -1,13e-4, ohne Wechsel.
- **Rauchtest:** Lokal steht keine Physik-Umgebung (torch) bereit, deshalb lokal gar kein Python. Der Rauchtest laeuft
  auf der .69 ueber kleintest.sh (Spur cpu, --budget 100):
  - kurve --dim 2 --omega2-liste 0.62 --n-rho 40 --h 0.04 --rm 9 --n-wechsel-fein 0
  - exakt --dim 2 --h 0.04 --x0 0.62 --offsets 0,1e-3,-1e-3 --u-dx 1e-3 --u-n 10 --rm 9 --neu-legen nein
- Code auf der .69 nie in place ueberschreiben: neue Fassung unter neuem Namen hochladen, dann mv.

## 6. Grenzen

- Keine Geheimnisse, keine gesperrten Pfade, kein git, kein Peerbus, keine Unteragenten, keine Dienste.
- Geschrieben wird nur in RUNDE-12/leiter2d-praez/ und runde12-leiter2d-praez/.

## 7. Nachtrag, nachtraeglich festgelegt (2026-10-01 17:39:12 CEST, date)

Festgelegt nach den Laeufen RM9, RM12, RM15, REC und FEIN, vor den Folgelaeufen. Diese Laeufe aendern den
vorab festgelegten Ausgang nach Abschnitt 3 nicht. Sie werden getrennt und als nachtraeglich berichtet.

- **Anlass:**
  - REC rechnet W auf einem feinen rho-Gitter (Abstand 3e-5 bis 7e-4) und findet dort s > 0 bei 0,5289 bis 0,5292 und
    s < 0 bei 0,529275 bis 0,5295.
  - kurve findet bei denselben omega^2 s ~ -1e-4. kurve tastet rho mit 400 Punkten ab (Abstand 3,6e-3) und
    interpoliert linear.
- **Hypothese [H]:** Der Wert s in kurve ist bei n >= 7 vom Interpolationsfehler des groben rho-Gitters beherrscht.
  - Begruendung: L(y_a) und L(y_b) haben fast parallele Gradienten (cond J = 3,3e4 in REC).
  - s ist nur der kleine Rest nach dieser Fast-Ausloeschung.
  - Der Fehler der linearen Interpolation waechst mit der Kruemmung, die vom Kernanteil kommt.
- **Folgelaeufe** (Code v1 fuer kurve; v2 = v1 plus --u-runden fuer das Rechteck, Diff bic2_2d_praez_v2.diff):
  - F7: kurve --omega2-liste 0.5285,0.5290,0.5295,0.5300 --n-rho 4000 --rm 12 --n-wechsel-fein 1 (Spur cpu)
  - F8: kurve --omega2-liste 0.5255,0.5260 --n-rho 4000 --rm 12 --n-wechsel-fein 1 (Spur cpu2)
  - F6: kurve --omega2-liste 0.533,0.535 --n-rho 4000 --rm 12 --n-wechsel-fein 1 (Spur cpu3, Kontrolle)
  - REC2: exakt wie REC, mit v2 und --u-runden 20 (Spur cpu4)
- **Vorhersagen (vor den Folgelaeufen):**
  - F7: s wechselt zwischen 0,5290 und 0,5295 das Vorzeichen (s(0,5290) etwa +1e-5 bis +2e-5, s(0,5295) etwa -1e-5 bis
    -2e-5). Die Verfeinerung landet bei 0,52927 +- 3e-5 mit |Im Pol| < 1e-6.
  - F8: Wechsel zwischen 0,5255 und 0,5260, Verfeinerung bei 0,52578 +- 5e-5 (wahrscheinlich 0,6; nur zwei Punkte).
  - F6: Der Wechsel bleibt, die Verfeinerung trifft 0,5338453 +- 1e-5.
  - REC2: beide Rechtecke aufgeloest (Sprung < 0,4 rad), Umlauf -1.
- **Scheitern der Hypothese:** F7 ohne Vorzeichenwechsel (s bleibt an allen vier Punkten negativ), oder REC2 aufgeloest
  mit Umlauf 0.
