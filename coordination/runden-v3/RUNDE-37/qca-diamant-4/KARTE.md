# QCA-DIAMANT-4: Gibt es auf Finns Diamantnetz eine Quanten-Spielregel mit Spin-1/2-Kegel, wenn jeder Knoten vier Zustaende hat? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 06:47:15 CEST (date), vor jeder Rechnung.
- **Anlass:** QCA-TETRA-1 (RUNDE-37/qca-tetra-1/ERGEBNIS.md, Folgevorschlag des Agenten).
  - BCC-Netz mit 2 Zustaenden: Isotropie im Sinn der Quelle (L_2, die drei 180-Grad-Drehungen) erzwingt Spin 1/2 und
    einen Weyl-Kegel. Mit der vollen Tetraedergruppe T (auch 120-Grad-Drehungen) gibt es keinen Automaten.
  - Diamantnetz (Finns Netz, vier Striche je Knoten) mit 2 Zustaenden je Knoten: kein isotroper unitaerer Automat.
  - Die Ausgaenge dort waren am Schreibtisch beweisbar (M1 bis M7 in qca-tetra-1/PLAN.md).
- **Frage:**
  - Teil A: Was ist auf dem Diamantnetz mit 4 Zustaenden je Knoten moeglich?
  - Teil B: Gibt es auf BCC mit 4 Zustaenden einen Dirac-Automaten, der unter der vollen Tetraedergruppe T symmetrisch
    ist?
- Kennzeichen: [M] Mathematik, [L] Literatur, [L?] unsicher, [H] Hypothese.

## Vorgehen (Code-Agent)

- **Schreibtisch zuerst (Pflicht):**
  - Fuer jede Vorhersage vor jeder Rechnung pruefen, ob ein Beweis sie entscheidet (Darstellungstheorie, Defektformel,
    Unitaritaetsbedingungen wie in M1 bis M7).
  - Was bewiesen ist, wird als "vorab ableitbar" gekennzeichnet; die Numerik bestaetigt dann nur.
  - Gerechnet wird vor allem, was offen bleibt.
- **Teil A (Diamant, 4 Zustaende je Knoten):**
  - Gleiche Schrittstruktur wie QCA-TETRA-1 Teil C: A -> B laengs +e_a, B -> A laengs -e_a.
  - Zusaetzlich eine im Plan begruendete zweite Fassung, z. B. ein gleichzeitiger Sprung beider Untergitter.
  - Isotropie im Sinn der Quelle, auf die Punktgruppe des Diamantknotens uebertragen: die Gruppe, die die vier
    Richtungen ineinander ueberfuehrt (L_2 bzw. T), je 4-dim Darstellung (linear und projektiv, zerlegbar und
    unzerlegbar). Die Liste im Plan vollstaendig machen.
  - Suche mit vielen Starts. Treffer einordnen: trivial, Kegel bei k = 0, Knotenlinien. Wirkung von 360 Grad auf die
    inneren Zustaende.
- **Teil B (BCC, 4 Zustaende, volle Gruppe T):** Dirac-artiger Automat (zwei Weyl-Anteile mit Massenkopplung) mit
  Kovarianz unter T, inklusive 120-Grad-Drehungen?

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QD0 | Kontrolle: QCA-TETRA-1 wiedergefunden (BCC-Weyl mit 2 Zustaenden unter L_2: Treffer; Diamant mit 2 Zustaenden: keine Treffer) | 90 % |
| QD1 | [H] Teil A: Auf dem Diamantnetz gibt es mit 4 Zustaenden je Knoten einen nichttrivialen isotropen unitaeren Automaten mit Kegel bei k = 0 | 50 % |
| QD2 | [H] Bei jedem solchen Treffer wirken die Drehungen projektiv auf die inneren Zustaende (360 Grad -> -1) | 60 % |
| QD3 | [H] Teil B: Auf BCC gibt es mit 4 Zustaenden einen nichttrivialen unitaeren Automaten mit Kegel, der unter der vollen Gruppe T (mit 120-Grad-Drehungen) kovariant ist | 35 % |

**Bedeutung (vorab):**
- **QD1 und QD2 treffen ein:** Auf Finns Netz traegt die einfachste richtungsgleiche Quanten-Spielregel ein
  Spin-1/2-Teilchen, nur mit doppelt so vielen inneren Zustaenden wie auf BCC. Das waere ein Dirac- oder doppeltes
  Weyl-Fermion aus dem Tetraedernetz.
- **QD3 trifft ein:** Mit 4 Zustaenden ist die volle Tetraeder-Symmetrie samt Spin 1/2 erreichbar.
- **QD1 verfehlt:** Das Diamantnetz mit einfachen Spruengen traegt keine Weyl/Dirac-Regel. Dann waere BCC (acht
  Tetraederrichtungen je Knoten) die natuerlichere Netzform fuer Fermionen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und p4000b; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
