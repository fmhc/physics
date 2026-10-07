# Runde 25 (v3, explorativ, Nachtbetrieb)

Leitung: claude-primary. Angelegt: 2026-10-03 02:23:35 CEST (date). Runde 24 ist abgeschlossen (Journal nr 561).

## Lage

- Wartend auf Codex: blinde Nachrechnung der beta-1-Sprossen (angeboten 02:22).
- Wartend auf Finn: Papierschnitt, BLASE-EW-Weitergabe, Dashboard-Feed.
- Aktive Agenten: keine.

## Zufallskarte R25 (gezogen 02:23:35 mit `shuf -n 1` aus den Pool-Eintraegen "parken")

- {"id":"G2-10","titel":"(vom Operator)","ergebnis_kurz":"nein nach Kartenregel: 2D-Leiter auf dem Raster gesehen (fuenf Stellen 0,6536 bis 0,5401, d = 1 keine), Sprossenabstand in 1/eps 4,62 wie vorhergesagt; alle Lagen 0,0016 bis 0,0067 tiefer als vorhergesagt","testpfad":"GEN-02/G2-10/lauf-69-kopie (bic2_2d.py, .69 cpu/cpu2/cpu6)"}
- **Schreibtisch zur Zufallskarte G2-10:**
  - G2-10 fand in 1D keine stille Stelle (omega^2 0,55 bis 0,70, frueher 0,55 bis 0,88) und erklaerte das mit fehlender
    Innenbarriere.
  - Nach dem Mechanismus der ebenen Wand muesste es die 1D-Leiter geben, aber erst bei kleinem eps.
    - Das Plateau waechst nur logarithmisch, L ~ ln(1/eps)/sqrt2.
    - Die Sprossen liegen geometrisch dicht: Delta ln(1/eps) = sqrt2 pi/k_in = 2,31, also Faktor ~0,1 in eps.
  - G2-10 hat also wahrscheinlich nur nicht tief genug gesucht [H].
- **Entscheidung:** G2-10 wird als Test LEITER-1D wieder aufgenommen.
  - Karte RUNDE-25/leiter-1d/KARTE.md, 02:25:15; L1D-1 65 %, L1D-2 45 %, L1D-3 50 %.
  - Code-Agent gestartet, Zeitbox 120 min.
- Aktive Agenten (1 von 3): LEITER-1D.

### Ernte LEITER-1D (RUNDE-25/leiter-1d/ERGEBNIS.md; eingetragen 2026-10-03 03:02:44 CEST)

- Agent, Plan eingefroren 02:50:22.
- **L1D-1 bis L1D-3 eingetroffen**, gegengelesen an lauf-69/auswertung.json (alle true).
- Fuenf stille Stellen in 1D, beide Gitter (h = 0,02 und 0,01), Vorzeichenwechsel und aufgeloester Umlauf:
  - eps = 6,0e-3 (gerade), 8,8e-4 (ungerade), 8,0e-5 (gerade), 8,1e-6 (ungerade) und 8,1e-7 (gerade)
  - Die Paritaet wechselt; je Paritaet wechselt auch der Umlauf.
- Schritte in ln(1/eps): 1,916 / 2,395 / 2,289 / 2,314. Die letzten zwei liegen -0,90 % und +0,18 % neben
  sqrt2 pi/k_in = 2,3100.
- rho_n - rho_z: -0,045 / +0,0070 / -0,0018 / +0,00028 / -0,000057. Die Werte naehern sich abwechselnd von unten und oben
  und laufen gegen die ebene Wandnullstelle.
- Kontrollen:
  - Profil exakt aus der ersten Integralform.
  - Die ebene Wand mit demselben Verfahren trifft WAND-BETA auf 3e-11.
  - Gitter, Verfahren und Gebiet stimmen auf <= 3e-7.
  - G2-10 reproduziert (keine Stelle bei omega^2 0,55 bis 0,70); die Leiter beginnt erst bei eps = 6e-3.
- **Einschraenkung des Agenten** [H, nachtraeglich]:
  - Nach dem eigenen Barrierekriterium von G2-10 hat der 1D-Ball fuer eps < 0,017 (ungerade) bzw. 0,042 (gerade) eine
    Innenbarriere; an allen fuenf Sprossen ist sie vorhanden (B = 0,42 bis 0,83).
  - Widerlegt ist damit "in 1D fehlt die Barriere", nicht gezeigt ist "die Barriere ist unnoetig".
  - Die Bedeutungszeile der Karte war hier zu stark. Belastbar ist: **Die Leiter braucht keine Kruemmung.**
- **Selbstanzeige der Leitung:** Im Auftrag stand "groesste Wurzel" fuer den Umkehrpunkt. Richtig ist die kleinere,
  S0 = 1 - sqrt(2 eps); der Agent hat das berichtigt. Das Suchfenster hat er offen auf [1,30; 1,70] erweitert.
- **Lesart [H]:**
  - Der Mechanismus "ebene Wandnullstelle plus Fabry-Perot" erklaert die Leiter in d = 1, 2, 3 mit einer einzigen
    Wandgroesse.
  - In 3D ist der Schritt in 1/eps 2 sqrt(beta) pi/k_in. In 1D ist er in ln(1/eps) gleich lambda pi/k_in mit lambda = sqrt2;
    bei beta = 1/2 stimmen beide Zahlen ueberein (2,3100).
- **Abschaetzung: weiter.**
  - Papierrelevant: Die stille Leiter ist kein Kruemmungseffekt.
  - Codex informieren; vor einer Papierzeile eine blinde Nachrechnung einer 1D-Sprosse anbieten.

### Codex-Ernte und Selbstanzeige zur Verblindung (eingetragen 2026-10-03 03:05:48 CEST)

- **Papier I v0.42** ist als projektinterne Arbeitsfassung angenommen: 52 Seiten, die beta-1-Wandpassage steht auf Seite
  11, alle QA-Tore haben gehalten. Weder eine radiale beta-1-Replikation noch ein Grenzwertsatz ist behauptet.
- **Blindheit der beta-1-Sprossen-Nachrechnung nicht gegeben** (Codex 7ae5975f, 02:28):
  - Mein Angebot nannte "8 Sprossen, Schritte 2,54 bis 2,60".
  - Ausserdem zeigten die Prozess-Argumente des LEITER-BETA-Agenten auf der .69 Kandidaten-rho0, sichtbar bei einer
    Kapazitaetsinventur.
  - Codex fuehrt eine Nachrechnung deshalb nur noch als "unabhaengig, nicht vollstaendig blind". Ihre Selbstverpflichtung:
    In Inventuren zeigen sie nur PIDs, CPU, Status und Lockbesitz.
- **Selbstanzeige der Leitung:** Das Blind-Angebot enthielt Ergebniszahlen. Lehre in der neuen Memory
  feedback-blind-angebot-ohne-zahlen: nur Fenster nennen, Zielwerte per Datei statt Befehlszeile. Das 1D-Angebot
  (508bbc38) nennt nur Fenster, die Lagen nicht.
- Peerbus-Altbestand (unquittierte Meldungen seit 01.10.) quittiert; nichts Ungelesenes von Codex offen.

## Abschluss Runde 25 (Leitung, 2026-10-03 03:05:48 CEST)

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| Zufallskarte G2-10, als LEITER-1D | L1D-1 bis L1D-3 eingetroffen: fuenf 1D-Sprossen bei eps 6e-3 bis 8e-7, Schritt ln(1/eps) -> 2,31, rho_n -> rho_z | erledigt im Pool; weiter als Papierbaustein ("Leiter braucht keine Kruemmung"), Codex-Nachrechnung angeboten (nur Fenster) |

### Einfach gesagt (Runde 25)

Bisher dachten wir, dass es die stillen Schwingungen eines Q-Balls in einer Dimension nicht gibt. Sie verstecken sich aber
nur: ganz nah an der Grenze, wo der Ball sehr lang wird, liegen sie wie Sprossen einer Leiter, jede etwa zehnmal naeher an
der Grenze als die vorige. Den Abstand konnten wir vorher allein aus der Wand des Balls ausrechnen, und er stimmt auf 0,2
Prozent. Damit wissen wir: Fuer die Stille braucht der Ball keine runde, gekruemmte Form.

- Journal: nr 562 (claude-runde-v3-25-20261003), pruefen ohne Befund; Sicherung .69 -> TS440 gestartet (Log ...-20261003-r25.log). Runde 25 geschlossen 2026-10-03 03:06:06 CEST.
