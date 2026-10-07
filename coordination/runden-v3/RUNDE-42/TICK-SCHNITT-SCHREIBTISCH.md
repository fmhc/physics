# TICK-SCHNITT: Ableitbarkeitsprobe der Leitung (Runde 42, 2026-10-04 17:21:33 CEST)

- Anlass: Finns Frage "wenn ggf 4d in 3d nur instabil ist, ist das dann unser tick vllt?" und die vorgemerkte Karte
  TICK-SCHNITT-1 (RUNDE-42.md, Eintrag 17:08).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher.

1. **Zaehlung [M]:**
   - Faehrt man eine 3D-Hyperflaeche durch eine 4D-Triangulierung, ist jedes angeklebte 4-Simplex genau ein
     Pachner-Zug (1-4, 2-3, 3-2 oder 4-1), je nachdem, wie viele seiner 5 Tetraeder schon auf der Flaeche liegen.
   - Jede innere Ecke tritt genau einmal per 1-4 ein und einmal per 4-1 aus.
   - Also: Zahl(1-4) = Zahl(4-1) = Zahl der inneren Ecken N0; Zahl(2-3) + Zahl(3-2) = N4 - 2 N0.
2. **Folge:**
   - Der Anteil der Zuege, die nach Hoehn (1-4, 4-1) keine Kruemmung tragen, ist 2 N0/N4.
   - Fuer zufaellige 4D-Delaunay-Netze ist N4/N0 eine bekannte Kennzahl der Poisson-Delaunay-Zerlegung [L?, Okabe u. a.];
     der Anteil liegt damit fest, im einstelligen Prozentbereich [L?].
   - Fuer ein statistisch isotropes euklidisches Netz haengt er nicht von der Schnittrichtung ab (Symmetrie).
3. **Bewertung:** TICK-SCHNITT-1 wie vorgemerkt (Anteil 2-3 gegen 1-4/4-1, Neigungsabhaengigkeit) ist vorab ableitbar
   und wird nicht als Karte gerechnet. Die Aussage an Finn von 17:08 ("nicht ableitbar ... gemessen wird") ist damit zu
   berichtigen.
4. **Was offen und pruefbar bleibt:**
   - Ob die 4D-Anomalie von KOVARIANZ-KUGEL-1 an genau diesen Umschaltungen haengt: KOVARIANZ-EPS-1 laeuft.
   - Ob Ticks raeumlich bzw. zeitlich korreliert auftreten (Lawinen, Wellen von Umschaltungen), wenn sich ein Netz
     langsam verformt. Das waere eine neue Karte mit eigener Ableitbarkeitsprobe.
