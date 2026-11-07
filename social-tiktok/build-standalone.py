"""Build a portable tracker with no neighboring-file dependencies.
Reads approved brand assets unchanged. Writes only inside social-tiktok/.
"""
from pathlib import Path
from base64 import b64encode
from html import escape
import json, zipfile
ROOT = Path(__file__).resolve().parent

def asset(name, mime):
    return 'data:' + mime + ';base64,' + b64encode((ROOT.parent / 'brand' / name).read_bytes()).decode()

html = (ROOT / 'index.html').read_text()
html = html.replace('href="../brand/logo-icon.svg"', 'href="' + asset('logo-icon.svg', 'image/svg+xml') + '"')
html = html.replace('src="../brand/logo.svg"', 'src="' + asset('logo.svg', 'image/svg+xml') + '"')
css = (ROOT.parent / 'brand' / 'brand.css').read_text() + '\n' + (ROOT / 'tracker.css').read_text()
css += '\n#document-dialog {width:min(900px,calc(100% - 24px))} #document-copy {white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;line-height:1.7;}\n'
html = html.replace('<link rel="stylesheet" href="../brand/brand.css"><link rel="stylesheet" href="tracker.css">', '<style>\n' + css + '\n</style>')
html = html.replace('<script src="content.js" defer></script><script src="tracker.js" defer></script>', '')
# Make documentation links work even when this is the only file downloaded.
docs = ['profile-and-strategy.md', 'content-calendar.md', 'video-scripts.md', 'README.md']
for name in docs:
    html = html.replace('href="' + name + '"', 'href="#document" data-document="' + name + '"')
csv_url = 'data:text/csv;base64,' + b64encode((ROOT / 'content-calendar.csv').read_bytes()).decode()
html = html.replace('href="content-calendar.csv" download', 'href="' + csv_url + '" download="content-calendar.csv"')
html = html.replace('</body>', '<dialog id="document-dialog" aria-labelledby="document-title"><div class="dialog-heading"><h2 id="document-title">Reference document</h2><button id="close-document" aria-label="Close document">✕</button></div><pre id="document-copy"></pre></dialog>\n</body>')
doc_json = json.dumps({name: (ROOT/name).read_text() for name in docs}, ensure_ascii=False).replace('<', '\\u003c')
script = (ROOT/'content.js').read_text() + '\n' + (ROOT/'tracker.js').read_text()
script += '\n(() => {\nconst docs = ' + doc_json + ''';
document.addEventListener('click', e => {
  const link = e.target.closest('[data-document]');
  if (!link) return;
  e.preventDefault();
  document.querySelector('#document-title').textContent = link.dataset.document;
  document.querySelector('#document-copy').textContent = docs[link.dataset.document];
  document.querySelector('#document-dialog').showModal();
});
document.querySelector('#close-document').addEventListener('click', () => document.querySelector('#document-dialog').close());
})();
'''
# Put scripts after the DOM, since inlined classic scripts do not honor defer.
assert '</script' not in script.lower(), 'Inline script needs HTML escaping before bundling.'
html = html.replace('</body>', '<script>\n' + script + '\n</script>\n</body>')
(ROOT/'profitlane-tiktok-standalone.html').write_text(html)
with zipfile.ZipFile(ROOT/'profitlane-tiktok-download.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    z.write(ROOT/'profitlane-tiktok-standalone.html','OPEN-TRACKER.html')
    z.writestr('START-HERE.txt', 'ProfitLane TikTok tracker\n\n1. Extract this ZIP.\n2. Double-click OPEN-TRACKER.html to open it in Chrome, Edge, Firefox or Safari with JavaScript enabled. No install or server is required.\n3. Use Export backup regularly. Browser storage is local to the browser and file location. Keep the HTML in the same place for future use.\n\nChat file previews may not run interactive HTML. Download and open the file in a regular browser. All sample results are fictional. No TikTok account is connected.\n\nAll CSS, JavaScript, approved logo assets and reference documents are embedded unchanged from the repository sources.\n')
    for name in docs+['content-calendar.csv']:
        z.write(ROOT/name,name)
print('Built self-contained tracker and download ZIP inside social-tiktok/.')
