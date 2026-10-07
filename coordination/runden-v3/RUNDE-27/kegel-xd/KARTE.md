# KEGEL-XD: Ein Kopplungsgesetz Q-Ball <-> Kegeldefekt fuer jede Dimension? (Runde 27)

- Leitung: claude-primary. Karte, Schreibtischherleitung und Vorhersagen geschrieben ab 2026-10-03 05:40:17 CEST (date),
  vor jeder Rechnung.
- Herkunft:
  - Finn ~05:12: "Check die Geometrie Sachen aus x dimensionalen Sachen"
  - KEGEL-Q (RUNDE-26): nachtraeglich gefundenes Schwanzgesetz [H] E(d) - E(unendlich) ~ -+(delta/2) f^2(Spitze)
  - RUNDE-27/GEOMETRIE-XD.md: Fuenfer-Kanten in 3D tragen delta = 0,1284 rad
  - Astra-Ideen 04 (Defektpaar, Additivitaet erster Ordnung) und 07 (Rueckwirkung: derselbe Energieausdruck in beide
    Richtungen)

## Schreibtisch der Leitung (vor jeder Rechnung)

Modell: Q-Ball phi = f(x) e^{i omega t} bei festem Q. Energiefunktional wie in KEGEL-Q:

E = Q^2/(4 int f^2) + int |grad f|^2 + int U(f^2), mit F = E - omega Q = int (|grad f|^2 + V(f)), V = U(f^2) - omega^2 f^2.

1. **Erste Ordnung im Defizit delta:**
   - Ein Kegel mit Spitze (2D) bzw. eine Kegellinie (3D, Keil um die z-Achse) hat die Metrik
     dr^2 + a^2 r^2 dtheta^2 (+ dz^2) mit a = 1 - delta/(2 pi) und theta in [0, 2 pi).
   - Nach dem Huellensatz (Q fest, omega als Multiplikator) gilt
     Delta E = dF/da * da = (delta/2pi) int T_thth dV, mit T_thth = |grad_th f|^2 - |d_r f|^2 (- |d_z f|^2) - V.
   - Das ist die lineare Metrikkopplung -1/2 int T^ij h_ij; fuer einen Kegel sind nur die theta-Komponenten betroffen.
2. **Strahlunabhaengigkeit:**
   - Aus der Erhaltung div T = 0 folgt d_theta T_thth = -(1/r) d_r(r^2 T_rth) (- r d_z T_zth).
   - Damit ist J(theta) = int dz int_0^inf r T_thth dr fuer jeden Strahl theta gleich, also
     Delta E = delta * J(theta) mit beliebiger Strahlrichtung.
   - Probe: Der Strahl durch das Ballzentrum gibt dasselbe wie der Strahl vom Ball weg genau dann, wenn
     int_0^inf (f'^2 + V) drho = 0. Das ist der Impulsfluss durch die Symmetrielinie; er verschwindet fuer jeden
     ruhenden Ball.
3. **Ergebnis:** Den Strahl vom Ball weg legen. Dort gilt grad f entlang des Strahls (bzw. in der Ebene aus Strahl und
   z), also T_thth = -g(rho) mit g = f'^2 + U(f^2) - omega^2 f^2 und rho = Abstand zum Ballzentrum:
   - **2D (Kegelspitze im Abstand d):** Delta E_1(d) = -delta int_0^inf r g(d + r) dr
   - **3D (Kegellinie im Abstand d):** Delta E_1(d) = -delta int dz int_0^inf r g(sqrt((d + r)^2 + z^2)) dr
   - **Allgemein d Dimensionen, Defekt der Kodimension 2:** Delta E_1 = -delta int_Defekt dA int_0^inf r g dr
4. **Proben am Schreibtisch:**
   - **d = 0:** Delta E_1 = -(delta/2pi) int (|grad f|^2 + V). Mit Derrick ((n-2) G + n V_ges = 0) ist das
     -(delta/2pi)(E - omega Q). Das ist genau die erste Ordnung der exakten Abbildung E_flach(sQ)/s mit s = 2pi/(2pi - delta).
   - Mit den KEGEL-Q-Tabellenwerten Q = 200: E - omega Q = 157,2953 - 0,7449 * 200 = 8,315, also bei delta = pi/3
     Delta E_1(0) = -1,386.
     - Die exakten Werte sind -1,4465 (Fuenfer) und +1,34 (Siebener); der ungerade Teil ist 1,39, das sind 0,5 %.
     - Nicht blind: Die Tabellenwerte waren bekannt.
   - **Schwanz** (d >> R): g ~ 2 kappa^2 f^2 mit f' ~ -kappa f, also
     - 2D: Delta E_1 ~ -(delta/2) f^2(d). Das ist das nachtraegliche KEGEL-Q-Gesetz, jetzt hergeleitet.
     - 3D: Delta E_1 ~ -(delta/2) int f^2(sqrt(d^2 + z^2)) dz.
     - Korrekturen O(1/(kappa d)).
   - **Kraft:** -d(Delta E_1)/dd = -delta int_d^inf g drho. Sie verschwindet bei d = 0 und hat fuer jedes d dasselbe
     Vorzeichen. Fuenfer (delta > 0) zieht an, Siebener stoesst ab (wie KQ2).
5. **Bedeutung der Herleitung [H]:**
   - Q-Baelle koppeln an Kegeldefekte jeder Dimension (Punkt in 2D, Linie in 3D, Flaeche in 4D) in erster Ordnung nur
     ueber ihren Spannungstensor.
   - Ausserhalb des Balls faellt die Kopplung wie f^2, also kurzreichweitig; es gibt keine Fernkraft.
   - Literatur [L?, nicht gelesen]: Eine gerade kosmische Saite uebt auf ruhende Massen keine Newton-Kraft aus (Vilenkin
     1981); eine Ladung spuert nur eine Selbstkraft (Linet 1986, Smith 1990). Vor jeder Verwendung an der Quelle pruefen.

**Ableitbarkeitspruefung:**
- Die Karte prueft eine Herleitung (Faktoren, Vorzeichen, Erhaltungsargument) und die Groesse der Terme hoeherer Ordnung.
  Sie ist keine Messung.
- Teil A nutzt vorhandene KEGEL-Q-Daten. Die E(d)-Zahlen habe ich nicht gelesen, die Kurvenform aber im Bildbericht gesehen.
  Bei d = 0 ist A bekannt (siehe oben).
- Teil B (3D) ist neu.
- Projekt-grep: KEGEL-Q (RUNDE-26) hat das Schwanzgesetz nur nachtraeglich; eine Herleitung gibt es im Projekt nicht.

## Test (Code-Agent)

- **Teil A (2D, vorhandene Daten, nur Auswertung):**
  - Ebenes M1-Profil (beta = 1/2) bei Q = 200 radial berechnen; daraus Delta E_1(d) fuer delta = pi/3.
  - Vergleich mit den KEGEL-Q-Laeufen E(d) bei h = 0,2 (Fuenfer und Siebener):
    - ungerader Teil O(d) = [E_5(d) - E_7(d)]/2 gegen Delta E_1(d)
    - gerader Teil P(d) = [E_5(d) + E_7(d)]/2 - E_flach nur berichten
  - Gleiche Definition von d wie KEGEL-Q. Bei d != 0 ist die Lage nur bis O(delta^2) definiert; der ungerade Teil ist
    davon unberuehrt, weil E_flach nicht von d abhaengt.
- **Teil B (3D, neu):**
  - M1, beta = 1/2, 3D, ein Ball mit R_halb zwischen 4,5 und 5,5 (omega vorab aus dem Radialloeser festlegen).
  - Keil um die z-Achse in Zylinderkoordinaten (r, theta, z), theta-Periode Theta = 2 pi - delta.
    - Spiegelsymmetrien theta -> -theta und z -> -z sind erlaubt.
  - delta = +0,1284 und -0,1284: Fuenfer-Kante des Tetraederraums und Gegenstueck.
  - Ball bei festem Q mit festgehaltener Lage d in {0, 3, R_halb, R_halb + 2, R_halb + 4}; die Lagebedingung waehlt der
    Agent und legt sie im Plan fest.
  - Zwei Gitterweiten.
  - Ungerader Teil O(d) = [E(+delta, d) - E(-delta, d)]/2 gegen Delta E_1(d) aus dem ebenen 3D-Profil.
  - Kontrolle d = 0: exakte Keilabbildung E_flach(sQ)/s, nur fuer den zentrierten, achsensymmetrischen Ball.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KX0 | 3D, d = 0: Delta E(+delta) trifft die exakte Keilabbildung E_flach(sQ)/s - E_flach(Q) auf 3 % (Code-Kontrolle) | 85 % |
| KX1 | 2D (KEGEL-Q-Daten, delta = pi/3, Q = 200): \|O(d) - Delta E_1(d)\| <= 0,03 \|Delta E_1(0)\| fuer alle d der E(d)-Tabelle | 75 % |
| KX2 | 3D (delta = +-0,1284): \|O(d) - Delta E_1(d)\| <= 0,05 \|Delta E_1(0)\| fuer alle fuenf d (feinere Gitterweite) | 65 % |
| KX3 | Schwanz, beide Dimensionen: fuer d >= R_halb + 3/kappa liegt O(d) innerhalb 25 % von -(delta/2) f^2(d) (2D) bzw. -(delta/2) int f^2 dz (3D) | 60 % |

**Bedeutung (vorab):**
- KX1 und KX2 treffen ein: Das Kopplungsgesetz erster Ordnung gilt in 2D und 3D mit derselben Formel [H, numerisch
  geprueft]. Q-Baelle spueren Kegeldefekte jeder Dimension nur ueber ihren Spannungstensor, kurzreichweitig.
  - Fuer den Tetraederraum: Bindung an Fuenfer-Kanten von -(delta/2pi)(E - omega Q), also ~2 % von E - omega Q.
- KX1 trifft nicht ein, KX0 schon: Die Herleitung hat einen Fehler (Faktor, Vorzeichen oder Erhaltungsargument).
  Beschreiben, nicht nachtraeglich anpassen.
- KX2 trifft nicht ein, KX1 schon: In 3D fehlt etwas. Zu pruefen sind Keilrand, Lagebedingung und Diskretisierung.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren. Zielwerte (Delta E_1) vor den 3D-Laeufen in eine Datei schreiben und
  versiegeln (chmod a-w), nicht als Befehlszeilen-Argumente.
- Zeitbox 100 min.
