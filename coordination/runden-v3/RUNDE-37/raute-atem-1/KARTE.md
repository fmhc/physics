# RAUTE-ATEM-1: Finns Raute aus zwei Dreiecken mit atmenden Ecken (1 PU): Faltet sie zum Tetraeder, oeffnet sie sich wieder (Klapptakt), und wo sitzen die Kraefte? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben zwischen 2026-10-04 18:18:56 CEST und 2026-10-04 18:20:18 CEST (date), vor
  jeder Rechnung.
- **Finn (04.10.), woertlich:**
  - Zwischen 18:13 und 18:16: "also vllt dann die connection dings mit dem radius 1PU vom punkt dazu der auf sinus
    atmet."
    - Skizze RUNDE-42/finn-skizze-raute-20261004.png: Raute aus zwei Dreiecken mit gemeinsamer Kante, dicker Pfeil nach
      unten in der Mitte, aussen Pfeile nach oben, Eckkreise verschiedener Groesse.
  - Zwischen 18:16 und 18:19: "darin könnte im tetraeder eine kraft entstehen - eine große durhc das schanier und eine
    kleine an den außenrändern des nicht am schanier befindlichen punktes"
- **Schreibtisch der Leitung [M]:** RUNDE-42/SCHALTER-UND-ATMEN.md Teil E.
  - Gemittelte Huellen-Kopplung gibt psi_A = 0, psi_B = 120 Grad, psi_C = psi_D = 240 Grad.
  - Die Atemwellen der zwei Dreiecke laufen gegenlaeufig, auf der Scharnierkante beide nach unten (Finns Skizze).
  - Im Medium ziehen sich Gleichtakt-Paare an (C-D); 120-Grad-Paare stossen sich schwach ab.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Literatur, [H] Hypothese.

## Modell (Laengen in PU, Zeit in Takten)

- Vier Punkte A, B (Scharnier), C, D. Durchmesser d_i = 1 + eps sin(phi_i).
- Bindungen A-B, A-C, B-C, A-D, B-D: harmonisch, Ruhelaenge (d_i + d_j)/2 (sich beruehrende Huellen), Steifigkeit k.
  - Rest der Paare: Huellenabstossung bei Beruehrung.
  - C-D bindet, wenn sich die Huellen beruehren (Fangabstand delta_f).
- Phasen: phi_i' = omega - mu_phi dU/dphi_i + Rauschen (Huellen-Kopplung ueber die Bindungen, wie ATEM-NETZ-1).
- Medium (schaltbar): gemittelte Bjerknes-Kraft zwischen allen Paaren, Betrag B cos(phi_i - phi_j) / r^(D-1),
  gleichphasig anziehend.
- Lagen ueberdaempft: x_i' = mu_x F_i.
- Start:
  - 3D: Raute flach, Faltwinkel 180 Grad plus kleine Stoerung.
  - 2D-Kontrolle: in der Ebene, kein Falten moeglich.

## Ableitbarkeitsprobe (Leitung)

**Vorab ableitbar:**
- Phasenmuster der flachen Raute bei schwacher Kopplung (120 Grad, C = D).
- **Falten bei freiem Scharnier**, solange C und D im Gleichtakt bleiben und das Medium an ist: Das geht bergab. RA1 ist
  deshalb nur Kontrolle.
- **Kraefte im geschlossenen Tetraeder bei festen Phasen:** Das Stabwerk ist statisch bestimmt (6 Staebe, 4 Knoten).
  Jeder Stab traegt genau die Bjerknes-Paarkraft seines Paars:
  - C-D (Gleichtakt) Druck B.
  - alle 120-Grad-Staebe, auch das Scharnier, Zug B/2.
  - Damit sagt das einfache Modell bei festen Phasen das **Gegenteil** von Finns Kraftbild voraus: Die groesste Kraft
    sitzt im Schliessstab C-D, nicht im Scharnier.

**Nicht ableitbar:**
- Wie sich die Phasen nach dem Schliessen umordnen. Auf dem Tetraeder will die Huellen-Kopplung zwei Gegentakt-Paare.
- Ob sich die Raute dann wieder oeffnet: ein langsamer, selbst erzeugter Klapptakt.
- Wie die Kraefte im zeitlichen Mittel und als Wechselanteil wirklich verteilt sind.
- Was in 2D statt des Faltens geschieht.

## Messgroessen

- Faltwinkel theta(t) um AB und Abstand C-D.
- Schliess- und Oeffnungsereignisse, Dauer eines Klappzyklus in Takten.
- Phasendifferenzen aller Paare.
- **Stabkraefte je Kante:** zeitgemittelt und Wechselamplitude, Scharnier A-B gegen Aussenkanten A-C, B-C, A-D, B-D
  gegen C-D.
- Bilanz: Kraefte je Knoten summieren sich zu null (Werkzeugprobe).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RA0 | Kontrolle: ohne Medium flache Raute mit 120 Grad je Dreieck und C-D-Differenz < 0,1 rad; in 3D kein Falten (Winkelaenderung < 5 Grad in 200 Takten); Kraftbilanz je Knoten < 1e-6 | 85 % |
| RA1 | Kontrolle (ableitbar): mit Medium faltet die Raute in 3D, und C-D schliesst in <= 200 Takten | 80 % |
| RA2 | [H] Nach dem Schliessen ordnen sich die Phasen um, und die Raute oeffnet sich mindestens zweimal wieder in 500 Takten (selbst erzeugter Klapptakt) | 20 % |
| FP | [H, Finns Vorhersage] Im gefalteten bzw. geschlossenen Zustand traegt das Scharnier A-B die groesste zeitgemittelte Stabkraft (Betrag), und die Aussenkanten an C und D tragen die kleinsten | 25 % |

**Bedeutung (vorab):**
- **RA2 trifft ein:** Atmende Punkte erzeugen aus Gleich- und Gegentakt von selbst einen langsamen Klapptakt. Das waere
  ein "pumpendes Konstrukt" mit eigenem, langsamerem Takt [H].
- **RA2 verfehlt:** Das Tetraeder bleibt zu oder die Raute bleibt offen; kein zweiter Takt.
- **FP trifft ein:** Finns Kraftbild gilt, obwohl die einfache Statik bei festen Phasen das Gegenteil sagt. Der Grund
  waere die Phasenumordnung.
- **FP verfehlt:** Die groesste Kraft sitzt am Schliessstab bzw. aussen.

## Dimensionsvergleich (AGENTS.md)

- 2D: Die Raute kann nicht falten; dort C-D-Abstand, Stabkraefte und Phasen getrennt melden.
- 3D: Falten zum Tetraeder.
- Medium-Kraft 1/r^(D-1), also 1/r in 2D und 1/r^2 in 3D.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu5 (frei seit TAKT-RAND-4D-1). Je Lauf <= 10 min,
  1 Thread. Zeitbox 90 min.
- Parameter (eps, k, mu_phi, B, Rauschen, delta_f) im Plan begruenden. Fuer RA2 mindestens drei B-Werte und vier Saaten,
  vor dem Einfrieren festgelegt; nicht nach dem Befund nachregeln.
