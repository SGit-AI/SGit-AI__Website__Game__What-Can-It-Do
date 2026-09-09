/* vault-app-embed.js — a vault app, live on a normal web page, over the SG/Vault embed protocol.
 *
 * This is the sgit.ai `assets/vault-ui-embed.js` component with one behaviour added and one
 * default flipped, for the reason set out in briefs/00__PLAN.md §4:
 *
 *   · APP-ONLY BY DEFAULT. The sgit.ai component always appends the vault-browser surface
 *     under App Mode, because on that site the browser IS the argument. Here the game is the
 *     argument, so the browser surface is opt-in (`data-browser="1"`). That is the whole of
 *     the "small change" the plan asked for.
 *   · CHROMELESS MODE (`data-chromeless="1"`). Drops the surface label and the status line so
 *     the app is the only thing on the page. For the player site, where a reader who has never
 *     heard of a vault should see a game and nothing else.
 *
 * Everything that matters about the protocol is unchanged, and is unchanged deliberately:
 *
 *   1. Load `<origin>/en-gb/app/?embed=1&parent=<our origin>`.
 *   2. Wait for `{sg:'vault-embed-ready'}` FROM THAT FRAME — not from any frame, and not from
 *      any other origin. Every inbound message is checked against `ORIGIN` first.
 *   3. Post `{sg:'vault-open', key, mode}` with `targetOrigin` PINNED to the vault origin.
 *
 * That third point is why this component exists rather than an `<iframe src="…/#key">`: the
 * credential is handed over by postMessage to one named origin. It never appears in a URL, so
 * it is never in browser history, never in a Referer header, and never in a server log.
 *
 * WHY THIS HOST AND NOT THE MINIMAL ONE. sgit.ai also ships `assets/vault-embed.js`, which
 * decrypts the vault in this page and boots the app in a sandboxed srcdoc frame. It is smaller
 * and it renders faster, and it serves reads ONLY — no `sg.llm.*`, no `sg.append.*`, and it
 * never reads `app.json`. The games declare `llm.chat` (the chat panel, v0.14.0) and
 * `append.write` (the telemetry lane), so under that host the chat panel is dead and the
 * permission grants are inert. Real host, or no chat panel: there is no third option.
 *
 * Usage:
 *   <div class="sgv-app" data-vault="4evnlwrj" data-readkey="<64 hex>"
 *        data-label="The game, running out of the vault"
 *        data-entry="which-agent-is-it/index.html"   <!-- optional deep link -->
 *        data-chromeless="1"                          <!-- optional -->
 *        data-browser="1"></div>                      <!-- optional: also show the browser -->
 *
 * The read key is a PUBLISHED read-only credential. It cannot write, and a page that holds one
 * cannot mutate the vault whatever it does. Never put a vault key here: `<passphrase>:<id>` is
 * the vault-key shape, it carries write access, and `admin/build/validate.js` fails the build
 * on anything shaped like one.
 */
(function () {
  'use strict';

  var ORIGIN = 'https://dev.vault.sgraph.ai';
  var HANDSHAKE_MS = 12000;   // then fall back to the fragment flow
  var READY_MS     = 9000;    // then open the next surface anyway

  function mountAll() {
    var hosts = document.querySelectorAll('.sgv-app');
    for (var i = 0; i < hosts.length; i++) mount(hosts[i]);
  }

  function mount(el) {
    var vaultId = el.getAttribute('data-vault');
    var readKey = el.getAttribute('data-readkey');
    if (!vaultId || !readKey) return;

    var entry      = el.getAttribute('data-entry') || '';
    var chromeless = el.getAttribute('data-chromeless') === '1';
    var withBrowser= el.getAttribute('data-browser') === '1';
    var cred       = 'sgit_rk1_' + readKey + ':' + vaultId;

    // The label names the surface. It has to come from the mount: this component is used
    // for the games AND for Licence to Operate, and a page embedding the simulation that
    // announces "the game" is simply lying to the reader.
    var label = el.getAttribute('data-label') || 'Running live out of the vault';
    var sections = [section(el, cred, entry, 'app', '▶ ' + label, chromeless)];
    if (withBrowser) {
      sections.push(section(el, cred, '', 'vault', '▤ Vault browser — FILES / SGIT / SETTINGS', chromeless));
    }

    // One listener per mount; replies are routed by which frame sent them. Origin is checked
    // before anything else — a message from any other origin is not ours, whatever it says.
    window.addEventListener('message', function (e) {
      if (e.origin !== ORIGIN) return;
      for (var i = 0; i < sections.length; i++) {
        var s = sections[i];
        if (!s.frame.contentWindow || e.source !== s.frame.contentWindow) continue;
        var d = e.data || {};
        if (d.sg === 'vault-embed-ready' && s.armed) {
          clearTimeout(s.fallbackT);
          var msg = { sg: 'vault-open', key: cred, mode: s.mode };
          if (s.entry) msg.deepLink = s.entry;
          e.source.postMessage(msg, ORIGIN);
          s.say('Handshake complete — the key went over postMessage, never in a URL. Opening…');
        } else if (d.sg === 'vault-ready') {
          s.say('Open, <b>read-only</b>' + (d.fileCount ? ' — ' + d.fileCount + ' files decrypted in the frame' : '') + '.');
          s.settle();
        } else if (d.sg === 'vault-error') {
          s.say('The vault would not open: ' + esc(d.message || 'no reason given') + '. ' +
                'You can <a href="' + ORIGIN + '/#' + encodeURIComponent(cred) + '">open it in a new tab</a> instead.');
          s.settle();
        }
        return;
      }
    });

    // Open the first surface now, the next when the previous reports ready (so its fetches hit
    // a warm object cache), with a grace timeout so one slow surface never blocks the next.
    var chain = sections.slice();
    (function next() {
      var s = chain.shift();
      if (!s) return;
      var advanced = false;
      s.settle = function () { if (!advanced) { advanced = true; next(); } };
      setTimeout(function () { s.settle(); }, READY_MS);
      s.open();
    }());
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function section(el, cred, entry, mode, label, chromeless) {
    var s = { mode: mode, entry: entry, armed: false, fallbackT: null, settle: function () {} };

    if (!chromeless) {
      var h = document.createElement('div');
      h.className = 'sgv-uiembed-label';
      h.textContent = label;
      el.appendChild(h);
    }

    s.note = document.createElement('p');
    s.note.className = 'sgv-app-note';
    if (chromeless) s.note.classList.add('sgv-app-note-quiet');
    s.note.textContent = 'Opening…';
    el.appendChild(s.note);

    s.say = function (html) { s.note.innerHTML = html; };

    s.frame = document.createElement('iframe');
    s.frame.className = 'sgv-embed-frame sgv-embed-ui';
    s.frame.setAttribute('allow', 'fullscreen');
    s.frame.setAttribute('allowfullscreen', '');
    s.frame.title = mode === 'app'
      ? label.replace(/^▶\s*/, '') + ', opened read-only'
      : 'The SG/Vault browser, opened read-only';
    el.appendChild(s.frame);

    s.open = function () {
      s.armed = true;
      s.say('Handshaking with the vault…');
      s.frame.src = ORIGIN + (mode === 'vault' ? '/en-gb/vault/' : '/en-gb/app/')
                  + '?embed=1&parent=' + encodeURIComponent(location.origin);
      clearTimeout(s.fallbackT);
      // If the handshake never lands, fall back to the fragment flow. That does put the key
      // in the frame's URL — which is why it is a FALLBACK and the page says it happened,
      // rather than the thing we do first.
      s.fallbackT = setTimeout(function () {
        s.frame.src = ORIGIN + '/#' + encodeURIComponent(cred);
        s.say('The embed handshake timed out, so this fell back to the URL-fragment flow. ' +
              'It still opens read-only.');
        s.settle();
      }, HANDSHAKE_MS);
    };
    return s;
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountAll);
  else mountAll();

  // For a frame created after load — the "Load a pack" control on /data/ builds a mount for
  // the pack the reader chose and hands it here. Same protocol, same pinned origin.
  window.SGVaultApp = { mount: mount, mountAll: mountAll };
}());
