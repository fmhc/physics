# INDUZIERT-WILSON-2D: Gibt ein Fermion mit Wilson-Glied auf dem Zufallsnetz mit "Zahl = Volumen" Polyakovs Antwort, und haelt die Kaehler-Dirac-Herleitung? (Runde 40)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 11:31:50 CEST (date), vor jeder
  Rechnung.
- **Anlass (INDUZIERT-DIRAC-2D, RUNDE-37/induziert-dirac-2d/ERGEBNIS.md):**
  - Skalar auf dem Zufallsnetz mit Punkten nach Flaeche: c_eff = 0,92 +- 0,12 (Polyakov).
  - (A) naiver Dirac-Operator: c_eff = 1,69 +- 1,15, siebenmal so verrauscht wie der Skalar; Ursache vermutlich das dichte
    Band bei E = 0 (Doppler des Zufallsnetzes, wie in 3D bei SPIN-ZUFALLSNETZ-1).
  - (B) Kaehler-Dirac: +48,4 (Netzartefakt vermutet). Schreibtisch des Agenten [M, nicht gegengelesen]: abs det'(d + delta)
    = det' Delta_0 det' Delta_2, Delta_2 isospektral zu Delta_0, also c = -4, falsches Vorzeichen schon im Kontinuum.
- **Idee:** Das Standardmittel gegen Doppler ist ein Wilson-Glied r L (L = Skalar-Laplace des Netzes, je
  Spinorkomponente). Es hebt das Band bei E = 0 an und laesst den langwelligen Kegel bis O(k^2) unberuehrt. Erwartung im
  Kontinuum: c = 1 fuer das leichte Fermion; schwere Anteile geben in 2D nur lokale Glieder [L].
- **Ableitbarkeitsprobe (Leitung):** Ob ein Gitter das universelle c = 1 trifft, ist wie beim Skalar eine
  Realisierungsfrage, nicht ableitbar; das Rauschen ist nicht ableitbar. Projekt-grep "wilson": nur Hinweise in
  SPIN-ZUFALLSNETZ-1 (Abhilfe) und GEGENLESEN-R35, keine Rechnung.
- Kennzeichen: [M] Mathematik, [L] Literatur, [H] Hypothese.

## Test (Code-Agent; Schreibtisch zuerst)

- **Schreibtisch W4 (vor jeder Rechnung):** die KD-Herleitung des Vorgaengers frisch pruefen (Hodge-Zerlegung in 2D,
  Vorzeichen und Normierung von c relativ zum Skalar, Fermion-Konvention Gamma = -log abs det). Hoechstens 3 gezielte
  Abrufe zur Literatur (konforme Anomalie von Dirac-Kaehler-Fermionen in gekruemmtem 2D); Fundstellen nur aus selbst
  gelesenem Text. Ergebnis in PLAN.md, bevor gerechnet wird.
- **Netze und Messgroesse:** wie INDUZIERT-DIRAC-2D (Code dort wiederverwenden; Punkte nach physikalischer Flaeche,
  Neuvernetzung je Verformung, gleiches k-Fenster, k^4-Ausgleich, zwei Netzabstaende). Dieselben Saaten wie dort, damit
  Skalar und (A) bitgleich nachgerechnet werden koennen.
- **Fermion mit Wilson-Glied:** D_W = D_A + r L (Gewichte von L wie beim Skalar). Zwei Werte r = 1 und r = 1/2, vor dem
  Einfrieren gebunden, kein dritter Wert nach Befund. Gamma = -(1/2) log det'(D_W^dagger D_W), Nullmoden-Behandlung im
  Plan begruenden.
- **Kontrollen:** Skalar und (A) ohne Wilson bitgleich mit INDUZIERT-DIRAC-2D auf denselben Saaten; Spektrum von D_W
  nahe E = 0 (Band angehoben?); Determinante gegen dichte Eigenwerte bei kleinem N.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| W0 | Kontrolle: Skalar und (A) ohne Wilson auf denselben Saaten bitgleich mit INDUZIERT-DIRAC-2D | 85 % |
| W1 | [H] Wilson r = 1: c_eff im Band [0,7; 1,3] mit SE <= 0,3 | 40 % |
| W2 | [H] Streuung je Saat des Wilson-Fermions hoechstens doppelt so gross wie die des Skalars | 55 % |
| W3 | [H] r = 1/2 und r = 1 stimmen innerhalb 2 SE ueberein | 55 % |
| W4 | Schreibtisch: Die KD-Beziehung gilt, und c_KD = -4 in der Normierung der Karte (Kontinuum) | 75 % |

**Bedeutung (vorab):**
- **W1 und W2 treffen ein:** Mit dem Standardmittel geben auch Fermionen auf dem Zufallsnetz mit "Zahl = Volumen" die
  richtige 2D-Schwerkraft-Antwort. Materie beider Sorten steht dann auf derselben Buehne (2D, euklidisch) [H].
- **W1 verfehlt mit c_eff > 1,3:** Das raue Band traegt auch mit Wilson-Glied bei; Doppler auf Zufallsnetzen stoeren die
  Schwerkraft-Antwort.
- **W4 haelt:** Kaehler-Dirac ist als schwerkrafttaugliche Fermion-Bauart in 2D ausgeschlossen; bricht W4, wird der Satz
  in der Ernte von INDUZIERT-DIRAC-2D zurueckgenommen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 120 min.
