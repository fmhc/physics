# LADUNG-MONOPOL-1: Wird ein spinloses geladenes Teilchen am Gitter-Monopol zu Spin 1/2? (Runde 38)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 06:01:34 CEST (date), vor jeder Rechnung.
- **Herkunft:** Vorschlag der Literaturkarte LADUNG-MONOPOL-L (RUNDE-37/ladung-monopol-l/DOSSIER.md, Abschnitt 9),
  Modell und Vorhersagen von der Leitung uebernommen; der Ordner liegt unter RUNDE-37/ wie die uebrigen Karten.
- **Anlass:** Spin-1/2-Linie (STRATEGIE-SPIN-20261004.md, Linie 1); Pool H2 (Ladung + Monopol).
- **Frage:** Wird ein spinloses Teilchen der Ladung q auf dem Gitter um einen Gitter-Monopol zu einem Spin-1/2-Dublett
  (q = 1) bzw. zu einem Spin-1-Triplett (q = 2)? Das ist der H2-Mechanismus (Spin = q/2) auf dem Netz, im
  Einteilchen-Bild.
- **Rueckfragen des Dossiers, beantwortet:**
  - "Monopol" ist der Defekt des konjugierten Feldes (emergenter Monopol des Quanten-Eises).
  - Fuer spaetere Q-Ball-Stufen koppelt der Q-Ball an das Eis-U(1).
- Kennzeichen: [M] Mathematik, [L] Literatur, [S] an der Quelle gelesen (laut Dossier), [ES] eigener Schluss, [H]
  Hypothese.

## Modell (Teil A, kubisch; aus dem Dossier)

- **Gitter:** offene Box L^3, L in {12, 16, 24}. Einheitsmonopol (Fluss 2 pi) im Mittelwuerfel.
- **Fluss je Plakette:** Phi_p = Omega_p/2, mit Omega_p dem Raumwinkel der Plakette vom Monopol aus.
  - Das ist exakt wuerfelsymmetrisch und quellenfrei in jedem Wuerfel ausser dem Mittelwuerfel.
  - Im Mittelwuerfel ergibt sich 6 x pi/3 = 2 pi, jeder Wert in (-pi, pi]. Das ist ein zulaessiger kompakter
    Gitter-Monopol.
- **Peierls-Phasen:** A mit rot A = Phi_p - 2 pi [Plakette vom Dirac-String durchstossen], String entlang +z zum Rand.
  Loesung z. B. mit lsqr, Rest <= 1e-10.
- **Hamilton:** H = -sum_<ij> (e^{i q A_ij} c_i^+ c_j + h.c.) - V0 sum_{i in 8 Ecken des Mittelwuerfels} n_i.
  - q in {0 (ohne Monopol), 1, 2}; V0 in {0, 1, 2, 3, 4, 6, 8, 12}.
  - Der Kern-Topf ist die noetige Zusatzkraft: Ohne sie keine Bindung (Kato).
- **Messgroessen:**
  - tiefste 12 Eigenwerte
  - gebunden: E < -6 - 1e-3 und Gewicht in r <= 3 mindestens 0,9
  - Entartung: relativer Abstand <= 1e-8
  - Kommutatorzeichen s = <U_x U_y U_x^-1 U_y^-1> auf der tiefsten Stufe, mit U = pi-Drehung um x bzw. y durch den
    Wuerfelmittelpunkt mal passender Eichtransformation
  - Schwelle V0c je q (Bisektion auf 1e-3)

## Vorhersagen (vor jeder Rechnung; aus dem Dossier uebernommen)

| Nr | Vorhersage | ableitbar? | Wahrsch. |
|---|---|---|---|
| LM0 | Kontrolle q = 0: s = +1, tiefste gebundene Stufe einfach. Eichkonstruktion Rest <= 1e-10; Spektrum unabhaengig von der String-Richtung (+z, -z, +x) auf 1e-10 | ja | 95 % |
| LM1 | Kontrolle q = 1: s = -1 auf allen Stufen, jede Stufe gerade entartet; q = 2: s = +1 | ja (Paritaet des Gesamtflusses) | 90 % |
| LM2 | q = 1, L = 24, jedes V0 ueber der Schwelle: tiefste gebundene Stufe genau 2-fach (Dublett), nicht 4-fach | nein (Gitterkern) | 80 % |
| LM3 | q = 2, gleiche Bedingungen: tiefste gebundene Stufe genau 3-fach (Triplett, j = 1) | nein | 70 % |
| LM4 | V0c(q=1) > V0c(q=0) (Kato); Verhaeltnis V0c(1)/V0c(0) in [1,3; 3,0] | Vorzeichen ja, Groesse nein | 60 % |
| LM5 | gebundene Eigenwerte bei L = 16 und L = 24 auf 1e-6 gleich | nein (Endlichkeit) | 85 % |

**Bedeutung (vorab):**
- **LM2 und LM3 treffen ein:** Auf dem Gitter wird ein spinloses Teilchen am Monopol zu Spin q/2. Damit ist der
  H2-Mechanismus und die Q/2-Regel im Netz gezeigt.
  - Die Austauschstatistik ist damit nicht gezeigt (dafuer Goldhaber [S]).
  - Ebenso wenig, dass das Quanten-Pfeil-Eis Monopole hat.
- **LM2 verfehlt (Quartett unten):** Der Gitterkern kehrt die Reihenfolge um. Dann beschreiben, ab welchem Kernradius
  bzw. L das Dublett unten liegt.
- **LM4 ausserhalb des Bandes:** Die Kontinuumsabschaetzung traegt auf Kernradius ~1 nicht; nur beschreiben.
- **Ehrlich vorab:** LM0 und LM1 pruefen den Code, nicht die Physik. LM2 und LM3 uebertragen eine Kontinuums-Erwartung
  [L Wu/Yang 1976] auf ein neues Gitter.
- **Folgestufen (eigene Karten, erst nach Teil A):**
  - Teil B: dasselbe auf dem Pyrochlor-Kanten-Netz von FLUSS-1, also Finns Netz.
  - Teil C: geladener Q-Ball am Monopol mit Portal-Topf.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (geteilt; der Starter wartet auf den Lock); je
  <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
