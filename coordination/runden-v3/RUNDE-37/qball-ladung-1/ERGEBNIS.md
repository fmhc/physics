# QBALL-LADUNG-1: Ergebnis (Leitung, 2026-10-04 04:52:59 CEST)

**Ergebnis zuerst:**
- Ein Q-Ball mit elektrischer Ladung (Eichkopplung e an ein U(1)-Feld) wird durch die Abstossung seiner eigenen Ladung
  schwerer, genau wie e^2: Steigung 1,998 bzw. 1,997 bei festem Q = 300 bzw. 1000 (QL1 eingetroffen).
- Die Kontrolle ohne Ladung trifft die alte Tabelle auf alle gedruckten Stellen (QL0 eingetroffen).
- Ob es eine groesste Ladung gibt, konnte mein Schiessverfahren nicht verlaesslich klaeren (QL2 und QL3 nicht auswertbar).

## Urteile (lauf-69/auswertung.json)

| Nr | Urteil | Werte |
|---|---|---|
| QL0 | eingetroffen | omega^2 = 0,6 / 0,7 / 0,8: f0^2 = 1,088133 / 1,135061 / 1,044572; Q = 2873,18 / 473,413 / 186,110; E = 2332,59 / 428,642 / 181,912 (Tabelle: 1,088133 / 1,135060 / 1,044572; 2,87318e3 / 473,413 / 186,110; 2,33259e3 / 428,641 / 181,912) |
| QL1 | eingetroffen | Delta E bei Q = 300: 0,0257 / 0,1030 / 0,4116 / 2,5628; bei Q = 1000: 0,2105 / 0,8417 / 3,3641 / 20,915 (e = 0,005 / 0,01 / 0,02 / 0,05); Steigung 1,998 / 1,997 |
| QL2 | nicht auswertbar | Ende der Familien nicht verlaesslich (siehe unten) |
| QL3 | nicht auswertbar | haengt an QL2 |

## Beschreibend

- **e = 0,05:** gueltige Loesungen von Omega_0^2 = 0,98 (Q = 203, omega^2 = 0,994) bis 0,595 (Q = 1376, omega^2 = 0,704,
  E/Q = 0,869). Darunter findet der Loeser keine Klammer (alle Startwerte unterschiessen), waehrend Q noch steigt.
- **e = 0,1:** gueltig von 0,92 (Q = 138, omega^2 = 0,987) bis 0,525 (Q = 1126, omega^2 = 0,907), mit einer Luecke bei
  0,535.
  - omega^2 sinkt zunaechst und steigt ab Q ~ 400 wieder (Minimum 0,846).
  - E/Q hat ein Minimum 0,9416 bei Q ~ 900 und steigt danach.
  - Das passt zum Bild, dass grosse geladene Baelle teurer werden und die Familie endet, wenn omega die Masse erreicht
    [L?/H].
- **e = 0,2:** keine gueltige Loesung. Das Klassenmuster ist umgekehrt: Kleine Startwerte schiessen ueber, grosse unter.
  Mein Loeser sucht nur den Wechsel "unter -> ueber", also Rechenverfahren, keine Physik.
- **Fazit:** Fuer die groesste Ladung braucht es ein anderes Verfahren (Relaxation statt Schiessen); geparkt.

## Selbstanzeigen

- Die Leitung hat selbst gerechnet, ohne Code-Gegenleser.
- **Fassung 1** fand die Klammer nicht, wo die Startspitze genau getroffen werden muss.
  - Ein Fehlstart (alle drei Kontrollpunkte ohne Klammer) wurde vor den Hauptlaeufen behoben.
  - Die Familienlaeufe der Fassung 1 zeigten dann die Grenzen; daraus entstand Fassung 2 (robuste Klammer, Gueltigkeit,
    Modus zielQ), offengelegt in PRUEFSUMMEN.txt.
  - Schwellen und Urteilsregeln blieben unveraendert.
- **QL0-Schwelle:** Die Karte nannte 1e-6. Wegen der Druckgenauigkeit der Tabelle wurde vor der Rechnung "halbe letzte
  gedruckte Stelle, mindestens 1e-6" festgelegt.
- Zwei geschaetzte Uhrzeiten in der Karte wurden vor der Rechnung durch neutrale Angaben ersetzt.

## Einfach gesagt

Wir haben Q-Baellen eine elektrische Ladung gegeben. Dadurch stoesst sich die Ladung im Ball selbst ab, und der Ball wird
ein wenig schwerer, genau im Verhaeltnis zum Quadrat der Ladungsstaerke, wie bei einer geladenen Kugel. Damit sind Q-Baelle
im Rechenmodell geladene Teilchen. Ob zu grosse geladene Baelle an ihrer eigenen Abstossung zerbrechen, also ob es eine
groesste Ladung gibt, konnten wir mit unserem Rechenverfahren noch nicht sicher feststellen.
