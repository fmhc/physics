# LICHT-FINN-NETZ-1: Wie stark weicht das Lichttempo auf Finns regelmaessigem Tetraeder-Netz bei kurzen Wellen ab, und wie fein muss die Masche dann sein? (Runde 43, messnah)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 19:47:40 CEST (date), vor jeder Rechnung.
- **Finn (19:28 bis 19:31):** "der raum ist das netz"; dazu "weiter rechnen" (zwischen 19:38 und 19:40).
- **Herkunft:**
  - STRICH-NETZ-1: Zufallsnetz, Weyl 1 - 0,117 k^2, FEM 1 - 0,022 k^2.
  - WEYL-LINEAR-1: kein lineares Glied im Mittel; quadratischer Anker l < 5,9e-28 m.
  - STRANG-ANKER-L: LHAASO E_QG,2 > 6,9e11 GeV, E_QG,1 > 1,0e20 GeV.
  - Fuer Finns **regelmaessiges** Netz (Diamant bzw. Pyrochlor) fehlen die Zahlen: Gitter mit kubischer Symmetrie haben
    eine richtungsabhaengige k^2- bzw. k^4-Abweichung.
- Kennzeichen: [M], [E], [S], [P], [H].

## Ableitbarkeitsprobe

**Vorab ableitbar [M]:**
- Bei kubischer bzw. tetraedrischer Symmetrie ist die lineare Geschwindigkeit eines einzelnen Kegels isotrop (ein
  Tensor 2. Stufe ist dort proportional zur Einheit).
- Die Abweichungen sind Fourier-Rechnungen eines gegebenen Operators.

**Nicht vorab bekannt:** die Zahlenwerte der k^2-Koeffizienten (und ihrer Richtungsabhaengigkeit) fuer die Operatoren auf
Finns Netz und die daraus folgende Maschen-Schranke. Das ist eine Rechnung, keine Vorhersagepruefung; die Vorhersagen
unten betreffen nur Groessenordnungen.

## Auftrag (Code-Agent)

1. **Operatoren auf Finns Netz** (Diamant-Knoten = Tetraedermitten; Pyrochlor = Ecken), Kantenlaenge 1 PU:
   - (a) Skalar-Wellengleichung mit FEM- bzw. patch-test-konsistenten Gewichten
   - (b) Weyl-Operator bzw. Weyl-Quantenautomat auf dem Diamant-Netz, falls im Projekt vorhanden (QCA-DIAMANT-4, per grep;
     nur kopieren)
   - (c) Maxwell auf Kanten (Whitney-Formen bzw. Coulomb-Phase) als Licht im engeren Sinn, wenn in 90 min machbar
2. **Dispersion:** omega(k)/(c k) = 1 + a2(n) (k l)^2 + a4(n) (k l)^4 je Richtung n (26 Richtungen); a2 und a4 mit
   Richtungsmittel und Spannweite.
3. **Bedingte Schranke** ("wenn das Netz das Licht traegt"): Maschenweite l aus LHAASO E_QG,2 > 6,9e11 GeV (Umrechnung
   wie WEYL-LINEAR-1/STRANG-ANKER-L, nachrechnen); Richtungsabhaengigkeit als Doppelbrechungs- bzw. Richtungsanker
   nennen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LF0 | Kontrolle: Langwelliges Tempo isotrop (Spannweite < 1e-6) fuer alle gerechneten Operatoren; kubisches Z^3-Gitter als Probe gibt a2 = -1/24 je Achse | 85 % |
| LF1 | [H] Auf Finns Netz liegt abs(a2) im Richtungsmittel zwischen 0,01 und 0,2 (also in der Groessenordnung des Zufallsnetzes) | 60 % |
| LF2 | [H] Die Richtungsabhaengigkeit von a2 betraegt mehr als 10 % des Mittels (sichtbare Anisotropie bei kurzen Wellen) | 50 % |

**Bedeutung (vorab):**
- Die Rechnung gibt eine bedingte, messnahe Schranke fuer Finns Maschenweite: Wenn das Netz das Licht traegt, muss die
  Masche unter einem Wert liegen, den LHAASO setzt.
- **LF2 trifft ein:** Finns regelmaessiges Netz haette eine Vorzugsrichtung fuer kurze Wellen; Gammablitze aus
  verschiedenen Himmelsrichtungen waeren ein zusaetzlicher Test [H].

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu4 und cpu11 (frei seit DIM-LEITER-QBALL-1). Je Lauf <= 10 min,
  1 Thread. Zeitbox 90 min.
