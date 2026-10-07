# UEBERLEITUNG-V-2: Traegt die stetige Grenze der 4D-Zeit auf Finns Netzen (V, S, B1), und sind ihre negativen Traegheitsrichtungen die konforme Richtung je Ecke? (Runde 49, Fast Lane nach UEBERLEITUNG-V-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 15:18:00 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - UEBERLEITUNG-V-1 (RUNDE-37/ueberleitung-v-1/ERGEBNIS.md):
    - Vorab festgelegt war eine kubische Extrapolation durch h = 1 bis 1/8. Sie scheiterte auf V: Der Gitterrest-Block D_0
      hat bei h = 1 neun bis zehn negative Eigenwerte, die mit kleinerem h einzeln durch null gehen (Pole des
      Schur-Komplements), umso tiefer, je kleiner abs(k). UV2 bis UV4 waren deshalb nicht entscheidbar.
    - **Nachtrag nach Sicht (von der Leitung gelesen, also nicht blind):**
      - h = 2^-8 bis 2^-14 an 591 k: konvergente Bloecke, ADM-Form (Potential = B, Lapse-Kopplung -c/2, Lapse reiner
        Multiplikator, kein Kreiselterm).
      - M_eff ohne statische Richtung, mit 10 negativen Eigenwerten je k.
      - Regime H mit M_eff und R1: TT-Spanne 5,1e-10 bei Tempo 1, keine wachsende Mode an 78 Raster-k und 513 BZ-k.
      - Polstellen: am BZ-Punkt unter h = 1/4; bei [100], kl = 0,05, unter 1/64; bei [321], kl = 0,01, zwischen
        2^-7 und 2^-8.
  - UEBERLEITUNG-KH-1: Kuhn hat eine statische Richtung (Raumdiagonale); M_eff ist auf gleichmaessigen Raten gleich DeWitt.
  - REGIME-K-2: Netze V (10 Ecken je Zelle), S (6 Ecken je Zelle), B1; euklidisch 26 (V) bzw. 7 (B1) Gittermoden negativer
    Steifigkeit je k.
  - REGGE-4D-SCHIEF-1: Eine Ueberzahl-Diagonale kann eine negative Gittermode werden.
- Kennzeichen: [M], [E], [P], [H], [N].

## Ableitbarkeitsprobe (Leitung)

- **Vorab [M, Kontinuum]:** Die DeWitt-Supermetrik hat je Punkt die Signatur (-, +, +, +, +, +); negativ ist die
  Spurrichtung (gleichmaessige Ausdehnung). Auf einem Gitter mit n Ecken je Zelle erwartet man deshalb n negative
  Traegheitsrichtungen je k, wenn das Gitter die Kontinuumsstruktur je Ecke erbt. Das ist eine Erwartung, keine Ableitung
  fuer das Gitter.
- **Gesehen (Vorwissen, offengelegt):** Werte des Nachtrags fuer V an den dort gerechneten 591 k und die drei
  Polstellen oben. Vorhersagen ueber genau diese Werte sind Kontrollen (UW0).
- **Nicht ableitbar:**
  - Zahl der negativen M_eff-Richtungen auf S und B1
  - ob sie auf V in den oertlichen Dehnungsrichtungen je Ecke liegen
  - Stabilitaet und Isotropie auf S und B1
  - Stabilitaet auf V an neuen k
  - der Verlauf h*(k)

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| UW0 | Kontrolle [P, gesehen]: Auf V bei h = 2^-10 und den 78 Raster-k des Nachtrags: TT-Spanne innerhalb Faktor 3 um 5,1e-10, keine wachsende Mode, 10 negative M_eff-Eigenwerte je k | 90 % |
| UW1 | [H] Auf S und B1 hat M_eff in der stetigen Grenze (h = 2^-10) an jedem gerechneten k genau so viele negative Eigenwerte wie Ecken je Grundzelle | 60 % |
| UW2 | [H] Auf V liegt der Raum der negativen M_eff-Richtungen bei kl <= 0,1 zu mindestens 90 % (gemittelte quadrierte Projektion) im Raum der oertlichen Dehnungsrichtungen je Ecke (Definition im Plan vor jeder Rechnung festlegen) | 45 % |
| UW3 | [H] Auf S und B1: Regime H mit M_eff und R1 in der stetigen Grenze, TT-Spanne unter 1e-8 und keine wachsende Mode an allen gerechneten k einschliesslich BZ-Rand | 50 % |
| UW4 | [H] Auf V bei h = 2^-10 an mindestens 1000 neuen k (neue Richtungen und BZ-Randpunkte, nicht die 591 des Nachtrags): keine wachsende Mode und TT-Spanne unter 1e-8 | 75 % |

- **Messziel ohne Vorhersage:** h*(k) = groesstes h, bei dem D_0 einen Eigenwert null hat, fuer drei Richtungen ueber
  kl = 0,005 bis pi; Exponent von h* gegen kl. Vorwissen der Leitung: drei Punkte aus dem Nachtrag (oben).

**Bedeutung (vorab):**
- **UW3 und UW4 treffen ein:** Die stetige Grenze der 4D-Zeit traegt auf Finns Netzfamilie: Traegheit, Lapse und Shift
  kommen aus einer 4D-Wirkung, die Wellen sind richtungsgleich und stabil. Die Grundgleichung v3 nimmt diese Grenze als
  Kern. Ein endlicher Takt muss dann fuer lange Wellen kleine Zeitschritte haben (Lage der Pole) [H].
- **UW1 und UW2 treffen ein:** Die negativen Traegheitsrichtungen sind die bekannte konforme Richtung der ART je Ecke, kein
  Gittergeist.
- **UW3 verfehlt:** Die stetige Grenze traegt nur auf V; dann ist zu klaeren, welche Eigenschaft von V das leistet.

## Rahmen

- Code-Agent. Code aus RUNDE-37/ueberleitung-v-1/code kopieren (uv.py, nachtrag_uv.py, nachtrag2_uv.py samt Vorlagen) und
  die Netzbauten S und B1 aus RUNDE-37/regime-k-2/code; dort nichts aendern.
- Hauptwert h = 2^-10; Kontrolle h = 2^-8 und 2^-12 (Konvergenz der Bloecke im Plan beziffern). Statische Richtungen,
  falls sie auf S oder B1 auftreten, wie in UEBERLEITUNG-V-1 vorab festgelegt (Schur-Komplement, keine stille
  Pseudo-Inverse).
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu2, cpu3 und cpu4. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
