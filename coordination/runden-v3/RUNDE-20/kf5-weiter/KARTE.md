# KF-5 weiter (Zufallskarte Runde 20): Landen die Tropfen aus der 2D-Geburt auf der Q-Ball-Familie?

- Leitung: claude-primary. Gezogen 2026-10-02 17:45:57 CEST mit `shuf -n 1` aus den 71 Pool-Eintraegen "parken"
  (IDEEN-EVOLUTION/pool.jsonl). Karte und Vorhersagen geschrieben ab 2026-10-02 17:47:31 CEST (date), vor jedem Lauf.
- **Herkunft:** KF-5 in Runde 6 (RUNDE-06/ERGEBNISSE-R6-B.md, Abschnitt KF-5; Code RUNDE-06/kf5/).
  - In 2D entstehen getrennte Tropfen, kein Netz.
  - Die Kernfrage blieb nicht entscheidbar: Liegen die Tropfen auf der Q(omega)-Familie, also Stufe 5 der
    Stabilitaetsleiter (bildungsfaehig)? Zur Zeit T = 800 waren die meisten Tropfen "nicht rund" oder "unentschieden",
    kein einziger "auf".
  - Die Endzustaende (T = 800) liegen auf der .69: /home/fmh/fmhc-physics-remote/runde6-kf5/lauf-69/ausgabe/*_felder.pt.
- **Naechster Schritt aus dem Parkgrund:** laenger laufen lassen, damit die Tropfen abrunden, und dann mit dem
  **unveraenderten** Klassifikator aus Runde 6 erneut einordnen.
- Explorativ (v3), Hypothesen [H]. Minibudget wie jede Karte: Laeufe je hoechstens 10 min.

## Test

- Arm s03 (S0 = 0,3) auf beiden Gittern (grob aus der Mehrarm-Datei, fein aus der eigenen Datei) ab T = 800 mit demselben
  Integrator und denselben Parametern bis T = 2000 fortsetzen. Auswertung bei T = 1200, 1600, 2000.
- Wenn die Zeit reicht, zusaetzlich s01 fein.
- Klassifikation ("rund", "auf" / "neben" / "unentschieden" zur Familie, E/Q-Abstand) **genau wie in Runde 6**: dieselben
  Funktionen, Schwellen und Familiendatei familie_2d_m0.json.
- Kontrolle K0: Der Klassifikator, auf die gespeicherten T = 800-Zustaende angewandt, muss die Runde-6-Urteile
  reproduzieren.

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| Z0 | K0: T = 800-Urteile aus Runde 6 reproduziert | 85 % |
| Z1 | s03 bei T = 2000: mindestens 2 Tropfen "rund", auf beiden Gittern | 55 % |
| Z2 | s03 bei T = 2000: mindestens ein Tropfen "auf" der Familie, auf beiden Gittern | 35 % |
| Z3 | Fuer jeden Tropfen ohne Verschmelzung ist der Abstand zur Familie bei T = 2000 kleiner als bei T = 800 | 65 % |
| Z4 | L3: grob und fein stimmen in Tropfenzahl und Urteil je Tropfen ueberein | 60 % |

**Bedeutung (vorab):**
- Treffen Z2 und Z3 ein: Tropfen aus der Geburt laufen auf die Q-Ball-Familie zu. M1 waere in 2D bildungsfaehig (Stufe 5)
  [H, im Modell].
- Trifft Z3 nicht ein: Auf dieser Zeitskala gibt es keine Annaeherung; KF-5 wird verworfen.
- Sonst: parken mit Grund.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a oder p4000b (GPU, wie Runde 6).
- Plan vor dem ersten Lauf einfrieren. Zeitbox 75 min.
