# KOLL-1 Ergebnis: kollektive Atmungswellen an der stillen Stelle (Runde 9)

- Bearbeiter: Code-Agent (Anthropic, Opus). Auftrag der Leitung 07:07; Plan PLAN.md ab 07:22:55 CEST (date), Nachtraege
  07:43:24. Ergebnis geschrieben ab 08:14 CEST (date).
- Rechnungen: .69, kleintest.sh, Spuren p4000a/p4000b, Ordner /home/fmh/fmhc-physics-remote/runde9-koll1/, Kopien in
  lauf-69/ (ohne Zustandsdateien). Lokal nur Rauchtests (lauf-lokal/).
- Belegstufen:
  - **Rechnung (a):** radiale 1D-Loesung plus 2D-Quadratur, ein Haus.
  - **Zeitlauf fein:** 2D achsensymmetrisch, h = 0,1, 4. Ordnung, eine Gitterstufe, sofern nicht anders gesagt.
  - **Rauchtest:** lokal, grobes Gitter, nicht belastbar.
  - Alles ist Modellrechnung ohne Messbezug; Deutungen sind als [H] markiert.

## Kurz

1. **(a) Die Kopplung ist stark und rein kurzreichweitig.**
   - J = -5,6e-3 / -1,65e-3 / -5,0e-4 bei d = 10 / 12 / 14 (still).
   - Volle Uebergabe nach 280 / 950 / 3150 Zeiteinheiten, das sind 80 / 260 / 870 Atemperioden.
   - Der offene Kanal traegt an der stillen Stelle ab d = 10 weniger als 3e-4 davon bei.
   - Bei 0,76 ist J um 40 % groesser, aber Gamma = 2e-3 frisst die Weitergabe ab d ~ 12 auf (Gamma/|J| = 0,25 / 0,82 / 2,7).
2. **Freie Baelle (nichtlinear, wie im Auftrag): Sie fliegen auseinander, bevor die Atmung ankommt.**
   - Der Abstand waechst von 10 auf 16,4 (t = 50) und 24,9 (t = 100).
   - Bei B kommen nur 8,6 % (still) bzw. 10,9 % (0,76) der Amplitude an. Die stille Stelle bringt hier keinen Vorteil.
   - Der Abstand traf die Vorhersage aus (a) auf 1 bis 5 %. Die Weitergabe blieb unter der Obergrenze aus (a)
     (0,086 gegen 0,107 still, 0,109 gegen 0,140 bei 0,76).
3. **Gehaltene Baelle (linear, eingefrorener Hintergrund, Zusatz der Bearbeitung):**
   - Frueh laeuft es wie in der Kopplungsmodentheorie: d = 14, t = 500, still: a/b = 0,973/0,230 gegen 0,969/0,247
     (CMT), Energie der Atmung 1,000.
   - Bei 0,76 sind im selben Paar nur noch 16 % der Energie uebrig, wie beim Einzelball.
   - Danach waechst jedes eingefrorene Paar weg, mit Raten 0,002 bis 0,08: gleich- und gegenphasig, auch im
     ungeraden Sektor; im groben Rauchtest auch mit Haltepotential.
   - Ein dauerhaftes Band ist damit **nicht entscheidbar**.
4. **Kontrollen:**
   - Einzelball still auf dem Gitter: |Gamma| < 2e-6 (obere Schranke; lin 7e-8, voll -1,2e-6).
   - Einzelball 0,76: 1,991e-3 bis 1,995e-3 (bic2-Pol 1,988e-3).
   - Ladung auf 1e-8 erhalten.
   - Hintergrundatmung entspricht eps = 7e-5 bei eps = 5e-3.
   - Grobes Gitter h = 0,15: freie Laeufe gleich auf unter 0,3 %.
5. **Zur Hypothese der Leitung [H]:**
   - Weg (i) ist bestaetigt: Ueberlapp, e^(-kappa_c d)/d, Vorzeichen negativ.
   - Weg (ii) faellt an der stillen Stelle weg; linear hat der Einzelball keinen Verlust.
   - Die "uebergeordnete Schwingung" scheitert aber an der Mechanik der Klumpen: Freie Baelle halten keinen Abstand,
     und eingefrorene Paare sind im Modell instabil.
   - Vorschlag: parken, bis es eine stabile Anordnung gibt (Gitter mit Rand oder Druck, periodische Kette,
     Mehrkomponenten-Bindung).

## (a) Kopplungsmodentheorie (lauf-69/aus-cmt; .69 P4000, 07:41:21 bis 07:42:08 CEST)

- **Profile:**
  - still: S0 = 1,049058, Schwanz A = 7,5183, Q = 189,1443 (Codex 189,144), E = 184,62
  - 0,76: S0 = 1,104389, A = 11,331, Q = 254,12, E = 241,90
- **Mode (max |u + v| = 1):**
  - still: N = 269,10, C_v = 15,149, K = 4 pi C_v^2/N = 10,72, offene Aussenamplitude 1,6e-7
    - An der stillen Stelle verschwinden die Wachstumskoeffizienten beider regulaeren Loesungen (bic2: W = 0).
    - Die Mode kommt deshalb aus dem kleinsten Singulaervektor; der erste Rauchtest ohne diese Korrektur gab eine falsche
      Mode.
  - 0,76 (Resonanzspitze rho_r = 1,72815): N = 524,1, C_v = 24,35, K = 14,22; Breite aus der Abtastung 2,07e-3
    (bic2 1,988e-3)
- **Formel:** J = t_AB/N, mit t_AB ~ -4 pi C_v^2 e^(-kappa_c d)/d. Asymptotik und volles 2D-Integral stimmen ab
  d = 10 auf 1 % ueberein (d = 10: -5,659e-3 gegen -5,629e-3).

| d | J still | t_tr still | J 0,76 | t_tr 0,76 | Gamma/\|J\| 0,76 | \|J_rad\| 0,76 | offener Kanal still | Delta/N gegenphasig still |
|---|---|---|---|---|---|---|---|---|
| 8 | -1,94e-2 | 81 | -2,67e-2 | 59 | 0,07 | 1,1e-4 | +3,5e-5 | +4,4e-3 |
| 10 | -5,63e-3 | 279 | -8,06e-3 | 195 | 0,25 | 8,6e-5 | +1,7e-6 | +1,8e-3 |
| 12 | -1,65e-3 | 950 | -2,41e-3 | 652 | 0,82 | 7,2e-5 | +7e-8 | +7,1e-4 |
| 14 | -4,99e-4 | 3148 | -7,36e-4 | 2133 | 2,7 | 6,2e-5 | +3e-9 | +2,6e-4 |
| 16 | -1,54e-4 | 10190 | -2,29e-4 | 6846 | 8,7 | 5,4e-5 | +1e-10 | +9,5e-5 |

- Gamma/|J| ist mit dem bic2-Pol 1,988e-3 gebildet. J_rad = Gamma/(qd) ist der Dicke-Anteil bei 0,76; an der stillen
  Stelle ist er null.
- **Vorzeichen:** t_AB < 0 fuer beide Phasenlagen. Die im chi-Bild symmetrische Paar-Mode liegt tiefer; bei
  Gegenphase heisst das im Dichtebild Gegentakt.
- **Gemeinsame Verschiebung Delta/N:** Sie ist so gross wie J/3, verstimmt aber beide Baelle gleich und stoert die
  Weitergabe im Paar nicht. In der Kette ist der Mittelball doppelt verschoben.
- **Abstossung, Mittelebenen-Spannung der Ueberlagerung:**
  - E_int gegenphasig = +1,54 / +0,53 / +0,19 bei d = 10 / 12 / 14 (still); gleichphasig -1,46 / -0,52 / -0,19.
  - Die Formel 8 pi A^2 e^(-k0 d)/d trifft auf 3 %.
  - Freie Bewegung aus der Ruhe, d0 = 10: d(50) = 16,6, d(100) = 25,7, Endgeschwindigkeit 0,18.
  - Das Integral |J| dt ergibt b_max frei ~ 0,107 (still) bzw. 0,140 (0,76).

## (b) Freie Baelle, voll nichtlinear (wie im Auftrag)

Aufbau:
- gegenphasig, d0 = 10, eps = 0,005 entlang der Mode an Ball A
- Stapel: Paar mit eps = 0, +eps, -eps; Einzelball an A's Ort mit 0, +eps, -eps
- lineare Antwort (phi_+ - phi_-)/(2 eps)
- Amplituden aus der Inversion der Ueberlappmatrix; Gewichte folgen den Baellen
- T = 200, h = 0,1

| Groesse | still 0,7976768 | 0,76 | Vorhersage (Nachtrag 2 bzw. a) |
|---|---|---|---|
| d(25) / d(50) / d(100) | 12,40 / 16,38 / 24,91 | 12,62 / 16,82 / 25,69 | still 12,28 / 16,56 / 25,65; 0,76 12,67 / 17,37 / 27,15 |
| b_max (Zeit) | 0,086 (t = 114, danach flach) | 0,109 (t = 79) | <= 0,11 bzw. <= 0,14 |
| Summe a^2 bei t = 200 (Paar) | 0,915 | 0,68 | - |
| Einzelball: Gamma, a(200) | -1,2e-6, 1,0003 | 1,991e-3, 0,779 | 0 bzw. 1,988e-3 |
| Ladung Einzelball Anfang -> Ende | 189,167961 -> 189,167963 | 254,14342 -> 254,14342 | erhalten |
| Ladungsasymmetrie durch Anregung (still) | -1,45e-2 (t = 25), -1,52e-2 (t = 100), waechst nicht | - | - |

- Die Uebertragung ist nach t ~ 70 praktisch abgeschlossen (b = 0,085), weil der Abstand dann ueber 19 liegt.
- Das Paar verliert an der stillen Stelle 8,5 % seiner Atmungsenergie, der Einzelball nichts. Der Linearfluss des
  Paares ist 57-mal groesser als der des Einzelballs. [H] Solange die Baelle nahe sind, verstimmt der Nachbar die stille
  Stelle; die Groessenordnung passt zu Delta/N ~ 2e-3.
- Hintergrundatmung des unangeregten Einzelballs: aequivalentes eps 6,9e-5 (still) bzw. 5,3e-5 (0,76). Beim Paar ist die
  Zahl (1e-2) durch die Drift verfaelscht und nicht verwertbar.

## (b) Gehaltene Baelle: linear, eingefrorener Hintergrund (Zusatz der Bearbeitung, nicht im Auftrag)

Stapel: Einzelball, Paare d = 10 / 12 / 14, Kette d = 10; Anregung der Mode an A, h = 0,1.

| Lauf (Ordner) | d = 14, t = 500: a / b | CMT fuer t = 500 | Wachstumsrate der Stoermode d = 10 / 12 / 14 | arg(b/a) frueh, d = 14 |
|---|---|---|---|---|
| still gegenphasig (aus-lin-still-fein) | 0,973 / 0,230 | 0,969 / 0,247 | 0,031 / 0,018 / 0,009 | -1,62 |
| still gleichphasig (-gleich) | 0,939 / 0,249 | 0,969 / 0,247 | 0,071 / 0,035 / 0,010 | -1,62 |
| 0,76 gegenphasig (aus-lin-076-fein) | 0,382 / 0,129 | 0,371 / 0,143 | 0,025 / 0,013 / 0,005 | -1,65 |
| 0,76 gleichphasig (-gleich) | 0,343 / 0,221 (schon gestoert) | 0,371 / 0,143 | 0,080 / 0,040 / 0,013 | -1,65 |
| still, ungerader Sektor (-ungerade) | a = -b: 0,502 (Start 0,5) | stabil | 0,029 / 0,014 / 0,002 | pi (erzwungen) |
| 0,76, ungerader Sektor (-ungerade) | a = -b: 0,205 (Einzelball 0,398 von 1) | ~ Einzelball | 0,024 / 0,009 / 0,0006 | pi (erzwungen) |

- **Frueh gilt die CMT:**
  - Bei d = 14 und t = 500 liegt der Uebergabewinkel atan(b/a) bei 0,232 (gegen) und 0,259 (gleich); CMT 0,250.
  - Das Mittel beider Phasenlagen trifft J auf 1,4 %.
  - Die Phase arg(b/a) = -1,62 bis -1,65 bestaetigt das Vorzeichen t_AB < 0 (Vorhersage -pi/2 = -1,571).
- **Verlust frueh (d = 14, t = 500):**
  - still: Summe a^2 = 1,000 (gegenphasig)
  - 0,76: 0,163, wie beim Einzelball (0,158)
  - Der ungerade Sektor bei 0,76 klingt wie der Einzelball ab (0,41 gegen 0,40 relativ). Die kollektive Mode bei 0,76 ist
    also nicht geschuetzt.
- **Spaeter waechst in allen eingefrorenen Paaren und Ketten eine Stoermode.** Der Einzelball im selben Stapel bleibt
  stabil.
  - Die Raten fallen mit d.
  - Bei Gegenphase liegen die Raten bei d = 10 und 12 nahe sqrt(2 |d omega/dQ| E0) = 0,031 / 0,019 (Josephson-artiger
    Phasen-Ladungs-Austausch; d omega/dQ aus den zwei Profilen, Hand, grob; E0 aus (a)).
    - Die Stoermode bei d = 10 liegt aber im ungeraden Sektor: Mit und ohne Projektion hat sie bei t = 500 dieselbe
      Amplitude 337.
    - Die relative Phase des Gegenphasen-Paars waere gerade. Die Zuordnung ist also offen; die Naehe der Zahlen kann
      Zufall sein.
  - Die Demodulationsphase zeigt niederfrequente Moden, die in das Atmungsfenster durchsickern, keine Atmungsmode.
  - Ein Haltepotential V = R/F macht den Hintergrund exakt stationaer; im lokalen Rauchtest (h = 0,3) wuchs trotzdem eine
    Mode (0,008). Das ist nicht belastbar.
  - [H] Der eingefrorene Ueberlagerungs-Hintergrund ist keine Loesung, und seine Hesse-Form hat Richtungen, die der echte
    Ball-Zustand nicht hat (Phase/Ladung, Lage). Nicht geklaert.
- **Folge:** Die langfristigen Aussagen (volle Uebergabe, Verlust je Uebergabe, Kette) sind **nicht entscheidbar**. Belegt
  ist nur die fruehe Phase bis t ~ 500 bei d = 14.

## (c) Kette aus drei

- Nur im eingefrorenen Stapel gerechnet (Zusatz). Sie waechst noch schneller weg (0,038 gegen- bzw. 0,082 gleichphasig,
  still). Nicht entscheidbar.
- Die CMT sagt voraus (Hand):
  - A -> C nach pi/(sqrt 2 |J|) = 395 bei d = 10 (still)
  - Der Mittelball ist um Delta/N ~ 1,8e-3 verstimmt; das ist klein gegen |J| = 5,6e-3.

## Kontrollen

- **Einzelball im selben Stapel wie die Paare:**
  - still: Gamma 8e-8 / 7e-8 / 7e-8 (lin) und -1,2e-6 (voll)
  - 0,76: 1,995e-3 (lin) und 1,991e-3 (voll)
  - Das Gitter bildet die stille Stelle ab: Gamma still ist mindestens 1000-mal kleiner als bei 0,76 (obere Schranke 2e-6).
- **Ohne Anregung (eps = 0):**
  - Einzelball ortsfest (z = -5,000000), Ladung auf 1e-8 erhalten
  - Das Paar driftet wie in (a) vorhergesagt.
- **Zwei Gitterstufen (freie Laeufe, h = 0,15 gegen 0,10; aus-voll-*-grob, 08:10:37 bis 08:15:25 CEST):**

  | Groesse | still grob / fein | 0,76 grob / fein |
  |---|---|---|
  | b_max (Zeit) | 0,0859 (114) / 0,0859 (114) | 0,1089 (79) / 0,1090 (79) |
  | d(25) / d(50) / d(100) | 12,372 / 16,353 / 24,930 gegen 12,396 / 16,384 / 24,913 | 12,589 / 16,798 / 25,712 gegen 12,618 / 16,819 / 25,694 |
  | Summe a^2 Paar bei t = 200 | 0,9141 / 0,9148 | 0,6814 / 0,6816 |
  | Gamma Einzelball | -1,10e-6 / -1,17e-6 | 1,987e-3 / 1,991e-3 |
  | Linearfluss Paar / Einzel (2. Haelfte) | 0,132 / 0,0023 gegen 0,129 / 0,0023 | 2,40 / 3,16 gegen 2,41 / 3,17 |
  | Hintergrundatmung (aequivalentes eps) | 1,5e-4 / 6,9e-5 | 1,2e-4 / 5,3e-5 |

  - Die Aussagen der freien Laeufe haengen nicht vom Gitter ab (Unterschiede unter 0,3 %).
  - Die Hintergrundatmung skaliert etwa wie h^2, also wie der Zeitschritt; der Leapfrog-Fehler ist die Quelle.
  - Die lin-Laeufe gibt es nur fein; wegen der Stoermoden war eine grobe Stufe dort nicht mehr sinnvoll.
- **Ladungsasymmetrie durch die Anregung (frei):** still -1,4e-2 bis -1,5e-2, 0,76 -2,6e-2 bis -3,5e-2, zwischen t = 25 und
  100 fast konstant. Kein wachsender Ladungsaustausch in der echten Dynamik; [H] das ist die Ladung zweiter Ordnung der
  Anregung.
- **Uebersprechen der Messgewichte:** 1,4 % bei d = 10 (still), 2,2 % (0,76), per Matrixinversion entfernt.

## Vorab gegen Ausgang

| Vorab (PLAN, Zeit) | Ausgang | Urteil |
|---|---|---|
| K ~ 2 (0,5 bis 6), \|J\|(10) ~ 1e-3 innerhalb Faktor 4 (07:22:55) | K = 10,7; \|J\|(10) = 5,6e-3 | verfehlt (Faktor 5,6; Anschlussradius und v/u unterschaetzt) |
| t_tr(10) 400 bis 6000 | 279 | verfehlt |
| \|J_ev\|(0,76)/\|J_ev\|(still) 1,0 bis 1,3 | 1,43 bis 1,48 | knapp verfehlt |
| E1 still gehalten: B >= 0,9, Verlust je Uebergabe < 1 % | frueh verlustfrei (Summe 1,000 bei t = 500, d = 14); volle Uebergabe nicht erreicht (Stoermode) | nicht entscheidbar |
| E1 0,76 gehalten: B <= 0,3 (d = 10), <= 0,1 (d = 12, 14) | CMT mit dem neuen J: 0,68 / 0,37 / 0,13; im Lauf nicht messbar (Stoermode) | nicht entscheidbar; mit dem gemessenen J waere das Vorab bei allen drei Abstaenden verfehlt (0,68 / 0,37 / 0,13) |
| E2 t_AB < 0, arg(b/a) = -pi/2 | (a): negativ. Zeitlauf d = 14: -1,62 bis -1,65 in vier Laeufen | getroffen |
| E3 freie Baelle: E_int(12) 0,04 bis 1; v_end 0,03 bis 0,15; Abstand +2 in 30 bis 150; b_max frei <= ~0,1, still ~ 0,76 | E_int(12) = 0,53; v_end 0,107; +2,4 bis t = 25; b_max 0,086 und 0,109 (d0 = 10) | getroffen |
| E4 Kette: C >= 0,85 nach ~395 | Kette waechst weg | nicht entscheidbar |
| E5 Einzelball still: Gamma < 1e-4 grob, < 1e-5 fein; 0,76 1,99e-3 +- 15 % | fein 7e-8 bis 1,2e-6 (Betrag), grob 1,1e-6; 0,76: 1,987e-3 bis 1,995e-3 | getroffen |
| E5 Hintergrundatmung < 1e-3 der Anregung | 1,4e-2 (eps 6,9e-5 gegen 5e-3) | verfehlt; fuer die Differenzmethode unerheblich |
| E5 Ladung auf 1e-4 | 1e-8 | getroffen |
| Nachtrag 2: freie Abstaende auf 10 % | 1 bis 5 % | getroffen |
| Nachtrag 2: b_max frei <= 0,11 / <= 0,14 | 0,086 / 0,109 | getroffen |
| Nachtrag 2: gehalten, J aus der Zeitreihe auf 15 % | d = 14 frueh: -7 % / +4 % (still), -11 % (0,76 gegen); spaeter gestoert | teilweise (nur d = 14 frueh) |

## Grenzen

- Das Atmungsmodell ist die lineare l = 0-Mode. Die Nachbarn regen im Paar auch l = 1 an (der Nachbarschwanz wirkt als
  Dipol); nicht untersucht.
- Die freie Rechnung hat zwei Gitterstufen (h = 0,1 und 0,15). T = 200 reicht, weil die Baelle danach weit getrennt
  sind.
- Die eingefrorenen Laeufe modellieren gehaltene Baelle nicht verlaesslich (Stoermoden). Ein physikalisch sauberes
  "Halten" (Falle, Gitter unter Druck, periodische Kette mit Abstossung) ist nicht gerechnet.
- Codex' Hierarchie-Modelle (hierarchy-memory-20260930) sind nicht gedoppelt; gelesen wurde nur die Dateiliste.

## Dateien

- PLAN.md (Vorab 07:22:55, Nachtraege 07:43:24), koll1.py, ERGEBNIS.md
- lauf-69/: aus-cmt, aus-lin-*-fein (gegen), -gleich, -ungerade, aus-voll-*-fein, aus-voll-*-grob, LAUF-*.log
- lauf-lokal/: Rauchtests

## Regelhinweis

- 08:14 lief lokal einmal ein leerer Aufruf `python3 -` (leerer Heredoc) vor einem sed-Befehl. Das war ein Versehen in
  der Befehlszeile; gerechnet wurde nichts. Sonst lokal nur Rauchtests nach Auftrag.

## Einfach gesagt

Zwei Q-Baelle koennen ihr Pulsieren tatsaechlich aneinander weitergeben, und zwar ueber ihre Raender. An der stillen
Stelle geht dabei in der Rechnung fast nichts als Welle verloren, anders als bei 0,76. Das Problem ist die Mechanik:
Zwei gegenphasige Baelle stossen sich so stark ab, dass sie weggeflogen sind, bevor mehr als etwa ein Zehntel des
Pulsierens beim Nachbarn ankommt. Haelt man die Baelle kuenstlich fest, stimmt die Weitergabe am Anfang genau mit der
Formel, aber die festgehaltene Anordnung wird nach einiger Zeit selbst instabil. Ein "Band" uebergeordneter
Schwingungen braeuchte also zuerst eine Anordnung, in der die Klumpen von selbst an ihrem Platz bleiben.
