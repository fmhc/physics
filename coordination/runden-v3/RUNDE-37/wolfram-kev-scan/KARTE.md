# WOLFRAM-KEV-SCAN: wolframphysics.org automatisiert mit Kev nach Relevanz fuer unser Weltmodell vorsortieren (Werkzeugkarte, Runde 41)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 14:16:34 CEST (date).
- **Auftrag von Finn (04.10., nach 14:12, woertlich):** "noch ein subagent: können wir mit KEV/JEV Technologie die
  wolfram seiten automatisiert abscannen nach relevanten sachen die uns weiter helfen können?"
- **Was KEV/JEV hier ist (Leitung, an den Dateien auf der .69 gelesen):**
  - Kev (Jared Palmer, Apache-2.0) ist eine Familie kleiner Entscheidungsmodelle (Qwen3.5-Basis, 0,8B/4B/9B), "Jev-like":
    Zu einem Eingabetext beantwortet es Ja/Nein- ("noul"), Auswahl- ("choice") und Bewertungsfragen ("score") mit
    kalibrierten Wahrscheinlichkeiten, ohne Text zu erzeugen. Jev ist das kommerzielle Vorbild (System One von TypeSafe,
    ueber das Vercel AI Gateway, kostenpflichtig); kev/jev.py ist nur der Vergleichsharness dafuer. Jev nutzen wir nicht.
  - Auf der .69: ~/brain-kev mit kev-0.8b und Qwen3.5-0.8B-Base im HF-Cache, ein feinjustiertes brain-kev-0.8b (Adapter,
    auf Retrieval-Relevanz trainiert; eval_report.md: brain_relevant Acc 0,892, ECE 0,064), eigene Umgebung
    ~/brain-kev/kev/.venv. Kein Kev-Dienst laeuft (systemctl --user: keine Einheit aktiv).
  - Vorbehalt: Kev ist auf allgemeine bzw. Retrieval-Relevanz trainiert, nicht auf Physik. Seine Werte sind fuer unsere
    Fragen unkalibriert und dienen nur zur Vorsortierung; lesen und urteilen muss ein Mensch bzw. ein Agent.
- **Zusammenhang:** WOLFRAM-SCAN-L (feldforscher) liest die Seite gerade "komplett" mit bis zu 60 Abrufen und schreibt eine
  Seitenkarte. Diese Karte ergaenzt das um eine vollstaendige, automatische Vorsortierung aller Seiten nach unseren fuenf
  Schichten, damit kein relevanter Abschnitt uebersehen wird.

## Auftrag (Code-Agent)

1. **Erlaubnis und Umfang pruefen:** robots.txt von wolframphysics.org lesen und einhalten; nur oeffentliche HTML-Seiten
   unter wolframphysics.org (keine Anmeldung, keine Formulare, keine Downloads von Programmen); hoechstens 600 Seiten,
   hoeflich (nacheinander, mindestens 1 s Abstand, erkennbarer User-Agent). Abruf lokal mit curl (reines Laden), Speichern
   im Kartenordner unter seiten/ (Rohdaten) mit Liste URL, Abrufzeit, Groesse, sha256.
2. **Aufbereiten und bewerten auf der .69 (nicht lokal):** HTML zu Text, in Abschnitte von etwa 300 bis 600 Woertern
   teilen, je Abschnitt Kev-Fragen stellen (Fragenkatalog im Plan festlegen, vor dem ersten Lauf einfrieren). Mindestens:
   - score 0 bis 10 je Schicht: S0 Buehne mit eigener Dynamik (Netz plus Regel), S1 Ausbreitung (Dimension, Lorentz,
     Lichtgeschwindigkeit), S2 Inhalt (Teilchen als stabile Strukturen, Spin 1/2, Fermionen, Licht bzw. Eichfelder), S3
     Wechselwirkung (Ladung, Kopplung, Bindung), S4 Schwerkraft (Kruemmung, Einstein-Gleichungen, Newton-Grenzfall)
   - noul: "Enthaelt der Abschnitt eine konkrete, nachrechenbare Aussage (Regel, Zahl, Ergebnis)?"
   - choice: Art der Aussage (Herleitung, Rechnung bzw. Bild, Behauptung, Ausblick, Sonstiges)
   - noul: "Bezieht sich der Abschnitt auf Kausalgraphen bzw. Kausalmengen?" (Bezug zu unserer Ue3)
   Welches Modell (kev-0.8b oder brain-kev-0.8b) und warum, im Plan begruenden; Rauchlauf zuerst.
3. **Gegenprobe (L2), blind:** Bevor du Kev-Werte ansiehst, 25 zufaellig gezogene Abschnitte selbst lesen und je Schicht
   von Hand einstufen (relevant ja/nein). Danach vergleichen: Trefferquote unter den Top 10 je Schicht, Rangkorrelation.
   Ist Kev nicht besser als eine einfache Stichwortsuche (Vergleichslauf mit grep-Stichworten je Schicht), das klar sagen.
4. **Ausgabe:** je Schicht die 15 bestbewerteten Abschnitte (URL, Ueberschrift, kurzer Auszug, Kev-Werte), eine
   Leseliste der 30 wichtigsten Seiten fuer die Leitung bzw. den feldforscher, Abdeckung (Seiten, Abschnitte, Laufzeit),
   Ergebnis der Gegenprobe.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| WK0 | Kev laeuft auf der .69 in Laeufen von hoechstens 10 min und bewertet alle gecrawlten Abschnitte | 65 % |
| WK1 | [H] In der Gegenprobe liegen je Schicht mindestens 6 der Kev-Top-10 in den von Hand als relevant markierten Abschnitten (soweit die Stichprobe welche enthaelt) | 45 % |
| WK2 | [H] Kev ist besser als die Stichwortsuche (mehr relevante Abschnitte in den Top 10, ueber alle Schichten gemittelt) | 40 % |

## Rahmen

- Code-Agent. Rechnen nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (GPU) oder, falls Kev dort nicht laeuft
  (Pascal-GPUs, Kev-Qwen3.5 braucht neuere Kerne), die CPU-Spuren cpu3 bis cpu5; je <= 10 min. Wird die Kev-Umgebung
  ~/brain-kev/kev/.venv gebraucht, darf das Skript des Starters sie innerhalb seiner Einheit als Unterprozess aufrufen;
  keine neuen Dienste, Timer, Hooks oder Wrapper ausserhalb eines Laufs; den Kev-Server nicht als Dienst starten.
- Lokal kein python, awk oder perl; curl, sed, grep, jq, sha256sum, ssh, scp erlaubt.
- Plan vor dem ersten echten Lauf einfrieren. Zeitbox 120 min.
