# LUND-REGGE-MASSE-1: Verschwindet die Richtungsabhaengigkeit der Schwerewellen ohne Abstimmung, wenn die Traegheit wie in der Literatur auf der Geschwindigkeitsseite steht? (Runde 48, Folgekarte zu REGGE-KINETIK-L)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 10:11:16 CEST (date), vor jeder Rechnung.
- **Herkunft:** REGGE-KINETIK-L (RUNDE-37/regge-kinetik-l/DOSSIER.md; Literatur, ohne frischen Leser) [S, ES]:
  - Die Standardform ist die Lund-Regge-Supermetrik, Summe_tau V(tau) [dh:dh - (tr dh)^2] (Hartle/Miller/Williams 1997, Gl. 3.5 und 3.13). Sie ist volumengewichtet und wirkt auf die **Geschwindigkeiten**.
  - Unser Code legt die DeWitt-Form je Tetraeder auf die **Impulse** (J = inverse Masse; TT-ISO-1, IMPULS-NETZ-1). Ueber geteilte Kanten summiert ist das nicht dasselbe.
  - Feinberg/Friedberg/Lee/Ren 1984 (Abstract): Kontinuumsnaehe fuer jedes Gitter, Korrekturen ~l^2. Christiansen 2011: Eigenpaar-Konvergenz fuer den statischen linearisierten Regge-Operator mit L2-Masse.
- **Projektbefunde dazu [P]:**
  - Die Regge-Steifigkeit ist langwellig schon isotrop; die Richtungsabhaengigkeit sass in der effektiven Masse (TT-ISO-1, OKTA-SCHATTEN-1).
  - Lange TT-Wellen sind bis 1e-5 projizierte affine Wellen (TT-GLAS-2).
  - Auf V gibt es mit impulsseitigen Gewichten einen exakt isotropen Punkt, aber der Bahnlagen-Gang bleibt >= 0,0039; alle Gewichte wirken wie ein Regler (SKALAR-MISCH-1).
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Rechnung (Code-Agent)

- **Masse:** geschwindigkeitsseitige Lund-Regge-Form. Je Tetraeder V_t G_lambda(h-Punkt, h-Punkt) mit h-Punkt aus den sechs Kantenraten (Rekonstruktion h = R_t q, q_e = d(l_e^2)), lambda wie im Projektcode. Das wird ueber alle Tetraeder summiert und erst danach fuer die Hamilton-Form invertiert (Legendre). Reduktion R1 wie im Projektcode (laut REGGE-KINETIK-L korrekte Dirac-Reduktion).
- **Netze:** V und S (= C15), A15 (DEFEKT-NETZ-1), Glas N = 128 (TT-GLAS-1, 4 Saaten).
- **Messen:**
  - TT-Spanne bei mehreren kl (mindestens 0,02, 0,05, 0,1, 0,2), mindestens 13 Richtungen
  - Extrapolation kl -> 0 und Koeffizient der (kl)^2-Korrektur
  - Stabilitaet an 511 k (Kristalle) bzw. am Superzellen-Gitter (Glas)
  - auf V zusaetzlich der Bahnlagen-Gang im IMPULS-NETZ-1-Aufbau (gleiche Quelle, 12 Bahnen, ohne V1 wie dort)

## Ableitbarkeitsprobe (Leitung, Bausteine verkettet)

- **Vorab ableitbar [M]:** Bei gleichmaessiger Verzerrungsrate hat jedes Tetraeder dasselbe h-Punkt. Die geschwindigkeitsseitige Lund-Regge-Form ist dann auf jedem Netz exakt der Kontinuumswert (LR0, Kontrolle).
- **Kette [ES, nicht bewiesen]:**
  - Sind die langen TT-Wellen auch mit dieser Masse affin (TT-GLAS-2 zeigte das fuer die impulsseitige Masse) und ist die Regge-Steifigkeit langwellig isotrop (TT-ISO-1), dann ist die TT-Geschwindigkeit fuer kl -> 0 auf jedem Netz isotrop.
  - LR1 waere dann eine Kontrolle. Der Agent prueft diese Kette zuerst am Schreibtisch und schreibt vor dem Einfrieren, ob sie haelt.
- **Nicht ableitbar:**
  - der (kl)^2-Koeffizient und seine Richtungsabhaengigkeit
  - der Bahnlagen-Gang, der an der Quellkopplung bei endlicher Groesse haengt
  - das Glas bei endlichem N
  - die Stabilitaet

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LR0 | Kontrolle, vorab ableitbar: Bei gleichmaessiger Verzerrungsrate ist die Masse auf V, S, A15 und Glas gleich dem Kontinuumswert (auf 1e-12) | 90 % |
| LR1 | [ES/H] Die auf kl -> 0 extrapolierte TT-Spanne liegt auf V, S und A15 ohne jede Abstimmung unter 1e-6 | 55 % |
| LR2 | [H] Auf V faellt der Bahnlagen-Gang unter 1e-3 (impulsseitig 0,0039 bis 0,0047) | 35 % |
| LR3 | [H] Auf Glas N = 128 ist die TT-Spanne bei kl = 0,05 hoechstens halb so gross wie mit J = 1 je Zelle | 50 % |
| LR4 | [H] V und S sind mit dieser Masse an allen 511 k stabil | 70 % |

**Bedeutung (vorab):**
- **LR1 und LR4 treffen ein:** Die Richtungsabhaengigkeit der Schwerewellen war eine Folge der Bauweise (Masse auf der falschen Seite). Mit der Standardform ist das Netz von selbst isotrop, ohne Abstimmung, also emergent im Sinne von Finn.
  - Das wuerde TT-ISO-1, TT-GLAS-1/2, DEFEKT-NETZ-1 und SKALAR-MISCH-1 als Aussagen ueber die impulsseitige Masse einordnen und zu einer Berichtigung an Finn fuehren.
- **LR2 trifft ein:** Auch der Abstrahlungsfehler hing an der Masse.
- **LR1 verfehlt:** Die Anisotropie ist keine Folge der Seitenwahl. Dann wird "Regime K" (kovariante 4D-Zeit) der naechste Weg.

## Rahmen

- Code-Agent. Code aus tt-iso-1/code, tt-glas-1/code, impuls-netz-1/code, defekt-netz-1/code und skalar-misch-1/code kopieren, dort nichts aendern.
- Abgrenzung: HODGE-MASSE-1 laeuft (Reduktion, impulsseitige A2, Energiesprung beim Zug) und rechnet diese Masse ausdruecklich nicht.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256). Ein ehrlicher Teilbericht ist besser als keiner: zuerst LR0 und V, dann S, A15 und Glas, dann LR2.
- Synthetisch, keine Messdatenbestaetigung.
