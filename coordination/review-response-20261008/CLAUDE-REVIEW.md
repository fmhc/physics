# Bewertung der zwei Reviews vom 08.10.2026 durch Claude (Leitung claude-primary)

Grundlage: USER-REVIEW.txt und USER-REVIEW-2.txt in diesem Ordner, dazu die Ergebnisdateien im Arbeitsprojekt. Nichts
neu gerechnet. Kennzeichen: [E] gerechnet (Projektdatei), [M] Mathematik am Schreibtisch, [L] Literatur aus dem
Gedaechtnis, [H] Hypothese.

## 1. Gesamturteil zu den Reviews

Beide Reviews sind im Kern berechtigt, und ich teile das Hauptergebnis: Das Repo ist ein glaubwuerdiges, transparentes
Rechen-Notizbuch, aber keine validierte neue Theorie. Die positiven Befunde sind Konsistenzpruefungen bekannter Physik
auf einem neuen Gitter.

- **Zustimmung:**
  - **Kontinuums- und Volumenlimes fehlen.** Bei U(1) nur L = 2 und 3, bei SU(2) zwei Gitterabstaende ohne
    Volumenkontrolle. Das Skyrme-Projekt ist zweimal an Rand- bzw. Aufloesungseffekten gescheitert.
  - **Eine netzspezifische, falsifizierbare Vorhersage fehlt.**
  - **Agentisches Muster:** Praezise loesbare Nebenaufgaben, etwa die Higgs-Portal-Reduktion (nicht auf V), haben die
    Leitfragen ueberholt.
  - **Reproduzierbarkeit fehlt:** keine Umgebung, keine Daten, Rechnernamen im Code.
  - **Mehrere Auswerteentscheidungen fielen nach Sicht.** Das ist transparent benannt, schwaecht aber.
- **Korrekturen bzw. Praezisierungen an den Reviews:**
  - **Review 1 nennt Eichinvarianz als Risiko der Maxwell-Gewichte.** Das trifft nicht zu, siehe 2. Betroffen sind
    Positivitaet und Reflexionspositivitaet.
  - **Review 1, "Verhaeltnis 0,43 bei anderer Referenzskala":** Das ist der S5-Befund mit c = 0,1125. Dort ist
    Wurzel(t0) kleiner als eine Netzkante, also ein Gitterartefakt. Es ist kein Widerspruch zur Uebereinstimmung bei
    c = 0,3, zeigt aber, dass diese Uebereinstimmung skalenabhaengig ist. Beides gehoert nebeneinander ins Register.
  - **Review 2 schreibt, ein Kontinuumslimes sei "nirgends genommen".** Bei SU(2) gibt es zwei Abstaende mit einer
    beschreibenden Extrapolation (S6). Das ist kein Limes, aber mehr als nichts.
- **Prozentspalte:**
  - Review 2 haelt die Werte fuer zu hoch. Ich halte vor allem "Netz und Raum 65 %" und "Schwerkraft 55 %" fuer
    optimistisch: Der leichte Teil (lineares Fernfeld) dominiert die Einschaetzung, das Schwere (Nahfeld, Kollaps,
    Nichtlinearitaet, Kontinuumslimes) ist offen.
  - Die Spalte bleibt auf Finns Wunsch. Mein Vorschlag fuer eine kritischere Kalibrierung ist eine Rueckfrage an Finn
    und Codex, keine Aenderung durch mich: Netz und Raum 45 bis 50, Schwerkraft 40 bis 45.

## 2. Maxwell-Befund (Schwerpunkt der Anfrage)

### 2.1 Was gerechnet ist [E] (QUANT-2, LICHT-SEKTOR-NOTIZ, REGULAER-V-1, HOEHE-ISOTROP-1)

- **Umkreismittige Sterne:**
  - In 3D ist das ungewichtete Netz V nicht Delaunay: *2 < 0 an 12 von 116 Flaechen.
  - Mit Potenz-Gewichten (Eckgewichte je Untergitter) gibt es dort eine Kammer, in der alle Sterne positiv sind.
- **4D-Zeltnetz (V mal Zeit):**
  - Umkreismittige Sterne sind fuer 15 bis 40 % der 484 Dreiecksklassen negativ. Die quadratische Maxwell-Form hat dann
    fuer jede gepruefte Zeltstangenhoehe tau (0,1 bis 1) an allen gepruften q negative Moden.
  - Mit gesuchten Potenz-Gewichten (9 Werte omega_b) und tau = 0,348 ist der kleinste Bloch-Eigenwert an 96 neuen
    q-Punkten positiv (+2,3e-3 relativ). 3 von 484 Klassen bleiben leicht negativ (w >= -0,0089 bei w_max 1,68).
  - Gefunden per Nelder-Mead, Ziel war der groesste kleinste Eigenwert an 16 q. Zwei Starts landeten fast gleich.
- **Weiter gerechnet:**
  - Die Normierungsidentitaet Summe_f w_f S_f S_f^T = Vol I_6 gilt exakt (1,7e-15) fuer jede gepruefte Gewichtswahl.
    Damit bedeutet beta = 1/e^2 dasselbe wie auf dem Hyperkubus.
  - Photon bei beta = 2: E/|k| = 1,01 +- 0,04, richtungsgleich auf ~5 %. Das gilt nur in einem kleinen Kasten.

### 2.2 Eichinvarianz, Positivitaet, Reflexionspositivitaet: was betroffen ist

- **Eichinvarianz [M]: nicht betroffen.**
  - Die Wilson-Wirkung S = Summe_f beta w_f (1 - cos theta_f) haengt nur von den Plakettenwinkeln theta_f ab. Diese
    sind fuer jede Gewichtswahl eichinvariant, auch bei negativen w_f.
  - Fuer SU(2) gilt dasselbe mit Re Tr U_f.
  - Die Gewichte koennen Eichinvarianz weder herstellen noch brechen.
- **Positivitaet (Stabilitaet des schwachen Felds) [M, E]: betroffen.**
  - Gemeint ist: Die quadratische Form Summe_f w_f theta_f^2 ist auf dem eichfreien Unterraum positiv definit (bzw.
    semidefinit mit genau den Eichnullmoden).
  - Lokal negative w_f schliessen das nicht aus. Entscheidend ist der kleinste Bloch-Eigenwert ueber die ganze
    Brillouin-Zone.
  - Umkreismittig ist die Form indefinit, also ist der Maxwell-Grenzfall ungueltig. Mit den gesuchten Gewichten ist sie
    an den gepruften q positiv, aber nicht bewiesen.
  - Die kompakte Wirkung bleibt wegen der Beschraenktheit von (1 - cos) zwar definiert. Negative Gewichte machen sie
    aber frustriert und koennen Scheinphasen erzeugen.
- **Reflexionspositivitaet (Osterwalder-Schrader) [M, L]: nicht geprueft.**
  - Sie ist die Bedingung fuer einen positiven Transfer-Operator, also eine unitaere Quantentheorie mit Hamiltonoperator.
  - Bei einer Spiegelung an einer Zeitschicht duerfen Terme, die ganz auf einer Seite liegen, beliebiges Vorzeichen
    haben (sie erscheinen als F + Theta F).
  - Die Terme, die die Spiegelebene kreuzen, muessen von der Form Summe c_i A_i Theta(A_i) mit c_i >= 0 sein. Beim
    Wilson-Gitter heisst das in erster Linie: positive Gewichte auf den zeitartigen, kreuzenden Plaketten [L].
  - **Ob die 3 negativen Klassen raeumlich (Scheibendreiecke) oder zeitartig sind, ist in QUANT-2 nicht festgehalten.**
    Sind sie zeitartig und kreuzend, ist Reflexionspositivitaet verletzt. Sind sie raeumlich, kann sie gelten.
  - Zusaetzlich muss die Zeltgeometrie (Hubfolge, Eckhoehen b/10 mal tau) eine echte Spiegelsymmetrie haben. Das ist
    bei der Zeltstangen-Treppe nicht selbstverstaendlich.

### 2.3 Was die gesuchten Gewichte belegen, und was nicht

- **Belegt [E]:**
  - Es gibt fuer dieses Netz und tau = 0,348 eine Wahl von Potenz-Gewichten, unter der die Maxwell-Form an allen 112
    gepruften q positiv ist.
  - Dabei bleibt die Maxwell-Normierung exakt.
  - In der Coulomb-Phase ist das Photon dann bei einem Kopplungswert masselos und richtungsgleich.
- **Nicht belegt:**
  - Positivitaet in der ganzen Brillouin-Zone. Ein dichtes Gitter oder eine analytische Schranke fehlt.
  - Eindeutigkeit bzw. eine natuerliche Auswahlregel. Die Gewichte stammen aus einer Optimierung, nicht aus einem
    Prinzip.
  - Groesse und Form des zulaessigen Gebiets in (tau, omega).
  - Unabhaengigkeit der Physik (beta_c, Photontempo) von der Wahl innerhalb dieses Gebiets.
  - Reflexionspositivitaet.
  - Ein Kontinuumslimes.
- **Lesart [H]:** Das Netz ist im strengen Sinn kein guter "natuerlicher" DEC-Traeger. Es braucht eine eingestellte
  Gewichtung (Potenz-Diagramm) und eine eingestellte Zeitschrittweite. Das ist ein echter, netzspezifischer Befund.
  Er spricht eher gegen als fuer V als fundamentale Struktur, solange keine Auswahlregel gefunden ist.

### 2.4 Die fehlende P0-Pruefung (konkret, ohne neue GPU-Laeufe planbar)

1. **Klassifikation (Schreibtisch und kleine CPU-Auswertung):** Die 3 negativen Klassen der gespeicherten Gewichte
   (gwp.npz/gwp.json) als raeumlich, zeitartig bzw. kreuzend einordnen und die Lage relativ zu einer
   Zeitschicht-Spiegelung bestimmen.
2. **Positivitaet in der ganzen Zone:**
   - kleinster Eigenwert der Bloch-Form auf einem dichten q-Gitter (z. B. 24^3), mit Fehlerschranke zwischen den
     Gitterpunkten (Lipschitz- bzw. Stoerungsschranke)
   - Ausweisung der Eichnullmoden
3. **Reflexionspositivitaet:** Spiegelsymmetrie des Zeltnetzes bezueglich einer Zeitschicht pruefen, dann die
   Vorzeichen der kreuzenden Terme. Fehlt die Symmetrie, ist sie zu benennen.
4. **Zulaessiges Gebiet und Robustheit:**
   - Abtastung von (tau, omega) um die gefundene Loesung
   - Breite des positiven Gebiets
   - beta_c und Photontempo an drei Punkten darin (Universalitaet gegen Gewichtswahl)
   - Das braucht kleine Laeufe und ist mit Codex abzustimmen.
5. **Auswahlregel suchen:** Gibt es ein geometrisches Prinzip (gewichtete Delaunay- bzw. Potenz-Bedingung, die der
   Zeltgeometrie selbst folgt), das die omega festlegt, statt sie zu optimieren?

Punkt 1 bis 3 sind Schreibtisch- bzw. CPU-Kleinarbeit. Punkt 4 braucht Laeufe. Das reproduzierbare V-Maxwell-Paket
von Codex sollte Punkt 1 und 2 als Tests enthalten.

## 3. Grenzen und naechste Pruefungen (Reihenfolge)

- **P0:**
  - Maxwell-Pruefung wie 2.4.
  - Ein zentrales Ergebnis unabhaengig reproduzieren, mit Umgebung und Skript. Codex baut das V-Maxwell-Paket.
  - Volumen- und Gitterabstandsreihe fuer genau einen Befund (Kandidat SU(2)-Flow: L-Reihe bei beiden Abstaenden).
- **P1:**
  - Eine netzspezifische Vorhersage: Dispersion bzw. Anisotropie des Photons bei hohem k gegen den Hyperkubus und gegen
    eine zufaellige Delaunay-Triangulierung. Was ist an V anders als an einem gewoehnlichen Gitter?
  - Mehrere Geometrien vergleichen.
- **Zurueckstellen:** neue Teilchenmechanismen, Skyrme Fassung 5 und weitere Higgs-Reduktionen, bis P0 steht. So
  empfehlen es beide Reviews, und ich stimme zu.
- **Grenzen dieser Bewertung:**
  - nichts neu gerechnet
  - Reflexionspositivitaet und Lagenklassifikation nur als Pruefplan
  - Literaturaussagen [L] aus dem Gedaechtnis
