# REGIME-K-3: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 49)

- Karte KARTE.md unveraendert und bindend (RT0 bis RT3, Wortlaut, Schwellen, Wahrscheinlichkeiten).
- Plan PLAN.md, eingefroren 2026-10-05 14:56:43 CEST (date): PLAN.md.eingefroren-20261005-145643 (sha256 0701dd47...),
  code/rk3.py (b921377b...), code/kette.sh (3e946d09...), code/rauch.sh (7cfeb1c3...), dazu unveraendert aus
  RUNDE-37/regime-k-2/code (eingefroren) kopiert: rk.py (afd77889...), rk2.py (eb361e43...), pt.py (bc360991...), ew.py
  (fa7b6417...), tp.py (419d7da6...); je mit *.eingefroren-20261005-145643. Liste EINGEFROREN-SHA256.txt; auf der .69
  dieselben Summen (EINGEFROREN-SHA256-69.txt). Alle 12 Hauptlaeufe und die Auswertung nennen rk3.py b921377b...
  (Python 3.12.3, numpy 2.4.4). Nicht eingefroren, nur Startskript: code/auswertung.sh (9a2b149e...).
- **Zeiten (date; die .69 schreibt UTC, CEST = UTC + 2):**
  - Start 14:13:04 CEST. Projekt-grep 14:30:35. Plantext ab 14:30:46 CEST, vor jedem Rauchtest.
  - Rauchtests 12:38:49 bis 12:55:41 UTC (14:38:49 bis 14:55:41 CEST). Plan-Nachtrag (PLAN 9) ab 14:55:51 CEST.
  - Eingefroren 14:56:43 CEST.
  - Hauptlaeufe 12:56:58 bis 13:14:48 UTC; Auswertung 13:14:51 bis 13:14:56 UTC (lauf-69/auswertung.json).
  - Ergebnistext: Entwurf ab 14:58:43 CEST (waehrend der Laeufe, ohne Werte), Endfassung ab 15:17:18 CEST; Abgabe in der
    letzten Zeile.
- **Laeufe** (alle ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/regime-k-3/,
  1 Thread; Laufzeit = Service runtime):

| Lauf | Spur | Inhalt | Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| r1 bis r6 (Rauch, 27 Starts) | cpu8, cpu9, cpu10 | PLAN 9 (je 4 Raster- und 4 BZ-Punkte; r6 Auswertungsprobe) | 12:55:41 | je <= 34 s | alle 0 |
| KW-raster, KW-bz | cpu8 | Kuhn, 539 Rasterpunkte bzw. 511 BZ-Punkte | 12:57:06 / 12:57:12 | 8,1 / 6,2 s | 0 |
| B1-t1-raster, B1-t1-bz | cpu8 | B1 ohne Fuellung, 539 / 511 | 12:58:33 / 12:59:45 | 80,0 / 72,8 s | 0 |
| V-A-raster-0 bis -3 | cpu9 (0, 1, 2), cpu8 (3) | V, Raster in vier Teilen (135, 135, 135, 134) | 13:02:53 / 13:08:54 / 13:14:48 / 13:10:32 | 355 / 361 / 354 / 352 s | 0 |
| V-A-bz-0 bis -3 | cpu10 (0, 1, 2), cpu8 (3) | V, BZ in vier Teilen (128, 128, 128, 127) | 13:01:50 / 13:06:48 / 13:11:47 / 13:04:40 | 292 / 298 / 299 / 295 s | 0 |
| auswertung | cpu8 | Urteile, Kontrollen, beschreibend (code/auswertung.sh) | 13:14:56 | 4,1 s | 0 |
| nachtrag (nach Sicht) | cpu10 | code/nachtrag_rk3.py: Maxima und Zaehlungen nur ueber ungesperrte Punkte | 13:20:33 | ~2 s | 0 |
| nachtrag2 (nach dem Gegenlesen, GL-3) | cpu10 | code/nachtrag2_rk3.py: unverfeinerte T-Eigenwerte gegen nachgeschaerfte, K6 mit T-Werten | 13:36:39 | ~1 s | 0 |

  - 42 Starts (27 Rauch, 12 Haupt, 1 Auswertung, 2 Nachtraege), alle rc = 0, alle unter 600 s; nur cpu8, cpu9, cpu10.
    Pruefsummen der Laufdateien auf der .69 erzeugt (lauf-69/PRUEFSUMMEN-lauf-69.txt, 30 Dateien; die drei leeren
    nohup-*.txt sind nicht darin), lokal bestanden; Nachtraege: nachtrag-69/PRUEFSUMMEN-NACHTRAG.txt.
- Alles synthetische Gitterrechnung, linearisiert um flach, euklidisch gerechnet und formal fortgesetzt. Keine Messdaten,
  keine Messdatenbestaetigung.
- **Kennzeichen:** [E] hier gerechnet, [M] Mathematik, [P] Projektdatei, [L] Gedaechtnis, [H] Hypothese oder Lesart,
  [K] Kopfrechnung aus gerechneten Werten, [F] Festlegung im Plan, [N] Nachtrag nach Sicht (beschreibend, kein Urteil).
- **Begriffe:** KW = Kuhn-Gitter, B1-t1 = B1-Kopie ohne Fuellung, V-A = Finns gefuelltes Netz V mit Hubfolge A, alle mit
  Zeltstangen-Treppe und tau = 1 (wie REGIME-K-2). z = Eigenwert der Takt-Transfermatrix (= exp(i k_tau tau)).
  delta = abs(Arg z); "abs(lambda)" = exp(delta) (PLAN 2.5); "g" = abs(lambda) - 1 = exp(delta) - 1. TT = die zwei
  Schwerewellen-Moden (je vorwaerts und rueckwaerts, also 4 Eigenwerte je k). "Instabil" = Eigenwert mit g > 1e-6
  (sicher, Regel 2.5). "Schnitt" = z reell negativ (delta = pi). "Kreis" = abs(z) = 1 (euklidischer Nulldurchgang).

## 1. Ergebnis zuerst

1. **Kuhn ist stabil, die Kontrolle haelt [E].** An allen 1050 gerechneten k (539 Raster, 511 BZ) liegen alle
   physikalischen Takt-Eigenwerte auf dem Einheitskreis: groesstes g = 1,5e-12 (Schwelle 1e-10). Es sind je k genau 4 (zwei
   Moden, je vorwaerts und rueckwaerts; im Raster als TT zugeordnet); die dritte Kuhn-Groesse hat keine Traegheit
   (statisch, nicht propagierend, zaehlt nach PLAN 9 nicht). Die TT-Dispersion ist die Wuerfelgitter-Formel von
   REGGE-WELLE-1 (auf 6,3e-10). **RT0 eingetroffen.**
2. **Die TT-Frequenzen aus REGIME-K-2 sind kein Effekt der Nullstellensuche [E].** Die nachgeschaerften Takt-Eigenwerte
   geben alle 98 REGIME-K-2-Nullstellen auf V bei abs(k) = 0,05 auf 3,3e-13 wieder (Kuhn 48 auf 6,6e-14, B1 48 auf 8,8e-14);
   das ist zum Teil konstruktionsbedingt, weil die Nachschaerfung dieselbe Laurent-Form benutzt. Unabhaengig davon geben
   die **unverfeinerten** Transfermatrix-Eigenwerte sie auf 1,6e-7 wieder (Kuhn 1,6e-12, B1 1,2e-9), und ihr TT-delta bei
   abs(k) = 0,05 ist 9,485e-6, nachgeschaerft ebenso (Unterschied <= 1,6e-7) [N]. Die V-TT-Eigenwerte liegen also neben
   dem Kreis: g bis 9,5e-6 bei abs(k) = 0,05, 3,3e-5 bei kl = 0,05, 2,6e-4 bei kl = 0,1, wachsend wie k^3 [K].
   **RT1 nicht eingetroffen** (Schwelle 1e-8; 190 Punkte verletzt, 104 kleine k gesperrt).
3. **Auf V ist die Zeltstangen-Zeit in dieser Lesart durchweg instabil [E].** Nicht nur einzelne Gittermoden: An jedem
   ungesperrten Rasterpunkt sind 52 bis 56 der 56 Eigenwerte instabil, in der BZ 44 bis 56; nach dem Nachtrag [N] sind es
   an jedem ungesperrten Rasterpunkt **alle 52 Gitter-Eigenwerte** (dazu je nach k 0, 2 oder 4 TT-Eigenwerte); in der BZ
   sind an 504 von 511 Punkten alle 56 instabil, an 7 Punkten 44 bis 50. Das groesste abs(lambda) ist e^pi - also
   g = 22,14 - (z reell negativ); im Mittel liegen je Rasterpunkt zwei Eigenwerte auf dem euklidischen Kreis (98 je 49
   Punkte, bei kl = 0,005 96; delta ~ 2,56, abs(lambda) ~ 13 [K]), die REGIME-K-2 als imaginaere Wurzeln gesehen hatte.
   **RT2 eingetroffen** (nach Plan und nach Kartenwortlaut).
4. **B1 ohne Fuellung ist ebenfalls instabil, aber deutlich schwaecher [E].** Je k 8 bis 12 instabile von 24 Eigenwerten
   im Raster (BZ 8 bis 24; Mittel 9,4 bzw. 12,0), V 52 bis 56 von 56 (Mittel 55,3 bzw. 55,9). Im Mittel hat B1 also nur
   etwa ein Fuenftel so viele instabile Eigenwerte wie V (0,17 bzw. 0,21 [Leser, K]); der groesste Wert ist gleich
   (e^pi). An allen 421 vergleichbaren Rasterpunkten gilt N_B1 <= N_V/2. **RT3 eingetroffen** (Anteil gesperrter V-Punkte
   9,9 %, knapp unter der 10-%-Grenze).
5. **Bedeutung [H]:** Die Takt-Transfermatrix von V ist in der Konvention von REGGE-WELLE-1 (Osterwalder-Schrader-Lesart)
   an keinem ungesperrten k positiv; an den ungesperrten Rasterpunkten sind nur die TT-Eigenwerte nahe am Kreis. Eine
   unitaere Echtzeit-Entwicklung ergibt die Treppe ueber V so nicht. Kuhn zeigt, dass es nicht an Regge oder an den
   Zeltstangen an sich liegt. Regime K ist in dieser Form auf V nicht der Hauptweg; offen bleiben eine
   zeitspiegelsymmetrische Treppe, eine echte Lorentz-Fortsetzung (Zeltstangen zeitartig), andere Fuellungen, oder dass V
   als Netz ausscheidet (Abschnitt 6).

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 14:56:43 CEST, Abschnitte 4 und 9) durch code/rk3.py (Modus auswertung); Werte in
lauf-69/auswertung.json ("urteile", "K5", "K6", "PK-T", "arme", "beschreibend").

| Nr | Vorhersage (Kartenwortlaut) | Wahrsch. | Urteil nach Plan | Urteil nach Kartenwortlaut | Kennzahlen [E] |
|---|---|---|---|---|---|
| RT0 | Kontrolle [P]: Auf Kuhn liegen alle physikalischen Eigenwerte der Takt-Transfermatrix auf dem Einheitskreis (abs(lambda) - 1 < 1e-10) an allen gerechneten k, passend zu REGGE-WELLE-1 | 80 % | **eingetroffen** | **eingetroffen** | 1050 Punkte, keiner gesperrt, kein Verstoss; g_max = 1,52e-12; je k 4 physikalische Eigenwerte (TT), 2 nicht propagierende (statische Richtung) |
| RT1 | [H] Auf V liegen fuer die zwei TT-Moden bei \|k\| <= 0,1 die Eigenwerte auf dem Einheitskreis (abs(lambda) - 1 < 1e-8); die komplexen Frequenzen aus REGIME-K-2 waeren dann ein Effekt der Nullstellensuche | 45 % | **nicht eingetroffen** | **nicht eingetroffen** | Lesart Koordinaten (abs(k) <= 0,1): 294 Punkte, 190 mit Verstoss, 104 gesperrt, TT-g_max = 3,27e-5; Lesart kl <= 0,1: 392 Punkte, 288 Verstoss, 104 gesperrt, TT-g_max = 2,63e-4. K6: REGIME-K-2-Nullstellen auf 3,3e-13 reproduziert |
| RT2 | [H] Auf V gibt es an mindestens einem gerechneten k einen Eigenwert mit abs(lambda) > 1 + 1e-6 (Instabilitaet, vermutlich aus den Gittermoden negativer Steifigkeit) | 55 % | **eingetroffen** | **eingetroffen** | 946 von 1050 Punkten mit Verstoss (104 gesperrt), 52620 verletzte Eigenwerte; g_max = 22,14 (= e^pi - 1, Schnitt); ohne Schnitt-Eigenwerte (Kartenlesart) 52544 und g_max = 22,1398 |
| RT3 | [H] Auf B1 ohne Fuellung gibt es hoechstens halb so viele instabile Eigenwerte je k wie auf V | 50 % | **eingetroffen** | **eingetroffen** | Raster: 421 Punkte verglichen, 0 Verstoesse; BZ: max 24 gegen 56, Mittel 11,98 gegen 55,90; gesperrt B1 5,5 %, V 9,9 % (Grenze 10 %) |

- **Pipeline** (PLAN 4): PK-T bestanden (441 KW-Rasterpunkte mit abs(k) <= 0,1, alle TT zuordenbar, TT-g_max 1,5e-12), K1
  bestanden (Schicht gegen rk.Gitter.H: <= 1,4e-15 KW, 4,0e-15 B1, 5,0e-15 V), K6 bestanden (KW, B1, V). Kein Urteil steht
  auf "unklar (Pipeline)".
- **Zu RT1:** Verletzt ist es nicht knapp: Schon bei kl = 0,02 liegt TT-g bei 2,1e-6, bei abs(k) = 0,05 bei 9,5e-6, also
  200- bis 1000-mal ueber 1e-8. Gesperrt sind die kleinsten k (V: kl = 0,005 48 von 49, kl = 0,01 41, kl = 0,02 15 Punkte),
  wo die Bulk-Elimination schlecht konditioniert ist (Abschnitt 3); dort ist auch die TT-Zuordnung bei kl = 0,005 nur an 27
  von 49 Punkten moeglich. Der Kartensatz "die komplexen Frequenzen aus REGIME-K-2 waeren dann ein Effekt der
  Nullstellensuche" ist widerlegt: K6 gibt sie auf 3,3e-13 wieder (nachgeschaerft, zum Teil konstruktionsbedingt), und
  die unverfeinerten Transfermatrix-Eigenwerte geben sie unabhaengig auf 1,6e-7 wieder, bei TT-delta 9,5e-6 [N].
- **Zu RT2, ausdruecklich:** RT2 ist eine Existenzaussage; jeder einzelne Verstoss an einem ungesperrten Punkt entscheidet.
  Das Feld "urteil" in plan_detail und karte_detail von auswertung.json heisst dort "nicht eingetroffen", weil es die
  Kreis-Frage ("alle auf dem Kreis?") beantwortet; das RT2-Urteil steht in "plan" und "karte". Die Klammer der Karte
  ("vermutlich aus den Gittermoden negativer Steifigkeit") ist nach PLAN 4 nur Lesart: Gerechnet ist, dass fast alle
  instabilen Eigenwerte zur Art Gitter gehoeren und ab kl ~ 0,02 auch die TT-Moden ueber der Schwelle liegen (Tabelle 5.3);
  ob die instabilen Gitter-Eigenwerte die Moden negativer Steifigkeit sind, ist nicht geprueft (Abschnitt 6).
- **Zu RT3:** Die 10-%-Regel haette RT3 bei 106 statt 104 gesperrten V-Punkten "nicht auswertbar" gemacht; der Nenner sind
  alle 1050 Punkte (Regel). Alle Sperren liegen im Raster, wo Teil (a) vergleicht: dort sind es V 104 von 539 (19,3 %) und
  B1 58 von 539 (10,8 %) [Leser]. Nach Plan und Wortlaut gleich, weil B1 und V auch ohne Schnitt-Eigenwerte dieselbe
  Ungleichung erfuellen.
- **Bedeutung, wie auf der Karte vorab festgelegt:**
  - "RT1 trifft ein, RT2 nicht: ... Regime K wird der Hauptweg": **nicht ausgeloest**.
  - "RT2 trifft ein: Die Zeltstangen-Zeit ist auf V instabil (Gittermoden); dann ist zu klaeren, ob eine andere
    Zeltstangen-Folge oder eine andere Fuellung das heilt, oder ob V als Netz ausscheidet": **ausgeloest**. Einschraenkung:
    instabil in der Konvention von REGGE-WELLE-1 (formale Fortsetzung, OS-Lesart), und nicht "einige" Gittermoden: an den
    ungesperrten Rasterpunkten alle, in der BZ an 504 von 511 Punkten alle 56 Eigenwerte; auch B1 ohne Fuellung ist
    instabil.
  - "RT1 verfehlt: Auch die langen Schwerewellen wachsen oder daempfen; das waere eine Grenze der diskreten Zeit auf V":
    **ausgeloest**, mit dem Zusatz, dass die Abweichung wie k^3 gegen null geht (Langwellenlimes stabil).
- **Agenten-Vorhersagen** (PLAN 8, vorab; gehen in kein Urteil ein):

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 | K6 auf V-A auf <= 1e-10 (85 %) | eingetroffen (3,3e-13) |
| A2 | RT1 nicht eingetroffen, TT-g bei 0,05 bis ~1e-5 (85 %) | eingetroffen (9,5e-6 bei abs(k) = 0,05) |
| A3 | RT2 eingetroffen, groesster Wert aus Gittermoden mit abs(z) = 1, delta bis ~2,6 (85 %) | erster Teil eingetroffen; zweiter verfehlt: der groesste Wert kommt von reell negativen z (delta = pi) |
| A4 | RT0 eingetroffen (55 %); drittes Kuhn-Paar mit z > 0 (55 %) | erster Teil eingetroffen; zweiter gegenstandslos: die dritte Kuhn-Groesse ist statisch (kein Paar) |
| A5 | RT3 nicht eingetroffen (55 %) | verfehlt (RT3 eingetroffen) |
| A6 | d = E_s - 4 NV ueberall (75 %); H_bb regulaer bei B1 und V, Kuhn 3 Nullrichtungen (65 %) | erster Teil eingetroffen (d 3, 12, 28 an allen 1050 Punkten); zweiter Teil teilweise verfehlt: Kuhn 3 Nullrichtungen ueberall, B1 und V aber an 2 bzw. 23 Punkten bei kleinen k numerisch singulaer (Eigenwert unter 1e-14 relativ) |

## 3. Verfahren in Kuerze [M, F]

- **Schicht = ein Takt** der Zeltstangen-Treppe (Gitter unveraendert aus REGIME-K-2, tau = 1). Randdaten l_n = die Kanten
  der Flaeche Sigma_n (raeumliche Kanten auf Stufe n; bei B1 und V wegen der gestaffelten Hoehen nicht eben), Bulk =
  Zeltstangen (Lapse) und Diagonalen (Shift). Schicht-Hesse aus rk.Gitter.Hloc mit Bloch-Phasen nur im Raum.
- **Bulk-Elimination (Hoehn):** Schur-Komplement ueber H_bb. Kuhn: 3 exakte Nullrichtungen je k (tote Hyperdiagonale,
  Lapse unten, Lapse oben); die Lapse-Richtungen geben die lineare Hamilton-Bedingung C^H l = 0 (Vor- = Nach-Bedingung).
  B1 und V: keine exakte Nullrichtung, aber fuer k -> 0 ein weich werdender Bulk-Eigenwert (Relativverschiebung der
  Stufen), der die Elimination bei den kleinsten k schlecht konditioniert (PLAN 9; daher die Sperren).
- **Eichreduktion:** G_l = 4D-Eckverschiebungen auf den Randkanten (Rang 3 NV bei Kuhn, 4 NV bei B1 und V);
  W = (Bild [G_l, C])^perp, d = E_s - 4 NV (Kuhn 3, B1 12, V 28), an allen 1050 Punkten je Netz.
- **Statische Richtungen:** Bei Kuhn hat B_W an allen 1050 Punkten genau eine Richtung ohne Kopplung zwischen den Stufen
  (rechter = linker Kern). Lesart [H]: die Raumdiagonale wie in UEBERLEITUNG-KH-1 [P]; die Richtung selbst ist nicht
  bestimmt. Sie wird statisch eliminiert; ihre formalen Eigenwerte 0 und unendlich heissen "nicht propagierend" und zaehlen
  nicht als physikalisch (PLAN 9, Festlegung). Bei V gab es einen Punkt (fib09, kl = 0,1) mit zwei fast singulaeren
  Richtungen ohne gemeinsamen Kern; dort Buendel-Ausweichpfad (Meldung), 56 endliche Eigenwerte, ungesperrt.
- **Transfermatrix:** T auf (v, pi) in W (Kuhn: auf dem nicht-statischen Rest), Groesse 2d (Kuhn 4, B1 24, V 56).
  Symplektisch: T^H J T = J. Eigenwerte z = exp(i k_tau tau), Paare z, 1/conj(z).
- **Nachschaerfen:** Jeder T-Eigenwert per Newton auf der vollen 4D-Form det Ql^H H(k_s, z) Qr = 0 (unabhaengig von der
  Bulk-Elimination); Echtheit s_voll komplementfrei; TT-Anteil eichinvariant.
- **Lorentz-Lesart (Konvention REGGE-WELLE-1, Osterwalder-Schrader-Lesart [L]):** omega = -Log(z)/tau, lambda =
  exp(-i omega tau); abs(lambda) := exp(abs(Arg z)) (groesster Faktor je Takt eines reellen Feldes mit +k und -k,
  Hauptzweig). Auf dem Einheitskreis genau dann, wenn z reell positiv ist (zweigunabhaengig). Ein euklidischer Takt mit
  einem nicht positiven Eigenwert hat in dieser Lesart keine unitaere Echtzeit-Entwicklung.

## 4. Ableitbarkeit, nachtraeglich bewertet

- PLAN 1.2 hatte vorab festgehalten [M, P]: Die Takt-Eigenwerte sind dieselben z wie die Nullstellen der Laurent-Form von
  REGIME-K-2; mit der Konvention von REGGE-WELLE-1 ist abs(lambda) = exp(abs(Arg z)). Damit waren RT1 (verfehlt) und
  RT2 (eingetroffen) **bedingt vorab ableitbar**, unter der Bedingung, dass REGIME-K-2 richtig gerechnet hat. Die Karte
  nannte sie "nicht ableitbar"; das trifft nur zu, solange die Konvention offen ist.
- Neu geprueft hat diese Karte: (a) die REGIME-K-2-Nullstellen auf einem zweiten Weg (K6 an den nachgeschaerften Werten,
  zum Teil konstruktionsbedingt; unabhaengig nur die unverfeinerten T-Eigenwerte, auf 1,6e-7 [N]); (b) das **vollstaendige**
  Spektrum aller physikalischen Eigenwerte an jedem k, nicht nur den Lichtkegelbereich R und den Zensus; (c) TT gegen
  Gittermoden; (d) den BZ-Rand; (e) B1 gegen V (RT3); (f) die dritte Kuhn-Groesse (RT0: statisch).

## 5. Tabellen [E]

### 5.1 Netze, Reduktion, Kontrollen (je 1050 Punkte: 539 Raster, 511 BZ)

| Groesse | KW | B1-t1 | V-A |
|---|---|---|---|
| Randkanten E_s / Bulk NB / Kanten NE / Ecken NV | 7 / 8 / 15 / 1 | 28 / 32 / 60 / 4 | 68 / 78 / 146 / 10 |
| Zeltstangen / Diagonalen / tote Kanten | 1 / 7 / 1 | 4 / 28 / 0 | 10 / 68 / 0 |
| Nullrichtungen H_bb (entkoppelt / unten / oben / gemischt) | 3 (1/1/1/0) ueberall | 0 an 1048, 1 gemischt an 2 | 0 an 1027, 1 gemischt an 23 |
| Rang G_l / Rang C / d | 3 / 1 / 3 | 16 / 0 / 12 | 40 / 0 / 28 |
| statische Richtungen, nicht propagierende Eigenwerte | 1 / 2 (ueberall) | 0 / 0 | 0 / 0 (1 Punkt Buendel) |
| physikalische Eigenwerte je k | 4 | 24 | 56 |
| gesperrte Punkte (Gruende) | 0 | 54 (symplektisch 38, verfeinerung 26, unecht 3, bulk 2, eichung 2) | 104 (verfeinerung 104, symplektisch 88, unecht 88, bulk 23) |
| K1 Schicht gegen rk.Gitter.H (32 Punkte) | 1,4e-15 | 4,0e-15 | 5,0e-15 |
| Symplektizitaet s_sym max | 8,9e-16 | 2,8e-9 | 3,0e-12 |
| Paarfehler p_err max (alle Punkte; gesperrte eingeschlossen) | 1,5e-12 | 0,84 | 0,69 |
| err max (2 x letzter Newton-Schritt; alle Punkte) | 2,6e-12 | 4,6 | 2,3e3 |
| s_voll max (alle Punkte) | 5,6e-16 | 3,0e-2 | 1,0e-3 |
| Eichidentitaeten auf W max / Hermitezitaet | 1,3e-7 / 1,8e-15 | 1,2e-5 / 6,4e-16 | 6,3e-7 / 6,4e-16 |
| K5 (+k gegen -k, 44 Paare) | 0 | 0 | 0 |
| K6 REGIME-K-2-Nullstellen bei abs(k) = 0,05 | 48, max 6,6e-14 | 48, max 8,8e-14 | 98, max 3,3e-13 |

- Die grossen Werte von p_err und s_voll gehoeren zu gesperrten Punkten (kleinste k); p_err > 1e-8 und s_voll > 1e-8
  sperren nach Regel. B1-Eichmaximum 1,2e-5 liegt ueber 1e-6 an 2 Punkten (Sperre "eichung").
- **[N] Nachtrag nach Sicht** (nachtrag-69/nachtrag.json, code/nachtrag_rk3.py, nicht eingefroren, beschreibend): Maxima
  nur ueber **ungesperrte** Punkte:

| ungesperrt | KW (1050) | B1-t1 (996) | V-A (946) |
|---|---|---|---|
| p_err | 1,5e-12 | 9,8e-9 | 2,0e-10 |
| err | 2,6e-12 | 4,0e-3 (kl = 0,01; ab kl = 0,03 im Raster <= 4e-10, BZ <= 9,0e-10) | 5,2e-6 |
| s_voll | 5,6e-16 | 3,3e-10 | 7,8e-16 |
| Eichidentitaeten auf W | 1,3e-7 | 5,3e-9 | 5,9e-9 |

  - Wo err gross ist, wird ein Test "unsicher" und der Punkt zaehlt fuer RT3 als gesperrt: B1 hat so 4 Punkte mehr (58 von
    1050 = 5,5 % [K]), V keinen (104 = 9,9 %).
- K5 = 0 exakt: Die Rechnung bei -k ist bitweise die konjugierte (Hloc reell) [M].

### 5.2 Instabile Eigenwerte (g > 1e-6 sicher) nach Art, alle Punkte (beschreibend, gesperrte eingeschlossen)

| Art | KW | B1-t1 | V-A |
|---|---|---|---|
| TT (zuordenbar bei abs(k) <= 0,25) | 0 | 0 | 1252 |
| Gitter, euklidisch auf dem Kreis (abs(z) = 1) | 0 | 0 | 1704 |
| Gitter, Schnitt (z reell negativ) | 0 | 5136 | 338 |
| Gitter, sonst komplex | 0 | 5981 | 54466 |
| N_inst je k im Raster (ungesperrt): min / max / Mittel | 0 / 0 / 0 | 8 / 12 / 9,41 | 52 / 56 / 55,30 |
| N_inst je k in der BZ: min / max / Mittel | 0 / 0 / 0 | 8 / 24 / 11,98 | 44 / 56 / 55,90 |

- V: Haeufigkeit im Raster 52 (31 Punkte), 54 (90), 56 (314); 52 = alle Gitter-Eigenwerte, 54 und 56 = dazu 2 bzw. 4
  TT-Eigenwerte ueber der Schwelle. BZ: 56 an 504 von 511 Punkten. B1: Raster 8 (312), 12 (169).
- Auf dem euklidischen Kreis liegen bei V je Betrag 98 Gitter-Eigenwerte auf 49 Punkten (im Mittel 2 je Punkt; bei
  kl = 0,005, 48 Punkte gesperrt, 96); ob es an jedem Punkt genau 2 sind, ist nicht gezaehlt. Beispiel x+,
  abs(k) = 0,05: z = -0,8390 - 0,5441 i und -0,8341 + 0,5516 i (abs(z) = 1,0000 [K]), also Arg z = -2,566 und +2,557 [K];
  REGIME-K-2-Zensus: Im omega = 2,566 [P].

### 5.3 Eigenwerte je Mode und k (Raster; g = abs(lambda) - 1; Maxima ueber die 49 Richtungen, gesperrte eingeschlossen)

| Betrag | KW TT-g | B1 TT-g | B1 Gitter-g | V TT-g | V Gitter-g | V TT zuordenbar | V gesperrt |
|---|---|---|---|---|---|---|---|
| kl = 0,005 | 1,5e-12 | 5,7e-10 | 22,14 | 6,9e-8 | 22,14 | 27 von 49 | 48 |
| kl = 0,01 | 9,7e-13 | 6,6e-9 | 22,14 | 2,6e-7 | 22,14 | 48 | 41 |
| kl = 0,02 | 5,3e-13 | 1,2e-13 | 22,14 | 2,1e-6 | 22,14 | 49 | 15 |
| kl = 0,03 | 1,6e-13 | 6,6e-8 | 22,14 | 7,1e-6 | 22,14 | 49 | 0 |
| kl = 0,05 | 1,4e-13 | 4,7e-14 | 22,14 | 3,3e-5 | 22,14 | 49 | 0 |
| kl = 0,07 | 1,6e-13 | 2,1e-14 | 22,14 | 9,0e-5 | 22,13 | 49 | 0 |
| kl = 0,1 | 9,7e-14 | 1,6e-14 | 22,14 | 2,6e-4 | 22,13 | 49 | 0 |
| kl = 0,14 | 1,1e-13 | 1,4e-14 | 22,14 | 7,3e-4 | 22,13 | 49 | 0 |
| kl = 0,2 | 6,2e-14 | 7,6e-15 | 22,14 | - | 22,14 | 0 | 0 |
| abs(k) = 0,05 | 7,9e-14 | 3,5e-14 | 22,14 | 9,5e-6 | 22,14 | 49 | 0 |
| abs(k) = 0,2 | 2,0e-14 | 1,2e-14 | 22,14 | 6,1e-4 | 22,13 | 49 | 0 |

- V-TT: von kl = 0,05 auf 0,1 Faktor 8,0, also ~k^3 [K]; bei abs(k) = 0,05 entspricht g = 9,5e-6 genau Im omega tau aus
  REGIME-K-2 (1,9e-4 x 0,05 [P, K]). Bei kl = 0,2 (abs(k) = 0,30) versucht die beschreibende Auswertung keine
  TT-Zuordnung: Der Code hat dort eine Schranke abs(k) <= 0,25, die nicht im Plan steht (Selbstanzeige 14; kein Urteil
  betroffen). [N] Ohne diese Schranke (nachtrag2) ist V-TT-delta bei kl = 0,2 bis 2,1e-3.
- B1-TT bei kl = 0,005, 0,01 und 0,03 (5,7e-10 bis 6,6e-8) schliesst gesperrte Punkte ein (B1 gesperrt: 29, 16, 7, 2 bei
  kl = 0,005, 0,01, 0,02, 0,03). [N] Nur ungesperrte Punkte: B1-TT-g <= 4,3e-13 (kl = 0,005, 20 Punkte), 5,4e-9
  (kl = 0,01, 33 Punkte; dort err bis 4e-3, also nicht belastbar), <= 1,3e-13 ab kl = 0,02. In REGIME-K-2 waren die
  B1-TT-Nullstellen bei 0,05 reell (<= 4,3e-13 [P]), hier 3,5e-14.
- [N] Nur ungesperrte V-Punkte: An **jedem** Rasterpunkt mit TT-Zuordnung sind alle uebrigen (Gitter-)Eigenwerte
  instabil (kl = 0,005 bis 0,14, abs(k) = 0,05 und 0,2: 1 + 8 + 34 + 7 x 49 Punkte [K]); bei kl = 0,2 (keine TT-Zuordnung)
  ist kein einziger Eigenwert stabil. In der BZ sind an jedem Punkt hoechstens 12 der 56 stabil. Zahl instabiler
  TT-Eigenwerte bei abs(k) = 0,05: 2 an 31, 4 an 17, 0 an 1 Richtung (nach Paaren: eine oder beide Polarisationen).
  B1: je ungesperrtem Rasterpunkt 8 bis 12 der 20 Gitter-Eigenwerte stabil, in der BZ 0 bis 16 der 24 Eigenwerte (dort
  ohne TT-Zuordnung).
- KW-TT gegen die Wuerfelgitter-Formel sinh^2(omega/2) = Summe sin^2(k_i/2): groesste relative Abweichung 6,3e-10
  (REGGE-WELLE-1 [P]).

### 5.4 BZ-Rand und Symmetriepunkte (beschreibend)

| Netz | BZ-Randpunkte (Wigner-Seitz) | g_max | N_inst max / Mittel | gesperrt | Symmetriepunkte: N_inst von 4 / 24 / 56 |
|---|---|---|---|---|---|
| KW | 169 | 1,6e-14 | 0 / 0 | 0 | X 0, M 0, R 0 (g <= 4,9e-17) |
| B1-t1 | 169 | 22,14 | 24 / 12,45 | 0 | X 8, M 8, R 24 |
| V-A | 61 | 22,14 | 56 / 55,15 | 0 | X 46, L 50, W 56, K 56, U 56 |

- Groesste Werte bei V am Randpunkt m = (0, 0, 4): z reell negativ bis -14385 (delta = pi), alle mit s_voll <= 4,3e-16.
- Das Feld "pfad_buendel" = 169 bei KW in auswertung.json zaehlt die statisch eliminierten Punkte mit (Code zaehlt jeden
  Pfad ausser "T"); kein KW-Punkt nahm den Buendel-Pfad.

## 6. Bedeutung [H] und was nicht gezeigt ist

- **Fuer Regime K als Hauptweg:** In der Lesart von REGGE-WELLE-1 (formale Fortsetzung, OS) ist die Zeltstangen-Treppe
  ueber V keine stabile Echtzeit-Dynamik. Es sind nicht einzelne Moden: An jedem ungesperrten Rasterpunkt sind alle 26
  Gitter-Freiheitsgrade (52 Eigenwerte) nicht positiv, in der BZ an 504 von 511 Punkten alle 56 Eigenwerte (an 7 Punkten
  sind 6 bis 12 positiv). Der TT-Sektor ist langwellig stabil (g ~ k^3 -> 0), aber nicht exakt.
  Damit ist Regime K **in dieser Bauart** (Treppe mit Hubfolge A, formale Fortsetzung) auf V nicht der Hauptweg.
- **Woran es liegt, Lesarten:**
  - Kuhn ist stabil (positiver Takt), also nicht Regge, nicht die Zeltstangen, nicht die formale Fortsetzung an sich.
  - B1 ohne Fuellung ist schon instabil (8 bis 24 von 24 je k); die Fuellung verstaerkt, sie verursacht nicht allein.
  - Zahlenspiel [H, nicht geprueft]: V hat 26 Gitter-Freiheitsgrade im Takt, und REGIME-K-2 fand 26 euklidische
    Gittermoden negativer Steifigkeit [P]. B1 hat 10 Gitter-Freiheitsgrade und 7 negative Moden [P]; instabil sind im Raster
    8 bis 12 der 20 Gitter-Eigenwerte (4 bis 6 Freiheitsgrade [K]), in der BZ 8 bis 24 der 24 Eigenwerte. Ob negative
    Steifigkeit und Nicht-Positivitaet dasselbe zaehlen, ist offen.
  - Ohne Zeitspiegelung hat der euklidische Takt keine Reflexionspositivitaet [L]; dann sind komplexe z erlaubt. Die
    ungeraden Terme der Treppe (REGIME-K-2) passen dazu.
- **Naechste Fragen (aus der Kartenbedeutung):** zeitspiegelsymmetrische Treppe (z. B. A und B abwechselnd) gegen
  Reflexionspositivitaet; geometrische Lorentz-Fortsetzung (zeitartige Zeltstangen, tau < Kantenlaenge, Courant-Bedingung);
  andere Fuellung oder ein Netz ohne negative Gittermoden. Erst dann laesst sich sagen, ob V als Netz ausscheidet.
- **Ausdruecklich nicht gezeigt:**
  - Lorentz-Regge mit zeitartigen Zeltstangen; gerechnet ist die formale Fortsetzung einer euklidischen Form.
  - Andere Hubfolgen, Hoehen, tau; die zeitspiegelsymmetrische Treppe.
  - Die kleinsten k bei V und B1 (gesperrt, numerisch, nicht physikalisch begruendet).
  - Was die nicht positiven Gittermoden in einer echten Echtzeit-Dynamik tun (wachsen, Geister, Zwangsbedingungen).
  - Materie, Umklappen, nichtlineare Stabilitaet, gekruemmter Hintergrund.

## 7. Selbstanzeigen

1. **Kontrollschwellen nach Rauchtest gelockert (vor dem Einfrieren, ohne Vorhersagewerte gesehen zu haben):** Sinus
   Vor-/Nach-Bedingungen 1e-8 -> 1e-5, Eichidentitaeten 1e-9 (ungeprojiziert) -> 1e-6 (auf W projiziert), Verschiebung
   durch die Verfeinerung 1e-4 -> 1e-2; dazu H_bb-Nullschwelle 1e-10 -> 1e-14 (strenger). Begruendet mit der gemessenen
   Rundungsskala (~k^-4) bzw. einer berichtigten Herleitung (PLAN 9), aber es sind Lockerungen nach Sicht auf
   Kontrollwerte. Die Schwellen der Vorhersagen RT0 bis RT3 sind unveraendert.
2. **Plan nach dem Rauchtest erweitert:** statische Elimination der Richtungen ohne Traegheit, Newton-Nachschaerfung auf
   der vollen 4D-Form mit Deflation, neue Sperre "verfeinerung", Fehlerschaetzung err = 2 x letzter Newton-Schritt
   (statt T gegen QZ). Ein zweiter Eigenwertweg (Begleitbuendel der vollen Form, r4) wurde probiert und verworfen.
3. **Festlegung mit Gewicht fuer RT0:** Die statische Kuhn-Richtung (formale Eigenwerte 0 und unendlich) zaehlt nicht als
   "physikalischer Eigenwert". Wer sie mitzaehlt, findet RT0 nicht entscheidbar (abs(lambda) ist dort nicht definiert).
4. **Vorwissen aus den Rauchtests:** Ich sah in r1 bis r5, dass Kuhn je k nur 4 propagierende Eigenwerte hat (eine
   statische Richtung, 2 nicht propagierende). Damit hing RT0 nur noch am TT-Paar, das REGGE-WELLE-1 schon als reell kennt;
   RT0 war danach weitgehend absehbar. Eigenwerte, delta oder Urteile habe ich vor dem Einfrieren nicht gesehen.
5. **Erratum im eingefrorenen PLAN 9:** Dort steht "r5 (eingefrorener Stand bis auf VERF_MAX)" und "Aenderung nach r5:
   VERF_MAX = 1e-2". Tatsaechlich lief r5 schon mit VERF_MAX = 1e-2: r5 und r6 nennen dasselbe rk3.py wie der eingefrorene
   Stand (sha256 b921377b...). Die Aenderung kam nach r4.
6. **Rauchtest r1:** Ein Shellfehler (Variable in einer Hintergrund-Untershell) startete zwei Rauchlaeufe nicht; die Shell
   versuchte Logs nach "/" zu schreiben und scheiterte (Permission denied). Nichts wurde geschrieben.
7. **Hintergrundwerkzeuge schrieben nach /tmp/claude-1000:** die Warteschleife (Bash im Hintergrund) und der Monitor legen
   ihre Ausgabe im Sitzungsordner unter /tmp/claude-1000/.../tasks/ ab (Werkzeugverhalten, kein eigener Schreibbefehl).
8. **Ein sinnloser Kopierbefehl** nach /dev/null (cp -p auswertung.sh /dev/null) scheiterte am Zeitstempel; geschrieben
   wurde nichts.
9. **Nach Sicht angesehen, nicht ausgewertet:** Waehrend der Hauptlaeufe habe ich einzelne Eigenwertlisten fertiger Teile
   mit jq gelesen (KW x+, fib05; B1 x+; V xy-, x+; V Symmetriepunkt U) und Sperren mit grep -c gezaehlt; die Urteile
   stammen nur aus auswertung.json. Abschnitt 5.2 nennt zwei Beispielwerte aus dieser Lesung (x+).
10. **RT3 knapp:** Die 10-%-Sperrgrenze (Plan, Nenner alle 1050 Punkte) hat RT3 knapp auswertbar gelassen (9,9 %). Alle
    Sperren liegen im Raster, wo Teil (a) vergleicht: dort V 19,3 %, B1 10,8 % [Leser]. Ich habe keine Regel geaendert.
11. **Nachtraege nach Sicht:** code/nachtrag_rk3.py (nach der Auswertung) und code/nachtrag2_rk3.py (nach dem Gegenlesen,
    GL-3), beide neu, nicht eingefroren, beschreibend; sie benutzen die eingefrorenen Funktionen ev, test, tt_zuordnung
    unveraendert. Je ein Lauf auf cpu10 (13:20:31 bis 13:20:33 und 13:36:38 bis 13:36:39 UTC). Nachtrag 1 stuetzt "alle 52
    Gitter-Eigenwerte" (Abschnitt 1 Punkt 3), Nachtrag 2 die Unabhaengigkeit von der Nachschaerfung (Punkt 2); kein Urteil
    haengt an ihnen.
12. **Werkzeuge lokal:** date, ssh, scp, sha256sum, jq (nur Lesen und Auswahl von Feldern), grep (auch -c zum Zaehlen),
    sed (Lesen; sed -n zum Zusammenfuegen von rk3.py vor dem Einfrieren), cp, mv, chmod, mkdir, ls, cat, tail, head, comm,
    sort, uniq, wc, cut, until-Schleifen mit sleep. Kein python, awk oder perl lokal; auf der .69 python nur ueber
    kleintest.sh. Heredocs nur gequotet.
13. **Schreibpfade:** RUNDE-37/regime-k-3/ (lokal) und /home/fmh/fmhc-physics-remote/regime-k-3/ (.69); sonst nur die
    Werkzeugausgaben aus Punkt 7. sed -i nur an eigenen Dateien (ERGEBNIS.md: Nummerierung, Dateiliste).
14. **Schranke nur im Code (GL-4):** Die beschreibende Auswertung (und Nachtrag 1) versucht die TT-Zuordnung nur bei
    abs(k) <= 0,25. Das steht nicht im Plan; es betrifft nur die Spalten der Tabellen 5.2 und 5.3 (V bei kl = 0,2), kein
    Urteil (RT1 nutzt abs(k) <= 0,1).
15. **K6 an nachgeschaerften Werten (GL-3):** Seit PLAN 9 vergleicht K6 die per Newton auf derselben Laurent-Form wie
    REGIME-K-2 nachgeschaerften Eigenwerte; die Uebereinstimmung auf 3,3e-13 ist daher zum Teil konstruktionsbedingt. Mit
    den unverfeinerten T-Eigenwerten waere die K6-Schwelle 1e-8 (PLAN 5) auf V verfehlt (1,6e-7 [N]); die Pipeline-Regel
    und damit die Urteile beruhen auf der nachgeschaerften Fassung. Fuer die Aussage "neben dem Kreis" aendert das nichts
    (TT-delta 9,5e-6 gegen Unterschied <= 1,6e-7).

## 8. Negativliste (was dieses Ergebnis nicht sagt)

- Nicht: "V ist in echter Zeit instabil" schlechthin (nur die Zeltstangen-Treppe mit Hubfolge A, formal fortgesetzt,
  OS-Lesart; keine Lorentz-Regge-Rechnung).
- Nicht: "die Gittermoden negativer Steifigkeit verursachen die Instabilitaet" (Zahlenspiel 26 = 26 nur als Hypothese;
  bei B1 passt es nicht eins zu eins).
- Nicht: "die Fuellung macht V instabil" (B1 ohne Fuellung ist ebenfalls instabil).
- Nicht: "Schwerewellen wachsen auf V merklich" (TT-g ~ k^3; bei kl = 0,05 rund 3e-5 je Takt).
- Nicht: "REGIME-K-2 hat sich verrechnet" (das Gegenteil: K6 nachgeschaerft auf 3,3e-13, unverfeinert auf 1,6e-7).
- Nicht: "alle Gittermoden von V sind an jedem k instabil" (an den ungesperrten Rasterpunkten ja; in der BZ an 7 von 511
  Punkten sind 6 bis 12 Eigenwerte stabil).
- Nicht: "B1 ist halb so instabil" (B1 hat im Mittel etwa ein Fuenftel so viele instabile Eigenwerte wie V, der groesste
  Wert ist gleich).
- Nicht: "an allen k gerechnet" (V: 104, B1: 54 Punkte bei den kleinsten k gesperrt).
- Nicht: "Kuhn hat drei propagierende Groessen" (die dritte ist statisch).
- Keine Messdatenbestaetigung.

## 9. Einfach gesagt

Wir haben ausgerechnet, was mit einer kleinen Stoerung passiert, wenn Finns Netz einen Zeitschritt nach dem anderen
macht. Auf dem einfachen Wuerfelnetz bleibt alles brav: Die Schwerewellen schwingen nur, nichts waechst. Auf Finns
gefuelltem Netz dagegen gibt es neben den Schwerewellen viele kleine Wackelformen des Netzes, und praktisch jede davon
schaukelt sich in dieser Rechenweise von Schritt zu Schritt auf. Auch die Schwerewellen selbst wachsen ein winziges
bisschen, umso weniger, je laenger die Welle ist. Das ungefuellte Netz hat das Problem auch, aber deutlich seltener (etwa
ein Fuenftel so viele wackelnde Formen). Fuer echte Zeit braucht Finns Netz also eine andere Bauart des Zeitschritts, eine
andere Rechnung, oder es scheidet als Netz aus.

## 10. Dateien

- KARTE.md (unveraendert), PLAN.md, PLAN.md.eingefroren-20261005-145643, EINGEFROREN-SHA256.txt, EINGEFROREN-SHA256-69.txt.
- code/: rk3.py (neu), rk.py, rk2.py, pt.py, ew.py, tp.py (unveraendert kopiert), kette.sh, rauch.sh, je mit
  *.eingefroren-20261005-145643; auswertung.sh (Startskript der Auswertung).
- rauch-69/: r1 bis r6 (json, log), rk3-stand-r3.py.txt, rk3-stand-r4.py.txt.
- nachtrag-69/: nachtrag.json, nachtrag.log, nachtrag2.json, nachtrag2.log, PRUEFSUMMEN-NACHTRAG.txt (Nachtraege nach Sicht;
  Skripte code/nachtrag_rk3.py, code/nachtrag2_rk3.py).
- lauf-69/: KW-raster, KW-bz, B1-t1-raster, B1-t1-bz, V-A-raster-0 bis -3, V-A-bz-0 bis -3 (json, log), auswertung.json
  und .log, kette-cpu8/9/10.txt, kette-auswertung.txt, nohup-*.txt, PRUEFSUMMEN-lauf-69.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/regime-k-3/ (code/, rauch/, lauf/).

## 11. Gegenlesen

- Frischer Leser (pruefer-opus, nur lesend, nach seiner Angabe 15:22:30 bis 15:34:12 CEST per date) gegen KARTE,
  eingefrorenen PLAN, ERGEBNIS, auswertung.json, nachtrag.json, Laufdateien, Logs, Pruefsummen und rk3.py.
- Urteil zur ersten Fassung: **OK MIT KLEINIGKEITEN.** Alle vier Urteile nach Plan und Wortlaut bestaetigt, ebenso die
  Zuordnung der Kartenbedeutung. Rund 340 Zahlen geprueft, 338 richtig, 2 ungenau (GL-7, GL-8); keine falsche Zahl
  beruehrt ein Urteil. EINGEFROREN-SHA256.txt 10 von 10, PRUEFSUMMEN-lauf-69.txt 30 von 30, Laufzeiten und Endzeiten
  bestaetigt.
- Umgesetzt (alle gegen die Belege nachgesehen):
  - GL-1: Klammer von RT2 als Lesart, nicht als "trifft zu" (Abschnitt 2).
  - GL-2: "alle Gitter-Eigenwerte" auf ungesperrte Rasterpunkte beschraenkt, BZ-Ausnahme (7 Punkte, 6 bis 12 stabil)
    genannt (Abschnitte 1, 2, 6, 8, 9).
  - GL-3: K6 als zum Teil konstruktionsbedingt gekennzeichnet; Nachtrag 2 (unverfeinerte T-Eigenwerte: 1,6e-7, TT-delta
    gleich) und Selbstanzeige 15.
  - GL-4: Schranke abs(k) <= 0,25 der beschreibenden Auswertung offengelegt (5.3, Selbstanzeige 14).
  - GL-5: Sperranteile im Raster (V 19,3 %, B1 10,8 %) zu RT3 und Selbstanzeige 10.
  - GL-6: "halb so stark" ersetzt (etwa ein Fuenftel so viele, gleiches Maximum).
  - GL-7, GL-8: Kreis-Zaehlung (96 bei kl = 0,005, "im Mittel 2"), B1-BZ-err 9,0e-10, "0 bis 16 der 24".
  - GL-9: Zahlenspiel B1 neu formuliert (4 bis 6 Freiheitsgrade im Raster).
  - GL-10: A6 "teilweise verfehlt".
  - GL-11: Abgabezeile; leere nohup-Dateien nicht in den Pruefsummen.
  - GL-12: "Einfach gesagt" nennt auch "V scheidet als Netz aus".
- Nicht vom Leser geprueft: vollstaendige Nachzaehlung aller Eigenwerte (nur Stichproben), die Physik der Schur- und
  Eichreduktion, Zeiten ohne Dateispur (14:13:04, 14:58:43, 15:17:18 CEST), die Dateien auf der .69.
- Die Umsetzung und Nachtrag 2 hat kein weiterer Leser gesehen. Pruefsummen der Nachtraege lokal gleich der .69-Liste
  (dort mit absoluten Pfaden, daher per Augenvergleich).

---
Abgabe: 2026-10-05 15:41:07 CEST (date). Zeitbox 150 min ab 14:13:04 CEST eingehalten. Kein Lauf mehr aktiv (letzter Lauf nachtrag2 endete 13:36:39 UTC). Geschrieben nur in RUNDE-37/regime-k-3/ und auf der .69 in /home/fmh/fmhc-physics-remote/regime-k-3/ (Ausnahme: Ausgabedateien der Hintergrundwerkzeuge, Selbstanzeige 7).
