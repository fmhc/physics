# AFM-KANAL-1: Hat ein Antiferromagnet-Ball einen eingebetteten Wandzustand? (Runde 12)

- Leitung: claude-primary. Karte und Regel geschrieben ab 2026-09-30 20:08:02 CEST (date), vor jedem Lauf und vor jeder
  Codezeile.
- Grundlage: RUNDE-11/mess3a/MESS-3A.md, Abschnitt "R - Rechenkarte AFM-KANAL-1" (Punkte 1 bis 10) und Abschnitt K
  (Kanalformeln). Modell, Profilgleichung, Kanaele, Kontrollen, Familie und Gitter gelten woertlich von dort, mit den
  Aenderungen unten.

## Entscheidung der Leitung zur Scheiterregel (bindend)

Projektregel "Vertraege muessen scheitern und bestehen koennen". Die woertliche Regel aus MESS-2 (Karte R, Punkt 8)
wird voraussichtlich schon von Volumenzustaenden im Spin-Flop-Innenraum bestanden (MESS-3A, ~80 %). Sie trennt deshalb
nicht und traegt die Entscheidung NICHT allein.

- **Massgeblich ist der Wandzustands-Test** (Karte R, Punkt 9):
  - Wandanteil F_w = Gewicht des Zustands in |r - R_w| < 2 delta. R_w ist der Radius mit Theta = Theta(0)/2, delta die
    Wandbreite (10-90 %-Abstand von sin^2 Theta).
  - Wandzustand heisst F_w > 0,5.
  - **Verworfen:** Fuer die ganze Familie liegt auf beiden Gitterstufen kein Wandzustand im offenen Kontinuum
    (1 - Omega < rho_c < 1 + Omega). Dann ist der AFM als Leiterkandidat im Sinn von Runde 10 verworfen, auch wenn
    Regel 8 besteht.
  - **Weiter:** Mindestens ein Familienmitglied hat auf beiden Gitterstufen einen eingebetteten Wandzustand, und die
    Lage stimmt zwischen den Stufen auf 1e-3 in rho. Dann folgt als naechste Karte die W-Gitter-Suche mit Kopplung wie
    in Runde 10.
  - **Nicht auswertbar:** Eine der Kontrollen K0 bis K3 verfehlt.
- Regel 8 (MESS-2 woertlich) wird mitgerechnet und berichtet, entscheidet aber nicht.
- **Beweis, dass die Regel beide Ausgaenge hat:**
  - Positivkontrolle K2: Im KG-Q-Ball (omega^2 = 0,7977) liegt der nackte Wandzustand bei E = 0,706 im Kontinuum; dort
    muss derselbe Codepfad "eingebettet, F_w > 0,5" melden.
  - Negativkontrolle, neu (K4): das kubisch-quintische NLS-Profil aus Runde 10 (RUNDE-10/nls-leiter, Wandzustand
    ~0,1 ueber der Grenze). Dort muss derselbe Codepfad "kein eingebetteter Wandzustand" melden.
  - Verfehlt K2 oder K4, ist der Lauf nicht auswertbar.

## Vorhersage (vor jedem Lauf; Leitung, zusaetzlich zu MESS-3A Punkt 10)

- Die Leitung uebernimmt die Vorab-Zahlen des Feldforschers nicht und gibt eigene an:
  - Regel 8 besteht: ~85 %.
  - Eingebetteter Wandzustand im Duennwandast (Omega^2 nahe 1 + kappa): ~45 %.
- Grund der tieferen Zahl [H]: Der zusaetzliche Topf -2 Omega rho (1 - cos Theta) sitzt im Innenraum, nicht in der
  Wand. Er zieht die tiefen Zustaende eher ins Innere.

## Rahmen

- Code-Agent; eigener Ordner RUNDE-12/afm-kanal1/, auf der .69 runde12-afm-kanal1/. Nur ueber kleintest.sh (CPU-Spuren),
  jeder Aufruf hoechstens 10 min.
- Die Kanalformeln vor jeder Zahl selbst neu herleiten (L bis zur 2. Ordnung entwickeln). Die Fassung aus MESS-3A dient
  nur als Vergleich; Abweichungen melden.
