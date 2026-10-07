# PHASE-3D-BLIND (Runde 31): lauf-69/sprossen.json aus lauf-69/auswertung.json (PLAN.md Abschnitt 7; nur Umformung).
# Aufruf: jq --arg erzeugt "<date>" -f sprossen.jq lauf-69/auswertung.json
def groesser($a; $b): if $a == null then $b elif $b == null then $a elif $a > $b then $a else $b end;
{erzeugt: $erzeugt,
 quelle: "lauf-69/auswertung.json (code/auswertung.jq aus den suche.json der Laeufe h004, h002, u004, rand)",
 konventionen: {eps: "omega^2 - omega_min^2, omega_min^2 = 1 - 1/(4 beta)",
                omega2: "Wurzel von s(omega^2) auf h = 0,02 (Lauf h002)",
                umlauf: "Kreuzungszaehlung des Rechtecks (Lauf u004, h = 0,04); umlauf_phase = Phasenaufloesung",
                R_halb: "S(R) = S_c/2 mit S_c = 1/(2 beta) wie RUNDE-26 (Hermite auf dem bic2-Profil, h = 0,02)",
                R_halb_S0: "S(R) = S(0)/2 (bic2 r_halb)",
                rho: "Nullstelle von L(y_b) an der Sprosse (h = 0,02)",
                unsicherheit_omega2: "|omega2(h002) - omega2(h004)| + groessere Endklammer (Plan)",
                rauschmass_omega2: "groesseres von h002/h004: 1e-15 * groesster Einzelterm von L(y_a) / |ds/domega^2| (Bericht)",
                index: "beta = 1/2: Leiternummer n; beta = 1: Fortsetzung der R24-Zaehlung k (k = 1 bei eps 0,030879)"},
 sprossen: [.sprossen[] | {beta, index, name, omega2, eps, inv_eps, umlauf, umlauf_phase, rechteck_aufgeloest,
                           R_halb, R_halb_S0, rho, unsicherheit_omega2, unsicherheit_inv_eps,
                           rauschmass_omega2: groesser(.rauschmass_omega2_h002; .rauschmass_omega2_h004),
                           gitter_vergleich,
                           kernwachstum_kandidat: .kernwachstum_kandidat_h002}],
 pb0: .pb0, pb1: {je_fenster: .pb1.je_fenster, wechsel: .pb1.wechsel, eingetroffen: .pb1.eingetroffen}}
