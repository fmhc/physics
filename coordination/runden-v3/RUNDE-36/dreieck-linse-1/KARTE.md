# DREIECK-LINSE-1: Wirkt eine Fuenfer-Spitze auf Q-Baelle wie eine Linse aus der 2+1-Gravitation? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 01:18:36 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Idee A2 aus IDEEN-EVOLUTION/GEN-03.md.
  - Gedankenexperiment GE3: In 2+1 Dimensionen ist eine Masse ein Kegel mit Fehlwinkel delta = 8 pi G M, ohne
    Ortskraft [L: Deser/Jackiw/'t Hooft 1984; Dossier E3].
  - Finns Dreiecke: Eine Ecke mit fuenf Dreiecken ist so ein Kegel (delta = pi/3).
  - Vorlauf: EINFANG-1 und -2 (Einfang nur unter v ~ 0,011 bei frontalem Lauf), LICHT-1, KEGEL-Q (Muldentiefe 1,447 bei
    Q = 200 an der Fuenfer-Spitze).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Geodaeten auf dem Kegel** [M]: Abgerollt ist der Kegel eine Ebene, aus der ein Keil mit Winkel delta fehlt.
  - Zwei Bahnen, die links und rechts an der Spitze vorbeilaufen, kreuzen sich danach unter dem Winkel delta,
    unabhaengig vom Abstand b. Das ist das Doppelbild der kosmischen Strings [L: Vilenkin 1981].
  - Fuer eine einzelne Bahn ist die "Ablenkung" eine Frage der Bezugswahl. Messbar ist der Winkel zwischen den beiden
    Bahnen.
- **Fuenfer-Spitze:** delta = pi/3 = 60 Grad.
- **Q-Ball:** Weit weg folgt er der Geodaete. Nahe der Spitze spuert er die kurzreichweitige Mulde (KEGEL-Q, Schwanz
  ~ exp(-kappa d)); das gibt zusaetzliche Anziehung bei kleinem b.

## Test (Code-Agent)

- **Code-Basis:** RUNDE-34/einfang-1/code/einfang.py (M1, beta = 1/2, Q = 200, triangulierte Flaeche mit einer
  Fuenfer-Ecke). Dazu RUNDE-34/einfang-1/ERGEBNIS.md und RUNDE-34/licht-1/ (Messgroessen; Schwerpunkt per
  Ladungsfluss bzw. glattem Fenster, keine Schwerpunktmasse direkt an der Spitze).
- **Netz:** gross genug fuer b bis 40 und lange gerade Strecken davor und danach. Gegenprobe: flaches Netz ohne Spitze.
- **Laeufe:** Startschnelle v0 = 0,05 (weit ueber der Einfangschwelle), Stossparameter b = +-10, +-20, +-30, +-40
  (links und rechts).
- **Messung:** Ein- und Auslaufrichtung je Bahn ueber Geradenausgleich der Schwerpunktbahn fern der Spitze.
  - Den Winkel zwischen den Auslaufrichtungen der Bahnen +b und -b bestimmen, ueber die Entwicklungskarte des Netzes
    entlang eines Wegs, der die Spitze nicht umrundet.
  - Dazu die Endschnelle.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| D0 | Kontrolle flaches Netz: Winkel zwischen den Bahnen +b und -b < 0,5 Grad fuer alle b; Schnelle konstant auf 1 % | 85 % |
| D1 | Fuenfer-Spitze, b = 20, 30, 40: Die beiden Bahnen laufen danach unter 60 Grad +- 2 Grad aufeinander zu, unabhaengig von b (Streuung ueber b < 2 Grad) | 70 % |
| D2 | [H] b = 10: zusaetzliche Ablenkung zur Spitze hin, Winkel mindestens 3 Grad groesser als 60 Grad (Mulde) | 50 % |
| D3 | Endschnelle = Startschnelle innerhalb 2 % fuer b >= 20 (kein Energieverlust ohne Spitzennaehe) | 75 % |

**Bedeutung (vorab):**
- D1 und D3 treffen ein: Eine Ecke mit fuenf Dreiecken wirkt auf Q-Baelle wie eine Masse in der 2+1-Gravitation. Keine
  Kraft in der Ferne, aber ein fester Knick in den Bahnen, wie ein kosmischer String, der Doppelbilder macht.
  - Finns "Masse = Fehlwinkel" bekommt damit eine sichtbare Wirkung: Linsen statt Anziehung.
- D2 trifft ein: In der Naehe kommt die kurzreichweitige Mulde dazu. Das ist der Unterschied zwischen einem endlich
  grossen Q-Ball und einem Punktteilchen.
- D1 verfehlt: Q-Baelle folgen den Geodaeten nicht, auch fern der Spitze; beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (nicht cpu, cpu2, cpu3, cpu4, cpu5, cpu6,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
