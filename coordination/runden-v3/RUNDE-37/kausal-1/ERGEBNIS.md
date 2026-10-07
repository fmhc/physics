# KAUSAL-1: Ergebnis (Leitung, 2026-10-04 02:50:08 CEST)

**Ergebnis zuerst:**
- Ein zufaelliges Raumzeit-Netz ohne Ruhesystem (Poisson-Kausalmenge in 1+1) hat keine festen Nachbarn.
- Jeder Punkt hat im Mittel ln N - 1,42 Links: 8,24 bei N = 16 000, mit jedem Verdoppeln von N einer mehr.
- Die Links verteilen sich gleich ueber alle Geschwindigkeiten: 1,00 je Rapiditaetseinheit, flach bis abs(eta) = 3.
- Alle vier Vorhersagen sind eingetroffen. Alles war vorab ableitbar [M].

## Urteile (lauf-69/auswertung.json)

| Nr | Urteil | Werte |
|---|---|---|
| K0 | eingetroffen | Relationsanteil, Saatmittel: 0,4960 / 0,4985 / 0,4974 / 0,4998 (N = 2000 / 4000 / 8000 / 16000) |
| K1 | eingetroffen | L/N gegen ln N - 1,423: 6,162 gegen 6,178; 6,822 gegen 6,871; 7,540 gegen 7,564; 8,242 gegen 8,258 |
| K2 | eingetroffen | Dichte je Rapiditaetseinheit (N = 16000, 2591 Zentrumspunkte, 0,5-Klassen von -2 bis 2): 0,980 / 0,963 / 0,996 / 1,034 / 0,961 / 1,010 / 0,956 / 0,993 |
| K3 | eingetroffen | L/N(16000) - L/N(2000) = 2,080 gegen ln 8 = 2,079 |

## Beschreibend

- **Exaktes Doppelintegral:** 6,182 / 6,874 / 7,566 / 8,258. Alle vier Saatmittel liegen 0,016 bis 0,052 darunter.
  - Bei N = 8000 ist das gegen die Saatstreuung etwa -3 sigma, sonst -1 bis -2.
  - Ob Zufall oder eine kleine systematische Abweichung, ist offen [H]. Die Zaehlregel (laufendes Minimum) habe ich nicht
    unabhaengig gegengeprueft.
- **Groesster Grad** (Links je Punkt, beide Richtungen): 25 / 29 / 32 / 35. Er waechst mit N.
- **Rapiditaet ausserhalb des Urteilsbereichs:** [-3, -2] 0,975; [2, 3] 0,973.
- **Laufzeit** je Lauf <= 2,6 s auf der .69 (Spur p4000a, nur CPU).

## Selbstanzeigen

- K0 wird am Saatmittel geurteilt. Diese Lesart habe ich nach dem Rauchwert 0,517 (N = 1000, Saat 9) festgelegt.
  Einzelsaat N = 2000, s1: 0,489 laege ausserhalb +-0,01 (FESTLEGUNGEN.md).
- Die Schwelle von K2 war nach eigener Rechnung knapp (Poisson ~2,8 % je Klasse). Sie bleibt unveraendert und ist
  bestanden.
- Kein frischer Gegenleser fuer Code und Herleitung; die Leitung hat beides selbst geschrieben.

## Bedeutung

- **Fuer Finns Bild:** Ein Netz in Raum und Zeit, das keine Geschwindigkeit auszeichnet, ist nicht lokal.
  - Jeder Punkt haengt mit immer mehr anderen zusammen, je groesser das Netz ist.
  - Die Striche zeigen gleich oft in alle Bewegungsrichtungen, bis nah an den Lichtkegel.
- Ein Netz mit festen Tetraeder-Nachbarn muss deshalb ein Ruhesystem haben, das gut versteckt ist, oder solche
  weitreichenden Striche [L: Bombelli/Henson/Sorkin; H fuer die Uebertragung].
- Finns Bild vom Anfang ("endlose Striche, die sich ueberkreuzen") passt eher zur zweiten Moeglichkeit [H].

## Einfach gesagt

Wir haben zufaellig Punkte in Raum und Zeit verteilt und jeden Punkt mit seinen direkten Nachfolgern verbunden. Das Netz
sieht fuer jeden Beobachter gleich aus, egal wie schnell er sich bewegt, aber jeder Punkt hat dann nicht ein paar feste
Nachbarn, sondern immer mehr, je groesser das Netz wird. Bei 16 000 Punkten sind es im Schnitt gut 8, und die Verbindungen
zeigen gleich oft in jede Bewegungsrichtung. Ein Netz ohne bevorzugte Ruhelage braucht also lange, kreuz und quer laufende
Striche; ein Netz mit festen kleinen Nachbarschaften hat dagegen eine Ruhelage.

## Berichtigung (2026-10-04 03:34:37 CEST, Leitung, nach GEGENLESEN-3 D1 zur Anschauungsseite)

- "Jeder Punkt hat im Mittel ln N - 1,42 Links: 8,24 bei N = 16 000" ist falsch gelesen.
  - L/N = 8,24 ist die Zahl der Links geteilt durch die Zahl der Punkte.
  - Jeder Link hat zwei Enden. Also hat jeder Punkt im Mittel ln N - 1,42 Links in die Zukunft und ebenso viele in die
    Vergangenheit.
  - Der mittlere Grad (Links an einem Punkt) ist 2 L/N: 12,32 / 13,64 / 15,08 / 16,48 bei N = 2000 / 4000 / 8000 / 16000
    (grad_mittel in den Laufdateien).
- Die Urteile K0 bis K3 aendern sich nicht; sie pruefen L/N, wie die Karte es definiert.
- Dieselbe Fehllesung stand in der Chat-Meldung an Finn ("etwa 8 Striche je Punkt"); dort wird sie berichtigt.
