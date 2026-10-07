# KAUSAL-WELLE-4D: Plan (Code-Agent fuer die Leitung, Runde 38, explorativ nach v3)

- Start des Code-Agenten 07:10:34 CEST (date). Plantext ab 07:37 CEST (date vor dem Schreiben: 07:37:05).
- Vor dem Plantext liefen nur technische Rauchlaeufe (Abschnitt 8): Codeprobe, Zeitmessung N = 5 000 / 10 000 / 20 000,
  Feld rho = 4 (Saaten 91, 92) und rho = 16 (Saat 91) nur fuer Zeit und Speicher, Kontinuum.
  Saatmittel, Streuungen, Normen und Linkzahlen der Kausalmenge habe ich vor dem Einfrieren nicht angesehen (Abschnitt 8).
- Karte: KARTE.md. Die Vorhersagen KV0 bis KV3 und ihre Schwellen sind unveraendert uebernommen (Abschnitt 6).
- Code:
  - code/kausal4d.py: Streuung, Kausalmatrix, Links (GEMM-Bloecke), Johnston-Rekursion, Zuschauer, Messsummen, Probe
  - code/kontinuum4d.py: Kontinuum (k-Raum und direkte Faltung), Johnston-Erwartung bei endlichem rho, Linkzahl-Integral
  - code/auswertung4d.py: Urteile, Bilder, auswertung.json
- Kennzeichen:
  - [S] an der Quelle gelesen; [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [H] Hypothese
  - [M] eigene Mathematik; [F] Festlegung dieses Plans (von der Karte offengelassen); [E] im Rauch gesehen

## 1. Quelle und Formeln

- **Gelesen [S]:** S. Johnston, "Particle propagators on discrete spacetime", CQG 25 (2008) 202001, arXiv:0806.3083v2
  (ein WebFetch-Abruf, PDF lokal gelesen; die Nummer stimmt).
  - (2.2): (A_R)_ij = 1, wenn v_i -<* v_j (Link), sonst 0; natuerliche Nummerierung, streng obere Dreiecksmatrix.
  - (3.2): Summe ueber Pfade, Phi = a A_R. (3.3), (3.5): K = I + Phi (I - b Phi)^-1; der Summand I ist Konvention (S. 5).
  - 3.2.2: "in 3+1 dimensions the propagator requires us to sum over paths". (3.33): V = (pi/24) tau^4,
    mu_rho = exp(-rho V). (3.36): lim sqrt(rho) mu_rho = (sqrt 24/2) delta(tau^2).
  - (3.44): **a = sqrt(rho)/(2 pi sqrt 6), b = -m^2/rho.** Die Kartenformeln stimmen in Faktor und Vorzeichen.
  - (3.25): Kontinuum K_m = (1/2pi) delta(tau^2) - (m/4pi) J1(m tau)/tau im Vorwaertskegel; (3.17): (Box + m^2) K = delta.
  - (3.13) bis (3.15), (3.32): Erwartungswert ueber Streuungen: K_P = Summe a^n b^(n-1) P_n,
    K_P~ = a mu~/(1 - a b rho mu~).
  - **Gueltigkeit [S, S. 10 und 11]:** "For sprinklings into 3+1 dimensional Minkowski spacetime the propagator's
    expected value equals the continuum propagator only in the infinite density limit." Vorlaeufige Simulationen nur
    in kleinen Volumina, Bedingung m^2 << sqrt(rho). Grund: Man kann nicht genug Punkte fuer grosse Dichte in grossem
    Volumen streuen.
- **Feld [M]:** phi(x) = (1/rho) Summe_y (K - I)(y, x) J(y) = (a/rho) (L^T psi)(x).
  - psi ist die Loesung von psi = J - (a m^2/rho) L^T psi (Vorwaertsrekursion in Zeitordnung).
  - Gleichwertig psi = J - m^2 phi, also phi = K_0 (J - m^2 phi) mit K_0 = a L.
- **Johnston-Erwartung bei endlichem rho [M, aus (3.13) bis (3.15), (3.32) und (3.44)]:**
  - Fuer einen festen Zuschauerpunkt gilt E[phi] = K_P * J.
  - K_P~ = k~/(1 + m^2 k~) mit k~(Z) = (4 pi a/Z) Integral tau^2 exp(-pi rho tau^4/24) K1(Z tau) dtau und
    Z^2 = |k|^2 - omega^2. Die Formel fuer lorentzinvariante retardierte Funktionen habe ich selbst hergeleitet.
  - Fuer rho -> inf folgt 1/(Z^2 + m^2), also das Kontinuum.
  - **Bei endlichem rho ist E[phi] nicht das Kontinuum.** Die Pole von K_P~ liegen bei Im omega > 0, die Erwartung waechst
    also mit der Zeit.
  - Erste Ordnung [M]: Im omega = (sqrt 6/4) m^4/(omega sqrt rho), etwa 0,61/sqrt(rho) bei omega ~ 1.
  - Numerisch (Kontinuum-Rauch, Abschnitt 8): Abschnitt 6.1.

## 2. Gebiet, Quelle, Dichten, Saaten

- **Einheiten:** m = 1. **Quelle (Karte):** J = exp(-(t^2 + |x|^2)/(2 sigma^2)) exp(-i(omega t - p z)), omega = cosh eta,
  p = sinh eta.
  - [F] sigma = 1; eta in {0; 0,5} (p = 0 und 0,521, Paket ruhend und mit v = 0,462 in z). Beide laufen als Spalten auf
    derselben Streuung.
  - [F] Gekappt bei r4 = sqrt(t^2 + |x|^2) <= R_S = 3,5 sigma. Huelle dort e^(-6,1) = 0,2 %; Anteil ausserhalb der Kappe
    1,6 % des 4D-Integrals von |J|.
- **Gebiet [F]:** D = J+(B) geschnitten J-(top), B die 4-Kugel vom Radius R_S um 0, top = (5, 0, 0, 0).
  - **Vollstaendige Vergangenheit [M]:**
    - D ist kausal konvex (Zukunftsmenge geschnitten Vergangenheitsmenge) und enthaelt den Traeger der gekappten Quelle.
    - Jede Kette von einem Quellpunkt zu einem Punkt von D liegt in D. Links zwischen Punkten von D sind dieselben wie
      in einer unbegrenzten Streuung.
    - phi ist deshalb an jedem Punkt von D und an jedem Zuschauer in D exakt; es gibt keinen Feldrand.
  - Volumen V_D = 1271,6 (Abschnitt 8). Raeumlich kugelsymmetrisch.
  - **Randeffekt der Linkzahl:**
    - Elemente nahe dem unteren Rand von D haben weniger Vergangenheitslinks; ihre Vergangenheit ausserhalb D traegt
      kein Feld.
    - Das exakte Integral (KV0) enthaelt diese Randbeschraenkung; die Linkzahl je Zeitklasse wird beschreibend gezeigt.
- **Kausalrelation:** y vor x, wenn t_x - t_y >= |x - y| und t_x > t_y.
- **Links:** L = C und nicht (C C > 0). C wird als float32 gespeichert, das Produkt laeuft in 2048er-Bloecken (nur
  obere Dreiecksbloecke, Zwischenindex in [I0, J1)). Ein Gewinde (Starter).
- **Laufzeit und N (Rauch, Abschnitt 8):** Links N = 5 029 / 10 007 / 20 037: 3,3 / 18,8 / 117 s; rho = 16
  (N = 20 633): 137 s je Saat, 1,87 GB.
  - N = 3 x 10^4 sprengt die 4G-Grenze (C allein 3,6 GB) und braeuchte ~400 s je Saat.
  - **Groesstes machbares N ~ 2 x 10^4.**
- **Dichten [F]:** rho in {4; 8; 16}, also E[N] = 5 086 / 10 173 / 20 345; ell = rho^(-1/4) = 0,71 / 0,59 / 0,50.
- **Saaten [F]:**
  - Feld: Saaten 1 bis 12 je rho, SeedSequence([20261004, 38, 81, 1000 rho, s]).
  - Codeprobe: rho = 1,2, Saat 1, eigene Saatfolge (83).
  - Rauchsaaten 91 und 92 gehen nicht in Urteile ein.

## 3. Messung

- **Pruefpunkte (Zuschauer, Palm-Lesart) [F]:**
  - Je Konfiguration t in {2,0; 2,6; 3,2}, jeweils an drei Lagen: A = (0, 0, v t) Paketmitte, B = (0,6, 0, v t),
    C = (0, 0, v t - 0,6).
  - Das sind 9 je Konfiguration, 18 zusammen; alle liegen in D.
  - phi am Zuschauer = (a/rho) Summe ueber seine Links in die Menge. Links eines Zuschauers sind die maximalen Elemente
    seiner Vergangenheit.
  - Dazu 17 Profilpunkte bei t = 3,2, x = y = 0, z = -1,6 bis 1,6 (nur Bild).
- **Norm:** Zeitscheiben [2,0; 2,5), [2,5; 3,0), [3,0; 3,5), [3,5; 4,0).
  - n_k = Summe |phi|^2 ueber die Elemente der Scheibe / (rho w), w = 0,5. Das schaetzt Integral |phi|^2 d^3x ueber die
    Kugel |x| <= 5 - t.
  - Die Laufstrecke ist nur 2/m; mehr erlaubt das Gebiet bei N ~ 2 x 10^4 nicht.
- **Linkzahl je Element:** L/N, die Zahl der Links durch die Zahl der Elemente.
  - Jeder Link zaehlt einmal, L/N ist also die mittlere Zahl der Vergangenheitslinks je Element. Der Grad waere 2 L/N
    (vgl. Berichtigung in KAUSAL-1).
- **Kontinuum (zwei Wege plus ein dritter):**
  - (a) k-Raum exakt je Mode (Duhamel, Faddeeva) fuer die ungekappte Quelle, achsensymmetrische Hankel/Fourier-Quadratur.
    Daraus phi an allen Punkten und n_c,k.
  - (b) Direkte Faltung mit (3.25), Gauss-Legendre in Kegelkoordinaten, gekappt und ungekappt; ungekappt auch fein.
  - (c) Konturintegral mit 1/(Z^2 + m^2) (rho = inf) auf der Linie Im omega = Gamma.
  - **Bezug fuer KV1 und KV2 [F]:** (b) gekappt, also das exakte Kontinuum fuer die tatsaechlich benutzte Quelle.
    Fuer KV3 dient n_c,k aus (a), ungekappt; der Kappenfehler ist in Abschnitt 8 beziffert.
- **Johnston-Erwartung** E[phi] bei rho = 4 / 8 / 16 an allen Punkten (Kontur, Gamma = 0,8 und 1,4 als Gegenprobe):
  beschreibend. Sie trennt die Abweichung durch endliche Dichte von Codefehlern und Rauschen.
- **Statistik:** Mittel ueber Saaten; SE = Std (ddof = 1)/sqrt(n).
  - Komplex [F, wie KAUSAL-WELLE-1]: SE_c = sqrt(var Re + var Im)/sqrt(n).
  - Relative Streuung = sqrt(var Re + var Im)/|phi_Bezug|.

## 4. Kontrollen (ohne Urteilskraft)

- **Codeprobe** (rho = 1,2, N ~ 1 500, Bloecke 256):
  - GEMM-Links gegen dichtes (C C) in float64
  - C gegen eine unabhaengige Koordinatenpruefung
  - Rekursion gegen dichte Loesung und gegen die abgebrochene Reihe
  - Zuschauer gegen eine Schleife ueber die maximalen Elemente
- **Kontinuum:** (a) gegen (b) ungekappt (grob und fein) und gegen (c); Kappeneffekt (b) gekappt gegen ungekappt.
- **Johnston-Erwartung:** Gamma-Unabhaengigkeit; rho = 10^6 gegen das Kontinuum.
- **Linkzahl-Integral:** zwei Aufloesungen. Bezug ist die feine. Der Unterschied E[L/N] gegen E[L]/E[N] ist
  ~1/(2N) relativ [M], also <= 10^-4.
- **Stabilitaet einzelner Saaten:** max |phi|, Endlichkeit, G je Saat (beschreibend).

## 5. Laeufe

- Nur .69 ueber kleintest.sh, Spuren cpu und cpu6, hoechstens zwei zugleich, je Lauf < 10 min.
- Das Skript bricht vor einer Saat ab, wenn die Zeitgrenze (540 s) sonst ueberschritten wuerde. Fehlende Saaten folgen in
  einem weiteren Lauf, mit denselben Saatnummern.
- **Reihenfolge nach dem Einfrieren:**
  - Spur cpu: kontinuum (rho 4, 8, 16), feld 16 Saaten 1 bis 3, feld 16 Saaten 7 bis 9, feld 4 Saaten 1 bis 12
  - Spur cpu6: probe, feld 16 Saaten 4 bis 6, feld 16 Saaten 10 bis 12, feld 8 Saaten 1 bis 12
  - Danach auswertung4d.py lauf kont aus 4,8,16 12

## 6. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| KV0 | Kontrolle: Die mittlere Linkzahl je Element trifft den exakten Erwartungswert (numerisches Integral fuer das Gebiet) innerhalb 3 Standardfehlern | 80 % |
| KV1 | Das Saatmittel des Pakets trifft die Kontinuumsloesung an mindestens 80 % der Pruefpunkte innerhalb 3 Standardfehlern (groesste Dichte) | 50 % |
| KV2 | [H] Die relative Streuung an den Pruefpunkten ist bei der groessten Dichte kleiner als 50 % und faellt mit rho | 40 % |
| KV3 | Stabil: Die Norm waechst ueber die Laufstrecke um hoechstens den Faktor 1,5 gegenueber dem Kontinuum | 55 % |

- Alle Urteile rechnet code/auswertung4d.py mechanisch.
- "Nicht auswertbar", wenn fuer eine Dichte weniger als 12 Saaten vorliegen oder ein Lauf nicht endliche Werte hat.
- **KV0 [F]:**
  - Je Dichte: abs(Saatmittel L/N - E) <= 3 SE. E ist das feine Integral fuer D (E[L]/E[N]).
  - Eingetroffen, wenn das fuer alle drei Dichten gilt.
- **KV1 [F]:**
  - Bei rho = 16, an den 18 Pruefpunkten: abs(Saatmittel - phi_Bezug) <= 3 SE_c (komplex).
  - Eingetroffen, wenn das an mindestens 80 % der Punkte gilt, also an mindestens 15 von 18.
- **KV2 [F]:**
  - s(rho) ist das geometrische Mittel der relativen Streuung ueber die 18 Pruefpunkte.
  - Eingetroffen, wenn s(16) < 0,5 und s(4) > s(8) > s(16).
  - Beschreibend daneben: strenge Lesart (jeder Punkt < 0,5 bei rho = 16) und die Steigung log s gegen log rho.
- **KV3 [F, wie KAUSAL-WELLE-1]:**
  - R_k = Saatmittel(n_k)/n_c,k; G = R der letzten Scheibe / R der ersten Scheibe.
  - Eingetroffen, wenn G <= 1,5 in allen 6 Faellen (3 Dichten x 2 Konfigurationen).
  - Beschreibend daneben: max R_k und G je Saat.

### 6.1 Eigene Erwartung (Schreibtisch und Kontinuum-Rauch des Code-Agenten [M/E], keine Urteilsregel)

- **Johnston-Erwartung bei endlicher Dichte [M, numerisch im Kontinuum-Rauch, Abschnitt 8]:**
  - Pole von K_P~ (Wachstumsrate Im omega bei k = 0 / k = p):

    | rho | 4 | 8 | 16 |
    |---|---|---|---|
    | Im omega | 0,246 / 0,220 | 0,198 / 0,177 | 0,152 / 0,137 |
    | Re omega | 1,017 / 1,138 | 1,042 / 1,162 | 1,055 / 1,174 |

  - Erste Ordnung 0,61/(omega sqrt(rho)) trifft bei rho = 16 auf 1 % (0,153 / 0,136).
  - An den Pruefpunkten ist E[phi]/phi_Bezug bei rho = 16 im Betrag 1,30 (t = 2) / 1,44 (t = 2,6) / 1,62 (t = 3,2), die
    Phase verschiebt sich um +0,32 bis +0,36 rad. Die relative Abweichung betraegt 0,50 / 0,60 / 0,75.
  - Bei rho = 4 sind es 1,35 bis 1,80 im Betrag und 0,83 bis 1,17 relativ. Bei rho = 10^6: 0,5 %.
- **Erwartung je Vorhersage:**
  - KV0 eingetroffen (85 %): Das Integral ist exakt bis auf 2e-7, und E[L/N] weicht von E[L]/E[N] nur um ~1/(2N) ab.
  - KV1 **nicht** eingetroffen (80 %).
    - Schon die Erwartung liegt bei rho = 16 um 50 bis 75 % neben dem Kontinuum.
    - Mit 12 Saaten fiele das nur unter 3 SE_c, wenn die relative Streuung je Saat ueber ~0,6 bis 0,9 laege. Dann
      scheiterte aber KV2.
    - KV1 und KV2 schliessen sich bei dieser Dichte praktisch aus [M].
  - KV2 offen (50 %). Streuung je Saat geschaetzt 0,2 bis 0,5 bei rho = 16 [H, grobe Abschaetzung des Linkanteils],
    fallend mit rho.
  - KV3 **nicht** eingetroffen (75 %).
    - |E phi|^2 waechst gegenueber dem Kontinuum ueber die Laufstrecke um ~1,7 (rho = 16) bis ~2,1 (rho = 4).
    - Abgeschaetzt aus den Pruefpunktverhaeltnissen und den Polen, noch ohne Rauschleistung.
    - Das waere kein Rauschen, sondern das Anwachsen der Erwartung selbst, mit einer Rate ~ m^4/sqrt(rho), die mit der
      Dichte verschwindet [M].

## 7. Hinweise zur Karte (vor dem Einfrieren offengelegt)

1. **KV1 vermischt zwei Dinge (Hinweis, keine Berichtigung).**
   - Johnston selbst sagt: In 3+1 ist der Erwartungswert nur im Grenzfall unendlicher Dichte das Kontinuum [S, S. 10].
   - Bei rho = 16 ist m^2/sqrt(rho) = 0,25, also nicht << 1.
   - KV1 prueft daher zugleich den Code und den Abstand vom Kontinuumsgrenzfall.
   - Die Regel bleibt wie in der Karte. Beschreibend kommt der Vergleich mit der Johnston-Erwartung bei derselben Dichte
     hinzu (Abschnitt 3).
   - Die Kartenbedeutung "im Mittel richtig" ist bei endlicher Dichte nur als "im Mittel wie Johnstons Erwartung" zu lesen.
2. **Offen gelassen und festgelegt:** sigma, eta, Kappe, Gebiet, Dichten, Saaten; Pruefpunkte und Bezug (KV1, KV2);
   Dichten fuer KV0; Zusammenfassung der Streuung (KV2); Scheiben und Lesart des Wachstumsfaktors (KV3). Alles [F] in
   den Abschnitten 2, 3 und 6.
3. **Laufstrecke:** Die Karte nennt keine Laenge. Bei N ~ 2 x 10^4 erlaubt das Gebiet nur 2/m Laufstrecke nach dem
   Abklingen der Quelle (t = 2 bis 4; Huelle bei t = 2 auf e^(-2)). In 1+1 waren es 20/m.
4. **Kein Kartenfehler in den Formeln:** a, b, V und die Linkdefinition stimmen mit der Quelle [S].

## 8. Rauch (vor dem Einfrieren)

Ordner rauch-69/ (Kopie von /home/fmh/fmhc-physics-remote/runde38-kausal-4d/rauch/); .69-Zeiten in UTC, alle rc = 0.

- **Codeprobe** (05:29:43 bis 05:29:52, rho = 1,2, N = 1 489, L = 32 146):
  - GEMM-Links gleich dichtem C C: ja. C gleich unabhaengiger Koordinatenpruefung: ja.
  - Rekursion gegen dichte Loesung: 4,7e-16. Reihe: 1,8e-16. Zuschauer gegen Schleife: 3,8e-16.
- **Zeitmessung** (05:29:45 bis 05:31:48), Modus zeit, rho = N/V_D:
  - N = 5 029 / 10 007 / 20 037: Links 3,3 / 18,8 / 117 s; Speicher 0,19 / 0,50 / 1,69 GB.
  - Dabei gesehen [E]: L/N = 47,3 / 70,8 / 104,0. Das war bei rho = 3,93 / 7,86 / 15,73, also nicht bei den
    Urteilsdichten.
- **Feld rho = 4, Saaten 91 und 92; rho = 16, Saat 91** (05:34:04 bis 05:36:36):
  - Nur Zeit, Speicher und Endlichkeit angesehen (jq-Auswahl).
  - rho = 4: 5,7 und 6,7 s je Saat. rho = 16: N = 20 633, Links 127 s, gesamt 137 s, 1,87 GB; endlich.
- **Kontinuum** (05:34:01 bis 05:39:04, 303 s):
  - V_D = 1271,583 (Quadratur) gegen 1271,583 (Mittelpunktregel).
  - Direkte Faltung ungekappt gegen k-Raum an 18 Pruefpunkten: <= 3,1e-13 relativ (grob und fein).
  - Kappeneffekt (gekappt gegen ungekappt): 0,08 bis 0,31 %.
  - Kontur rho = inf gegen k-Raum an 70 Punkten: <= 4,8e-6. Johnston-Erwartung Gamma 0,8 gegen 1,4: <= 2e-14.
    rho = 10^6 gegen Kontinuum: <= 0,67 %.
  - Linkzahl-Integral E[L]/E[N] = 47,45286 / 71,14680 / 105,37049 (rho = 4 / 8 / 16); fein 47,45288 / 71,14681 /
    105,37051, Unterschied <= 4e-7 relativ.
  - Norm n_c,k (eta = 0): 2,53 / 1,81 / 1,09 / 0,37; (eta = 0,5): 2,49 / 1,75 / 0,96 / 0,31. Sie faellt, weil die Kugel
    |x| <= 5 - t schrumpft und das Paket auslaeuft.
  - Pole und E[phi]/phi_Bezug wie in Abschnitt 6.1 (Werkzeug code/kont_blick.py, nur Kontinuumsdaten, 05:40 UTC).
- **Pfadprobe auswertung4d.py** auf dem Rauchordner (rho = 4 und 16, Saaten 91 und 92): rc = 0, vier Bilder und
  auswertung.json geschrieben. Angesehen habe ich nur die Schluessel, nicht die Urteile, Bilder oder Werte.
- **Folge fuer den Plan:** rho = 16 als groesste Dichte (N ~ 2 x 10^4), 12 Saaten je Dichte, drei Saaten je Lauf bei
  rho = 16. Keine Schwelle nach einem Rauchwert geaendert.
- **Reihenfolge offengelegt:**
  - Die Pole (05:36 UTC) hatte ich gesehen, bevor ich die Urteilsregeln schrieb (ab 07:37 CEST). Die
    Pruefpunktverhaeltnisse (kont_blick, 05:40 UTC) sah ich erst danach.
  - Die Lesart "alle drei Dichten" fuer KV3 folgt KAUSAL-WELLE-1. Nach den Polen macht sie KV3 schwerer: Die Rate ist bei
    rho = 4 am groessten.
  - Beschreibend berichte ich deshalb auch das Urteil nur bei rho = 16.

## 9. Einfrieren

- Kopie PLAN.md.eingefroren-JJJJMMTT-HHMMSS (Zeit per date), Code-Kopien mit derselben Endung, sha256 in
  code/pruefsummen-einfrieren.txt.
- Danach aendern sich Plan und Urteilsregeln nicht. Code nur bei echten Fehlern, offengelegt im ERGEBNIS.
