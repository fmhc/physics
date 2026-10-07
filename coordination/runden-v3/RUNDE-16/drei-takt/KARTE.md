# DREI-TAKT: Finns Hypothese "zwei bearbeiten ein drittes" (Runde 16)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 08:32:15 CEST (date), vor jeder Codezeile und
  jedem Lauf.
- Auftrag Finn (02.10., woertlich): "prüfe folgende hypothese: wenn zwei teile ein drittes bearbeiten ist es eine
  zeitlang stabil, und äußere einflüsse im gleichen takt können die stabilität positiv beeinflussen, aber äußere
  einflüssen können in einem 3er system auch mehr chaos verursachen"
- Explorativ nach v3. Bis zur Rechnung ist alles Hypothese [H]. Literaturangaben der Leitung sind aus dem Gedaechtnis
  [L?].

## Zerlegung in drei pruefbare Teile

| Teil | Aussage | Pruefbare Form |
|---|---|---|
| H1 | Zwei wirken auf ein drittes: eine Zeitlang stabil | Endliche, aber lange Lebensdauer nahe einer Stabilitaetsgrenze, die zur Grenze hin waechst |
| H2 | Aeusserer Einfluss im gleichen Takt stabilisiert | Ein periodischer Einfluss bei der Eigenfrequenz des Systems macht Zustaende stabil, die ohne ihn instabil sind; besser als bei anderen Takten |
| H3 | Aeusserer Einfluss erzeugt im Dreiersystem mehr Chaos | Mit Einfluss positive Lyapunov-Exponenten, ohne nicht. Zusatz: Ist drei dabei besonders, gilt es fuer zwei also nicht? |

**Leitfrage:** Haengt die Antwort davon ab, ob das System konservativ (Gravitation) oder gedaempft bzw. selbsterregt
(Taktgeber, Phasenmodelle) ist? Die Leitung erwartet: ja.

## D1 Gravitation: zwei Hauptkoerper, ein Dritter (eingeschraenktes Dreikoerperproblem, konservativ)

Zwei Hauptkoerper mit den Massen 1 - mu und mu kreisen umeinander. Ein masseloser Dritter sitzt nahe dem Lagrangepunkt L4,
wie die Trojaner bei Jupiter. Die zwei "bearbeiten" den Dritten, ohne dass er zurueckwirkt.

- **D1a, Exzentrizitaet als Einfluss im Umlauftakt (linear, Floquet):**
  - Bei elliptischer Hauptkoerperbahn (Exzentrizitaet e) pulsieren die Kraefte auf den Dritten im Umlauftakt
    (elliptisches eingeschraenktes Problem).
  - Linearisierung um L4, in pulsierenden Koordinaten mit der wahren Anomalie f als Zeit [L?, selbst herleiten bzw. an
    der e = 0-Kontrolle pruefen]:
    x'' - 2 y' = (Uxx x + Uxy y) / (1 + e cos f),  y'' + 2 x' = (Uxy x + Uyy y) / (1 + e cos f),
    mit Uxx = 3/4, Uyy = 9/4, Uxy = (3 sqrt(3)/4)(1 - 2 mu).
  - Monodromiematrix ueber 2 pi, Gitter mu in [0; 0,06], e in [0; 0,6].
  - Stabil heisst: alle Multiplikatoren auf dem Einheitskreis (Toleranz angeben, zwei Schrittweiten).
- **D1d, Einfluss mit frei waehlbarem Takt (linear, Floquet):**
  - Kreisbahn (e = 0). Die Anziehung pulsiert mit einem aeusseren Takt Omega:
    rechte Seiten mal (1 + eps cos(Omega t)).
  - Gitter Omega in [0,2; 10], eps in [0; 0,3], fuer mu in {0,01; 0,02; 0,035; 0,0390; 0,0400; 0,0420}.
  - Zu messen: Wo liegen die Instabilitaetszungen? Gibt es fuer mu oberhalb der Routh-Grenze Fenster, in denen der Takt
    stabilisiert? Bei welchem Omega: nahe den Eigenfrequenzen ("gleicher Takt") oder bei schnellem Takt?
- **D1b, Lebensdauer oberhalb der Grenze (nichtlinear):**
  - Volle Gleichungen, e = 0, mu von 0,0386 bis 0,05.
  - Start mit Auslenkung 0,005 bzw. 0,02 aus L4, je 64 Richtungen.
  - Bis 10^3 Umlaeufe. Lebensdauer: bis der Abstand zu L4 groesser als 0,5 ist oder der kleine Hauptkoerper naeher als
    0,05 kommt.
  - Dazu die groesste Auslenkung vor dem Ende.
- **D1c, Chaos (nur wenn Zeit bleibt):**
  - Endliche Lyapunov-Zahl ueber 10^3 Umlaeufe nahe L4 fuer mu in {0,001; 0,01; 0,02; 0,03} und e in
    {0; 0,05; 0,1; 0,2}.
- **Kontrollen D1:**
  - e = 0: Routh-Grenze mu_R = (1 - sqrt(69)/9)/2 = 0,0385209.
  - Zungenspitze bei mu = (1 - sqrt(8/9))/2 = 0,0285955; dort ist die lange Librationsfrequenz 1/2.
  - Eigenwertgleichung bei e = 0: lambda^4 + lambda^2 + (27/4) mu (1 - mu) = 0.
  - Jacobi-Konstante bei e = 0 auf < 1e-9 relativ.

## D2 Taktgeber: zwei Schrittmacher und ein Dritter (Phasenmodell, gedaempft)

- Modell: dtheta_C/dt = omega_C + K [sin(theta_A - theta_C) + sin(theta_B - theta_C)] + F sin(Omega t + psi - theta_C).
  - A und B laufen frei mit omega_A = omega_B = 1 und gleicher Phase.
  - C hat die Verstimmung Delta = omega_C - 1.
- **D2a (H1):**
  - Ohne aeusseren Takt rastet C ein, wenn |Delta| < 2K.
  - Knapp ausserhalb ist C eine Zeitlang gerastet, dann folgt ein Phasensprung.
  - Gemessen wird die mittlere Rastdauer gegen den Abstand zur Grenze. Exakte Kontrolle (Adler):
    T = 2 pi / sqrt(Delta^2 - 4 K^2).
- **D2b (H2):**
  - Delta knapp ausserhalb der Rastung, aeusserer Takt mit Omega = 1 (gleicher Takt wie A und B), Phase psi von 0 bis
    2 pi, F klein.
  - Rastkarte in (psi, F) und in (Omega, F).
- **D2c (H2, zwei verschiedene Takte, explorativ):**
  - omega_A ungleich omega_B. Hilft ein aeusserer Takt bei omega_A, bei omega_B oder dazwischen?

## D3 Chaos: zwei gegen drei (gekoppelte Phasen mit aeusserem Takt)

- Modell (Kuramoto-Sakaguchi, alle mit allen):
  dtheta_i/dt = omega_i + (K/N) sum_j sin(theta_j - theta_i - alpha) + F sin(Omega t - theta_i).
- Faelle:
  - N = 2 mit Takt
  - N = 3 ohne Takt
  - N = 3 mit Takt
  - N = 4 ohne Takt als Vergleich
- Groesster Lyapunov-Exponent lambda_max (Benettin, tangentiale Gleichung, im mitlaufenden Bild autonom).
- Zufallsstichprobe von etwa 2000 Parameterpunkten je Fall:
  - K in [0; 4], alpha in [0; 1,5], F in [0; 2]
  - Omega um die mittlere Frequenz +-2
  - omega_i-Streuung in [0; 2]
  - Je Punkt Einschwingen 500, Messung 2000 Zeiteinheiten.
- Theorie [L?]:
  - N = 2 mit Takt und N = 3 ohne Takt leben auf einem 2-Torus. Dort ist kein Chaos moeglich.
  - N = 3 mit Takt lebt auf einem 3-Torus. Chaos ist dort moeglich, wie bei N = 4 ohne Takt mit einem Schrittmacher [H].
- Treffer mit lambda_max > 0,01: nachrechnen mit dt/2, doppelter Messzeit und anderer Anfangsbedingung.

## Vorhersagen (Leitung, vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K | Kontrollen D1 bei e = 0 auf 1e-4; D2 trifft Adler auf 1 % | 98 % |
| D1a-1 | e > 0 macht Faelle instabil, die bei e = 0 stabil sind (Zunge ab mu ~ 0,0286). Der Umlauftakt schadet hier. | 95 % |
| D1a-2 | e > 0 macht irgendwo oberhalb mu_R stabil. Der Umlauftakt hilft hier. | 35 % |
| D1d-1 | Zungen bei Omega ~ 2 omega_k / n und bei Kombinationen omega_s +- omega_l. "Gleicher Takt" destabilisiert. | 90 % |
| D1d-2 | Wenn ein Takt oberhalb mu_R stabilisiert, dann ein schneller (Omega >> 1, Kapitza-artig), nicht der gleiche | 60 % |
| D1b-1 | Oberhalb mu_R: Lebensdauer endlich, waechst zur Grenze etwa wie (mu - mu_R)^(-1/2) | 55 % |
| D1b-2 | Stattdessen: Knapp oberhalb mu_R bleiben Teilchen 10^3 Umlaeufe gefangen (nichtlineare Begrenzung) | 35 % |
| D1c | e erhoeht die Chaoszahl nahe L4 im Mittel | 85 % |
| D2a | Rastdauer ~ (abs(Delta) - 2K)^(-1/2) nahe der Grenze | 99 % |
| D2b | Gleicher Takt in Phase (psi = 0) rastet C ein; gegenphasig (psi = pi) rastet er C aus. Takt allein reicht nicht, die Phase entscheidet. | 97 % |
| D3-1 | N = 2 mit Takt und N = 3 ohne Takt: nirgends robust lambda_max > 0,005 | 97 % |
| D3-2 | N = 3 mit Takt: mindestens ein robuster Punkt mit lambda_max > 0,01 | 70 % |
| D3-3 | N = 4 ohne Takt: robuste Punkte mit lambda_max > 0,01 vorhanden | 75 % |

## Antwortklassen je Teil (vorab)

- **gestuetzt:** in mindestens einem Modell klar, mit Kontrollen
- **teilweise:** nur unter Bedingungen, etwa nur gedaempft, nur in Phase oder nur bei schnellem Takt
- **in diesen Modellen nicht gestuetzt:** kein "widerlegt"; das Ergebnis gilt nur fuer die gerechneten Modelle
- **offen:** Numerik nicht aufgeloest, Kontrolle verfehlt oder Zeit aus

## Rahmen

- Code-Agent, eigener Code (numpy/scipy), alles in RUNDE-16/drei-takt/.
- Nur .69 ueber kleintest.sh, Spuren cpu3 und cpu4; jeder Aufruf hoechstens 10 min.
- Lokal nur Rauchtests (<= 120 s, ein Thread, nice 19).
- Plan vor dem ersten Lauf einfrieren. Zeitbox 90 min.
- Reihenfolge bei Zeitnot: D1a, D3, D1d, D2, D1b, D1c.
