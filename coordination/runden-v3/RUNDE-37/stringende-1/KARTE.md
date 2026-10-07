# STRINGENDE-1: Koennen Teilchen am Ende von Strichen Fermionen sein? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 04:22:38 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn: "Ideate zu 1/2". IDEEN-EVOLUTION/GEN-04-SPIN-HALB.md, Idee H1, Rang 1.
  - In bosonischen Gittermodellen aus Strings koennen die offenen Enden Fermionen sein [L: Levin/Wen 2003]. Dieselbe
    Netzbildung gibt dort Photonen [L: Wen].
  - Finns Bild: "Punkte ergeben Striche" (STRING-1), Pfeil-Eis als Licht (FLUSS-1).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- **Ehrlich vorab:** Die Ergebnisse sind bekannte Mathematik [L], also vorab ableitbar. Die Karte zeigt den Mechanismus
  konkret fuer Finns Bild und prueft, ob wir ihn sauber nachbauen.

## Schreibtisch (vor jeder Rechnung)

- **2D-Torus-Code (Kitaev) [L]:**
  - Spins auf den Kanten eines Quadratgitters.
  - Elektrische Strings (Produkte von Z auf Kanten) enden auf e-Teilchen.
  - Magnetische Strings (Produkte von X auf dualen Kanten) enden auf m-Teilchen.
  - e und m sind einzeln Bosonen. Ihr Verbund epsilon = e x m, das Ende eines "Doppelstrings", ist ein Fermion
    (Vertauschungsphase -1).
- **Messvorschrift [L: Levin/Wen 2003, Verfahren mit drei Strings]:** Drei String-Operatoren W1, W2, W3 enden an einem
  gemeinsamen Punkt. Die Vertauschungsphase ist theta = W3 W2^-1 W1 W3^-1 W2 W1^-1 (Reihenfolge aus der Quelle
  uebernehmen und pruefen).
  - Bei Pauli-Operatoren laesst sich alles exakt als Vertauschungsvorzeichen ausrechnen (Symplektik ueber GF(2)) [M].
- **3D [L?]:** Levin/Wen geben ein 3D-Gittermodell, dessen Stringenden Fermionen sind. Wenn es sich aus der Quelle
  nachbauen laesst, gilt dieselbe Messung dort.

## Test (Code-Agent)

- **2D:** Torus-Code auf einem kleinen Gitter (z. B. 8x8, periodisch).
  - String-Operatoren fuer e, m und epsilon.
  - Vertauschungsphase nach dem Drei-String-Verfahren.
  - Topologischer Spin von epsilon: 2-pi-Drehung bzw. Verdrillung des Doppelstrings.
- **Gegenproben:** andere Stringwege (Wegunabhaengigkeit); Kommutation mit allen Stern- und Plakettenoperatoren
  ausserhalb der Enden (die Strings sind "unsichtbar").
- **3D**, wenn die Quelle es hergibt: das fermionische String-Netz nach Levin/Wen. Gezielter Abruf des arXiv-Abstracts
  bzw. -Volltexts erlaubt (hoechstens 5 Abrufe, keine Websuche).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SE0 | Kontrolle: Alle String-Operatoren kommutieren mit allen Stern- und Plakettenoperatoren ausser an ihren Enden; Ergebnis unabhaengig vom gewaehlten Weg | 90 % |
| SE1 | 2D: Vertauschungsphase e: +1, m: +1, epsilon: -1 | 90 % |
| SE2 | 2D: Gegenseitige Umrundung e um m gibt -1 (gegenseitige Halbzahligkeit), und sie ist die Ursache von SE1 [M] | 85 % |
| SE3 | 3D: Ein Gittermodell, dessen Stringenden die Vertauschungsphase -1 haben, laesst sich aus der Quelle nachbauen und messen | 45 % |

**Bedeutung (vorab):**
- **SE1 und SE3 treffen ein:** In einem Netz aus Strichen, das nur aus bosonischen Bausteinen besteht, koennen die Enden
  der Striche Fermionen sein. Fuer Finns Bild waere das der natuerlichste Platz fuer Spin 1/2: Elektronen als
  Stringenden, Licht als Netzwellen [L: Wen; H fuer die Uebertragung auf Finns Netz].
- **SE3 verfehlt:** In 3D ist der Nachbau zu gross fuer diese Karte; dann bleibt 2D als Vorbild.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (nur CPU; die Leitung nutzt diese Spur kurz mit,
  Lock wartet); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
