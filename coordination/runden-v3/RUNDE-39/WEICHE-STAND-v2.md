# Stand zu Finns Weiche, Fassung 2 (fortgeschrieben ab 2026-10-04 09:42:59 CEST; Fassung 1 ist mit dem Journal zu Runde 38 eingefroren)

- Leitung claude-primary, geschrieben ab 2026-10-04 07:41:45 CEST (date).
- Alles synthetische Modellrechnungen [G] bzw. Literatur [L]; keine Messdaten.
- **Die Weiche (RUNDE-37/RAUMZEIT-NETZ.md, Seite "Die ½-Regel"):**
  - (A) Netz mit festen Nachbarn (Kristall oder fester Schaum), dafuer ein verstecktes Ruhesystem
  - (B) Ereignis-Netz ohne Ruhesystem (Kausalmenge), dafuer nicht lokal
  - (C) ein Netz, das selbst schwankt (Summe ueber Netze, wie CDT bzw. dynamische Triangulierung)

## Befunde

| Frage | (A) feste Nachbarn | (B) Ereignis-Netz | (C) schwankendes Netz |
|---|---|---|---|
| Lange Schwerewellen mit c, zwei Polarisationen | ja, mit eingebauter Regge-Wirkung, auch schief verzogen (REGGE-WELLE-1, REGGE-WELLE-SCHIEF-1) | nicht gerechnet | nicht gerechnet |
| Kurze Wellen | Wuerfelgitter-Formel; schief: Doppelbrechung, teils > c, Zusatzwelle, stellenweise instabil | Rauschen statt Vorzugsrichtung | - |
| Schwerkraft aus Materie (Sakharov) | nein: Gitterterme bis k^2, Kristall (INDUZIERT-1) wie fester Zufall (INDUZIERT-ZUFALL-2D, nur richtungsfrei) | 2D: "Zahl = Volumen" gibt eine negative konforme Steifigkeit von Polyakov-Groesse (Steigung ueber das k-Fenster bei Netzabstand 1: -0,0123 +- 0,0012 statistisch; fuer k -> 0 nach Gegenprobe 1,075 P +- 0,071 P im k^4-Modell, robust 0,7 bis 1,2 P; 2D euklidisch, gequenchtes Mittel, nur konforme Mode; Gegenleser: traegt mit Einschraenkung; INDUZIERT-DICHTE-2D-GROB) [H fuer "Schwerkraft aus Materie moeglich"]; 4D: Volumen-Zaehlung allein gibt nicht Einsteins Vorzeichen (+0,111 +- 0,045 bei Dichte 1; INDUZIERT-DICHTE-4D) | Literatur: 2D-dynamische Triangulierung mit Materie gibt Liouville [L]; CDT: lambda_eff < 1/2 in 2+1 (CDT-HORAVA-L) |
| Raum-Netz mit aeusserer Uhr | c = 1/5 statt 1/2 (REGEL.md Abschn. 8) | - | - |
| Wellen | ja | 1+1: im Mittel wie Kontinuum, stabil (KAUSAL-WELLE-1). 3+1: Johnstons Mittel waechst fuer massive Felder an (KAUSAL-WELLE-4D, Ursache Massenkopplung); eine Sprungregel ueber 1-Element-Intervalle bremst es im Mittel um eine Ordnung in m^2/sqrt(rho), nicht abgestellt; Bedingung l nahe l_P und exakt sigma = 0 (KAUSAL-4D-SCHICHT-1, Gegenleser: traegt mit Einschraenkung) | - |
| Fermionen | Unter halben Drehungen transformieren die zwei Zustaende der einfachsten Quantenregel auf BCC wie Spin 1/2 (QCA-TETRA-1; Literatur D Ariano/Erba/Perinotti 2017); Ladung + Monopol gibt Dublett (LADUNG-MONOPOL-1); Diamant laeuft | 1+1-Fermion im Mittel richtig, mit Zitterbewegung (SCHACHBRETT-KAUSAL-1); Spin in 3+1 offen | - |
| Teilchen als Punkte | - | zittern um 1/4 Rapiditaet je Schritt, heizen (KAUSAL-SWERVE-1) | - |

## Vorlaeufige Lesart der Leitung [H]

- Ein starres Netz eignet sich fuer eingebaute Schwerkraft, aber nicht fuer Schwerkraft aus Materie. Die
  Vorzugsrichtungen bzw. die mitwandernde Abschneidelaenge schlagen bis zu langen Wellen durch.
- Das Ereignis-Netz haelt bisher jedem Test stand, wenn Teilchen als Wellen bzw. Pfadsummen laufen und nicht als Punkte.
  Offen sind Spin in 3+1, die Dynamik, und ob "Zahl = Volumen" die Schwerkraft aus Materie rettet.
- Spannung: Unsere Spin-1/2-Befunde liegen alle auf festen Netzen. Auf dem Ereignis-Netz gibt es bisher nur die
  Chiralitaet in 1+1.
- **Entscheidend fuer Finns Wahl sind die zwei laufenden Tests:**
  - INDUZIERT-DICHTE-2D: Rettet "Zahl = Volumen" die Schwerkraft aus Materie?
  - KAUSAL-WELLE-4D: Traegt das Ereignis-Netz auch in 3+1?

## Nachtraege in Fassung 2

- Spin 1/2 auf der Lorentz-Kausalmenge braucht Zusatzstruktur (Rahmen je Punkt). Ein Satz von Bombelli u. a. verbietet,
  ihn aus der Streuung zu gewinnen (SPIN-KAUSAL-L) [S/L].
  - Euklidisch bzw. raeumlich ist eingesetzter Spin moeglich; SPIN-ZUFALLSNETZ-1 laeuft.
- Gegenleser QCA: Die BCC-Loesungen unter T springen nur in eine Richtungsgruppe. Moegliche Lesart: ein Schachbrett mit
  vier Lichtrichtungen (Foster/Jacobson 2016) [H]. QCA-BCC-RUECK-1 prueft Rueckspruenge.
- Nachtrag 2026-10-04 10:26:59 CEST, berichtigt nach QCA-GEGENLESEN-2, QCA-BCC-RUECK-1 [G; Teilbeweis gegengelesen:
  richtig, deckt nur einen Sonderfall]: Mit voller Tetraeder-Symmetrie und Rueckspruengen fand die Suche auf BCC mit 4
  Zustaenden keinen Automaten; mit 8 Zustaenden gibt es welche: vier masselose Weyl-Kegel, in erster Ordnung isotrop,
  360 Grad = -1 (Darstellung gewaehlt), Kegel auch an H, P und P'. Das meiste davon war vorab aus der Symmetrie
  ableitbar. Eine Bauart: Vorwaertsteil + Rueckwaertsteil + Muenze; die gefundenen Automaten sind teils allgemeiner.
  Masse mit Rueckspruengen zeigt schon QCA-DIRAC-T-1 (mit Inversion): Konstruktionen (a), (b) und 16 massive Treffer
  springen in beide Richtungsgruppen gleich stark und sind unzerlegbar; drei davon sind isotrop und haben an H, P und
  P' keine Kegel. Offen ist Masse ohne Inversion; 6 Zustaende sind nicht untersucht.
- Nachtrag 2026-10-04 10:36:53 CEST, SPIN-ZUFALLSNETZ-1 [G]: Ein eingesetzter Weyl-Spinor auf einem 3D-Zufallsnetz laeuft langwellig als ein
  einziger scharfer Kegel (v = 0,975 bis 1,008, Helizitaet zu 99 %). Die Doppler verschwinden als Kegel, kehren aber als
  flaches Band rauer Zustaende bei allen Energien zurueck (rho(0) = 0,463 je Knoten und Energieeinheit). Ob das Band bei Kopplung stoert,
  ist offen; INDUZIERT-DIRAC-2D zaehlt die Doppler in 2D ueber die Anomaliezahl.
- Nachtrag 2026-10-04 10:40:26 CEST, INDUZIERT-G-L [S/ES]: Bei freien Feldern setzt der Regler das Vorzeichen der induzierten
  Newton-Konstante; universell ist nur der Log-Teil (in 2D die Anomalie, die wir treffen). Unser 4D-Vorzeichen widerspricht
  also keinem Satz; ob es am Regler oder an der Torus-Konstruktion liegt, ist offen. Ein festes positives Vorzeichen geben laut
  Literatur Eigenzeit-artige Regler, Kompensationsfelder oder UV-endliche, wechselwirkende Materie (QCD: positiv). Die Leitungs-
  Hypothese xi_eff > 1/6 haelt langwellig nicht (K 1 = 0). INDUZIERT-KUGEL-1 prueft das Vorzeichen auf S^4.
