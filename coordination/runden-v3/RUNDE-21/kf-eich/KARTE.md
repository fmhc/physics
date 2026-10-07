# KF-EICH: Positive Eichprobe des Familien-Klassifikators aus Runde 6 (Runde 21)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 18:20:33 CEST (date), vor jedem Lauf.
- Herkunft: KF-5 weiter (Runde 20, Zufallskarte), geparkt mit Grund.
  - Der Klassifikator aus Runde 6 ("auf" / "neben" / "unentschieden" zur Q(omega)-Familie, "rund" / "nicht rund") wurde
    nie an einem Objekt geeicht, das sicher auf der Familie liegt.
  - In Runde 6 und Runde 20 sagte er nie "auf". Ohne Eichung ist unklar, ob das an den Tropfen oder am Klassifikator
    liegt.
  - Schwerpunkt: Stufe 5 der Stabilitaetsleiter (bildungsfaehig).
- Explorativ (v3), Hypothesen [H]. Minibudget: Laeufe je hoechstens 10 min.

## Test

- Code aus RUNDE-06/kf5 (kf5_geburt.py) und die Familiendatei familie_2d_m0.json, unveraendert importiert.
- Auf demselben Gitter wie Runde 6 (grob und fein, Box 96) werden einzelne exakte Familien-Q-Baelle (m = 0) gesetzt:
  - **Satz E (exakt):** drei Baelle mit omega aus der Familiendatei, eines davon im Bereich der Tropfen aus Runde 6 und
    20 (omega ~ 0,72 bis 0,73), dazu zwei weitere (z. B. omega^2 0,60 und 0,70). Je ein Lauf ruhend, einer bewegt (v = 0,05).
  - **Satz A (angeregt):** dieselben Profile mit Amplitude x 1,05.
- Entwicklung bis T = 200. Klassifikation zu T = 0, 50, 100, 200 mit dem **unveraenderten** Klassifikator.
- Berichtet werden je Ball die Rohgroessen (Q, E, E/Q, omega, Rundheit, Abstandsmasse) und das Urteil.

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| E0 | Satz E ruhend: alle Baelle zu allen Zeiten "rund" und "auf", auf beiden Gittern | 55 % |
| E1 | Satz E bewegt: ebenfalls "auf" (die Geschwindigkeitskorrektur traegt bei v = 0,05) | 45 % |
| E2 | Satz A: zu T = 0 "neben" oder "unentschieden", nicht "auf" | 60 % |
| E3 | Scheitert E0, liegt es an einer Schwelle oder an der omega-Messung (nicht an der Familiendatei) | 70 % |

**Bedeutung (vorab):**
- E0 trifft ein: Der Klassifikator kann "auf" sagen. Das "nie auf" der Tropfen in Runde 6 und 20 ist dann ein Befund:
  Die Tropfen lagen zu diesen Zeiten neben der Familie.
- E0 trifft nicht ein: Alle bisherigen "nie auf"-Urteile sind ohne Aussage. Vor jedem weiteren Bildungsversuch wird der
  Klassifikator repariert, und KF-5 bleibt geparkt.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a oder p4000b, je <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 60 min.
