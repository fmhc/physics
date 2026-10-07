# TAKT-UMKLAPP-1: Zwischenstand Teil A (HT0, HT1')

- Geschrieben ab 2026-10-05 07:46:25 CEST (date), auf Bitte der Leitung (Zusatz 07:27).
- Grundlage: Lauf tu-A1 auf der .69 (Spur cpu8, kleintest.sh), 05:45:19 bis 05:45:29 UTC (07:45:19 bis 07:45:29 CEST),
  Laufzeit 9,0 s, rc = 0. Code eingefroren 07:45:03 CEST (code/tu.py sha256 6c5c3a95...; EINGEFROREN-SHA256.txt).
  Ergebnisdatei auf der .69: takt-umklapp-1/lauf/teilA-1-zellen.json (sha256 58e14052...).
- Zahlen von Hand aus der Ergebnisdatei gelesen (jq auf der .69); die mechanische Auswertung (tu.py auswertung) laeuft
  erst am Ende ueber alle Laeufe. Synthetische Gitterrechnung, keine Messdaten.

## Urteile nach Kartenwortlaut

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil (Wortlaut) | tragende Zahlen [E] |
|---|---|---|---|---|
| HT0 | P = -W^H B W = c d0^T *1 d0 auf V und S, festes c an allen k, auf 1e-10 | 75 % | **eingetroffen** | c = 8 (Median 7,999999999999998 auf V, 8,0 auf S; Streuung ueber k <= 4e-16); max \|P - c L1\| / max \|P\| = 6,6e-16 (V) und 5,5e-16 (S) an je 252 k (216 Gitter-k, 16 kleine k, 20 Zufalls-k) |
| HT1' | Auf V trotz negativer *2 alle *1 > 0; V_D Delaunay; S offen | 55 % | **eingetroffen** | V: 12 von 116 *2 negativ (alle -8/9), *1 alle positiv (1/720 bis 1/2), *0 alle positiv. V_D (12 2-3-Zuege, keine 3-2): *2 alle positiv (0,533 bis 8), kein mu < 0 (kleinster Randabstand 0,2204) |

- **Beides war vorab ableitbar bzw. schon bekannt (PLAN Abschnitt 1):** HT0 ist Glickensteins Satz (hier sogar je
  Tetraeder: Rest <= 9e-16, c = 8 in jedem Tetraeder). HT1' wiederholt mit einem zweiten Code, was PUMPE-NETZ-1 (*1 auf V
  positiv) und der UMKLAPP-1-Nachtrag (12 verletzte Flaechen je Zelle, V_D Delaunay, Randabstand 0,220) schon gerechnet
  hatten. Das ist keine neue Messung.
- **Nach Plan** (strenger, mechanisch erst am Ende): Fuer HT0 sind auch c_V = c_S, c(k) konstant und die Gegenprobe der
  Bauweise erfuellt (P aus ew.ops + mn.W_of von MATERIE-NETZ-1 gleich P aus tg auf 5,5e-16). Fuer HT1' entsteht V_D mit
  genau 12 2-3-Zuegen je Zelle. Beide Urteile sehen nach Plan ebenfalls nach "eingetroffen" aus; endgueltig durch die
  Auswertung.

## Neu und beschreibend

- **c = 8 genau**, wie im HODGE-L-Dossier erwartet [H dort]: Finns Takt ist achtmal der umkreisbasierte Hodge-Laplace,
  an jedem k und in jedem Tetraeder.
- **S ist Delaunay** (kleinster Randabstand mu = 1,237, keine Verletzung), alle *1 (0,098 bis 0,168), *2 (1,67 bis 3,6)
  und *0 positiv. S_D = S (kein Zug). Die Karte liess S offen.
- **P positiv semidefinit** auf V, S, V_D an allen 252 k (kleinster Eigenwert relativ >= -1,1e-16, also nur k = 0 null).
- **Traegheitskontrolle (HT3-Identitaet)** an allen 251 k != 0 auf V, S, V_D, S_D erfuellt: n_-(B) = 10 (V, V_D) bzw. 6
  (S) = n_+(P), n_-(B_red) = 0. Schwellenabstand: als null gezaehlte |lambda(B)| <= 7,8e-16, nicht null >= 7,7e-8
  (relativ).
- **Kontrollen:** sum l A* = 3 V, sum *0 = V, sum |f| L* = 3 V je auf 4e-16; Vorzeichen *2 und mu (Delaunay-Abstand)
  an allen Flaechen gleich; Diedersumme 2 pi auf 1,8e-15.
- **Offene Abweichung (K6, beschreibend):** PUMPE-NETZ-1 nennt fuer die P1-Gewichte auf V "1/60 bis 1/2"; hier ist der
  kleinste *1-Wert 1/720. Das Maximum 1/2 stimmt. Ursache nicht geprueft (andere Groesse, andere Normierung oder ein
  Schreibfehler dort); fuer HT0 ohne Belang, weil P = 8 L1 hier direkt gerechnet ist.

## Weiter

- Teil A laeuft weiter (Glasnetze, UMKLAPP-1-Netze fuer HT2, Traegheit fuer HT3), danach Teil B (TU1) wie geplant auf
  cpu8, cpu9, cpu10.

## Einfach gesagt

Finns Takt-Regel ist genau achtmal ein bekannter mathematischer Operator, der "Hodge-Laplace" des Netzes, und das gilt
in jedem einzelnen Tetraeder exakt. Auf Finns Netz V sind die Gewichte dieses Operators alle positiv, obwohl V an zwoelf
Flaechen je Zelle nicht "ordentlich" (Delaunay) ist. Nach zwoelf Umklappungen je Zelle ist V ordentlich. Das kantenaermere
Netz S ist schon von sich aus ordentlich. Das meiste davon war vorher bekannt oder herleitbar, es ist hier mit einem
zweiten Rechenweg bestaetigt.

## Berichtigung (2026-10-05 08:03:56 CEST, date)

- Oben steht, HT1' wiederhole, was PUMPE-NETZ-1 "(*1 auf V positiv)" schon gerechnet habe, und die Abweichung 1/60
  gegen 1/720 sei ungeklaert. Beides ist berichtigt: PUMPE-NETZ-1 hat P1-Gewichte (3D-Kotangens) gerechnet, und die
  sind in 3D nicht die umkreisbasierten *1 (Nachtrag, ERGEBNIS.md 4.5 a). "*1 > 0 auf V" ist also hier neu gerechnet,
  nicht wiederholt. Das Urteil HT1' (eingetroffen) aendert sich nicht.
