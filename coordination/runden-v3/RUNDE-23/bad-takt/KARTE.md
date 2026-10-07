# BAD-TAKT: Synchronisiert die Strahlung der anderen Uhren, oder treibt sie Vergroeberung? (Runde 23, Finns Frage)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 22:02:12 CEST (date), vor jedem Lauf.
- Finn ~22:05: "syncronisieren sich die uhren ueber zeit durch die allgemeine strahlung die die anderen uhren abgeben?
  ploppen die uhren in eine groesse in der sie sich stabil halten oder so?"
- Herkunft:
  - SCHWEBUNGSUHR (R23): Nah beieinander frisst der Grosse den Kleinen; schwach gekoppelt laufen die Takte auseinander.
  - Schreibtisch der Leitung (RUNDE-23.md, 22:0x): omega = dE/dQ ist das chemische Potential, und stabile Baelle haben
    dQ/domega < 0. Ladung fliesst deshalb vom kleinen (hohes omega) zum grossen Ball, und der Unterschied waechst
    (Ostwald-Reifung).
- **Schreibtisch-Vorhersage zu Finns "stabiler Groesse" [H]:** Ein gemeinsames Strahlungsbad mit chemischem Potential mu
  wuerde alle Baelle zu omega = mu ziehen, also synchronisieren. Dieses Gleichgewicht ist fuer stabile Baelle aber selbst
  instabil: Ein etwas groesserer Ball hat ein kleineres omega, nimmt mehr auf und waechst weiter. Erwartet wird deshalb
  Vergroeberung (der groesste gewinnt), nicht Synchronisation.
- Ableitbarkeitspruefung: Mehrere angeregte Q-Baelle in einer reflektierenden Box (gemeinsames Strahlungsbad) wurden im
  Projekt nicht gerechnet.
- Explorativ (v3), Hypothesen [H]. Laeufe je <= 10 min (lange Zeiten in Abschnitten).

## Test

- M1 in 1D, Code der SCHWEBUNGSUHR (RUNDE-23/schwebungsuhr/code/schwebung1d.py) als Grundlage.
- Drei Q-Baelle mit omega^2 = 0,58, 0,62, 0,66, weit getrennt (Abstand mindestens wie der schwach gekoppelte Zusatzlauf, ~15).
  Jeder angeregt mit Amplitude x 1,05, damit er atmet und strahlt.
- Zwei Arme:
  - **Bad:** Rand reflektierend (Dirichlet ohne Absorber); die Strahlung bleibt als gemeinsames Bad in der Box.
  - **Kontrolle:** Rand absorbierend; die Strahlung verlaesst die Box.
- Zeit bis T = 6000 (in Abschnitten), zwei Gitter fuer den Bad-Arm.
- Messgroessen je Ball:
  - omega_i(t) aus der Phasendrehung am Zentrum
  - Q_i(t)
  - Atmungsamplitude
  - Spreizung Delta = max omega_i - min omega_i ueber die Zeit
  - die Ladung im Bad (Gesamtladung minus Ballladungen)

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| BT1 | Bad-Arm: Die Spreizung Delta waechst bis T = 6000 (keine Synchronisation) | 65 % |
| BT2 | Bad-Arm: Der groesste Ball (kleinstes omega) gewinnt Ladung, der kleinste verliert, auf beiden Gittern | 65 % |
| BT3 | Kontrolle: Jedes omega_i aendert sich bis T = 6000 um < 1 % | 60 % |
| BT4 | Bad-Arm: Kein Ball "ploppt" in eine gemeinsame Groesse; die Spreizung faellt zu keiner Zeit unter die Haelfte des Anfangswerts | 75 % |

**Bedeutung (vorab):**
- BT1, BT2 und BT4 treffen ein: Die Strahlung der anderen Uhren synchronisiert nicht, sie treibt Vergroeberung (der groesste
  Ball waechst), wie die Schreibtisch-Ueberlegung sagt. Eine gemeinsame Zeit bleibt am Ende nur als die eines einzigen
  Balls [H, 1D].
- BT1 oder BT4 trifft nicht ein: Es gibt eine Synchronisation ueber das Bad; Mechanismus beschreiben. Das widerspraeche der
  Schreibtisch-Ueberlegung.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren), je <= 10 min.
- Plan vor dem ersten echten Lauf einfrieren. Zeitbox 75 min. Danach ein kurzer Literaturcheck (Q-Baelle im Bad,
  chemisches Gleichgewicht omega = mu, Verdampfen bzw. Wachstum; z. B. Laine/Shaposhnikov) als L4.

## Nachtrag der Leitung vor jedem Lauf (2026-10-02 22:29:33 CEST)

- **Anlass:** Gegenlesen von SCHWEBUNGSUHR-2, nach dem Schreiben dieser Karte (RUNDE-23.md).
  - Q_i(t = 0) ist ein Extremwert des Josephson-Pendelns. Ein Vergleich "Ende gegen t = 0" misst deshalb den Versatz der
    Startphase, keine Drift.
- **Messregeln** (gelten fuer BT1 bis BT4):
  - Alle Groessen, auch die Spreizung Delta, als Fenstermittel.
  - Jedes Fenster ist mindestens zwei Schwebungsperioden der langsamsten Paarung lang, das erste beginnt fruehestens bei
    t = 100.
  - "Waechst" heisst: Das letzte Fenster vor T liegt ueber dem ersten. "Gewinnt/verliert" ist ebenso definiert.
- **Startphasen:** zwei Phasensaetze, (0, 0, 0) und (0, 2/3, 4/3) mal pi.
  - BT1, BT2 und BT4 gelten nur, wenn sie fuer beide Phasensaetze eintreffen. BT3 gilt fuer den Kontrollarm mit Phasensatz
    (0, 0, 0).
  - Das zweite Gitter wird nur fuer Phasensatz (0, 0, 0) gerechnet.
- Die Vorhersagen BT1 bis BT4 und die Wahrscheinlichkeiten bleiben unveraendert.
