# ZUS-10 Pruefplan (Runde 9, v3)

- **Schreibbeginn: 2026-09-30 08:18:57 CEST (date).** Ende: letzte Zeile (nach dem Schreiben gemessen).
- Pruefer: frischer Anthropic-Agent (Fable), nicht der Verfasser der Ideen. Auftrag: Leitung claude-primary.
- Grundlage: IDEEN-10.md, sha256 5d78822913055eb6fa04a1fe63dd2f9c4309b2da54d3e5f8144687aa259c2711, um 08:08:48 CEST
  geprueft (identisch mit der eingefrorenen Kopie -080653). Vorhersagen, Scheiterregeln und Gegenproben sind bindend.
- Gelesen vor diesem Plan: IDEEN-10.md; RUNDE-07.md, RUNDE-08.md, RUNDE-09.md; RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md
  (1 bis 4.6); RUNDE-08/gf-bic/ERGEBNIS.md (ganz, inkl. R9.1 bis R9.5); RUNDE-08/VORHERSAGEN-SP1.md; RUNDE-08/sp1/ERGEBNIS.md;
  RUNDE-09/koll1/PLAN.md und ERGEBNIS.md sowie die lin-Berichte in koll1/lauf-69/ (Stand 08:16); RUNDE-06.md (Z. 100 bis
  175); ERGEBNISSE-R6-A.md (R-2, per grep); ERGEBNISSE-R7-A.md (R5F-c) und
  RUNDE-07/r5f/lauf-69/ausgabe-kavitation/kavitation_raster_bericht.txt (Einzellaeufe); Code: bic2.py (Kopf, pole_omega,
  bruecke, main), gfbic.py (koeff, lin_g, fd_*, spektrum_stelle, ueberlapp, main), r5f.py (Kopf, Kavitation, main),
  t5k.py (ganz), tests1d_r3.py (Signaturen, gitter, ball, entwickeln, Messfunktionen); Laufzeiten aus den .69-Logs.
- Nicht geoeffnet: KS-1-Ergebnisse, T8-SOLL-*, vertraege-20260925/, ks-1-dk-lauf(e)/, Geheimnisordner.
- Rechenort: .69, Arbeitsordner /home/fmh/fmhc-physics-remote/runde9-zus10/ (Kopien der Skripte samt Nachbarmodulen;
  Originale unveraendert). Hauptspur cpu6; cpu2 sobald frei; p4000a/b nur fuer t5k (braucht CUDA). Je Aufruf
  hoechstens 10 min (kleintest.sh, RuntimeMaxSec 600). Aufrufketten als einfache Shell-Skripte im Arbeitsordner
  (kein Dienst, kein Timer, kein Hook), gestartet mit nohup aus meiner Sitzung.
- Lokal: kein python, python3, awk; JSON mit jq. Kein git, kein Journal.
- Vorab-Kostenschaetzung aus den Logs: `pole` ~85 s je omega^2 und Stufe (LAUF-P8: 3 Werte, 253 s); `bruecke` ~45 s je
  Dimensionspunkt (LAUF-R: 2 Punkte, 90 s); `ueberlapp` ~12 s je Rasterpunkt (R8: 44 Punkte in 547 s);
  `spektrum` ~250 s je Stelle mit vier g (R8), mit einem g geschaetzt ~130 s; Kavitation CPU ~1 ms je Schritt
  fuer 10 Laeufe x 2000 Punkte (LAUF3), also 75 Laeufe grob ~1 bis 2 min.

## Reihenfolge

1. Rechnungen mit fertigem Rechenweg: Ideen 1, 3, 4, 8 (Kette A auf cpu6, in dieser Reihenfolge; Kette B auf cpu2,
   sobald die Spur frei ist).
2. Papier und Literatur: Ideen 2, 5, 10 (parallel zu den Laeufen).
3. Kleine Codeaenderungen: Idee 9 (gfbic_delta.py, Kette C), Idee 7 (t5k_zus7.py, GPU-Spur mit Wartezeit).
4. Idee 6: nur Lesen von RUNDE-09/koll1/ (kein eigener Lauf). Stand 08:16: Die lin-Paarlaeufe still/0,76 (T = 2500
   bzw. 3500) und -gleich sind numerisch explodiert (Amplituden 1e40 und mehr); die Varianten -ungerade laufen noch.
   Liegt bis zu meinem Ende kein brauchbares Paar-Ergebnis vor, gilt "offen".

## Lesarten der Scheiterregeln (vor dem Ansehen der Ergebnisse festgelegt)

### Idee 1 (gfbic.py ueberlapp, zweite Leiter n = 6 bis 9)

- Aufrufe (cwd runde9-zus10, Spur cpu6):
  - `kleintest.sh cpu6 z1ua gfbic.py ueberlapp --xmin 0.545 --xmax 0.5625 --dx 0.0025 --hp 0.02 --g 0.2 --out aus-ueberlapp-fein-a`
  - `kleintest.sh cpu6 z1ub gfbic.py ueberlapp --xmin 0.5625 --xmax 0.580 --dx 0.0025 --hp 0.02 --g 0.2 --out aus-ueberlapp-fein-b`
  - Abweichung vom Vorschlag der Idee: `--g 0.2` statt der Vorgabe 0,0.2,0.5,1.0, damit die anschliessende Polpruefung an
    den Wechselstellen ins Zeitbudget passt (die Polpruefung ist keine Vorhersage der Idee, nur Zugabe).
  - Kontrolle bei Zeit: `--xmin 0.548 --xmax 0.577 --dx 0.001 --hp 0.02 --g 0.2 --out aus-ueberlapp-fein-c` (feineres
    Raster statt `--hp 0.01`; der Interpolationsfehler des 0,0025-Rasters ist die groessere Unsicherheit).
- Auswertung: Vorzeichenwechsel von I/A (Spalte "Vorzeichenwechsel ... linear interpoliert" im Bericht), je Fenster.
  Zuordnung n: der Wechsel im bzw. am naechsten beim Fenster n.
- Lesart der Regeln:
  - "mehr als 0,0003 ausserhalb ihres Fensters": scheitert, wenn |x_n - x_vorab| > (halbe Fensterbreite + 0,0003), also
    > 0,0006 fuer n = 6 und > 0,0005 fuer n = 7, 8, 9.
  - "das feine Raster bestaetigt 0,5752 und 0,5656": scheitert, wenn der Wechsel fuer n = 6 innerhalb +-0,0003 von
    0,5752 liegt und der fuer n = 7 innerhalb +-0,0003 von 0,5656 (beide).
  - "eine weitere Stelle dazwischen": mehr als ein Wechsel zwischen zwei aufeinanderfolgenden vorhergesagten Stellen
    (Fenster 0,5496 bis 0,5742).
  - "mittlerer Schritt 2,26 oder mehr": Mittel der drei Schritte in 1/(x - 0,5) von n = 6 nach 9 >= 2,26.
  - Mehrdeutig: Die Idee gibt "0,5742 +- 0,0003" als Fenster und zugleich "X-Fenster 20,37 bis 20,50"; ich nehme die
    omega^2-Fenster der Tabelle. Gemeldet.
- Gegenprobe (Papier): erste Leiter in X = 2 omega/(omega^2 - 1/2) an den bekannten Stellen n = 1 bis 5 nachrechnen
  (Hand); Z3 (0,551156) gegen 0,5558 / 0,5496 mit |c| < 0,02.

### Idee 3 (bic2.py bruecke, l = 1 bei omega^2 = 0,70)

- Aufrufe (zwei Teile wegen des Zeitbudgets, ~45 s je Punkt):
  - `kleintest.sh cpu6 z3ba bic2.py bruecke --geraet cpu --omega2 0.7 --l 1 --start 1.7777169-1.328e-5j --dims 1,1.25,1.5,1.75,2,2.1,2.2,2.3 --h 0.02 --budget 540 --out aus-bruecke-l1-070-a`
  - `kleintest.sh cpu6 z3bb bic2.py bruecke ... --start <rho bei d = 2,3 aus Teil a> --dims 2.3,2.4,2.5,2.6,2.7,2.8,2.9,3 --out aus-bruecke-l1-070-b`
  - Gegenprobe l = 0 (Start 1.4937770-6.716e-5j), dieselbe Teilung, nur wenn Spuren frei sind.
- Lesart:
  - "V-Minimum" in d = 2,3 bis 2,9: lokales Minimum von |Im rho| auf dem 0,1-Raster, dessen Wert mindestens 10-mal
    unter beiden Nachbarn (+-0,1) liegt. Die Vorhersage "mindestens 100-mal tiefer" pruefe ich getrennt als
    Zahlenvorhersage; fuer die Scheiterregel gilt die 10-fach-Schwelle (ein glattes Minimum gaebe Verhaeltnisse nahe 1).
  - Endpunkt: |Re rho(3) - 1,7635198| > 0,005 scheitert. Vorhersage-Zahl 1,76352 +- 0,001 getrennt.
  - Bricht die Spur ab (Newton ohne Konvergenz auch nach Halbierung), gilt "nicht entscheidbar" fuer den Endpunkt.
  - Schwaechere Aussage (zweites Minimum bei 1,9 +- 0,25) nur berichten.

### Idee 4 (bic2.py pole, l = 2 Rayleigh-Ast)

- Aufrufe (eine Stufe h = 0,02 statt 0,02,0,01 wegen des Budgets; je 2 bis 3 omega^2 je Aufruf):
  - `z4pa: pole --geraet cpu --l 2 --omega2 0.64,0.67,0.70 --h 0.02 --bereich alles --out aus-pole-l2-rayl-a`
  - `z4pb: pole --geraet cpu --l 2 --omega2 0.73,0.76 --h 0.02 --bereich alles --out aus-pole-l2-rayl-b`
  - `z4pc: pole --geraet cpu --l 2 --omega2 0.80,0.84,0.88 --h 0.02 --bereich resonanz --out aus-pole-l2-rayl-c`
  - `z4pd: pole --geraet cpu --l 3 --omega2 0.60,0.63,0.66 --h 0.02 --bereich alles --out aus-pole-l3-rayl`
- Auswertung: je omega^2 der tiefste l = 2-Pol (gebunden oder Resonanz) mit Re rho < 0,3; Kante 1 - omega.
- Lesart:
  - Uebertritt: erstes omega^2 des Rasters, bei dem der tiefste l = 2-Pol Resonanz (Im != 0, Re rho > 1 - omega) ist,
    und letztes, bei dem er gebunden ist; Uebertritt = Mitte, Unsicherheit = halber Rasterabstand. Scheitert, wenn
    dieses Intervall ganz ausserhalb 0,64 bis 0,78 liegt. Ist bei 0,64 schon Resonanz oder bei 0,76 noch gebunden und
    der Nachbarpunkt fehlt, gilt "nicht entscheidbar" fuer die Lage.
  - Steigung: aus den zwei kleinsten Raster-omega^2 mit Resonanz: d ln Gamma / d ln q mit q = sqrt((omega + Re rho)^2 - 1).
    Scheitert, wenn < 3 oder > 7. Gibt es nur einen Resonanzpunkt, "nicht entscheidbar".
  - V-Einbruch: Gamma < 1e-6 an einem Resonanzpunkt oberhalb der Kante scheitert.
  - Findet `pole` den tiefen Pol an einem Punkt nicht (weder gebunden noch Resonanz), zaehlt der Punkt als fehlend, nicht
    als Beleg.
  - Gegenprobe: l = 3 muss bei 0,60 bis 0,66 frueher uebertreten als l = 2 (also bei 0,66 schon Resonanz, waehrend l = 2
    bei 0,64 noch gebunden ist); sonst "Rayleigh-Deutung zweifelhaft" (kein Scheitern der Hauptregel).

### Idee 8 (r5f.py kavitation, S0 >= 1)

- Aufrufe:
  - `z8kv: r5f.py kavitation --geraet cpu --nur-vorhersage --teil raster --s0 0.68,0.70,0.72,0.75,0.80,0.85,0.90,0.95,0.98,0.99,1.05,1.2 --out aus-kav-vorhersage` (Keimtabelle F_b, x_halb; keine Zeitentwicklung)
  - `z8ka: r5f.py kavitation --geraet cpu --teil raster --s0 0.95,1.05,1.2 --stufe beide --T 600 --out aus-kav-raster-hoch`
    (75 Laeufe; fuer S0 >= 1 ist F_b nicht definiert, die Vorhersage wird "unklar", die Klasse heilt/kavitiert zaehlt).
- Lesart:
  - (a) "keine einzige Delle kavitiert" bei S0 >= 1: Klasse "heilt" in allen 24 Dellen je S0 (1,05 und 1,2), grob und
    fein. Scheitert, wenn eine Delle bei S0 >= 1,05 in der zweiten Laufhaelfte Klasse "zerfaellt" oder "Kaverne" hat.
  - (b) S0 = 0,95: Kavitation nur bei "deutlich breiteren" Dellen als bei 0,70 bis 0,80. Lesart: Bei 0,70 bis 0,80
    kavitieren Dellen ab w = 1 (tief) bzw. w = 2 (mittel). (b) gilt als getroffen, wenn bei 0,95 keine Delle mit w <= 2
    kavitiert; verfehlt, wenn eine mit w <= 2 kavitiert.
  - (c) F_b(S0) monoton wachsend fuer S0 -> 1 gegen 0,707 (+-5 %): aus der Keimtabelle. Hand: Der Grenzwert der
    bounce-Formel ist sqrt(2)/2 = 0,7071 (S_t -> 0).
  - (d) w* := x_halb(S0) der Keimtabelle (Halbbreite des kritischen Keims bei halber Tiefe); Dellenhalbbreite bei halber
    Tiefe = w sqrt(2 ln 2) = 1,177 w. Scheitert, wenn ein Fehltreffer 1,177 w > x_halb hat. Die zweite Haelfte von (d)
    ("alle richtig kavitierenden w >= w*") pruefe ich als Zahlenvorhersage getrennt. Hinweis: Die R7-Tabelle mit x_halb
    und w war beim Festlegen dieser Lesart schon gelesen (sie war noetig, um die Groessen zu kennen); ich melde das.
  - (e) 3D: nicht pruefbar hier, "nicht geprueft".
  - Gegenprobe P < 0 bei 0,70 bis 0,80: Hand, P = S0^2 (S0 - 1) (aus P = S U' - U nachgerechnet). F_b bei 0,68 am
    kleinsten: aus der Keimtabelle.

### Idee 9 (gfbic_delta.py, Massenverstimmung der zweiten Komponente)

- Codeaenderung nur in der Kopie gfbic_delta.py: neuer Parameter `--delta-m2` (Vorgabe 0), addiert auf die Diagonale
  des psi_2-Operators: koeff("psi2") -> U1(S) + delta; lin_g("psi2") -> dv + delta, d0 + delta; lu_zaehlung (L_u, L_v)
  + delta. Diff im Ergebnis.
- Aufrufe (nur g = 0,2, damit ~2 min je Lauf): `spektrum --stellen P1 --g 0.2 --delta-m2 {0,0.05,0.10,0.08}`.
- Lesart:
  - lambda(delta) = Im des rein imaginaeren Pols (Schiessen Stufe B, sonst A, sonst FD "instabil"). Scheitert, wenn bei
    delta = 0,10 eine instabile Mode (Im nu > 1e-7, lokalisiert) bleibt, oder lambda(0,05) ausserhalb 0,030 bis 0,042.
  - Kontrolle: delta = 0 muss 0,0462 (R8) reproduzieren; sonst ist die Kopie fehlerhaft und die Laeufe zaehlen nicht.
  - Gegenprobe delta -> -delta: ein Lauf mit -0,05, wenn Zeit bleibt (sonst nur Hand: die Formel ist gerade in delta).

### Idee 7 (t5k_zus7.py, Rest der Q/Anti-Q-Vernichtung)

- Neues Skript in der Kopie: Abstaende und T als Argumente; Stapel: Paar d = 4, 6, 8 (theta = 0), Paar d = 8 mit
  theta = pi/2, Einzelball d = 8 (Kontrolle); Messung alle 0,5: Q_abs in |x| < 75 (wie bisher), E in |x| < 15, Q links
  (x < 0), Q rechts (x > 0), psi(0), S_max; zwei Stufen grob/fein wie tests1d_r3. Auswertung im Skript: E15(t)/E15(0)
  bei t = 1000, 2000, 3000; Hauptfrequenz |Omega| aus dem Spektrum von psi(0, t) im Fenster t >= T/3;
  Vorzeichenwechsel von Q_links im Fenster t >= 1000; max |Q_links| und Korrelation Q_links gegen -Q_rechts dort.
- Spur p4000a oder p4000b (t5k braucht CUDA); Rauchtest mit --kurz auf cpu6 (m.DEV auf cpu umgestellt).
- Lesart:
  - Anfangsenergie = E in |x| < 15 bei t = 0 (bei d <= 8 liegen beide Baelle darin).
  - Scheitert, wenn E15(2000)/E15(0) < 0,005 (fuer d = 8, den Bezugslauf von Chem 14) oder |Omega| > 1 (feine Stufe;
    grob als L3-Kontrolle).
  - (a) getroffen, wenn E15(1000)/E15(0) >= 0,03 und E15(3000)/E15(1000) > 0,5. (b) 0,75 <= |Omega| <= 1,0.
    (c) >= 10 Vorzeichenwechsel von Q_links mit Q_links ~ -Q_rechts, sonst neutral mit max |Q_links| < 0,01.
    (d) E15(3000)/E15(0) bei d = 4 und 6 groesser als bei d = 8.
  - Ist die GPU-Spur bis zu meinem Ende belegt, gilt "nicht geprueft (Spur belegt)".

### Ideen 2, 5, 10 (Papier, Literatur)

- Idee 2: (a) und (d) von Hand pruefen (O(4)-Stationaritaet; Quellfrequenzen des Paarterms; Grenzfall alpha -> 0 gegen
  das lineare psi_2-Problem). (b), (c) brauchen die Codeerweiterung (1 bis 2 h laut Idee): ausserhalb des Zeitrahmens,
  "nicht geprueft". Literatur zu Ladungstausch-Q-Baellen mit Idee 7 zusammen.
- Idee 5: k-Tabelle von Hand nachrechnen; Gesetz A ~ t^(-1/(2k-2)) aus Fluss ~ eps^(2k) von Hand; Literatur
  (Soffer/Weinstein 1999, Bambusi/Cuccagna 2011, Manton/Merabet 1997) per WebSearch/WebFetch an der Quelle: zaehlt nur
  als [L], wenn ich Abstract oder Volltext selbst gelesen habe. Die nichtlineare Rechnung (koll1.py mit l = 2, > 10 min,
  Codeaenderung) mache ich nicht: zweite Scheiterregel "nicht geprueft".
- Idee 10: Gordon-Metrik g_0i von Hand (Faktor 4); Praezessionsverhaeltnis GP-B/LAGEOS von Hand; Literatur Garat/Price
  2000, Visser/Weinfurtner 2005 und Suche nach einer exakten Gordon-Darstellung von Kerr per WebSearch/WebFetch.

### Idee 6 (nur Lesen)

- Vorhersage-Zahlen |sin(qd)/(qd)| bei q = 2,3999: von Hand nachrechnen. Ergebnis der KOLL-1-Zeitlaeufe aus
  RUNDE-09/koll1/ (ERGEBNIS.md, lauf-69/*bericht.txt) am Ende erneut lesen. Scheiterregel: kollektive Mode mit
  Gamma < 0,5 Gamma0 bei 0,76 und d >= 10. Lesart: Gamma der symmetrischen und antisymmetrischen Paar-Mode aus dem
  Abklingen der Summe a^2 (Gamma_Summe im Bericht), Gamma0 = Einzelball (1,995e-3). Explodierte Laeufe (Amplituden
  wachsen exponentiell) zaehlen nicht als Ergebnis.

## Abbruchkriterien

- Zeitrahmen etwa zweieinhalb Stunden ab 08:08 (also bis etwa 10:40 CEST). Danach: offene Laeufe werden nicht mehr
  gestartet; was fehlt, ist "nicht geprueft" mit Grund.
- Ein Arm, der mit technischem Fehler endet, wird einmal repariert (dokumentiert), nicht durch einen Platzhalter ersetzt.

**Ende des Plans: siehe date-Zeile unten (nach dem Schreiben gemessen).**

**Ende des Plans: 2026-09-30 08:20:52 CEST (date, nach dem Schreiben gemessen).**

## Nachtrag 2026-09-30 10:10:59 CEST (date)

- Kette A2, Teil b von Idee 3 (Lauf z3bb, aus-bruecke-l1-070-b, LAUF-z3bb.log): **ungueltig**, nicht bewertet. Grund: `seq -s,` erzeugte unter deutscher Locale Dezimalkommas (dims 2,3,2,4,...,3,0), bic2.py trennt an ",". Befund Codex (status-audit-20260930/codex-wm1/VIER-BEFUNDE-PRAEZISE.txt). Reparatur: kette-zus10-a3.sh (explizite Liste, LC_ALL=C, Argumentliste vor dem Start ausgegeben), Lauf z3bc.
- Idee 7: erster Rauchtest (z7rauch) technisch gescheitert (CUDA-Sync in tests1d_r3.uhr auf der CPU). Reparatur nur in t5k_zus7.py (eigene Zeitfunktion), Fremdmodul unveraendert; Rauchtest z7rauch2 und GPU-Lauf z7gpu danach.
- Pause der Leitung 08:37 bis 09:51 CEST; Zeitrahmen danach etwa 90 min.
