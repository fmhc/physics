# GUERTEL-2: Wie hoch ist die Sperre auf einem konstruierten Entwirrungsweg am Tetraeder-Knoten? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 16:44:40 CEST (date), vor jeder
  Rechnung.
- **Herkunft:** Kartenvorschlag 1 aus GUERTEL-1 (RUNDE-37/guertel-1/ERGEBNIS.md, Z. 250 ff.).
- **Finns Auftrag (04.10.):** "teste die gürtel-1 sache durch als basis für kleinste bewegungen ... und auch
  grundsätzlich".
- **Stand nach GUERTEL-1:**
  - Einfaches Abkuehlen findet die 720-Grad-Entwirrung nicht.
  - Der vorwaerts gewickelte Zustand ist metastabil (Ratsche mit Zwischenrasten).
  - Die Abkuehlung war zu schwach (T0 = 0,5); E_min(0) ist vermutlich nicht das wahre Minimum.
- **Bau (Vorschlag des Agenten, Staley-Weg):**
  - Schalendrehungen g_s(r) = Rot(x, 2 pi f_aussen(r)) Rot(n(s), 2 pi f_innen(r)); n(s) dreht von x ueber y nach -x.
  - Die Faeden bleiben radial monoton; fuer duenne Faeden ist das durchdringungsfrei [M, Agent].
  - Daraus wird der Anfangsstring zwischen idealer 4-pi-Wicklung und Grundzustand gebildet und mit der vorhandenen
    Stringmethode samt Sonde relaxiert.
  - Zusaetzlich ein String vom gemessenen Zwischenrast-Zustand W = (1, 0, 1, 0) aus.
- **Ableitbarkeitsprobe:**
  - Die Existenz des Wegs ist ableitbar.
  - Die Hoehe der Sperre S ist nicht ableitbar: S = 0 in fuehrender Ordnung ist durch GUERTEL-1 widerlegt, weil der
    Vorwaertsast metastabil ist.
  - Projekt-grep: keine Stringrechnung mit konstruiertem Staley-Weg.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [H] Hypothese.

## Auftrag (Code-Agent)

1. GUERTEL-1 vollstaendig lesen: ERGEBNIS, PLAN, code; die Selbstanzeigen besonders. Den Code kopieren, nicht aendern.
2. **PLAN:**
   - Bau des Staley-Wegs und Durchdringungsprobe entlang des ganzen Anfangsstrings.
   - Stringrelaxation (Bilderzahl, Konvergenz).
   - Energiemasse: S = max E entlang des relaxierten Wegs minus E(Ende); dE_360 wie in GUERTEL-1.
   - Abkuehlung staerker als in GUERTEL-1 (Temperaturleiter), um E_min(0) neu zu bestimmen.
   - Fadenlaengen 1,3 und 1,8.
3. Plan, Rauchlauf, Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GZ0 | Kontrollen: Der konstruierte Anfangsstring ist durchdringungsfrei (Mindestabstand ueber der Ausschlussgrenze an jedem Bild); die Stringmethode reproduziert an einem trivialen Weg (0 nach 0 Grad) S = 0 auf 1 % | 85 % |
| GZ1 | [H] Bei Fadenlaenge 1,8 endet der relaxierte String ohne Durchdringung im entwirrten Zustand, und S < dE_360 | 40 % |
| GZ2 | [H] S faellt mit der Fadenlaenge (S(1,8) < S(1,3)), wenn beide Wege gefunden werden | 65 % |
| GZ3 | [H] Mit staerkerer Abkuehlung liegt E_min(0) mindestens 10 % unter dem Wert von GUERTEL-1 | 50 % |

**Bedeutung (vorab):**
- **GZ1 trifft ein:** Der 720-Grad-Trick ist am Tetraeder-Knoten energetisch zugaenglich; die "Ratsche" aus GUERTEL-1 war
  kinetisch. Die Sperre S gibt die Energieskala, ab der der Knoten "Spin-1/2-artig" werden kann [H].
- **GZ1 verfehlt:** Der Weg bleibt an einer Kontaktsperre haengen oder ist teurer als eine Umdrehung. Dann ist die
  Zweifach-Struktur am Knoten energetisch gesperrt.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, auf den Spuren, die die Leitung beim Start eintraegt; je Lauf
  <= 10 min, 1 Thread. Zeitbox 150 min.

## Erweiterung vor dem Start (Leitung, 2026-10-04 17:10:47 CEST): Teil B "Guertel im Feld"

- **Finn (Nachricht zwischen 17:08 und 17:10, woertlich):** "kann es sein das rotation / tick bewegung in den
  dreiecken / tetraedern dazu führt das eine art gürtel effekt in dem feld zwischen innen und außenfeld vom objekt
  passiert?"
- **Einordnung [L, M]:**
  - Das ist der Mechanismus, mit dem ausgedehnte Objekte halben Spin bekommen koennen (Finkelstein/Rubinstein 1968;
    Skyrmionen als Fermionen).
  - Der "Guertel" ist das Feld zwischen Kern und Aussenraum. Eine 360-Grad-Drehung des Kerns gegen aussen verdrillt
    dieses Feld; 720 Grad lassen sich in 3D entdrillen (pi_1(SO(3)) = Z_2).
  - In 2D sammelt sich die Verdrillung an (pi_1(SO(2)) = Z). Passend dazu GUERTEL-1: Verdrillen ist im Raum 65-mal
    billiger als in der Ebene [E].
  - Unsere Q-Baelle in der bisherigen Formel haben diesen Guertel nicht (Feldraum zusammenziehbar, Projekt-Gedaechtnis
    "Spin 1/2: unveraenderte Formel kann es nicht"); mit Codex' Erweiterung C x S^2 schon.
- **Teil B (gekoppelt, gleicher Agent):**
  - Ein Kern, ein Tetraeder bzw. ein fester Drehrahmen, sitzt in einem Orientierungsfeld mit Werten in SO(3): ein
    Gitter aus Drehrahmen mit Kopplung tr(R_i^T R_j), der Rand im Aussenraum ist festgehalten.
  - Der Kern wird ueber viele Umdrehungen weitergedreht (quasistatisch, mit Relaxation); dasselbe in 2D mit SO(2) als
    Kontrolle.
  - Gemessen wird E_min(theta) ueber 0 bis 1440 Grad. Saettigt sie mit Periode 720 Grad (Guertel wirkt) oder waechst sie
    weiter (Verdrillung sammelt sich)?
  - Dazu die Sperre beim Uebergang zum entdrillten Zustand.
- **Ableitbarkeitsprobe:**
  - Topologisch ist E_min im Kontinuum 720-Grad-periodisch in 3D und in 2D nicht periodisch. Das ist eine Kontrolle.
  - Nicht ableitbar: ob die Relaxation auf dem Gitter den Entdrillweg findet, wie hoch die Sperre ist, und ob die Antwort
    mit der Gittergroesse stabil bleibt.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GZ4 | Kontrolle 2D (SO(2)-Feld): E_min waechst bei jeder vollen Umdrehung weiter (keine Saettigung bis 1440 Grad) | 85 % |
| GZ5 | [H] 3D (SO(3)-Feld): Mit Relaxation saettigt E_min; E_min(720) liegt innerhalb 10 % bei E_min(0), E_min(360) deutlich darueber | 45 % |
| GZ6 | [H] Die Sperre im Feld ist kleiner als im Faden-Modell von GUERTEL-1, bezogen auf die jeweilige Umdrehungsenergie dE_360 | 40 % |

- Zeitbox damit 180 min.

## Start (Leitung, 2026-10-04 17:12:39 CEST)

- Spur: cpu10 (neu seit 04.10.). Ordner auf der .69: /home/fmh/fmhc-physics-remote/runde42-guertel-2/ (code/, rauch/, lauf/).
