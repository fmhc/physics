# QBALL-GITTER-1: Wie schnell kann ein Q-Ball werden, wenn der Raum ein Gitter ist? (Runde 35)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 21:55:53 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn 03.10.: "beschleunigen eingefangene baelle auf lichtgeschwindigkeit?" (LICHT-1: in Kegelmulden hoechstens 0,42 c).
  - Finns Netzbild: Lichtgeschwindigkeit als Netzgeschwindigkeit.
  - NETZ-C-1, Teil B: Ein Kink in der Kette wird relativistisch mit der Netzgeschwindigkeit als c. Unter konstanter Kraft
    ohne Reibung saettigt gamma aber bei 1,78 / 2,61 / 3,86 (h = 0,5 / 0,25 / 0,125), weil er abstrahlt.
  - Offen ist dasselbe fuer unseren Q-Ball (Schwerpunkt der Schleife). Bezug Spin-2-Kette Glied 10 (Lorentz-Invarianz)
    und LORENTZ.md.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Modell:** M1 in 1D auf einem Gitter mit Abstand h: komplexes psi_n, U(S) = S - S^2 + S^3/2 (beta = 1/2).
  - Die Kontinuums-Q-Baelle in 1D sind fuer alle omega in (omega_min, 1) stabil [M, Vakhitov-Kolokolov, dQ/domega < 0].
  - Gewaehlt omega^2 = 0,7; Breite ~ 1/sqrt(1 - omega^2) ~ 1,8.
- **Kraft:** gleichmaessiges aeusseres "elektrisches" Feld E auf die U(1)-Ladung, eichtreu auf dem Gitter.
  - Am einfachsten zeitliche Eichung mit Peierls-Phase auf den Verbindungen, (D psi)_n = (exp(-i h a(t)) psi_{n+1} -
    psi_n)/h mit a(t) = E t. Vorzeichen so pruefen, dass eine positive Ladung nach +x beschleunigt.
  - Im Kontinuum gilt d(gamma M v)/dt = Q E (geladenes Teilchen) [M].
- **Gitterlinearwellen** [M]: omega(k)^2 = 1 + (4/h^2) sin^2(k h/2). Groesste Gruppengeschwindigkeit
  v_g,max = 0,781 / 0,883 / 0,940 (h = 0,5 / 0,25 / 0,125), also gamma 1,60 / 2,13 / 2,92.
  - Der Kink aus NETZ-C-1 lag darueber (1,78 / 2,61 / 3,86). Ein nichtlineares Objekt ist nicht an v_g,max gebunden.
- **Bloch-Bild** [M, H]: In zeitlicher Eichung haengt die Gitterdynamik nur ueber exp(i h a(t)) von a ab. Sie ist
  periodisch mit der Bloch-Periode T_B = 2 pi/(h E).
  - Ein Teilchen, dessen Impuls die ganze Brillouin-Zone durchlaeuft, beschleunigt nicht unbegrenzt. Es pendelt zurueck
    (Bloch-Schwingung), wenn es nicht vorher abstrahlt oder zerfaellt.
  - Ob ein Q-Ball pendelt, abstrahlt oder zerbricht, ist offen.

## Test (Code-Agent)

- **Gitter:** h = 0,5, 0,25, 0,125; Laenge so, dass der Ball den Rand bis Laufende nicht erreicht (oder Absorber,
  offenlegen).
- **Start:** Gitter-Q-Ball bei omega^2 = 0,7, ruhend (stationaere Gitterloesung per Relaxation oder Schiessen, oder
  Kontinuumsprofil mit Einschwingen; offenlegen).
- **Feld:** E so, dass Q E/M ~ 0,005 (M = Ballenergie in Ruhe); zum Vergleich ein zweites E (doppelt).
- **Gemessen:**
  - Ladungsschwerpunkt X(t), Schnelle v(t), gamma(t)
  - im Ball verbliebene Ladung (Fenster um X)
  - Abstrahlung (Ladung und Energie ausserhalb), Energiebilanz mit der Arbeit des Felds
- **Laufzeit:** bis mindestens T_B/2 bei h = 0,5, bei den feineren h mindestens bis zum Saettigen oder Umkehren.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| G0 | Kontrolle: ohne Feld bleibt der Gitter-Ball liegen (Drift < 1e-4 bis t = 500), Ladung auf 1e-10, Energie auf 1e-7 erhalten | 90 % |
| G1 | h = 0,125: anfaengliche Beschleunigung relativistisch, gamma M v = Q E t innerhalb 2 % bis gamma = 1,5 | 75 % |
| G2 | gamma erreicht ein Maximum gamma_max(h), das mit kleinerem h waechst; gamma_max(0,125) >= 1,5 gamma_max(0,5) | 70 % |
| G3 | [H] Nach dem Maximum wird der Ball langsamer und kehrt um (Schnelle wechselt das Vorzeichen) vor t = T_B, mit >= 50 % seiner Ladung (Bloch-artig) | 35 % |
| G4 | [H] Bei gleichem h ist gamma_max des Q-Balls mindestens so gross wie beim Kink aus NETZ-C-1 (1,78 / 2,61 / 3,86) | 50 % |

**Bedeutung (vorab):**
- G1 und G2 treffen ein: Auf einem Gitter verhalten sich Q-Baelle relativistisch, aber nur bis zu einer Hoechstgamma, die
  von der Maschenweite abhaengt.
  - In Finns Netzbild hiesse das: Teilchen lassen sich nicht beliebig beschleunigen.
  - Die schnellsten gemessenen Teilchen (kosmische Strahlung, gamma ~ 1e11 [L]) begrenzen dann das Verhaeltnis von
    Maschenweite zu Teilchengroesse [H, Uebertragung von 1D].
- G3 trifft ein: Der Ball pendelt im Gitter wie ein Elektron im Kristall (Bloch). Das waere ein scharfes Unterscheidungs-
  merkmal eines Gitterraums.
- G3 verfehlt, dafuer Ladungsverlust: Der Ball zerstrahlt an der Gittergrenze. Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (nicht cpu, cpu2, cpu5, cpu6, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
