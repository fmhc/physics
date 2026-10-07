# TROPFEN-LEITER: Ergebnis der Rechnung (Leitung, Runde 23, explorativ)

- Gerechnet von der Leitung auf der .69 (kleintest.sh, cpu bis cpu6):
  - sieben Laeufe 21:16:09 bis 21:20:06 UTC (23:16 bis 23:20 CEST), alle rc = 0, je 68 bis 168 s
  - Code wand_transmission_v3.py (eingefroren 23:16:05, zusammen mit KARTE.md)
- Drei Rauchlaeufe vorher, alle ausserhalb der echten Abtastbereiche (Laufplan in KARTE.md).
- Auswertung mit jq auf lauf-69/*.json. Geschrieben ab 23:21:06 CEST (date).
- Der Literaturteil (E1 bis E5) folgt getrennt in LITERATUR.md.

## Ergebnis zuerst

1. **Die ebene Q-Ball-Wand (M1, omega^2 = 1/2) hat genau eine stille Frequenz**, rho_z = 1,5241498.
   - Im ganzen Fenster (0,30 bis 1,70) gibt es nur diese eine Transmissionsnullstelle.
   - Zwei unabhaengige Verfahren stimmen auf 9e-9 ueberein: Schiessen 1,52414976 und Randwertproblem nach Richardson
     1,52414977.
   - Dort ist T = 5,4e-11; 1e-4 daneben ist T = 9e-4, 1e-3 daneben 0,08. Es ist eine scharfe, quadratische Nullstelle.
2. **Vorhergesagt waren 1,5275 +- 0,002, aus einer linearen Hochrechnung der Sprossen.** Die Nullstelle liegt 0,0034
   tiefer; TR0 ist damit **streng nicht eingetroffen**. Die uebrigen Teile von TR0 sind eingetroffen (genau eine
   Nullstelle, T < 1e-6).
3. **Die Quantentropfen-Oberflaechen haben keine stille Frequenz.**
   - Weder der 1D-Tropfen (omega 0,225 bis 2,0) noch die ebene Wand des 3D-LHY-Tropfens (0,505 bis 4,0) hat eine
     Nullstelle. TR1 und TR2 sind nicht eingetroffen.
   - Die Oberflaeche ist fuer Phononen oberhalb der Schwelle fast durchsichtig: T steigt von 0,76 (1D) bzw. 0,42 (3D)
     an der Schwelle schnell gegen 1.
   - Anregungen oberhalb der Schwelle verdampfen dort also ungehindert.
4. **Nachtraeglich [H], nicht vorhergesagt:**
   - Der Sprossenabstand aus der ebenen Nullstelle ist b_inf = sqrt2 pi/k_in(rho_z) = 2,3100, ohne Eichung.
   - Die gemessenen 3D-Schritte (n = 12 bis 15) steigen auf diesen Wert zu: 2,3043 / 2,3053 / 2,3068. Das geeichte
     Modell im Papier gibt 2,298, die nackte Wandnaeherung 2,334.
   - Die Sprossenfrequenzen naehern sich rho_z gekruemmt:
     - (rho_n - rho_z)/eps steigt in 3D von 1,099 auf 1,134 (n = 7 bis 10) und in 2D von 1,104 auf 1,119 (n = 7, 8).
     - Das erklaert, warum die lineare Hochrechnung zu hoch lag.
5. **Warum der Tropfen nicht still wird [H, nachtraeglich]:**
   - Die stille Frequenz braucht offenbar einen an der Wand gebundenen Zustand im geschlossenen Kanal (Fano-Bild, wie
     die "bare closed-channel wall approximation" des Papiers).
   - M1 hat diese Mulde: W = U' + U'' S faellt an der Wand auf 0,111 (bei S = 4/9), aussen ist W = 1, innen 1,5. Fuer
     rho in (1,040; 1,707) gibt es also einen erlaubten Bereich an der Wand. Die Nullstelle liegt darin, darunter liegt
     keine.
   - In beiden Tropfenmodellen sinkt das Wandpotential des geschlossenen Kanals nicht tief genug: Noetig waere
     h_min < -|mu0|, es ist h_min = -0,059 gegen -0,222 (1D) bzw. -0,319 gegen -0,5 (3D).

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| TR0 | M1: genau eine Nullstelle in [1,45; 1,65], bei 1,5275 +- 0,002, dort abs(t)^2 < 1e-6 | **nicht eingetroffen (Lage)**: eine Nullstelle (sogar die einzige in 0,30 bis 1,70), aber bei 1,52415 (-0,0034); T(f_z) = 5,4e-11 |
| TR1 | Tropfen 1D: mindestens eine Nullstelle in (2/9; 8/9) | **nicht eingetroffen**: keine im ganzen Bereich 0,225 bis 2,0 |
| TR2 | Tropfen 3D: mindestens eine Nullstelle in (1/2; 2) | **nicht eingetroffen**: keine im ganzen Bereich 0,505 bis 4,0 |
| TR3 | Stufe 2 (nur wenn TR1) | entfaellt |

**Bedeutung (vorab festgelegt):**
- Fuer TR0 ist formal die Zeile "TR0 trifft nicht ein" ausgeloest. Beschrieben wird, ohne Umdeutung:
  - Eine ebene Nullstelle gibt es, und zwar genau eine.
  - Nur ihre Lage verfehlt die Toleranz, und zwar so, wie die gekruemmte Annaeherung der Sprossen es nahelegt
    (Punkt 4, nachtraeglich).
- TR1 und TR2: "Im Fenster haben die Tropfenmodelle keine stille Oberflaeche." Gilt.

## Kontrollen

- K0: Hintergrundrest <= 1,2e-15 (analytische Ableitungen), Innen-Dispersion gegen die Formeln <= 1,8e-15, Flussbilanz
  R + T - 1 <= 2,9e-10 in allen Laeufen.
- Gegenproben an der M1-Nullstelle:
  - rtol 1e-9: Abweichung 4e-14
  - Gebiet +10: 1e-15
  - Randwertproblem h = 0,002 / 0,004: 1,524149747 / 1,524149674, Richardson 1,524149771
- Keine Beinahe-Nullstellen: Ausser bei der M1-Nullstelle ist das kleinste |c_in| je Lauf mindestens 0,42 des Medians,
  bei den Tropfen jeweils am Schwellenrand.

## Latten (v3)

- L1: ja. TR0 hat formal verfehlt, TR1 und TR2 sind gescheitert.
- L2: ja. Die Lage kam aus einer Hochrechnung, die ebene Rechnung ist unabhaengig, und es gibt zwei Verfahren.
- L3: ja (zwei Verfahren, zwei Toleranzen, zwei Gebiete, zwei Schrittweiten).
- L4: offen bis LITERATUR.md. Das Papier nennt das ebene Wandproblem als ungeloest.
- L5: teilweise. Die ebene Nullstelle als Grenzwert der Leiter mit parameterfreiem Abstand ist im Projekt neu; ob in der
  Literatur, klaert LITERATUR.md.

## Selbstanzeigen

- Die Toleranz +-0,002 in TR0 war zu eng gewaehlt, obwohl ich in der Karte selbst "leicht gekruemmt" (3D-Steigung 1,00
  bis 1,04) notiert hatte.
- Die Fassungen 1 und 2 des Codes hatten Fehler. Beide fielen im Rauchlauf auf und wurden vor dem Einfrieren behoben
  (Laufplan in KARTE.md).
- Punkt 4 und 5 sind nachtraegliche Lesarten, keine Vorhersagen.

## Einfach gesagt

Die Wand eines Q-Balls ist wie ein Spiegel mit einer besonderen Farbe. Genau bei einer Frequenz laesst sie gar nichts
durch, und daraus entstehen die stillen Sprossen. Die Frequenz haben wir jetzt direkt ausgerechnet, ohne einen
einzelnen Ball zu simulieren. Sie liegt etwas tiefer als geschaetzt, sagt aber den Abstand der Sprossen sehr gut voraus.
Bei echten Quantentropfen ist die Oberflaeche dagegen fast durchsichtig: Es fehlt eine "Mulde" an der Wand, in der sich
eine Welle kurz fangen kann. Dort gibt es diese Stille deshalb nicht.

## Nachtrag: Literatur (LITERATUR.md, Rechercheagent; eingetragen 2026-10-02 23:45:30 CEST)

- E1 bis E4 eingetroffen, E5 nur dem Wortlaut nach (anderer Mechanismus). Fundstellen in LITERATUR.md, Marken [S]/[L?]
  dort.
- **Keine Arbeit zu einer stillen Tropfenoberflaeche** (E3), weder gerechnet noch gemessen, gesucht auch im
  24-Monats-Fenster.
  - Naechster Verwandter: "resonance states" einer He-4-Schicht ohne Atomsignal aussen (Dalfovo u. a. 1995,
    cond-mat/9505121). Gefunden wurden sie durch Abstimmen der Schichtdicke.
  - Mechanismus dort: Zwei innere laufende Kanaele (R+, R-) loeschen sich aus. Eine dichte Einzelwand ist es nicht.
- **He-4-Nullstelle am Maxon** (Dalfovo u. a. 1997): ein Schwelleneffekt, keine Fano-Nullstelle.
- **Die Leiterregel an der Schwelle ist Literatur:**
  - Tylutki u. a. 2020 (arXiv:2003.05803) rechnen genau unser 1D-Modell. Moden verlassen den gebundenen Bereich bei
    konstantem Abstand Delta N = 2,664.
  - Die Leitung hat nachgerechnet: k^2 = (2/9)(sqrt5 - 1) = 0,2747 bei omega = |mu0|, also n0 pi/k = 2,664.
  - Das ist Fabry-Perot an der Schwelle; eine stille Frequenz oberhalb der Schwelle zeigen sie nicht. Passt zu TR1.
- **Datenbruecke schwach:**
  - Selbstverdampfung ist nie beobachtet worden, Dreikoerperverluste verhindern es (Hirthe/Tarruell 2026,
    arXiv:2603.17745, nach dem Agenten [S]).
  - Das skalare Tropfenmodell laesst den Spinkanal weg. Im vollen Gemisch gibt es innen zwei laufende und aussen zwei
    offene Kanaele, die Kanalzaehlung der Karte gilt dort nicht.
- **Latten neu:**
  - L4 fuer die Tropfen: ja. Das Negativergebnis ist mit der Literatur vereinbar.
  - L4 fuer die M1-Wand: weiter offen. Der Agent hat nur die Tropfen- und He-4-Seite gesucht; das Papier nennt das ebene
    Wandproblem ungeloest.
- Selbstanzeigen des Agenten:
  - ein lokaler `python3`-Start mit leerer Eingabe, ohne Code
  - drei Kopfrechnungen, als [ES] markiert; die zum Abstand 2,664 hat die Leitung bestaetigt
  - eine Ueberschrift, die bei einem Edit verloren ging und im Anhang nachgetragen ist
  - "Fabry-Perot-BIC" bei Hsu 2016 nur aus der Erinnerung

## Nachtrag: Selbstanzeige zur Ableitbarkeitspruefung (Leitung, 2026-10-03 01:00:54 CEST)

- In der Karte stand: "Tropfen-Oberflaechen wurden im Projekt nie gerechnet". Das ist falsch.
- RUNDE-10/nls-leiter/ERGEBNIS.md (01.10.) hat beim Petrov-Troepfchen den nackten Wandzustand gerechnet und gefunden:
  - Im Flachkuppenbereich liegt er bei E_0 = +0,08 bis +0,11, noetig waere weniger als mu = -0,40 bis -0,46.
  - Es gibt also keinen Wandtopf und keine Leiter; die MESS-1-Begruendung ist dort numerisch belegt.
  - Fazit dort: "Fuer Optik und kalte Atome (Troepfchen) folgt: keine stille Leiter, nichts zum Messen." Die Leiter braucht
    den Antiteilchen-Zweig bei rho ~ 2 m, den die NLS-Naeherung abschneidet.
- Folgen:
  - Der Ausgang von TR1 und TR2 war im Kern ableitbar. Neu ist nur die direkte Rechnung der Transmission an der ebenen
    Tropfenwand (keine Nullstelle, T -> 1).
  - Meine nachtraegliche "Mulden"-Lesart (Punkt 5 oben) ist der Wandtopf aus RUNDE-10, also kein neuer Befund.
  - Die Ideensammlung (IDEEN-LOGIK-TEILCHEN.md, Punkt 2) haette TROPFEN-LEITER nicht als beste Datenbruecke fuehren
    duerfen.
  - Die M1-Wandrechnung (TR0) ist davon nicht beruehrt.
- Ursache: Ich habe die Rohdatenprobe nur fuer die Leiterzahlen gemacht und nicht nach "Troepfchen/Petrov" im Projekt
  gesucht. Lehre: Vor einer Karte zu einem neuen Modell das Projekt per grep nach dem Modellnamen absuchen.
