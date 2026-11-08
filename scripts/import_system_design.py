#!/usr/bin/env python3
"""Import the supplied PDF once. Builds consume Markdown and original image bytes."""
from pathlib import Path
import hashlib,html,json,re,sys
import pymupdf
from bs4 import BeautifulSoup,NavigableString
from import_distributed import inline,norm
ROOT=Path(__file__).resolve().parent.parent
KEY='system-design'
def e(x):return html.escape(x,quote=True)
def slug(x):return re.sub('[^a-z0-9]+','-',x.lower()).strip('-')
def run(path):
 doc=pymupdf.open(path);starts=[(t,p-1) for _,t,p in doc.get_toc() if t.startswith('CHAPTER ')]
 dest=ROOT/'src'/KEY;assets=ROOT/'web/assets'/KEY;dest.mkdir(exist_ok=True);assets.mkdir(exist_ok=True)
 chapters=[];figures=[];total=0
 for ci,(title,start) in enumerate(starts,1):
  end=starts[ci][1] if ci<len(starts) else 268
  title=title.split(': ',1)[1].capitalize()
  for a,b in {'url':'URL',' id ':' ID ','youtube':'YouTube','google drive':'Google Drive'}.items():title=title.replace(a,b)
  sections=[{'title':title,'body':[]}];refs=[];in_refs=False
  skip_title=True
  for pn in range(start,end):
   page=doc[pn];links=page.get_links()
   for b in page.get_text('dict')['blocks']:
    if b['type']==1:
     filename=f'figure-{len(figures)+1:03}.{b["ext"]}';(assets/filename).write_bytes(b['image'])
     value=f'<figure class="source-figure"><a href="../../assets/{KEY}/{filename}" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/{KEY}/{filename}" width="{b["width"]}" height="{b["height"]}" loading="lazy" alt="{e(title)} — original diagram {len(figures)+1}"></a></figure>'
     (refs if in_refs else sections[-1]['body']).append(value)
     figures.append({'file':filename,'page':pn+1,'sha256':hashlib.sha256(b['image']).hexdigest()});continue
    groups=[];current=[];kind=None
    for line in b['lines']:
     text=norm(''.join(s['text'] for s in line['spans'])).strip()
     if not text:continue
     size=max(s['size'] for s in line['spans'])
     if pn==start and skip_title:
      if size>16:continue
      skip_title=False
     if line['bbox'][1]>780 and text.isdigit():continue
     heading=size>=13.5 and all('Bold' in s['font'] or not s['text'].strip() for s in line['spans'])
     newkind='heading' if heading else 'text'
     if newkind!=kind and current:groups.append((kind,current));current=[]
     kind=newkind;current.append(line)
    if current:groups.append((kind,current))
    for kind,lines in groups:
     value=inline({'lines':lines},links);plain=BeautifulSoup(value,'html.parser').get_text(' ',strip=True)
     if kind=='heading':
      if re.match(r'^Reference (materials|material)',plain,re.I):in_refs=True;continue
      if in_refs:refs.append('<h4>'+value+'</h4>');continue
      sections.append({'title':plain,'body':[]})
     else:
      body=refs if in_refs else sections[-1]['body']
      if plain.startswith('•'):
       body.append('<ul>'+''.join('<li>'+s.strip()+'</li>' for s in value.split('•') if s.strip())+'</ul>')
      elif re.match(r'^\d+\. ',plain):
       parts=re.split(r'\s+(?=\d+\. [A-Z])',value)
       body.append('<ol start="'+re.match(r'^(\d+)',plain)[1]+'">'+''.join('<li>'+re.sub(r'^\d+\.\s*','',s)+'</li>' for s in parts)+'</ol>')
      else:body.append('<p>'+value+'</p>')
  sections=[s for s in sections if s['body']]
  last=f'{KEY}/lessons/{ci:02}-{len(sections):02}-{slug(sections[-1]["title"])}'
  # Original references remain in the final section of the chapter/module.
  refhtml=''
  if refs:
   raw=BeautifulSoup('\n'.join(refs),'html.parser')
   for a in list(raw.find_all('a')):
    if a.get_text(strip=True).startswith(('http://','https://')):a.string=a.get('href',a.text)
   text=raw.get_text(' ',strip=True)
   entries=re.split(r'\[(\d+)\]\s*',text)
   if len(entries)>1:
    refhtml='<section class="lesson-references"><h3 id="references-'+str(ci)+'">References</h3><ol>'
    for j in range(1,len(entries),2):
     body=e(entries[j+1].strip())
     body=re.sub(r'https?://[^\s<>]+',lambda m:'<a href="'+m[0]+'">'+m[0]+'</a>',body)
     refhtml+=f'<li id="reference-{ci}-{entries[j]}" value="{entries[j]}">'+body+'</li>'
    refhtml+='</ol></section>'
   else:refhtml='<section class="lesson-references"><h3 id="references-'+str(ci)+'">References</h3>'+str(raw)+'</section>'
  chunks=[]
  for si,s in enumerate(sections,1):
   soup=BeautifulSoup('\n\n'.join(s['body']),'html.parser')
   for tag in soup.find_all(['em','strong','sup']):
    if not tag.get_text().strip():tag.unwrap()
   for p in list(soup.find_all('p',recursive=False)):
    prev=p.previous_sibling
    while isinstance(prev,NavigableString) and not prev.strip():prev=prev.previous_sibling
    if getattr(prev,'name',None)=='p' and p.text[:1].islower() and prev.text.rstrip()[-1:] not in '.!?:;':
     prev.append(' ')
     for c in list(p.contents):prev.append(c.extract())
     p.decompose()
   # Link bracket citations without changing their displayed wording.
   for node in list(soup.find_all(string=True)):
    if any(a.name in ('a','pre','code') for a in node.parents):continue
    text=str(node);pieces=re.split(r'(\[\d+\])',text)
    if len(pieces)>1:
     for part in pieces:
      if re.fullmatch(r'\[\d+\]',part) and f'id="reference-{ci}-{part[1:-1]}"' in refhtml:
       a=soup.new_tag('a',href=f'study:{last}/#reference-{ci}-{part[1:-1]}');a.string=part;node.insert_before(a)
      else:node.insert_before(part)
     node.extract()
   video=f'<section class="chapter-video" aria-label="Video for {e(s["title"])}"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>{e(s["title"])}</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>'
   chunks.append('## '+s['title']+'\n\n'+video+'\n\n'+str(soup)+(('\n\n'+refhtml) if si==len(sections) else ''))
  route=f'{KEY}/chapter-{ci:02}';source='# '+title+'\n\n'+'\n\n'.join(chunks)+'\n';(ROOT/'src'/(route+'.md')).write_text(source)
  chapters.append({'number':ci,'title':title,'slug':route,'sections':len(sections),'sha256':hashlib.sha256(source.encode()).hexdigest()});total+=len(sections)
 (dest/'overview.md').write_text('# System design\n\nA practical path from scaling foundations to complete system architectures.\n')
 manifest={'key':KEY,'title':'System design','overview':KEY+'/overview','chapters':chapters,'source_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'page_count':len(doc),'lesson_count':total,'figures':figures}
 (ROOT/'scripts/system-design-import.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(f'Imported {len(chapters)} modules, {total} sections, {len(figures)} exact original graphics.')
if __name__=='__main__':run(sys.argv[1])
