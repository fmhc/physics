Urteil: einfuegen nach genannten Aenderungen (N10, N12 erfuellt; N11 erfuellt, neu N14 (R); N9 teilweise, neu N13 (A); Empfehlungen E13-E16; Zitate 8 von 8 woertlich)

# Lesung letzte Schicht V4 (Nachtrag spin2-d4, Stellen N9 bis N12)

- Leser: pruefer-opus (Haus Anthropic), frischer Leser
- Auftrag: Kurzauftrag der Leitung claude-primary (eine BRIEF-Datei mit Pfad und sha256 wurde nicht genannt; der Kurzauftrag gilt als Auftrag)
- Beginn (date): 2026-10-01 21:48:03 CEST
- Material: NACHTRAG-ENTWURF-V4.md gegen NACHTRAG-ENTWURF-V3.md (diff), Anforderungen LESUNG-LETZTE-SCHICHT-V3.md Abschnitt 5 (N9 bis N12)
- Nicht geoeffnet: Ordner codex-lesung (paralleler Pruefer), gesperrte Pfade

## 0. Gefundene Aenderungen (diff V3 -> V4)

Der diff zeigt fuenf Bloecke, nicht vier:

| V3 | V4 | Bezug |
|---|---|---|
| Z. 16-17 | Z. 16-17 | N12 |
| Z. 46-47 | Z. 46-52 | N11 |
| Z. 56-57 | Z. 61-62 | N10 |
| Z. 79 | Z. 84 | nicht angekuendigt; Folgeaenderung zu N11 ("Regge-Beschraenktheit" aus der Folgezeile entfernt), geprueft in Abschnitt 2 |
| Z. 86-88 | Z. 91-100 | N9, darin auch N10 ("(S. 2, oben)" -> "(S. 2)") |

Alle uebrigen Zeilen sind gleich (diff ohne weitere Bloecke).

## 1. Stelle N12: Satz zum Nachtrag vom 24.09.

- **Anforderung erfuellt.** WARUM-SPIN-2.md Z. 539: "... (Maenaut et al., arXiv:2411.17893: `ell` unter etwa 35 km, 95 %)
  gelten nur ohne diese UV-Annahme und sagen dann nichts ueber Spin >= 3." Die Zeichenfolge "gelten nur ohne diese
  UV-Annahme" steht dort woertlich.
- Abgrenzung: Z. 534 ist der Kopf des 24.09.-Nachtrags, Z. 543 der Kopf des 27.09.-Nachtrags; Z. 534-542 ist also genau
  der 24.09.-Nachtrag. CEMZ-Satz, EGHS-Satz, Zuordnungssatz und Ringdown-Satz stehen alle im Spiegelstrich "Zu Glied 7,
  massive Fassung, und Glied 10" (Z. 539). "Derselbe Absatz" stimmt.
- Richtung: Subjekt "Ringdown-Grenzen", Aussage "gelten nur ohne diese UV-Annahme", wie im Original. Zweiter Teil: Original
  "Die Zuordnung dieser Laborschranke zum Turm ist eine Einordnung des Feldforschers, keine Messung am Turm". Die Wiedergabe
  "nennt die Zuordnung ... eine Einordnung des Feldforschers" stimmt. Nichts vertauscht.
- Neue Ueberziehung: nur eine kleine. Im Original steht "Ringdown-Grenzen **auf kubische Korrekturen**". V4 kuerzt das
  Subjekt ausserhalb der Anfuehrungszeichen zu "Ringdown-Grenzen". Damit ist das Subjekt breiter als im Original. Fuer den
  Zweck des Satzes (der Absatz enthaelt selbst einen Hinweis auf eine Bedingung) hat das keine Folge. Siehe E13.

## 2. Stelle N11: Block "Zum UV-Verhalten der Amplitude"

- **Anforderung erfuellt.** Die Form bei CHLPSD steht da: verschmierte Amplituden, nicht (2.20). Die Einordnung als
  zusaetzliche Voraussetzung wird Bucciotti zugeschrieben.
- Seiten: 2201.06602.txt Z. 477-541. Die Fusszeile "-8-" folgt nach Z. 500, also steht (2.20) (Z. 483) auf S. 8. (2.22)
  (Z. 528), (2.23) (Z. 536) und der Schlusssatz (Z. 538-541) stehen auf S. 9. Stimmt.
- Zitate: "(not what we'll assume)" steht in Z. 483 (dort typografischer Apostroph). "conservative assumptions directly
  traceable to causality and unitarity" steht woertlich in Z. 540-541. Bucciotti (RUNDE-11/cemz-mess/quellen/2605.00089.txt):
  Die Fusszeile "- 21 -" steht vor der Stelle, also S. 22. Dort steht: "The S-matrix approach ... On the other hand, it
  requires assumptions about the UV behaviour of the amplitude, in particular Regge boundedness". Das stimmt.
  "zusaetzliche" steht nicht in der Quelle. Dort ist es eine Gegenueberstellung zum geometrischen Weg ("On the other hand").
  Ohne Anfuehrungszeichen ist das als Einordnung vertretbar.
- "uebliche Regge-Schranke bei festem t": Die Quelle sagt "Typically one assumes a Froissart-Martin-like bound at fixed
  momentum transfer" (Z. 480-481), und zwar im Abschnitt "Regge boundedness and all that". Das ist gedeckt.
- "nennen das": Die Quelle sagt "We believe that these are conservative assumptions ...". Mit "nennen" faellt das "We
  believe" weg, die Einschaetzung der Autoren wirkt dadurch etwas fester. Siehe E14.
- **Richtung, neue Gefahr (N14, R):** Z. 47 ("stuetzen sich nicht auf die uebliche Regge-Schranke") und Z. 51-52 ("...
  insbesondere Regge-Beschraenktheit ... nicht die der Autoren") lassen sich zusammen so lesen, als setzten CHLPSD gar keine
  Regge-Beschraenktheit voraus. Die Quelle sagt etwas anderes:
  - S. 2, Z. 120-123: "We will use asymptotic causality, but crucially, imposed at all energy scales ... This leads to sharp
    mathematical statements involving crossing symmetry, analyticity, and Regge boundedness of scattering amplitudes [10]."
  - S. 10, Fn. 7: "The bound (2.23) amounts to J0 <= 1 but all we ultimately use in this paper is J0 < 2."
  - S. 11, Z. 621: "the Regge growth (2.23)".
  - Die Autoren setzen also selbst eine verschmierte Regge-Schranke voraus und nennen sie so. Sie fuehren sie auf
    Kausalitaet bei allen Energien zurueck. Abweichend von Bucciotti sind nur zwei Dinge: die Einordnung (Folge der
    Kausalitaet, keine Zusatzannahme) und die Form (verschmiert statt bei festem t).
  - Woertlich ist Z. 51-52 durch das Wort "zusaetzliche" richtig, und Z. 44-45 sowie Z. 49-50 fangen die Fehllesung teilweise
    ab. Der Block ist aber gerade die Genauigkeitsstelle zu N11, die Gegenlesart liegt nahe. Anforderung siehe Abschnitt 5.
- Folgeaenderung Z. 84 (V3 Z. 79): Sie passt zu N11 und bringt keine Ueberziehung. Ein Lesefehler ist moeglich: "der Annahmen
  zum UV-Verhalten der Amplitude und der schwachen Kopplung" kann man als "UV-Verhalten ... der schwachen Kopplung" lesen.
  Siehe E16.

## 3. Stelle N10: Satz "Schranken fuer die Kopplung ... bleiben offen"

- **Anforderung erfuellt.**
  - (a) "(S. 2, oben)" ist gestrichen. Z. 100 nennt jetzt "(S. 2)", Z. 61-62 ebenfalls S. 2. Die Angaben sind eindeutig.
  - (b) Die Wiedergabe ist auf das Begrenzen beschraenkt: Z. 61 "Schranken fuer die Kopplung ... bleiben offen", Z. 100
    "Schranken ... bleiben bei ihnen ausdruecklich offen".
- Zitat und Seite: 2201.06602.txt Z. 144-145 lautet "The task of bounding their couplings to Standard Model fields is left to
  future work." Das ist woertlich. Die Stelle liegt auf PDF-Seite 4, Z. 117-162, das ist die gedruckte S. 2.
- Richtung: "their" bezieht sich auf "new states" (Z. 143-144: "we constrain the mass M of new states and their couplings to
  gravitons"). Das ist richtig wiedergegeben.
- Neue Ueberziehung: keine. In Z. 61 fehlt "bei ihnen". Der Satz steht aber unter dem CHLPSD-Spiegelstrich, der Kontext
  reicht. "ausdruecklich" in Z. 100 ist durch den eigenen Satz der Autoren gedeckt.

## 4. Stelle N9: alpha-~-1-Block

- **Anforderung nur teilweise erfuellt.**
  - Teil (b) ist erfuellt: CHLPSD Abschn. 4.5 ist genannt und verschwindet nicht hinter "ausdruecklich offen".
  - Teil (a) ist zur Haelfte erfuellt: Der Gegenstand ist jetzt genau benannt ("behauptet eine Yukawa-Kraft mit alpha ~ 1"),
    und die Titel- und Abstract-Eintraege sind als ungeprueft markiert (Z. 94). Bei der Kreisangabe ist dagegen ein neuer
    Fehler entstanden (N13).
- **N13 (A), Kreis schliesst EGHS aus:**
  - Z. 91 legt den Kreis fest als "(Volltexte in quellen/ von SPIN2-D4)". quellen/SHA256SUMS.txt fuehrt genau fuenf
    Volltexte: 2201.06602, 2202.08280, 2501.17949v2, 2501.18465 und 2512.13780v2. Dazu kommen nur Such-XML und -JSON.
  - EGHS (1704.01590) gehoert nicht dazu. Der Volltext liegt in RUNDE-11/cemz-mess/quellen/1704.01590.txt.
  - Der Satz nennt als einzigen Behaupter also eine Arbeit ausserhalb des Kreises, den er selbst setzt. Woertlich genommen ist
    er damit falsch: Im genannten Kreis behauptet niemand alpha ~ 1, CHLPSD nur heuristisch und ohne Staerke.
  - Zugleich faellt eine Gruppe aus beiden Angaben heraus: Arbeiten, die an der Quelle gelesen wurden, aber ausserhalb von
    quellen/ liegen, z. B. Bucciotti (RUNDE-11) und CEMZ (Fundort nicht geprueft). Beide zitiert der Nachtrag selbst. Sie
    stehen weder in "an der Quelle gelesen (quellen/)" noch in Z. 94 ("nur ueber Titel oder Abstract"). Fuer sie ist offen, ob
    die "nur"-Aussage gilt.
  - Hinweis ohne Volllesen: Eine Wortsuche nach "yukawa|fifth force" in Bucciotti ergab 0 Treffer. CEMZ habe ich nicht
    geprueft.
- Zitate in Z. 91-100, alle woertlich:
  - "parametrically equal to gravitational": 1704.01590.txt Z. 753, danach die Fusszeile "- 13 -", also S. 13. Damit ist der
    offene Punkt der V3-Lesung (S. 13 nicht pruefbar) jetzt an der Quelle bestaetigt.
    - Umfeld: "these new particles would mediate a new force between all Standard Model particles ... The range of such a
      force will be of order r ~ c3^(1/4)/Lambda and the strength will be parametrically equal to gravitational".
    - "Yukawa-Kraft mit alpha ~ 1" ist als Wiedergabe zulaessig: Reichweite plus Staerke.
  - "Can higher-spin states be hidden from the Standard Model?": Inhaltsverzeichnis Z. 54, S. 33.
  - "less rigorous": Z. 1860, S. 33.
  - "because gravity is universal and couples to all matter": Z. 1866, S. 33.
- Richtung der Wiedergabe in Z. 97-98:
  - Die Quelle sagt: "What do collider searches tell us about higher spin particles, of the kind that can lead to
    modifications of GR? Heuristically, because gravity is universal and couples to all matter, one might expect that
    modifications to it also couple to everything."
  - Grammatisches Subjekt der Quelle ist "modifications to it". Es ist an die Hoeherspin-Teilchen des Vorsatzes gebunden.
    "solche Zustaende" ist also vertretbar.
  - Das Objekt heisst in der Quelle "everything". V4 schreibt "alle Materie", das ist aus der Praemisse uebernommen.
  - Keine Umkehr. "duerften" passt zu "one might expect".
- "Eine Staerke alpha ~ 1 leiten sie nicht ab" haelt.
  - S. 35, Z. 1993-1995: "new higher-spin states could be exchanged between Standard Model fields and the higher-spin
    particle. But these could then be produced directly with a four-derivative graviton-strength coupling".
  - Das betrifft die Erzeugung ueber eine Vier-Ableitungs-Kopplung, keine statische Yukawa-Staerke. V4 nennt diese Stelle
    nicht mehr, verlangt war das nicht. Siehe E15.
- Ob Abschnitt 4.5 bis S. 35 reicht, habe ich nur ueber diese Stelle geprueft, nicht ueber den Beginn von Abschnitt 5.

## 5. Urteil und Anforderungen

**Urteil: einfuegen nach genannten Aenderungen.**

| Anforderung V3 | Stand V4 | Neuer Befund |
|---|---|---|
| N9 (A) | teilweise: (b) erfuellt, (a) Gegenstand erfuellt, Kreisangabe fehlerhaft | N13 (A) |
| N10 (R) | erfuellt | - |
| N11 (R) | erfuellt | N14 (R) |
| N12 (R) | erfuellt | - |

Woertliche Zitate in den geaenderten Stellen: 8 von 8 stimmen.

Kennzeichen wie bisher: A = vor dem Einfuegen zu erfuellen, R = redaktionell, vor dem Einfuegen, E = Empfehlung. Ich
schreibe keinen Ersatztext.

- **N13 (A), Z. 91-94.** Kreis und Behaupter muessen zusammenpassen.
  - Die Kreisangabe muss den Ort einschliessen, an dem EGHS an der Quelle gelesen wurde (RUNDE-11/cemz-mess/quellen/).
    Alternativ muss die Aussage fuer den tatsaechlich genannten Kreis stimmen.
  - Fuer die an der Quelle gelesenen Arbeiten ausserhalb von spin2-d4/quellen/, die der Nachtrag selbst heranzieht
    (mindestens CEMZ und Bucciotti), ist anzugeben, ob die "nur"-Aussage fuer sie geprueft ist.
- **N14 (R), Z. 46-52.** Der Block darf nicht als "CHLPSD setzen keine Regge-Beschraenktheit voraus" lesbar sein.
  - Kenntlich machen, dass die Autoren selbst eine verschmierte Regge-Schranke voraussetzen und so nennen (S. 10, Fn. 7:
    J0 <= 1, genutzt J0 < 2; S. 11: "Regge growth (2.23)").
  - Ebenso, dass sie Regge-Beschraenktheit als Folge ihrer Kausalitaetsannahme fuer alle Energien nennen (S. 2).
  - Von Bucciotti unterscheiden sie sich in Form und Einordnung, nicht darin, ob eine solche Annahme gemacht wird.
- **E13, Z. 16.** Das Subjekt "Ringdown-Grenzen" wie im Original auf kubische Korrekturen begrenzen.
- **E14, Z. 49-50.** Die Vorsicht der Quelle ("We believe") nicht in ein "nennen" umwandeln.
- **E15, Z. 95-100.** CHLPSD S. 35 ("four-derivative graviton-strength coupling") erwaehnen oder begruendet weglassen. Wer
  nach Kopplungen gravitativer Staerke sucht, findet diese Stelle.
- **E16, Z. 84.** Eindeutig machen, worauf "der schwachen Kopplung" grammatisch bezogen ist.

## 6. Ende

- Abschluss der Pruefung (date, vor dem Schreiben dieses Abschnitts): 2026-10-01 21:54:47 CEST. Beginn 21:48:03, also
  6 min 44 s (21:48:03 bis 21:54:03 sind 6 min, dazu 44 s). Das liegt in der Zeitbox von 10 min.
- sha256 des geprueften Entwurfs NACHTRAG-ENTWURF-V4.md um 21:54:47: ca9d3ade8851d66e... Zu Beginn habe ich keinen Hash
  genommen. Beim diff um 21:48 gab es keine abweichenden Bloecke ausser den fuenf in Abschnitt 0.
- Gelesen, alles nur in Ausschnitten:
  - diff V3/V4, V4 vollstaendig
  - LESUNG-LETZTE-SCHICHT-V3.md Abschn. 5-6
  - WARUM-SPIN-2.md Z. 528-546
  - 2201.06602.txt Z. 117-150, 477-545, 591-601, 619-623, 1860-1870, 1990-1997, dazu grep auf Zitate
  - 2605.00089.txt Z. 1148-1160
  - 1704.01590.txt Z. 749-772
  - quellen/SHA256SUMS.txt
  - grep-Zeilen aus SPIN2-D4.md
- Nicht gelesen: Ordner codex-lesung (paralleler Pruefer), gesperrte Pfade, KARTE.md.
- Kein BRIEF-Pfad genannt; der Auftrag stammt aus der Nachricht der Leitung. Keine Interpreter, kein awk, kein git, kein
  Peerbus, keine Unteragenten.
