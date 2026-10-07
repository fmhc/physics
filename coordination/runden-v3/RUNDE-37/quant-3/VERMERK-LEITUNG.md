# QUANT-3: Vermerk der Leitung zum Bericht von Gemini (06.10.2026)

- Geprueft auf der .69 (m1.json): Der Lauf m1 (Netz L = 4, Nt = 8) hat beta von 1,0 bis 6,0 aufwaerts und abwaerts
  gescannt, mit heissen und kalten Starts und 200 Messungen je Punkt. Die Aussage von S2 zum Bereich 1 bis 6 ist damit
  belegt, allerdings nur mit wenig Statistik.
- **Berichtigungen zum Wortlaut von ERGEBNIS.md:**
  - Kleines beta heisst starke Kopplung (beta = 4/g^2). Eingesperrt wird bei kleinem beta, also starker Kopplung;
    frei werden die Ladungen bei festem Nt oberhalb von beta_c, also bei schwaecherer Kopplung bzw. hoeherer
    Temperatur. Im Bericht ist "schwach" und "stark" vertauscht.
  - "neu" ist zu stark. Dass SU(2) mit Wilson-Wirkung keinen Volumenuebergang hat, ist auf dem Hyperkubus Literatur.
    Neu ist nur der Befund auf Finns Netz, und auch der nur bei L = 4 mit 200 Messungen je Punkt.
  - "physiklos aufplatzender Volumenuebergang" und "Riss in der Raumzeit" streichen. Der U(1)-Uebergang ist ein
    bekannter Phasenuebergang, kein Riss.
  - Die L = 6-Laeufe sind nicht ganz gescheitert. Die Graph-Erfassung lief ins Speicherlimit (OOM), danach rechneten sie
    ohne Graph weiter: b2-n6t6.json hat 470 Messungen, nur heisse Starts. Sie sind nicht ausgewertet.
- Zum Abbruch: Die Laeufe a3 (n6t8) und b3 (n4t8) liefen noch, als der Agent fertig war (Start 17:00 UTC). Sie sind
  nicht ausgewertet.
