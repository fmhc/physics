# MESS-1 "Troepfchen-Bruecke" (Runde 9): Plan und Vorab-Erwartung

- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung claude-primary nach Finn 07:53 ("überlege noch mal wo wir in
  bestehenden experimenten sowas aus rechnungen nachweisen können"). Explorativ (v3), Literatur und Rechnung in einer Hand.
- Beginn: 2026-09-30 07:51:27 CEST (date, erster Befehl). Dieser Abschnitt geschrieben ab 2026-09-30 07:58:41 CEST
  (date), **vor jedem Literaturabruf und vor jeder Rechnung**. Gelesen hatte ich bis dahin nur: RUNDE-09.md,
  RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md (Zeilen 1 bis 460), bic2/PLAN.md (Zeilen 1 bis 80), Teile von bic2.py
  (Pluecker-Verfahren, direkt_m, umlauf), Kopf von RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md.
- Markierungen: **[H]** Hypothese; **[L?]** Literatur aus dem Gedaechtnis, nicht geprueft; **(Hand)** Schreibtischrechnung.

## 1. Modell (Stand vor der Quellenpruefung, [L?])

- Symmetrische binaere Mischung, Dichten gekoppelt, Petrov 2015, einheitenlos:
  i psi_t = (-1/2 lap - 3 |psi|^2 + (5/2) |psi|^3 - mu) psi, also F(n) = -3 n + (5/2) n^(3/2).
  - Energiedichte e(n) = -(3/2) n^2 + n^(5/2); Druck p = n F - e = -(3/2) n^2 + (3/2) n^(5/2) = 0 bei n = 1 (Hand).
  - Flaches Innenprofil n -> 1, mu -> -1/2 fuer N -> unendlich. Schallgeschwindigkeit c^2 = n F'(n) = 3/4 (Hand).
- Grundzustand phi_0(r) reell bei festem mu in (-1/2, 0): phi'' + (2/r) phi' = 2 (F(phi^2) - mu) phi (Schiessen).
- Bogoliubov-de-Gennes fuer l = 0, reduziert U = r u, V = r v (Hand):
  - U'' = 2 (D - eps) U + 2 C V,  V'' = 2 C U + 2 (D + eps) V
  - D = (n F)'(n_0) - mu = -6 n_0 + (25/4) n_0^(3/2) - mu,  C = n_0 F'(n_0) = -3 n_0 + (15/4) n_0^(3/2)
  - Das ist genau die Form von bic2 (m11 = dp - (omega + rho)^2, m22 = dp - (omega - rho)^2, sp): m11 = 2 (D - eps),
    m22 = 2 (D + eps), Kopplung 2 C. Aussen: Kanal u offen fuer eps > |mu| (q = sqrt(2 (eps - |mu|))), Kanal v immer
    geschlossen (kappa = sqrt(2 (eps + |mu|))). Also fuer jedes eps > |mu| genau ein offener Kanal, wie im Fenster des
    Q-Balls, aber ohne obere Grenze.
- Werkzeug: mess1.py, Kopie der Pluecker- und W-Teile aus bic2.py (numpy statt torch), neues Profil und neue Koeffizienten.
  - W(eps, mu) = L(y_a) + i L(y_b) bei reellem eps (L = Koeffizient der im Kanal v wachsenden Loesung); Umlaufzahl auf
    Rechtecken in (eps, mu) wie bic2 exakt. Gegen das Kernwachstum grosser Tropfen: fortlaufende Orthonormierung der
    beiden regulaeren Loesungen (Gram-Schmidt mit positiver Diagonale, aendert Nullstellen und Umlaufsinn nicht).
  - Breite: komplexe Pole eps = eps_r - i Gamma der Pluecker-Determinante (wie bic2 pole), Gamma = Amplitudenrate.
  - "kurve": Vorzeichen einer reellen Kopplungsgroesse entlang des Resonanzasts (wie bic2 kurve), nur als Wegweiser.

## 2. Vorab-Erwartung Literatur (vor dem Abruf; wird je Abruf in ERGEBNIS.md abgehakt)

- **E-L1** [L?] Petrov 2015 (PRL 115, 155302): Gleichung wie oben; kritische Zahl N_c ~ 18,65 (reduziert), Energie
  negativ ab ~ 22,5. "Selbstverdampfung": Die Monopolmode liegt ueber der Emissionsschwelle -mu in einem mittleren
  Fenster der Atomzahl, grob 20 < N~ < 1000 (Grenzen unsicher, eher 1e3 als 1e4 oben); Oberflaechenmoden l >= 2 treten
  erst bei einigen hundert bis tausend unter die Schwelle.
- **E-L2** Eine Breite der Monopolmode gegen N (Gamma(N) als Pol oder Abklingrate) hat niemand systematisch gerechnet;
  Nullstellen, Fano-Strukturen oder "embedded modes" bei Troepfchen sind nicht berichtet (Wahrscheinlichkeit ~85 %).
  Hoechstens Zeitentwicklungen (Selbstverdampfung, Atmung nach Anregung) mit qualitativer Daempfung.
- **E-L3** Experimente (39K Barcelona/Florenz 2018, 41K-87Rb Florenz 2019, dipolar Stuttgart/Innsbruck): keine
  aufgeloeste Messung der Atmungsbreite gegen N. Lebensdauer von Dreikoerperverlusten begrenzt (einige bis ~20 ms bei
  39K), Atomzahl auf 10 bis 20 % genau. Selbstverdampfung hoechstens indirekt (Wahrscheinlichkeit ~70 %).
- **E-L4** Eingebettete Solitonen (Yang, Malomed, Kaup 1999; Champneys u. a. 2001): Kodimension 1, also dasselbe
  Zaehlargument wie bei uns; optische Experimente dazu wenige oder keine. Kubisch-quintische "fluessige Lichttropfen"
  (Michinel u. a. 2002/2006): Oberflaechenspannung und flaches Profil, eine Rechnung der Atmungsbreite erwarte ich dort
  nicht.
- **E-L5** Riesen-Monopolresonanz: Fluchtbreite (Teilchenemission) klein gegen die Gesamtbreite und glatt in A; keine
  Nullstellen berichtet.

## 3. Vorab-Erwartung Rechnung (vor dem ersten Lauf)

- **E-R1 Kontrollen:** N_c = 18,65 +- 0,05 als Minimum von N(mu); N bei E = 0 nahe 22,5 (falls richtig erinnert);
  zwei Gitterstufen geben Lagen auf 1e-4 relativ gleich.
- **E-R2 Schwellenlage der Grundmode (Atmung, n_r = 0):**
  - Bei N_c geht eps_0 gegen 0 (Vakhitov-Kolokolov); knapp darueber gebunden (eps_0 < |mu|).
  - Kreuzt die Schwelle bei N_1 ~ 20 (Spanne 19 bis 30) nach oben und bei N_2 ~ 1e3 (Spanne 400 bis 3000) wieder nach
    unten (Hand: Tropfen mit freier Oberflaeche, eps_0 ~ pi c / R = 2,72/R, R = (3 N/(4 pi))^(1/3), gibt eps_0 = 1/2 bei
    N ~ 700; Oberflaechenkorrekturen verschieben).
  - Dazwischen ist die Atmung eine Resonanz mit Gamma > 0, an beiden Enden Gamma -> 0 wie die s-Wellen-Schwelle
    (Gamma ~ q).
- **E-R3 Breite der Grundmode:** glatt, ein Maximum, **keine exakte Nullstelle** im Fenster (N_1, N_2) (Wahrscheinlichkeit
  ~75 %). Gamma/eps_0 in der Fenstermitte zwischen 1e-3 und 1e-1.
- **E-R4 Mechanismus-Vorhersage [H] (Hand), kann scheitern:**
  - Beim Q-Ball brauchte die Leiter einen an die Wand gebundenen Zustand des geschlossenen Kanals (Innenbarriere plus
    Wandtopf: dp_min < (omega - rho)^2 < dp(S0)).
  - Beim Troepfchen ist die Innenbarriere immer da (D_innen + eps = 3/4 + eps > 0), aber der Wandtopf fehlt im
    flachen Grenzfall: D_min = -0,8192 - mu (bei n = 0,4096), also D_min + eps >= -0,8192 - 2 mu = +0,18 fuer mu = -1/2.
    Der Kanal v ist dort ueberall verboten.
  - Ein Wandtopf (D_min + eps < 0) ist nur moeglich fuer mu > -0,41 und eps < -0,8192 - mu, also bei kleinen Tropfen
    knapp ueber der Schwelle.
  - Stufenmodell (scharfe Oberflaeche, Hand): Eine BIC verlangt k_p cot(k_p R) = +kappa_innen (Kanal u) und
    = -kappa_aussen (Kanal v) zugleich; das geht nicht. Also keine BIC ohne Wandstruktur.
  - **Folgerung:** Im duennwandigen Bereich grosser N erwarte ich **keine** Leiter, weder fuer die Grundmode (dort ohnehin
    gebunden) noch fuer die Oberschwingungen n_r = 1, 2 (Wahrscheinlichkeit fuer mindestens eine exakte Stelle dort
    ~25 %). Wenn Stellen auftauchen, dann eher im Bereich kleiner Tropfen mit Wandtopf (mu > -0,41).
  - Scheitert, wenn im duennwandigen Bereich (mu < -0,45) eine Umlaufzahl +-1 fuer n_r = 1 oder 2 auftaucht.
- **E-R5 Oberschwingungen:** n_r = 1 liegt fuer grosse N ueber der Schwelle (eps_1 ~ 2 pi c/R > 1/2 fuer R < 11, also
  N < ~5000), n_r = 2 fuer R < 16 (N < ~17000). Breiten groesser als die der Grundmode, glatt.

## 4. Messbezug (Plan)

- Umrechnung der reduzierten Groessen mit Petrovs Einheiten (n_0, xi, Zeit hbar/|mu|-Skala) fuer 39K (Semeghini u. a.
  2018; Cabrera u. a. 2018) mit Streulaengen aus der Quelle. Erwartung: N~ = 20 bis 1000 entspricht einigen 1e3 bis 1e5
  Atomen; Zeitskala der Atmung ~ 1 ms; Dreikoerperverluste (~10 ms) und Atomzahlrauschen (10 bis 20 %) lassen einen
  schmalen Einbruch der Breite heute nicht aufloesen, falls es ihn gibt.

## 5. Ablauf und Grenzen

- Rauchtest lokal (CPU, 1 Thread, nice 19, timeout 120, Ausgaben nach lauf-lokal/); Messlaeufe auf der .69 ueber
  kleintest.sh (Spur cpu oder p4000a/b), je hoechstens 10 min, Logs mit absolutem Pfad.
- Belegstufen wie Runde 7: "gesehen" (Minimum), "Umlauf +-1" (exakt im abgeschnittenen radialen linearen Modell).
  Modell ist keine Messung.
