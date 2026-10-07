# TETRA-KOPPLUNG: Spueren sich zwei verspannte Klumpen ueber ihr Spannungsfeld? (Runde 17)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 10:53:21 CEST (date), vor jeder Rechnung.
- Anlass:
  - Finn, 02.10.: "könnten tetraeder spannungen besitzen die sie miteinander koppeln?"
  - TETRA-KLUMPEN: Zwei Ikosaeder, die sich ein Stueck teilen, sind teurer als einzeln (Delta = +0,0043).
  - Quellenpruefung: Runde Klumpen (Ikosaeder-Symmetrie) wirken wie Dilatationszentren und koppeln im isotropen Medium
    in erster Ordnung nicht. Unrunde (19er, axial) koennen mit ~ 1/d^3 koppeln (Eshelby-Bild [L?/teilweise S]).
- Frage: Wie haengt die Kopplung zweier getrennter, eingebetteter Spannungsquellen vom Abstand, von der Richtung, von der
  Form der Quelle und von der Anisotropie des Mediums ab?
- Explorativ (v3), Hypothesen [H].

## Modell

- Federgitter mit Naechstnachbarfedern (k = 1, Ruhelaenge 1), lineare Elastizitaet:
  - Verschiebung u loest K u = f; f kommt aus geaenderten Ruhelaengen der Defektbindungen. Duenne Matrix, direkter
    Loeser.
  - Energie E = (1/2) u^T K u - f^T u + const, bzw. die exakte harmonische Energie der Fehlpassung.
- **Medien:**
  - M-iso: 2D-Dreiecksgitter, elastisch isotrop
  - M-aniso2: 2D-Quadratgitter mit zweiten Nachbarn, stabil und anisotrop
  - M-fcc: 3D fcc mit Naechstnachbarn (Anisotropie A = 2 C44/(C11 - C12) = 2 aus STABIL S1)
- **Quellen:**
  - Q-A ("runder Klumpen"): alle Bindungen eines Knotens zu seinen Nachbarn um eps = 0,05 verkuerzt. Das ist ein
    isotropes Dilatationszentrum, im Kleinen wie das Ikosaeder mit gestauchten Speichen.
  - Q-B ("unrunder Klumpen"): zwei benachbarte Knoten, deren Bindungen und die gemeinsame Bindung verkuerzt; axial wie
    der 19er.
- **Wechselwirkung:** E_int(d, Richtung) = E(zwei Quellen) - 2 E(eine Quelle) + E(keine).
  - Fuer d von 3 bis etwa L/4, mindestens in drei Richtungen, bei Q-B dazu zwei relative Orientierungen.
  - Zwei Systemgroessen (periodisch oder fester Rand; Bildladungseffekte berichten).
- **Kontrollen:**
  - E_int ist exakt quadratisch in eps (lineare Elastizitaet).
  - Zwei Systemgroessen.
  - E einer Einzelquelle gegen die Kontinuumsformel der Eshelby-Dilatation, nur als Groessenordnung [L?].

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K1 | M-iso, Q-A/Q-A: E_int faellt schneller als 1/d^2 (in erster Ordnung null, Rest aus Diskretheit ~ 1/d^4) | 75 % |
| K2 | M-aniso2, Q-A/Q-A: E_int ~ 1/d^2, Vorzeichen wechselt mit der Richtung (Achse gegen Diagonale) | 70 % |
| K3 | M-iso, Q-B/Q-B: E_int ~ 1/d^2, ungleich null, Vorzeichen haengt von der relativen Orientierung ab | 80 % |
| K4 | M-fcc, Q-A/Q-A: E_int ~ 1/d^3, Vorzeichenwechsel zwischen [100] und [111] | 65 % |
| K5 | M-fcc: Bei gleichem d ist abs(E_int) fuer Q-B/Q-B groesser als fuer Q-A/Q-A | 70 % |

**Bedeutung fuer Finn (vorab):**
- Treffen K1 bis K3 ein: Spannungen koppeln verspannte Klumpen, aber nur, wenn Klumpen oder Umgebung "unrund" sind. Runde
  Klumpen in einem runden Medium spueren sich kaum.
- Ob anziehend oder abstossend, haengt von Richtung und Ausrichtung ab. Das ist eine Kraft aus Geometrie, nicht
  eingesetzt [H].

## Rahmen

- Code-Agent, eigener Code (numpy, scipy.sparse). Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu6, je <= 10 min.
  Plan vorab einfrieren, Nachtraege nur eingefroren. Zeitbox 90 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
