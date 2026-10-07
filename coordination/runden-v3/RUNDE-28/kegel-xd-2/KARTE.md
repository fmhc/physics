# KEGEL-XD-2: Ist die 2D-Abweichung hoehere Ordnung oder ein Fehler der Herleitung? (Runde 28)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 06:30:47 CEST (date), vor jeder Rechnung.
- **Herkunft:** KEGEL-XD (RUNDE-27/kegel-xd/ERGEBNIS.md).
  - Das Kopplungsgesetz erster Ordnung, Delta E_1(d) = -delta int_0^inf r g(d + r) dr mit g = f'^2 + U(f^2) - omega^2 f^2,
    traf in 3D bei delta = +-0,1284 an allen Abstaenden auf 0,081 % von |Delta E_1(0)|.
  - In 2D (KEGEL-Q-Gitter, delta = +-pi/3, Q = 200) verfehlte es KX1: In der Wandzone lag es bis 4,1 % daneben (d = 6,0 und
    7,2), sonst <= 0,86 %.
  - Zwei Lesarten: (A) Terme dritter Ordnung bei grossem delta; (B) ein Fehler der Herleitung, der nur in der Wandzone
    wirkt.

## Schreibtisch (vor jeder Rechnung)

- Fuer d != 0 haengt E(delta, d) glatt von delta ab. Der ungerade Teil O(d; delta) = [E(+delta) - E(-delta)]/2 enthaelt
  daher nur ungerade Potenzen: O = delta J_1(d) + delta^3 J_3(d) + ...
- Nach der Herleitung ist delta J_1 = Delta E_1.
- Die relative Abweichung r(d; delta) = [O - Delta E_1]/|Delta E_1(0)| faellt unter (A) wie delta^2:
  r(delta) = r(pi/3) (3 delta/pi)^2 (1 + O(delta^2)).
- Aus KEGEL-XD folgt max_d |r(pi/3)| = 4,1 %. Unter (A) ergibt das ~1,0 % bei delta = pi/6 und ~0,26 % bei delta = pi/12.
  - Korrekturen der Ordnung delta^2 gegenueber delta^2 bei pi/3 sind bis Faktor ~1,3 moeglich, daher die Bereiche unten.
- Unter (B) bliebe r in der Wandzone etwa gleich gross (~4 %), auch bei kleinem delta.
- Ableitbarkeitspruefung:
  - Die delta^2-Skalierung folgt nur, wenn die erste Ordnung richtig ist; genau das wird geprueft.
  - Projekt-grep: Kleine Defizite gibt es im Projekt nur in 3D (KEGEL-XD).

## Test (Code-Agent)

- **2D-Kontinuumskegel in Polarkoordinaten** (r, theta), theta-Periode Theta = 2 pi - delta, Spiegel theta -> -theta
  erlaubt.
- **Modell und Ball:** M1, beta = 1/2, Q = 200, Funktional und Lagebedingung wie KEGEL-Q bzw. KEGEL-XD (gleiche Definition
  von d).
- **Defizite:** delta = +-pi/3 (Kontrolle gegen KEGEL-Q), +-pi/6 und +-pi/12.
- **Abstaende:** die 17 Abstaende der KEGEL-Q-Tabelle (0 bis 19,2).
- **Gitter:** zwei Gitterweiten; Urteil auf der feineren.
- **Delta E_1(d):** aus dem ebenen Radialprofil wie in KEGEL-XD Teil A, fuer jedes delta; nur der Faktor delta aendert
  sich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K2-0 | Kontrolle: Bei delta = pi/3 trifft der Kontinuumscode den ungeraden Teil der KEGEL-Q-Gitterwerte (h = 0,2) an allen 17 Abstaenden auf 0,3 % von \|Delta E_1(0)\| | 80 % |
| K2-1 | delta = pi/6: max_d \|r\| liegt zwischen 0,6 % und 1,6 % | 65 % |
| K2-2 | delta = pi/12: max_d \|r\| liegt zwischen 0,15 % und 0,45 %, und das Verhaeltnis max\|r(pi/6)\|/max\|r(pi/12)\| liegt zwischen 3 und 5,5 | 60 % |

**Bedeutung (vorab):**
- K2-1 und K2-2 treffen ein: Lesart (A). Die erste Ordnung ist richtig, die 2D-Abweichung bei delta = pi/3 sind hoehere
  Ordnungen [H, numerisch gestuetzt].
- max|r| bleibt bei pi/12 ueber 2 %: Lesart (B). In der Wandzone fehlt der Herleitung etwas; beschreiben, wo.
- Alles dazwischen beschreiben, ohne nachtraegliche Bereiche.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren. Delta E_1(d) vorab versiegeln, nicht als Befehlszeilen-Argumente.
- Zeitbox 90 min.
