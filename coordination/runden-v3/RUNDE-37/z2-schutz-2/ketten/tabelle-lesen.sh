#!/bin/bash
# Z2-SCHUTZ-2: liest die Ergebnisfelder je Groesse (nur jq-Auswahl, keine Rechnung). Aufruf auf der .69 im Ordner lauf/.
set -u
for t in r10-R20 r10-R24 r10-R28 r10-R32 r8-R24 r12-R24 r14-R24; do
  echo "== $t"
  [ -e start-$t.json ] && jq -c '{E_S, fmax, grund, schritte, hw: .hesse_S.eigenwerte, hu: .hesse_S.symmetrie_ueberlapp, ht: .hesse_S.laufzeit_s, N: .netz_info.N, frei: .netz_info.frei, kern: .netz_info.kern, sonde: .sonde, laufzeit_s}' start-$t.json
  [ -e bisekt-$t.json ] && jq -c '{barriere, genau, pfad_ok, weg_art, gA: .gueltig_A_ohne_S, n_halb, lambda_lo, lambda_hi, zahl_M, zahl_offen, s1: (.sattel1 // {} | {E_sattel, barriere, fmin_oben, fmin_unten, klasse_oben, klasse_unten, genau}), s2: (.stufe2 | {gilt, n_halb}), s3: (.stufe3 | {gerechnet, n_halb, s3b: (.stufe3b // {} | {gilt, n_halb}), sat2: (.sattel2 // {} | {E_sattel, barriere, fmin_oben, fmin_unten, klasse_oben, klasse_unten, genau, unten_ende_gleich_M, unten_ende_D_zu_M})}), fr: (.freigabe // {} | {klasse, schritte, E_end, E_max, T_erreicht, E_max_unter_ES, bindungen_c_le_0_ende, t}), lok: (.lokalisierung // {} | {L10, L6, n50, Delta_max, r_max, gamma_max_grad, c_sattel_max, bindungen_c_le_0, anteil_kernbindungen}), laufzeit_s}' bisekt-$t.json
  [ -e weg-haupt-$t-neb.json ] && jq -c '{barriere, E_sattel, it: .weg.iterationen, grund: .weg.grund, konv: .weg.konvergiert, ki: .weg.ki, fki: .weg.fki, fband: .weg.fband, prof: .weg.E_profil, eben: .kletterbild_eben_rest, lok: (.lokalisierung // {} | {L10, L6, n50, Delta_max, r_max, gamma_max_grad, c_sattel_max, bindungen_c_le_0, anteil_kernbindungen}), laufzeit_s}' weg-haupt-$t-neb.json
done
