# LEITER-1D: Ergebnis (Code-Agent, Runde 25, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 02:26:08 CEST (date).
- Rauchlaeufe (Parameter in keinem echten Lauf): .69, 00:45:32 bis 00:48:10 UTC, alle rc = 0 (PLAN.md Abschnitt 4).
- Plan eingefroren 02:50:22 CEST (PLAN.md.eingefroren-20261003-025022, code/*.eingefroren-20261003-025022), nach den
  Rauchlaeufen und vor jedem echten Lauf. Plan, Code und Startskripte sind seither unveraendert (sha256, Kontrollen).
- **Phase 1** (k0, drei Scans, Uebersicht): .69, 00:50:26 bis 00:52:48 UTC, fuenf Aufrufe, alle rc = 0.
- **Phase 2** (Sprossen auf h = 0,02, h = 0,01 und h = 0,01 mit D = 40): 00:52:55 bis 00:53:23 UTC, drei Aufrufe, rc = 0.
- **Phase 3** (DOP853-Gegenprobe, mechanische Regel): 00:53:41 bis 00:53:47 UTC, rc = 0. Urteile in
  lauf-69/auswertung.json.
- Geschrieben ab 02:57:32 CEST (date); Ende in der letzten Zeile.
- Markierungen: [A] Festlegung des Code-Agenten (im Plan vor den Laeufen), [H] Deutung/Hypothese. Alles gilt im
  linearen Zweikanalmodell des 1D-Q-Balls (M1, beta = 1/2): numerische Evidenz im Modell, keine Messung.

## Ergebnis zuerst

1. **Die stille Leiter gibt es auch in 1D.** In eps = omega^2 - 1/2 aus [1e-7; 0,05] liegen fuenf stille Stellen, bei
   eps = 6,0e-3, 8,8e-4, 8,0e-5, 8,1e-6 und 8,1e-7.
   - Jede hat auf beiden Stufen (h = 0,02 und 0,01) einen Vorzeichenwechsel von F2 entlang der F1-Nullstellenlinie und
     einen aufgeloesten Umlauf +-1 (groesster Phasensprung 0,10 bis 0,36 rad).
   - Die Paritaet wechselt von Sprosse zu Sprosse (gerade, ungerade, gerade, ungerade, gerade).
   - Je Paritaet wechselt der Umlauf: gerade +1, -1, +1; ungerade +1, -1. L1D-1 ist eingetroffen.
2. **Der Abstand ist der der ebenen Wand.**
   - Die Schritte in ln(1/eps) sind, von grossem zu kleinem eps: 1,9163, 2,3945, 2,2892, 2,3141.
   - Die zwei Schritte bei kleinstem eps liegen -0,90 % und +0,18 % neben 2,3100. L1D-2 ist eingetroffen.
   - Jede Sprosse liegt also etwa zehnmal naeher an omega_min als die vorige (eps-Verhaeltnis 0,091 bis 0,101; der
     erste Schritt 0,147).
3. **Die Frequenzen laufen auf rho_z zu, abwechselnd von beiden Seiten.**
   - rho_n - rho_z = -0,0450, +0,00696, -0,00175, +0,000275, -0,0000572: gerade Sprossen liegen darunter, ungerade
     darueber, der Abstand faellt streng.
   - Die Sprosse mit dem kleinsten eps liegt 5,7e-5 neben 1,52415. L1D-3 ist eingetroffen.
4. **Die Numerik ist in 1D unkritisch.**
   - Stufen: hoechstens 2,9e-7 in ln(1/eps) und 3,4e-9 in rho.
   - Zweites Verfahren (DOP853, adaptiv): hoechstens 1,9e-8 und 2,3e-10. Gebiet D = 40 statt 30: hoechstens 3e-12.
   - Das Profil ist exakt (geschlossene Quadratur der ersten Integralform).
5. **G2-10 bestaetigt, aber nur fuer grosses eps.**
   - Fuer omega^2 0,55 bis 0,70 gibt es keine Stelle; dort hat F2 auf beiden Aesten ein festes Vorzeichen.
   - Der gerade Ast stimmt mit G2-10 auf 2,8e-6 bis 4,5e-6 ueberein.
   - Die Leiter beginnt erst bei eps = 6,0e-3, also unterhalb des alten Suchbereichs.
   - Nachtraeglich [H]: Nach dem G2-10-Kriterium hat der 1D-Ball fuer kleines eps sehr wohl eine Innenbarriere (Bedeutung,
     Einschraenkung 1).

## Vorab gegen Ausgang

Mechanisch nach PLAN.md Abschnitt 6 (Kommando regel, lauf-69/auswertung.json). K0 bestanden (Profil und ebene Wand).

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| L1D-1 | In eps [1e-7; 0,05] mindestens drei stille Stellen (beide Paritaeten zusammen), mit aufgeloestem Umlauf | 65 % | **eingetroffen**: fuenf Sprossen, alle auf beiden Stufen, Umlauf +-1 aufgeloest und gleich |
| L1D-2 | Die zwei kleinsten-eps-Schritte Delta ln(1/eps) innerhalb +-10 % von 2,3100 | 45 % | **eingetroffen**: 2,3141 (+0,18 %) und 2,2892 (-0,90 %) |
| L1D-3 | Frequenzen laufen mit fallendem eps auf rho_z zu; Sprosse mit kleinstem eps innerhalb 0,005 von 1,52415 | 50 % | **eingetroffen**: abs(rho_n - rho_z) = 0,0450 > 0,00696 > 0,00175 > 0,000275 > 0,0000572; Abstand zu 1,52415: 5,7e-5 |

- Auslegungen [A], vor den Laeufen festgelegt: "die zwei kleinsten-eps-Schritte" = die zwei Schritte mit den kleinsten
  eps; "laufen zu" = abs(rho_n - rho_z) faellt streng entlang fallender eps.
- Gegenlesart (nicht gewertet): Die zwei Schritte bei groesstem eps (1,9163 = -17,0 %, 2,3945 = +3,7 %) laegen nicht
  beide im Band.

**Bedeutung (nach Karte):** L1D-1 und L1D-2 treffen ein:
- "Die stille Leiter gibt es auch in 1D. Dafuer reicht die ebene Wand mit stehender Innenwelle; eine Kruemmung oder
  'Innenbarriere' ist nicht noetig. In 1D liegen die Sprossen geometrisch dicht (Faktor ~0,1 in eps) [H]. Die
  Projekt-Erklaerung 'ohne Innenbarriere keine Leiter' (G2-10) ist dann ueberholt."

**Einschraenkungen:**
1. **"Innenbarriere nicht noetig" zeigt dieser Test nicht** [H, nachtraeglich, nicht im Plan].
   - G2-10 nennt als Barriere B = dp(S0) - (omega - rho)^2 > 0 in der Ballmitte, dp(S) = 1 - 4S + 4,5 S^2.
   - Ich habe B nachtraeglich mit jq entlang der Hauptaeste ausgewertet, mit S0 = 1 - sqrt(2 eps) und dem rho des Astes
     (G2-10 setzte statt (omega - rho)^2 den 3D-Wert c(eps)^2 ein).
   - Ergebnis: B > 0 fuer eps bis 0,042 (gerader Ast) bzw. 0,017 (ungerader Ast), darueber negativ. An allen fuenf
     Sprossen ist B = 0,42 bis 0,83.
   - Ueberholt ist damit die Annahme "in 1D fehlt die Innenbarriere". Sie gilt nur oberhalb von eps 0,017 bzw. 0,042,
     also auch dort, wo G2-10 suchte (0,05 bis 0,2).
   - Ob die Leiter ohne Barriere existieren kann, bleibt offen. Im Wandbild ist B > 0 dasselbe wie ein reelles kappa_in,
     also Teil des Mechanismus der ebenen Wand und keine Alternative zu ihm [H].
2. **Ohne Kruemmung geht es:** Die Sprossen entstehen in 1D, und Lage und Abstand folgen der ebenen Wand. Das ist der
   belastbare Teil der Bedeutung.
3. **Geltungsbereich:** nur M1 bei beta = 1/2, linear, eine Methode (W-Abbildung), zwei Integratoren.
   - Die naechste Sprosse waere bei ln(1/eps) ~ 16,34 (eps ~ 8e-8), unterhalb des Suchbereichs; nicht gerechnet.
   - Die Leiter reicht nicht bis eps = 0,05: Die groesste Sprosse liegt bei 6,0e-3.

## Sprossen (Lage aus h = 0,01, D = 30)

rho_z = 1,5241497621. "Schritt" = ln(1/eps) bis zur naechsten Sprosse mit kleinerem eps. Paare: fein / grob.

| Nr | Paritaet | ln(1/eps) | eps | omega^2 | rho | rho - rho_z | Umlauf | Schritt | eps-Verhaeltnis |
|---|---|---|---|---|---|---|---|---|---|
| 1 | gerade | 5,11778357 | 5,989e-3 | 0,50598928 | 1,479131799 | -4,502e-2 | +1 / +1 | 1,91631574 | 0,147 |
| 2 | ungerade | 7,03409931 | 8,813e-4 | 0,50088131 | 1,531110484 | +6,961e-3 | +1 / +1 | 2,39453320 | 0,091 |
| 3 | gerade | 9,42863251 | 8,039e-5 | 0,50008039 | 1,522399051 | -1,751e-3 | -1 / -1 | 2,28917953 | 0,101 |
| 4 | ungerade | 11,71781204 | 8,147e-6 | 0,50000815 | 1,524425143 | +2,754e-4 | -1 / -1 | 2,31406051 | 0,099 |
| 5 | gerade | 14,03187254 | 8,054e-7 | 0,50000081 | 1,524092563 | -5,720e-5 | +1 / +1 | - | - |

| Nr | Stufen grob - fein: d ln(1/eps) / d rho | D = 40 - D = 30 | DOP853 - RK4 (fein) | groesster Sprung (rad) | Punkte / Runden | min abs(F) am Rand | Aussen-Iterationen |
|---|---|---|---|---|---|---|---|
| 1 | 1,06e-7 / 3,4e-9 | 6e-15 / 4e-16 | -7,0e-9 / -2,2e-10 | 0,098 | 240 / 0 | 0,024 | 8 |
| 2 | 1,83e-7 / 8,5e-10 | 4e-15 / 2e-16 | -1,22e-8 / 5,6e-11 | 0,166 | 240 / 0 | 0,019 | 5 |
| 3 | 2,10e-7 / 2,6e-10 | -3,0e-12 / -1e-15 | -1,40e-8 / -1,8e-11 | 0,184 | 240 / 0 | 0,040 | 4 |
| 4 | 2,53e-7 / 5,5e-11 | 2e-14 / -2e-16 | -1,69e-8 / 3,5e-12 | 0,353 | 247 / 2 | 0,020 | 3 |
| 5 | 2,92e-7 / 4,0e-12 | 4e-14 / 0 | -1,94e-8 / -4,3e-13 | 0,355 | 246 / 2 | 0,039 | 3 |

- **Umlauf:** Rechteck rho_c +- 0,01, ln(1/eps)_c +- 0,5 um die lineare Lage aus dem feinen Scan, fuer beide Stufen
  dasselbe. Die Summen sind +-1,0000 auf beiden Stufen; die groben Spruenge weichen von den feinen um <= 1,3e-7 rad ab.
  Der D = 40-Lauf gibt dieselben Umlaeufe.
- **Konsistenz der Fehler:** RK4 hat Ordnung 4. Mit grob - fein = 15 x Fehler(fein) folgt Fehler(fein) = 7e-9 bis 1,9e-8
  in ln(1/eps). DOP853 misst -7,0e-9 bis -1,94e-8, passend in Betrag und Vorzeichen.
- **Gleiche Paritaet:** gerade 1 -> 3 -> 5: Schritte 4,3109 und 4,6032 (2 b = 4,6200); ungerade 2 -> 4: 4,6837.
- **Scan:** Je eps und Paritaet gibt es genau eine F1-Wurzel in [1,30; 1,70] (2001 Punkte). Ausnahme: ungerade bei
  eps >= 0,119 (j >= 243), dort laeuft der Ast oberhalb von 1,70 hinaus. Alle Wurzeln beider Stufen sind konvergiert
  (je 496). Fein und grob stimmen auf <= 4,9e-10 in rho.
- **F2 auf dem Ast:**
  - gerade: schwingt mit Periode ~9,2 in ln(1/eps) und Amplitude ~0,12. Oberhalb der ersten Sprosse ist F2 < 0, mit
    Extremum -0,112 bei eps = 0,032; danach faellt abs(F2) monoton bis 0,011 bei eps = 0,2.
  - ungerade: Amplitude ~0,06. Oberhalb von eps = 8,8e-4 ist F2 > 0, mit Extremum 0,056 bei eps = 0,0084; danach faellt
    F2 monoton bis 0,011 am Fensterrand (eps = 0,112) und 0,0027 bei omega^2 = 0,70 (k0, ganzes Fenster).
  - Beide Aeste naehern sich also zum Rand eps = 0,2 hin der Null, ohne sie zu erreichen. Ob jenseits von omega^2 = 0,70
    weitere Stellen liegen, ist nicht gerechnet.

### Nullstellenlinie (Hauptast) gegen rho_z

Groesste Abweichung abs(rho - rho_z) je Dekade in eps (40 Punkte je Dekade; [0,1; 0,2] angebrochen):

| Ast | rho bei eps = 1e-7 | [1e-7, 1e-6) | [1e-6, 1e-5) | [1e-5, 1e-4) | [1e-4, 1e-3) | [1e-3, 1e-2) | [1e-2, 1e-1) | [0,1; 0,2] |
|---|---|---|---|---|---|---|---|---|
| gerade | 1,5242588 (+1,09e-4) | 1,13e-4 | 9,9e-4 | 1,82e-3 | 8,16e-3 | 6,39e-2 | 0,155 | 0,144 (13 Punkte) |
| ungerade | 1,5241518 (+2,0e-6) | 8,7e-5 | 3,4e-4 | 2,27e-3 | 7,22e-3 | 3,09e-2 | 0,152 | 0,171 (3 Punkte) |

- Die Linie laeuft fuer eps -> 0 gegen rho_z, die Kontrolle der Karte ist erfuellt.
- Meine Erwartung [A] im Plan war: Abweichung bei 1e-7 < 0,01 und je Dekade fallend.
  - Beim ungeraden Ast ist sie erfuellt.
  - Beim geraden Ast ist sie erfuellt bis auf die angebrochene oberste Dekade (0,144 < 0,155).

### Schreibtisch des Code-Agenten gegen Ausgang (PLAN.md Abschnitt 8, keine Wertung)

| Erwartung [H] | Ausgang |
|---|---|
| (i) Paritaet wechselt von Sprosse zu Sprosse | ja |
| (ii) rho_n - rho_z wechselt mit der Paritaet das Vorzeichen | ja: gerade unter, ungerade ueber rho_z |
| (iii) abs(rho_n - rho_z) ~ eps_n^0,726 | gleiche Paritaet: Exponent 0,743 (gerade 3 -> 5), 0,689 (ungerade 2 -> 4) |
| (iv) Huelle des Hauptasts ~ eps^0,363 | nicht sauber pruefbar: Die Dekaden-Maxima mischen den schwingenden Anteil mit dem Versatz ~eps^0,73 |
| (v) 5 oder 6 Sprossen in [1e-7; 0,05] | 5; die Leiter beginnt aber erst bei 6,0e-3 |

## Kontrollen

- **K0 Profil** (eps = 1e-7, 1e-5, 1e-3, 0,05, 0,2):
  - Reste der ersten Integralform <= 6,1e-16, der Bewegungsgleichung <= 1,9e-15.
  - Quadratur x(S) (scipy quad) gegen die geschlossene Form <= 2,7e-10.
  - S0 ist die kleinere Wurzel 1 - sqrt(2 eps) (PLAN.md Abschnitt 2); S am Integrationsstart (x_w + 30) <= 3,6e-15.
- **K0 ebene Wand** mit demselben RK4:
  - rho_z = 1,52414976213 auf h = 0,01 und 0,005, also 3,3e-11 neben WAND-BETA.
  - k_in = 1,9233246, kappa_in = 1,0262127, sqrt2 pi/k_in = 2,3100016.
- **RK4 gegen DOP853** (rohe W-Vektoren, 9 Punkte, eps 1e-6 bis 0,1): relativ <= 3,9e-9 (h = 0,01), <= 2,5e-10 (h = 0,005).
- **G2-10** (omega^2 0,55 bis 0,70 in 31 Schritten, ganzes Fenster, h = 0,01):
  - je Paritaet genau eine F1-Wurzel; F2 < 0 (gerade) bzw. > 0 (ungerade) auf allen 31 Werten; keine Stelle
  - gerader Ast gegen G2-10:

| omega^2 | 0,55 | 0,60 | 0,65 | 0,70 |
|---|---|---|---|---|
| rho_b (G2-10) | 1,375130 | 1,380272 | 1,427327 | 1,494353 |
| rho_b (hier) | 1,3751328 | 1,3802755 | 1,4273315 | 1,4943574 |
| Abstand | +2,8e-6 | +3,5e-6 | +4,5e-6 | +4,4e-6 |

  - Auch das Vorzeichen von s stimmt mit G2-10 ueberein (dort -3,5e-2 bis -5,6e-3).
- **Uebersicht ganzes Fenster** (4001 Punkte, jedes vierte eps, h = 0,02):
  - je Paritaet ueberall genau eine F1-Wurzel, also keine Nebenaeste
  - Wurzeln ausserhalb [1,30; 1,70] nur auf dem ungeraden Ast fuer eps >= 0,126 (1,709 bis 1,777), mit F2 > 0
  - Die Wurzeln im Leiterfenster stimmen mit dem Haupt-Scan gleicher Stufe auf 1,1e-13 ueberein.
- **Grobe Stufe allein:** dieselben fuenf Kandidaten, keiner nur grob.
- **Unveraendert seit dem Einfrieren (sha256, lokal = .69):**
  - PLAN.md = PLAN.md.eingefroren-20261003-025022: 9b2291189ba5107c1d998db326e68761735365c9e3367fb6c1a60be3679a30cb
  - leiter_1d.py f236d3770a02f7ad8adf26f4e3bb9582e39803550e3a7a99e5f490b7baa8205f
  - start1.sh 023fad7a..., start2.sh acbefdc9..., start3.sh f682fed9... (volle Werte in PLAN.md Abschnitt 10)
  - auswertung.json fc9307bba538808ba37b157c2d2b8fd77d797ab6b5abf8502ab845896c78d861
- **Laufzeiten** (.69, Python-Start bis Ende):
  - k0 72 s; Scans 136 bis 141 s; Uebersicht 61 s
  - Sprossen 16 s (grob), 19 s (fein), 28 s (D = 40); DOP853 5 s; Regel 1 s
  - Keine Wartezeit auf Spur-Sperren.

**Nebenbefunde (nachtraeglich, ohne Wertung):**
- **Schritte nach Paritaetsfolge:**
  - gerade -> ungerade: 1,9163, dann 2,2892; ungerade -> gerade: 2,3945, dann 2,3141.
  - Die Abweichung von 2,3100 wechselt von Schritt zu Schritt das Vorzeichen (-0,394, +0,085, -0,021, +0,004). Bei
    gleicher Art schrumpft sie um den Faktor 19 (gerade -> ungerade) bzw. 21 (ungerade -> gerade).
  - [H] Der Versatz d e^(-kappa_in L) schiebt die gerade und die ungerade Bedingung gegeneinander. Er faellt wie
    eps^0,73, ueber einen Doppelschritt (4,62) also um den Faktor ~29; beobachtet sind 19 bis 21.
- **Versatz der Sprossen:** Fuer die zwei geraden Sprossen 3 und 5 sagt e^(-2 kappa_in Delta x_w) mit x_w = arccosh(1/sqrt(2
  eps))/sqrt(2 - 4 eps) das Verhaeltnis 0,035 voraus; gemessen 0,033. Ungerade 2 -> 4: 0,034 gegen 0,040.
- **Innenbarriere nach G2-10:** Einschraenkung 1 oben (jq ueber auswertung.json: hauptast.*.verlauf und sprossen).

## Latten (v3)

- **L1 (kann scheitern): ja.**
  - Drei Vorhersagen mit Zahlengrenzen standen vor jeder Rechnung; die Regeln waren vor dem ersten echten Lauf
    eingefroren.
  - G2-10 hatte in der Naehe nichts gefunden.
  - Der erste Schritt weicht um 17 % ab. Haette die Leiter eine Sprosse frueher geendet, waere L1D-2 gescheitert.
- **L2 (Gegenprobe): ja, mit Grenzen.**
  - je Sprosse zwei Kriterien (Vorzeichenwechsel, Umlauf) auf zwei Stufen
  - zwei Integratoren (festes RK4, adaptives DOP853), zwei Gebietslaengen
  - ein fremdes Programm (bic2_2d aus G2-10) trifft den geraden Ast auf 4,5e-6 und die Stellenlosigkeit auf 0,55 bis 0,70
  - die ebene Wand ist mit demselben RK4 auf 3e-11 nachgerechnet
  - Es fehlt eine Nachrechnung durch ein anderes Haus und eine Zeitentwicklung.
- **L3 (Numerik): ja.** Stufen <= 2,9e-7, DOP853 <= 1,9e-8, Gebiet <= 3e-12 (alles in ln(1/eps)); Umlaeufe mit Spruengen
  <= 0,36 rad; Profil exakt. In 1D ist das Kernwachstum e^(kappa_in x_w) bei eps = 1e-7 nur ~450.
- **L4 (schon bekannt): teilweise.**
  - Projekt: 3D-Leiter (RUNDE-12/13), WAND-BETA (rho_z, b), G2-10 (1D ohne Stelle bis 0,05), EW-2 (der N = 1-Ast ist die
    kubisch-quintische NLS).
  - Das flache 1D-Profil dieses Potentials ist vermutlich Literatur (Flat-top-Soliton der kubisch-quintischen
    Gleichung) [L?, nicht nachgeschlagen].
  - Literatur zu eingebetteten Eigenwerten des 1D-Q-Balls nicht gesucht.
- **L5 (Messbezug): nein.** Modellinterne Aussage: linear, 1D, beta = 1/2.

## Selbstanzeigen

1. **Rauchlaeufe vor dem Einfrieren** (rauch1.sh, rauch2.sh; h = 0,025 / 0,0125, D = 25, eps >= 0,063 bzw. G2-10-Bereich
   0,05 bis 0,2):
   - Sie zeigten beide Aeste bei grossem eps ohne Vorzeichenwechsel.
   - Sie zeigten den Randpunkt eps = 0,05 des Vorhersagebereichs: je Paritaet eine Wurzel, F2 fest.
   - Aus eps < 0,05 habe ich vor dem Einfrieren nichts gesehen. Die Vorhersagen standen vorher; eigene Erwartungen
     (Plan Abschnitt 8) habe ich vor den echten Laeufen notiert.
2. **Code vor dem Einfrieren geaendert:**
   - nach Rauchrunde 1: Koeffizienten vorab tabelliert (Zeit), DOP853 als eigenes Kommando, RK4-gegen-DOP853 in k0
   - Rauchrunde 2 gab den Rauch-Scan bitgleich wieder.
3. **Berichtigung zum Auftrag:**
   - "S0 = groesste Wurzel" ist fuer das Profil nicht erreichbar.
   - Gerechnet ist mit der kleineren Wurzel 1 - sqrt(2 eps) (Plan Abschnitt 2; die k0-Ausgabe zeigt beide).
4. **Auslegungen [A]** (im Plan vor den Laeufen):
   - Leiterfenster [1,30; 1,70] statt des vorgeschlagenen [1,45; 1,65], damit der G2-10-Ast bei 1,37 darin liegt
   - "zwei kleinsten-eps-Schritte"; "laufen zu" = streng fallender Abstand
   - Sprosse = beide Stufen auf 1e-4 / 1e-5 gleich und Umlauf +-1 gleich; Rechteck +-0,01 x +-0,5
   - An keiner Auslegung haengt ein Urteil knapp. Die engste Stelle ist L1D-2 mit -0,90 % bei +-10 % Band.
5. **Nachtraeglich, nicht im Plan, ohne Wertung:**
   - das G2-10-Barrierekriterium entlang der Aeste (Einschraenkung 1)
   - die Exponenten- und Verhaeltnisrechnungen der Nebenbefunde
   - die Auswertung meiner Schreibtisch-Erwartungen
   - alles mit jq/awk lokal aus auswertung.json
6. **Meine Hauptast-Erwartung [A]** (je Dekade fallend) ist beim geraden Ast in der angebrochenen obersten Dekade
   verfehlt; sie ist keine Regel.
7. **Lokal:**
   - kein Interpreter
   - nur bash, jq, awk, ssh, scp, rsync, sha256sum, date, cp, mkdir, chmod, ls, grep, sort, diff, head, tail, cat,
     timeout und sleep (Warteschleifen)
8. **Sonst:**
   - kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Dienste, Timer oder Hooks
   - nur die Spuren cpu, cpu2, cpu3, cpu4 und cpu6; jeder Aufruf unter 150 s
   - auf der .69 nichts in place ueberschrieben (Code und Skripte per .neu und mv)
   - Dateien nur in RUNDE-25/leiter-1d/ und runde25-leiter-1d/
   - keine Abweichung vom Plan

## Einfach gesagt

Ein Q-Ball kann bei bestimmten Frequenzen schwingen, ohne Wellen abzustrahlen; diese stillen Stellen bilden eine Leiter.
Bisher galt im Projekt: In einer eindimensionalen Welt gibt es diese Leiter nicht, weil dort etwas Wichtiges fehle. Wir
haben jetzt viel naeher an der Grenze gesucht, wo der Ball sehr breit wird, und fuenf stille Stellen gefunden. Jede
liegt etwa zehnmal naeher an der Grenze als die vorige, genau im vorher berechneten Abstand, und ihre Frequenzen naehern
sich dem Wert, den eine flache Wand allein vorgibt. Die alte Suche hatte einfach zu weit weg von der Grenze geschaut;
das "fehlende Teil" ist bei so breiten Baellen auch in einer Dimension vorhanden, und alles gilt nur im Rechenmodell.

---
Letzte Aenderung dieser Datei: 2026-10-03 03:01:41 CEST (date). Zeitbox 120 min ab 02:26:08 eingehalten.
