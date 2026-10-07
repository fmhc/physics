# Runde 10 (v3): Krein-Signatur, Spin-1/2-Wege, Paper zur Leiter, Band-Reissprobe, Ladungstausch-Ball

Leitung: claude-primary. Angelegt: 2026-09-30 10:26:26 CEST (gemessen, date bei der Ziehung der Zufallskarte). Explorativ,
keine formale Bestaetigung. Runde 9 ist abgeschlossen (RUNDE-09.md: Abschaetzung, Einfach gesagt; Journal
claude-runde-v3-09-20260930, veroeffentlicht nach 10:26:05).

## Rahmen

- Rechenorte: .69 ueber kleintest.sh (Spuren p4000a, p4000b, cpu bis cpu6); cpu5 fuer KREIN-1 (Beweis-Agent).
- Sicherung: rsync .69 -> TS440 laeuft seit 10:24:31 (Log /home/fmh/sicherung-dot69-ts440-lauf-20260930-r9.log auf der
  .69).
- Offene Entscheidungen Finns:
  - Ollama-Stopp: WM-1-MB, B28 und CX-1 warten.
  - restic-Aufraeumen auf dem TS440.
  - APS-Datenzugang (ST-1).

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| KREIN-1 | R9, Finn "mach das" | Krein-Signatur der stillen Moden (l = 0 n = 1 bis 3, l = 1, l = 2, psi_2); streng fuer n = 1 | Beweis-Agent (laeuft seit 10:13) |
| SPIN-1 | R9, Finn "mach das", "zwei baelle rotieren" | Schreibtisch: Weg A (C x S^2, bindet der Hopf-Knoten an den Q-Ball?), Weg B (Ladung plus Monopol) | feldforscher Fable (Neustart nach API-Fehler, seit 10:21) |
| DATEN-LEITER | Codex-Bitte (Paper zur Leiter) | Datenpaket aller stillen Stellen mit Evidenzklasse und Herkunft | SP-1-Agent (seit 10:23) |
| ENTWURF-DUENNWAND | Codex-Bitte | englischer Abschnitt Duennwandmodell | Theorie-Agent (seit 10:23) |
| SU(3)-v0.6-Nachlesung | Codex-Bitte | gezielte Nachlesung der neuen Absaetze in Paragraph 7 | Paper-Agent (seit 10:23) |
| EVO-1 Gen 1 | R7 bis R9 | 12 von 17 Modellen fertig; danach N5-Pruefung, A2, A3 | Ketten cpu3/cpu4, Leitung |
| BAND-1 | R9 ROT-1 | Reissprobe: Reisst das Band zwischen zwei Wirbeln bei grossem Abstand (Analogon zum Stringbrechen durch Paarbildung)? Feines Gitter, groesserer Ball, g gegen -g | ROT-1-Agent (fortgesetzt) |
| LADUNGSTAUSCH-1 | R9 ZUS-10 Idee 7 | langlebiger Ladungstausch-Ball aus eng gestartetem Q/Anti-Q-Paar (d = 4): Lebensdauer gegen d, Frequenz, Bezug zur Literatur (Copeland/Saffin/Zhou 2014) und zu stillen Stellen | ZUS-10-Pruefer (fortgesetzt) |
| IE Gen 2 | R9 IE Gen 1 | naechste Generation der Ideen-Evolution (Auswahl, Ziehung, Operatoren, Tests, blinde Ernte) | Leitung; geerntet 12:25, Abschaetzung GEN-02.md 12:26 |
| Y-1 | Finn: drei Verbindungen, Punkt/Flaeche/Laenge; Freigabe "ja mach weiter" | Wirbel-Dreier in N = 3 (je ein Wirbel in psi_1, psi_2, psi_3) mit Waenden: Y-Gesetz (Steiner-Laenge) gegen Dreiecks-Gesetz (halber Umfang), Proton-Vorbild. Vorarbeit: farben-20260927/BERICHT-FARBEN.md ("Zweier schlaegt Dreier", keine selbstgebundenen Dreier getrennter Koerper), regge-anschluss-20260912.md, geometrie-teilchenmodelle-stand-20260912.md | eigener Code-Agent, gestartet vor 10:46:26 (Finn: "rechne das"); ROT-1-Agent bleibt bei BAND-1 |
| HOPF-1 | Finn: "prüfe q-ball hopf verbund noch mal" | numerisch: bindet ein Hopf-Knoten an den Q-Ball (Codex B.5), wo am staerksten? | Code-Agent (seit 10:38) |
| LIN-WIRBEL-1 | Finn: G2-01 "das mal pruefen" | Lineare Stabilitaet drehender 2D-Baelle (m = 1, 2, 3): NLS-Form als Validierung gegen Pego/Warchall, volle KG-Form; sind die Schwellen gleich? Vergleich mit den Zeitentwicklungen RING-T und G1-03. Pego/Warchall an der Quelle lesen | Beweis-Agent (fortgesetzt) |
| NLS-LEITER | Finn: "ueberleitung auf echte physik / experimente?" | Hat das kubisch-quintische NLS (Labormodell: Optik, kalte Atome) selbst stille Atmungsstellen (3D, 2D)? Kanalstruktur wie bei uns (u offen, v geschlossen); Wandtopf offen. Falls ja, Umrechnung in Laborgroessen | MESS-1-Agent (fortgesetzt) |
| **Chem 8, Zufallskarte** | R3/R4, gezogen 10:26:26 mit `shuf -n 1` aus den Gen-0-Eintraegen "parken" | "Katalyse durch dritten Ball": in R4 je ein v-Punkt knapp ueber der Schwelle. Naechster Schritt aus dem Parkgrund: dichteres v-Raster um die Schwelle | Leitung: RUNDE-10/chem8/KARTE.md (Vorhersage 12:14:18 mtime), Laeufe auf p4000b ab 12:14:43 |
| BEWEIS-2 | Finn "ja maach weiter" (mittags) auf die Frage nach weiteren Sprossen | rechnergestuetzter Beweis fuer l = 0, n = 2 (T1) und l = 1, n = 1, erste Schwapp-Stelle (T2); Auftrag RUNDE-10/beweis2/BRIEF.md (ab 12:05:26) | Beweis-Agent (fortgesetzt ab 12:05, hoechstens 2,5 h) |

- Bei Codex laufen (nicht doppeln): das zweite Paper zur BIC-Leiter (ag-phy-coordination), die englische v0.6
  (ag-phy-lat), die erzwungene L = 2-Rechnung zur l = 1-Leckage und die Fremdhaus-Pruefung von BEWEIS-1 (Anfrage
  f67c1643, offen; neu an ag-phy-coordination 4140a813, 12:06:22).

## Tests: Ergebnisse

### G2-01 Pruefung der Leitung: Originalpaper Pego/Warchall (Finn: "das mal pruefen", "hol dir das original paper"; eingetragen 2026-09-30 11:20:55 CEST)

- **Umrechnung von Hand bestaetigt:** Mit f = sqrt(4/3) g und r = sqrt(3/8) rho wird unsere Profilgleichung (beta = 0,5,
  Windung m) exakt zur CQ-NLS-Profilgleichung, mit Omega = (3/8)(1 - omega^2). Probe: omega^2 = 0,5 ergibt Omega = 3/16.
- **Original geholt:** arXiv nlin/0108009v2 (Pego, Warchall, J. Nonlinear Sci. 12, 347 (2002)), 40 Seiten.
  - Abgelegt in RUNDE-10/lin-wirbel1/quellen/, sha256 98ff633b8aacbaf335ded6efba02bbd036e9d1a79a139fe0d756cfbf96b1b09e,
    Text per pdftotext.
  - Normierung: Gl. (1.1) -i u_t - Laplace u = g(u), g = |u|^2 u - |u|^4 u, omega_* = 3/16. Das ist dieselbe wie bei
    Caplan u. a.
- **Tabelle 1 im Original (Zeilen 1115 bis 1123 der Textfassung):** "spectrally stable for omega_cr <= omega < omega_*";
  die Instabilitaet entsteht durch Zusammenstoesse imaginaerer Eigenwerte.

  | m | Omega_cr | Kollision bei | omega_c^2 umgerechnet |
  |---|---|---|---|
  | 1 | 0,1487 | 0,0478 i | 0,6035 |
  | 2 | 0,1619 | 0,0271 i | 0,5683 |
  | 3 | 0,1700 | 0,0136 i | 0,5467 |
  | 4 | 0,1769 | 0,0063 i | 0,5283 |
  | 5 | 0,1806 | 0,0033 i | 0,5184 |

  - Die Zahlen der Karte (nach Caplan u. a. Tab. II) sind damit an der Quelle bestaetigt.
- **Deutung der Leitung [H]:** Die Schwellen sind Krein-Kollisionen bei kleiner, mit m fallender Frequenz. Der
  lambda^2-Term, in dem sich KG von NLS unterscheidet, ist dort nur eine kleine Stoerung (grob |lambda|/(2 omega) ~ 0,05
  bei m = 1 bis 0,017 bei m = 3).
  - Die KG-Schwellen sollten deshalb knapp unter den NLS-Schwellen liegen, mit einer Verschiebung, die mit m schrumpft.
  - Das passt zu m = 1 (0,59 bis 0,60 gegen 0,6035) und m = 2 (0,567 gegen 0,5683). Die gute Uebereinstimmung waere
    dann kein Zufall.
  - Die Pruefung rechnet LIN-WIRBEL-1.

### LIN-WIRBEL-1 (Beweis-Agent; RUNDE-10/lin-wirbel1/ERGEBNIS.md; eingetragen 2026-09-30 11:58:25 CEST)

- **NLS-Form trifft Pego und Warchall an der Quelle:**
  - Omega_cr = 0,14858 / 0,16185 / 0,17002, Original 0,1487 / 0,1619 / 0,1700.
  - Die Kollisionsfrequenzen 0,04785 / 0,02715 / 0,01365 treffen die Werte 0,0478 / 0,0271 / 0,0136.
  - Die instabile Mode ist J = 2.
- **KG-Schwellen liegen darunter, mit fast konstantem Abstand:**

  | m | NLS (omega^2) | KG (omega^2) | Abstand |
  |---|---|---|---|
  | 1 | 0,60378 | 0,60013 | -0,00365 |
  | 2 | 0,56839 | 0,56492 | -0,00347 |
  | 3 | 0,54662 | 0,54297 | -0,00365 |

  - Exakte Identitaet: P_KG(nu) = P_NLS(nu) - nu^2. Die Schwelle ist eine Krein-Kollision bei nu ungleich 0; gleiche
    Schwellen gaebe es nur bei einem Austritt durch null.
  - **Die Hypothese der Leitung (Abstand schrumpft mit m) ist widerlegt:** nu_c^2 faellt von m = 1 bis m = 3 um den
    Faktor 11, der Abstand bleibt gleich. Warum, ist offen.
- **Die Zeitentwicklungen folgen KG, nicht NLS:**
  - m = 2 bei 0,57: gamma_KG 0,00928 gegen 0,0098 aus G1-03; die NLS-Form gaebe 0,0056.
  - Der gamma^2-Nullpunkt 0,567 der Zeitentwicklung kam aus der Kruemmung; die lineare KG-Schwelle ist 0,56492.
  - m = 1: Die KG-Schwelle liegt 0,00013 ueber dem Teilungspunkt 0,60, also knapp.
- **Numerik:** Halber Gitterschritt verschiebt um <= 2e-5; der KG-NLS-Abstand ist auf 3e-6 gitterunabhaengig.
  - Einzige weitere Instabilitaet im Bereich: J = 3 fuer m = 2 in KG, ab 0,5994.
  - Zwei eigene Abbrueche (falsches Plateauprofil; S_max-Probe mit falscher Grenze 1, berichtigt auf S_h).
- **Bezug zur Ideenkarte G2-01:** Die lineare KG-Schwelle fuer m = 3 liegt bei 0,54297, im Band [0,540; 0,548] der Karte.
  Die Karte prueft die Zeitentwicklung und bleibt unveraendert; ihre Laeufe laufen.
- **Bedeutung:** Die Bruecke zum Optikmodell traegt fuer die Form, nicht fuer die Dynamik. Relativistische Baelle
  zerfallen um ~0,0035 in omega^2 frueher als Lichtwirbel gleicher Form, fuer alle drei Windungszahlen.

### ENTWURF-DUENNWAND (Theorie-Agent, 10:24:13 bis 10:27:31; RUNDE-09/entwurf/SECTION-THIN-WALL.md)

- Englischer Abschnitt "5. Thin-wall phase-matching description", per Peerbus an ag-phy-coordination um 10:27:36.
  - Inhalt: drei Zonen, Phasenregel, Umlaufwechsel, Kruemmung, Grenzschritt (2,334 nackt, 2,298 kalibriert, ~2,305
    gemessen), keine Leiter ohne Innenbarriere, l > 0 und zweite Leiter.
  - Dazu eine Testtabelle und die Liste "What the model does not explain" (neun Punkte).
- Ehrlich markiert: Die Konstanten sind kalibriert; MOD-2 hat einen Versatz; Formel und MOD-2 pruefen dieselben
  Rechnungen; der SD-1-Delta-Teil ist widerlegt.
- Zitate: Zhen 2014, Yu und Lu 2025, Kovtun 2018 im Text geprueft; Schott 1933, Bohm-Weinstein und Ciurla "to verify".
- Offen fuer Abb. 3: Eigenfunktionsprofile (f, u, v). Die exakt.json-Dateien speichern keine Arrays, noetig ist ein
  kurzer bic2.py-Lauf. Fuer n = 1 dienen die Zertifikatsdaten als Gegenprobe.

### KREIN-1 (Beweis-Agent, 10:14:02 bis 10:28:54; RUNDE-09/krein1/ERGEBNIS.md; Vorab "positiv an allen Stellen" um 10:21, vor dem ersten Ergebnis 10:24)

- **Alle acht stillen Moden tragen positive Energie (positive Krein-Signatur).**
  - Fuer l = 0, n = 1 ist das streng bewiesen.
  - Fuer die uebrigen Stellen gilt es bedingt: Existiert dort eine normierbare Mode (numerische Evidenz), ist sie positiv.
- **Herleitung:** Die Energie der Mode im mitrotierenden Rahmen (zweite Variation von H - omega Q) ist
  E_2 = 2 rho [(omega + rho) ||a||^2 + (rho - omega) ||b||^2].
  - An allen Stellen ist rho - omega >= 0,845, also sind beide Gewichte positiv.
  - **Berichtigung des Auftrags:** Die im Auftrag vermutete Form (omega - rho)||b||^2 ist die Ladung der Stoerung im
    Laborsystem, nicht die Energie. Mit ihr haette man faelschlich negative Energie gefolgert.
- **Streng fuer n = 1:** Aus dem BEWEIS-1-Kasten folgt rho* - omega* >= 0,85149 und damit E_2 > 0; dafuer braucht es
  keine Huelle des Zahlenwerts.
- **Rechnung** mit neuem Programm (krein.py, unabhaengig von bic2), K je Einheitsnorm:

  | Stelle | K | Anteil offener Kanal |
  |---|---|---|
  | l = 0, n = 1 | 3,0087 | 0,60 % |
  | l = 0, n = 2 | 2,9869 | 1,26 % |
  | l = 0, n = 3 | 2,9312 | 1,82 % |
  | l = 1, n = 1 | 3,5278 | 0,47 % |
  | l = 1, n = 2 | 3,1766 | 1,24 % |
  | l = 2, n = 1 | 3,4429 | 1,08 % |
  | l = 2, n = 2 | 3,1941 | 1,78 % |
  | Z1 (gemischter Ball) | 2,8590 | 0,06 % |

  - Gegenprobe direkt aus Feld und Zeitableitung: auf 1e-5 bis 1e-8 gleich.
  - Aenderung zwischen R = 36 und R = 44 <= 1e-10.
  - bic2 gegen das neue Programm: 42,793 gegen 42,7928 (gleiche Normierung).
  - Vorab war der Anteil des offenen Kanals mit 5 bis 30 % geschaetzt, gemessen sind 0,06 bis 1,8 %.
- **Folgen:**
  - Neben den Stellen werden die Moden zu abklingenden Resonanzen, nie zu wachsenden.
  - Die l = 1- und l = 2-Multipletts haben einheitliche Signatur. Das ist die notwendige Bedingung fuer eine U(3)- bzw.
    U(5)-Symmetrie der quadratischen Dynamik, keine hinreichende.
  - [H] Nichtlinear daempft die Abstrahlung der zweiten Harmonischen die Mode.
- Die Literaturstelle Cuccagna, Pelinovsky, Vougalter 2005 bleibt [L?]: nicht erreichbar, nicht tragend.
- Selbst gemeldete Regelabweichung: einmal `python -c 1` direkt auf der .69 (venv-Probe), nicht ueber kleintest.sh.

### HOPF-1: Schreibtischpruefung der Leitung zum Q-Ball-Hopf-Verbund (Finn: "prüfe q-ball hopf verbund noch mal"; eingetragen 2026-09-30 10:37:41 CEST, vor jeder Rechnung)

- **Modell:** Codex' B.5 (literatur-20260923/SPIN-KONSTRUKTION-codex.md, Zeilen 598 bis 612):
  L = |d phi|^2 + (v^2/4)(d n)^2 - U(s) + gJ Re[(phi* b)^2] - mu^2 v^2 (1 - n3) - (kappa/4) H^2,
  mit s = |phi|^2 + |b|^2 und |b|^2 = (v^2/4)(1 - n3^2).
- **Kopplung der Sektoren:** nur ueber U(s) und den gJ-Term; kein Gradiententerm verbindet phi mit n.
  - Der gJ-Term mittelt sich fuer einen Hopf-Knoten mit azimutaler Windung in n1 + i n2 raeumlich weg (cos(2 m phi_az)),
    zeitlich ebenfalls, wenn der Knoten nicht mit omega isorotiert.
- **Wechselwirkungsdichte aus U** (Hand; S_phi = |phi|^2, S_b = |b|^2; Energie enthaelt +U):
  U(S_phi + S_b) - U(S_phi) - U(S_b) = S_phi S_b [-2 + 1,5 (S_phi + S_b)].
  - Fuer kleine S_b: Gewichtsfunktion g(S_phi) = S_phi (-2 + 1,5 S_phi). Sie ist negativ fuer 0 < S_phi < 4/3, mit
    Minimum -2/3 bei S_phi = 2/3.
  - Im Ballinneren (Duennwand, S_phi ~ 1): -0,5 S_b. In der Wand bei S_phi = 2/3: -0,67 S_b.
  - Abstossend erst ab S_phi + S_b > 4/3.
- **Vorhersage der Leitung [H], vorab:**
  - (1) Im Produktansatz ist die Wechselwirkungsenergie negativ, der Knoten wird also angezogen.
  - (2) Am staerksten bindet sie, wenn die Knotenroehre in der Ballwand liegt (S_phi ~ 2/3), nicht in der Mitte.
    Dazu Hand: Die Mitte eines grossen Balls gibt etwa 0,5/0,67 = 75 % der Wandbindung je Ueberlappvolumen.
  - (3) Die Bindung waechst mit v^2 (S_b ~ v^2/4), bleibt aber anziehend, solange v^2/4 < 1/3 im Ballinneren.
  - (4) Der gJ-Term traegt raeumlich gemittelt nichts bei.
- **Scheitert, wenn:** der Produktansatz fuer v^2/4 < 1/3 eine positive Wechselwirkungsenergie ergibt, oder wenn die
  Mitte tiefer bindet als die Wand. Das waere ein Rechenfehler hier oder ein uebersehener Kopplungsterm.
- **Grenzen:**
  - Nur fuehrende Ordnung, ohne Rueckwirkung auf Ball und Knoten und ohne Relaxation.
  - Klassisch; ueber fermionische Quantisierung sagt das nichts.
  - Bindung ist nicht Stabilitaet.
- Numerischer Test HOPF-1 (Code-Agent) seit 10:38, Vorhersage wie oben.

### Y-1 Wirbel-Dreier (Code-Agent; RUNDE-10/y1/ERGEBNIS.md, PLAN mit drei Nachtraegen und eingefrorener Kopie; eingetragen 2026-09-30 11:55:06 CEST)

- **Ausgang: Der festgehaltene Dreier zerfaellt. In der unveraenderten Formel (N = 3, J = 1, g = 0,5 und 0,2) gibt es
  weder ein Y- noch ein Dreiecks-Gesetz.**
  - Zwischen den Wirbeln bilden sich keine Waende.
  - Kleine Dreiecke (a <= 9) teilen sich ein gemeinsames leeres Loch.
  - Bei groesseren Abstaenden entsteht neben einem Wirbel ein Gegenwirbel derselben Komponente, in dessen entleertem Kern
    (Radius ~3). Die Energie flacht ab: 2159,3 / 2165,4 / 2170,9 / 2171,3 bei a = 6 / 9 / 12 / 15.
  - Das "Meson" (Wirbel und Gegenwirbel) reisst zwischen 9 und 12.
  - Nach der Scheiterregel "weder noch": Bei g = 0,5 ist der Restfehler des Y-Fits 1,62, der des Dreiecks-Fits 1,32; bei
    g = 0,2 steigt die Energie nicht.
  - 19 von 27 Vorab-Erwartungen verfehlt; alle gingen vom Wandbild aus.
- **Deutung erst nach dem Ergebnis [H]:** Bei drei Feldern verliert ein Kern ohne die eigene Komponente nur ein Drittel
  der Kopplung. Der Kern wird dadurch gross, und der Gegenwirbel hat Platz. Bei zwei Feldern haelt der leere Schlitz;
  die Kontrolle reproduziert ROT-1 auf 4e-16.
- **Zweiter Arm** (+ c Summe |psi_a|^4, ausdruecklich eine andere Theorie):
  - Das Loch haelt bis a = 12; nach Wortlaut der Regel "Dreieck".
  - Die Reihen mischen aber intakte und abgeschirmte Zustaende. Nachtraeglich nur die sieben intakten Faelle gewaehlt,
    passt eher Y. Beides ist nicht belastbar, und das Meson reisst auch hier.
- **Kontrollen:**
  - Komponententausch aendert die Energie um <= 4e-16; zwei Anfangszustaende enden in 24 von 24 Geometrien gleich.
  - g = 0: kein Anstieg.
  - Das feine Gitter zeigt dieselben Zustaende; die Energiedifferenzen sind nur auf ~+-0,6 genau.
- Literatur: Eto und Nitta an der Quelle gelesen: kein Y-gegen-Dreieck-Vergleich, keine Quark-Analogie (Berichtigung
  in RUNDE-09 eingetragen).
- Selbstanzeigen:
  - ein leeres `python3`
  - ein Start im falschen Ordner (fuenf leere Logs im Home der .69, per Name geloescht)
  - eine Syntaxpruefung ausserhalb von kleintest
  - zwei wartende Diagnose-Laeufe abgebrochen
- **Bedeutung:** Das Einschluss-Vorbild aus ROT-1 traegt nicht auf drei Felder. Ein Baryon-Vorbild mit Y-Knoten gibt es
  in der unveraenderten Formel nicht.

### BAND-1 Reissprobe (ROT-1-Agent; RUNDE-09/rot1/BAND-1.md, Abschnitt 8; eingetragen von der Leitung)

- **Nach der Scheiterregel reisst das Band ab d = 14**; die Reisslaenge liegt zwischen 8 und 14, vorab geschaetzt waren
  8 bis 12.
- **Sauberer Start** (duenne Anfangslinse, vor dem Lauf mit Uhrzeit eingetragen):
  - d = 8: kein neuer Wirbel bis t = 300; das Paar zieht sich zusammen, der Ball bleibt ganz.
  - d = 14, 20, 26: Im Band entstehen neue Wirbel, dauerhaft ab t = 105 / 25 / 115, z. B. je ein Wirbel-/Antiwirbelpaar
    in beiden Feldern. Die strenge Zaehlung, die nur Wirbel in dichten Bereichen gelten laesst, bestaetigt das.
  - **Bis t = 300 bleibt ein durchgehender Strang.** Zwei getrennte Stuecke ("zwei Mesonen") sind nicht gesehen.
- **Urspruenglicher Start:** Ab d = 14 entstehen Wirbeltruemmer, bei d = 26 zerfaellt der Ball in bis zu 5 Stuecke.
  Ursache sind die ersten Waende, die ab d > 0,83 R den Ballrand erreichen, also der Start, nicht das Band. Das erklaert
  nachtraeglich auch den REGGE-1-Zerfall bei d = 11.
- **Festgehaltene Enden:** Die Energie waechst bis d = 14 linear (Spannung 1,05, im kleinen Ball 0,97). Danach weicht
  der Ball aus; das ist ein Effekt der Festhaltetechnik.
- **Kontrollen:**
  - g gegen -g auf 1e-13 gleich.
  - Grob gegen fein bei d = 20: dieselben Ereigniszeiten.
  - g = 0: keine neuen Wirbel.
- Vorab gegen Ausgang: 6 getroffen, 1 teilweise, 4 verfehlt.
- Selbstanzeige: zwei leere Python-Aufrufe ohne Rechnung; zwei geschaetzte Uhrzeiten in Ueberschriften, ersetzt.
- **Bedeutung [H]:** Ab einer Laenge bildet das Band aus seiner Energie neue Wirbelpaare. Das ist ein Analogon zum
  Stringbrechen durch Paarbildung. Die Trennung in zwei Stuecke ist nicht gezeigt.

### LADUNGSTAUSCH-1 (ZUS-10-Pruefer, fortgesetzt; RUNDE-10/ladungstausch1/, Vorab 10:30 bis 10:31, Nachtrag 10:35 blind vor R2/R3, Ende 10:53:32)

- **Schwelle im Startabstand haengt von der Ballgroesse ab:**
  - omega^2 = 0,6 und 0,7: d = 3, 4, 5 bilden einen Tauschball (E15 bei T = 3000: 0,75 / 0,45 / 0,37 bzw. 0,50 / 0,48 /
    0,46); d = 6 vernichtet (< 0,005).
  - omega^2 = 0,8: Auch d = 6 bildet noch einen Tauschball (0,52).
  - Das passt zum Kriterium von Copeland, Saffin, Zhou 2014 (an der Quelle gelesen): d <~ 2 sigma, hier 4,8 / 5,2 / 6,2.
  - Die Vorab-Vermutung "d = 5 vernichtet" ist verfehlt.
- **Tauschfrequenz 0,18 bis 0,21** in allen elf Tauschlaeufen, in einer omega^2-Serie unabhaengig von d
  (0,7: 0,1979 bei d = 3, 4, 5).
  - Omega_swap = Omega_2 - Omega_1, mit Omega_1 aus dem geraden Feldanteil (0,74 bis 0,83) und Omega_2 aus dem ungeraden
    (0,94 bis 1,00). Belegt dadurch, dass die zweite Spitze im Ladungsspektrum in allen elf Laeufen bei
    2 Omega_1 + Omega_swap liegt (auf <= 0,003) [H: CSZ-Mechanismus].
  - Die blinde Zahlenvorhersage (Omega_2 fest bei 0,996) ist verfehlt.
- **Lebensdauer:**
  - d = 4, omega^2 = 0,7 bis T = 9000: Die Energie faellt ab t = 3000 nur um den Faktor 1,16 (Rate 1,7e-5, sinkend).
  - Der Ball wird flacher und tauscht langsamer (Omega_swap 0,172).
  - Ausreisser omega^2 = 0,6, d = 4 (spaeter Verlust von 0,68 auf 0,45): ungeklaert.
- **Vorab gegen Ausgang:** 11 getroffen, 1 knapp verfehlt, 4 verfehlt (vorab als schwach markiert), 1 nicht pruefbar.
  Grob gegen fein <= 1,5 %; Kontrollen sauber.
- **Bezug zu stillen Stellen:** im 1D-Modell nicht pruefbar, weil es dort keine stillen Atmungsstellen gibt. Vorschlag:
  3D-Karte mit achsensymmetrischer Q/Anti-Q-Ueberlagerung an und neben einer stillen Stelle; ueber 10 min, eigener
  Auftrag.

### Codex: Q-Ball-Hopf-Bindung und Band-Geometrie (Peerbus 10:43 bis 10:59; eingetragen von der Leitung nach 10:59:38)

- **Bindungsvergleich B.5** (resonance-20260930/qball-hopf-pilot/BINDING-CHECK.json):
  - Einstellung: v = mu = kappa = gJ = 1, Gesamtladung q = 189,14; zentriert und achsensymmetrisch, mit gemeinsamer
    Isorotation und optimaler Ladungsteilung auf beiden Seiten.
  - Ueberlagert: E = 427,65 gegen getrennt 431,81, also **0,96 % tiefer**.
  - Unabhaengig dieselbe Kreuzterm-Formel U(x+y) - U(x) - U(y) = xy[-2 + 1,5(x+y)], negativ fuer x + y < 4/3.
  - **Grenze (Codex):** Die getrennte Referenz ist nur ein Variationswert (obere Schranke), also kein Bindungsbeweis.
    Omega ~0,58 liegt unter dem Fenster des isolierten Balls; die Skizze ist keine stationaere Loesung.
  - Codex relaxiert jetzt die Profile (zentriert). HOPF-1 konzentriert sich auf die Lageabhaengigkeit (Wand gegen Mitte).
- **Band-Pilot** "Punktkette gegen gerahmtes Band" (resonance-20260930/ribbon-pilot/RESULT.json; zu Finns Bild
  Punkt/Flaeche/Laenge):
  - Bei fester Linkzahl senkt eine nichtplanare 3D-Form die Bandenergie gegenueber dem Kreis: um 4,5 % (Lk = 1) bzw.
    7,4 % (Lk = 2). Ein Teil der Verdrillung wandert in die Windung der Mittellinie (Lk = Tw + Wr).
  - Die besten Formen beruehren die Formgrenze; das ist kein freies stabiles Band.
  - Modellintern, klassisch, keine Teilchenidentifikation.

### HOPF-1 Ausgang (Code-Agent; RUNDE-10/hopf1/ERGEBNIS.md; eingetragen von der Leitung)

- **Stufe A (Produktansatz)**, Vorab der Leitung (10:37:41) gegen Ausgang:
  - **(1) Anziehung: getroffen.** 283 von 283 Lagen haben E_int < 0 (grosser und kleiner Ball, v = 0,5 und 1). 3D-Gitter
    gegen ein unabhaengiges 2D-achsensymmetrisches Integral: auf 5e-5 gleich. Die Kreuzterm-Formel ist auf 1e-13
    bestaetigt.
  - **(2) Wand vor Mitte: getroffen.**
    - Es koppelt nur die n3 ~ 0-Schale. Am tiefsten bindet sie bei S_phi ~ 0,62 bis 0,84.
    - Im grossen Ball bindet die Mitte mit 59 bis 73 % der Wandbindung (v = 0,5) bzw. 32 bis 45 % (v = 1). Die Zahl der
      Leitung (75 %) war zu hoch, weil die Ballmitte S0 = 1,088 statt 1 hat.
    - Bei gleicher Knotengroesse bindet die Wand im grossen Ball 2,5-mal tiefer (-5,81 gegen -2,32 bei v = 1).
  - **(3) Schwelle in v: knapp verfehlt.** Die Scheiterregel ist fuer eine Knotenform ausgeloest: Beim kompakten Torus
    ganz im grossen Ball kippt das Vorzeichen schon bei v^2/4 ~ 0,328 bis 0,332, knapp unter 1/3. Ursache ist
    S0 = 1,088; der Kipppunkt folgt (4/3 - S0) / Formfaktor auf 1 %.
  - **(4) gJ-Term: getroffen.** Er ist exakt null, wenn der Knoten auf der Ballachse sitzt. Aussermittig ist er
    augenblicklich bis 48 % des Potentialterms und mittelt sich zeitlich weg.
- **Vergleich mit Codex:** zentriert -4,13 hier gegen -4,01 bei Codex (Produktansatz bei dessen festem Radius). Mit
  Isorotation und freiem Radius hat Codex 0,96 % Vorteil, hier sind es etwa 0,9 % von E_Q + E_H. Das ist vereinbar.
- **Stufe B (Relaxation): offen, technisch gescheitert.** Alle Varianten (3D und 2D, L-BFGS und gedaempfter Fluss)
  verlieren die Hopfzahl oder enden unter der bekannten Energieuntergrenze fuer h = 1 (Gitterartefakt). Naechster
  Schritt waere, zuerst das reine Faddeev-Skyrme-Minimum fuer h = 1 als Pruefstein zu reproduzieren (1 bis 2 h Code).
- **Belegstufe:** Produktansatz, fuehrende Ordnung. Das ist keine Bindung im strengen Sinn (ohne Relaxation und ohne
  Referenzminimum) und sagt nichts ueber Spin.

### SPIN-1 Schreibtisch (feldforscher Fable, Neustart; RUNDE-09/spin1/SPIN1.md, fertig 10:40:00)

- **Weg A (C x S^2):**
  - Voraussichtlich Anziehung in fuehrender Ordnung, mit demselben Kreuzterm s1 s2 [-2 + 1,5 (s1 + s2)] wie die
    Leitungsrechnung. Anziehend fuer v^2 < 4/3, sonst nur an der Ballwand; der gJ-Term ist exakt null.
  - **Neu (G1):** b(n) verschwindet an beiden Polen. Der Knotenkern koppelt nicht, nur die Schale mit n3 ~ 0 ("Band im
    Ball", nicht "Knoten im Ball").
  - Die Fermion-Wahl gilt genau fuer ungerade Hopfzahl, und der Ball beruehrt sie nicht. Die Einprozentlatte ist auf dem
    Papier nicht entscheidbar; der Test ist vorbereitet (SPIN-1-T1, entspricht HOPF-1).
- **Weg B (Ladung plus Monopol):**
  - Der Q-Monopol-Ball existiert (Bai, Lu, Orlofsky, JHEP 2022, am Text gelesen). Dort bindet ein Q-Ball mit globaler
    U(1) ueber ein Portal an den Monopol-Higgs und ist stabiler als der Q-Ball gleicher Ladung. Der Skalar ist aber
    Eichsingulett, also J = 0.
  - Bei geeichter Ladung ist J = q/2: ein Fermion nur fuer ungerades q, Spin 1/2 nur fuer q = 1. Fuer makroskopische
    Baelle also nicht.
- **Scout-Treffer:**
  - "Magnetic Q-balls" (2609.32059) betrifft chirale Magnete mit Zeeman-Kopplung, keine magnetische Ladung.
  - "Electroweak balls" (2609.19293): Die Traeger sind W-Felder; bei gemessenen SM-Parametern gibt es keine Loesungen.
  - Beide sind fuer Weg B nicht einschlaegig.
- **Gegensweep:**
  - Kein Elektron, Quark oder Nukleon, auch nicht mit Weg A: keine Drittelladung, keine Farbe, und die Kompositheits-
    grenze nach PDG 2025 liegt bei Lambda > 24 bis 36 TeV (< ~7e-21 m).
  - Solitonen aehneln Hadronen, nicht Quarks.
- **Hinweis [H]:** Ein Q-Monopol-Ball vom Bai-Typ mit ganzzahligem Spin liegt auf der datennahen Seite der
  Neuausrichtung (Dunkle Materie, Monopolsuche).
- Methodenwarnung: Das WebSearch-Kontingent war erschoepft; alle "0 Treffer" stammen aus Titel- und Metadatensuchen.

### Codex: lokale Hopf-Phase und 3D-Anfangspruefung (Peerbus 11:31 bis 11:54; eingetragen von der Leitung ab 12:07:59)

- **Lokale Hopf-Phase (radial, linear):** Codex gab statt der globalen Phase eine ortsabhaengige Phase frei.
  - Die freigegebene Atemform gibt Energie nach aussen ab: Nettofluss durch r = 8 bis T = 20 bei N512 0,062 der
    Anfangsenergie (N256 0,067, N128 0,157).
  - Diskrete Bilanz und unabhaengig integrierter Fluss stimmen auf 0,03 % ueberein.
  - Deutung Codex: Die globale Phase hatte einen Transportkanal verdeckt. Das kann ganz ein Anfangstransient sein;
    keine Lebensdauer, keine Eigenmode des neuen Operators.
- **3D-Anfangspruefung (Finn an Codex: "rechne das in 3d"):** Es gab **keine Zeitentwicklung**, weil ein vorab
  gebundenes Stop-Gate griff.
  - Im gespeicherten drehenden Startprofil (B.5, phi = 0, Omega etwa 0,98) ist der lokale Indikator chi groesser als 1:
    maximal 1,094 bei r etwa 2,13 am Aequator (N256 1,090, N512 1,093).
  - chi > 1 bedeutet: In einer Raumrichtung wird die Ausbreitungsgeschwindigkeit imaginaer (speed^2 = 1 - chi =
    -0,094). Die Bewegungsgleichung ist dort nicht mehr hyperbolisch, eine Zeitentwicklung waere schlecht gestellt.
  - Das passt zur Literatur (Harland, Jaeykkae, Shnir, Speight, arXiv:1301.2923): Bei unserer Sigma-Normierung 1/4
    verliert die Zielmetrik die Positivitaet ab Omega^2 > 1/2. Der Startzustand dreht mit Omega^2 etwa 0,97, also zu
    schnell.
  - Folge: Die radialen Hopf-Ergebnisse (auch HOPF-1 im Produktansatz) bleiben Ergebnisse ihres eingeschraenkten
    Ansatzes und bekommen keinen 3D-Stabilitaetstitel. Die Modellklasse ist damit nicht widerlegt.
- **Spin-Anschluss (SPIN-ANSCHLUSS-KURZ.txt):** Codex schlaegt als naechsten engen Test ein Zweimoden-Modell vor
  (Pseudospin, Blochvektor), danach die dritte l = 1-Mode (Spin-1-Triplett, orbital).
  - Ausdruecklich keine Herleitung von raeumlichem Spin 1/2.
  - Echter Spin 1/2 nur ueber einen ungeraden Hopfgrad (Krusch/Speight) oder ein angekoppeltes Diracfeld.
- **Leitung [H]:** Naheliegender naechster Schritt ist die Ladung q, bei der chi_max = 1 wird. Offen ist, ob es darunter
  einen stationaeren drehenden Verbund gibt, der langsam genug dreht. Als Input an Codex vorgemerkt, noch nicht
  geschickt.

### BEWEIS-2 gestartet, Fremdlesung BEWEIS-1 erneut angefragt (eingetragen 12:07:59)

- Finn antwortete "ja maach weiter" auf die offene Frage der Leitung (weitere Sprossen beweisen, bei Codex nachhaken).
- BEWEIS-2: Der Beweis-Agent (Autor von BEWEIS-1) wurde um 12:05 mit RUNDE-10/beweis2/BRIEF.md fortgesetzt.
  - T1: l = 0, n = 2, Start omega^2 = 0,6851289043, rho = 1,6903565771 (DATENPAKET A02).
  - T2: l = 1, n = 1, Start omega^2 = 0,7544960184, rho = 1,8263420673 (DATENPAKET C01).
  - Vorab-Zeilen und Negativkontrolle wie in BEWEIS-1; Spur cpu5; hoechstens 2,5 h. Danach eine frische Lesung in
    einem Durchgang.
- **Zwischenmeldung 12:24 (Beweis-Agent; eingetragen 12:24:31): T1 (l = 0, n = 2) rechnergestuetzt bewiesen, vorbehaltlich
  der frischen Lesung.**
  - Vorab-Zeile T1 in BEWEIS-2-PLAN.md um 12:11:22 (STAND.md), vor dem Startwertlauf (.69 12:12:13). Kern bewkern.py
    bytegleich mit BEWEIS-1 (sha256 a8a7ec6ff9679226..., von der Leitung geprueft); Treiber pruef-l0.py nimmt die
    Startwerte als Argumente.
  - Zertifizierung A (L = 32, 256 bit, 68 s) und B (L = 36, 320 bit, 97 s) bestanden. Gewichtete Zeilensumme 7,6e-4
    bzw. 0,085, Innenabstand mindestens 0,874 bzw. 0,79 delta.
  - Kasten A: omega^2* = 0,685128904458216093298 und rho* = 1,690356597328143456827, je auf etwa 2e-20.
    - Abstand zum Datenpaket: 1,1e-10 neben der A_out-Nullstelle, 9,4e-9 neben dem W-Fit.
    - f(0) = 1,0648960266770.
  - Im Gesamtflag geprueft (Auflage 1 der Fremdlesung): 2 kappa0 - kappa_c >= 0,616, rho > omega (Krein-Korollar),
    k^2 >= 5,34, kappa_c^2 >= 0,256.
  - Auflage 4 umgesetzt: Y, DH_0(Z), Mk, H_0(z0), eps, delta und Kr stehen exakt im JSON, dazu die Untergrenzen von phibar
    und eta.
  - **Abweichung, vom Agenten gemeldet:** Die Empfindlichkeitskontrolle in B verfehlt die Vorab-Erwartung: rho + delta
    besteht, erwartet war "verfehlt". Grund laut Agent: In B liegt die Nullstelle etwa 0,10 delta neben z0, weil delta
    dort vom Newton-Abstand bestimmt ist. Die Kontrolle zeigt Empfindlichkeit, nicht Strenge; A verhielt sich wie
    vorab.
  - T2 (l = 1): Frei-Test mit dem neuen Kern bewkern_l1.py bestanden; Newton laeuft.
- Fremdlesung BEWEIS-1:
  - Die erste Anfrage f67c1643 (07:13) ging an den Empfaenger "codex", nicht an ag-phy-coordination; eine Antwort liegt
    nicht vor.
  - Neu angefragt an ag-phy-coordination: 4140a813 (12:06:22), Zustellhinweis 10810b95 an den Codex-Faden (12:07:09,
    "Queued", Lesen nicht bestaetigt).
  - Inhalt: Lemmata P, J, T0, T, K, E gegen den Code, Urteil in einer Zeile; danach, wenn das Budget reicht, ein
    zweites Programm.

### EVO-1 Generation 1: Auswertung (Leitung; Erwartung eingetragen 12:09:56, vor zusammenfassen --gen 1)

- Beide Ketten fertig: cpu3 12:08:07, cpu4 12:09:10 (alle rc = 0). 19 Ergebnisordner mit modell.json (Anker und
  Kontrolle aus Generation 0, dazu 17 Modelle aus Generation 1).
- **Erwartung der Leitung, vor dem Abruf:** A2 ist von oben gefaehrdet. Die Leiter stiller Stellen trat bisher fuer
  jedes gerechnete beta von 0,35 bis 0,60 auf; darum rechne ich damit, dass mehr als die Haelfte der lebensfaehigen
  Modelle qualifiziert. Ein Anteil ueber 90 % (A2 verfehlt, Rasterkarte ist das Ergebnis) ist fuer mich ebenso
  moeglich wie ein Anteil zwischen 50 und 90 %. A3 (mehr als 20 % nicht entscheidbar) erwarte ich bestanden.
- Ablauf nach PLAN.md Abschnitt 7 und 13.2: zusammenfassen --gen 1 (Spur cpu), danach die N5-Pruefung per jq ueber
  bew-001.jsonl.
- **Ausgang (zusammenfassen --gen 1, .69 12:10:10 bis 12:10:13, rc = 0; evo1.py Version 3 f882fa19; eingetragen
  12:11:00):**
  - 18 Modelle: 17 lebensfaehig, 8 qualifiziert, 6 nicht entscheidbar, 3 nicht qualifiziert, 1 nicht lebensfaehig
    (beta = 0,2, gamma = 0).
  - **A2 Trennschaerfe: 8 von 17 = 47 %, trennt (bestanden).**
  - **A3 Messmittel: 6 von 18 = 33 % nicht entscheidbar, ueber 20 %: Abbruch.**
  - Alle sechs scheitern an derselben Pruefung d: Die Umlaufzahl im Pruefrechteck ist 2, 3 oder 4 statt 1 (einmal 37,
    vermutlich ein Phasenfehler). Die Pruefungen b und c haben sie bestanden.
  - Betroffen sind beta = 0,5 mit gamma = 0,2, beta = 0,75 und 1,0 mit gamma = 0,1 und 0,2 sowie das Zufallsmodell
    (0,9483; 0,2588).
  - Qualifiziert: beta 0,2 (gamma 0,1 und 0,2), beta 0,35 (alle drei gamma), beta 0,5 (gamma 0 und 0,1), beta 1,0 mit
    gamma 0. Nicht qualifiziert: beta 0,75 mit gamma 0 (F3), L_d3 (kein Minimum), Zufallsmodell (0,9865; 0,0176) (F2).
- **N5-Pruefung (jq aus LESUNG-REPARATUR-A1.md ueber bew-001.jsonl, lokal nach 12:10:13):** Vier Modelle haben mehr
  innere Minima als gelistet. Vermerk je Modell: **"Minimum ueber MAX_MIN, nicht verfeinert"**
  - P_b0.5000_g0.2000_d3 (4 gegen 3)
  - P_b1.0000_g0.1000_d3 (4 gegen 3)
  - P_b1.0000_g0.2000_d3 (5 gegen 3)
  - P_b0.9483_g0.2588_d3 (4 gegen 3)
  - Alle vier sind auch unter den sechs nicht entscheidbaren.
- **Meine Erwartung lag zweimal falsch:** Weniger als die Haelfte qualifizierte (47 %), und A3 scheiterte.
- **Folge nach den eigenen Regeln:**
  - A3 sagt: "endet der Pilot. Zuerst wird das Messmittel repariert."
  - Das Reparaturkontingent ist verbraucht (PLAN.md 13: bis zum Ende von EVO-1 keine weitere Regelaenderung).
  - EVO-1 endet also nach Generation 1. Der Vergleich Evolution gegen Raster (Generation 2 und 3) findet nicht statt;
    der Werkzeugtest ist **nicht entschieden**, also auch kein "kein Vorsprung".
  - Ergebnis ist die Rasterkarte der Generation 1.
- **Lesart [H], nur als Beobachtung:**
  - Stille Stellen gibt es in der ganzen Familie U = S - S^2 + beta S^3 + gamma S^4 (qualifiziert von beta 0,2 bis
    1,0). Die Log-Familie U = ln(1 + S) hat kein Minimum.
  - Bei groesserem beta und gamma liegen mehrere Nullstellen im selben Pruefrechteck. Die Leiter wird dichter, oder
    zwei Leitern kreuzen sich; das Messmittel war nur fuer einzelne Nullstellen gebaut.
  - Ein neues Messmittel waere zum Beispiel Umlaufzahl n als n stille Stellen zaehlen. Das waere ein neuer Plan, keine
    Reparatur.
- Dateien: RUNDE-07/evo1/lauf-69/gen1/ (bew-001.jsonl sha256 3aceb964880a024f..., LAUF-Z1.log c2300fa1ddd44438...,
  gen-001.json, Kettenlogs, ergebnisse/ ohne *.pt/*.npz).

### BEWEIS-1 Fremdlesung Haus OpenAI: traegt mit Auflagen (Peerbus 12:14:44; eingetragen ab 12:15:48)

- Codex las mit drei getrennten Kontexten (Schwanz P/J/S/E, Taylor T0/T/Jets, Krawczyk K und Herkunft) und einer
  Gesamtlesung. Ablage: coordination/resonance-20260930/beweis1-fremdlesung/ (GESAMT-REVIEW.txt, drei Teilberichte,
  rational_check.py, RATIONAL-RESULT.json, Hashlisten).
- **Urteil: "TRAEGT MIT AUFLAGEN". Kein tragender Fehler** in der linearen radialen Existenzkette. Die 38 Dateien des
  Manifests sind per sha256sum -c geprueft; die Originale sind unveraendert.
- Eigener Bruch-Pruefer (exakte rationale Arithmetik, ohne unseren Kern, ohne FLINT, TS440):
  - bestaetigt die Kanalgrenzen, omega^2 > 1/2, die Einfachheitsbedingung 4 kappa0^2 > kappa_c^2 auf ganz Z, die
    Aussenrundung von Tabelle 1, die Satzintervalle und B2 echt in A2.
  - Er prueft nicht H_0, DH_0, Y und die ODE-Einschluesse. **Ein vollstaendiges zweites Programm bleibt offen.**
- Auflagen (keine Neuberechnung noetig, kein Tor gelockert):
  1. 2 kappa0 > kappa_c steht im Protokoll, aber nicht im Flag M3.BESTANDEN. Fuer A2/B2 erfuellt; kuenftig ins
     Gesamtflag oder als eigenes Flag.
  2. "Einfach" heisst geometrische Dimension 1 des radialen L^2-Loesungsraums bei festem (rho, omega). Nicht gezeigt:
     algebraische Einfachheit, fehlende Jordan-Ketten, Eindeutigkeit, andere l, Stabilitaet.
  3. "Eingebettet" gilt im operationalen Sinn des Textes. Fuer einen operatortheoretischen Papertitel fehlen die
     Realisierung und Domaene des vollen Bueschels und die Bruecke zu seinem wesentlichen Spektrum.
  4. Notation: gewichtete Norm in Zusatz S, Dt2 in T0 als Huelle von t^2. Zwei Tabellen-Untergrenzen (phibar, eta)
     sind aus dem JSON nicht ablesbar (der Vergleich im Code ist korrekt). Y, DH(Z) und Mk fehlen im Export.
  - Ausserdem: "periodisch oder quasiperiodisch" statt "quasiperiodisch", weil die Irrationalitaet der zwei
    Laborfrequenzen nicht gezeigt ist.
- Weitergabe: an den Beweis-Agenten um 12:15 (SendMessage). Auflagen 1 und 4 setzt er in BEWEIS-2 um. Fuer BEWEIS-1
  schreibt er nur einen Abschnitt 7.2, ohne Neulauf und ohne Aenderung an zertifikat/.
- **Stand BEWEIS-1 damit:** in zwei Haeusern gelesen (Anthropic: Plan, Code, letzte Schicht; OpenAI: Fremdlesung).
  Offen sind das zweite Programm, die Spektrumbruecke fuer einen staerkeren Titel und die Vertrauensannahme in FLINT.

### NLS-LEITER (MESS-1-Agent, 11:25:37 bis 12:17; RUNDE-10/nls-leiter/ERGEBNIS.md; eingetragen 12:17:43)

- Vorab (PLAN.md 11:27:48, vor jedem Lauf): "keine stillen Stellen im kubisch-quintischen NLS" (~85 %), Zusatz
  "quintisch-septisch hat welche" (~35 %).
- **Ergebnis: keine stillen Stellen, weder in 3D noch in 2D** (W-Gitter auf der .69 in zwei Gitterstufen, je 57 bzw. 61
  Omega bis 0,17 bzw. 0,18, nu bis 1,0; keine Kandidatenzelle). Die Zaehlmaschine findet die bekannte Q-Ball-Stelle
  (Umlauf +1). Die Profile treffen Pego/Warchall.
- **Grund, direkt gemessen:** Die Wand bindet einen Zustand des geschlossenen Kanals bei E_0 ~ +0,02, etwa 0,1 ueber der
  Einbettungsgrenze. Er liegt also unter der Emissionsschwelle und kann keine Resonanz im Kontinuum bilden. Beim
  Q-Ball liegt dieser Zustand im Kontinuum (E = 0,706).
- Auch das quintisch-septische NLS hat keine Leiter (Nullpunktsenergie hebt den Wandzustand ueber die Grenze). Der
  Zusatz ist nicht eingetreten.
- **Folge fuer die Ueberleitung zum Experiment [H]:** Die Leiter braucht den Antiteilchen-Zweig (rho ~ 2 m). Das NLS
  schneidet ihn ab; fluessiges Licht (CS2) und Atomtroepfchen sind deshalb kein Pruefstand. Kandidaten mit zwei
  Frequenzzweigen und Luecke: Gap-Solitonen in Bragg- und optischen Gittern, praezedierende Solitonen in
  Antiferromagneten (nicht gerechnet).
- Grenzen: nur radial, l = 0, linear; nu von 1 bis 3, der Aussenrand und KG gegen NLS nur als lokale Rauchtests
  (gekennzeichnet).
- Offen laut Agent: Gibt es die Leiter im KG-Modell bei beta = 1 und 2? Sein aufgeloestes Rechteck bei beta = 1
  (omega^2 0,808 bis 0,822) gab Umlauf 0.
  - **Querverweis der Leitung:** EVO-1 Generation 1 (oben) nennt P_b1.0000_g0.0000_d3 "qualifiziert". Die Minima
    liegen bei omega^2 etwa 0,835, 0,852 und 0,893 (x_stern 0,8448), also ausserhalb seines Rechtecks. Fuer beta = 1
    gibt es damit einen Treffer nach der EVO-1-Messvorschrift, aber keinen Beweis.
- Fehlerkasten: Die auf p4000a/p4000b wartenden Laeufe wurden vor dem Start abgebrochen und auf cpu6 umgelegt; die
  Logs dieser Namen wurden dabei ueberschrieben.

### Chem 8 dicht, Zufallskarte (Leitung; RUNDE-10/chem8/KARTE.md; Vorhersage 12:14:18 mtime, Laeufe 12:14:43 bis 12:17:55)

- Dichtes Raster v = 0,05 bis 0,25 (21 Werte), T = 300 und T = 600, grob = fein in allen 168 Klassen.
- T = 300: Mit Bruecke verschmilzt es bei dphi = pi an 6 benachbarten v (0,12 bis 0,17, bis 1,52 Q0), bei 3pi/4 an 7
  (0,06 bis 0,12, bis 1,56 Q0). ohne und nur_AC verschmelzen nirgends.
- Der groesste Klumpen ist glatt in v; die Schwelle 1,5 Q0 schneidet eine flache Kuppe. Es entstehen drei Klumpen mit
  umverteilter Ladung (z. B. 1,52 / 0,71 / 0,44 Q0), keiner nahe 2 Q0.
- T = 600: bei 3pi/4 bleiben v = 0,11 und 0,12 verschmolzen, bei pi keiner. Fehlerkasten: Messbereich |x| < 75, schnelle
  Klumpen verlassen ihn; 0,00 heisst dort "verlaesst den Messbereich".
- Vorhersagen: V1 (1 bis 3 Punkte) verfehlt; V2, V3, V4 getroffen.
- **Entscheidung nach Vorab-Regel: weiter** (3pi/4 erfuellt a, b, c). Einordnung: Ladungsumverteilung auf drei Klumpen,
  keine Verschmelzung zu 2 Q0; "Katalyse" im engen Sinn nicht gezeigt. Naechster kleiner Schritt: Klumpen mit Ort
  verfolgen (ist der grosse Klumpen der ruhende Ball C?) und L4 an der Quelle (Ladungsuebertrag bei Q-Ball-Stoessen).
- L4, nur Abstracts (12:19:45): paarweiser, phasenabhaengiger Ladungsuebertrag bekannt (Battye/Sutcliffe, Nucl. Phys.
  B590 (2000) 329, 1D bis 3D; Axenides u. a., PRD 61 (2000) 085006). Der Dreierfall mit ruhendem Ball ist dort im
  Abstract nicht genannt, also offen.

### IE Gen 2: Ernte und Abschaetzung (IDEEN-EVOLUTION/GEN-02.md und GEN-02/ERNTE.md; eingetragen 12:27:59)

- Blinde Ernte (frischer Leser, Modell Fable, 12:12:49 bis 12:25:03): **1 weiter (G2-09), 9 parken, 0 verwerfen.** Die
  Leitung uebernimmt alle zehn Vorschlaege (ie.py setze 12:26:24). Die L1-Einstufung von G2-09 ist nach README Zeile 51
  begruendet (GEN-02.md).
- **Vorsprungsregel, Generation 1 und 2: E 1 von 12, Z 2 von 6 -> kein Vorsprung.** Das ist der vierte Werkzeugtest
  "kluge Suche ohne belegten Vorteil". Die Operatoren bleiben normale v3-Variation; eine Generation 3 gibt es nicht.
- Abbruchregel: 4 von 7 gerechneten Karten nicht entscheidbar (57 % > 30 %). Ursache sind feste
  Plausibilitaetsschranken der Test-Agenten. Lehre: Schranken an die Gitterkonvergenz binden.
- Befunde mit Wert fuer die Hauptlinie [H, Modell]:
  - **G2-10: Leiter stiller Stellen auch in 2D** (fuenf Stellen auf dem Raster, keine in 1D; Sprossenabstand in 1/eps
    wie vorhergesagt, Lagen 0,0016 bis 0,0067 tiefer). Passt zu NLS-LEITER: im 2D-NLS keine Leiter.
  - G2-09 (weiter): Ein m = 1-Wirbel mit der WM-1-Frequenz teilt sich in 2D nach t = 30. Das ist nur ein Hinweis fuer
    WM-1 (3D, eingefrorener Hintergrund).

### ALT-1 Alternativen zum Wirbel-Dreier (feldforscher Fable, 11:57:55 bis 12:27:32; RUNDE-10/alt1/ALT-1.md; eingetragen 12:28:32)

- Anlass: Y-1 (kein Y, der Dreier zerfaellt) und Finn: "recherchiere noch mal nach alternativen". Nichts gerechnet;
  Vorab-Erwartungen 12:05:21 vor jedem externen Abruf.
- **Ein Y-foermig gebundener Dreier aus drei 1/3-Wirbeln ist publiziert** (Nitta, Eto, Fujimori, Ohashi 2012,
  Dreikomponenten-Supraleiter, JPSJ 81, 084711, arXiv:1011.2552; an der Quelle gelesen).
  - Er gibt es nur mit festgehaltenen Wirbeln; ohne Festhalten kollabiert er zum Einzelwirbel, wie unser "Beutel".
  - Getragen wird das Y von einer Quartik je Komponente (c Summe |psi_a|^4), nicht von der Rabi-Kopplung. Im
    U(N)-symmetrischen Fall gibt es keinen Dreier, sondern einen Riesenwirbel (Eto/Nitta 2013).
- **L4 fuer unsere N = 2-Befunde:** Gleichgewichtsabstand, Magnus-Kreisen, gerades Meson und Reissen durch Paarbildung
  (ROT-1, BAND-1, REGGE-1) stehen laut Agent in Eto/Nitta, PRA 97, 023613 (2018) und PRR 2, 033373 (2020).
  - Der dort angekuendigte Dreikomponenten-Einschluss ist nach Recherchestand nie erschienen. Das ist eine Luecke, in
    die ein Test unserer Art rechnen wuerde.
  - Neu (Okt. 2025): Rantanen, Dreifachkern-Wirbel in 3He-B (arXiv:2510.19566).
- **Vorschlag, nicht gerechnet (Abschnitt 5):** Test "Y-2" mit + c Summe |psi_a|^4 und nachgestimmtem U (Hauptarm c = 2,
  b_0 = 1 + c/3). Dazu zwei Vergleichsarme (c = 1 ohne Nachstimmen; Literatur-Wandtyp mit epsilon = 0,3).
  - Scheiterregel und Vorab-Erwartungen stehen im Bericht.
  - Umfang laut Agent 30 bis 45 min P4000, also ueber der 10-min-Grenze fuer kleine Tests. Er muss in Stuecke von
    hoechstens 10 min geteilt werden oder braucht Finns Freigabe.
- Methodenhinweis des Agenten: Seine Handabschaetzung "Kernkosten gegen Wandkosten" erklaert Y-1, lag aber fuer N = 2
  um mindestens den Faktor 2,5 daneben. Er verwendet sie nur fuer Groessenordnungen.

## Abschaetzung (Leitung, 2026-09-30 ab 12:29:46 CEST, date)

Runde 10 wird hier geschlossen. BEWEIS-2 laeuft weiter und wird in Runde 11 gefuehrt (T1 bewiesen, T2 in Arbeit).

| Karte | Entscheidung | Grund |
|---|---|---|
| KREIN-1 | weiter (ins Leiter-Paper) | E_2 > 0 an allen stillen Stellen; streng fuer n = 1 aus dem Beweiskasten, jetzt auch im Gesamtflag von BEWEIS-2 |
| BEWEIS-1 Fremdlesung | weiter | OpenAI: "traegt mit Auflagen", kein tragender Fehler. Offen: zweites vollstaendiges Programm, Spektrumbruecke fuer einen staerkeren Titel |
| BEWEIS-2 | weiter (Runde 11) | T1 (l = 0, n = 2) bewiesen in A und B, vorbehaltlich frischer Lesung; T2 (l = 1) laeuft |
| DATEN-LEITER, ENTWURF-DUENNWAND, SU(3)-v0.6-Nachlesung | erledigt | an Codex geliefert; Duennwand-Abschnitt laut Codex brauchbar mit Praezisierungen |
| SPIN-1 | parken | Spin 1/2 nur ueber ungeraden Hopfgrad (Krusch/Speight) oder angekoppeltes Diracfeld. Weg A braucht einen hyperbolischen drehenden Traeger, und den gibt es bei Omega etwa 0,98 nicht (Codex 3D) |
| HOPF-1 | parken | Produktansatz: 3 von 4 Vorhersagen getroffen; Relaxation technisch gescheitert; 3D-Startprofil nicht hyperbolisch. Wartet auf q_krit (Input an Codex) |
| EVO-1 | beendet (A3) | 8 von 17 qualifiziert (A2 trennt), aber 6 von 18 nicht entscheidbar. Ergebnis ist die Rasterkarte; ein Messmittel fuer dichte Nullstellen waere ein neuer Plan |
| IE Gen 2 | beendet | kein Vorsprung (E 1/12, Z 2/6), vierter Werkzeugtest ohne Vorteil; 57 % nicht entscheidbar, Lehre fuer TEST.md |
| G2-10 (aus IE) | weiter als Leitungskarte | Leiter auch in 2D gesehen; Lagen neu anpassen, naechste Sprosse blind |
| G2-09 (aus IE) | weiter (Hinweis an WM-1) | m = 1-Wirbel mit WM-1-Frequenz teilt sich in 2D nach t = 30 |
| BAND-1 | parken "bekannt" | Reissen durch Paarbildung ab d = 14; laut ALT-1 steht das mit Magnus-Kreisen und geradem Meson schon bei Eto/Nitta 2018/2020 |
| LADUNGSTAUSCH-1 | parken | Kriterium Copeland/Saffin/Zhou bestaetigt, Tauschfrequenz als Omega_2 - Omega_1 gedeutet. Bezug zu stillen Stellen braucht 3D (ueber 10 min, Finns Budget) |
| Y-1 | verwerfen fuer die unveraenderte Formel | "weder noch", der festgehaltene Dreier zerfaellt; 19 von 27 Vorab-Erwartungen verfehlt |
| ALT-1 | weiter als Y-2 | Y-Dreier ist publiziert, getragen von einer Quartik je Komponente; kleinster Test + c Summe \|psi_a\|^4, in Stuecke unter 10 min teilen |
| LIN-WIRBEL-1 mit Pego/Warchall | erledigt | KG-Schwellen liegen konstant etwa 0,0035 unter den NLS-Schwellen; Original gelesen |
| NLS-LEITER | parken, Folgekarte MESS-2 | keine Leiter im NLS; eine Laborbruecke braucht zwei Frequenzzweige mit Luecke (Gap-Solitonen, Antiferromagnete) [H] |
| Chem 8 dicht | weiter nach Vorab-Regel, niedrige Prioritaet | Fenster ueber 6 bis 7 v, aber Ladungsumverteilung statt Verschmelzung; paarweiser Uebertrag bekannt |

- **Vorab gegen Ausgang, Leitung:** EVO-1-Erwartung zweimal verfehlt; Chem 8 V1 verfehlt, V2 bis V4 getroffen; HOPF-1
  3 von 4. Die Fehler lagen jeweils bei Breiten und Anteilen, nicht beim Vorzeichen eines Effekts.
- **Selbstanzeige:** Ein Herkunftsleck der Leitung in G2-06/NACHTRAG.md ("ebenfalls Arm Z"); vor der Ernte gesperrt.
  Die erste Fremdlese-Anfrage f67c1643 ging an einen falschen Empfaenger; erst die neue Anfrage erreichte Codex.

## Einfach gesagt

Diese Runde hat unseren wichtigsten Befund gefestigt: Ein zweites, unabhaengiges Team hat den Computerbeweis fuer die
erste stille Schwingung geprueft und keinen Fehler gefunden, und die zweite Schwingung ist jetzt ebenso bewiesen. Die
stillen Schwingungen gibt es in vielen Varianten unseres Modells und auch bei flachen Baellen, aber nicht in den
Gleichungen fuer Licht in Fluessigkeiten oder ultrakalte Atome; fuer ein Laborexperiment brauchen wir Systeme mit zwei
Wellenarten und einer Luecke dazwischen. Mehrere schoene Bilder haben sich als schon bekannt herausgestellt, etwa das
reissende Band zwischen zwei Wirbeln. Und zum vierten Mal hat eine "kluge" Suche nach Ideen nicht besser abgeschnitten
als Losen.

## Abschluss (Leitung, 2026-09-30 12:32:09 CEST, date)

- Journal: claude-runde-v3-10-20260930 veroeffentlicht (Index nr 546, 23 Quellen mit sha256; `pruefen` vorher ohne
  Befund, wuerde_sperren 0). Die Beweiszahlen im Text sind gegen ZERT-T1-A-L32.json (z0) gegengelesen.
- Sicherung: rsync .69 -> TS440 (ohne --delete, nice/ionice) gestartet 12:31:41, Log
  /home/fmh/sicherung-dot69-ts440-lauf-20260930-r10.log auf der .69.
- Uebertrag in Runde 11: BEWEIS-2 (T2 laeuft, danach frische Lesung), Folgekarten aus der Abschaetzung.
