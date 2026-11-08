"""Editorial pass after PDF import; requires beautifulsoup4 only when reimporting."""
from pathlib import Path
import re
from bs4 import BeautifulSoup, NavigableString

COMPOUNDS={'single','multi','two','three','cross','client','server','load','fault','large','small','high','low','real','end','at','on','off','self','well','read','write','full','semi','pre','post','non','ad','time','memory','thread','long','short','data','state','message','event','application','service','network','region'}
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')
def edit(root):
    files=sorted((Path(root)/'src/distributed-systems').glob('chapter-*.md'))
    lessons=[];chapter_map={};section_map={};modules={};chapter=0
    for module,file in enumerate(files,1):
        text=file.read_text();parts=re.split(r'^## (.+)\n',text,flags=re.M)
        modules[module]=(parts[0].splitlines()[0][2:],f'distributed-systems/modules/{module:02}-{slug(parts[0].splitlines()[0][2:])}')
        for num in range(1,len(parts),2):
            title=parts[num]; code=f'{module:02}.{(num+1)//2:02}';route=f'distributed-systems/lessons/{module:02}-{(num+1)//2:02}-{slug(title)}'
            item={'file':file,'title':title,'code':code,'route':route,'body':parts[num+1]};lessons.append(item)
            if not title.startswith('Overview:'):chapter+=1;chapter_map[str(chapter)]=item
            soup=BeautifulSoup(item['body'],'html.parser')
            for h in soup.select('h3,h4'):
                m=re.match(r'(\d+(?:\.\d+)+)\s+(.+)',h.get_text(' ',strip=True))
                if m:section_map[m[1]]=(item,h.get('id'),m[2])
    for index,item in enumerate(lessons):
        soup=BeautifulSoup(item['body'],'html.parser');references=[]
        for ref in soup.select('.source-footnote'):
            raw=ref.decode_contents()
            # Some PDF text blocks contain more than one numbered footnote.
            raw=re.sub(r'<a[^>]+>(\d+)</a>',r'\1',raw)
            for fragment in re.split(r'\s+(?=\d{1,2}[A-Z“])',raw):
                m=re.match(r'\s*(\d+)\s*(.*)',fragment,re.S)
                if m:references.append((m[1],m[2]))
            ref.decompose()
        for marker in soup.select('.source-page'):marker.decompose()
        # Collapse artificial PDF line-wrap fragments of the same URL.
        for a in list(soup.find_all('a')):
            if not a.parent:continue
            href=a.get('href','')
            while True:
                nxt=a.next_sibling
                if isinstance(nxt,NavigableString) and not nxt.strip():nxt=nxt.next_sibling
                if getattr(nxt,'name',None)=='a' and nxt.get('href')==href:
                    nxt.decompose()
                else:break
            if a.get_text(strip=True).startswith(('http://','https://')):a.string=href
        for tag in soup.find_all(['em','strong','sup']):
            if not tag.get_text().strip():tag.unwrap()
        # Join paragraphs interrupted solely by PDF page breaks/footnotes.
        for p in list(soup.find_all('p',recursive=False)):
            if p.get('class'):continue
            prev=p.previous_sibling
            while isinstance(prev,NavigableString) and not prev.strip():prev=prev.previous_sibling
            if getattr(prev,'name',None)!='p' or prev.get('class'):continue
            left=prev.get_text().rstrip();right=p.get_text().lstrip()
            if left and right and right[0].islower() and left[-1] not in '.!?:;”':
                if left.endswith('-'):
                    token=re.search(r'([A-Za-z]+)-$',left)
                    if token and token[1].lower() not in COMPOUNDS:
                        last=prev.find_all(string=True)[-1];last.replace_with(str(last).rstrip()[:-1])
                else:prev.append(' ')
                for child in list(p.contents):prev.append(child.extract())
                p.decompose()
        if references:
            section=soup.new_tag('section',attrs={'class':'lesson-references','aria-label':'References'})
            h=soup.new_tag('h3',id='references-'+item['code']);h.string='References';section.append(h)
            ol=soup.new_tag('ol')
            for n,raw in references:
                li=soup.new_tag('li',id=f'reference-{item["code"]}-{n}',value=n)
                fragment=BeautifulSoup(raw,'html.parser')
                for a in fragment.find_all('a'):
                    href=a.get('href','')
                    if href.startswith(('http://','https://')):a.string=href
                # Merge repeated fragments after replacing their broken URL labels.
                seen=set()
                for a in list(fragment.find_all('a')):
                    if a.get('href') in seen:a.decompose()
                    else:seen.add(a.get('href'))
                for child in list(fragment.contents):li.append(child.extract())
                ol.append(li)
            section.append(ol);soup.append(section)
        for h in soup.select('h3,h4'):
            label=re.sub(r'^\d+(?:\.\d+)+\s+','',h.get_text(' ',strip=True));h.clear();h.append(label)
        # Rewrite prose only; code examples, attributes and external titles stay intact.
        for node in list(soup.find_all(string=True)):
            if any(p.name in ('pre','code','a') for p in node.parents):continue
            value=str(node)
            for old,new in {'multi-ple':'multiple','NG- INX':'NGINX','Idempotency- Key':'Idempotency-Key','fairloss':'fair-loss','acknolowedgment':'acknowledgment','asynchrounous':'asynchronous','this this':'this','was was':'was','messages that that':'messages that'}.items():value=value.replace(old,new)
            for pattern,replacement in [(r'\bThis book\b','This module'),(r'\bthis book\b','this module'),(r'\bthe book\b','this learning path'),(r'\bthis chapter\b','this lesson'),(r'\bThis chapter\b','This lesson'),(r'\bprevious chapters\b','earlier lessons'),(r'\bnext chapters\b','following lessons'),(r'\bThe previous chapter\b','The previous lesson')]:value=re.sub(pattern,replacement,value)
            value=re.sub(r'\b(first|second|third|fourth|fifth) part of this learning path\b',lambda m:{'first':'Communication','second':'Coordination','third':'Scalability','fourth':'Resiliency','fifth':'Maintainability'}[m[1]]+' module',value)
            pattern=r'\b(?:[Cc]hapter|[Ss]ection)\s+(\d+(?:\.\d+)*)\b|\bPart\s+(I{1,3}|IV|V)\b|\b(the next|the previous) chapter\b'
            last=0;pieces=[]
            for m in re.finditer(pattern,value):
                target=None
                if m[1]:
                    if '.' in m[1] and m[1] in section_map:
                        lesson,anchor,label=section_map[m[1]];target=(f'study:{lesson["route"]}/#{anchor}',label+' in '+lesson['title'])
                    elif m[1] in chapter_map:
                        lesson=chapter_map[m[1]];target=(f'study:{lesson["route"]}/',lesson['title']+' (lesson '+lesson['code']+')')
                elif m[2]:
                    mn={'I':2,'II':3,'III':4,'IV':5,'V':6}[m[2]];name,route=modules[mn];target=('study:'+route+'/',name+' (module '+str(mn)+')')
                else:
                    j=index+(1 if m[3]=='the next' else -1)
                    if 0<=j<len(lessons):
                        lesson=lessons[j];target=('study:'+lesson['route']+'/',lesson['title']+' (lesson '+lesson['code']+')')
                pieces.append(value[last:m.start()])
                if target:
                    a=soup.new_tag('a',href=target[0]);a.string=target[1];pieces.append(a)
                else:pieces.append(m[0])
                last=m.end()
            pieces.append(value[last:])
            for piece in pieces:node.insert_before(piece)
            node.extract()
        # Match citation markers to the notes moved below this reading.
        numbers={n for n,_ in references}
        for sup in soup.select('sup'):
            n=sup.get_text(strip=True)
            if n in numbers:
                a=soup.new_tag('a',href=f'#reference-{item["code"]}-{n}',attrs={'aria-label':f'Reference {n}'})
                a.string='['+n+']';sup.clear();sup.append(a)
        # Restore display math and numbered steps lost in the PDF text stream.
        for p in list(soup.select('p')):
            if p.get_text(strip=True)=='Bandwidth =WinSize' or p.get_text(' ',strip=True)=='Bandwidth = WinSize':
                nxt=p.find_next_sibling('p')
                if nxt and nxt.get_text(strip=True)=='RTT':
                    p.clear();p.string='Bandwidth = WinSize / RTT';p['class']='display-equation';nxt.decompose()
            if re.match(r'^\d+\. ',p.get_text()):
                raw=p.decode_contents();steps=re.split(r'\s+(?=\d+\. [A-Z])',raw)
                ol=soup.new_tag('ol',start=re.match(r'(\d+)',p.get_text())[1])
                for step in steps:
                    li=soup.new_tag('li');frag=BeautifulSoup(re.sub(r'^\d+\.\s*','',step),'html.parser')
                    for child in list(frag.contents):li.append(child.extract())
                    ol.append(li)
                p.replace_with(ol)
        for a in soup.select('.lesson-references a'):
            previous=a.previous_sibling
            if isinstance(previous,NavigableString) and previous and not previous[-1].isspace():a.insert_before(' ')
        item['body']=str(soup).strip().replace('CHAPTER VIDEO','LESSON VIDEO')
    for file in files:
        title=file.read_text().splitlines()[0]
        file.write_text(title+'\n\n'+'\n\n'.join('## '+x['title']+'\n\n'+x['body'] for x in lessons if x['file']==file)+'\n')

if __name__=='__main__':
    import hashlib,json
    root=Path(__file__).resolve().parent.parent
    edit(root)
    p=root/'scripts/distributed-import.json';data=json.loads(p.read_text())
    data['editorial_revision']=2
    data['sources']={slug:hashlib.sha256((root/'src'/(slug+'.md')).read_bytes()).hexdigest() for slug in data['sources']}
    p.write_text(json.dumps(data,indent=2)+'\n')
