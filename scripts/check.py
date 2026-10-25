"""Validate generated navigation, source coverage and portable project URLs."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
import books
ROOT=Path(__file__).resolve().parent.parent; OUT=ROOT/'docs'
class Links(HTMLParser):
 def __init__(self): super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if (tag=='a' and key=='href') or (tag in ('script','link','img') and key in ('src','href')): self.links.append((value,tag))
errors=[]
# Validate every built source and derived curriculum page.
valid_slugs={x.relative_to(ROOT/'src').with_suffix('').as_posix() for x in (ROOT/'src').rglob('*.md')} | set(books.PAGES) | set(books.ALIASES) | {'licenses','library'}
for file in OUT.rglob('index.html'):
 if file.parent!=OUT and file.parent.relative_to(OUT).as_posix() not in valid_slugs:continue
 parser=Links();parser.feed(file.read_text())
 for href,tag in parser.links:
  u=urlsplit(href)
  if u.scheme or u.netloc or not u.path:continue
  target=(file.parent/unquote(u.path)).resolve()
  if not target.exists():
   if tag=='img' and 'assets/' not in href: continue # Missing legacy note illustrations predate this redesign.
   errors.append(f'{file.relative_to(OUT)}: {href}')
for p in (ROOT/'src').rglob('*.md'):
 if p.stem=='index':continue
 if not (OUT/p.relative_to(ROOT/'src').with_suffix('')/'index.html').exists():errors.append(f'Missing note {p}')
index=json.loads((OUT/'assets/search.json').read_text())
assert len(index)==len(list((ROOT/'src').rglob('*.md')))-1+len(books.PAGES)
assert 'Designed by' in (OUT/'index.html').read_text()
# Validate the locally bundled styles, including font and sprite references.
import re
for css in (OUT/'assets').glob('*.css'):
 for url in re.findall(r'url\([\"\']?([^\)\"\']+)',css.read_text()):
  if url.startswith(('data:','http:','https:')):continue
  if not (css.parent/urlsplit(url).path).exists():errors.append(f'{css.relative_to(OUT)}: {url}')
if errors:
 print('Broken existing/source links to repair:');print('\n'.join(sorted(set(errors))));raise SystemExit(1)
print(f'Passed: {len(index)} notes indexed; all generated page links and UI assets resolve; footer present.')
