# QUANT-3: Sperrt ein SU(2)-Eichfeld auf Finns 4D-Netz Ladungen ein, ohne Phasensprung zwischen starker und schwacher Kopplung? (Runde 50, Ziel Schritte c und d, schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-05 19:23:00 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - QUANT-2: Kompaktes U(1) auf dem 4D-Zeltnetz (V mal Zeit) braucht Eckgewichte (Potenz-Dual) und tau = 0,348.
    Ergebnisse: beta_c = 1,45, ein masseloses, richtungsgleiches Photon in der Coulomb-Phase, Einschluss nur bei starker
    Kopplung. Diese Phase hat in 4D keinen Kontinuumslimes [L]. Mesonen und Baryonen (Faeden mit zwei bzw. drei
    Enden) brauchen deshalb einen nichtabelschen Sektor.
  - GLUONEN-L: Finns Netz hat die Form einer Gittereichtheorie; Gluonen brauchen SU(3) je Ecke. K1 ZWEI-T-AUSFRIER-1
    (2T gegen SU(2) auf Diamant mal Zeit) ist geparkt, weil Finns Netz T hat, nicht 2T.
  - Projektsuche der Leitung (19:20, mit Sperrausschluessen; SU(2) mit Monte/Waermebad/Wilson/Kennedy/Creutz,
    nichtabelsch, QUANT-3): Im Projekt gibt es keine nichtabelsche Gitterrechnung, nur Literaturordner (GLUONEN-L,
    GLUON-PAAR-L, Athenodorou/Teper).
- **Ableitbarkeit:**
  - [L] Bei starker Kopplung gilt auf jedem Gitter ein Flaechengesetz (Wilson 1974). Einschluss bei kleinem beta ist
    deshalb vorab sicher.
  - [L] Auf dem Hyperkubus hat SU(2) mit Wilson-Wirkung keinen Volumenuebergang. Der Deconfinement-Uebergang bei
    Nt = 4 liegt bei beta = 2,2986. T_c/Wurzel(sigma) = 0,709 im Kontinuum (Lucini/Teper/Wenger 2004).
  - Nicht ableitbar: ob Finns gewichtetes Zeltnetz einen Volumenuebergang hat (U(1) hatte einen), wo der
    Deconfinement-Uebergang liegt und wie gross die Gitterfehler in T_c/Wurzel(sigma) sind.
- **Keine Neuheit der Architektur:** Eichtheorie auf unregelmaessigen Gittern ist Literatur (u. a. Christ/Friedberg/Lee
  1982 [L]). Neu waere nur die Zahl auf Finns Netz.

## Modell

- Wilson-Wirkung S = beta Summe_f w_f (1 - Re Tr U_f / 2) ueber die Dreiecke des 4D-Zeltnetzes.
- Gewichte w_f und tau = 0,348 wie QUANT-2 (Potenz-Dual, gwp.npz). Dieselbe Maxwell-Identitaet gibt beta = 4/g^2 wie
  auf dem Hyperkubus.
- Algorithmus: SU(2)-Waermebad (Kennedy-Pendleton oder Creutz) und Ueberrelaxation, Faerbung wie in QUANT-2, auf der
  GPU (torch).
- Kontrolle: Hyperkubus L^4 bzw. L^3 x Nt mit w = 1.

## Messgroessen

- M1: Plakette <P>(beta) heiss aufwaerts und kalt abwaerts. Ein Sprung oder eine Hysterese zeigt einen
  Volumenuebergang.
- M2: Polyakov-Schleife |L| und ihre Suszeptibilitaet bei festem Nt gegen beta. Das gibt den
  Deconfinement-Uebergang beta_c(Nt).
- M3: Wo moeglich, sigma aus Polyakov-Korrelatoren mit Multihit bei tiefer Temperatur. Daraus der dimensionslose
  Quotient T_c/Wurzel(sigma), mit T_c = 1/(Nt tau a) beim beta_c(Nt).

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| S1 | Kontrolle: Hyperkubus mit Nt = 4, Maximum der Polyakov-Suszeptibilitaet bei beta = 2,30 +- 0,04 | 80 % |
| S2 | Finns Netz: kein Volumenuebergang. Die Plakette steigt fuer beta = 1 bis 5 ohne Sprung; heiss und kalt stimmen innerhalb von 3 Fehlern | 60 % |
| S3 | Finns Netz: Bei festem Nt (4 bis 8 Zeitschichten) springt die Polyakov-Schleife innerhalb von beta = 1 bis 6 von nahe 0 auf einen endlichen Wert | 65 % |
| S4 | Wo sigma messbar ist: T_c/Wurzel(sigma) auf Finns Netz innerhalb von 20 % an 0,709 | 35 % |

## Rahmen

- Code-Agent ohne Einfrieren und Leser (Finn: einfach machen).
- GPU-Spuren p4000a und p4000b ueber kleintest.sh, geteilt mit AEQUIVALENZ-DREI-1 ueber die Spur-Locks, je Lauf
  hoechstens 10 min. Auswertungen auf cpu oder cpu7.
- df vor jedem Lauf, abbrechen unter 10 GB frei. Keine Konfigurationsserien speichern.
- Synthetisch, keine Messdaten. SU(2) statt SU(3) aus Kostengruenden; SU(3) folgt erst, wenn S2 traegt.
