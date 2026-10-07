# REGGE-4D-1: Hat die Simplex-Wirkung genau Einsteins Spin-2-Struktur, samt Minus-Modus? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 00:53:10 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn ~22:30: "Wie kommen wir auf die spin2 kopplung ... aus punkten strichen Dreiecken ...?"
  - REGGE-RAND-1 und die Nachrechnung der Leitung bestaetigen nur den Newton-Teil (3D, zeitsymmetrisch).
  - Dossier GRAVITON-NETZ-L, E2: Rocek/Williams 1981 fanden auf dem 4D-Hyperkubus mit Diagonalen (15 Kanten je Ecke) den
    Kontinuumspropagator im schwachen Feld; 4 Nullmoden sind Eichung; dazu eine unerwartete fuenfte Nullmode [S,
    sekundaer].
  - TENSOR-EIS-N und LAMBDA-1: Anziehung braucht einen Minus-Modus mit genau abgestimmtem Faktor.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [S] laut Dossier an der Quelle gelesen, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Gitter:** 4D-Kuhn-Zerlegung des Hyperkubus, 4! = 24 Simplizes je Wuerfel. Kanten sind alle 0/1-Vektoren ausser 0,
  also 15 je Ecke.
- **Euklidische Regge-Wirkung:** S = sum_Dreiecke A_t eps_t. Gelenke sind in 4D die Dreiecke; eps_t = 2 pi minus die
  Summe der Diederwinkel zwischen den zwei Tetraederflaechen jedes Simplex an t [L].
- **Zweite Ordnung um das flache Gitter** [M, Schlaefli]: dS = sum A_t d eps_t ist null, also
  M_ee' = sum_t (dA_t/dl_e)(d eps_t/dl_e'). Es genuegen die ersten Ableitungen der Fehlwinkel. Fourier gibt eine
  15 x 15-Matrix M(k).
- **Kontinuum** [L, Spinprojektoren nach Barnes/Rivers]: Die linearisierte euklidische Einstein-Hilbert-Wirkung auf h_mu_nu
  (10 Komponenten) ist ~ k^2 (P^(2) - 2 P^(0,s)).
  - 4 Eichmoden mit Eigenwert 0.
  - 5 Spin-2-Moden positiv.
  - 1 konformer Modus negativ, mit Faktor -2 gegen Spin 2. Das ist das "falsche Vorzeichen" aus TENSOR-EIS-N.
- **Bei k = 0** [M]: Jede affine Verzerrung des flachen Gitters bleibt flach. Das sind 10 Nullmoden (symmetrische
  4 x 4-Verzerrungen).
- **Die 5 ueberzaehligen Kanten je Ecke** (15 - 10) sollten Gittermoden mit Eigenwert O(1) sein; nach Rocek/Williams ist
  eine davon aber eine Nullmode [S, sekundaer].
  - Effektiv: die Gittermoden per Schur-Komplement ausintegrieren, bleibt eine 10 x 10-Form auf h_mu_nu. Dabei gilt
    delta(l_e^2) = e^mu e^nu h_mu_nu.

## Test (Code-Agent)

- **Fehlwinkel:** Kuhn-Gitter 4D, periodisch L = 4 (oder 3). Fehlwinkel aus exakten Diederwinkeln: 4-Simplex aus den zehn
  Kantenlaengen einbetten, Normalen der Tetraederflaechen. Erst die Flachheit pruefen.
- **Ableitungen:** d eps_t/dl_e fuer die 15 Kantentypen an der Ursprungsecke per zentraler Differenz; dA_t/dl_e
  analytisch (Heron). Daraus M(0, R), dann M(k).
- **Spektrum:** M(k) auf 15 x 15 fuer k = 0 und kleine abs(k) (0,05 bis 0,4) in mehreren Richtungen. Zaehlen: Nullmoden,
  negative und positive Moden, Gittermoden mit Eigenwert O(1).
- **Effektive Form:** 10 x 10 auf h_mu_nu (Abbildung h -> delta(l^2) bzw. delta l; die 5 Gittermoden per Schur-Komplement
  heraus). Zerlegung in Spinprojektoren, Vergleich mit k^2 (P^(2) - 2 P^(0,s)) bis auf eine gemeinsame Normierung.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| G0 | Kontrolle: flaches Kuhn-Gitter (alle Fehlwinkel < 1e-12); M(k) hermitesch; bei k = 0 genau 10 Nullmoden (affine Verzerrungen) | 85 % |
| G1 | Bei kleinem k: 4 Eichmoden (< 1e-6 relativ), 5 positive und 1 negativer Modus ~ k^2; die uebrigen 5 sind Gittermoden. Eine zusaetzliche Nullmode wie bei Rocek/Williams ist erlaubt und wird gezaehlt | 50 % |
| G2 | Effektive 10 x 10-Form: Verhaeltnis negativer Spin-0- zu Spin-2-Koeffizient = -2 innerhalb 10 % bei abs(k) <= 0,2 | 55 % |
| G3 | Die Spin-2-Koeffizienten haengen bei abs(k) <= 0,2 nicht von der Richtung ab (innerhalb 5 %) und sind fuenffach entartet | 55 % |

**Bedeutung (vorab):**
- G1 bis G3 treffen ein: Aus Dreiecken bzw. 4-Simplizes mit Kantenlaengen als Feld kommt genau Einsteins Spin-2-Struktur.
  - Sie enthaelt den konformen Minus-Modus mit Faktor -2, also das "falsche Vorzeichen", das gleiche Massen anziehen
    laesst (TENSOR-EIS-N).
  - Das ist die Antwort auf Finns Frage: Spin 2 und die Anziehung entstehen zusammen, wenn die Striche Laengen sind.
  - Hineingesteckt ist dabei die Regge-Wirkung (Regime A).
- G1 verfehlt (mehr Nullmoden oder kein Minus-Modus): Das Kuhn-Gitter hat Gitterartefakte wie bei Rocek/Williams;
  beschreiben, welche.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (nicht cpu, cpu2, cpu5, cpu6, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
