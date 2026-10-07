// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// Nur fuer die CSP-Pruefung (Testkopien mit Meta-Richtlinie), NICHT Teil der oeffentlichen Fassung.
// Zaehlt securitypolicyviolation-Ereignisse, schreibt sie in die Konsole und zeigt eine Plakette.
(function () {
  var liste = [];
  var plakette = null;
  console.info('CSP-ZAEHLER aktiv: ' + location.pathname);
  function zeigen() {
    document.documentElement.setAttribute('data-csp-verstoesse', String(liste.length));
    if (!document.body) return;
    if (!plakette) {
      plakette = document.createElement('div');
      plakette.id = 'csp-plakette';
      var s = plakette.style;
      s.setProperty('position', 'fixed');
      s.setProperty('top', '4px');
      s.setProperty('left', '50%');
      s.setProperty('transform', 'translateX(-50%)');
      s.setProperty('z-index', '99');
      s.setProperty('padding', '3px 10px');
      s.setProperty('font', '500 12px/1.3 monospace');
      s.setProperty('pointer-events', 'none');
      document.body.appendChild(plakette);
    }
    var ok = liste.length === 0;
    plakette.style.setProperty('background', ok ? '#0d3b1e' : '#5a0f0f');
    plakette.style.setProperty('color', ok ? '#9ff0b8' : '#ffd0d0');
    plakette.style.setProperty('border', '1px solid ' + (ok ? '#2f9e5a' : '#ff6b5e'));
    plakette.textContent = 'CSP-Test (Meta-Richtlinie): ' + liste.length + ' Verstöße' + (ok ? '' : ': ' + liste.join(' | '));
  }
  document.addEventListener('securitypolicyviolation', function (e) {
    var eintrag = e.effectiveDirective + ' ' + (e.blockedURI || '-') + ' @ ' + (e.sourceFile || '-') + ':' + (e.lineNumber || 0);
    liste.push(eintrag);
    console.error('CSP-VERSTOSS ' + eintrag + ' sample=' + (e.sample || ''));
    zeigen();
  });
  document.addEventListener('DOMContentLoaded', zeigen);
  window.addEventListener('load', function () {
    zeigen();
    console.info('CSP-ZAEHLER Stand nach load: ' + liste.length);
  });
  setInterval(zeigen, 1000);
})();
