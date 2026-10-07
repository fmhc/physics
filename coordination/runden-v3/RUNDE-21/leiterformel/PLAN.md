# PLAN LEITERFORMEL (Runde 21)

- Code-Agent. Start 2026-10-02 18:36:32 CEST (date). Plan geschrieben ab 18:43:40 CEST (date), vor jeder Rechnung.
- Verbindlich aus der Karte (unveraendert): k_innen aus dem a-b-Block wie Runde 18; K0; Delta Phi = k_innen(R_n+1) R_n+1
  - k_innen(R_n) R_n je benachbartem Sprossenpaar; Vergleich mit pi/k_innen; LF0 bis LF4; Bedeutung. Nichts davon wird
  nach dem Ergebnis geaendert.
- Gelesen: KARTE; RUNDE-18/huellen-leiter ERGEBNIS, PLAN, PLAN-NACHTRAG-1 bis 4, KARTE, code/ (stille3.py,
  huellen_leiter.py), aus/laeufe/stellen.json, aus/prof-st1/profile-info.json; ERGEBNIS und aus/ (nur die genannten
  JSON) von RUNDE-19/huellen-leiter-3, RUNDE-20/sprossen-vorab, RUNDE-19/huellen-dipol, RUNDE-20/huellen-quadrupol,
  RUNDE-21/sprossen-l1l2. Auf der .69: Ordner runde18-huellen-leiter/aus/prof-st1 (Profile Stufe 1).

## 1 k_innen (Runde 18, unveraendert)

- Formel woertlich aus RUNDE-18 ERGEBNIS Abschnitt 4 (Schreibtisch-Abschaetzung): Im Balleinneren (g = 0, S = S0)
  - Va = omega^2 + S0 (3 S0 - 2), gs = S0 (3 S0 - 2), Ea = (w + rho)^2, Eb = (w - rho)^2, w = sqrt(omega^2)
    (wie stille3.energien).
  - k_innen^2 = -[(Va - Ea + Va - Eb)/2 - sqrt(((Ea - Eb)/2)^2 + gs^2)].
- **Welcher Eigenwert:** Der a-b-Block von M - E im Inneren ist [[Va - Ea, gs], [gs, Va - Eb]] (stille3: Maa = U_S + S U_SS,
  Mab = S U_SS, mit U_S = omega^2, U_SS = 3 S - 2). k_innen gehoert zum unteren Eigenwert lambda_- = (Va - Ea + Va - Eb)/2
  - sqrt(...); die Mode schwingt (u'' = lambda_- u, lambda_- < 0), k_innen = sqrt(-lambda_-). Wie Runde 18 (Minus vor der
  Wurzel). Berichtet je Stelle: lambda_- < 0 und lambda_+ > 0 (sonst Merker).
- **S0 (Inneramplitude) je Stelle, vorab festgelegt:** S0 = f(0)^2 des Hintergrundprofils bei omega^2 der Stelle, Stufe 1
  (hp = 0,01), auf dem Rechenweg der Vorlaeufer (HUELLEN-LEITER cmd_umlauf): Anker = gespeichertes Runde-18-Profil der
  naechsten Zeile mit omega^2 <= omega^2 der Stelle (.69, runde18-huellen-leiter/aus/prof-st1, nur gelesen), dann
  stille3.Umgebung(M2, Anker).profil(omega^2) (Fortsetzung auf dem Gitter des Ankers). f0 aus stille3.profil_info.
  - Begruendung: An den Stellen selbst sind keine Profile gespeichert; gespeichert sind nur die Zeilen. Gerechnet wird
    also nur das fehlende Profil an der Stelle, Anker werden nicht neu gerechnet. Fehlt ein Ankerprofil, wird es mit
    huellen_leiter.cmd_profile in meinem Ordner gerechnet und das gemeldet.
  - Kontrollen (berichtet, keine Wertung): Rchi dieses Profils gegen das R der Liste; chi0 (Formel setzt g = 0 innen
    voraus; Merker bei chi0 > 1e-3); S0_wurzel = (2 + sqrt(6 omega^2 - 2))/3 (U_S(S0) = omega^2 bei g = 0) und die
    Aenderung von Delta Phi / pi, wenn man S0_wurzel nimmt.
- R in Phi = k_innen R: das R der Stellenliste (Huellenradius chi = 1/2), wie die Karte.

## 2 Stellen (Grundlage)

- l = 0: RUNDE-18 aus/laeufe/stellen.json (88, Stufe 1: w2, rho, R, umlauf_1); die 8 HUELLEN-LEITER-3-Sprossen
  (k = 0 bis 3) mit den Stufe-1-Werten aus SPROSSEN-VORAB aus/l4-d1/l4-auswertung.json (Eintraege mit Quelle "HL3";
  dort alle 8 angenommen, auch k = 3); die 12 SPROSSEN-VORAB-Sprossen (aus/test/test-auswertung.json, st1). Die 4
  Runde-18-Stellen in deren L4 sind Duplikate und werden aus Runde 18 genommen.
- l = 1: HUELLEN-DIPOL aus/laeufe/stellen.json (19); SPROSSEN-L1L2 aus/test/test-auswertung.json, l = 1, angenommen
  (Satz A und Satz B, 8).
- l = 2: HUELLEN-QUADRUPOL aus/laeufe/stellen.json (15); SPROSSEN-L1L2 l = 2, angenommen (Satz A und B, 5).
  - **Stelle l = 2, k = 2, R = 22,2923 (Satz B, formal nicht angenommen):** In SPROSSEN-L1L2 Nachtrag 1 als stille Stelle
    belegt (Newton in 1 Schritt, E1, Rang 2, sigma2/sigma1 4,6e-12 / 1,3e-11, Rechteck-Umlauf +1 aufgeloest auf beiden
    Stufen; aus/nachtrag1/umlauf-st1.json). Sie wird aufgenommen und **gekennzeichnet** ("nachtraeglich belegt"). LF2
    wird mit ihr gewertet; Nebenlesart ohne sie wird berichtet.
- Kurve k = Rang aus der jeweiligen Quelle (in allen Quellen auf beiden Stufen = k geprueft). Umlauf: Runde 18, DIPOL,
  QUADRUPOL Zellen-Umlauf Stufe 1; HL3 und SPROSSEN-VORAB F-Umlauf Stufe 1; SPROSSEN-L1L2 Rechteck-Umlauf Stufe 1
  (alle in der Konvention der Runde 18, von den Vorlaeufern geprueft).
- Doppelte (gleiches l, k, abs(Delta R) < 0,01) werden einmal gezaehlt (Vorrang: Quelle mit vollstaendiger Suche).

## 3 Paare

- Je (l, k) die Stellen nach R ordnen; Paar = zwei in R aufeinanderfolgende Stellen derselben Liste.
- **Gezaehlt (ohne Luecke)**, wenn (i) der Umlauf von Stelle zu Stelle wechselt und (ii) Delta R <= 1,5 x Median der
  Abstaende dieser Kurve. Sonst Merker "Luecke?", nicht gezaehlt, berichtet. Begruendung: Eine fehlende Sprosse
  dazwischen gaebe zweimal den Abstand und gleichen Umlauf.
- Je Paar: Delta R = R_n+1 - R_n; Phi = k_innen R je Stelle; Delta Phi; Delta Phi / pi; Rest = Delta Phi / pi - 1.
  pi/k_innen (Mittel beider Stellen) = (pi/k_n + pi/k_n+1)/2; relative Abweichung davon zum Abstand:
  (pi/k_innen Mittel) / Delta R - 1.

## 4 K0 (zuerst, eigener Lauf vor allen Stellen)

- An den Runde-18-Stellen Nr 81 (k = 0; omega^2 0,76524821, rho 1,02705186) und Nr 88 (k = 1; 0,764059, 1,1883409),
  Lage aus stellen.json: pi/k_innen mit S0 nach Abschnitt 1.
- **Bestanden**, wenn abs(pi/k_innen - 2,37) <= 0,01 (Nr 81) und abs(pi/k_innen - 2,07) <= 0,01 (Nr 88) (Kartenzahlen).
  Berichtet auch gegen die dreistelligen Runde-18-Werte 2,368 / 2,065 und mit S0_wurzel.
- Faellt K0 durch: Umsetzung gegen die Formel pruefen; nur Programmfehler beheben (dokumentiert, sha256), keine
  Definition aendern. Bleibt K0 durchgefallen, laufen die Stellen trotzdem, alle Ergebnisse unter Vorbehalt "K0 nicht
  bestanden".

## 5 Wertung LF0 bis LF4 (vorab operationalisiert)

- LF0: K0 bestanden (Abschnitt 4).
- LF1: Paare mit l = 0, gezaehlt, R_n >= 15 (R_n = kleineres R des Paares). Eingetroffen, wenn abs(Delta Phi/pi - 1)
  <= 0,03 bei mindestens 80 % dieser Paare.
- LF2: Paare mit l = 1 oder 2 (gepoolt), gezaehlt, R_n >= 10. Eingetroffen, wenn abs(Delta Phi/pi - 1) <= 0,03 bei
  mindestens 70 % dieser Paare. Mit der gekennzeichneten Stelle l = 2 / 22,29; Nebenlesart ohne sie; je l berichtet.
- LF3: alle gezaehlten Paare mit l = 0. Eingetroffen, wenn Mittel abs(Delta Phi/pi - 1) < Mittel abs((pi/k_innen
  Mittel)/Delta R - 1). Nebenlesart R_n >= 15 berichtet.
- LF4: alle gezaehlten Paare (alle l, alle R). Eingetroffen, wenn mindestens 80 % der Paare beim Rest dasselbe
  Vorzeichen haben (Anteil des haeufigeren Vorzeichens >= 0,8). Je l und fuer die LF1-/LF2-Mengen berichtet.
- Bedeutung woertlich nach Karte: LF1 und LF2 eingetroffen -> "Die Leitern fuer l = 0, 1, 2 folgen einer
  Phasenbedingung der Innenwelle [H, im Modell]. Das waere ein geschlossener Baustein der Gesamtformel." LF1 nicht
  eingetroffen -> "Das Halbwellenbild ist nur qualitativ; die Restabweichung wird beschrieben." Andere Kombination: keine
  vorab festgelegte Bedeutung, so berichtet.

## 6 Beschreibung der Restabweichung (vorab festgelegt, keine Wertung)

- Je l: Mittel, Standardabweichung, Minimum, Maximum des Rests; Spearman(Rest, R_n).
- l = 0: Mittel des Rests je k (Kurven mit >= 3 gezaehlten Paaren); Rest gegen R auf k = 0.
- [H, getrennt] Fuer l >= 1: Vergleich mit dem Abstand aufeinanderfolgender Nullstellen von j_l (McMahon,
  z_n ~ beta_n - l(l+1)/(2 beta_n)): erwarteter Rest ~ l(l+1)/(2 pi) (1/Phi_n - 1/Phi_n+1). Nur Beschreibung.

## 7 Laeufe (.69, kleintest.sh, Spuren cpu bis cpu4, cpu6; je <= 600 s)

- Code: code/leiterformel.py (eigen); code/stille3.py und code/huellen_leiter.py unveraendert aus RUNDE-18 kopiert
  (sha256 gegen Runde 18 geprueft). Eingabe hilfs/stellen-eingabe.json (per jq aus den Quellen gebaut, Abschnitt 2).
- V0: py_compile. V1: K0 (Befehl k0). V2: alle Stellen (Befehl stellen, ggf. in Teilen auf mehrere Spuren). V3:
  Auswertung (Befehl ausw: Paare, LF0 bis LF4, Beschreibung). Ausgaben nach aus/.
- Programmfehler werden behoben und mit sha256 dokumentiert; das Verfahren bleibt. Nachtraege nur eingefroren und als
  nachtraeglich markiert.
