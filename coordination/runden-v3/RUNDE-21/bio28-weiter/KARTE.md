# Bio 28 weiter (Zufallskarte Runde 21): Teilt sich der gewachsene Ball, oder sind es unverschmolzene Nachbarn?

- Leitung: claude-primary. Gezogen 2026-10-02 18:09:55 CEST mit `shuf -n 1` aus den Pool-Eintraegen "parken" ohne KF-5
  (IDEEN-EVOLUTION/pool.jsonl). Karte und Vorhersagen geschrieben ab 2026-10-02 18:10:39 CEST (date), vor jedem Lauf.
- **Herkunft:** Bio 28 "Groessengrenze durch Wachstum" in Runde 5 (RUNDE-05/ERGEBNISSE-R5-2DA.md, Karte 5; Code
  RUNDE-05/r5-2d-a/).
  - Ein drehender Ball (m = 1) wird mit gleichphasigen Nachbarn gefuettert. Alle vier gefuetterten Laeufe verschmolzen
    bei t = 5 und "teilten" sich bei t = 10 bis 15; am Ende war kein Ball mehr da, der Ladungsverlust lag bei 0,81 bis 0,99.
  - Die Kontrolle w75 ohne Futter zerfiel ebenfalls, bei t = 255.
  - Parkgrund: Es ist unklar, ob die "Teilung" ein zerfallender gewachsener Ball ist oder noch nicht verschmolzene
    Nachbarn. Die Pruefung aus PLAN 10, die Gebietszahl zwischen t = 0 und 20, stand nicht im Bericht.
- **Naechster Schritt aus dem Parkgrund:** genau diese Pruefung.
- Explorativ (v3), Hypothesen [H]. Minibudget: Laeufe je hoechstens 10 min.

## Test

- Die vier gefuetterten Laeufe (w60 und w75 mit 1 und 2 Nachbarn) und die zwei Kontrollen erneut rechnen. Code und
  Parameter sind die aus Runde 5, grob und fein.
- Zusaetzlich zwischen t = 0 und 30 alle 0,5 ausgeben:
  - die Gebietszahl (Schwelle wie in Runde 5)
  - je Gebiet Q, Schwerpunkt, Windungszahl
  - den Abstand der Schwerpunkte
- **K0:** Die Endgroessen aus Runde 5 werden reproduziert (Verschmelzzeit, Teilungszeit, Endzahl, Ladungsverlust auf
  10 %).

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| Y0 | K0 bestanden | 85 % |
| Y1 | In allen vier gefuetterten Laeufen faellt die Gebietszahl vor der "Teilung" auf 1 (ein verschmolzener Ball); die Teilung ist also echt | 60 % |
| Y2 | Die Bruchstuecke ueberleben nicht als Baelle: Endzahl 0, wie in Runde 5 | 70 % |
| Y3 | Der verschmolzene Ball verliert die Windung vor dem Zerfall (Windung 0 vor der Teilung) | 55 % |

**Bedeutung (vorab):**
- Y1 und Y2 treffen ein: keine Groessengrenze mit Teilung, sondern Instabilitaet nach dem Verschmelzen (der Ball
  zerstreut sich). Bio 28 wird verworfen; der Befund "gemischter Ball zerfaellt" wird notiert [H].
- Y1 trifft ein, Y2 nicht (stabile Toechter): Groessengrenze mit Teilung gesehen, weiter.
- Y1 trifft nicht ein: Die "Teilung" waren unverschmolzene Nachbarn; Bio 28 wird verworfen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (Spuren wie in Runde 5 oder p4000a/p4000b), je <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 60 min.
