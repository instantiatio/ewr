"""Build the static compatibility site still served under /iEWR/."""
from pathlib import Path
from html import escape
import json
import shutil

ROOT = Path(__file__).resolve().parent


def redirect_html(target, old_base, new_base):
    # Fixed origins; only the old path, query and fragment cross the boundary.
    script = '''const oldBase = new URL(OLD_BASE);
const newBase = new URL(NEW_BASE);
const current = new URL(window.location.href);
let suffix = current.pathname.startsWith(oldBase.pathname)
  ? current.pathname.slice(oldBase.pathname.length) : "";
if (suffix.endsWith("index.html")) suffix = suffix.slice(0, -10);
if (!suffix) suffix = "eng/";
const destination = new URL(newBase.href + suffix);
destination.search = current.search;
destination.hash = current.hash;
document.getElementById("destination").href = destination.href;
window.location.replace(destination.href);'''.replace('OLD_BASE', json.dumps(old_base)).replace('NEW_BASE', json.dumps(new_base))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,follow">
<title>Instantiatio — page moved / Страница перенесена</title>
<link rel="canonical" href="{escape(target, quote=True)}">
<meta http-equiv="refresh" content="0; url={escape(target, quote=True)}">
</head><body><p>This page has moved. / Страница перенесена.</p>
<p><a id="destination" href="{escape(target, quote=True)}">Continue / Перейти</a></p>
<script>{script}</script></body></html>'''


def main():
    config = json.loads((ROOT / 'routes.json').read_text())
    site = ROOT / 'site'
    if site.exists():
        shutil.rmtree(site)
    site.mkdir()
    for name in config['html_files']:
        relative = name.removesuffix('index.html')
        target = config['new_base'] + (relative or 'eng/')
        page = site / name
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(redirect_html(target, config['old_base'], config['new_base']))
    (site / '404.html').write_text(redirect_html(config['new_base'] + 'eng/', config['old_base'], config['new_base']))
    # PDFs, ZIPs, images and fonts cannot be forwarded using an HTML document.
    # Keep downloads and cached pages usable without retaining site source in iEWR.
    shutil.copytree(ROOT.parent / 'website/assets', site / 'assets',
                    ignore=shutil.ignore_patterns('.DS_Store', '._*'))
    (site / '.nojekyll').touch()
    (site / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + config['new_base'] + 'sitemap.xml\n')
    (site / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        '<sitemap><loc>' + config['new_base'] + 'sitemap.xml</loc></sitemap></sitemapindex>\n')
    print(f'Built {len(config["html_files"])} legacy redirect pages, fallback and compatible assets')


if __name__ == '__main__':
    main()
