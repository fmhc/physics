# TAKT-RAND-4D-1: Traegt der 3D-Rand eines getakteten 4D-Netzes ein ungepaartes Weyl-Teilchen? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 17:31:03 CEST (date), vor jeder
  Rechnung.
- **Herkunft:**
  - DREIECK-TAKT-1 (RUNDE-37/qca-windung-1/teil2-dreieck-takt/ERGEBNIS.md): In 2D gibt Finns Dreiecks-Takt einseitige
    Randwellen; in 3D hat jeder streng lokale Takt W3 = 0 (K-Theorie-Argument, ungeprueft).
  - Finns Fragen zu Takt und Haendigkeit sowie "4D in 3D" (RUNDE-41.md und RUNDE-42.md).
  - CHIRAL-L: "Platte in einer 4. Raumrichtung" als Ort der Anomalie.
- **Idee [H]:** Wie die 1D-Randwelle am 2D-Takt-Netz koennte der 3D-Rand eines getakteten 4D-Netzes ein ungepaartes
  Weyl-Teilchen tragen. Das waere die Floquet-Fassung der Domain-Wall-Fermionen (Kaplan 1992); die Haendigkeit sitzt
  dann am Rand, nicht im lokalen 3D-Takt.
- **Ableitbarkeitsprobe:**
  - In 2D sind anomale Floquet-Phasen (Rudner/Lindner/Berg/Levin 2013) und ihre Randwelle bekannt; das ist eine
    Kontrolle.
  - In 4D ist die passende Invariante vermutlich eine Windung von U(k, t) ueber Zone und Takt [L?, an der Quelle
    pruefen].
  - Ob ein konkreter, streng lokaler 4D-Schrittplan einen 3D-Rand mit ungepaartem, isotropem Kegel gibt, ist nicht
    ableitbar.
  - Projekt-grep: keine 4D-Takt-Rechnung.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Literatur, [S] Quelle, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Literatur (hoechstens 3 Abrufe):** hoeherdimensionale anomale Floquet-Phasen bzw. Floquet-Systeme mit
   Weyl-Randzustaenden; Invariante, Beispielmodell.
2. **Bau:**
   - Kontrolle in 2D: Rudner-Modell (Schrittplan auf dem Quadratgitter) mit einseitiger Randwelle.
   - In 4D: ein streng lokaler Schrittplan auf einem 4D-Gitter (Platte: drei Richtungen periodisch, eine endlich), z. B.
     die 4D-Verallgemeinerung des Rudner-Plans bzw. das Modell aus der Literatur.
3. **Messgroessen:**
   - Quasienergie-Spektrum der Platte gegen den 3D-Impuls.
   - Randzustaende je Rand; Zahl und Chiralitaet der Weyl-Kegel je Rand und Quasienergie-Luecke.
   - Isotropie des tiefsten Kegels.
   - Kontrolle: Der gegenueberliegende Rand traegt die entgegengesetzte Chiralitaet.
4. Plan, Rauchlauf, Einfrieren wie ueblich. Code aus RUNDE-37/qca-windung-1/teil2-dreieck-takt/code/ wiederverwenden
   (nur kopieren).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TR0 | Kontrolle: 2D-Rudner-Modell mit einseitiger Randwelle; die Netto-Randfluesse beider Raender sind entgegengesetzt gleich | 90 % |
| TR1 | [H] Ein streng lokaler 4D-Schrittplan wird gebaut, dessen 3D-Rand je Rand eine ungerade Zahl von Weyl-Kegeln bei einer Quasienergie traegt (Netto-Chiralitaet ungleich 0; am Gegenrand umgekehrt) | 30 % |
| TR2 | [H] Wenn TR1: Der tiefste Randkegel ist isotrop auf 10 % | 30 % |

**Bedeutung (vorab):**
- **TR1 trifft ein:** Ein getaktetes 4D-Netz kann an seinem 3D-Rand ein einzelnes links- oder rechtsdrehendes Teilchen
  tragen. Die Haendigkeit sitzt im Takt der vierten Richtung [H].
- **TR1 verfehlt:** Auch am Rand eines Takt-Netzes kein ungepaartes Weyl-Teilchen; der Takt-Weg zur Haendigkeit ist dann
  in dieser Form zu.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu5 (frei seit KOPPLUNG-TETRA-1). Je Lauf
  <= 10 min, 1 Thread. Zeitbox 150 min.
