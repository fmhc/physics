# TT-ISO-1: Lassen sich die zwei Schwerewellen-Zweige (TT) auf Finns gefuelltem Netz durch Gewichte langwellig isotrop machen? (Runde 43, Fast Lane)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 21:52:24 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - GAMMA-NETZ-L (RUNDE-37/gamma-netz-l/DOSSIER.md, V4 und O1):
    - Bindend fuer "Netz = Raum" ist die Spin-2-Ausbreitung, nicht gamma.
    - Messanker: c_T/c - 1 in [-3e-15; 7e-16].
  - EINE-WELT-LOCH-1 (ERGEBNIS Abschnitt 1, Punkt 5, und Abschnitt 5):
    - Mit Fuellung gibt es 2 masselose TT-Moden.
      - V: omega^2/k^2 = 0,1189 bis 0,1264, Spanne 6,2 %.
      - S: 0,211 bis 0,217, Spanne 2,6 %.
    - Ohne Fuellung ist das Tempo isotrop (0,25), aber nur mit der Reduktion R1; R2 gibt 0,2222 in [111].
    - Nachtrag: fuenf feste Bewegungsvarianten, Spanne 3,2 bis 10,6 % (Lesung GAMMA-NETZ-L).
  - ZWEI-KOPIEN-1 (laeuft) prueft den anderen Weg: ungefuelltes, isotropes Netz mit oertlicher Eckkopplung.
    - Isotropie wird dort beschreibend mitgemessen (Zusatz Leitung).
- Kennzeichen: [M] Mathematik, [E] Rechnung, [P] Projektdatei, [S] Quelle, [L] Gedaechtnis, [H] Hypothese.

## Ableitbarkeitsprobe (Leitung, Schreibtisch, vor der Karte)

- **Projektsuche** (isotrop, TT, Zener, kinetik.json, Friedberg, Zufallsnetz):
  - NETZ-C-1 (R35): Skalare und elastische Netze haben mehrere Geschwindigkeiten; abgestimmt ist Isotropie moeglich.
  - LICHT-GLEICH-L: Gleiches Tempo gibt es nur durch Abstimmen oder Symmetrie [P].
  - Zufallsnetze sind im Mittel isotrop (RUNDE-36, RUNDE-39; Christ/Friedberg/Lee 1982 [L]).
  - Fuer die TT-Zweige gibt es keine Gewichtsabtastung, nur die fuenf festen Varianten des Nachtrags.
  - Der Agent prueft die Rohdaten (eine-welt-loch-1/nachtrag-69/kinetik.json, per jq 'keys') vor dem Plan und nennt die Felder.
- **Symmetrie [M, Leitung, ungeprueft]:**
  - Bei kubischer Punktgruppe zerfallen die spurfreien Polarisationen in Eg + T2g.
  - Jede kubisch symmetrische Bewegungsenergie wirkt darauf nur ueber zwei Gewichte m_E und m_T. Fuer die Tempi zaehlt nur m_E/m_T.
  - In [111] sind die zwei TT-Zweige durch C3v entartet; so war es auch im Hauptlauf. In [100] und [110] ist das nicht erzwungen.
  - Die Gradientenenergie hat kubisch 9, isotrop 4 Invarianten (Sym2 k mal Sym2 h).
  - Isotropie verlangt also mehrere Bedingungen, und ein einzelnes Verhaeltnis erfuellt generisch hoechstens eine.
  - **Folgerung:**
    - Die Richtung von TB1 ("generisch nicht isotrop") ist ableitbar, die kleinste erreichbare Spanne nicht.
    - Voraussetzung ist die volle kubische Punktgruppe des gefuellten Netzes. Der Agent prueft das fuer V und S vor dem Plan.
    - Hat das gefuellte Netz eine kleinere Gruppe, gilt die Zaehlung nicht; das vermerkt der Agent im Plan.
- **Masse gegen Steifigkeit:**
  - Gewichte der Bewegungsenergie wirken nur auf die Masse.
  - Das Gewicht l_e der skalaren Regel wirkt auf die Zwangsflaeche, also auf die Steifigkeit. Es wurde nie variiert (EINE-WELT-LOCH-1, Selbstanzeige 3).
  - Ein anderes l_e-Gewicht verlaesst die Regge-Lesart von GAMMA-NETZ-L (Hamilton-Bedingung). TB2 ist daher eine reine Abstimmungsfrage.

## Auftrag (Code-Agent)

1. **Code kopieren:** aus eine-welt-loch-1/code nach tt-iso-1/code, dort nichts aendern.
   - Gerechnet werden die Hauptlauf-Paarung A1-R1 und die an allen 511 k stabilen Paarungen A2-R1 und A3-R2.
2. **Kontrolle:** Hauptlaufwerte und je eine Nachtragsvariante reproduzieren (TB0).
3. **Bewegungsgewichte:** J_t je Tetraeder-Art (Arten nach dem Code, z. B. Finn-Tetraeder und Fuelltetraeder) als freie positive Zahlen.
   - Abtasten im Plan-Bereich, mindestens 1e-2 bis 1e2 je Gewicht, logarithmisches Gitter.
   - Danach eine lokale Verfeinerung um das beste Gitterfeld.
   - Gesucht ist die kleinste TT-Spanne.
4. **Zusatz:** das Gewicht l_e der skalaren Regel je Kantenart als weitere freie Zahl, gleicher Ablauf (TB2).
5. **Messgroesse:** omega^2/k^2 der zwei masselosen TT-Zweige.
   - Bei |k| = 1e-3 und 2e-3.
   - In mindestens 13 Richtungen: [100], [110], [111] und 10 weitere, vor dem Einfrieren festgelegt.
   - Spanne = max/min - 1 ueber Richtungen und Zweige.
   - Fuer die beste Wahl zusaetzlich: keine negative Mode an den 511 k des Gitters L = 8 (Stabilitaet, Konkurrenzzustand).
6. **Fuellungen:** V ist das Hauptergebnis, S wird beschreibend mitgerechnet.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TB0 | Kontrolle: A1-R1 (V) gibt in [100] wieder 0,1189 / 0,1264 und die Spanne 6,2 % auf 1e-3 relativ; ohne Fuellung (R1) isotrop 0,25 | 90 % |
| TB1 | [H] Ueber alle Bewegungsgewichte im Plan-Bereich bleibt die kleinste TT-Spanne in V bei jeder der drei Paarungen ueber 1 % | 70 % |
| TB2 | [H] Mit zusaetzlich freiem Gewicht der skalaren Regel sinkt die kleinste Spanne in V unter 0,1 %, ohne negative Mode an den 511 k | 20 % |

**Bedeutung (vorab):**
- **TB1 trifft ein:** Bewegungsgewichte allein machen das gefuellte Netz nicht isotrop.
  - Schwerewellen liefen dort um mehr als 1 % richtungsabhaengig; erlaubt ist etwa 1e-15.
  - Auswege [H]: Steifigkeiten abstimmen (TB2), die ungefuellte Variante mit Eckkopplung (ZWEI-KOPIEN-1) oder ein Zufallsnetz.
- **TB1 verfehlt:** Ein Gewichtsverhaeltnis macht die TT-Zweige isotrop.
  - Das ist eine Abstimmung. Fuer 1e-15 muesste sie extrem genau sitzen oder einen Grund haben [H].
- **TB2 trifft ein:** Zwei Abstimmungen genuegen, zumindest auf 0,1 %. Ob 1e-15 erreichbar ist, waere die naechste Frage.
- **TB2 verfehlt:** Auch mit Regelgewicht bleibt das gefuellte regelmaessige Netz anisotrop.
  - Es braucht weitere Bauteile oder Unordnung [H].

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu5 (frei seit GUERTEL-FELD-STAB-2).
- Je Lauf hoechstens 10 min, 1 Thread. Zeitbox 75 min.
