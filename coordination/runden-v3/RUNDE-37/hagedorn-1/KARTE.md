# HAGEDORN-1: Schwingt ein drehender Q-Ball-Ring wie ein String, oder zerfaellt er? (Glied 7, Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 05:45:29 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Schwerpunkt "Glieder 10 und 7 der Spin-2-Kette".
  - Nach CEMZ [L: Camanho/Edelstein/Maldacena/Zhiboedov 2014] braucht jede Korrektur von Einsteins Drei-Graviton-Kopplung
    einen stringartigen Turm schwerer Teilchen mit hohem Spin.
  - RG-1 (RUNDE-06): Die fuehrende Bahn drehender Q-Baelle folgt J ~ E^2 wie bei Strings. Das folgt aber schon aus der
    Ringform (Radius ~ m, Ladung ~ m).
  - Offen seit RUNDE-07 (MT-2), in der Warteschlange seit RUNDE-36 (B3 HAGEDORN-1): Zaehlt der Ringturm wie ein String?
- **Schreibtisch vorab (warum die Zaehlung allein nichts prueft):**
  - Einzelne Ringzustaende (m, n) wachsen polynomial in E, das ist vorab ableitbar [M]. Die B3-Vorhersage waere also
    selbsterfuellend.
  - Ein String hat Hagedorn-Dichte, weil seine Schwingungen laengs der Laenge L laufen, mit omega_l ~ l/L, und L mit E
    waechst [L].
  - Fuer den Ring heisst das: Erst lineare, stabile Schwingungen laengs des Rings (omega_l ~ c_s l/R) und Energie
    proportional zur Ringlaenge ergeben zusammen eine Zustandsdichte exp(const * E) [M/H].
  - Der eigentliche Test ist also das Schwingungsspektrum des Rings.
- **Literatur (aus dem Gedaechtnis):**
  - Im NLS-Grenzfall sind duenne Wirbelringe azimutal instabil und zerfallen in Stuecke [L].
  - In der kubisch-quintischen NLS sind dicke Wirbel-Solitonen mit kleinem m bei grosser Norm stabil [L?:
    Quiroga-Teixeiro/Michinel 1997; Malomed u. a.].
  - Unser N = 1-Ast ist die kubisch-quintische NLS (Projekt, EW-2).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- **Modell und Profile** wie RG-1 (RUNDE-06/regge/regge2d.py): 2D, M1-Potential U(S) = S - S^2 + S^3/2,
  phi = f(r) e^(i m theta - i omega t).
  - m in {0; 1; 2; 3; 5; 8}, omega^2 in {0,55; 0,7; 0,85; 0,95; 0,99}, soweit Profile existieren.
- **Lineare Stabilitaet (Bogoliubov-de-Gennes):**
  - Stoerungen u(r) e^(i (m + l) theta) und v(r) e^(i (m - l) theta) mit Zeitfaktor e^(-i Omega t), fuer l = 0 bis 12.
  - Radiales Eigenwertproblem, nicht hermitesch, finite Differenzen.
  - Gesucht: Eigenwerte mit Im Omega > 0 (Zerfall) und die tiefsten reellen Moden je l (Ringschwingungen).
- **Kontrollen:**
  - Nullmoden: Phase (l = 0) und Verschiebung (l = +-1) auf <= 1e-6.
  - Konvergenz bei Gitterverdopplung.
  - m = 0 gegen die Vakhitov-Kolokolov-Regel (stabil, wo dQ/domega < 0).
- **Ringradius** R = Ort des Maximums von f. Pruefe, ob die tiefsten Moden fuer l = 2 bis 6 linear in l/R laufen.
- **Beschreibend:** N(E) der (m, n)-Ringzustaende (nicht geurteilt, vorab ableitbar).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| HG0 | Kontrollen: Nullmoden (l = 0, +-1) auf <= 1e-6; Eigenwerte konvergent bei Gitterverdopplung (<= 1e-4 relativ); m = 0 stabil genau dort, wo dQ/domega < 0 | 75 % |
| HG1 | Duenne Ringe zerfallen: Fuer omega^2 >= 0,95 und m >= 3 hat jedes Profil eine Mode mit Im Omega > 1e-4 | 70 % |
| HG2 | Dicke Ringe halten: Fuer omega^2 <= 0,7 ist mindestens ein Profil mit m >= 1 stabil (alle Im Omega < 1e-6 fuer l = 0 bis 12) | 55 % |
| HG3 | [H] Stringartig, wo stabil: Fuer jedes stabile Profil mit m >= 2 laufen die tiefsten reellen Moden fuer l = 2 bis 6 linear in l (Anpassung Omega = a + b l mit R^2 > 0,98 und b > 0) | 35 % |
| HG4 | [H] Energie waechst mit der Ringlaenge: Auf dem stabilen Ast gilt E proportional zu R (Steigung der doppelt-logarithmischen Anpassung von E gegen R bei festem omega: 1 +- 0,15) | 40 % |

**Bedeutung (vorab):**
- **HG2 bis HG4 treffen ein:** Dicke drehende Q-Ball-Ringe verhalten sich wie geschlossene Strings, mit Zugspannung und
  Schwingungen laengs des Rings.
  - Der Ringturm haette dann Hagedorn-Dichte [H]. Fuer Glied 7 hiesse das: Q-Baelle liefern vielleicht den
    stringartigen Turm, den CEMZ verlangen.
  - Folge: Kopplung an das Graviton (CEMZ-Bedingung) als Schreibtischkarte.
- **HG1 trifft ein und HG2 verfehlt:** Der Ringturm zerfaellt, ist also kein String. Glied 7 bleibt bei Strings oder
  anderen Auswegen (Vasiliev, kontinuierlicher Spin).
- **HG3 verfehlt (quadratisch statt linear):** Der Ring ist ein biegesteifer Stab, kein String.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
