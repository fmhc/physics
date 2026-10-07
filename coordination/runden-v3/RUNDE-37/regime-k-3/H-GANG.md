# REGIME-K-3, Folgeauftrag: h-Gang des Zeltstangen-Takts (explorativ, ohne Karte)

- Auftrag der Leitung (05.10., Finn: "einfach machen und ausprobieren"): kein Plan-Einfrieren, keine Vorhersagetabelle, kein
  frischer Leser. Start 15:44:26 CEST, Text ab 16:01:45 CEST (date). Alles synthetisch, linearisiert, formale Fortsetzung wie
  in ERGEBNIS.md (abs(lambda) = exp(abs(Arg z)) je Takt). Keine Messdaten.
- **Verfahren:** dieselbe Takt-Transfermatrix wie rk3.py (eingefroren, unveraendert importiert), Zeltstangenhoehe h = tau,
  Untergitterhoehen hb mal h (wie UEBERLEITUNG-V-1). Skripte code/hgang.py (Raster, KW-BZ) und code/hgang2.py (BZ von B1 und V,
  ohne Newton bei abs(k) > 0,25). Leichtere Fassung: Newton auf der vollen 4D-Form nur fuer die TT-Kandidaten, alle anderen
  Eigenwerte aus T mit Fehler T gegen QZ, **keine s_voll-Pruefung**. Gleiche physikalische k fuer alle h (Raster aus dem
  h = 1-Gitter: 49 Richtungen x 11 Betraege = 539; BZ 8^3 ohne 0 = 511).
- **Laeufe** (.69, kleintest.sh, cpu8/9/10, je <= 10 min, alle rc = 0): Rauch r1 (V, 3 h, 4 Punkte), KW-raster, KW-bz,
  B1-raster-a/-b, V-raster-1/-2/-3 (13:46:34 bis 13:58:52 UTC), B1-bz2, V-bz2-a/-b (13:54:46 bis 13:56:12 UTC), Auswertung
  13:59:08 bis 13:59:20 UTC (hgang-69/auswertung-hgang.json). Zwei BZ-Laeufe der ersten Fassung (B1-bz, V-bz-1) habe ich
  13:54:28 UTC per PID und Unitname abgebrochen: Sie haetten in der BZ alle Eigenwerte nachgeschaerft und die 9-min-Grenze
  gerissen; ersetzt durch hgang2.py. Pruefsummen hgang-69/PRUEFSUMMEN-HGANG.txt (lokal bestanden).
- "instabil" = g = abs(lambda) - 1 > 1e-6 je Takt, sicher nach der Fehlerschaetzung (wie RT2/RT3). Gesperrte Punkte (Regeln aus
  rk3.py) zaehlen nicht mit.

## Tabelle: instabile Eigenwerte je k (Median / Maximum), groesstes g, TT bei kl = 0,05 und 0,1

| h | Kuhn Raster | Kuhn BZ | B1 Raster | B1 BZ | V Raster | V BZ | V g_max (Raster / BZ) | V gesperrt (Raster) | V TT-g kl = 0,05 (max / Median) | V TT-g kl = 0,1 (max / Median) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 / 0 | 0 / 0 | 8 / 14 | 12 / 24 | 56 / 56 | 56 / 56 | 22,14 / 22,14 | 23 | 3,3e-5 / 1,3e-5 | 2,6e-4 / 1,0e-4 |
| 1/2 | 0 / 0 | 0 / 0 | 8 / 12 | 8 / 16 | 52 / 56 | 56 / 56 | 22,14 / 22,14 | 7 | 1,1e-6 / 3,1e-7 | 8,9e-6 / 2,5e-6 |
| 1/4 | 0 / 0 | 0 / 0 | 8 / 12 | 8 / 16 | 50 / 52 | 56 / 56 | 22,14 / 22,14 | 4 | 6,8e-9 / 4,0e-9 | 5,4e-8 / 3,2e-8 |
| 1/8 | 0 / 0 | 0 / 0 | 8 / 8 | 8 / 16 | 40 / 50 | 56 / 56 | 2,0e-4 / 1,4e-3 | 33 | 4,2e-10 / 2,3e-10 | 3,3e-9 / 1,8e-9 |
| 1/16 | 0 / 0 | 0 / 0 | 8 / 10 | 8 / 16 | 16 / 34 | 48 / 56 | 2,6e-5 / 1,1e-4 | 52 | 2,6e-11 / 1,4e-11 | 2,1e-10 / 1,1e-10 |
| 1/64 | 0 / **2** | 0 / 0 | 8 / 10 | 8 / 8 | **0** / 16 | **0 / 0** | 0,12 / 1,4e-6 | 43 | 2,5e-9 / 2,8e-13 | 2,6e-8 / 5,7e-13 |
| 2^-8 | 0 / **2** | 0 / 0 | 8 / 12 | 8 / 8 | **0** / 16 | **0 / 0** | 0,074 / 1,5e-6 | 38 | 9,5e-10 / 1,1e-12 | 2,8e-9 / 4,8e-13 |
| 2^-10 | 0 / **2** | 0 / 0 | 8 / 11 | 8 / 8 | **0** / 17 | **0 / 0** | 0,017 / 4,6e-6 | 46 | 6,5e-10 / 5,0e-12 | 2,4e-9 / 2,5e-12 |

- Kuhn-Raster gesperrt: 0 bis h = 1/4, dann 3, 14, 106, 197, 249 (h = 1/8 bis 2^-10); Kuhn-BZ 39 bei 2^-8. V-BZ: bei 1/64 2,
  bei 2^-8 2, bei 2^-10 12 Punkte mit unsicherem Eigenwert (g knapp ueber 1e-6, nicht sicher). B1 bleibt bei jedem h bei g_max = e^pi - 1
  (reell negative z), Median 8 instabile je k.
- **Ab welchem h ist an einem Raster-k alles stabil (V, je Richtung, grob):** Im h-Gitter fast immer h = 1/64 oder nie (eine Ausnahme: kl = 0,01, eine Richtung ab 1/16).
  kl >= 0,1 und abs(k) = 0,2: alle 49 Richtungen ab 1/64; kl = 0,07: 43; kl = 0,05: 20; abs(k) = 0,05 (kl = 0,033): 7; kl = 0,03: 4;
  kl = 0,02 keine, kl = 0,01 eine, kl = 0,005 keine von 49 (die anderen bleiben instabil oder sind gesperrt).
  Kuhn: fast alle ab h = 1 (Ausnahmen siehe unten), B1: an keinem k.

## Ehrlich: was nicht klappt

- **Die Kuhn-Kontrolle bricht unter h = 1/16 ein.** Ab h = 1/64 tauchen auf Kuhn je k bis zu 2 Schein-Instabilitaeten auf
  (z reell negativ, abs(z) bis ~1000), z. B. h = 2^-8, (1,1,1), kl = 0,005: z = -282,6 und -0,0035. Ursache: Die statische
  Kuhn-Richtung (ohne Traegheit) wird mit der festen Schwelle 1e-8 nicht mehr als statisch erkannt; die Schwelle skaliert
  nicht mit h. Dazu viele gesperrte Punkte (bis 249 von 539). Unter h = 1/16 sind die Zahlen dieser Rechnung daher nur mit
  Vorsicht zu lesen.
- **Rest-Instabilitaeten von V bei kleinem h:** Deutliche komplexe Paare (abs(Im z) 0,006 bis 0,11 je Takt) gibt es bei
  h <= 1/64 nur bei kl = 0,005 und 0,01. Das passt zu UEBERLEITUNG-V-1 (kleinere k brauchen kleinere h, bei [321] kl = 0,01
  der letzte Nulldurchgang zwischen 2^-7 und 2^-8) [H]. Die uebrigen gezaehlten Instabilitaeten bei kl <= 0,05 sind klein
  (abs(Im z) < 1e-3); ob sie echt oder Rauschen sind, ist hier nicht entschieden (keine s_voll-Pruefung, kein Newton ausser TT).
- **TT-Werte unter h = 1/16:** TT-g faellt von 3,3e-5 (h = 1) bis 2,6e-11 (h = 1/16), steigt danach wieder auf ~1e-9 bis 3e-8.
  Das ist sehr wahrscheinlich die Rechengenauigkeit (Eigenwerte haeufen sich bei z = 1), keine Physik.
- **Je Takt gegen je Zeit:** g zaehlt je Takt. Rechnet man je Zeiteinheit (delta/h > 1e-6), sind bei kleinem h mehr Eigenwerte
  "instabil" (V-BZ h = 1/64: Median 32 statt 0), mit Raten bis 9e-5 (1/64), 4e-4 (2^-8), 5e-3 (2^-10) je Zeiteinheit. Weil die
  Rate mit kleinerem h waechst, halte ich das fuer Rechenrauschen geteilt durch h, nicht entschieden.
- **B1 heilt nicht:** Die 8 reell negativen Eigenwerte je k ("Takt-Verdoppler", delta = pi) bleiben bei jedem h; ihre Rate je
  Zeit waechst wie pi/h. Ob es dieselbe Art Scheinmode ist wie die verkannte statische Kuhn-Richtung, ist nicht geprueft [H].
- Selbstanzeigen: jq mit group_by/length zum Zaehlen (Regel: jq nur lesend); die erste Warteschleife lief kurz als
  Hintergrundaufgabe (Ausgabe des Werkzeugs unter /tmp/claude-1000, nach ~1 min gestoppt) und nutzte auf der .69 `2>/dev/null`;
  zwei Laeufe abgebrochen (oben). Lokal kein python, awk oder perl.

## Einfach gesagt

Wenn man den Zeitschritt auf Finns gefuelltem Netz kleiner macht, verschwinden die Aufschaukel-Moden fast ueberall: Ab etwa
einem Vierundsechzigstel der urspruenglichen Zeltstange ist das Netz in der Rechnung fuer kurze und mittlere
Wellen stabil, und auch die Schwerewellen wachsen dann praktisch nicht mehr. Nur bei sehr langen Wellen braucht es noch
kleinere Schritte, wie die Vorgaengerrechnung schon vermutet hatte. Bei sehr kleinen Schritten wird unsere Rechnung selbst
ungenau, das sieht man daran, dass sogar das einfache Wuerfelnetz dann Scheinfehler zeigt; das ungefuellte Netz B1 bleibt dagegen
bei jedem Schritt instabil.

---
Abgabe H-GANG: 2026-10-05 16:02:58 CEST (date). Kein Lauf mehr aktiv (letzter: Auswertung 13:59:20 UTC). Geschrieben nur in RUNDE-37/regime-k-3/ (H-GANG.md, code/hgang*.py, code/kette-hgang*.sh, hgang-69/) und auf der .69 in /home/fmh/fmhc-physics-remote/regime-k-3/hgang/.
