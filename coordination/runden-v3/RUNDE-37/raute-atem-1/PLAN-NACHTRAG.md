# RAUTE-ATEM-1: Nachtrag zum Plan (nach dem Einfrieren; beschreibend)

- Geschrieben ab 2026-10-04 18:47:30 CEST (date), nach dem Einfrieren (18:39:07 CEST) und nach dem Ende der Hauptlaeufe
  (16:45:19 UTC), **vor jeder Sicht auf Hauptergebnisse** (gesehen nur Laufzeiten und rc). PLAN.md und der eingefrorene
  Code bleiben unveraendert; Urteile nach PLAN.md Abschn. 5 gelten weiter.
- Anlass: Berichtigung der Leitung (frischer Leser SCHREIBTISCH-LESER, Befund A1, Datei
  RUNDE-37/schreibtisch-leser/GEGENLESEN.md), eingegangen nach dem Einfrieren. Alles hier ist **[Zusatz Leitung, nicht
  Kartenwortlaut]**.

## N1. Pruefung von A1 [M, selbst nachgerechnet]

- Gemittelte Huellenkopplung auf den fuenf Rautenkanten, alle gleich stark (J): H = J Summe cos(Delta_ij).
- Setze A = 0, B = theta. C und D sind je an A und B gekoppelt; ihr bester Wert ist theta/2 + 180 Grad mit Beitrag
  -2 |cos(theta/2)| je Punkt. Also E(theta) = J [cos(theta) - 4 |cos(theta/2)|].
  - theta = 0: E = -3 J (A = B, C = D = A + 180 Grad).
  - theta = 120 Grad: E = -2,5 J; dE/dtheta = J [-sin(theta) + 2 sin(theta/2)] = +0,866 J, also nicht einmal stationaer.
  - Um theta = 0: E = J (-3 + theta^4/32 + ...), das Minimum ist nur quartisch (weiche A-B-Phase).
- **A1 haelt.** Mein Plan (D1, D5) hat den Fehler der Karte uebernommen: Ich hatte nur gegen "A, B gegenphasig" verglichen,
  nicht gegen A = B.
- Folgen [M]:
  - Der Raute-Grundzustand (0, 0, 180, 180) hat Zeigersumme 0 und liegt damit schon in der Grundmannigfaltigkeit des
    geschlossenen Tetraeders (K4). Beim Schliessen ist keine Umordnung zu erwarten, also kein Antrieb fuer einen
    Klapptakt.
  - C = D bleibt im Gleichtakt -> Anziehung -> Falten und Schliessen (RA1) bleibt erwartet.
  - Statik bei diesen festen Phasen (Tetraeder): A-B und C-D Gleichtakt -> je Druck B/r^2; vier Aussenstaebe Gegentakt
    -> je Zug B/r^2. **Alle sechs Betraege sind B (bis auf r).** "Das Gegenteil von Finns Kraftbild" (Karte) faellt.
    Gedrueckte Staebe sind kuerzer (r < 1), gezogene laenger: Am Schreibtisch liegen A-B und C-D gleichauf oben, die
    Aussenstaebe knapp darunter. Ob A-B oder C-D vorn liegt, entscheiden dann kleine Effekte (z. B. kurzes Loesen der
    C-D-Fangbindung im Atemtakt). Die eingefrorene FP-Regel hat keine Gleichstandstoleranz; ich aendere sie nicht, nenne
    aber im Ergebnis den Abstand |A-B| - |C-D| in Einheiten von B und die Saatenstreuung.

## N2. Kennzeichnung der Urteile (vorab, vor Sicht)

- **RA0 nach Kartenwortlaut (120 Grad je Dreieck) ist vorab als verfehlt ableitbar** (N1). Ebenso der Phasenteil von RA0
  nach Plan. So gekennzeichnet; Regel nicht umgeschrieben.
- **RA2: als Vorhersage stehen gelassen, vorab "erwartet verfehlt"** (kein Umordnungsmechanismus).
- FP: unveraendert Finns Vorhersage. Erwartung nach N1: Gleichstand A-B gegen C-D, Ausgang offen, Abstand klein.
- RA1: unveraendert erwartet eingetroffen.

## N3. B-Befund des Lesers: Grenzen

- Das Medium wirkt nach der Karte nur auf die Lagen, nicht auf die Phasen (in einer echten Fluessigkeit koppelt die
  Abstrahlung auch die Takte). Das bleibt so; es ist eine **Grenze des Modells**: Ein Medium, das Gleichtakt auch in den
  Phasen beguenstigt, koennte das Phasenmuster und damit Falten und Kraefte aendern.
- Lagenbeweglichkeit zu Takt: mu_x k / omega = 0,32 (PLAN Abschn. 1 D1 und Abschn. 3). Begruendung: Raute und Tetraeder
  sind statisch bestimmt; folgen die Lagen dem Atmen schnell (mu_x k >> omega), verschwinden Stabkraefte und
  Huellenkopplung (Anteil omega^2/(lambda^2 + omega^2) je Mode). Langsam gegen den Atem, aber schnell gegen Falten
  (mu_x B = 0,06 bis 0,16 je Takt) und Phasenordnung (K = 0,063 je Takt).

## N4. Zusatzvariante [Zusatz Leitung], beschreibend, eigene Regel vorab

- **Modell:** wie PLAN.md, aber eps_A = eps_B = 0,10 und eps_C = eps_D = 0,05 (Finns Skizze: kleine Seitenkreise). Die
  gemittelte Kopplung einer Kante ist proportional eps_i eps_j: A-B 1, Aussenkanten 1/2, C-D 1/4 (relativ). Code:
  code/raute_var.py (aus raute.py; nur EPS_VEC je Punkt, sonst identisch), Auswertung code/auswertung_var.py (ruft die
  eingefrorenen Funktionen aus auswertung.py).
- **Schreibtisch [M]:**
  - Raute mit J_AB = 2 J_aussen (Einheit J_aussen): E(theta) = 2 cos(theta) - 4 |cos(theta/2)|;
    dE/dtheta = 0 bei cos(theta/2) = 1/2, also theta = 120 Grad, E = -3 gegen -2 bei theta = 0.
    **Hier ist das 120-Grad-Muster der Grundzustand** (A = 0, B = 120, C = D = 240 Grad, gegenlaeufige Umlaeufe).
  - Geschlossen (C-D-Kopplung 1/4 von A-B): Spaltung C = 240 + delta, D = 240 - delta gibt
    E(delta) = -1 - 2 cos(delta) + 0,5 cos(2 delta) = -2,5 + delta^4/4 + ...: **die Spaltung ist (quartisch) stabil**,
    also auch hier keine Umordnung am Schreibtisch erwartet.
  - Statik bei festen Phasen: C-D Druck B, uebrige Zug B/2 -> FP verfehlt erwartet.
- **Laeufe:** 3D haupt fuer B = 0,03, 0,05, 0,08 (je 4 Saaten, 500 Takte); Kontrollen B = 0 in 3D und 2D; 2D haupt
  B = 0,05. Ordner .69 raute-atem-1/lauf-var/, lokal lauf-69/var/.
- **Regeln (beschreibend, zaehlen nicht als Kartenurteil):** wie PLAN.md Abschn. 5 in der Plan-Fassung:
  - V-RA0: alle 8 Kontrollen 120 Grad auf den fuenf Staeben (< 0,1 rad) und |Delta_CD| < 0,1 rad; 3D keine Faltung
    (< 5 Grad in 200 Takten); Werkzeugprobe < 1e-6.
  - V-RA1: alle 12 3D-Laeufe schliessen bis 200 Takte.
  - V-RA2: wie RA2 (Plan und Karte).
  - V-FP: wie FP (Plan und gepoolt).
- **Meine Erwartung [H]:** V-RA0 ja, V-RA1 ja, V-RA2 nein, V-FP nein.
