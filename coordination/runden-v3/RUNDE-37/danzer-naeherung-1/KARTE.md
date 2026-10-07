# DANZER-NAEHERUNG-1: Faellt die kubische Richtungsabhaengigkeit von Licht und Skalar auf ikosaedrischen Naeherungsnetzen mit der Naeherungsordnung, wie die Symmetrie es verlangt? (Runde 46, Finns Weiche Kristall/Glas/Quasikristall)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 06:46:15 CEST (date), vor jeder Rechnung.
- **Finn (05.10., vor 05:50:21):** "Meine Tetraeder können zufällig und unregelmäßig sein." Damit sind ikosaedrische Netze aus unregelmaessigen Tetraedern zugelassen.
- **Herkunft:** Kartenvorschlag aus DANZER-L (RUNDE-37/danzer-l/DOSSIER.md, Abschnitt 6), frisch gegengelesen (GEGENLESEN-R45, Teil C). Frage, Messgroessen, Vorhersagen N1 bis N3 und Ableitbarkeitsprobe sind **woertlich bindend**; die Wahrscheinlichkeiten setzt die Leitung. Zusaetze der Leitung sind markiert.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Rechnung (woertlich, dazu Zusatz)

- **Woertlich:**
  - Kubische rationale Naeherungen 1/1, 2/1 und 3/2 der Danzer-Pflasterung (Schnitt aus D6 mit tau -> F_(n+1)/F_n, Bauplan nach Al-Siyabi u. a.).
  - Falls das in der Zeit nicht geht: die Ammann-Kramer-Pflasterung aus Z^6 mit einer vorab festgelegten symmetrischen Zerlegung der Rhomboeder in Tetraeder.
  - Darauf Skalar (Graph-Laplace) und Maxwell in der Coulomb-Phase mit dem Bloch-Werkzeug aus LICHT-FINN-NETZ-1.
- **[Zusatz Leitung, Bauweg]:** Erlaubt ist auch der einfachste Weg: Schnitt- und Projektionsmenge aus Z^6 (Fenster: rhombisches Triakontaeder) mit tau -> F_(n+1)/F_n, kubisch periodisch, dann periodische Delaunay-Tetraederzerlegung der Eckenmenge. Entartungen bricht eine vorab festgelegte, kleine und ueber Saaten gemittelte Stoerung auf. Die Wahl steht im Plan vor der Rechnung.
- **[Zusatz Leitung, Hodge]:** Aus HODGE-L: Positive Hodge-Sterne verlangen in 3D Delaunay (Hirani u. a. 2013).
  - Maxwell hier mit Einheitsgewichten (topologisch); die Geometrie geht ueber die Bloch-Phasen ein.
  - Zusaetzlich beschreibend die Vorzeichen von *1 und *2 auf den Naeherungen.

## Messgroessen (woertlich)

- Spanne des Grundtempos
- l = 4-Anteil von a2 (Koeffizient von S4) und l = 6-Anteil, je Naeherungsordnung

## Vorhersagen (woertlich; vorab)

| Nr | Vorhersage | Wahrsch. (Leitung) |
|---|---|---|
| N1 | Das Grundtempo ist auf jeder Naeherung isotrop (Stufe 2, kubisch genuegt). Vorab ableitbar, nur Kontrolle | 90 % |
| N2 | [H] Der l = 4-Anteil von a2 faellt mit der Ordnung ungefaehr wie die Phason-Verzerrung ~ 1/F_n^2. Er kann scheitern: Bleibt er ueber 1/1 -> 3/2 hoeher als ein Drittel seines Startwerts, dominiert die lokale Bauweise, nicht die Symmetrie | 50 % |
| N3 | [H] Der l = 6-Anteil bleibt endlich und naehert sich einem Grenzwert | 55 % |

## Ableitbarkeitsprobe (woertlich)

- N1 ist ableitbar.
- Bei N2 ist nur die Richtung ableitbar (lineare Kopplung der G-Verzerrung an l = 4); die Zahlen und Vorfaktoren nicht.
- N3 ist nicht ableitbar.
- Projekt-grep (04:29): keine Danzer-, Naeherungs- oder Phason-Rechnung im Projekt.
- Grenze: Die TT-Moden und die Phasonen prueft diese Karte nicht; dafuer braeuchte es die Regge-Maschine aus TT-ISO-1 auf der Naeherung, eine Stufe spaeter.

**Bedeutung (vorab):**
- **N2 trifft ein:** Die Symmetrie setzt sich auf dem Weg zum Quasikristall durch. Die kubische Restanisotropie verschwindet mit der Ordnung; der ikosaedrische Zweig von Finns Weiche ist numerisch gestuetzt.
- **N2 verfehlt:** Die lokale Bauweise (Zerlegung, Delaunay) dominiert. Die Gruppenaussage allein traegt dann nicht.

## Rahmen

- Code-Agent; Bloch-Werkzeug aus licht-finn-netz-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4, sobald UMKLAPP-1 sie freigibt, sonst cpu5. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256). Hauptaufwand ist der Bau.
- Ein ehrlicher Teilbericht ist besser als keiner: zuerst 1/1 und 2/1.
