# Bio 28c: Wohin geht der Drehimpuls des gefuetterten Drehballs? (Runde 22)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 19:37:13 CEST (date), vor jedem Lauf und jeder Auswertung.
- Herkunft:
  - Bio 28b (R22): Der gefuetterte Drehball (m = 1) verschmilzt mit nicht drehenden Nachbarn und teilt sich in zwei
    Toechter ohne Windung. Sie fliegen mit v = 0,16 bis 0,30 auseinander und ueberleben; 3 von 8 sind "auf".
  - Der Drehball traegt aber Drehimpuls J = m Q_m1. Wohin geht er?
- Ableitbarkeitspruefung: Drehimpulse wurden in R5, R21 und R22 nicht ausgegeben; die Ausgaenge sind nicht ablesbar.
  Bekannt sind nur Flugrichtung und Geschwindigkeit der Toechter, nicht ihr Bahndrehimpuls.
- Explorativ (v3), Hypothesen [H]. Minibudget: Laeufe je hoechstens 10 min.

## Test

- Die vier gefuetterten Laeufe aus Bio 28b (Box dreifach), nur grob, mit Ausgabe der Feldgroessen bis T = 90, also bevor
  Abstrahlung den Absorberrand (ab ~107) erreicht:
  - Gesamt-Drehimpuls L_z = Integral (x P_y - y P_x) mit der Impulsdichte P_i = -(psi_t* d_i psi + c.c.); Vorzeichen und
    Normierung so, dass ein exakter Drehball m = 1 L_z = Q ergibt
  - Aufteilung zu den Zeiten 0, 20, 40, 60, 90 in drei Teile:
    - (a) Bahndrehimpuls der Toechter um den gemeinsamen Ladungsschwerpunkt (aus Schwerpunkt und Impuls je Gebiet)
    - (b) Eigendrehimpuls je Gebiet um den eigenen Schwerpunkt
    - (c) Rest ausserhalb der Gebiete (Abstrahlung)
- **K0:**
  - Ein exakter Drehball m = 1 allein ergibt L_z = Q auf 1 %.
  - Der Gesamt-Drehimpuls ist bis T = 90 auf 1 % erhalten, solange nichts den Rand erreicht.

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| J0 | K0 bestanden | 80 % |
| J1 | Bei T = 60 tragen die Toechter als Bahndrehimpuls (a) mindestens 50 % des Anfangsdrehimpulses, in mindestens 3 der 4 Laeufe | 55 % |
| J2 | Der Eigendrehimpuls (b) der Toechter ist bei T = 60 kleiner als 10 % des Anfangsdrehimpulses | 70 % |

**Bedeutung (vorab):**
- J1 und J2 treffen ein: Der innere Drehimpuls des Drehballs geht beim Zerfall in die Bahnbewegung der Toechter ueber,
  wie bei einem sich teilenden rotierenden Tropfen [H, im Modell].
- J1 trifft nicht ein: Der Drehimpuls geht ueberwiegend in Abstrahlung (c); Groesse von (c) angeben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000b (bei Belegung p4000a), je <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 60 min.
