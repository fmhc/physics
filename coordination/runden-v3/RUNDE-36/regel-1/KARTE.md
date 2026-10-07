# REGEL-1: Netz mit eingebauter Regel: Schwerewellen, Newton und gleiches Fallen fuer Q-Baelle (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 01:32:09 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn ~01:25: "Bau die Regel". Schreibtisch RUNDE-36/REGEL.md (Regel: Kruemmungsmuster der Spannung kostenlos, also
    c = 1/2).
  - REGGE-4D-1: Im Laengen-Bild ist die Regel von selbst da (Faktor -2).
  - Hier: Weg B (Kraftfluss) mit eingebauter Regel, dazu Materie, deren Energie die Quelle ist (REGEL.md, Abschnitt 4).
- Kennzeichen: [M] Mathematik (vorab ableitbar), [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Gitter:** Gu/Wen-N-Typ (Code RUNDE-36/tensor-eis-n/ und lambda-1/), c = 1/2 exakt, ohne Strafterme. Die
  kinetische Energie ist dann invariant unter Gl. 23 (Regel), also gleich |E_TT|^2 auf der Zwangsflaeche [M].
- **Laufende Moden** [M, L]: Auf der Zwangsflaeche bleiben je k die zwei Helizitaet-2-Moden. Dispersion nach Gu/Wen Gl. 35
  linear bei kleinem k (N-Typ) [S laut TENSOR-EIS-N].
- **Materie:** Statische Energiedichten rho_E zweier Q-Baelle aus 3D-Radialprofilen von M1 (beta = 1/2), Q = 50 und
  Q = 500 (verschiedenes E/Q). Sie speisen die Massenregel: R^ii = kappa rho_E.
  - Die Antwort koppelt ebenfalls an rho_E (Wechselwirkung int Phi rho_E), also Kraft je Energie = -grad Phi
    (Aequivalenzprinzip) [M].
  - Zum Vergleich die Ladungskopplung: Quelle und Antwort ueber int abs(phi)^2 = Q/(2 omega) (AEQ-0). Dort ist der
    Unterschied ~15 % fuer duenne gegen dicke Waende.
- **Erwartung:** Newton U = -G_eff E1 E2/d fern (G_eff aus der Normierung, TENSOR-EIS-N: 1/(8 pi) je Einheitsquelle);
  gleiches Fallen bei Energiekopplung; ungleiches bei Ladungskopplung.

## Test (Code-Agent)

- **Teil 1, Wellen:** lineare Dynamik auf der Zwangsflaeche bei c = 1/2.
  - Zahl der laufenden Moden je k (Rest Eichung bzw. Null).
  - omega(k) bei kleinen abs(k) in mindestens 50 Richtungen; Geschwindigkeit v und Richtungsstreuung.
  - Kein Wachstum.
- **Teil 2, Newton mit Q-Ball-Quellen:** statische Loesung fuer zwei rho_E-Quellen auf dem Gitter (Groessenreihe bzw.
  Torus-Korrektur wie TENSOR-EIS-N und LAST-1).
  - U(d) fuer d von 4 bis 10 Ballradien; U d/(E1 E2) gegen d.
- **Teil 3, Fallen:** Kraft je Energie auf einen kleinen und einen grossen Ball (Q = 50 bzw. 500) im Feld einer
  schweren dritten Quelle bei gleichem Abstand.
  - Eotvos-Groesse eta = 2 abs(a1 - a2)/(a1 + a2).
  - Einmal mit Energiekopplung, einmal mit Ladungskopplung.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RG0 | Kontrolle: Invarianzdefekt unter Gl. 23 bei c = 1/2 < 1e-12; kein Wachstum auf der Zwangsflaeche | 90 % |
| RG1 | Je k genau 2 laufende Moden mit omega^2 = v^2 k^2 (1 + O(k^2)); v ueber 50 Richtungen bei abs(k) = 0,1 innerhalb 1 % gleich | 70 % |
| RG2 | Zwei Q-Ball-Quellen: U d/(E1 E2) konstant innerhalb 1 % fuer d >= 4 Ballradien (Newton), nach Torus-Korrektur | 70 % |
| RG3 | Energiekopplung: eta < 1e-3 (bei d = 8 Ballradien des grossen Balls); Ladungskopplung: eta > 5e-2 | 70 % |

**Bedeutung (vorab):**
- RG0 bis RG3 treffen ein: Mit der eingebauten Regel und Energie als Quelle gibt ein Netz zugleich
  - zwei Schwerewellen-Polarisationen,
  - Newtons Anziehung,
  - gleiches Fallen fuer verschieden gebaute Q-Baelle.
  - Das ist der statische Teil der Gesamtformel aus unseren Bausteinen [H: Lorentz-Invarianz und Nichtlinearitaet bleiben
    offen, REGEL.md Abschnitt 5].
- RG1 verfehlt: Die Wellen sind nicht linear bzw. nicht richtungsfrei (Gitterfassung). Wie bei Gu/Wen erwartet waere das
  fuer unsere Gravitation ausgeschlossen (GW170817 [L]).

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (nicht cpu, cpu2, cpu5, cpu6, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
