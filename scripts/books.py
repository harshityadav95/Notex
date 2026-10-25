"""Imported reading paths; provenance and hashes live in book-import.json."""
import html
import json
from pathlib import Path
from urllib.parse import quote

MANIFEST = json.loads(Path(__file__).with_name('book-import.json').read_text())
SERIES = MANIFEST['series']

def configure(groups, titles):
    for series, category in zip(SERIES, ('Languages', 'Systems')):
        slugs = [series['overview']] + [c['slug'] for c in series['chapters']]
        next(g for g in groups if g[0] == category)[5].extend(slugs)
        titles[series['overview']] = series['title']
        for chapter in series['chapters']:
            titles[chapter['slug']] = f"{series['key'].upper() if series['key'] == 'ddia' else 'Go'} {chapter['number']:02} · {chapter['title']}"

def context(slug, base):
    series = next((s for s in SERIES if slug == s['overview'] or any(c['slug'] == slug for c in s['chapters'])), None)
    if not series:
        return '', ''
    def link(target, label):
        return f'<a href="{base}{quote(target, safe="/")}/">{html.escape(label)}</a>'
    chapters = series['chapters']
    chapter = next((c for c in chapters if c['slug'] == slug), None)
    nav = '<nav class="chapter-navigation" aria-label="Chapter navigation">'
    if chapter:
        i = chapters.index(chapter)
        nav += link(chapters[i-1]['slug'], '← Previous chapter') if i else '<span>Start of collection</span>'
        nav += link(series['overview'], 'All chapters')
        nav += link(chapters[i+1]['slug'], 'Next chapter →') if i+1 < len(chapters) else '<span>End of collection</span>'
        graphic = f'<figure class="chapter-graphic"><div class="diagram-scroll" tabindex="0" role="region" aria-label="Chapter overview diagram"><img src="{base}{chapter["graphic"]}" alt="Conceptual overview for {html.escape(chapter["title"], quote=True)}" width="960" height="300"></div><figcaption>Original Notex overview. Source figure captions and descriptions are preserved below; original figure images are absent from the source repository.</figcaption></figure>'
        source = f'{MANIFEST["repository"]}/blob/{MANIFEST["revision"]}/{quote(chapter["source_path"])}'
        intro = f'<div class="source-credit">{link(series["overview"], series["title"])} · <a href="{source}">Original chapter ↗</a></div>' + graphic
    else:
        nav += link(chapters[0]['slug'], 'Start reading →')
        intro = f'<figure class="chapter-graphic"><div class="diagram-scroll" tabindex="0" role="region" aria-label="Chapter overview diagram"><img src="{base}{chapters[0]["graphic"]}" alt="{html.escape(series["title"], quote=True)} reading overview" width="960" height="300"></div></figure>'
    nav += '</nav>'
    return intro + nav, nav
