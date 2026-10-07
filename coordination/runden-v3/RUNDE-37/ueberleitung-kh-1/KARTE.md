# UEBERLEITUNG-KH-1: Die Ueberleitung von der 4D-Zeit (Regime K) zu Finns stetigem Takt (Regime H): Welche Traegheit und welche Regeln folgen fuer kleine Zeltstangen? (Runde 49, Finns Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 13:15:27 CEST (date), vor jeder Rechnung.
- **Herkunft:** Finn, 05.10.2026, nach Fassung 2.4 der Grundgleichung, woertlich: "entwickle das weiter wo finden wir eine überleitung".
  - Lesart der Leitung: die Ueberleitung zwischen den zwei Regimen. Im Regime K (4D-Regge mit Zeltstangen) laufen lange Schwerewellen auf dem Kuhn-Gitter mit c und zwei Polarisationen; im Regime H (stetige Zeit, gesetzte Traegheit, Finns Takt) gab es bisher keine zugleich isotrope und stabile Paarung.
  - Die Bruecke ist der Grenzfall kleiner Zeltstangen: Er sollte aus der 4D-Wirkung die Traegheit (Bewegungsenergie) und die Regeln (Lapse aus der Zeltstangenhoehe, Shift aus ihrer Neigung, also auch D_v) liefern.
- **Projektbefunde [P]:**
  - REGGE-4D-1 (RUNDE-36): euklidische 4D-Regge-Hesse auf dem Kuhn-Gitter, Einsteins (1/4) k^2 (P2 - 2 P0) auf 0,04 %; fuenfte Nullmode (tote Hyperdiagonale).
  - REGGE-WELLE-1 (RUNDE-37): echte Zeit ueber komplexes k_tau auf dem Kuhn-Gitter; v -> 1, genau zwei laufende Moden (TT), kein Anwachsen; die drei Richtungen ohne zweite Zeitableitung sind Lapse und Shift.
  - REGIME-K-1: B1 ohne Fuellung, euklidisch, langwellig exakt einsteinsch; Zeltstangenhoehe wirkt in fuehrender Ordnung nur ueber die Metrik.
  - REGGE-KINETIK-L: Lund-Regge-Supermetrik (Hartle/Miller/Williams 1997, Gl. 3.5, 3.13) auf den Geschwindigkeiten; Regime H gegen K (Dittrich/Hoehn).
  - HODGE-MASSE-1, LUND-REGGE-MASSE-1: Regime H auf V, S, A15, Glas mit A1, A2, A2L (Lund-Regge) und den Reduktionen R1, RH, R2. Isotrop nur A2L mit RH, dort wachsende Moden; A2L mit R1 anisotrop; die Anisotropie unter R1 sitzt in der Partnerbedingung c^+ p = 0.
  - Regime H ist auf dem Kuhn-Gitter nicht gerechnet (Leitung, grep in den Rundentabellen nach "Kuhn" mit "A2L", "RH", "R1": kein Treffer; vom Agenten zu wiederholen).
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar bzw. bekannt [M, L]:**
  - Fuer gleichmaessige Zeltstangenhoehe h und Fourier in der Zeit gibt die 4D-Hesse im Grenzfall h -> 0 eine quadratische Form in omega: Der omega^2-Teil ist eine effektive Traegheit M_eff, der omega^0-Teil die raeumliche Steifigkeit. Lapse und Shift erscheinen als Richtungen ohne omega^2-Teil (REGGE-WELLE-1: "drei Richtungen ohne zweite Zeitableitung").
  - [L, ungeprueft] Die Lund-Regge-Supermetrik wurde aus dem 4D-Regge fuer duenne Schichten gewonnen. Dann ist M_eff = Lund-Regge naheliegend.
- **Nicht ableitbar:**
  - ob M_eff auf dem Kuhn-Gitter genau Lund-Regge ist (Interpolation von Lapse und Shift, Schichtaufbau)
  - welche Regeln (Reduktion) der Grenzfall vorgibt, und ob sie R1, RH oder etwas Drittes sind
  - ob Regime H mit M_eff und diesen Regeln auf dem Kuhn-Gitter isotrop und stabil ist
  - ob das R1-Problem (Anisotropie ueber c^+ p = 0) auch auf dem Kuhn-Gitter auftritt

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| UL0 | Kontrolle [P]: Auf dem Kuhn-Gitter gibt die 4D-Seite REGGE-WELLE-1 wieder (v bei |k| = 0,05 zwischen 0,9997 und 0,9999; zwei laufende Moden) | 85 % |
| UL1 | [L/H] Im Grenzfall h -> 0 ist die effektive Traegheit M_eff auf dem Kuhn-Gitter die Lund-Regge-Supermetrik (A2L), relativ auf 1e-6 | 55 % |
| UL2 | [H] Regime H mit M_eff und den Regeln, die der Grenzfall vorgibt, ist auf dem Kuhn-Gitter langwellig TT-isotrop (Spanne < 1e-6) und an allen gerechneten k ohne wachsende Mode | 55 % |
| UL3 | [H] Regime H auf dem Kuhn-Gitter mit Lund-Regge-Masse und R1 ist anisotrop (TT-Spanne > 1 %), wie auf V | 50 % |
| UL4 | [H] Regime H auf dem Kuhn-Gitter mit Lund-Regge-Masse und RH hat wachsende Moden, wie auf den Kristallen | 50 % |

**Bedeutung (vorab):**
- **UL1 und UL2 treffen ein:** Die Ueberleitung steht: Die richtige stetige Form von Finns Takt ist Lund-Regge plus die Regeln aus der 4D-Wirkung. Die Probleme im Regime H lagen dann an der Wahl der Regeln (R1, RH), nicht an der Traegheit. Die Grundgleichung bekaeme ihre Traegheit, ihren Lapse und ihre Verschiebungsregel D_v aus einem einzigen 4D-Ansatz.
- **UL1 verfehlt:** Die 4D-Wirkung verlangt eine andere Traegheit als Lund-Regge; sie ist dann zu benennen und auf V zu pruefen.
- **UL2 verfehlt, UL0 haelt:** Die stetige Grenze verliert, was die diskrete 4D-Zeit leistet. Dann ist die Ueberleitung selbst die Stelle, an der die Probleme entstehen (Zeitschritt nicht vernachlaessigbar).
- **UL3, UL4:** zeigen, ob die Probleme des Regimes H netzunabhaengig sind.

## Rahmen

- Code-Agent.
  - 4D-Seite: Code aus RUNDE-36/regge-4d-1/code und RUNDE-37/regge-welle-1/code (komplexes k_tau) kopieren.
  - H-Seite: Massen A2L (Lund-Regge) und Reduktionen R1, RH aus RUNDE-37/hodge-masse-1/code und RUNDE-37/lund-regge-masse-1/code, auf das 3D-Kuhn-Netz (Wuerfel in 6 Tetraeder) uebertragen. Dort nichts aendern.
  - Grenzfall: h-Folge (z. B. 1, 1/2, 1/4, 1/8) mit Extrapolation; Abbildung der 4D-Variablen (Kanten in der Zeitrichtung bzw. diagonal) auf Lapse, Shift und Kantenraten im Plan festlegen und begruenden.
- Literatur nur zur Einordnung (hoechstens 5 Abrufe): Hartle/Miller/Williams 1997 (Herkunft Lund-Regge), Dittrich/Hoehn 2010 bzw. 2013 (kovariant gegen kanonisch), Piran/Williams 1986. Kein Urteil haengt daran.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8, cpu9 und cpu10. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
