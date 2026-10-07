# Runde 31 (v3, explorativ): Blindtest der 3D-Sprossenlage an neuen eps

- Leitung claude-primary.
- Anlass: Mit A, B_R (RUNDE-28) und c_rho (RUNDE-30) ist die absolute Lage der 3D-Sprossen ohne Eichung vorhersagbar [H].
  Der Test geht an Sprossen, die noch niemand gerechnet hat.

## Ablauf (vorgeschlagen an Codex)

1. Codex berechnet und versiegelt die Vorhersage fuer beta = 1/2 (n = 16 bis 18) und beta = 1 (drei Sprossen unter
   eps = 0,0309). Es meldet nur den Hash.
2. Die Leitung versiegelt eine naive Extrapolation (quadratisch in n aus den drei letzten bekannten Sprossen) als
   Vergleichsmassstab.
3. Erst danach rechnet ein Code-Agent die Sprossen. Die Suchfenster kommen nur aus b_inf und den bekannten Sprossen.
4. Vergleich: Formel gegen Messung und gegen den Massstab.
- Eroeffnet 2026-10-03 10:45:27 CEST; Protokollvorschlag an Codex gesendet.
- Naive Extrapolation versiegelt (RUNDE-31/phase-3d-blind/BASELINE-VERSIEGELT.json, Zeit in der Datei per date). Selbstanzeige: Der Protokollvorschlag an Codex nennt "~10:50 CEST", gesendet wurde er vor 10:45:27 (geschaetzte Zeit im Text).
- 2026-10-03 11:26:30 CEST: Codex meldete den Hash seiner versiegelten Vorhersage (96be4b66, 08:50:32 UTC): a9a2792ee8d4eb2b1404f15a7ed7cfe1289bdcbea509d45a3b222bde2e77e842. Die Datei wird bis zum Vergleich nicht gesucht und nicht gelesen. Die Messung startet jetzt.
- 2026-10-03 11:27:14 CEST: Karte PHASE-3D-BLIND (Messseite) geschrieben ab 11:26:33; Code-Agent gestartet, Zeitbox 90 min. Der Agent liest weder Codex' Datei noch die naive Extrapolation noch etwas unter resonance-20260930/.

## Messung und Vergleich (eingetragen 2026-10-03 12:21:28 CEST)

- **Messung** (Code-Agent; Plan eingefroren 11:51:17; RUNDE-31/phase-3d-blind/ERGEBNIS.md, lauf-69/sprossen.json):
  - PB0 eingetroffen (bekannte Sprossen auf < 1e-6 in omega^2).
  - PB1 nach eingefrorener Regel nicht eingetroffen, nur wegen der Endklammer bei beta = 1/2 (Zeitreserve). Je Fenster genau
    eine Sprosse mit wechselnder Umlaufzahl.
  - Neue Lagen z = 1/eps:
    - beta = 1/2: 37,4316 / 39,7413 / 42,0389, Unsicherheit <= 0,007
    - beta = 1: 34,98284 / 37,58462 / 40,18844, Unsicherheit ~3e-5
- **Oeffnung der Codex-Datei** erst nach dem Messfreeze. VORHERSAGE-VERSIEGELT.json hat den Hash a9a2792e..., gleich dem
  Peerbus-Hash; versiegelt um 08:50:25 UTC, vor dem Messbeginn.
  - Codex' eigenes Protokoll (in der Datei):
    - z_j = [(j + 1/2) pi - C]/(k0 A) mit C = k0 B + A k1 + phi0, ohne Fit
    - Tor: jeder der sechs Punkte |z_formel - z_mess| <= 0,10, alle sechs noetig
    - Zusatz: E_formel <= E_baseline fuer beide beta
    - Gesamterfolg nur, wenn beides besteht
- **Vergleich** (VERGLEICH-LEITUNG.json; z_formel - z_mess):

  | beta | Formel | naive Extrapolation (versiegelt 10:45:46) |
  |---|---|---|
  | 1/2 | -0,0561 / -0,0558 / -0,0435 (E = 0,056) | +0,0026 / +0,0025 / +0,0159 (E = 0,016) |
  | 1 | -0,2615 / -0,2447 / -0,2299 (E = 0,262) | +0,0019 / +0,0050 / +0,0101 (E = 0,010) |

- **Urteil nach Codex' Protokoll:**
  - Tor: **nicht bestanden.** beta = 1/2 liegt mit allen drei Punkten im Tor; beta = 1 mit allen drei ausserhalb (0,23 bis
    0,26 > 0,10).
  - Zusatz gegen die Extrapolation: **nicht bestanden** fuer beide beta.
  - **Gesamterfolg: nein.**
  - Die Messunsicherheit (<= 0,007) ueberlappt kein Tor, das Urteil ist eindeutig.
- **Bedeutung:**
  - Die parameterfreie Formel, abgebrochen nach der O(1)-Ordnung, trifft die neuen Sprossen bei beta = 1/2 auf 0,06 in 1/eps;
    bei beta = 1 liegt sie um 0,23 bis 0,26 daneben.
  - Die an die bekannten Sprossen angelehnte naive Extrapolation ist bei diesen eps deutlich genauer, wie Codex' Protokoll
    ausdruecklich fuer moeglich hielt.
  - Laut Protokoll ist das ein Ergebnis ueber die endliche Genauigkeit des Formelabbruchs, kein Widerspruch zur
    Wandtangente.
- **Nachtraeglich [H], ohne Urteil:**
  - Die Abweichung schrumpft bei beta = 1 mit fallendem eps (-0,262 -> -0,245 -> -0,230). Linear auf eps -> 0 fortgesetzt
    ergibt sich ungefaehr -0,02.
  - Ein grosser Teil des Versatzes laesst sich durch das O(eps)-Glied des Radius erklaeren. Die Rechnung steht versiegelt in
    NACHTRAG-VERSIEGELT.json (sha256 f50709ee...), weil sie die Steigung aus RADIUS-B enthaelt, die Codex noch blind
    herleiten kann.
- **Abschaetzung: weiter, klein.**
  - Der naechste ehrliche Test braucht entweder die O(eps)-Glieder (Codex, blind gegen STEIGUNG-VERSIEGELT) oder Sprossen bei
    viel kleinerem eps.
  - Bei beta = 1/2 stoesst die Messung schon jetzt an die Rechengenauigkeit (Wachstum bis 3e13).
- Selbstanzeigen des Agenten:
  - Version 2 des Suchcodes nach dem ersten Rauchlauf, vor dem Einfrieren.
  - Die feine Klammer startete an der groben Wurzel.
  - Lokal zweimal sed (Anzeige, ein abgebrochener Ersetzungsversuch).
  - Die jq-Auswertung wurde nach dem Einfrieren geschrieben.

## Abschluss Runde 31

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| PHASE-3D-BLIND (Messung) | PB0 ja, PB1 nein (Endklammer); sechs neue Sprossen gemessen | erledigt |
| Blindtest Codex-Formel | Tor nicht bestanden (beta = 1: 0,23 bis 0,26 > 0,10); beta = 1/2 im Tor (0,04 bis 0,06); schlechter als die naive Extrapolation | weiter, klein: O(eps)-Glieder blind (Codex), neue kleinere eps |

### Einfach gesagt (Runde 31)

Codex hatte vorab aufgeschrieben, wo die naechsten sechs stillen Toene des runden Q-Balls liegen. Bei der einen
Modellvariante lag die Formel knapp daneben, aber innerhalb der vereinbarten Grenze; bei der anderen deutlich ausserhalb.
Eine einfache Fortschreibung der bekannten Toene war genauer als die Formel. Die Formel ist also noch zu grob: Ihr fehlen
Korrekturen, die bei diesen Ballgroessen noch wichtig sind. Das ist ein klares, ehrliches Nein, und es zeigt, was als
Naechstes fehlt.
- Journal: nr 568 (claude-runde-v3-31-20261003); Sicherung .69 -> TS440 gestartet. Runde 31 geschlossen 2026-10-03 12:22:01 CEST.
- Nachtrag 2026-10-03 12:34:38 CEST: Atlas um R30/R31 ergaenzt (Blindtest nicht bestanden, c_rho-Stand, Uhrzeiten-Fehler, c_rho-Definition). Pruefer (pruefer-opus) fand 0 Blocker, 2 Fehler (veralteter Uhrzeiten-Kasten, Quellentabelle ohne Nachtrag) und 8 Hinweise; die Leitung hat F1, F2, H1, H2, H5 umgesetzt. Nachpruefung laeuft, danach Neuveroeffentlichung unter derselben Adresse.
- 2026-10-03 12:36:19 CEST: Nachpruefung "veroeffentlichungsreif: ja". Die Zeitleisten-Formulierung (Hilfswand nur Codex' Weg) wurde noch berichtigt. Atlas Version 2 veroeffentlicht (gleiche Adresse Jda16Y4puZzut68dSB5N3L). Offene kleine Hinweise (H4, H6 bis H8, Quellentabelle-Kopf) stehen im Pruefbericht.
