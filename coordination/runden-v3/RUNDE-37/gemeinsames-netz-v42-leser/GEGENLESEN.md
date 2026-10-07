Urteil: nicht weitergabefaehig; weitergabefaehig nach A12 bis A14 (drei kurze Textstellen, keine Rechnung). GW1 nicht eingetroffen, GW2 eingetroffen.

# Gegenlesen GEMEINSAMES-NETZ v4.2, nur die Aenderungen 4.1 zu 4.2 (dritter frischer Leser, Haus Anthropic)

- Geprueft: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-48/GEMEINSAMES-NETZ-v4.md, sha256 f5338cf4cdd004eabeda1f8f037ed342e4d3c74aedb6bc230e798c70d4dc2d11 (bei Beginn per sha256sum bestaetigt, 215 Zeilen).
- Unterschied: AENDERUNGEN-4.1-zu-4.2.diff. Ich habe ihn per diff gegen GEMEINSAMES-NETZ-v4.md.wie-gelesen-v41-leser (sha256 857a800c..., bestaetigt) neu gebildet: identisch.
- Soll: RUNDE-37/gemeinsames-netz-v41-leser/GEGENLESEN.md, Abschnitte 4 und 5.
- Zeilen = Zeilennummern der Fassung 4.2. Die Nummern schliessen an A8 bis A11 und B1 bis B9 des zweiten Lesers an.

## 1. Zeiten

- Beginn (date): 2026-10-05 10:06:01 CEST
- Ende (date, vor dem Eintragen dieser Zeile): 2026-10-05 10:16:32 CEST
- Dauer: 10 min 31 s [10:16:32 - 10:06:01: bis 10:16:01 sind es 10 min, dazu 31 s]. Zeitbox 20 min eingehalten.
- Quellenstand: RUNDE-48.md mit 217 Zeilen (letzter Eintrag 10:04:13, Fassung 4.2).

## 2. Ergebnis zuerst

1. **Weitergabefaehig: nein. Nach A12 bis A14: ja.** Alle drei sind kurze Textaenderungen ohne Rechnung.
2. **A8, A10, A11 sowie B1, B2, B6, B7 und B9 sind inhaltlich umgesetzt** (Reste in der B-Liste). A9 ist nur teilweise umgesetzt:
   - Z. 39 stellt den Verlust bei A = 1e-3 neben eine Gewinn-Spanne aus beiden Amplituden und laesst "im Mittel" weg (A12).
   - Einfach gesagt nennt die Ursache "Traegheit" weiter als Tatsache (A13).
   - Der Kopf meldet B5 als eingearbeitet, Z. 59 ist aber unveraendert (A14).
3. **Die neuen Saetze ausserhalb des Solls stimmen mit ihren Quellen:** Codex C1 (Rang 2 erzwingt nicht Rang 4), Codex C7 (kanonische Zustandsuebertragung), die Fluessigkeits-Regel und der Navier-Stokes-Zusatz. Belege: RUNDE-48.md, CODEX-REVIEW-LEITUNG-20261005.md, raum-gas-l/KARTE.md.
4. **Negativliste:** Nach Kernbegriffen steht kein Satz sinngemaess ausserhalb von Abschnitt 7 (GW2 eingetroffen). Zwei alte Eintraege stehen jetzt aber unter einer falschen Herkunftszeile (B11).

## 3. Urteile GW1 und GW2

| Nr | Erwartung | Wahrsch. | Urteil | Fundstelle |
|---|---|---|---|---|
| GW1 | Alle Aenderungen setzen den Sollinhalt um und sind nicht staerker als ihre Quelle | 70 % | **nicht eingetroffen** | A12 (Z. 39), A13 (Z. 212), A14 (Kopf Z. 9 gegen Z. 59). Ohne A-Befund: Z. 1, 8 bis 11, 20 (aber B10), 40, 53, 64, 68, 80, 81, 100, 123 (aber B12), 133 bis 135, 193 bis 204, 211, 213 (aber B13) |
| GW2 | Kein Negativlisten-Satz steht sinngemaess ausserhalb von Abschnitt 7 | 80 % | **eingetroffen** | Probe nach Kernbegriffen, ausserhalb von Abschnitt 7: <br>- "stabil" bei Glas: Z. 50, 60 und 123 nennen alle die (gerechneten) 112 k-Klassen. <br>- "Energie" beim Umklappen: Z. 39, 66, 133 und 212 sagen "nicht erhalten" bzw. Verlust oder Gewinn. <br>- "alle Richtungen": Z. 81 und 211 sagen "langwellig" bzw. "lange Lichtwellen". <br>- Doppelpulsar: Z. 82 und 213 sagen "offen". <br>- Licht-Identitaet und Schwerewellen: Z. 53 verneint. <br>- Cristobalit und 222-Form: Z. 59 sagt keine negative Ausdehnung und "isotroper Ast nicht beschrieben". <br>- alpha1: Z. 87 nennt ein "wirksames alpha1_eff", nicht "gemessen". <br>- Rayleigh-Jeans: Z. 100 ist die zulaessige Fassung V-1. <br>- "widerlegt", TES, Pound/Rebka, Glueballs, Connor Hill: kein Treffer ausserhalb von Abschnitt 7 |

**Ohne Befund gegen die Quelle geprueft** (Kopfrechnungen in eckigen Klammern):
- Z. 40:
  - Regge-Energie beim 2-3-Zug exakt stetig (<= 8e-13 H0): takt-dynamik-1/ERGEBNIS.md Z. 72 und 73.
  - Codex C7: RUNDE-48.md Z. 174 und 192; CODEX-REVIEW-LEITUNG C7 "richtig".
- Z. 53:
  - Zwei Identitaeten, 26 Netze, Spanne <= 5,5e-12, vorab ableitbar: danzer-naeherung-2/ERGEBNIS.md Z. 46 bis 50.
  - "Rang 2 erzwingt nicht Rang 4": CODEX-REVIEW-LEITUNG C1 und RUNDE-48.md Z. 171. Nachgerechnet: [isotrop M_ijkl = (d_ij d_kl + d_ik d_jl + d_il d_jk)/5, Spur (9 + 3 + 3)/5 = 3 = Summe \|n\|^4 der drei Achsen, also M_1122 = 1/5; bei den Achsen ist M_1122 = 0, weil jede Achse nur eine Komponente hat].
- Z. 64: "Unter den gerechneten Zerlegungen" nach R47 B8 (Soll B7). Z. 68: "sinngemaess gekuerzt" (Soll B9).
- Z. 80:
  - skalar-sektor-l/DOSSIER.md Z. 29 bis 33: woertlich "machbar, aber nicht wegen der Takt-Deutung"; 4D-Regge asymptotisch erfuellt; gefuelltes Netz konstant 0,90.
  - Z. 305: Khronon nur mit eigenem Feld.
  - "[S laut Agent]" steht schon in Z. 69 und ist kein neues Kennzeichen.
- Z. 100: V-1 fast woertlich nach gegenlesen-r45/GEGENLESEN.md Z. 176; es fehlt nur "(Teilchen und Loch tauschen nur die Rollen)", ohne Wirkung.
- Z. 133 bis 135:
  - RUNDE-48.md Z. 155: Scherung oder Kruemmung.
  - RUNDE-48.md Z. 202 bis 206: NS1 bis NS3 als Zusatz an RAUM-GAS-L.
  - raum-gas-l/KARTE.md Z. 32 bis 34: Querwellen nur fuer omega tau > 1 [L]; ob das gilt, haengt an Scherung oder Kruemmung.
  - takt-dynamik-1 Z. 270 bis 273: R daempft, P verstaerkt, die Groesse haengt an der Lesart.
- Z. 193 bis 204:
  - atem-vollzaehlung-l/DOSSIER.md: Ergebnis 4 und Negativliste Punkt 2 bis 4 (533 K, 5 %, 750 bis 2000 K, 1300 K).
  - skalar-sektor-l Abschnitt 10.
  - teile-schranke-l/DOSSIER.md Negativliste 2 und 3 ("ueber 22,5 m" entspricht "unterwegs").
- Z. 213: "Auf dem gerechneten Kristallnetz" und "mehr als die Messgenauigkeit" [0,15 % = 1,5e-3; 1,5e-3 / 1,3e-4 = 11,5, also rund 12-mal] stimmen mit impuls-netz-1/ERGEBNIS.md Z. 320 bis 327.

## 4. A-Liste (falsch oder zu stark; vor der Weitergabe zu berichtigen)

Den Wortlaut waehlt die Leitung.

**A12 Z. 39: Gewinn-Spanne aus zwei Amplituden, "je Zug" ohne "im Mittel" (Rest von A9).**
- Ist: "Je Zug aendert sie sich um 0,2 bis 0,5 %. Ueber 10 Perioden verliert die Welle bei A = 1e-3 2,4 bis 12,7 %, wenn die Raten ueber den Zug stetig gehalten werden; sie gewinnt 15 bis 80 %, wenn die Impulse stetig gehalten werden."
- Fehler:
  - Der Satz steht unter "bei A = 1e-3". Dort gewinnt die Welle mit stetigen Impulsen aber nur 15 bis 20 %. Die 80 % gehoeren zu A = 1e-2. So stehen Verlust und Gewinn mit verschiedenen Amplituden nebeneinander, und der Gewinn bei A = 1e-3 wirkt bis zu viermal so gross [80 / 20 = 4].
  - Die 0,2 bis 0,5 % sind das Mittel je Zug; einzelne Zuege erreichen 2,2 %.
- Soll (Inhalt):
  - Ein Zug aendert die Energie im Mittel um 0,2 bis 0,5 %, hoechstens um 2,2 %.
  - Bei A = 1e-3 verliert die Welle ueber 10 Perioden 2,4 bis 12,7 % (Raten stetig) oder gewinnt 15 bis 20 % (Impulse stetig). Bei A = 1e-2 sind es 10,5 bis 34,6 % bzw. 32 bis 80 %.
  - A = 1e-3 allein fuer beide Lesarten genuegt auch.
- Beleg: takt-dynamik-1/ERGEBNIS.md
  - Z. 69 bis 71 (Ergebnis zuerst 2, beide Lesarten und beide Amplituden; "im Mittel ... hoechstens 2,2 %").
  - Tabelle Z. 145 bis 152, Lesart P: A = 1e-3 +0,148 / +0,180 / +0,202 [also 15 bis 20 %], A = 1e-2 +0,324 bis +0,798 [also 32 bis 80 %].
  - Soll A9, Punkte 1 und 2.

**A13 Z. 212 (Einfach gesagt): Ursache als Tatsache (Rest von A9).**
- Ist: "Das liegt an der Traegheit der Zellen im Modell."
- Soll (Inhalt): Gemessen ist nur, dass der Sprung in der Bewegungsenergie sitzt. Dass die gleiche Traegheit jeder Zelle die ganze Ursache ist, ist eine Hypothese. Etwa: "Vermutlich liegt das an der Traegheit der Zellen im Modell." A9 verlangte dieses "vermutlich".
- Beleg:
  - takt-dynamik-1/ERGEBNIS.md Z. 73 bis 75: "dass das die ganze Ursache ist, ist nicht getrennt gerechnet [H]".
  - Ebenda Z. 260 und 261: Wie die Energie ueber den Zug weitergegeben wird, legt das Modell nicht fest.
  - Z. 40 der Fassung nennt selbst eine zweite moegliche Ursache: die fehlende kanonische Zustandsuebertragung beim Zug (Codex C7; die Leitung bewertet sie als richtig, CODEX-REVIEW-LEITUNG Z. 18).

**A14 Kopf Z. 9: "B5 eingearbeitet", aber Z. 59 ist unveraendert.**
- Ist:
  - Z. 9: "Eingearbeitet: A8 bis A11 inhaltlich, dazu B1, B2, B5 bis B9."
  - Z. 59 steht nicht im diff und sagt weiter: "Die zweite Atemform gehoert sehr wahrscheinlich zur starren P2_12_12_1-Familie ... [S, ES]". Die Schranke \|alpha_V\| <= 1,5e-6/K steht dort unter [S].
- Soll (Inhalt): Entweder B5 umsetzen, also die Zuordnung als [H] ohne Rechnung kennzeichnen und die Schranke als [E aus S] fuer 750 bis 2000 K. Oder B5 aus der Kopfzeile nehmen. Sonst haelt ein spaeterer Leser Z. 59 fuer berichtigt.
- Beleg:
  - Soll B5.
  - atem-vollzaehlung-l/DOSSIER.md Z. 54 bis 56: Kalibrierung (c), "Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen)", von [H] auf "sehr wahrscheinlich", ohne Rechnung.
  - Ebenda Tabelle Z. 186: [E aus S] [0,05 / 27,4 = 1,82e-3; 1,82e-3 / 1250 K = 1,46e-6/K, also <= 1,5e-6/K].
  - Ebenda Negativliste Punkt 4: "die Zuordnung ist [ES]".

## 5. B-Liste

- **B10 Z. 20, MATERIE-NETZ-1 unter "Ohne frischen Leser":** Das ist sachlich falsch, wenn auch in vorsichtiger Richtung.
  - Die Karte hatte einen frischen Leser (pruefer-opus, 04:49:21 bis 04:59:27; Befunde ab 05:05 eingearbeitet). Nur die letzte Textschicht hat keiner mehr gesehen (materie-netz-1/ERGEBNIS.md Z. 278 bis 286).
  - Sie gehoert also wie DEFEKT-NETZ-1 unter "Mit unabhaengigem Leser", mit dem Zusatz "letzte Textschicht ungesehen".
- **B11 Z. 205 und 206, Herkunftszeile:** "Glueballs" und "Connor Hill" standen in 4.1 unter "Aus den Runden 44 bis 48" (4.1 Z. 189 und 190).
  - Durch die Einfuegung stehen sie jetzt unter "Ergaenzt in 4.2 (zweiter v4-Leser, B8)".
  - Die Ueberschrift von Abschnitt 7 sagt weiter "ergaenzt in 4.1".
- **B12 Z. 123, Weiche 3:**
  - Das A8-Soll nennt "24 Delaunay-Glasnetze", die Zeile nur "Glasnetze". Die k-Einschraenkung steht da; ein Negativlisten-Treffer ist es also nicht.
  - "jedes einzelne ... wird mit mehr Punkten gleichmaessiger": Gleichmaessiger wird die Reihe mit wachsendem N, nicht das einzelne Netz (Z. 51: Spanne etwa wie N^(-1/2)).
- **B13 Z. 213, "offen, denn ein Teil der Rechnung fehlt noch":** Das nennt nur einen der Gruende.
  - Die Quelle nennt auch die unbekannte Lage der Gitterachsen. Vertraeglich ist nur ein Band Summe m_i^4 = 0,60 bis 0,67; "fuer die meisten Lagen" waere das Netz ausgeschlossen [ES] (skalar-sektor-l Z. 227 und 228; impuls-netz-1 Z. 324 bis 327).
  - Z. 82 sagt es richtig. Etwa: "offen: Wie das Netz zum Doppelstern liegt, ist unbekannt, und ein Teil der Rechnung fehlt noch."
- **B14 Z. 53, Vorbehalt nur bei Maxwell:** "(in der Quelle eigene Mathematik, ungeprueft)" steht nur nach der Maxwell-Identitaet.
  - In der Quelle gilt das fuer beide Identitaeten und fuer die Herleitung von c = 1 (danzer-naeherung-2 Z. 13, Z. 49 und 50, Z. 291 bis 294).
  - Numerisch bestaetigt sind beide auf 26 Netzen.
- **B15 Z. 80, L1 ohne CMC:** Das A11-Soll nannte Khronon und CMC; 4.2 nennt nur Khronon mit eigenem Feld.
  - Fuer das Netz liegt CMC naeher, weil K = 0 schon eingebaut ist (skalar-sektor-l Z. 119 und 120, Z. 183).
  - Nicht zu stark, aber unvollstaendig.
- **B16 Z. 211, "in jedem Netz":**
  - Genau heisst es "auf jedem periodischen Netz" (danzer-naeherung-2 Z. 11, 49 und 221; Z. 53 sagt es richtig). Das Einfach gesagt der Quelle sagt aber selbst "auf jedem Netz" (Z. 302 und 303), darum tragbar.
  - "bei sehr kurzen Wellen" ist schwaecher als das Soll ("bei kurzen Wellen").
- **B17 B8 nur teilweise:**
  - Aus ATEM-VOLLZAEHLUNG-L fehlen weiter Negativliste 8 ("Echter beta-Cristobalit atmet isotrop wie P2_13") und 11 ("Der RUM-Anteil ... ist gemessen").
  - In Z. 196 fehlt bei "ihre Familie ja" der Zusatz der Quelle "die Zuordnung ist [ES]".
- **B18 Z. 11, "kurze Textstellen nach den Sollinhalten des Lesers":** Drei Stellen gehen ueber das Soll hinaus: Z. 40 (C7), Z. 53 (C1) und Z. 135 (Navier-Stokes). Sie stimmen mit ihren Quellen (Abschnitt 3), der Kopf sollte sie aber nennen.
- **B19 Weiter offen:** B3 (Z. 87, L8, "nur w = 0") und B4 (Z. 60 und 125, Quasikristall) des zweiten Lesers. Der Kopf meldet sie richtig nicht als eingearbeitet.
- **B20 Ausserhalb der Fassung:** Die Antwort an Finn in RUNDE-48.md Z. 154 sagt weiter "Ein Gas-Raum traegt Schwerewellen nur mit energieerhaltendem Umklappen". Z. 133 der Fassung berichtigt das jetzt. Ein kurzer Nachtrag an Finn waere zu erwaegen.

## 6. Selbstanzeigen

- **Umfang:** Nur die diff-Stellen, dazu Z. 59 (wegen der Kopfangabe B5) und die Treffer der Kernbegriff-Probe. Unveraenderte Stellen habe ich nicht neu geprueft, auch B3 und B4 nicht.
- **Kernbegriff-Probe:**
  - Sie lief per grep ueber eine Begriffsliste: stabil, alle Richtungen, gleich schnell, widerleg, gemessen, ausgeschlossen bzw. ausschl, Doppelpulsar, TES, Pound, Uhrenvergleich, negative, 222, in der Literatur, schrumpf, harmlos, noetig, Energie, verloren, isotrop, Identitaet.
  - Die Treffer ausserhalb von Abschnitt 7 habe ich von Hand gelesen. Dazu habe ich jede geaenderte Zeile gegen alle Eintraege von Abschnitt 7 gelesen.
  - Begriffe ausserhalb der Liste koennen mir entgangen sein.
- **grep-Ausschluesse:**
  - Der Ordner-grep ueber raum-gas-l/ und RUNDE-48/ hatte alle Ausschluesse.
  - Der Ordner-grep ueber teile-schranke-l/ (nur *.md) und die greps auf einzelne Dateien hatten sie nicht. Das verstoesst gegen die Auftragsregel.
  - Nachpruefung per ls -R: In teile-schranke-l/ traegt kein Dateiname VERSIEGELT oder T8-SOLL (0 Treffer). Versiegeltes habe ich nicht geoeffnet.
- **Laufender Agent:** Der grep in raum-gas-l/ zeigte Zeilen aus dem Arbeitsfeld des laufenden RAUM-GAS-L-Agenten. Dort steht vorlaeufig, die Frage "Scherung oder Kruemmung" sei fuer das ruhende Netz "schon beantwortet: Kruemmung" (ARBEITSFELD.md Z. 47 und 48). Das ist ein Zwischenstand; ich habe ihn fuer kein Urteil verwendet.
- **Arbeitsweise:** Alle Zahlen habe ich im Kopf nachgerechnet. Ich habe keinen Interpreter benutzt, kein Journal, keinen Peerbus und keinen Commit. Geschrieben habe ich nur diese Datei.
- **Haus:** Ich bin vom selben Haus wie die Leitung und beide Vorleser (Anthropic). Eine Sicht aus einem fremden Haus fehlt.

## Arbeitsstand (Zwischennotizen zwischen den date-Marken 10:06:01 und 10:13:21; massgeblich sind die Abschnitte 2 bis 6)

- Zwischen 10:06:01 und 10:09:32 (date-Marken): Diff gegen GEMEINSAMES-NETZ-v4.md.wie-gelesen-v41-leser (sha256 857a800c... bestaetigt) neu gebildet und mit AENDERUNGEN-4.1-zu-4.2.diff verglichen: identisch.
- Vorlaeufige Kandidaten (noch gegen Quellen zu pruefen):
  - Kopf Z. 9 "B5 bis B9 eingearbeitet": B5 des zweiten Lesers (Z. 59 "sehr wahrscheinlich") steht unveraendert.
  - Z. 39 "gewinnt 15 bis 80 %" im Satz "bei A = 1e-3": 32 bis 80 % gehoeren laut Leser-Soll zu A = 1e-2.
  - Z. 212 "Das liegt an der Traegheit" ohne "vermutlich" (A9-Soll, letzter Punkt).
  - Z. 205/206 ("Glueballs", "Connor Hill") stehen jetzt unter "Ergaenzt in 4.2 (B8)", stammen aber aus 4.1 "Runden 44 bis 48".
  - Z. 123 Weiche 3: ohne "Delaunay"/"24" und ohne "Lesart"-Satz.
  - Z. 213 "offen, denn ein Teil der Rechnung fehlt" nennt nur einen der Gruende der Quelle.
- Zwischen 10:11:37 und 10:13:21 (date-Marken) Quellen geprueft: takt-dynamik-1 (Z. 69-75, 143-152, 256-272), RUNDE-48.md Z. 145-217, raum-gas-l/KARTE.md Z. 21-35, danzer-naeherung-2 (Z. 44-50, 216-245, 291-306), skalar-sektor-l (Z. 29-33, 117-120, 140-144, 218-232, 305), impuls-netz-1 Z. 318-327, gegenlesen-r45 Z. 176, atem-vollzaehlung-l (Z. 18-24, 35-40, 54-58, 282-301), teile-schranke-l Z. 143-156, materie-netz-1 Z. 278-286.
  - Bestaetigt: Z. 39 "15 bis 80 %" mischt A = 1e-3 (P: +14,8/+18,0/+20,2 %) und A = 1e-2 (+32,4 bis +79,8 %); "Je Zug 0,2 bis 0,5 %" ist laut Quelle das Mittel, hoechstens 2,2 %.
  - Bestaetigt: Ursache "Traegheit" ist in der Quelle [H] (Z. 75).
  - Neu: MATERIE-NETZ-1 hatte einen frischen Leser (ERGEBNIS Z. 278-286; letzte Textschicht ungesehen) -> steht in 4.2 falsch unter "Ohne frischen Leser".
  - Ohne Befund: V-1 (Z. 100) woertlich nach R45 V-1; L1 (Z. 80) nach DOSSIER Z. 29-33 und 305; Codex-Saetze (Z. 40, 53) nach RUNDE-48 Z. 171-174, 192; Gas-Weiche nach RUNDE-48 Z. 155 und raum-gas-l KARTE Z. 32-34; Negativliste 192-202 nach den Dossiers.
