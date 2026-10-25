"""Derive a navigable syllabus from the preserved book chapters."""
from pathlib import Path
import re
import study_notes
from markdown.extensions.toc import slugify

SKIP = {'A Note for Early Release Readers', 'Footnotes', 'References', 'O’Reilly Online Learning', 'How to Contact Us', 'Acknowledgments', 'Conventions Used in This Book'}

def headings(text, level):
    found = []
    fenced = False
    offset = 0
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith('```'):
            fenced = not fenced
        if not fenced and re.match(r'^#{'+str(level)+r'} ', line):
            found.append((offset, line[level+1:].strip()))
        offset += len(line)
    return found

def sections(text, level):
    hs = headings(text, level)
    return [(title, text[pos:hs[i+1][0] if i+1<len(hs) else len(text)]) for i,(pos,title) in enumerate(hs)]

def clean(text):
    text = re.sub(r'\n---\s*\n\s*- table of contents\b.*', '', text, flags=re.S|re.I)
    return text.replace('<!-- Skip to Content -->', '').strip()

def excerpt(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    paragraphs = [p for p in re.split(r'\n\s*\n', text) if p.strip() and not p.lstrip().startswith(('#','>','*Figure','**','-','|'))]
    fallback = next((line.lstrip('-* ') for line in text.splitlines() if line.startswith(('- ', '* '))), 'Read the examples, connect the ideas, and work through the notes.')
    value = re.sub(r'[`*]', '', re.sub(r'<[^>]+>', '', paragraphs[0] if paragraphs else fallback))
    value = ' '.join(value.split())
    return value[:177].rsplit(' ',1)[0]+'…' if len(value)>180 else value

def prepare(series, src):
    pages = {}
    for track in series:
        track['title'] = 'Go study notes' if track['key']=='go' else 'Data-intensive applications'
        track['modules'] = []
        track['lessons'] = []
        for module_number, chapter in enumerate(track['chapters'], 1):
            raw = (src/(chapter['slug']+'.md')).read_text()
            module = {'number':module_number, 'title':chapter['title'], 'slug':f"{track['key']}/modules/{module_number:02}-{slugify(chapter['title'],'-')}", 'chapter':chapter, 'lessons':[], 'summary':excerpt(raw)}
            chapter['module'] = module
            if track['key']=='ddia' and chapter['number']==0:
                module['title']='Study guide'
                module['slug']='ddia/modules/01-study-guide'
                module['summary']='Set study goals, review the learning path, and build a practical method for reasoning about data systems.'
            else:
                module['summary']=excerpt(study_notes.clean(raw, strip_citations=track['key']=='ddia'))
            for title, body in sections(clean(raw), 2):
                if title in SKIP:
                    continue
                # Deep sections become separate lessons at natural subsection boundaries.
                subs = sections(body,3)
                chunks = [(title,body)]
                if len(body.split())>2200 and len(subs)>1:
                    lead = body[:headings(body,3)[0][0]]
                    chunks = [(title,lead)] + [(sub,part) for sub,part in subs]
                for section_title, section_body in chunks:
                    number = len(module['lessons'])+1
                    original_section_title=section_title
                    section_title = {'if':'Branching with if','switch':'Choosing with switch','new':'Allocating with new','defer':'Cleaning up with defer','len':'Measuring slice length','append':'Growing slices with append','make':'Allocating slices with make'}.get(section_title,section_title)
                    if section_title == 'Exercises':
                        prior = module['lessons'][-1]['title'] if module['lessons'] else module['title']
                        section_title = 'Practice: '+prior.replace('Code Review: ','')
                    if section_title in ('Wrapping Up','Summary'):
                        section_title = 'Recap: '+module['title']
                    slug = f"{track['key']}/lessons/{chapter['number']:02}-{number:02}-{slugify(section_title,'-')}"
                    section_body = re.sub(r'^#{2,3} [^\n]+', '# '+section_title, section_body, count=1)
                    if track['key']=='ddia' and chapter['number']==0:
                        section_title,guide=study_notes.GUIDE[original_section_title]
                        section_body='# '+section_title+'\n\n'+guide+'\n'
                        slug=f"{track['key']}/lessons/{chapter['number']:02}-{number:02}-{slugify(section_title,'-')}"
                    section_body=study_notes.clean(section_body, strip_citations=track['key']=='ddia')
                    kind = 'practice' if section_title.startswith(('Practice:','Code Review:')) else 'reading'
                    lesson = {'slug':slug,'title':section_title,'text':section_body.strip()+'\n','number':number,'code':f'{module_number:02}.{number:02}','module':module,'series':track,'kind':kind,'minutes':max(1,round(len(section_body.split())/220)),'summary':excerpt(section_body)}
                    module['lessons'].append(lesson)
                    track['lessons'].append(lesson)
                    pages[slug] = lesson
            if not module['lessons']:
                continue
            if not (track['key']=='ddia' and chapter['number']==0):
                module['summary']=module['lessons'][0]['summary']
            track['modules'].append(module)
            pages[module['slug']] = {'slug':module['slug'],'title':module['title'],'text':'# '+module['title']+'\n','module':module,'series':track,'kind':'module'}
        track['description'] = ('Build fluency in Go through types, control flow, functions, memory, and testing.' if track['key']=='go' else 'Reason about data systems, from storage and replication to streams and responsible design.')
        track['headline'] = ('Write Go with a clearer mental model.' if track['key']=='go' else 'Understand how data systems fit together.')
    return pages
