# G2-02 Altern ueber einen masselosen Kanal: Ladungs- und Energiebilanz des Verdampfens

- Quelle: RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md, Kennung "Bio 48" ("Altern"). Nur ins Kartenformat gebracht, keine neue
  Idee. Bisheriges Ergebnis (R5-D altern, RUNDE-05/r5d/lauf-69/altern/): Rate 0,61 bis 1,37 der Formel, negative
  Endladung im Fenster bei omega^2 = 0,55, Bilanz unplausibel, geparkt ("vorher klaeren, was die negative Endladung bei
  0,55 bedeutet", ERGEBNISSE-R5-CD.md, D4). Test hier: der naechste Schritt aus dem Parkgrund, die Ladungs- und
  Energiebilanz des Alterns sauber machen.

- Hypothese (Bio 48): Eine schwache Kopplung an einen masselosen Kanal laesst den Q-Ball langsam verdampfen; in 1D mit
  der Rate erster Ordnung Gamma = eps^2 ft(omega)^2/omega, ft(k) = Int f(x) cos(k x) dx (R5-D, PLAN.md 2.4). Der Ball
  bleibt dabei ein Ball und gibt Ladung als eine auslaufende Linie bei seiner Frequenz omega ab [H].

- Papier vorab [S] (eigene Rechnung und Lesebefund, von Hand):
  - Modell wie R5-D altern: psi-Ball ruhend, chi frei mit mc2 = eps^2, eps = 0,05, Austausch eps (conj(psi) chi + c.c.);
    eine Eigenmode genau masselos. Box [-150, 150], Schwamm ab |x| = 110, T = 400, dx = 0,1, dt = 0,05.
  - Eine auslaufende Welle im masselosen Kanal bei Frequenz omega hat k = omega; Ladungsfluss 2 k |A|^2, Energiefluss
    2 omega k |A|^2. Also traegt eine einfarbige Linie genau E/Q = omega. Laengs einer Ballfamilie gilt dazu
    dE/dQ = omega. Verdampft der Ball nach der Formel, verliert das Fenster Energie und Ladung im Verhaeltnis omega.
  - Andere Kanaele verschieben dieses Verhaeltnis: Seitenbaender einer angeregten inneren Mode liegen bei
    omega + rho und omega - rho (bekannte 1D-Pole [A]: omega^2 = 0,55: 2,118 und -0,635; 0,70: 2,330 und -0,657). Das
    obere hebt E/Q, das untere hat negative Frequenz, traegt negative Ladung nach aussen und hebt E/Q ebenfalls.
  - Lesebefund R5-D (keine neue Rechnung): Bei 0,55 faellt die Fensterladung (|x| < 40) von 3,878 auf -0,932, die
    Boxladung (|x| < 100) aber nur um 23 %. Ladung hat das Fenster verlassen, ohne die Box zu verlassen; Strahlung mit
    Lichtgeschwindigkeit, die vor t = 340 ausgesandt wurde, waere bei T = 400 schon jenseits |x| = 100. Die
    Geradensteigung auf [100, 400] (6,8e-3) ist viel kleiner als der mittlere Abfall (1,5e-2): Der Abfall ist spaet
    und steil. Bei 0,51: Fenster -49 %, Box -32 %. Ab 0,6 stimmen Fenster und Box auf 2 % der Ladung ueberein.
  - Folge: Ab 0,6 muss die Bilanz nach der Formel schliessen. Bei 0,51 und 0,55 kommt spaet ein zweiter Vorgang dazu;
    ob Aufbruch, Ausstoss oder Ausbruch negativer Ladung, sagt die Karte nicht vorher [H].

- Kleiner Test:
  - Code: Kopie RUNDE-05/r5d/r5d.py als r5d_bilanz.py mit neuem Unterbefehl "bilanz" (gleiche 11 Laeufe und
    Anfangsfelder wie altern; Dynamik unveraendert). Neu sind nur Messgroessen, alle 0,5 Zeiteinheiten:
    - Q und E im Fenster |x| < 40, in der Schale 40 <= |x| < 110, im Schwammbereich |x| >= 110 und im ganzen Gitter
    - vom Schwamm geschluckt: Q_abs(t) = Q_ges(0) - Q_ges(t), E_abs(t) = E_ges(0) - E_ges(t)
    - negative Ladung im Fenster Q_neg = Int_{|x|<40} min(rho, 0) dx, getrennt fuer psi und chi auch Q_psi, Q_chi
    - Ball: Ort und Hoehe des Maximums von |psi|^2, mittleres |x| mit Gewicht |psi|^2 im Fenster, Frequenz in der
      Ballmitte omega(t) = Im(psi conj(psi_t))/|psi|^2 am Maximum
    - E/Q des Fensterverlusts: R_EQ = Steigung von E_Fenster geteilt durch Steigung von Q_Fenster (Geraden auf dem
      Auswertefenster), dazu omega_quer = Mittel von omega(t) im selben Fenster
  - Laeufe (eps = 0,05, T = 400, wie R5-D): masselos omega^2 = 0,500001 / 0,5001 / 0,51 / 0,55 / 0,6 / 0,7 / 0,8 / 0,9;
    Gegenproben wie unten; zusammen 11 Laeufe, grob und fein.
  - Rechenort: .69 ueber kleintest.sh, p4000a, ein Aufruf mit grob und fein (R5-D: 16 s und 32 s), etwa 1 bis 2 min.

- Vorhersage vorab:
  - V1 (Linie): Fuer omega^2 = 0,6 / 0,7 / 0,8 gilt auf [100, 400]: R_EQ/omega_quer = 1 +- 0,05.
  - V2 (Ball bleibt Ball): Fuer omega^2 = 0,6 / 0,7 / 0,8 / 0,9 bleibt das Maximum von |psi|^2 bei |x| <= 0,5, die
    negative Fensterladung bleibt klein (|Q_neg| <= 1e-3 Q(0)), und die Fensterladung faellt um hoechstens 5 % mehr
    als die Ladung von Fenster plus Schale (die Ladung, die das Fenster verlaesst, verlaesst auch die Box).
  - V3 (Parkgrund, 0,51 und 0,55): Auf [100, 200] gelten V1 und V2 auch dort (R_EQ/omega_quer = 1 +- 0,05, Maximum bei
    |x| <= 0,5, |Q_neg| <= 1e-3 Q(0)). Der zweite Vorgang setzt bei 0,55 erst nach t = 200 ein. Dass er spaet kommt, folgt
    schon aus dem Lesebefund oben; das ist keine starke Vorhersage. Neu gemessen wird, was er ist.
  - V4 (Anschluss): Die Fensterladung bei T = 400 stimmt mit R5-D auf 1e-6 relativ ueberein (gleiche Dynamik).
  - **Scheitert, wenn** eines davon eintritt:
    - R_EQ/omega_quer liegt bei einem der drei omega^2 aus V1 ausserhalb 0,95 bis 1,05
    - bei einem omega^2 aus V2 wandert das Maximum ueber |x| = 0,5 hinaus oder |Q_neg| > 1e-3 Q(0), oder Fenster und
      Fenster plus Schale verlieren um mehr als 5 % von Q(0) verschieden viel
    - bei 0,51 oder 0,55 reisst V1 oder V2 schon auf [100, 200]
  - Nicht entscheidbar, wenn V4 reisst oder die Plausibilitaetsschranke reisst.

- Gegenprobe:
  - Kanal mit Masse 1,2 (mc2 = 1,44 > omega^2) bei 0,500001 und 0,7: |Steigung Q_Fenster| < 1e-2 der Formelrate
    desselben omega, Q_abs(T) < 1e-3 Q(0). Ohne offenen Kanal kein Verdampfen.
  - eps = 0 bei 0,7: |Steigung Q_Fenster| < 1e-7, |Q_abs(T)| < 1e-7 Q(0), |Q_neg| < 1e-9.

- Plausibilitaetsschranke:
  - Gesamtladung (ganzes Gitter) bis t = 90 (vor jedem Schwammkontakt) auf 1e-9 relativ erhalten; Gesamtenergie bis
    t = 90 auf 1e-4 relativ
  - Der Schwamm schluckt nur: E_ges(t) steigt nie um mehr als 1e-6 E(0) ueber den bisherigen Tiefstwert
  - omega(t) in der Ballmitte liegt unter 1, solange |psi|^2 dort ueber 0,01 liegt
  - Fenster + Schale + Schwammbereich + geschluckt = Q(0) (Buchfuehrung, Rest < 1e-9 Q(0))

- Latten erwartet:
  - L1 ja: Verhaeltnis E/Q, Ort des Balls, negative Ladung und die Fruehphase bei 0,51 und 0,55 koennen je scheitern.
  - L2: Kanal mit Masse 1,2, eps = 0.
  - L3: dx/2 und dt/2; R_EQ auf 1 %, Gamma auf 5 x Aenderung (wie R5-D).
  - L4 teilweise: Verdampfung von Q-Baellen in masselose Fermionen (Cohen, Coleman, Glashow, Georgi 1986) [L, aus dem
    Gedaechtnis, nicht nachgelesen]; der bosonische Kanal hier hat keine Pauli-Grenze.
  - L5: nein.

- Einfach gesagt: Ein Q-Ball, der schwach an masselose Teilchen gekoppelt ist, verliert langsam Ladung, wie ein
  Wassertropfen, der verdunstet. In einem frueheren Test passte die Verlustrate zur Formel, aber bei einer Ballgroesse
  war am Ende sogar negative Ladung im Messfenster, und die Buchhaltung ging nicht auf. Jetzt fuehren wir genau Buch: wie
  viel Ladung und Energie wohin geht, wo der Ball ist und mit welcher Frequenz er schwingt. Wir sagen voraus: Bei den
  kleineren Baellen geht alles sauber als eine Welle bei der Ballfrequenz weg; bei den grossen passiert spaeter noch
  etwas anderes, das wir jetzt sichtbar machen.

- Karte geschrieben: 2026-09-30 11:15:58 CEST
- Vorhersage geschrieben: 2026-09-30 11:16:14 CEST
