"""Verify that imported chapters remain complete and their rendered media resolve."""
import hashlib
import json
import re
import study_notes
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
        assert [study_notes.code(c).expandtabs(4).strip('\n') for c in expected_code] == [c.strip('\n') for c in parser.code_blocks], f'Code content changed: {source}'
        for image in parser.images:
            assert not urlsplit(image).scheme, f'Unexpected remote chapter media: {image}'
            assert (generated.parent / unquote(image)).resolve().is_file(), f'Missing media: {image}'
        assert set(parser.fragments) <= set(parser.ids), f'Broken section anchors: {source}'
        entry = next(x for x in index if x['url'] == chapter['slug'] + '/')
        assert entry['category'] == ('Languages' if series['key'] == 'go' else 'Systems')
        assert not re.search(r"o[’' -]?reilly|oreilly\.com|FAANG_BOOKS|Early Release|learning-go-book",rendered,re.I),f'Publishing metadata remains: {source}'
        assert 'Original chapter ↗' not in rendered
        assert 'aria-label="Chapter navigation"' in rendered
        count += 1
assert count == 20
print(f'Passed: {count} chapter hashes, source sizes, search categories, code blocks, section anchors, chapter navigation, and all chapter images.')

# Each guided lesson must retain its extracted code and resolve every section anchor.
import books
lesson_count=0
for track in books.SERIES:
    for module in track['modules']:
        combined=[]
        for lesson in module['lessons']:
            file=ROOT/'docs'/lesson['slug']/'index.html'
            parser=Article();parser.feed(file.read_text())
            expected=re.findall(r'^```[^\n]*\n(.*?)^```',lesson['text'],re.M|re.S)
            if track['key']=='distributed-systems':
                source_parser=Article();source_parser.feed(lesson['text']);expected=source_parser.code_blocks
            assert [c.expandtabs(4).strip('\n') for c in expected]==[c.strip('\n') for c in parser.code_blocks],f'Lesson code changed: {lesson["slug"]}'
            assert set(parser.fragments)<=set(parser.ids),f'Lesson anchors broken: {lesson["slug"]}'
            assert 'A Note for Early Release Readers' not in file.read_text()
            assert '- table of contents' not in lesson['text']
            assert not re.search(r"o[’' -]?reilly|oreilly\.com|FAANG_BOOKS|Early Release|learning-go-book|About the source material|Original source ↗",file.read_text(),re.I),f'Publishing metadata remains: {lesson["slug"]}'
            combined.extend(expected)
            lesson_count+=1
        original=ROOT/'src'/(module['chapter']['slug']+'.md')
        expected=re.findall(r'^```[^\n]*\n(.*?)^```',original.read_text(),re.M|re.S)
        if track['key']=='distributed-systems':
            source_parser=Article();source_parser.feed(original.read_text());expected=source_parser.code_blocks
        assert combined==([study_notes.code(c) for c in expected] if track['key']!='distributed-systems' else expected),f'Code omitted or duplicated while splitting {original}'
assert lesson_count==sum(len(t['lessons']) for t in books.SERIES)
print(f'Passed: {lesson_count} guided lessons retain every source code block, omit publishing/navigation boilerplate, and have valid section anchors.')

# Keep publishing/import metadata out of all public course pages and search text.
for folder in ('go','ddia'):
    for file in (ROOT/'docs'/folder).rglob('index.html'):
        assert not re.search(r"o[’' -]?reilly|oreilly\.com|FAANG_BOOKS|Early Release|learning-go-book|About the source material|Original source ↗",file.read_text(),re.I),f'Publishing metadata remains in {file}'
for entry in index:
    if entry['url'].startswith(('go/','ddia/')):
        assert not re.search(r"o[’' -]?reilly|oreilly\.com|FAANG_BOOKS|Early Release|learning-go-book",entry['text'],re.I)
print('Passed: public study pages and search entries contain no publisher/import metadata.')

# Numeric array values are study content, not bibliography markers.
go_track=next(t for t in books.SERIES if t['key']=='go')
for module in go_track['modules']:
    original=(ROOT/'src'/(module['chapter']['slug']+'.md')).read_text()
    derived='\n'.join(l['text'] for l in module['lessons'])
    for literal in re.findall(r'\[(?:\d+,\s*){2,}\d+\]',original):
        assert literal in derived,f'Numeric example lost in {module["title"]}: {literal}'
print('Passed: bracketed numeric Go examples remain intact.')

# The supplied PDF's imported chapters and diagram bytes must remain intact.
distributed=json.loads((ROOT/'scripts/distributed-import.json').read_text())
track=next(t for t in books.SERIES if t['key']=='distributed-systems')
assert len(track['modules'])==6 and len(track['lessons'])==39
for slug,sha in distributed['sources'].items():
    assert hashlib.sha256((ROOT/'src'/(slug+'.md')).read_bytes()).hexdigest()==sha
for figure in distributed['figures']:
    for folder in ('web','docs'):
        path=ROOT/folder/'assets/distributed-systems'/figure['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==figure['sha256']
assert len(distributed['figures'])==85
for lesson in track['lessons']:
    content=(ROOT/'docs'/lesson['slug']/'index.html').read_text()
    assert content.count('class="chapter-video"')==1
    assert 'data-theme-toggle' in content
    assert not re.search('Understanding Distributed Systems|Roberto Vitillo',content,re.I)
    parser=Article();parser.feed(content)
    for image in parser.images:
        assert (ROOT/'docs'/lesson['slug']/unquote(image)).resolve().is_file(),image
print('Passed: 6 distributed systems modules, 39 video placeholders, preserved chapter hashes, and 85 byte-identical original diagrams.')
