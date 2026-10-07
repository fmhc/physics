# UNSCHAERFE-KANTE-L: Laesst sich Heisenbergs Unschaerfe in unserem Modell durch "Kantenfindung in Dimensionen" erklaeren, also dadurch, dass ein Teilchen in jedem Takt eine Kante waehlt? (Runde 46, Finn-Auftrag, Literatur und Schreibtisch)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 05:46:59 CEST (date), vor jedem Abruf.
- **Finn (05.10., vor 05:45:46), woertlich:** "Kann Heisenberg unschärfe durch Kantenfindung in Dimensionen in unserem Modell erklärt werden"
- **Lesarten der Leitung (alle pruefen):**
  - (a) Kantenwahl je Takt als **Zufall**: klassischer Irrweg bzw. Telegraphenprozess auf Finns Netz (Diamant: 4 Kanten je Knoten, 3 Dimensionen)
  - (b) Kantenwahl als **Amplitude**: Quantenlauf bzw. Dirac-Automat (im Projekt bekannt: D'Ariano/Perinotti, QCA-TETRA-1)
  - (c) **Diskretheit:** kleinste Laenge l, begrenzter Impuls (Brillouin-Zone), also eine verallgemeinerte Unschaerfe (GUP)
  - (d) **"In Dimensionen":** Spielt eine verborgene bzw. zusaetzliche Richtung mit (verborgene Haelfte, kompakte Dimension), deren Kantenwahl in 3D als Unschaerfe erscheint [H]?
- Kennzeichen: [S], [S Abstract], [L], [L?], [M], [ES], [H], [P].

## Projektsuche (vor der Karte, alle Dateitypen)

- **Gesamtformel:** gesamtformel-20260921/HILBERT.md Z. 89: Die klassische Gesamtformel hat keinen Kommutator [x, p] = i hbar, also keine Unschaerfe. Bekannte Luecke [P].
- **Zitterbewegung und Telegraphenprozess:**
  - Model-Lab five-why (09.09.): H = c p sigma_z + Delta sigma_x mit <v> = c cos(2 Delta t/hbar); klassisches Gegenmodell mit Poisson-Flips, <v> = c exp(-2 lambda t) [P].
  - Rabi-Runner bzw. innere Uhr: gitter-checkliste.json W3 [P].
- **Minimallaenge:** nur ein Literaturverweis (Hossenfelder 2013, RUNDE-06) [P]; keine GUP-Karte.
- **Stochastische Mechanik (Nelson):** nur im DOPPELSPALT-L-Katalog [P].

## Ableitbarkeitsprobe (vor der Karte, Leitung)

- **Vorab ableitbar [L, M]:**
  - Jede Wellenbeschreibung erfuellt Delta x Delta k >= 1/2 (Fourier); mit p = hbar k ist das Heisenberg. Das gilt auch fuer Wellen auf Finns Netz.
  - Auf dem Gitter ist der Ort diskret und k periodisch. Abweichungen gibt es erst bei Delta p ~ hbar/l.
  - Die Kantenfindung erklaert die Unschaerfe also nur, wenn sie die Welle bzw. die Amplitude erzeugt (Lesart b). Das ist der Dirac-Automat, im Projekt bekannt [P].
  - Klassischer Irrweg mit Schritt l und Takt tau in d Dimensionen: D = l^2/(2 d tau). Fuerths Relation Delta x Delta v >= D [L?]. Mit D = hbar/(2m) folgt m = d hbar tau/l^2 [M], die Masse aus Takt und Masche.
  - Telegraphenprozess mit Flip-Rate lambda: D = c^2/(2 lambda); mit lambda = m c^2/hbar folgt D = hbar/(2m) [M, L: Kac; Gaveau/Jacobson/Kac/Schulman 1984].
- **Nicht ableitbar (Literatur):**
  - Wie weit tragen klassische Kantenwahl-Modelle (Nelson, Telegraph): Einzelzeit-Statistik ja, Mehrzeit-Korrelationen bzw. Bell nein (Grabert/Haenggi/Talkner 1979 [L?])?
  - Welche Messschranken gibt es an eine verallgemeinerte Unschaerfe bzw. eine kleinste Laenge?
  - Was koennte "in Dimensionen" (Lesart d) zusaetzlich leisten, und gibt es Literatur dazu (Kaluza-Klein, "Unschaerfe aus Extradimensionen")?

## Auftrag (feldforscher)

1. **Lesarten (a) bis (d):** je Mechanismus, was folgt (Form der Unschaerfe, Vorfaktor, Masse aus Netzgroessen), wo es von der Quantenmechanik abweicht, Datenlage.
2. **Literatur:**
   - Fuerth 1933 bzw. Nelson 1966 (stochastische Mechanik)
   - Gaveau/Jacobson/Kac/Schulman 1984 (Telegraph und Dirac)
   - Grabert/Haenggi/Talkner 1979 (Mehrzeit-Korrelationen)
   - Hossenfelder 2013 bzw. GUP-Messschranken (z. B. Bawaj u. a. 2015)
3. **Schreibtisch:**
   - die Formel m = d hbar tau/l^2 gegenlesen
   - welche Masse ergaebe sich mit l ~ Planck-Laenge und tau = l/c? (Vermutlich die Planck-Masse; dann erklaert das keine leichten Teilchen [ES])
   - was Finns Diamant-Netz (4 Kanten je Knoten) am Vorfaktor aendert
4. **Hoechstens ein Kartenvorschlag,** mit Ableitbarkeitsprobe und Projekt-grep ueber alle Dateitypen.

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| HU1 | [L?] Fuerth (1933) leitete Delta x Delta v >= D fuer Diffusion her; Nelson (1966) baut darauf auf, mit D = hbar/(2m) formgleich zu Heisenberg | 75 % |
| HU2 | [L?] Klassische Kantenwahl- bzw. Nelson-Modelle geben die Einzelzeit-Statistik richtig, scheitern aber an Mehrzeit-Korrelationen bzw. Bell (Grabert/Haenggi/Talkner 1979) | 75 % |
| HU3 | [L?] Messschranken an eine verallgemeinerte Unschaerfe lassen eine Masche von Planck-Groesse unbegrenzt (beta-Schranken weit ueber 1) | 65 % |
| HU5 | [M, Kontrolle] Mit l = Planck-Laenge und tau = l/c ergibt m = d hbar tau/l^2 eine Masse der Ordnung der Planck-Masse, also keine leichten Teilchen | 80 % |

**Bedeutung (vorab):**
- **HU1, HU2 und HU5 treffen ein:**
  - Zufaellige Kantenwahl gibt Heisenbergs Form, aber nur mit einer Masse, die der Takt festlegt, und ohne Interferenz und Bell.
  - Erklaeren kann die Kantenwahl die Unschaerfe nur als Amplitude (Quantenlauf). Dann ist sie Teil der Quantenmechanik auf dem Netz, keine klassische Erklaerung.
- **HU3 trifft ein:** Eine Netz-Unschaerfe mit kleinster Laenge ist von den Daten nicht verboten, aber auch nicht pruefbar.

## Rahmen

- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/unschaerfe-kante-l/.
