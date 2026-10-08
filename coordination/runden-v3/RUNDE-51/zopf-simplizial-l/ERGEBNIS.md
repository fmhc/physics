# ZOPF-SIMPLIZIAL-L: Ergebnis (bereinigte Kurzfassung)

- Frage der [Karte](../modell-screening-1/karten/ZOPF-SIMPLIZIAL-L.md): Kann der gerahmte Graph der Zopf-Preonmodelle
  (Bilson-Thompson, Markopoulou, Smolin, Wan, Hackett) im Zustandsraum von Netz V auftreten?
- Literatur- und Schreibtischpruefung vom 07./08.10.2026 durch einen Claude-Rechercheagenten (Sonnet 5.5) fuer die
  Leitung. Kurzfassung des Dossiers aus dem Arbeitsprojekt; das volle Dossier enthaelt Arbeitsnotizen und lokale
  Quellverweise und ist nicht exportiert.
- Kennzeichen: [S] an der Primaerquelle gelesen (Seitenangabe), [M] eigene Handableitung (kein Maschinenbeweis, nicht von
  zweiter Hand gegengelesen), [H] Hypothese. Keine Rechnung, keine Energie- oder Dynamikaussage, keine Messdaten.

## Ergebnis

1. **Ausschluss im Standardrahmen [M].** In einem strikten Simplizialkomplex ist ein Simplex durch seine Eckenmenge
   bestimmt; zwei verschiedene Tetraeder teilen daher hoechstens ein Dreieck. Der Dualgraph von V ist ein einfacher
   4-regulaerer Graph ohne Mehrfachkanten. Der vierwertige Zopf (Wan 2007, Def. 1: zwei Knoten mit drei gemeinsamen
   Kanten und je einer Aussenkante) kommt deshalb in keinem Zustand von V vor, weder unverzopft noch verzopft. Das gilt
   unter den Annahmen: V ist strikt simplizial (aus dem Projekt uebernommen, fuer die Anfangszelle nicht eigens
   nachgeprueft), Dual = Knoten je Tetraeder und Kante je Dreieck, Umklappen mit Simplizialitaetspruefung.
2. **Die Autoren sagen dasselbe [S].** Smolin/Wan 2007 (arXiv:0710.1548, S. 11 und S. 17) und Bilson-Thompson/Hackett/
   Kauffman/Wan 2012 (arXiv:1109.0080, S. 18-19): Ein Knotenpaar mit drei gemeinsamen Kanten entsteht nicht als Dual
   einer regulaeren simplizialen Triangulierung; die Stabilitaet des Zopfes unter Einzelzuegen beruht gerade darauf.
3. **Erweiterter Zustandsraum [M].** Laesst man Mehrfachverklebung zu (Pseudokomplex), entsteht als kleinstes Beispiel
   das "Kissen" aus zwei Tetraedern mit drei gemeinsamen Flaechen (Burton 2013, arXiv:1208.2504, Def. 2.2). Es
   realisiert nur den trivialen Zopf (0 Kreuzungen, 0 Verdrillungen) und ist durch einen Zug wieder aufloesbar.
   Nichttriviale Zopfklassen sind Einbettungs- und Rahmungsdaten, die V nicht besitzt.
4. **Unterschied der Zugregeln [M].** Die Zuege der Quellen pruefen keine Ecken: 1->4 gefolgt von 3->2 auf drei der vier
   neuen Tetraeder erzeugt aus einem strikten Zustand das Kissen. Das Umklappen auf V mit Simplizialitaetspruefung
   verbietet genau diesen Zug.
5. **Recherchestand.** Drei Suchen im Fenster Okt. 2024 bis Okt. 2026 fanden keine Arbeit zur simplizialen
   Darstellbarkeit vierwertiger Zopfnetze. Das heisst "nach Recherchestand nicht belegt", nicht "es gibt nichts".

## Bedeutung und Grenzen

- Negativbefund fuer diese Kopplung: Aus den Zopfmodellen folgt fuer V keine Ladungs- oder Chiralitaetszaehlung.
  Das widerlegt die Zopfmodelle nicht; es zeigt nur, dass sie nicht als Teilgraph des Duals in dieses Netz passen.
- Eine nichttriviale Zopfklasse waere nur als neues Modell moeglich, etwa als zusaetzliche "dekorierte Roehren" in V
  mit eigenen Zugregeln [H]. Nicht ausgearbeitet.
- Offen: Strikt-Pruefung der Anfangszelle von V; ob die Quellen die Zugfolge 1->4, 3->2 selbst als zulaessig ansehen;
  Klassifikation inkompatibler Verklebungen; das dreiwertige Beispiel in hep-th/0603022, Abb. 15.
- Die Handbeweise sind einmal rueckwaerts gegengelesen, aber nicht unabhaengig geprueft.

## Quellen

1. Bilson-Thompson 2005, hep-ph/0503213. https://arxiv.org/abs/hep-ph/0503213
2. Bilson-Thompson, Markopoulou, Smolin 2007, Class. Quantum Grav. 24, 3975; hep-th/0603022. https://arxiv.org/abs/hep-th/0603022
3. Wan 2007, arXiv:0710.1312. https://arxiv.org/abs/0710.1312
4. Smolin, Wan 2008, Nucl. Phys. B 796, 331; arXiv:0710.1548. https://arxiv.org/abs/0710.1548
5. Hackett, Wan 2008, arXiv:0803.3203. https://arxiv.org/abs/0803.3203
6. Bilson-Thompson, Hackett, Kauffman, Wan 2012, SIGMA 8, 014; arXiv:1109.0080. https://arxiv.org/abs/1109.0080
7. Burton 2013, arXiv:1208.2504. https://arxiv.org/abs/1208.2504
