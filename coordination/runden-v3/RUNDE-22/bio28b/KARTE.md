# Bio 28b: Ueberleben die Toechter eines verschmolzenen Drehballs ohne Randverlust? (Runde 22)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 19:01:37 CEST (date), vor jedem Lauf.
- Herkunft:
  - Bio 28 weiter (R21, Zufallskarte, verworfen nach Wortlaut): Gefuetterte Drehbaelle verschmelzen bei t ~ 2 und
    teilen sich bei t = 7 bis 14 in Stuecke ohne Windung.
  - Die Stuecke tragen 110 bis 175 Einheiten fast ihre ganze Ladung und gehen erst am Absorberrand (ab ~30) verloren.
    Folgefrage Bio 28b im Pool, hier als gewaehlte Karte.
- Ableitbarkeitspruefung vor den Vorhersagen (Lehre R21):
  - Dass die Stuecke Windung 0 tragen, ist aus R21 bekannt und wird **nicht** vorhergesagt.
  - Ihr Ueberleben ohne Rand und ihre Familienlage sind aus R21 nicht ablesbar.
- Explorativ (v3), Hypothesen [H]. Minibudget: Laeufe je hoechstens 10 min.

## Test

- Code und Parameter aus RUNDE-05/r5-2d-a (r5_2d_a.py) bzw. RUNDE-21/bio28-weiter, unveraendert, aber in einer Box mit
  doppelter Kantenlaenge (oder Absorberrand so weit aussen, dass die Stuecke ihn bis T = 300 nicht erreichen;
  dokumentieren).
- Laeufe: w60 und w75, je mit 1 und 2 Nachbarn, grob und fein.
- **K0:** Fruehe Zeiten wie in R21 (Verschmelzen bei 1,5 bis 2, Teilung bei 7 bis 14) auf +-1.
- Bis T = 300 je Stueck: Q, Anteil an der Ladung zur Teilungszeit, Schwerpunkt, Geschwindigkeit, Rundheit und
  Klassifikation mit dem in KF-EICH geeichten Klassifikator aus RUNDE-06/kf5 (Familie m = 0). Wie der Klassifikator auf
  die R5-Ausgaben angewandt wird, legt der Plan vorab fest.

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| D0 | K0 bestanden | 85 % |
| D1 | In mindestens 3 der 4 gefuetterten Laeufe ueberleben bei T = 300 mindestens zwei Stuecke mit je >= 50 % ihrer Ladung zur Teilungszeit | 60 % |
| D2 | Mindestens eines dieser Stuecke ist bei T = 300 "auf" und "rund" (auf beiden Gittern) | 45 % |

**Bedeutung (vorab):**
- D1 und D2 treffen ein: Der gefuetterte Drehball zerfaellt in Q-Ball-Toechter ohne Windung. Das ist eine Teilung,
  aber keine Groessengrenze im Sinn von Bio 28 [H].
- D1 trifft nicht ein: Die Toechter zerfliessen auch ohne Rand.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000b (bei Belegung p4000a), je <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 75 min.
