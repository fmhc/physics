# QBALL-DOPPELSPALT-1: Lesefilter Dreifachspalt (nur Anzeige)
def r3: if . == null then null else (. * 1000 | round / 1000) end;
.kombis | to_entries[] | select(.value.nspalt == 3) |
  [.key, .value.n_durch, (.value.I3_kde.kappa_L1 | r3), (.value.I3_kde.kappa_int | r3), (.value.I3_ladung.kappa_L1 | r3),
   (.value.I3_ladung.kappa_int | r3), (.value.I3_zentral_bin5.kappa | r3), (.value.I3_zentral_ladung.kappa | r3), (.value.I3_ladung.delta | r3)]
