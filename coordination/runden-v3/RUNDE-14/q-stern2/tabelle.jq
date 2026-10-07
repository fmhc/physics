# Q-STERN-2: Kurztabelle je Lauf-JSON (jq -c -f tabelle.jq aus/*.json)
{datei: (input_filename | split("/") | last), alpha, psi, h, r_fak, laufzeit: (.laufzeit // .laufzeit_bisher),
 ende: (.ende // "laeuft/fehlt"), entfallen: ((.budget_entfallen // []) | length),
 kand: [.kandidaten[]? | {x: .lokal.x_stern, rho: .lokal.rho_stern, ri: .wechsel.richtung, kl: .lokal.klammer_breite,
        u: .rechteck.umlauf, ur: .rechteck.umlauf_roh, auf: .rechteck.aufgeloest, sp: .rechteck.max_sprung,
        k5: .K5.rest_rel, sv: .K5.sv_verh, komp: .kompaktheit_ort.kompaktheit, phirw: .kompaktheit_ort.Phi_Rw,
        fehler: (.fehler // .rechteck.fehler // null)}],
 wechsel: [.vorzeichenwechsel[]? | {x1, x2, rho1, rho2, ri: .richtung}],
 streifen: [.streifen[]? | {i, u: .umlauf, auf: .aufgeloest, sp: .max_sprung, f: .fehler}]}
