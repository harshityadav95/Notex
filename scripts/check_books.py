"""Verify that imported chapters remain complete and their rendered media resolve."""
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
manifest = json.loads((ROOT / 'scripts/book-import.json').read_text())
index = json.loads((ROOT / 'docs/assets/search.json').read_text())

class Article(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.code_blocks = []
        self.in_pre = False
        self.ids = []
        self.fragments = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'pre':
            self.in_pre = True
            self.code_blocks.append('')
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'img':
            self.images.append(attrs['src'])
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.fragments.append(attrs['href'][1:])

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.in_pre = False
    def handle_data(self, data):
        if self.in_pre:
            self.code_blocks[-1] += data

count = 0
for series in manifest['series']:
    for chapter in series['chapters']:
        source = ROOT / 'src' / (chapter['slug'] + '.md')
        assert hashlib.sha256(source.read_bytes()).hexdigest() == chapter['sha256'], f'Changed source: {source}'
        assert source.stat().st_size == chapter['bytes']
        generated = ROOT / 'docs' / chapter['slug'] / 'index.html'
        rendered = generated.read_text()
        parser = Article()
        parser.feed(rendered)
        expected_code = re.findall(r'^```[^\n]*\n(.*?)^```', source.read_text(), re.M | re.S)
        assert [c.expandtabs(4).strip('\n') for c in expected_code] == [c.strip('\n') for c in parser.code_blocks], f'Code content changed: {source}'
        for image in parser.images:
            assert not urlsplit(image).scheme, f'Unexpected remote chapter media: {image}'
            assert (generated.parent / unquote(image)).resolve().is_file(), f'Missing media: {image}'
        assert set(parser.fragments) <= set(parser.ids), f'Broken section anchors: {source}'
        entry = next(x for x in index if x['url'] == chapter['slug'] + '/')
        assert entry['category'] == ('Languages' if series['key'] == 'go' else 'Systems')
        # The final prose must be searchable too; long chapters must never be truncated.
        if chapter['bytes'] > 140000:
            assert len(entry['text']) > 140000 or source.read_text().splitlines()[-1].lstrip('- ').strip() in entry['text']
        assert 'Original chapter ↗' in rendered
        assert 'aria-label="Chapter navigation"' in rendered
        count += 1
assert count == 20
print(f'Passed: {count} chapter hashes, source sizes, search categories, code blocks, section anchors, chapter navigation, and all chapter images.')
