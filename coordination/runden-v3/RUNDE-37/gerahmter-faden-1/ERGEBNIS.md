# GERAHMTER-FADEN-1: Ergebnis (Runde 50)

- Code-Agent fuer die Leitung claude-primary. Ohne Einfrieren und ohne frischen Leser (Finn: "einfach machen und
  ausprobieren"). Karte (KARTE.md) und Erwartungen unveraendert.
- **Zeiten (alle per date):**
  - Start 2026-10-05 19:04:16 CEST. Code geschrieben nach 19:21:22 (letzter date-Stempel davor). Text dieses
    Ergebnisses ab 19:36:06 CEST.
  - Laeufe auf der .69 ueber kleintest.sh (Zeiten aus den Starter-Zeilen, UTC + 2 h), alle rc = 0:
    - Rauch 19:26:04 bis 19:26:29 (cpu8)
    - Basis (A, B, C; M1, M2, M4; n = 2, 3) 19:30:05 bis 19:30:58 (cpu8)
    - M3 n = 2 19:30:05 bis 19:32:50 (cpu9), M3 n = 3 19:30:05 bis 19:32:59 (cpu10)
    - Gegenprobe G2 19:33:29 bis 19:33:30 (cpu8)
  - Platte vor jedem Lauf: 17 GB frei.
- **Kennzeichen:** [P] Projektbefund; [M] Mathematik am Schreibtisch; [M nachher] erst nach dem Rauchlauf hergeleitet;
  [R] im Rauchlauf gesehen; [H] Hypothese.
- **Art:** synthetische, exakte Rechnung (GF(2)/Z4 fuer alle Vorzeichen). Die Rahmenfelder sind Gleitkomma-Quaternionen;
  ihre Geometrie geht nur ueber Vorzeichen von Determinanten ein, mit Randabstandspruefung. Keine Messdaten.

## Ergebnis zuerst

1. **C (Kopplungsgesetz plus Hebungsbuchhaltung) gibt das Spin-Vorzeichen, wie vorab skizziert.** Bei einer oertlichen
   2-pi-Drehung von q_i kippt jede der vier Bindungen an i ihren kurzen Lift genau einmal. Die Flussanpassungen
   summieren sich zum Gauss-Operator A_i. Ergebnis: -1 mit Ende, +1 ohne Ende, fuer alle drei Achsen. Das gilt in
   allen 42 Faellen je Netz (7 Rahmen, 2 Knoten, 3 Achsen). Die 4-pi-Drehung gibt ueberall +1.
2. **Das Austauschvorzeichen ist in A, B und C dasselbe:** -1 in allen Tripeln (1536 bzw. 5184), in jedem Rahmen. Es
   kommt aus dem Twist; der Lift in C ist eine c-Zahl und aendert daran nichts. Spin (aus dem Lift) und Statistik (aus
   dem Twist) kommen also aus zwei getrennten Regeln. Damit ist die vorab festgelegte Bedeutung "GFR2 und GFR3 treffen
   ein" ausgeloest.
3. **B (Projektionsrichtung n_i je Knoten) ist immer vertraeglich (M1 = 0), auch bei 60 Grad.** GFR1 ist damit nicht
   eingetroffen (es hatte bei 60 Grad Paare erwartet). Das ist strukturell: In Lesart S zerfaellt das
   Vertauschungsvorzeichen in Knotenbeitraege, die von der Projektion am Knoten nicht abhaengen [M nachher]. M1 konnte
   fuer B also gar nicht scheitern.
4. **B traegt keinen Spin.** Um die Achse n_i gibt B +1, und zwar per Konstruktion. Um die beiden anderen Achsen gibt es
   keinen lokalen unitaeren Transport: Jeder Pfad hat 2 bis 16 Seitenwechsel im Vertauschungsgraph der Huepfer. Meist
   aendert sich unterwegs auch der Fermionfluss am Knoten. Wo ein Vorzeichen definiert ist (Stufe F, 14 bzw. 12 von 112
   Pfaden), ist es +1. Nirgends tritt -1 auf.
5. **Neu und nicht auf der Karte:** Bei B erzeugt die Rahmentextur ein Flussmuster fuer die Fermionen. Bis zu 198 von
   432 Sechsecken haben Fluss -1, waehrend jede feste Projektion ueberall +1 gibt (TWIST-SPIN-1). Die Textur koppelt also
   an die Fermionen, aber als Eichfluss, nicht als Spin [H fuer die Deutung].

## Tabelle je Variante, Rahmenklasse und Netz

- **M1** = antivertauschende Paare (Schleife, Schleife) plus (Huepfer, Schleife). Paare je Netz: 8128 und 16 384
  (n = 2); 93 096 und 186 624 (n = 3).
- **M2** = Tripel mit Vorzeichen -1 von allen Tripeln.
- **M3** = Vorzeichen des Zustands mit Ende relativ zum Zustand ohne Ende, nach einer 2-pi-Drehung von q_i. Achsen:
  a1 = n_i; a2 nahezu senkrecht zu n_i; a3 schraeg. Gerechnet an zwei Knoten, (0,0,0) und (1,1,1); bei R1 nur Saat 0.
  "undef." heisst: kein Transport auf Stufe K, und auf Stufe F aendert sich der Fluss.
- **M4** = PSG-Invariante (C2)^2 unter T, nur R0 (wie auf der Karte).
- Rahmen R1: je theta_max 6 Saaten. Fuer B sind beide Push-off-Richtungen gerechnet: w_haupt = (-5, 4, 0) und
  w_alt = (-1, 0, 0).

| Variante | Rahmen | n | M1 | M2 | M3 a1 / a2 / a3 | M4 |
|---|---|---|---|---|---|---|
| A (P1, P2, P3) | alle (Rahmen ungenutzt) | 2 | 0 | 1536 / 1536 | +1 / +1 / +1 (0 Ereignisse) | +1 (P1, P2, P3) |
| A (P1, P2, P3) | alle | 3 | 0 | 5184 / 5184 | +1 / +1 / +1 | +1 (P1, P2, P3) |
| B | R0 | 2, 3 | 0 | alle -1 | +1 / undef. / undef. (w_alt, Knoten (0,0,0), a2: +1 auf Stufe F) | +1 (beide w) |
| B | R1, 15 Grad | 2, 3 | 0 (6 Saaten, beide w) | alle -1 | +1 / undef. / undef. (w_alt, (0,0,0), a2: +1 Stufe F) | - |
| B | R1, 30 Grad | 2, 3 | 0 | alle -1 | wie 15 Grad | - |
| B | R1, 45 Grad | 2, 3 | 0 | alle -1 | wie 15 Grad | - |
| B | R1, 60 Grad | 2 | 0 | alle -1 | wie 15 Grad | - |
| B | R1, 60 Grad | 3 | 0 | alle -1 | +1 / undef. / undef. (auch w_alt-a2 undef.: 3 Flusswechsel) | - |
| B | R2z (Kern um z) | 2, 3 | 0 | alle -1 | wie R0 (n_i = z ueberall, also B identisch mit R0) | - |
| B | R2x (Kern um x) | 2, 3 | 0 | alle -1 | +1 / undef. / undef. (w_alt-a2 an (0,0,0): +1 Stufe F) | - |
| C (Projektion P2) | R0, R1, R2z, R2x | 2 | 0 | 1536 / 1536 | -1 / -1 / -1 (ohne Ende +1; 4 pi: +1) | +1 (= A P2) |
| C (Projektion P2) | R0, R1, R2z, R2x | 3 | 0 | 5184 / 5184 | -1 / -1 / -1 (ohne Ende +1; 4 pi: +1) | +1 (= A P2) |

**Zusatzzahlen B** (Knoten mit anderer lokaler Konvention als bei n = z; Sechsecke mit Fermionfluss -1; Bereich ueber
6 Saaten):

| Rahmen | n | w_haupt: Knoten anders | w_haupt: Fluss -1 | w_alt: Knoten anders | w_alt: Fluss -1 | groesste Abweichung von n_i zu z |
|---|---|---|---|---|---|---|
| R1 15 | 2 | 1-7 von 64 | 1-20 von 128 | 0 | 0 | 13 Grad |
| R1 30 | 2 | 14-26 | 19-42 | 0 | 0 | 27 Grad |
| R1 45 | 2 | 22-39 | 29-54 | 0 | 0 | 41 Grad |
| R1 60 | 2 | 30-47 | 33-57 | 0-2 | 0-8 | 55 Grad |
| R2x | 2 | 24 | 38 | 24 | 46 | 122 Grad |
| R1 15 | 3 | 15-52 von 216 | 21-77 von 432 | 0 | 0 | 21 Grad |
| R1 30 | 3 | 74-122 | 76-130 | 0 | 0 | 43 Grad |
| R1 45 | 3 | 121-158 | 121-154 | 1-16 | 2-39 | 65 Grad |
| R1 60 | 3 | 139-174 | 140-198 | 19-62 | 39-113 | 88 Grad |
| R2x | 3 | 70 | 108 | 30 | 96 | 173 Grad |

- R0 und R2z: 0 Knoten anders, Fluss ueberall +1. In allen B-Faellen: 0 Fluss-Inkonsistenzen, 0 "kein Korand".
- **M3-Ereignisse bei B** (Achsen a2, a3; 112 Pfade je Netz, 2 pi und 4 pi): Es gibt 4 bis 26 Ereignisse je Pfad.
  - Davon 2 bis 16 Seitenwechsel: Der Vertauschungsgraph der Huepfer am Knoten aendert sich. Nach Satz K aus
    TWIST-SPIN-1 gibt es dafuer keine lokale Unitaere.
  - Die uebrigen Ereignisse sind Reihenfolgewechsel. Sie sind als CZ-Clifford-Abbildung exakt transportierbar. Dabei
    gehen aber insgesamt 792 bzw. 810 Schleifenoperatoren auf -1 mal den neuen; der Transport verlaesst also den
    Vakuumsektor.
  - Stufe K ist auf keinem der 112 Pfade definiert; Stufe F auf 14 (n = 2) bzw. 12 (n = 3), dort immer +1.
- **C im Rahmen R2:** 12 Bindungen mit Lift -1 (der Kern hat q nahe -1), aber w2 = +1 auf allen Schleifen. Das
  Kopplungsgesetz setzt also keinen Fluss: Der Lift ist dort eine reine Eichwahl. Die Bindungswinkel erreichen in R2
  bis 122 Grad (n = 2) bzw. 173 Grad (n = 3); "nearly flat" ist damit bei n = 3 knapp.
- **C im Rahmen R1:** alle Lifte +1 und w2 = +1. Das war vorab klar: Bei hoechstens 60 Grad je Bindung kommt ein
  Sechseck nicht auf 180 Grad im Quaternionabstand.

## Kontrollen

- **A gegen TWIST-PYRO-1 und TWIST-SPIN-1 (GFR0), alles bitgleich bzw. zahlgleich:**
  - Die lokale Kegelformulierung von Lesart S gibt fuer P1, P2, P3 bei n = 2, 3 genau die Z-Mengen von tp.drehung,
    fuer alle Huepfer und Schleifen.
  - Generik: 0 Entartungen, 0 unklare Kreuzungen.
  - M1 = 0; M2 = -1 in 1536 bzw. 5184 Tripeln, 0 Inkonsistenzen.
  - G1 = 1152 / 1536 / 1536 (n = 2) und 3888 / 5184 / 5184 (n = 3), wie TWIST-PYRO-1.
  - Fermionfluss +1 auf allen 128 bzw. 432 Sechsecken. K-Untergruppen C3 (P1) bzw. V4 (P2, P3); PSG-Invariante +1;
    Paarerzeuger +1. Alles wie TWIST-SPIN-1.
- **Ohne Ende:** M3 = +1 in A, in C (alle 84 Faelle je Netz) und in B, wo definiert.
- **Achse n_i:** B gibt +1 in 56 von 56 Faellen je Netz, mit 0 Ereignissen (per Konstruktion).
- **4-pi-Drehung:** C +1 (jede Bindung kippt zweimal, Anpassung leer), A +1. B: wo definiert +1, sonst wie bei 2 pi
  undefiniert.
- **Gegenprobe G1** (Huepfer gleichsinnig gerahmt): schlaegt in jedem Fall an. A siehe oben; B 1224 bis 1536 (n = 2)
  bzw. 4092 bis 5184 (n = 3). Die Huepfer-Schleifen-Pruefung kann also scheitern.
- **Gegenprobe G2** (Schleifenpaare; je Schleife eine eigene Push-off-Richtung, R0 exakt): ueberall 0.
  - Vorhersage vor dem Lauf g2 (19:33:20): gleicher Sektor 0, Gegenrichtung 0, anderer Sektor (4, 5, 0) > 0.
  - Ausgang: alle drei 0, obwohl beim anderen Sektor und bei der Gegenrichtung alle 128 bzw. 432 Z-Mengen anders sind.
    Die dritte Vorhersage ist gescheitert.
  - Grund (nachher): Das Jordan-Argument aus TWIST-PYRO-1 braucht fuer zwei Schleifen gar nicht denselben Push-off. Die
    Schleifenpaar-Pruefung kann in Lesart S mit geometrischer Rahmung nicht anschlagen. Angeschlagen hat sie in
    TWIST-PYRO-1 nur in Lesart V.
- **Gleitkomma:** B bei q = 1 in Gleitkomma ist identisch mit der exakten Fassung (4 von 4).
  - Kleinster Randabstand der Kegeltests: 8,8e-6 im Basislauf, 5,2e-6 im M3-Lauf (Schwelle 1e-9); 0 entartete Tests
    im Basis- und im M3-Lauf.
  - Der Rauchlauf mit der Achse genau x traf bei R0 exakt entartete Richtungen (112 entartete Tests, 4 scheinbare
    M1-Meldungen). Deshalb sind die Achsen im Hauptlauf generisch.
- **Schrittweite:** M3 mit 1440 Schritten je 2 pi. Mit 2880 Schritten sind Ereignisse, Flusswechsel und Urteile gleich
  (12 von 12 Vergleichen je Netz).

## Abgleich mit GFR0 bis GFR4 (beschreibend; Erwartungen der Karte unveraendert)

| Nr | Vorhersage (Karte) | Wahrsch. | Befund | vorab feststehend? |
|---|---|---|---|---|
| GFR0 | A gibt TWIST-PYRO-1/-SPIN-1 bitgleich wieder (0 Paare, -1 in allen Tripeln, (C2)^2 = +1) | 90 % | **eingetroffen**; bitgleiche Z-Mengen, alle Kennzahlen gleich | **ja, ganz** [P]; prueft nur Nachbau und Code |
| GFR1 | [H] B bei R1 bis 30 Grad vertraeglich, bei 60 Grad nicht (> 0 Paare) | 45 % | **nicht eingetroffen**: 0 Paare bei allen theta_max (auch 60 Grad), 6 Saaten, n = 2, 3, beide w; ebenso R2x und alle 336 Drehpfade aus M3 (224 davon mit Konventionswechseln). Die erste Haelfte stimmt, die zweite nicht | **faktisch ja** [M nachher]: Die zweite Haelfte konnte in Lesart S nicht eintreffen (siehe unten). Die Karte nannte GFR1 "echt offen"; das war es nicht |
| GFR2 | [H] B liefert in M3 kein achsenunabhaengiges -1 (ueberall +1 oder achsenabhaengig) | 70 % | **im Kern eingetroffen**: nirgends -1. Achse n_i +1; die anderen Achsen meist ohne definiertes Vorzeichen (kein Transport), +1 wo definiert. "Ueberall +1 oder achsenabhaengig" trifft im strengen Sinn nicht zu: Meist gibt es gar kein Vorzeichen | **ja**: Mit n_i unter den drei Achsen konnte ein achsenunabhaengiges -1 nicht auftreten (n_i-Drehung aendert per Konstruktion nichts). Die Karte nannte GFR2 "scheiterfaehig"; das war es so nicht |
| GFR3 | C liefert in M3 -1 mit Ende und +1 ohne, fuer alle drei Achsen; M2 in C gleich A | 75 % | **eingetroffen**: 42 von 42 (2 pi) je Netz; Anpassung = A_i; Transport konsistent; M2 gleich A | **ja, als Skizze** [M]: Jede Bindung kippt ihren Lift einmal; c-Zahlen aendern die Algebra nicht. Die Rechnung prueft die Buchhaltung |
| GFR4 | M4 bei R0: (C2)^2 = +1 in A, B und C | 70 % | **eingetroffen**: A (P1, P2, P3), B (beide w; K-Untergruppe V4), C (= A P2): Invariante +1 | **ja, als Skizze** [M]: R0 ist unter Konjugation fest; B wird bei R0 zur festen Projektion laengs z; C wird bei R0 zu A |

**Warum M1 bei B nicht scheitern kann [M nachher, nachgerechnet]:**

- In Lesart S ist der Beitrag einer Schleife am Knoten v ein Kegeltest mit Projektion und Push-off von v.
- Das Vertauschungsvorzeichen zweier Schleifen ist eine Summe ueber gemeinsame Knoten, und jeder Beitrag ist fest:
  - gemeinsamer Endknoten eines geteilten Wegs: 1
  - innerer Knoten des Wegs: 0
  - blosse Beruehrung: 0
- Fester Wert heisst: unabhaengig von Projektion und Push-off des Knotens, solange beide Schleifen am Knoten dieselbe
  Konvention benutzen. Ein geteilter Weg hat zwei Enden, also ist die Summe 0.
- (Huepfer, Schleife) ist knotenweise 0, weil delta_h = -delta_p gilt.
- Folge: Jede knotenweise Konvention ist vertraeglich, egal wie verschieden die Knoten sind. Gerechnet: bis 174 von 216
  Knoten mit anderer Konvention, M1 = 0.

## Ausgeloeste vorab festgelegte Bedeutung

- **Ausgeloest: "GFR2 und GFR3 treffen ein: Der Spin kommt nur aus der Hebungsbuchhaltung, die Statistik aus dem Twist.
  Das sind zwei getrennte Regeln. Folgekarte GERAHMTER-FADEN-2 mit Quantenrotor (j <= 1/2) je Knoten; die Huepfer
  transportieren den Rahmen."**
- Einschraenkungen dazu:
  - GFR2 konnte in der Kartenform nicht scheitern (Achse n_i).
  - Bei B ist das 2-pi-Vorzeichen auf den anderen Achsen meist gar nicht definiert. Das ist ein staerkerer Befund als
    "+1": Die knotenweise Richtung ist kein Rahmen, den man transportieren kann.
  - Das -1 in C ist Buchhaltung. Es folgt, sobald der Huepfer den Lift traegt; die Lift-Umbenennung q_i -> -q_i ist
    genau die Eichtransformation A_i. Ob eine Dynamik den Rahmen so dreht, ist nicht gezeigt; der Rahmen ist ein
    klassischer Hintergrund.
- **Nicht ausgeloest:** "GFR2 scheitert: Die knotenweise Levin/Wen-Rahmung traegt selbst Spin." B gibt nirgends -1.
- **Neu fuer die Folgekarte [H]:** Bei B sehen die Fermionen ein von der Rahmentextur erzeugtes Z2-Flussmuster. Offen:
  - Gibt es Quellen dieses Flusses (Kaefigprodukte)?
  - Wie haengt er an der Textur (Kammerwechsel, Raumwinkel)?
  - Ist er mit dem Kopplungsgesetz aus C verwandt?

## Grenzen

- Push-off w in B ist frei waehlbar; gerechnet sind zwei Richtungen. Bei n = z liegen beide im selben Sektor und geben
  dieselben Z-Mengen. Bei R1 unterscheiden sie sich stark, weil w_haupt nur 6 Grad neben einem projizierten Bein liegt.
  M1 = 0 und "kein -1 in M3" gelten fuer beide.
- R1 ist eine Konstruktion: 13 periodische Grundmoden, auf den groessten Bindungswinkel skaliert, 6 Saaten. Die globale
  Abweichung waechst mit dem Netz (bis 88 Grad bei n = 3). M3 nur fuer Saat 0 je theta_max.
- R2 als "kleine Kugel" auf dem Torus: Profil wie Z2-SCHUTZ (1/r), Kern r <= 1,8 (Knoten plus erste Schale), R = halbe
  Zellkante. Die Bindungswinkel sind gross (bis 173 Grad). R2z sieht B gar nicht (Drehung um z laesst n = z fest).
- M3-Transport: Stufe K heisst exakte Clifford-Abbildung von Huepfern und Sternen; Stufe F heisst gleicher
  Fermionfluss (LW S. 8, wie TWIST-SPIN-1).
  - Eine "bekleidete" Abbildung (Huepfer mal A_i) bei Seitenwechseln existiert algebraisch, ist aber nicht eindeutig.
    Sie ist nicht gerechnet. "B undefiniert" gilt fuer diese zwei Stufen.
- Nur eine oertliche Drehung eines einzelnen Knotens. Keine Dynamik, kein Rotor, kein Pyrochlor. Nur n = 2, 3.
- Spin-1/2-Pfeile statt Rotoren: wie in TWIST-PYRO-1 nur ueber die Vorzeichenalgebra (GF(2)).
- Synthetisch; keine Messdatenbestaetigung.

## Regelabweichungen und Selbstanzeigen

1. **Wie beauftragt:** kein Einfrieren, kein frischer Leser. Kein Journaleintrag, kein Peerbus, kein Commit; das bleibt
   bei der Leitung.
2. **Nach dem Rauchlauf geaendert:**
   - Achsen a2, a3 generisch, wegen exakter Entartung bei der Achse x.
   - Voller Fermionfluss je Rahmen ergaenzt.
   - Gegenprobe G2 ergaenzt. Die erste Fassung im Basislauf ist wirkungslos (beide Push-offs im selben Sektor, Ergebnis
     0, nicht verwertet). Die zweite Fassung lief im eigenen Lauf g2.
   - Vor allen Laeufen: Die R1-Saat gibt je Saat dieselbe Feldform fuer alle theta_max.
3. **Erklaerung erst nachher:** Die Herleitung "M1 kann in Lesart S nicht scheitern" stammt von nach dem Rauchlauf, nicht
   von vorab. Meine Erwartung vor dem Rauchlauf war das Gegenteil (Paare durch Kammerwechsel zwischen Nachbarn).
4. **Gescheiterte Vorhersage:** G2 "anderer Sektor > 0" ist nicht eingetreten.
5. **Codefassungen:** Basis und M3 liefen mit gerahmter_faden.py sha256 f7511531..., der Rauchlauf mit 9cd606b5....
   Die Endfassung dfddb50b... unterscheidet sich von f7511531... nur durch den nachgetragenen Modus g2. f7511531... ist
   nicht getrennt aufbewahrt; die Pruefsumme steht in jeder JSON-Kopfzeile.
6. **.69 ausserhalb des Starters:** mkdir, mv, sha256sum, tail, df, date, sleep und nohup fuer den Starter.
   - Beim Start der drei Laeufe lag die Standardeingabe auf "< /dev/null". Das ist eine Leseumleitung auf der .69,
     keine Schreibumleitung; der Brief verbietet Umleitungen dorthin, deshalb angezeigt.
   - Der ssh-Startbefehl lief als Hintergrundaufgabe des Werkzeugs; dessen Ausgabedatei legt das Werkzeug selbst im
     Sitzungsordner unter /tmp/claude-1000 ab.
7. **Lokal:** kein python, awk oder perl; jq nur lesend. Weiter benutzt:
   - sed -i (eine Zeile im eigenen neuen Code)
   - cp (der eingefrorenen Module, unveraendert)
   - sha256sum, scp, ssh, mkdir, cat, ls, date
   - grep nur im eigenen Code, kein Projekt-grep
8. **Code aus vorhandenen Ordnern:** twist_pyro.py und twist_spin.py nur kopiert (eingefrorene Fassungen, Pruefsummen
   17875033... und 3136d4e9...) und unveraendert importiert. gerahmter_faden.py ist neu.

## Dateien

- code/gerahmter_faden.py (neu), code/twist_pyro.py und code/twist_spin.py (unveraenderte Kopien)
- lauf-69/: rauch.json und .log; basis.json und .log; m3n2.json, m3n3.json und .log; g2.json und .log
- Pruefsummen beider Rechner: PRUEFSUMMEN-lokal.txt, PRUEFSUMMEN-69.txt (alle gleich)
- Auf der .69: /home/fmh/fmhc-physics-remote/gerahmter-faden-1/ (code/, rauch/, lauf/)

## Einfach gesagt

Wir haben getestet, ob das Teilchen am Fadenende beim Drehen ein Minuszeichen bekommt und ob das aus derselben Regel
kommt wie das Minuszeichen beim Vertauschen. Das Drehminus kommt nur, wenn man dem Faden ausdruecklich die
"Halbdrehungs-Buchhaltung" des Rahmens mitgibt; das Vertauschungsminus kommt dagegen aus dem Twist, also aus zwei
verschiedenen Regeln. Ein Rahmen, der nur die Blickrichtung je Knoten festlegt, ist immer widerspruchsfrei, gibt aber
kein Drehminus; er verbiegt nur das Feld, das die Teilchen beim Huepfen spueren.

---
Endzeit (date, beim Schreiben dieser Zeile): 2026-10-05 19:38:19 CEST. Zeitrahmen etwa 90 min ab 19:04:16 eingehalten.
