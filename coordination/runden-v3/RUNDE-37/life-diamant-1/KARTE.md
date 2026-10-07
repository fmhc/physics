# LIFE-DIAMANT-1: Gibt es "Game of Life"-Gleiter auf Finns Diamantnetz? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 07:04:39 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn, 04.10.: "... Ansätzen von Game of Life oder simpligizierungen".
  - Pool H13 LIFE-DIAMANT; STRATEGIE-SPIN-20261004.md, Weg 4.
  - Projektsuche: keine Vorarbeit zu Zellautomaten. Die grep-Treffer auf "gleiter" waren "Begleiter".
- **Frage:** Entstehen auf Finns Netz (Diamantgitter, vier Striche je Knoten) aus einer einfachen, ueberall gleichen
  Ja/Nein-Regel bewegte Muster ("Teilchen")?
  - Wie schnell sind sie gegen die Grenzgeschwindigkeit des Netzes (ein Strich je Schritt)?
  - Wie verhalten sie sich unter den Drehungen des Tetraeders?
- **Schreibtisch [M]:**
  - Jede Zelle hat 4 Nachbarn. Eine aussen-totalistische Regel ist durch die Geburtsmenge B und die Ueberlebensmenge S
    (Teilmengen von {0..4}) festgelegt.
    - Ohne 0 in B (sonst entsteht aus dem Nichts sofort Leben) sind das 16 x 32 = 512 Regeln. Die lassen sich
      vollstaendig durchsuchen.
  - Grenzgeschwindigkeit c = ein Strich je Schritt, also sqrt(3)/4 Zellkanten je Schritt.
  - Klassische Muster tragen kein Vorzeichen -1, also keinen echten Spin. Gefragt sind emergente Teilchen und ihr
    Lichtkegel, kein Spin.
  - Bei Conways Leben auf dem Quadratgitter sind die schnellsten endlichen Raumschiffe c/2 (orthogonal) bzw. c/4
    (diagonal) schnell [L].
  - Bei Bipartitheit kann ein Muster aus nur einem Untergitter nach einem Schritt nur auf dem anderen liegen. Das kann
    die moeglichen Perioden beschraenken [M].
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Test (Code-Agent)

- **Gitter:** Diamantgitter, periodischer Kasten aus L^3 kubischen Zellen (8 Knoten je Zelle).
  - Pruefen: jeder Knoten mit genau 4 Nachbarn, bipartit.
- **Regeln:** alle 512 (B ohne 0, S beliebig).
- **Startmuster:** Zufallsmuster in einem kleinen Bereich (z. B. 2x2x2 Zellen), mehrere Dichten, viele Saaten je Regel.
  Saaten parallel in einer Stapel-Dimension rechnen.
- **Verlauf:** bis T Schritte oder Abbruch. Einordnung:
  - ausgestorben
  - Stilleben bzw. Oszillator (Wiederkehr ohne Verschiebung)
  - Gleiter (Wiederkehr der Form mit Verschiebung, endliche Ausdehnung)
  - Wachstum bzw. Chaos (ueber eine Groessenschranke)
  - Formvergleich ueber eine verschiebungsfreie Kennung (kanonische Lage).
- **Fuer jeden Gleiter:** Periode, Verschiebung, Geschwindigkeit in c, Richtung (Tetraederrichtung oder andere), Groesse.
  - Wirkung der Tetraederdrehungen: Ist das gedrehte Muster derselbe Gleiter in anderer Phase oder Richtung?
  - Beschreibend: Gibt es Gleiter, bei denen eine Drehung um die Laufachse einer halben Periode entspricht?

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LD0 | Kontrolle: Gitter korrekt (4 Nachbarn, bipartit); B leer und S = {0..4} haelt jedes Muster fest; die Einordnung erkennt eingesetzte Kunstmuster (verschobene Kopie) richtig | 90 % |
| LD1 | [H] Mindestens eine der 512 Regeln hat einen Gleiter, der aus Zufallsstarts entsteht | 50 % |
| LD2 | [H] Falls Gleiter gefunden werden: alle sind hoechstens halb so schnell wie die Grenzgeschwindigkeit (v <= c/2) | 70 % |
| LD3 | [H] Falls Gleiter gefunden werden: Die schnellsten laufen laengs einer Tetraeder-Strichrichtung oder ihrer Gegenrichtung | 45 % |

**Bedeutung (vorab):**
- **LD1 trifft ein:** Finns Netz traegt aus einer einfachen Ja/Nein-Regel bewegte "Teilchen" mit einer
  Hoechstgeschwindigkeit. Das ist das Game-of-Life-Bild emergenter Teilchen auf dem Tetraedernetz.
  - Klassisch, ohne Spin. Der Quanten-Zellautomat (QCA-TETRA-1, QCA-DIAMANT-4) ist das Gegenstueck mit Spin.
- **LD1 verfehlt:** Mit vier Nachbarn je Knoten sind einfache Regeln zu arm fuer Gleiter. Dann braucht es mehr Nachbarn
  (etwa die 12 der fcc-Schale) oder mehr Zustaende.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu7; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
