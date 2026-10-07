# DENKNOTIZ: Warum atmen grosse Klumpen so lange, und hinterlaesst die Leiter stiller Stellen Spuren in der Bildung?

- Leitung: claude-primary, Schreibtisch. Geschrieben ab 2026-10-02 20:14:48 CEST (date), nach Finns "denk das weiter durch".
- Alles [H], nur aus vorhandenen Daten; keine neue Rechnung.

## 1. Was schon feststeht (Projektdaten)

- **Breite nahe einer Sprosse (2D, M1, n = 7; RUNDE-12/leiter2d-praez, Abschn. 2c/2d):**
  - Die Abstrahlbreite |Im rho| faellt V-foermig: 4,5e-4 ... 2,6e-7 ... 1,7e-4 ueber omega^2 0,5289 bis 0,5295.
  - Die signierte Wurzel der Breite ist linear mit Steigung -57 je Einheit omega^2. Also gilt |Im rho| ~ (57 dw)^2,
    mit dw = omega^2 - omega^2_Sprosse.
  - Die stille Mode hat rho ~ 1,556. Nur der a-Kanal (omega + rho) ist offen.
- **Keine stillen Stellen im kubisch-quintischen NLS und in Quantentroepfchen** (RUNDE-09 MESS-1, RUNDE-10 NLS-LEITER):
  Ohne zweiten, geschlossenen Kanal mit Wandzustand gibt es keine stille Stelle. Die naheliegende Bruecke zu
  Troepfchen-Experimenten traegt also nicht; ein Laborsystem braucht zwei Frequenzzweige mit Luecke.
- **BILDUNG-2, Arm A (omega^2 = 0,52, Q ~ 1421):** Der Klumpen atmet bis T = 1000 stark.
  - S_max schwankt zwischen ~1,00 und ~1,25; der exakte Familienball im selben Aufbau bleibt bei 1,0194 konstant.
  - Die Abtastung alle 10 Einheiten (lauf-69/ausgabe/fein_a_500-1000_ergebnis.json, diag) zeigt eine langsame
    Komponente mit Periode ~60 (rho ~ 0,1), dazu Spitzen (Aliasing moeglich).

## 2. Drei Erklaerungen fuer langes Nachschwingen

- **H1, Naehe zur Sprosse:** Lebensdauer tau ~ 1/(57 dw)^2.
  - Laenger als T lebt die Mode fuer |dw| < 1/(57 sqrt T): T = 1000 -> 5,5e-4, also ~28 % aller Groessen bei einem
    Sprossenabstand ~4e-3 in omega^2. T = 1e4 -> 1,75e-4, also ~9 %.
  - Zwischen den Sprossen (dw ~ 2e-3, quadratisch hochgerechnet) ist |Im rho| ~ 1e-2, also tau ~ 100.
- **H2, allgemein schwache Abstrahlung grosser, duennwandiger Baelle:** Die Breite ist dort ueberall klein, und die
  Sprossen setzen nur schmale Spitzen darauf.
- **H3, gebundene Moden unter der Abstrahlschwelle:** Moden mit rho < m - omega (hier 1 - 0,72 = 0,28) haben gar keinen
  offenen Kanal und strahlen linear nie ab. Grosse duennwandige Baelle haben eine niederfrequente Wand-Atmung.
  - Die langsame Komponente mit rho ~ 0,1 im Arm-A-Lauf passt dazu.

## 3. Folgerung

- Das lange Nachschwingen des grossen Klumpens ist **wahrscheinlich H3**, nicht die Leiter. Eine gebundene
  Wand-Atmung kann nur nichtlinear abklingen, also sehr langsam.
- Die stillen Moden der Leiter sind dagegen hochfrequent (rho ~ 1,5) und kurzwellig. Ein glatter Klumpen regt sie kaum
  an. Ihre Spur in der Bildung ist deshalb fuer glatte Klumpen **schwach zu erwarten** und erst bei heftiger Bildung
  (Stoesse, Verschmelzen) deutlich.
- Pruefbare Fingerabdruck-Vorhersage [H]: Ist die hochfrequente Mode angeregt, klingt sie an der Sprosse viel langsamer
  ab als zwischen den Sprossen. Das Fenster langer Lebensdauer schrumpft wie 1/sqrt(T).
  - In einem Ensemble gebildeter Baelle zeigt die spaete Restamplitude dieser Mode Gipfel an den Sprossen
    ("magische Groessen" langen Nachklingens).
- Ein Unterscheidungspunkt fuer H1 gegen H2 liegt bei n = 7 schon in den Frequenzdaten: Wie gross ist |Im rho| zwischen
  den Sprossen wirklich, statt hochgerechnet? Eine Zeitbereichsmessung der Abklingrate an der Sprosse und daneben waere
  zugleich eine unabhaengige Gegenprobe (L2) der Breiten aus Runde 12.

## 4. Naechster Test (Karte BILDUNG-LEITER, daneben)

1. Radiale Zeitentwicklung (l = 0, 2D) an der Sprosse n = 7 und daneben.
2. Gezielte Anregung der stillen Mode (rho ~ 1,556) bzw. glatter Klumpen.
3. Dichte Abtastung und Spektralzerlegung: gebundene gegen ueberschwellige Moden, Abklingraten gegen die
   Runde-12-Breiten.
