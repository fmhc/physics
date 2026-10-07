# LICHT-1: Wie schnell kann eine Kegelmulde einen Q-Ball machen? (Runde 34)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 18:56:41 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn ~18:31: "beschleunigen eingefangene baelle auf lichtgeschwindigkeit?"
  - Antwort der Leitung am Schreibtisch (RUNDE-34.md): am Muldengrund der Fuenfer-Ecke v = 0,135 c; Obergrenze fuer
    extreme Kegel ~0,42 c.
  - Finn ~18:55: "rechne das durch".

## Schreibtisch (vor jeder Rechnung)

- **Energieerhaltung** [M]: Ein Ball, der aus der Ferne fast in Ruhe startet, hat am Muldengrund
  gamma = 1 + (K0 + B)/E, also v = sqrt(1 - 1/gamma^2). Q = 200, M1 mit beta = 1/2, E_flach = 157,295.
- **Muldentiefe einer Spitze mit n Dreiecken** (Gesamtwinkel n pi/3, s = 6/n): exakte Abbildung fuer den zentrierten
  Ball B(s) = E_flach(Q) - E_flach(sQ)/s (KEGEL-Q, auf 0,05 % bestaetigt bei n = 5).
- **Duennwand-Naeherung** [H, grob]: E_flach(Q) ~ omega_min Q + sigma sqrt(Q) mit sigma sqrt(200) = 15,87, also
  B(s) ~ 15,87 (1 - 1/sqrt s).
  - n = 5 (s = 1,2): B ~ 1,38 (exakt 1,4465), v ~ 0,135
  - n = 4 (s = 1,5): B ~ 2,9, v ~ 0,19
  - n = 3 (s = 2): B ~ 4,6, v ~ 0,24
  - n = 2 (s = 3): B ~ 6,7, v ~ 0,28
  - n = 1 (s = 6): B ~ 9,4, v ~ 0,33
  - s -> unendlich: B -> E_flach - omega_min Q = 15,9, v -> 0,42
- **Eingefangene Baelle** verlieren je Durchgang Energie (EINFANG-1), werden also langsamer.

## Test (Code-Agent)

- **Teil A (statisch):**
  - E_flach(Q') mit dem Radialloeser aus KEGEL-Q (RUNDE-26/kegel-q/code/kegel_q.py) fuer Q' = s * 200 mit
    s = 6/5, 6/4, 6/3, 6/2, 6/1 und groesser (z. B. 12, 24, 48), so weit der Loeser traegt.
  - Daraus B(s), gamma, v am Grund.
  - Kontrolle n = 5 gegen KEGEL-Q.
- **Teil B (dynamisch, mit dem EINFANG-1-Code** RUNDE-34/einfang-1/code/einfang.py):
  - Netz mit einer Dreier-Spitze (n = 3, Defizit pi, wie die Ecke eines Tetraeders), Ball startet fast in Ruhe
    (v0 = 0,01) im Abstand ~25, frontal.
  - Gemessen: hoechste Schwerpunktgeschwindigkeit beim ersten und beim zweiten Durchgang, Energiebilanz.
  - Dazu B(s = 2) statisch auf demselben Netz (Ball auf der Spitze), damit der Vergleich mit der Energieerhaltung auf
    demselben Gitter steht.
  - Falls das Netz mit n = 3 nicht sauber traegt: n = 4, offenlegen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| L0 | Kontrolle: Die exakte Abbildung bei s = 1,2 trifft B = 1,4465 (KEGEL-Q, Q = 200) auf 0,2 % | 90 % |
| L1 | Grundgeschwindigkeit aus Teil A: n = 4: 0,15 bis 0,23; n = 3: 0,19 bis 0,29; n = 1: 0,26 bis 0,40; fuer alle s unter 0,45 | 75 % |
| L2 | Teil B: Die hoechste gemessene Schwerpunktgeschwindigkeit beim ersten Durchgang liegt innerhalb 15 % des Werts aus Energieerhaltung mit dem statischen B(s = 2) desselben Netzes | 70 % |
| L3 | Teil B: Beim zweiten Durchgang ist die Hoechstgeschwindigkeit kleiner als beim ersten (der Ball wird langsamer, nicht schneller) | 85 % |

**Bedeutung (vorab):**
- L1 bis L3 treffen ein: Kegelmulden beschleunigen Q-Baelle hoechstens auf einen Bruchteil der Lichtgeschwindigkeit,
  begrenzt durch den Oberflaechenanteil der Energie; eingefangene Baelle werden langsamer.
- L2 trifft nicht ein: Es gibt einen zusaetzlichen Beschleunigungs- oder Bremsmechanismus (Verformung, Gitter).
  Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (P4000- oder CPU-Spur; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 75 min.
