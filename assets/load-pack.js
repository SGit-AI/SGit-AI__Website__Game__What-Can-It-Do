/* load-pack.js — the "Load a pack" control on /data/.
 *
 * Pick a pack from the registry, or paste the URL of a folder that holds a pack.json manifest;
 * the control reads the manifest, says what it found (name, version, hash, file count), and
 * opens the game on that pack — the same vault, the same game, a different world to ask about.
 *
 * What it checks and what it does not: it fetches `<base>pack.json`, refuses anything that is
 * not a pack/v1 manifest, and reports the manifest's own figures. It does not verify the hash
 * (the game's build does that for its snapshot; a running page reads what the manifest names).
 * The honest signal is inside the game: its footer says which pack it actually read, computed
 * from the manifest it fetched. If the vault host does not carry the query string through to
 * the game, the footer says "the public pack", and that is the answer to the plan's open test.
 *
 * Mounting: the embed component exposes SGVaultApp.mount, so a frame can be opened after the
 * page has loaded, for a pack chosen by the reader.
 */
(function () {
  'use strict';

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function slashed(u) { return /\/$/.test(u) ? u : u + '/'; }

  function init() {
    var form = document.querySelector('form.loadpack');
    if (!form) return;
    var vault = form.getAttribute('data-vault');
    var readkey = form.getAttribute('data-readkey');
    var sel = form.querySelector('select');
    var url = form.querySelector('input[type="url"]');
    var out = form.querySelector('.lp-out');
    var mount = document.getElementById('lp-mount');
    var say = function (html) { out.innerHTML = html; };

    // the registry, from beside this page
    fetch(form.getAttribute('data-registry'), { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(function (reg) {
        (reg.packs || []).forEach(function (p) {
          var o = document.createElement('option');
          o.value = p.base;
          o.textContent = p.name + (p.resolved ? ' — ' + p.resolved.version + ' · ' + String(p.resolved.content_hash).slice(7, 15) : '');
          sel.appendChild(o);
        });
      })
      .catch(function () { say('The registry could not be read; paste a manifest URL instead.'); });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var base = (url.value || sel.value || '').trim();
      if (!/^https?:\/\//i.test(base)) return say('Pick a pack, or paste the URL of the folder that holds its pack.json.');
      base = slashed(base);
      say('Reading ' + esc(base) + 'pack.json …');
      fetch(base + 'pack.json', { cache: 'no-store' })
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
        .then(function (m) {
          if (!m || m.type !== 'pack/v1') throw new Error('not a pack/v1 manifest');
          var files = Array.isArray(m.contents) ? m.contents.length : '?';
          say('<b>' + esc(m.name || m.id || 'a pack') + '</b> · ' + esc(m.version || '') + ' · ' +
              esc(String(m.content_hash || '').slice(7, 15)) + ' · ' + esc(files) + ' files. ' +
              'Opening the game on it. The game\'s footer says which pack it actually read.');
          open(base);
        })
        .catch(function (err) {
          say('That is not a pack the game can read: ' + esc(err.message) + '. A pack is a folder ' +
              'with a <code>pack.json</code> manifest of type <code>pack/v1</code>, served with CORS open.');
        });
    });

    function open(base) {
      mount.innerHTML = '';
      var el = document.createElement('div');
      el.className = 'sgv-app sgv-breakout';
      el.setAttribute('data-vault', vault);
      el.setAttribute('data-readkey', readkey);
      el.setAttribute('data-entry', 'what-can-it-do/index.html?pack=' + encodeURIComponent(base));
      el.setAttribute('data-label', 'What Can It Do?, on the pack you chose');
      mount.appendChild(el);
      if (window.SGVaultApp && window.SGVaultApp.mount) window.SGVaultApp.mount(el);
      else say('The vault embed component did not load, so the game cannot be opened here.');
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
