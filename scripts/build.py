#!/usr/bin/env python3
"""Build Notex as portable static HTML. Run: python scripts/build.py."""
from pathlib import Path
import html, json, re, shutil, hashlib
from urllib.parse import quote, unquote
import markdown
import landing
import books
from pygments.formatters import HtmlFormatter
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'src'; OUT=ROOT/'docs'; WEB=ROOT/'web'
GROUPS=[
 ('Languages','Programming languages','python','rose',['Python fundamentals and examples','JavaScript, ES6 and beyond','C++, CSS and language references'],['python','Javascript-ES6-Notes','C++','css']),
 ('Systems','System design in depth','Learning_System_Design','sage',['Architecture from first principles','Scalability and design tradeoffs','Cross-platform system design'],['Learning_System_Design','Scalable_crossplatform_design']),
 ('AI & ML','AI & machine learning','ai_ml_index','yellow',['Foundations and learning resources','Research, papers and practical tools','Explore the AI learning landscape'],['ai_ml_index','Research']),
 ('Databases','Databases & SQL','sql','blue',['SQL queries and data modeling','PostgreSQL and MongoDB','Relational and document databases'],['sql','postgresql','MongoDB']),
 ('Development','Tools for building','django','teal',['Django and web development','Git workflows and version control','Markdown, Vim and useful tools'],['django','git','markdownsyntax','vimCheats','Tools_Compilation']),
 ('Algorithms','Data structures & algorithms','dsalgo/dsalgoindex','purple',['Sorting and problem solving','Programming interview study plan','Practice with worked solutions'],['dsalgo/dsalgoindex','dsalgo/sorting','dsalgo/sol1','Programming_Interview_Study_Plan']),
 ('The garage','Terminal & hardware','terminal_commands','gray',['Commands worth keeping close','ThinkPad setup and experiments','A practical developer workspace'],['terminal_commands','thinkpad'])]
TITLES={'python':'Python','Javascript-ES6-Notes':'JavaScript & ES6','C++':'C / C++','css':'CSS','Learning_System_Design':'System Design from Scratch','Scalable_crossplatform_design':'Scalable Cross-platform Design','ai_ml_index':'AI & Machine Learning','Research':'Research','sql':'SQL','postgresql':'PostgreSQL','MongoDB':'MongoDB','django':'Django','git':'Git','markdownsyntax':'Markdown','vimCheats':'Vim Cheatsheet','Tools_Compilation':'Developer Tools','dsalgo/dsalgoindex':'Data Structures & Algorithms','dsalgo/sorting':'Sorting Algorithms','dsalgo/sol1':'Worked Solutions','Programming_Interview_Study_Plan':'Programming Interview Study Plan','terminal_commands':'Terminal Commands','thinkpad':'ThinkPad','404':'Page Not Found'}
books.configure(GROUPS, TITLES)
GROUPS[0][4][2] = 'Go, C++, CSS and language references'
GROUPS[1][4][2] = 'DDIA: data systems and distributed design'
REPO='https://github.com/harshityadav95/Notex'
def esc(s): return html.escape(str(s),quote=True)
def route(slug): return quote(slug,safe='/')+'/'
def anchor(base,slug,label,cls=''): return f'<a class="{cls}" href="{base}{route(slug)}">{esc(label)}</a>'
def footer(base):
 cols=''.join(f'<div><h3>{esc(g[0])}</h3>'+''.join(anchor(base,s,TITLES[s]) for s in g[5] if '/chapter-' not in s)+ '</div>' for g in GROUPS[:5])
 return f'''<footer><div class="footer-top wrap"><div class="footer-brand"><a class="wordmark" href="{base}">notex<span class="badge">OPEN</span></a><p>A personal library for deliberate<br>technical practice.</p><a href="{REPO}">Explore the source ↗</a></div><div class="footer-links">{cols}</div></div><div class="footer-bottom wrap"><span>© 2026 Notex · Open knowledge, shared freely.</span><a href="{base}licenses/">Licenses & credits</a><span>Designed by <a href="https://harshityadav.in">harshityadav.in</a></span></div></footer>'''
def header(base):
 return f'''<a class="skip" href="#main-content">Skip to content</a><div class="announcement"><a href="{base}library/"><span class="badge live">OPEN</span> Your next idea starts with a note <span class="announcement-more">Explore the library →</span></a><button aria-label="Dismiss announcement" data-dismiss>×</button></div><header class="site-header"><div class="nav-wrap"><a class="wordmark" href="{base}">notex<span class="badge">OPEN</span></a><nav aria-label="Main navigation"><div class="dropdown"><button aria-expanded="false" data-dropdown>Learning <span>⌄</span></button><div class="dropdown-panel">{''.join(anchor(base,g[2],g[1]) for g in GROUPS)}</div></div><a href="{base}library/">Library</a><a href="{base}library/#handwritten">Handwritten</a><a href="{base}library/#notebooks">Notebooks</a><div class="dropdown"><button aria-expanded="false" data-dropdown>Explore <span>⌄</span></button><div class="dropdown-panel"><a href="{base}#paths">Learning paths</a><a href="{base}#about">About Notex</a>{anchor(base,'Research','Research')}{anchor(base,'Tools_Compilation','Developer tools')}</div></div><a href="{REPO}">GitHub ↗</a></nav><div class="nav-actions"><a class="pill open-source" href="{REPO}">100% open source ↗</a><button class="search-trigger tactile" aria-label="Search notes" data-search><img src="{base}assets/icons/search.svg" alt="" width="18" height="18"></button><a class="tactile desktop-start" href="{base}python/">Start reading</a><button class="tactile menu-trigger" aria-label="Open navigation menu" data-menu><img src="{base}assets/icons/menu.svg" alt="" width="16" height="16"> Menu</button></div></div></header><dialog class="menu-dialog"><div class="menu-head"><span class="wordmark">notex</span><button aria-label="Close menu" data-close>×</button></div><p>Notes, code and ideas. All in one place.</p><nav aria-label="Mobile navigation"><a href="{base}library/">All notes</a><a href="{base}library/#handwritten">Handwritten notes</a><a href="{base}library/#notebooks">Python notebooks</a><a href="{base}#about">About Notex</a>{''.join(anchor(base,g[2],g[1]) for g in GROUPS)}<a href="{REPO}">GitHub ↗</a></nav></dialog>'''
def shell(title,body,base='./',kind='home'):
 css_version=hashlib.sha256((WEB/'assets/style.css').read_bytes()).hexdigest()[:10]
 js_version=hashlib.sha256((WEB/'assets/app.js').read_bytes()).hexdigest()[:10]
 landing_version=hashlib.sha256((WEB/'assets/landing.css').read_bytes()).hexdigest()[:10]
 landing_styles=f'<link rel="stylesheet" href="{base}assets/landing.css?v={landing_version}">' if kind=='home' else ''
 page_header=landing.header(base,GROUPS) if kind=='home' else header(base)
 page_footer=landing.footer(base,GROUPS) if kind=='home' else footer(base)
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Notex: open notes, code snippets, system design, programming languages and handwritten resources by Harshit Yadav."><meta name="theme-color" content="#f7f7f8"><title>{esc(title)} · Notex</title><link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{base}assets/style.css?v={css_version}"><link rel="stylesheet" href="{base}assets/highlight.css">{landing_styles}<script src="{base}assets/app.js?v={js_version}" defer></script></head><body class="{kind}" data-base="{base}">{page_header}{body}{page_footer}<dialog class="search-dialog"><div class="search-top"><span>⌕</span><input type="search" placeholder="Search notes, topics, code…" aria-label="Search the library" autocomplete="off"><button aria-label="Close search" data-close>Esc</button></div><div class="search-hint">Search across the entire library <kbd>⌘ K</kbd></div><div id="search-results" aria-live="polite"></div></dialog><div class="toast" role="status"></div></body></html>'''
OUT.mkdir(exist_ok=True)
shutil.copytree(WEB/'assets',OUT/'assets',dirs_exist_ok=True)
(OUT/'assets/highlight.css').write_text(HtmlFormatter(style='friendly').get_style_defs('.codehilite'))
# Preserve every source attachment with its existing relative path.
for p in SRC.rglob('*'):
 if p.is_file() and p.suffix!='.md' and not any(part.startswith('.') for part in p.relative_to(SRC).parts):
  dest=OUT/p.relative_to(SRC);dest.parent.mkdir(parents=True,exist_ok=True)
  if not dest.exists() or (p.stat().st_size,p.stat().st_mtime_ns)!=(dest.stat().st_size,dest.stat().st_mtime_ns): shutil.copy2(p,dest)
index=[]
for p in SRC.rglob('*.md'):
 slug=p.relative_to(SRC).with_suffix('').as_posix()
 if slug=='index': continue
 title=TITLES.get(slug,slug)
 group=next((g for g in GROUPS if slug in g[5]),GROUPS[0]); base='../'*(len(Path(slug).parts)+0)
 text=p.read_text(); text=re.sub(r'\((?:\.\./)*Readme\.md\)', '('+base+')', text, flags=re.I); text=text.replace('(harshityadav.in)', '(https://harshityadav.in)'); md=markdown.Markdown(extensions=['extra','toc','sane_lists','codehilite'],extension_configs={'codehilite':{'guess_lang':False,'use_pygments':slug.startswith(('go/', 'ddia/'))}})
 content=md.convert(text)
 # Rebase existing Markdown links and attachments, including raw HTML links.
 def fixlink(m):
  attr,url=m.group(1),html.unescape(m.group(2))
  if url == base: return m.group(0)
  if re.match(r'^(https?:|mailto:|data:|#|//)',url): return m.group(0)
  target=(p.parent/unquote(url.split('#')[0])).resolve()
  try: rel=target.relative_to(SRC.resolve()).as_posix()
  except ValueError: return m.group(0)
  frag='#'+url.split('#',1)[1] if '#' in url else ''
  if rel.endswith('.md'): rel=route(rel[:-3]) if rel!='index.md' else ''
  else: rel=quote(rel,safe='/')
  return f'{attr}="{base}{rel}{frag}"'
 content=re.sub(r'(href|src)="([^"]*)"',fixlink,content)
 plain=re.sub('<[^>]+>',' ',re.sub(r'</?span[^>]*>', '', content)); plain=re.sub(r'\s+',' ',html.unescape(plain))
 index.append({'title':title,'url':route(slug),'category':group[0],'text':plain})
 # Keep a single page heading while preserving source anchors.
 first_heading=re.search(r'<h1 id="([^"]+)">(.*?)</h1>',content,re.S)
 heading_id=''
 if first_heading:
  normalize=lambda value: re.sub(r'[^a-z0-9]','',html.unescape(re.sub('<[^>]+>','',value)).lower())
  if normalize(first_heading.group(2))==normalize(title):
   heading_id=f' id="{first_heading.group(1)}"'
   content=content[:first_heading.start()]+content[first_heading.end():]
 content=re.sub(r'<(/?)h1(?=[ >])',r'<\1h2',content)
 sidebar='<a class="sidebar-overview" href="'+base+'library/">← All notes</a><p class="eyebrow">WORKSPACE</p>'
 for g in GROUPS:
  sidebar+=f'<details {"open" if slug in g[5] else ""}><summary>{esc(g[0])}<span>{len(g[5]):02}</span></summary>'+''.join(anchor(base,s,TITLES[s], 'active' if s==slug else '') for s in g[5])+'</details>'
 sidebar+=f'<div class="sidebar-foot">FREE TO READ · OPEN TO EVERYONE</div>'
 readtime=max(1,round(len(plain.split())/220))
 chapter_intro, chapter_nav = books.context(slug, base)
 body=f'''<div class="reader-bar"><button class="tactile" data-sidebar aria-expanded="false">☰ Topics</button><a href="{base}">Notex</a><span>/</span><span>{esc(group[0])}</span><span>/</span><strong>{esc(title)}</strong></div><div class="reader-layout"><aside class="sidebar" aria-label="Topic navigation">{sidebar}</aside><main id="main-content" class="reader-main"><div class="article-meta"><span class="eyebrow">{esc(group[0])} / NOTES</span><span>{readtime} MIN READ</span></div><h1 class="article-title"{heading_id}>{esc(title)}</h1><div class="article-actions"><button class="tactile" data-save="{esc(route(slug))}" aria-pressed="false">Save note</button><a href="{REPO}/blob/main/src/{quote(slug,safe='/')}.md">Edit on GitHub ↗</a><span>Always free to read</span></div><div class="article-layout"><article class="prose">{chapter_intro}{content}{chapter_nav}</article><aside class="article-toc"><span class="eyebrow">ON THIS PAGE</span>{md.toc}</aside></div><div class="article-end"><span class="eyebrow">KEEP EXPLORING</span><h2>One note leads to another.</h2><a class="tactile" href="{base}library/">Back to the library →</a></div></main></div>'''
 dest=OUT/slug/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(shell(title,body,base,'reading'))
index.sort(key=lambda x:(next((i for i,g in enumerate(GROUPS) if g[0]==x['category']),99),x['title']))
(OUT/'assets/search.json').write_text(json.dumps(index,ensure_ascii=False))
library=''.join(f'<a class="note-row" data-category="{esc(x["category"])}" data-url="{esc(x["url"])}" href="{x["url"]}"><span class="note-index">{i+1:02}</span><span>{esc(x["title"])}</span><small>{esc(x["category"])}</small><span>↗</span></a>' for i,x in enumerate(x for x in index if x['title']!='Page Not Found'))
files=''.join(f'<a class="resource-row" href="{quote(p.relative_to(SRC).as_posix())}"><span>PDF</span><strong>{esc(p.stem)}</strong><span>↗</span></a>' for p in sorted((SRC/'handwritten notes').glob('*.pdf')))
references=''.join(f'<a class="resource-row" href="{quote(p.relative_to(SRC).as_posix())}"><span>PDF</span><strong>{esc(p.stem)}</strong><span>↗</span></a>' for p in sorted(SRC.rglob('*.pdf')) if 'handwritten notes' not in p.parts)
notebooks=''.join(f'<a class="resource-row" href="{REPO}/blob/main/src/{quote(p.name)}"><span>IPYNB</span><strong>{esc(p.stem)}</strong><span>↗</span></a>' for p in sorted(SRC.glob('*.ipynb')))
archive=f'''<section class="wrap library" id="library"><div class="section-heading"><div><p class="eyebrow">THE COMPLETE COLLECTION</p><h2>Everything on <span class="mono">notex.</span></h2></div><button class="tactile" data-search>Search the library <kbd>⌘ K</kbd></button></div><div class="filter-bar" role="group" aria-label="Filter library"><button class="active" data-filter="all" aria-pressed="true">All notes</button>{''.join(f'<button data-filter="{esc(g[0])}" aria-pressed="false">{esc(g[0])}</button>' for g in GROUPS)}<button data-filter="saved" aria-pressed="false">Saved</button></div><div class="note-list">{library}</div><p class="empty-state" hidden>No saved notes yet. Open a note and select “Save note” to keep it here.</p></section><section class="wrap resource-section"><div id="handwritten"><p class="eyebrow">OFF THE KEYBOARD</p><h2>Handwritten notes.</h2><p class="muted">The original pages. Computer science, one page at a time.</p><div class="resource-list">{files}</div><h3 class="reference-heading">Reference shelf</h3><div class="resource-list">{references}</div></div><div id="notebooks"><p class="eyebrow">LEARN BY DOING</p><h2>Open a notebook.</h2><p class="muted">Python experiments and examples. Preview on GitHub.</p><div class="resource-list">{notebooks}</div></div></section>'''
# The complete archive lives on its own page so the landing page follows the reference composition.
def archive_href(match):
 value=match.group(1)
 return 'href="'+(value if re.match(r'^(https?:|mailto:|#|/)',value) else '../'+value)+'"'
archive=re.sub(r'href="([^"]+)"',archive_href,archive)
archive=archive.replace('<h2>Everything on <span class="mono">notex.</span></h2>','<h1>The complete library.</h1>')
archive='<main id="main-content">'+archive+'</main>'
(OUT/'library').mkdir(exist_ok=True)
(OUT/'library/index.html').write_text(shell('The complete library',archive,'../','library-page'))
body=landing.render(GROUPS,index)
(OUT/'index.html').write_text(shell('Technical learning, mapped',body))
license_body='<main class="wrap legal" id="main-content"><p class="eyebrow">OPEN SOURCE</p><h1>Licenses & credits</h1><p>The Notex website code is licensed under MIT. Existing notes and attachments retain their authorship and any original third-party licenses. External resources belong to their respective authors.</p><p>The visual direction references <a href="https://fanout.sh">fanout.sh</a>. Fanout branding, course content and proprietary artwork are not distributed with this website.</p><h2>Imported book notes</h2><p>Go and Designing Data-Intensive Applications notes are imported from <a href="https://github.com/harshityadav95/FAANG_BOOKS">FAANG_BOOKS</a>. Original text retains its respective authorship and rights. Original book figure files are absent upstream; Notex provides original conceptual overview diagrams alongside preserved descriptions.</p><h2>Artwork & icons</h2><p>Original Notex notebook artwork was generated for this project. Interface icons are from Phosphor Icons (MIT).</p><a href="../assets/icons/LICENSE">Phosphor Icons license</a><h2>Bundled open-source fonts</h2><p>Overused Grotesk by RandomMaerks — SIL Open Font License 1.1. Departure Mono by Helena Zhang and Tobias Fried — MIT.</p><a href="../assets/fonts/Overused-OFL.txt">Overused Grotesk license</a><br><a href="../assets/fonts/Departure-LICENSE.txt">Departure Mono license</a></main>'
(OUT/'licenses').mkdir(exist_ok=True);(OUT/'licenses/index.html').write_text(shell('Licenses & credits',license_body,'../','legal-page'))
(OUT/'.nojekyll').touch()
print(f'Built {len(index)} note pages, {len(list(SRC.rglob("*.pdf")))} PDFs and {len(list(SRC.glob("*.ipynb")))} notebooks into docs/.')
