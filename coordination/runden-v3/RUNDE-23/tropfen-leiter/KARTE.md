# TROPFEN-LEITER: Hat die Wand eine stille Frequenz? Q-Ball-Wand und Quantentropfen-Oberflaeche (Runde 23)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 22:58:18 CEST (date), vor jeder Rechnung und vor
  jedem Literaturabruf.
- Finn, ~22:45: "mach weiter, nimm die quantentropfen dazu" (Punkt 2 der Rangfolge in RUNDE-23/IDEEN-LOGIK-TEILCHEN.md).

## Herkunft und Schreibtisch

- **Rohdaten der Leitern** (Leitung, 22:5x, aus Dateien gelesen):
  - 2D, RUNDE-12/leiter2d-praez/ERGEBNIS.md: n = 7 bei eps = omega^2 - 1/2 = 0,0292654 mit rho* = 1,556457; n = 8 bei
    0,025780 mit rho* = 1,55299.
  - 3D, RUNDE-13/leiter3d-praez/ERGEBNIS.md: n = 7 bis 10 bei eps = 0,0598482 / 0,0526191 / 0,0469399 / 0,0423644 mit
    rho* = 1,58992 / 1,58271 / 1,57693 / 1,57218.
  - Lineare Extrapolation eps -> 0: 2D ergibt 1,5273 (Steigung 0,995). 3D aus den letzten zwei Sprossen ergibt 1,5282
    (Steigung 1,00 bis 1,04, leicht gekruemmt).
  - **Beide Dimensionen laufen auf denselben Grenzwert rho_inf ~ 1,5275 zu.**
- **Abstand:**
  - Das Papier (Abschnitt "thin-wall phase-matching") hat b_inf = 2 sqrt(beta) pi/k_inf mit
    k_in^2 = omega^2 + rho^2 - 3/2 + sqrt(4 omega^2 rho^2 + 1).
  - Bei rho = 1,5275 und omega^2 = 1/2 ist k_in = 1,9271 und b_inf = 2,3055. Die beobachteten 3D-Schritte (n = 12 bis 15)
    sind 2,3043 / 2,3053 / 2,3068.
- Das Papier schreibt: "The coupled planar wall problem has not been solved here."
- **Hypothese [H]:** Die stillen Sprossen sind Fabry-Perot-Resonanzen einer Wand, die bei einer Frequenz rho_z gar nicht
  durchlaesst (Transmissionsnullstelle, Fano-artig).
  - Der Grenzwert ist dimensionsunabhaengig, weil die ebene Wand in jeder Dimension dieselbe ist.
  - Zaehlung:
    - Auf jeder Seite der Wand gibt es einen offenen und einen geschlossenen Kanal; die Gleichungen sind reell
      (Zeitumkehr).
    - Eine Totalreflexion verlangt eine reelle Bedingung, also gibt es isolierte Nullstellen in der Frequenz.
- **Uebertragung auf Quantentropfen** [L?: Petrov 2015 fuer 3D, Petrov/Astrakharchik 2016 fuer 1D]:
  - Die Oberflaeche zwischen Fluessigkeit und Vakuum hat dieselbe Kanalstruktur.
    - Innen: Bogoliubov-Phonon (laufend) plus abklingende Mode.
    - Aussen: freie Atome (u, offen oberhalb |mu|) plus v (geschlossen).
  - Eine Transmissionsnullstelle omega_z hiesse: An dieser Frequenz verdampfen Oberflaechen-Phononen keine Atome.
  - Grosse Tropfen haetten dann bei bestimmten Atomzahlen stille Moden [H].
- **Ableitbarkeitspruefung:**
  - Die ebene Wand ist im Projekt nicht gerechnet (das Papier sagt es selbst).
  - Die Lage rho_z ist nur extrapoliert; die ebene Rechnung kann davon abweichen.
  - Tropfen-Oberflaechen wurden im Projekt nie gerechnet.

## Test (Leitung rechnet selbst; ein Skript, drei Modelle)

Ebene Wand, Frequenz reell, zwei Komponenten:

| Modell | Hintergrund (Knick) | Innen | Aussen offen / geschlossen |
|---|---|---|---|
| M1, omega^2 = 1/2 (relativistisch) | S = f^2 = 1/(1 + e^(sqrt2 x)) | S = 1 | B mit (rho + omega)^2 > 1 / A mit (rho - omega)^2 < 1 |
| Tropfen 1D: i psi_t = -psi_xx/2 + abs(psi)^2 psi - abs(psi) psi | phi = (2/3)/(1 + e^(2x/3)), mu0 = -2/9 | n0 = 4/9, c = 1/3 | u fuer omega > 2/9 / v |
| Tropfen 3D (LHY, ebene Wand): i psi_t = -lap psi/2 - 3 abs(psi)^2 psi + (5/2) abs(psi)^3 psi | phi' = -phi(1 - phi) sqrt(1 + 2 phi), mu0 = -1/2 | n0 = 1, c = sqrt3/2 | u fuer omega > 1/2 / v |

- **Verfahren:**
  - Aussen mit der rein abklingenden Loesung des geschlossenen Kanals starten und nach innen integrieren.
  - Innen auf die Moden der konstanten Innenmatrix zerlegen: c(Frequenz) ist der Anteil der ins Innere wachsenden
    abklingenden Mode.
  - c = 0 ist eine Transmissionsnullstelle.
  - Zur Kontrolle |t|^2 aus der Streuloesung (Flussbilanz |r|^2 + |t|^2 = 1).
  - Zwei Schrittweiten bzw. Toleranzen und zwei Gebietslaengen.
- **Fenster:**
  - M1: rho in (1 - omega, 1 + omega) = (0,293; 1,707). Dort ist ein Kanal offen, einer geschlossen.
  - Tropfen 1D: omega in (2/9; 2).
  - Tropfen 3D: omega in (1/2; 4).
- **K0:**
  - Der Hintergrund-Knick erfuellt die stationaere Gleichung (Rest < 1e-8).
  - Die Innen-Dispersion trifft die Bogoliubov- bzw. Papier-Formel.
  - Die Flussbilanz stimmt auf 1e-8.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TR0 | M1: genau eine Nullstelle von c in rho in [1,45; 1,65], bei rho_z = 1,5275 +- 0,002, und dort abs(t)^2 < 1e-6 | 70 % |
| TR1 | Tropfen 1D: mindestens eine Nullstelle im Fenster (2/9; 8/9) | 50 % |
| TR2 | Tropfen 3D (LHY): mindestens eine Nullstelle im Fenster (1/2; 2) | 50 % |
| TR3 | Stufe 2, nur wenn TR1 eintrifft, spaeter: Endliche 1D-Tropfen haben V-foermige Breitenminima in N; der Abstand je Paritaet liegt innerhalb 25 % von 2 pi n0/k_in(omega_z) | 45 % |

**Bedeutung (vorab):**
- **TR0 trifft ein:**
  - Der Mechanismus der Leiter ist eine Transmissionsnullstelle der ebenen Wand plus Fabry-Perot [H, M1].
  - Der offene Punkt des Papiers ("planar wall problem") ist numerisch geloest. Damit folgen rho_inf und der Abstand ohne
    Eichung.
- **TR0 trifft nicht ein:** Der Mechanismus ist ein anderer, etwa eine wesentliche Kruemmung oder keine ebene Nullstelle.
  Beschreiben; die Tropfen-Uebertragung ist dann geschwaecht.
- **TR1 oder TR2 trifft ein:**
  - Die Tropfen-Oberflaeche hat eine stille Frequenz omega_z, an der Oberflaechen-Phononen keine Atome verdampfen.
  - Grosse Tropfen haetten bei diskreten Atomzahlen nicht verdampfende Moden [H]. Das ist ein Entwurf fuer einen
    Messvorschlag, kein Befund.
- **TR1 und TR2 treffen nicht ein:** Im Fenster haben die Tropfenmodelle keine stille Oberflaeche.

## Literatur: Erwartung vor dem Abruf

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| E1 | Tylutki/Astrakharchik/Malomed/Petrov 2020 (1D-Tropfen, kollektive Anregungen) existiert und zeigt Moden, die mit fallendem N ins Kontinuum laufen | 85 % |
| E2 | Petrov 2015 beschreibt "self-evaporation" fuer 3D-Tropfen unterhalb N ~ 94 (Petrov-Einheiten) | 80 % |
| E3 | Keine Arbeit berichtet exakt stille Moden (BIC) von Quantentropfen oder eine Transmissionsnullstelle der Tropfenoberflaeche | 65 % |
| E4 | Es gibt Theorie zur Phonon-Atom-Umwandlung an der freien Oberflaeche von He-4 ("quantum evaporation") | 90 % |
| E5 | Diese He-4-Theorie zeigt eine Nullstelle oder ein scharfes Minimum der Verdampfungswahrscheinlichkeit bei einer Phononenergie | 30 % |

## Rahmen

- Explorativ (v3), Hypothesen [H]. Die Leitung rechnet selbst auf der .69 (kleintest.sh, CPU-Spur, je Lauf <= 10 min).
- Code: code/wand_transmission.py.
- Rauchlauf vor dem Einfrieren nur mit einem Fenster, das in keinem echten Lauf vorkommt.
- Danach Karte und Code als *.eingefroren-<zeit> schreibgeschuetzt kopieren.
- Literatur nach dem Einfrieren, getrennt in LITERATUR.md.

## Laufplan und Auswerteregeln (Nachtrag vor jedem echten Lauf, 2026-10-02 23:16:05 CEST)

- **Rauchlaeufe**, alle in Fenstern ausserhalb der echten Abtastbereiche (m1 [0,294; 0,299], d1 [2,05; 2,10],
  d3 [4,05; 4,10], je n = 3):
  - rauch (Fassung 1): Die Transmission aus zwei geschossenen Loesungen und D_out (Schiessen nach aussen) verloren durch
    Ausloeschung alle Stellen (Flussfehler 0,4 bzw. 1e60).
  - rauch2 (Fassung 2): Ersatz durch ein Randwertproblem T_fd mit exakt diskreten Randbedingungen. Dabei gab es einen
    Fehler beim d3-Knick.
  - rauch3 (Fassung 3): alle drei rc = 0. K0-Rest <= 1,2e-15, Dispersion <= 2,7e-15, Flussbilanz <= 4,2e-10.
- **Abweichung vom Kartentext:**
  - Die Gegenprobe "D_out" entfaellt, weil sie schlecht konditioniert ist. Die Gegenprobe der Nullstellenlage ist jetzt
    T_fd (unabhaengige Diskretisierung, h = 0,002 und 0,004, Richardson).
  - "abs(t)^2" in TR0 ist T_fd bei h = 0,002, ausgewertet an der geschossenen Nullstelle f_z.
- **Laeufe** (Code wand_transmission_v3.py, Schritt in f je Teilfenster):

| Name | Modell | Fenster | n | Schritt |
|---|---|---|---|---|
| m1a | m1 | [0,300; 0,770] | 471 | 0,001 |
| m1b | m1 | [0,770; 1,240] | 471 | 0,001 |
| m1c | m1 | [1,240; 1,700] | 461 | 0,001 |
| d1a | d1 | [0,225; 0,889] | 665 | 0,001 |
| d1b | d1 | [0,889; 2,000] | 556 | 0,002 |
| d3a | d3 | [0,505; 2,000] | 599 | 0,0025 |
| d3b | d3 | [2,000; 4,000] | 401 | 0,005 |

- **Auswerteregeln (mechanisch):**
  - Eine Nullstelle ist ein Vorzeichenwechsel von c_in zwischen benachbarten Abtastpunkten, verfeinert mit brentq.
  - Doppelt gezaehlte Nullstellen an den Teilfenster-Grenzen werden einmal gezaehlt.
  - TR0: genau eine Nullstelle in [1,45; 1,65], |f_z - 1,5275| <= 0,002, T_fd(f_z) < 1e-6.
  - TR1: mindestens eine Nullstelle in (2/9; 8/9).
  - TR2: mindestens eine Nullstelle in (1/2; 2).
  - Gegenproben je Nullstelle (berichtet, nicht Teil der Urteile): rtol 1e-9, Gebiet +10, FD-Lage bei zwei h mit
    Richardson.
- **Grenze:** Nullstellenpaare, die naeher beieinanderliegen als der Abtastschritt, kann die Abtastung verpassen.
