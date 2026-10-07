# INDUZIERT-DICHTE-4D: Gibt "Zahl = Volumen" auch in 4D der Materie Einsteins Vorzeichen fuer den konformen Modus? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 08:14:44 CEST (date), vor jeder Rechnung.
- **Anlass:** INDUZIERT-DICHTE-2D.
  - In 2D gibt die Streuung nach physikalischer Flaeche mit Neuvernetzung die konforme Steifigkeit -0,0123 +- 0,0012
    gegen Polyakov -0,0133. Sicher negativ und Polyakov-gross.
  - Das feste Netz gibt +0,159.
  - Der Gitterterm war ein Artefakt der beim Verbiegen mitwandernden Punktdichte.
  - In 4D (INDUZIERT-1, festes Kuhn-Netz) war der konforme Modus steif und positiv, c0s/c2 = +3,4 bis +142 statt -2.
- **Schreibtisch [L/M/H]:**
  - Im Kontinuum induziert ein minimal gekoppelter Skalar in 4D ein Einstein-Glied mit positivem G [L Sakharov; Visser].
    Der konforme Modus hat dann negative Steifigkeit (das bekannte "falsche" Vorzeichen).
  - Der Koeffizient ist nicht universell: ~ Lambda^2, also ~ rho^(1/2) bei Dichte rho in 4D [H].
  - Universell waere nur das Verhaeltnis c0s/c2 = -2. Es braucht spurfreie Verformungen und ist hier noch nicht Teil der
    Karte.
  - Pruefbar sind also Vorzeichen und Skalierung des konformen Modus.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- **Geometrie:** 4D-Torus, konforme Metrik g = e^(2 sigma) delta, sigma = s cos(k.x).
  - Feste Punktzahl N, verteilt nach physikalischem Volumen (Dichte ~ e^(4 sigma)), per 1D-Verteilungsfunktion laengs k
    wie in INDUZIERT-DICHTE-2D.
- **Netz:** periodische 4D-Delaunay-Vernetzung.
  - Randkopien nur in einem Saum, nicht alle 80 Kopien.
  - Kantenlaengen physikalisch; P1-Skalar aus den Simplex-Gram-Matrizen (Code aus INDUZIERT-1).
  - log det' per duenner LU.
- **Groessen:** N so gross, wie Laufzeit und 4 GB erlauben (Laufzeit vorab messen), mindestens zwei Dichten bei festem
  Volumen; viele Saaten.
- **Kontrolle:** Variante "festes Netz" (nur Kantenlaengen aendern sich) mit denselben Punkten.
- **Messung:** wie INDUZIERT-DICHTE-2D. Steigung von c(k) gegen k^2 ueber ein k-Fenster, k^0-Glied (Volumenterm) mit
  ausgeglichen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IV0 | Kontrolle: Die Variante "festes Netz" gibt eine positive konforme Steifigkeit (Vorzeichen wie INDUZIERT-1) | 70 % |
| IV1 | [H] Mit Streuung nach Volumen und Neuvernetzung ist die konforme Steifigkeit negativ (Einstein-Vorzeichen), Steigung + 2 SE < 0 | 50 % |
| IV2 | [H] Ihr Betrag waechst mit der Dichte etwa wie rho^(1/2): Exponent zwischen zwei Dichten 0,5 +- 0,2 | 35 % |
| IV3 | Kein Volumenterm: k^0-Glied innerhalb 3 SE mit null vertraeglich | 60 % |

**Bedeutung (vorab):**
- **IV1 trifft ein:** "Zahl = Volumen" gibt auch in 4D den konformen Modus mit Einsteins Vorzeichen. Das feste Netz hatte
  das falsche.
- **Dazu IV2:** Die induzierte Steifigkeit verhaelt sich wie ein Einstein-Glied mit der Netzdichte als Abschneidelaenge.
- **Naechster Schritt:** spurfreie Verformungen, also c2 und das Verhaeltnis -2. Das ist der eigentliche Einstein-Test.
- **IV1 verfehlt:** In 4D reicht Volumen-Zaehlung allein nicht; dann zaehlt auch die Netzdynamik.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
- Wenn die 4D-Vernetzung in 10 min nicht zu schaffen ist: "nicht gerechnet" mit Laufzeitmessung und Abschaetzung des
  noetigen Aufwands.
