"""Check exact legacy targets and downloadable evidence (stdlib only)."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json

ROOT = Path(__file__).resolve().parent


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refresh = self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('http-equiv') == 'refresh':
            self.refresh = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')


def main():
    config = json.loads((ROOT / 'routes.json').read_text())
    for name in config['html_files']:
        relative = name.removesuffix('index.html')
        expected = config['new_base'] + (relative or 'eng/')
        text = (ROOT / 'site' / name).read_text()
        head = Head()
        head.feed(text)
        assert head.refresh == '0; url=' + expected, name
        assert head.canonical == expected, name
        assert 'destination.search = current.search' in text, name
        assert 'destination.hash = current.hash' in text, name
        assert 'plausible' not in text, name
    manifest = json.loads((ROOT.parent / 'website/evidence-manifest.json').read_text())
    for name, digest in manifest.items():
        assert hashlib.sha256((ROOT / 'site' / name).read_bytes()).hexdigest() == digest, name
    print(json.dumps({'redirect_pages': len(config['html_files']),
                      'evidence_files': len(manifest), 'errors': []}))


if __name__ == '__main__':
    main()
