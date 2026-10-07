# HAGEDORN-2: Halten dicke drehende Q-Ball-Ringe mit grossem m, kurz vor der Duennwand-Grenze? (Glied 7, Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 06:34:51 CEST (date), vor jeder Rechnung.
- **Anlass:** HAGEDORN-1 (RUNDE-37/hagedorn-1/ERGEBNIS.md, Vorschlag des Agenten).
  - Stabil sind nur m = 1 und 2 bei omega^2 = 0,55.
  - m = 3, 5 und 8 sind dort schwach instabil (Im Omega 4,0e-3 bis 5,4e-3, bei l = 2 und 3).
  - Bei groesserem omega^2 sind alle Ringe instabil. Die Rate faellt mit sinkendem omega^2 (0,12 bei 0,70, 0,005 bei
    0,55).
- **Schreibtisch der Leitung [M]** (Ernte HAGEDORN-1 in RUNDE-38.md):
  - Fuer die Hagedorn-Dichte braucht es keine linearen Moden.
  - Ein 1D-Objekt der Laenge L mit lueckenlosen Moden omega ~ k^z hat S ~ L^(z/(z+1)) E_exc^(1/(z+1)). Mit L ~ E
    (Zugspannung) folgt S ~ E fuer jedes z.
  - Entscheidend ist also: Sind grosse Ringe stabil, und gilt dort E ~ R?
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Test (Code-Agent)

- **Code:** HAGEDORN-1 (code/hagedorn.py, auswertung.py, regge2d.py) wiederverwenden.
- **Raster:** omega^2 in {0,51; 0,52; 0,53; 0,54} plus 0,55 als Anschluss. m in {3; 5; 8; 12}.
- **Azimutale Stoerungen:** l = 0 bis 3m (die staerkste Instabilitaet lag bei l ~ 1,6 m bis 2 m).
- **Profile:** Nahe omega^2 = 0,5 (M1-Duennwand-Grenze) werden sie gross. Kasten und Gitter mitwachsen lassen, Konvergenz
  zeigen.
- **Messgroessen:** max Im Omega je Profil und l; tiefste reelle Ringmoden; E und R je Profil.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| HZ0 | Kontrolle: Anschluss an HAGEDORN-1 bei omega^2 = 0,55, m = 3 und 5: max Im Omega auf 1e-4 (absolut) gleich | 85 % |
| HZ1 | [H] Bei omega^2 = 0,52 sind m = 3, 5 und 8 stabil (alle Im Omega < 1e-6 fuer l = 0 bis 3m) | 40 % |
| HZ2 | Fuer m = 3, 5 und 8 faellt max Im Omega mit sinkendem omega^2 von 0,55 bis 0,51 monoton (oder wird null) | 65 % |
| HZ3 | [H] Auf den stabilen Profilen bei festem omega^2 gilt E ~ R: doppelt-logarithmische Steigung 1 +- 0,15 aus mindestens drei stabilen m | 45 % |

**Bedeutung (vorab):**
- **HZ1 und HZ3 treffen ein:** Kurz vor der Duennwand-Grenze gibt es einen Turm stabiler Ringe mit Zugspannung und
  lueckenlosen Ringmoden. Nach dem Schreibtisch ergibt das eine exponentielle Zustandsdichte (Hagedorn-artig) [M/H].
  - Fuer Glied 7 waeren Q-Ball-Ringe dann ein Kandidat fuer den stringartigen Turm, den CEMZ verlangen.
  - Die Kopplung an das Graviton bleibt eine eigene Frage.
- **HZ1 verfehlt:** Grosse Ringe zerfallen auch dicht an der Grenze. Der Ringturm ist kein String; Glied 7 bleibt bei
  Strings oder anderen Auswegen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
