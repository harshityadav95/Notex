#!/usr/bin/env python3
"""One-time, reproducible import of the user-supplied PDF. No PDF needed to build.
Usage: .venv/bin/python scripts/import_distributed.py /absolute/path/to/source.pdf
"""
from pathlib import Path
import hashlib, html, json, re, sys, unicodedata
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT/'src/distributed-systems'
ASSETS = ROOT/'web/assets/distributed-systems'

def e(s): return html.escape(s, quote=True)
def norm(s): return unicodedata.normalize('NFKC', s).replace('\u00ad', '')
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def inline(block, links):
    lines=[]
    for line in block['lines']:
        spans=[]
        for span in line['spans']:
            text=norm(span['text'])
            if not text: continue
            value=e(text)
            font=span['font']
            if span['flags'] & 1: value='<sup>'+value+'</sup>'
            if 'Italic' in font or font.endswith('-It'): value='<em>'+value+'</em>'
            if 'Bold' in font: value='<strong>'+value+'</strong>'
            if 'SourceCode' in font: value='<code>'+value+'</code>'
            for link in links:
                if pymupdf.Rect(span['bbox']).intersects(link['from']):
                    href=link.get('uri')
                    if href and re.match(r'^(https?://|mailto:)', href):
                        # The publication's personal contact is omitted from the interface.
                        if 'understandingdistributed.systems' not in href:
                            value='<a href="'+e(href)+'">'+value+'</a>'
                        break
            spans.append(value)
        lines.append(''.join(spans))
    result=''
    for line in lines:
        plain=html.unescape(re.sub('<[^>]+>', '', line)).lstrip()
        if result and re.search(r'-(</(?:em|strong|code)>)?$',result) and plain[:1].islower():
            tail=html.unescape(re.sub('<[^>]+>','',result)).split()[-1].lower()
            compound=bool(re.fullmatch(r'(?:single|multi|two|three|cross|client|server|load|fault|large|small|high|low|real|end|at|on|off|self|well|read|write|full|semi|pre|post|non|ad|time|memory|thread|long|short|data|state|message|event|application|service|network|region)-',tail))
            result=(result if compound else re.sub(r'-(</(?:em|strong|code)>)?$',lambda m:m.group(1) or '',result))+line.lstrip()
        else: result+=(' ' if result else '')+line
    return result

def run(path):
    doc=pymupdf.open(path)
    toc=doc.get_toc()
    starts=[(level,title,page-1) for level,title,page in toc if (level==1 and title=='Introduction') or (level==1 and re.match(r'^[IVX]+ ',title)) or (level==2 and page>=35)]
    modules=[]; number=0; figures=[]; blocks_kept=0; chapters=0
    for i,(level,title,start) in enumerate(starts):
        end=starts[i+1][2] if i+1<len(starts) else len(doc)
        if level==1:
            name='Foundations' if title=='Introduction' else title.split(' ',1)[1]
            module={'number':len(modules)+1,'title':name,'slug':f'distributed-systems/chapter-{len(modules)+1:02}', 'sections':[]}
            modules.append(module)
        is_part=level==1 and title!='Introduction'
        chapter_title='Overview: '+module['title'] if is_part else title
        if not is_part:number+=1;chapters+=1
        body=[]
        for page_no in range(start,end):
            page=doc[page_no]; blocks=page.get_text('dict')['blocks'];links=page.get_links()
            tables=page.find_tables().tables; emitted=set()
            if not blocks:continue
            body.append(f'<div class="source-page" id="source-page-{page_no+1}"></div>')
            for j,b in enumerate(blocks):
                if b['bbox'][1]<75:continue # repeated running header and page number
                table=next((t for t in tables if pymupdf.Rect(b['bbox']).intersects(pymupdf.Rect(t.bbox)) and b['bbox'][0]>=t.bbox[0]-2 and b['bbox'][2]<=t.bbox[2]+2),None)
                if table is not None:
                    if table.bbox not in emitted:
                        rows=table.extract()
                        rows=[[norm(c or '').replace('Meth od','Method') for c in r] for r in rows]
                        body.append('<table><thead><tr>'+''.join('<th>'+e(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+e(c)+'</td>' for c in row)+'</tr>' for row in rows[1:])+'</tbody></table>')
                        emitted.add(table.bbox)
                    continue
                if b['type']==1:
                    filename=f'figure-{len(figures)+1:03}.png'
                    (ASSETS/filename).write_bytes(b['image'])
                    caption=''
                    for nxt in blocks[j+1:]:
                        if nxt['type']==0:
                            possible=norm(' '.join(''.join(s['text'] for s in l['spans']) for l in nxt['lines']))
                            if possible.startswith('Figure'):caption=possible
                            break
                    alt=caption or f'{chapter_title}: technical diagram {len(figures)+1}'
                    body.append(f'<figure class="source-figure"><a href="../../assets/distributed-systems/{filename}" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/{filename}" alt="{e(alt)}" width="{b["width"]}" height="{b["height"]}" loading="lazy"></a></figure>')
                    figures.append({'file':filename,'page':page_no+1,'sha256':hashlib.sha256(b['image']).hexdigest(),'caption':caption})
                    continue
                plain=norm(' '.join(''.join(s['text'] for s in l['spans']) for l in b['lines'])).strip()
                spans=[s for l in b['lines'] for s in l['spans']]
                max_size=max(s['size'] for s in spans)
                if re.fullmatch(r'Chapter \d+|Part [IVX]+',plain) or max_size>19: continue # title rendered by the site shell
                if 'roberto@understandingdistributed.systems' in plain:continue
                value=inline(b,links)
                if max_size>13:
                    body.append(f'<h3 id="section-{slug(plain)}">{value}</h3>')
                elif max_size>11 and any('Bold' in s['font'] for s in spans):
                    body.append(f'<h4 id="section-{slug(plain)}">{value}</h4>')
                elif plain.startswith('Figure'):
                    body.append(f'<p class="source-caption">{value}</p>')
                elif all('SourceCode' in s['font'] or not s['text'].strip() for s in spans):
                    code='\n'.join(' '*max(0,round((l['bbox'][0]-72)/4.782)) + ''.join(s['text'] for s in l['spans']) for l in b['lines'])
                    body.append('<pre><code>'+e(norm(code))+'</code></pre>')
                elif max_size<8.5:
                    body.append(f'<p class="source-footnote">{value}</p>')
                elif plain.startswith('•'):
                    body.append('<ul>'+''.join('<li>'+item.strip()+'</li>' for item in value.split('•') if re.sub('<[^>]+>','',item).strip())+'</ul>')
                else:body.append(f'<p>{value}</p>')
                blocks_kept+=1
        video=f'<section class="chapter-video" aria-label="Video for {e(chapter_title)}"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>{e(chapter_title)}</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>'
        content='\n\n'.join(body).replace('</code></pre>\n\n<pre><code>', '\n')
        module['sections'].append({'title':chapter_title,'text':video+'\n\n'+content,'start':start+1,'end':end})
    SRC.mkdir(parents=True,exist_ok=True)
    for module in modules:
        text='# '+module['title']+'\n\n'+'\n\n'.join('## '+s['title']+'\n\n'+s['text'] for s in module['sections'])+'\n'
        (ROOT/'src'/(module['slug']+'.md')).write_text(text)
    (SRC/'overview.md').write_text('# Distributed systems\n\nCommunication, coordination, scalability, resiliency, and maintainability.\n')
    from edit_distributed import edit
    edit(ROOT)
    manifest={'editorial_revision':2,'key':'distributed-systems','title':'Distributed systems','overview':'distributed-systems/overview','chapters':[{k:m[k] for k in ('number','title','slug')} for m in modules], 'source_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'page_count':len(doc),'technical_pages':[19,len(doc)],'chapter_count':chapters,'lesson_count':len(starts),'text_blocks':blocks_kept,'figures':figures,'sources':{m['slug']:hashlib.sha256((ROOT/'src'/(m['slug']+'.md')).read_bytes()).hexdigest() for m in modules}}
    (ROOT/'scripts/distributed-import.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'Imported {chapters} chapters + {len(starts)-chapters} part introductions, {len(modules)} modules, {len(figures)} original diagrams, {blocks_kept} text blocks.')

if __name__=='__main__':
    ASSETS.mkdir(parents=True,exist_ok=True)
    run(sys.argv[1])
