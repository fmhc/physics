# QCA-BCC-RUECK-1: Gibt es tetraedersymmetrische Quanten-Spielregeln auf BCC, die in beide Richtungen springen? (Runde 38/39)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 09:23:48 CEST (date), vor jeder Rechnung.
- **Anlass:** Gegenleser der QCA-Beweise (RUNDE-37/qca-gegenlesen/GEGENLESEN.md), Befund A4.
  - Alle 165 BCC-Loesungen aus QCA-DIAMANT-4 unter der vollen Gruppe T springen nur in eine Richtungsgruppe (S+ oder S-).
  - D'Ariano/Perinotti verlangen in ihrer Definition, dass jeder Sprung auch rueckwaerts moeglich ist (Abschn. II).
  - Die isotropen Weyl-Kegel mit v = 1/3 sind also keine Automaten im Sinn der Quelle. "BCC als Fermionen-Netz mit voller
    Tetraeder-Symmetrie" ist offen.
  - Literatur: D'Ariano/Erba/Perinotti, PRA 96, 062101 (2017), Einteilung laut Abstract "completely general". Zuerst
    lesen; vielleicht beantwortet sie die Frage schon.
- Kennzeichen: [M] Mathematik, [L] Literatur, [S] an der Quelle gelesen, [H] Hypothese.

## Vorgehen (Code-Agent)

- **Literatur zuerst** (hoechstens 3 gezielte Abrufe; Fundstellen nur aus selbst gelesenem Text):
  - D'Ariano/Erba/Perinotti 2017: Was sagt ihre Einteilung ueber BCC, Dimension 2 und 4, Isotropiegruppen (L_2 bzw. T)
    und Rueckspruenge?
  - Steht die Antwort dort, ist das Ergebnis "vorab ableitbar". Gerechnet wird nur der Rest.
- **Schreibtisch:** Rueckspruung-Bedingung (A_gg' != 0 => A_g'g != 0) mit T-Kovarianz und Unitaritaet verbinden; was
  folgt ohne Rechnung?
- **Suche:**
  - BCC, Zustaende 4 und 8, Darstellungen von 2T wie in QCA-DIAMANT-4 und QCA-DIRAC-T-1.
  - Zusatzbedingung: Jede besetzte Sprungrichtung hat ihre Gegenrichtung besetzt, mit einer Mindestnorm (vor dem
    Einfrieren festlegen).
  - Treffer einordnen: Kegel, Isotropie, 360 Grad, Masse, Verdoppler.
- **Kontrolle:** Der L_2-Weyl-Automat der Quelle (Rueckspruenge erfuellt) wird gefunden.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QR0 | Kontrolle: Die Suche findet unter L_2 mit 2 Zustaenden den Weyl-Automaten der Quelle (mit Rueckspruengen) | 90 % |
| QR1 | [H] Mit 4 Zustaenden gibt es unter T keinen nichttrivialen Automaten mit Rueckspruengen und Kegel | 55 % |
| QR2 | [H] Mit 8 Zustaenden gibt es unter T einen nichttrivialen Automaten mit Rueckspruengen und isotropem Kegel, mit 360 Grad = -1 | 35 % |

**Bedeutung (vorab):**
- **QR1 und QR2 treffen ein:** Fuer die volle Tetraeder-Symmetrie mit Rueckspruengen braucht ein Fermion 8 innere
  Zustaende.
- **QR1 und QR2 verfehlt (keine Treffer):** Die volle Tetraeder-Symmetrie und die Regeln der Quelle vertragen sich auf BCC
  nicht. Dann bleibt L_2 die richtige Symmetrie fuer Fermionen auf dem Tetraeder-Netz.
- **QR1 verfehlt durch einen Treffer:** Die Aussage aus QCA-DIAMANT-4 laesst sich mit Rueckspruengen retten.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und p4000b; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
