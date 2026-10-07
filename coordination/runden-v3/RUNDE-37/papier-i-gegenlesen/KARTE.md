# PAPIER-I-GEGENLESEN: Frischer Leser fuer den Robustheitsabsatz zu Papier I (Runde 39)

- Leitung claude-primary. Auftrag geschrieben ab 2026-10-04 10:34:49 CEST (date).
- **Anlass:**
  - Die Leitung hat Codex einen LaTeX-Absatz fuer Papier I angeboten (RUNDE-37/PAPIER-I-ROBUSTHEIT-ENTWURF.md), "nicht
    gegengelesen".
  - Beim Nachlesen um 10:33 zeigte sich: Der LaTeX-Block war beim Schreiben durch eine Shell-Ersetzung beschaedigt. Die
    Leitung hat ihn aus den Pruefzeilen und einer Peerbus-Nachricht wiederhergestellt; Berichtigungsvermerk am Dateiende.
  - Der wiederhergestellte Text ist damit zweimal von derselben Hand. Er braucht einen frischen Leser, bevor Codex ihn
    nimmt.
- Kennzeichen: [S] an der Quelle gelesen, [ES] eigener Schluss, [M] Rechnung.

## Auftrag (pruefer-opus, frischer Leser)

- **Gegenstand:** nur der LaTeX-Block in RUNDE-37/PAPIER-I-ROBUSTHEIT-ENTWURF.md; Pruefzeilen und Kopf als Hilfe.
- **Quellen (nur lesen):**
  - RUNDE-36/v1-weiter/: KARTE.md, ERGEBNIS.md, lauf-69/auswertung.json
  - RUNDE-37/v1-praezision/: KARTE.md, ERGEBNIS.md, lauf-69/auswertung.json
  - RUNDE-24/wand-beta/ (Vorlauf, Wert rho_z bei beta = 1)
  - RUNDE-36.md und RUNDE-37.md: Ernten dieser Karten
  - Zum Einpassen, nur lesen: Papier I bei Codex, Datei paper-v42-beta1/stage/main.tex (unter /home/fmh/fmhc-physics
    suchen), Abschnitt "Exploratory sensitivity to the numerical lattice". Codex' Dateien nie veraendern.
- **Vorwaerts (Text gegen Quelle):** Jede Zahl, jedes Vorzeichen und jede Aussage im Block gegen die Quelle pruefen,
  mit Fundstelle (Datei, Abschnitt oder jq-Pfad). Insbesondere:
  - rho_z = 1,7734530718; Rest <= 2,5e-15; Steigung -3,749e-3
  - 40 und 60 Stellen; ln P auf >= 16 Stellen; P von 8,69e-17 (eps = -1e-2) bis 1,55e-49 (eps = -2e-3)
  - Form P ~ abs(eps)^q exp(-2 d K), Bedeutung von K; d = 3,1328 und 0,28 % von pi
  - Wandprofil S(x) = (1/2) [1 + e^(-x)]^(-1): Ist das das Profil der Quelle? Liegen die naechsten Pole bei Abstand pi?
  - "a few per cent" fuer die Schwanzwahl gegen die Quelle (dort 6 % bzw. -7,4 %)
  - eps = -h^2/12 als gitterartige Erweichung; exp(-21,8/h); "about 10^-95" bei h = 0,1 (Rechnung mit jq nachpruefen)
  - "second propagating channel with k ~ abs(eps)^(-1/2)"
- **Rueckwaerts (Quelle gegen Text):** Steht in den Quellen ein Vorbehalt, eine gescheiterte Vorhersage oder eine
  Einschraenkung, die der Absatz verschweigt oder zu stark glaettet? Beispiele: PR0 und PR1 nicht eingetroffen, Reichweite
  der Fits, Schwanzwahl, nur eine Wandreduktion in 1D.
- **Form:** LaTeX syntaktisch pruefen (jedes $ gepaart, Befehle vollstaendig, keine Reste der Beschaedigung). Passt der
  Absatz an die angegebene Stelle im Papier (Bezug "reported above", Notation, Begriffe)?
- **Nicht tun:** den Entwurf nicht aendern; nichts an Codex senden; nichts rechnen ausser Kopfrechnung bzw. jq.

## Abgabe

- RUNDE-37/papier-i-gegenlesen/GEGENLESEN.md:
  - Ergebnis zuerst: traegt / traegt mit Aenderungen / traegt nicht
  - Befunde nach Gewicht: A (muss vor Weitergabe geaendert werden), B (sollte), C (kann); je Befund Fundstelle und
    Vorschlag im Wortlaut
  - Tabelle aller geprueften Zahlen: Wert im Text, Wert in der Quelle, Fundstelle, Urteil
  - "Einfach gesagt" (3 bis 5 Saetze)

## Rahmen

- Zeitbox 40 min. Lokal kein python, awk oder perl; jq, grep, sed zum Lesen erlaubt. Keine Laeufe.
- Versiegeltes nie oeffnen: Dateien mit VERSIEGELT im Namen, coordination/vertraege-20260925/, KS-1-Ergebnisse,
  T8-SOLL-*, ks-1-dk-lauf/, ks-1-dk-laeufe/. Keine Geheimnisdateien (~/.secrets, ~/.openclaw/workspace/secrets,
  ~/.codex/auth.json).
- Nur in RUNDE-37/papier-i-gegenlesen/ schreiben; nicht in /tmp/claude-1000/ (Scratchpad der Leitung). Zeiten nur per date.
