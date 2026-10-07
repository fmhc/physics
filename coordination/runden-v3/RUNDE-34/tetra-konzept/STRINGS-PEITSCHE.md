# Punkte -> Striche: Kraft, Strings, Peitsche (Schreibtisch der Leitung, Runde 34)

- Leitung claude-primary, geschrieben ab 2026-10-03 19:13:20 CEST (date).
- Anlass: Finn ~19:12: "haben wir diese kraft auch schon wenn wir die stabilen punkte-ergeben-strich-logik folgen, oder
  werden wobbelnde strings automatisch daraus die ggf brechen wenn sie zu lang werden? wenn man mal so ne peitsche
  ueberlegt dann gibts da ja auch super schnelle bereiche, ist das vllt lichtgeschwindigkeit"
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## 1. Die Kraft haengt an der Dimension des Netzes [M]

Ein erhaltener Fluss zwischen Quelle und Senke (Gauss-Gesetz) breitet sich so weit aus, wie das Netz es erlaubt:

| Netz | Fluss im Abstand r | Potential | Kraft |
|---|---|---|---|
| Linie (Punkte -> Strich) | bleibt im Strich, ~1 | ~ r (linear) | konstant, unabhaengig vom Abstand |
| Flaeche (Dreiecke) | verteilt sich auf ~r | ~ ln r | ~ 1/r |
| Raum (Tetraeder) | verteilt sich auf ~r^2 | ~ 1/r | ~ 1/r^2 (Coulomb) |

- Das gilt, wenn jeder Flussbeitrag Energie kostet (Feldenergie ~ Fluss^2).
- Zaehlt nur die Zahl der Moeglichkeiten (entropisch, wie im klassischen Spin-Eis), ist die Linie ein Sonderfall: Der
  Fluss ist dort vollstaendig festgelegt, also gibt es gar keine Kraft. Die Flaeche gibt ln r [L: Quadrat-Eis,
  Hoehenmodell], der Raum 1/r [L: Coulomb-Phase].
- **Antwort auf Finns erste Frage:** Auf der Stufe "Punkte ergeben Striche" gibt es diese Kraft noch nicht als
  Fernkraft. Entweder zieht der Strich mit konstanter Kraft (wenn Fluss Energie kostet), oder es gibt gar keine Kraft
  (wenn nur gezaehlt wird). Die abnehmende Coulomb-Kraft entsteht erst im Raum.

## 2. Wobbelnde Strings, die brechen [L, H]

- **Ein Strich mit konstanter Zugkraft ist ein String**, genau wie zwischen Quark und Antiquark (Einschluss, linear
  wachsendes Potential) [L].
- **Brechen:** Wird der String so lang, dass seine Energie sigma * r die Kosten fuer ein neues Quelle-Senke-Paar (2 mu)
  uebersteigt, ist es guenstiger, ein Paar zu erzeugen. Dann bricht er bei r_c ~ 2 mu/sigma [M]. In der QCD heisst das
  String-Bruch [L; Gitternachweis z. B. Bali u. a. 2005, L?].
- **Wobbeln:** Ein String in einer Flaeche oder im Raum zittert quer. Das gibt einen universellen Zusatz zum Potential,
  V(r) = sigma r + c - pi (d - 2)/(24 r) mit d = Zahl der Raumzeit-Dimensionen (Luescher-Term) [L: Luescher, Symanzik,
  Weisz 1980]. Das Zittern selbst erzeugt also wieder einen kleinen 1/r-Anteil.
- **Wann Strings statt Coulomb im Raum:** Wird der Fluss in Rohre gezwungen, z. B. weil sein Ausbreiten Energie kostet wie
  ein Magnetfeld im Supraleiter (Abrikosov-Flussschlaeuche) oder durch Monopol-Plasma (Polyakov) [L], bilden sich auch
  im Raum Strings.
  - Unser Tetraeder-Eis (FLUSS-1, Netz A) erwartet Coulomb, also keine Strings.
  - Der frustrierte K4-Kristall (Netz B) erwartet Abschirmung, das ist das Gegenteil eines Strings: Die Kraft stirbt ab,
    statt konstant zu bleiben.

## 3. Peitsche und Lichtgeschwindigkeit [L, H]

- **Peitsche:** Eine Welle laeuft das duenner werdende Ende entlang. Dieselbe Energie steckt in immer weniger Masse, also
  wird die Spitze immer schneller; der Knall ist ein Ueberschallknall der Spitze [L?: Goriely/McMillen, PRL 2002].
- **Relativistischer String:** In einer lorentzinvarianten Theorie (wie unsere, c = 1) bildet ein schwingender
  geschlossener String (Nambu-Goto) typischerweise Spitzen ("Cusps"), an denen ein Punkt des Strings kurz genau die
  Lichtgeschwindigkeit erreicht [L: Turok 1984; Vilenkin/Shellard]. Bei kosmischen Strings senden diese Spitzen kurze
  Gravitationswellen-Blitze [L: Damour/Vilenkin 2000].
  - **Antwort auf Finns zweite Frage:** Ja, bei einem relativistischen String ist die "Peitschenspitze" genau
    Lichtgeschwindigkeit, fuer einen Punkt und einen Augenblick. Darueber geht es nie.
- **Unterschied zu Q-Baellen:** Ein Q-Ball ist ein Klumpen mit Ruhemasse. Er kann c nie erreichen; in Kegelmulden
  bleibt er bei einem Bruchteil (EINFANG-1: 0,14 c; LICHT-1 rechnet die Obergrenze). Die Peitschenspitze braucht ein
  ausgedehntes Objekt mit Zugspannung, das Energie in immer weniger Masse buendelt, also einen String oder eine Wand.

## 4. Was man rechnen koennte (Vorschlaege)

- **STRING-1:** dieselbe Flussregel auf Linie, Dreiecksflaeche und Tetraederraum, mit Energie je Fluss und erlaubter
  Paarerzeugung (Kosten 2 mu).
  - Vorhersage: linear mit Bruch bei r_c = 2 mu/sigma, dann ln r, dann 1/r.
  - Das zeigt Finns Kette Punkte -> Striche -> Dreiecke -> Tetraeder als Kette der Kraftgesetze.
  - Weitgehend Lehrbuch, also eher Vorfuehrung als Test.
- **PEITSCHE-1:** eine geschlossene Wand (Domaenenwand) in 2D in unserer Feldtheorie zusammenfallen lassen, oder einen
  schwingenden String.
  - Gemessen wird die hoechste lokale Geschwindigkeit; Vorhersage: naehert sich c.
  - Dazu eine Q-Ball-"Huelle" zum Vergleich.

## Berichtigungsvermerk (2026-10-03 22:39:20 CEST)

- Diese Datei hat der frische Gegenleser geprueft: RUNDE-35/GEGENLESEN-R35.md. Gueltige Fassung der betroffenen Stellen: RUNDE-35.md, Abschnitt "Berichtigung nach GEGENLESEN-R35". Der urspruengliche Text bleibt zur Nachvollziehbarkeit stehen.
