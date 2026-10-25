"""Book references and guided curricula derived from preserved source chapters."""
import html
import json
import re
from pathlib import Path
from urllib.parse import quote
import curriculum
import study_notes

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads(Path(__file__).with_name('book-import.json').read_text())
SERIES = MANIFEST['series']
PAGES = curriculum.prepare(SERIES, ROOT/'src')
ALIASES = {
    'ddia/modules/01-preface':'ddia/modules/01-study-guide',
    'ddia/lessons/00-01-who-should-read-this-book':'ddia/lessons/00-01-study-goals',
    'ddia/lessons/00-02-whats-new-in-the-second-edition':'ddia/lessons/00-02-topics-in-this-learning-path',
    'ddia/lessons/00-03-references-and-further-reading':'ddia/lessons/00-03-a-practical-study-method',
}

def e(value): return html.escape(str(value), quote=True)
def url(base,slug): return base+quote(slug,safe='/')+'/'
def track_for(slug):
    return next((s for s in SERIES if slug.startswith(s['key']+'/')), None)
def page_kind(slug):
    if slug in PAGES:return PAGES[slug]['kind']
    if slug.endswith('/overview') and track_for(slug):return 'overview'
    return 'reference' if track_for(slug) else 'note'
def configure(groups, titles):
    for series, category in zip(SERIES, ('Languages', 'Systems')):
        slugs = [series['overview']] + [c['slug'] for c in series['chapters']]
        next(g for g in groups if g[0] == category)[5].extend(slugs)
        titles[series['overview']] = series['title']
        for chapter in series['chapters']:
            display_title=chapter['module']['title']
            titles[chapter['slug']] = f"{series['key'].upper() if series['key'] == 'ddia' else 'Go'} {chapter['number']:02} · {display_title}"
        titles.update({p['slug']:p['title'] for p in PAGES.values() if p['series'] is series})

def section_label(track, module):
    n=module['chapter']['number']
    if track['key']=='go':return 'GO / CORE LANGUAGE'
    if n==0:return 'START HERE'
    if n<=5:return 'PART 1 / DATA FOUNDATIONS'
    if n<=10:return 'PART 2 / DISTRIBUTED SYSTEMS'
    return 'PART 3 / PROCESSING & RESPONSIBILITY'

def header(base, track):
    choices=''.join(f'<a href="{url(base,s["overview"])}">{e(s["title"])}</a>' for s in SERIES)
    return f'''<a class="skip" href="#main-content">Skip to content</a><header class="course-header"><a class="wordmark" href="{base}">notex<span class="badge">OPEN</span></a><span class="course-header-divider"></span><div class="dropdown"><button data-dropdown aria-expanded="false">{e('Learning Go' if track['key']=='go' else 'Data-intensive applications')} <span>⌄</span></button><div class="dropdown-panel">{choices}<a href="{base}library/">All notes</a></div></div><a class="course-header-overview" href="{url(base,track['overview'])}">Overview</a><div class="nav-actions"><button class="search-trigger tactile" aria-label="Search notes" data-search><img src="{base}assets/icons/search.svg" alt="" width="18" height="18"></button><a class="tactile course-library-link" href="{base}library/">Library ↗</a><button class="tactile menu-trigger" aria-label="Open navigation menu" data-menu>Menu</button></div></header><dialog class="menu-dialog"><div class="menu-head"><span class="wordmark">notex</span><button aria-label="Close menu" data-close>×</button></div><nav aria-label="Mobile navigation">{choices}<a href="{base}library/">All notes</a></nav></dialog>'''

def sidebar(slug,base):
    track=track_for(slug)
    if not track:return None
    current=PAGES.get(slug,{}).get('module')
    out=f'<a class="sidebar-overview" href="{base}library/">← All notes</a><p class="eyebrow">WORKSPACE</p><a class="course-overview-link {"active" if slug==track["overview"] else ""}" href="{url(base,track["overview"])}">Course overview</a><div class="course-access"><strong>{len(track["lessons"])} lessons · all open</strong><span>Read, practice, and keep your place.</span></div>'
    part=None
    for module in track['modules']:
        label=section_label(track,module)
        if label!=part:out+=f'<p class="eyebrow syllabus-part">{label}</p>';part=label
        out+=f'<details class="syllabus-module" {"open" if module is current else ""}><summary><span class="module-num">{module["number"]:02}</span><strong>{e(module["title"])}</strong><span>{len(module["lessons"])}</span></summary><a class="module-start {"active" if slug==module["slug"] else ""}" href="{url(base,module["slug"])}">Module overview →</a>'
        for lesson in module['lessons']:
            out+=f'<a class="syllabus-lesson {"active" if slug==lesson["slug"] else ""}" href="{url(base,lesson["slug"])}" data-lesson-link="{e(lesson["slug"])}"><span>{lesson["code"]}</span>{e(lesson["title"])}</a>'
        out+='</details>'
    out+=f'<div class="sidebar-foot" data-course-progress="{track["key"]}" data-course-total="{len(track["lessons"])}">0 / {len(track["lessons"])} LESSONS COMPLETE</div>'
    return out

def rows(module,base):
    out='<ol class="lesson-list">'
    for lesson in module['lessons']:
        tag='PRACTICE' if lesson['kind']=='practice' else 'READING'
        out+=f'<li data-lesson-kind="{lesson["kind"]}"><a class="lesson-row" href="{url(base,lesson["slug"])}" data-lesson-link="{lesson["slug"]}"><span class="lesson-number">{lesson["code"]}</span><span class="lesson-copy"><strong>{e(lesson["title"])}</strong><span>{e(lesson["summary"])}</span></span><span class="lesson-meta"><small>{tag}</small><span>{lesson["minutes"]} MIN</span></span><span class="lesson-arrow" aria-hidden="true">→</span></a></li>'
    return out+'</ol>'

def module_panel(track,module,base):
    total=sum(x['minutes'] for x in module['lessons'])
    return f'<section class="curriculum-module" id="module-{module["number"]:02}"><div class="module-heading"><span class="module-num">{module["number"]:02}</span><div><p class="eyebrow">{section_label(track,module)}</p><h2><a href="{url(base,module["slug"])}">{e(module["title"])}</a></h2></div><span class="module-count">{len(module["lessons"])} LESSONS · {total} MIN</span></div>{rows(module,base)}</section>'

def overview(slug,base):
    track=track_for(slug)
    first=track['lessons'][0]
    structure=''.join(f'<a href="#module-{m["number"]:02}"><span>{m["number"]:02}</span><strong>{e(m["title"])}</strong><small>{len(m["lessons"])} LESSONS</small><b aria-hidden="true">→</b></a>' for m in track['modules'])
    panels=''.join(module_panel(track,m,base) for m in track['modules'])

    return f'''<section class="course-hero"><div><p class="eyebrow">OPEN LEARNING PATH / {'GO' if track['key']=='go' else 'DDIA'}</p><h1>{e(track['headline'])}</h1><p>{e(track['description'])}</p><span class="course-stats">{len(track['modules'])} MODULES <span>·</span> {len(track['lessons'])} LESSONS <span>·</span> FREE TO READ</span></div><img class="course-book" src="{base}assets/books/{track['key']}-notebook.webp" alt="{e(track['title'])} textured notebook cover" width="1254" height="1254"></section><div class="course-start"><div><strong>A little progress, one lesson at a time.</strong><span data-course-resume-label="{track['key']}">Your progress stays in this browser.</span></div><a class="tactile" href="{url(base,first['slug'])}" data-course-resume="{track['key']}">Start learning →</a></div><section class="curriculum-structure" aria-labelledby="curriculum-structure"><h2 class="eyebrow" id="curriculum-structure">CURRICULUM STRUCTURE</h2><nav class="module-directory" aria-label="Module directory">{structure}</nav></section><div class="curriculum-toolbar"><h2>Full curriculum</h2><div role="group" aria-label="Filter lessons"><button class="active" data-lesson-filter="all" aria-pressed="true">All lessons</button><button data-lesson-filter="reading" aria-pressed="false">Reading</button><button data-lesson-filter="practice" aria-pressed="false">Practice</button></div><div role="group" aria-label="Curriculum layout"><button class="active" data-curriculum-layout="list" aria-pressed="true">List</button><button data-curriculum-layout="grid" aria-pressed="false">Grid</button></div></div><div class="course-curriculum" data-layout="list">{panels}<p class="course-empty" hidden>No practice lessons in this collection. Choose Reading to explore the curriculum.</p></div>'''

def display(slug, content, base):
    if page_kind(slug)=='overview':return overview(slug,base)
    page=PAGES.get(slug)
    if page and page['kind']=='module':
        module=page['module'];track=page['series']
        return f'<p class="module-intro">{e(module["summary"])}</p><div class="course-curriculum">{module_panel(track,module,base)}</div><div class="module-reference"><a href="{url(base,module["chapter"]["slug"])}">Read complete module notes →</a></div>'
    return content

def context(slug, base):
    track=track_for(slug)
    if not track or page_kind(slug)=='overview':return '', ''
    def link(target,label):return f'<a href="{url(base,target)}">{e(label)}</a>'
    page=PAGES.get(slug)
    if page:
        module=page['module']
        module_label=f'Module {module["number"]:02} · {module["title"]}'
        intro=f'<div class="course-breadcrumb">{link(track["overview"],"Overview")}<span>/</span>{link(module["slug"],module_label)}</div>'
        if page['kind']=='module':return intro,''
        lessons=track['lessons'];i=lessons.index(page)
        nav='<nav class="lesson-navigation" aria-label="Lesson navigation">'
        nav+=link(lessons[i-1]['slug'],'← '+lessons[i-1]['title']) if i else link(track['overview'],'← Course overview')
        nav+=link(lessons[i+1]['slug'],lessons[i+1]['title']+' →') if i+1<len(lessons) else link(track['overview'],'Back to overview →')
        nav+='</nav>'
        complete=f'<div class="lesson-completion"><button class="tactile" data-complete-lesson="{slug}" data-track="{track["key"]}" aria-pressed="false">Mark as understood</button><span>Progress is saved on this device.</span></div>'
        intro+=f'<div class="lesson-heading-meta"><span>{page["code"]}</span><span>LESSON {page["number"]:02} OF {len(module["lessons"])} · {page["minutes"]} MIN READ</span></div>'
        tail=f'<div class="module-reference">{link(module["chapter"]["slug"],"Read complete module notes →")}</div>'
        return intro,complete+nav+tail
    chapter=next(c for c in track['chapters'] if c['slug']==slug)
    i=track['chapters'].index(chapter)
    nav='<nav class="chapter-navigation" aria-label="Chapter navigation">'
    nav+=link(track['chapters'][i-1]['slug'],'← Previous chapter') if i else '<span>Start of collection</span>'
    nav+=link(chapter['module']['slug'],'Guided module')
    nav+=link(track['chapters'][i+1]['slug'],'Next chapter →') if i+1<len(track['chapters']) else '<span>End of collection</span>'
    nav+='</nav>'
    intro=f'<p class="reference-callout">Study one concept at a time. {link(chapter["module"]["slug"],"Open the guided module →")}</p>'
    return intro+nav,nav

def study_text(slug, text):
    """Display complete technical notes without publisher front/back matter."""
    track=track_for(slug)
    if not track or slug in PAGES or slug.endswith('/overview'):
        return text
    chapter=next(c for c in track['chapters'] if c['slug']==slug)
    if track['key']=='ddia' and chapter['number']==0:
        return '\n\n'.join('## '+title+'\n\n'+body for title,body in study_notes.GUIDE.values())+'\n'
    hs=curriculum.headings(text,2)
    intro=text[:hs[0][0]] if hs else text
    intro=re.sub(r'^# [^\n]+\n','',intro,flags=re.M)
    intro=re.sub(r'^>[^\n]*\n','',intro,flags=re.M)
    selected=[body for title,body in curriculum.sections(text,2) if title not in study_notes.DROP_SECTIONS]
    return study_notes.clean(intro+'\n\n'+'\n\n'.join(selected))
