/* Notex — MIT licensed. No services, telemetry or network dependencies. */
(()=>{'use strict';
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const base=document.body.dataset.base||'./';
let saved=[];try{saved=JSON.parse(localStorage.getItem('notex-saved')||'[]');if(!Array.isArray(saved))saved=[];}catch{}
function notify(message){const t=$('.toast');t.textContent=message;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2200)}
const search=$('.search-dialog'),input=$('input',search),results=$('#search-results');let dataPromise;
function loadIndex(){return dataPromise??=fetch(base+'assets/search.json').then(r=>{if(!r.ok)throw Error('Search index unavailable');return r.json()}).catch(e=>{dataPromise=null;throw e;});}
function safe(s){return s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
async function renderSearch(){const query=input.value.trim().toLowerCase();results.innerHTML='<p class="search-empty">Loading notes…</p>';try{const data=await loadIndex();if(query!==input.value.trim().toLowerCase())return;const terms=query.split(/\s+/).filter(Boolean);const found=data.filter(x=>x.title!=='Page Not Found'&&x.kind!=='reference'&&x.kind!=='module').map(x=>({...x,score:terms.reduce((n,t)=>n+(x.title.toLowerCase().includes(t)?10:0)+(x.category.toLowerCase().includes(t)?4:0)+(x.text.toLowerCase().includes(t)?1:0),0)})).filter(x=>!query||terms.every(t=>(x.title+' '+(x.collection||'')+' '+x.category+' '+x.text).toLowerCase().includes(t))).sort((a,b)=>b.score-a.score).slice(0,18);results.innerHTML=found.length?found.map(x=>{const pos=query?Math.max(0,x.text.toLowerCase().indexOf(terms[0])-45):0;return `<a class="search-result" href="${base+x.url}"><small>${safe(x.category)}</small><strong>${safe(x.title)}</strong><p>${safe(x.text.slice(pos,pos+145))}…</p></a>`}).join(''):`<p class="search-empty">No notes found for “${safe(query)}”. Try Python, SQL, Git, or a concept.</p>`;}catch{results.innerHTML='<p class="search-empty">Search could not load. Please try again or browse the library.</p>';}}
function openSearch(){search.showModal();input.focus();renderSearch();}
$$('[data-search]').forEach(b=>b.addEventListener('click',openSearch));input.addEventListener('input',renderSearch);
document.addEventListener('keydown',e=>{if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();search.open?search.close():openSearch();}if(e.key==='Escape')closeDropdowns();});
$$('[data-close]').forEach(b=>b.addEventListener('click',()=>b.closest('dialog').close()));
$$('dialog').forEach(d=>d.addEventListener('click',e=>{if(e.target===d){const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)d.close();}}));
const menu=$('.menu-dialog');$('[data-menu]')?.addEventListener('click',()=>menu.showModal());$$('a',menu).forEach(a=>a.addEventListener('click',()=>menu.close()));
function closeDropdowns(except){$$('[data-dropdown]').filter(b=>b!==except).forEach(b=>b.setAttribute('aria-expanded','false'));}
$$('[data-dropdown]').forEach(b=>b.addEventListener('click',()=>{const open=b.getAttribute('aria-expanded')==='true';closeDropdowns();b.setAttribute('aria-expanded',String(!open));}));document.addEventListener('click',e=>{if(!e.target.closest('.dropdown'))closeDropdowns();});
$('[data-dismiss]')?.addEventListener('click',()=>{$('.announcement').remove();try{sessionStorage.setItem('notex-announcement-hidden','1')}catch{}});try{if(sessionStorage.getItem('notex-announcement-hidden'))$('.announcement').remove()}catch{}
function updateSaved(){ $$('[data-save]').forEach(b=>{const on=saved.includes(b.dataset.save);b.textContent=on?'Saved ✓':'Save note';b.setAttribute('aria-pressed',String(on));});}
$$('[data-save]').forEach(b=>b.addEventListener('click',()=>{const key=b.dataset.save;saved=saved.includes(key)?saved.filter(x=>x!==key):[...saved,key];try{localStorage.setItem('notex-saved',JSON.stringify(saved));notify(saved.includes(key)?'Note saved in this browser':'Note removed from saved');}catch{notify('Browser storage is unavailable. Notes cannot be saved.');}updateSaved();}));updateSaved();
$$('[data-filter]').forEach(b=>b.addEventListener('click',()=>{$$('[data-filter]').forEach(x=>{x.classList.toggle('active',x===b);x.setAttribute('aria-pressed',String(x===b));});let count=0;$$('.note-row').forEach(a=>{const visible=b.dataset.filter==='all'||(b.dataset.filter==='saved'?saved.includes(a.dataset.url):a.dataset.category===b.dataset.filter);a.hidden=!visible;if(visible)count++;});const empty=$('.empty-state');if(empty)empty.hidden=count!==0;}));
const sidebar=$('[data-sidebar]');if(sidebar)sidebar.addEventListener('click',()=>{const show=$('.sidebar').classList.toggle('visible');sidebar.setAttribute('aria-expanded',String(show));});
})();
/* Landing interactions: a rotating headline, real preview, and FAQ disclosures. */
(()=>{
 const demo=document.querySelector('.demo-dialog');
 document.querySelectorAll('[data-demo]').forEach(button=>button.addEventListener('click',()=>demo?.showModal()));
 document.querySelectorAll('[data-cloud-path]').forEach(button=>button.addEventListener('click',()=>{
  document.getElementById(button.getAttribute('aria-controls'))?.showModal();
 }));
 const word=document.querySelector('[data-rotate-word]'),article=document.querySelector('[data-rotate-article]');
 if(word&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
  const companies=['Anthropic','Google','Microsoft','Meta','Stripe','Amazon','NVIDIA'];let index=0;
  setInterval(()=>{if(document.hidden||document.querySelector('dialog[open]'))return;word.classList.add('changing');setTimeout(()=>{index=(index+1)%companies.length;word.textContent=companies[index];if(article)article.textContent=/^[AEIOU]/.test(companies[index])?'an':'a';word.classList.remove('changing');},200);},3500);
 }
 document.querySelectorAll('.home .faq details').forEach(item=>item.addEventListener('toggle',()=>{if(item.open)document.querySelectorAll('.home .faq details[open]').forEach(other=>{if(other!==item)other.open=false;});}));
})();
/* Guided curricula: lesson filters, reading layout, and local progress. */
(()=>{
 const all=(s,r=document)=>[...r.querySelectorAll(s)];
 const curriculum=document.querySelector('.course-curriculum');
 all('[data-lesson-filter]').forEach(button=>button.addEventListener('click',()=>{
  all('[data-lesson-filter]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});
  let visible=0;
  all('[data-lesson-kind]').forEach(row=>{row.hidden=button.dataset.lessonFilter!=='all'&&row.dataset.lessonKind!==button.dataset.lessonFilter;if(!row.hidden)visible++;});
  all('.curriculum-module').forEach(module=>{module.hidden=!module.querySelector('[data-lesson-kind]:not([hidden])');});
  const empty=document.querySelector('.course-empty');if(empty)empty.hidden=visible!==0;
 }));
 all('[data-curriculum-layout]').forEach(button=>button.addEventListener('click',()=>{
  all('[data-curriculum-layout]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});
  if(curriculum)curriculum.dataset.layout=button.dataset.curriculumLayout;
 }));
 let completed=[],last={};
 try{completed=JSON.parse(localStorage.getItem('notex-understood')||'[]');if(!Array.isArray(completed))completed=[];completed=completed.filter(s=>typeof s==='string');last=JSON.parse(localStorage.getItem('notex-course-last')||'{}');if(!last||typeof last!=='object'||Array.isArray(last))last={};}catch{}
 const base=document.body.dataset.base||'./';
 const update=()=>{
  all('[data-lesson-link]').forEach(link=>link.classList.toggle('is-complete',completed.includes(link.dataset.lessonLink)));
  all('[data-course-progress]').forEach(el=>{const count=completed.filter(s=>s.startsWith(el.dataset.courseProgress+'/lessons/')).length;el.textContent=`${count} / ${el.dataset.courseTotal} LESSONS COMPLETE`;});
  all('[data-complete-lesson]').forEach(button=>{const done=completed.includes(button.dataset.completeLesson);button.textContent=done?'Understood ✓':'Mark as understood';button.setAttribute('aria-pressed',String(done));});
 };
 const active=document.querySelector('[data-complete-lesson]');
 if(active){last[active.dataset.track]=active.dataset.completeLesson;try{localStorage.setItem('notex-course-last',JSON.stringify(last));}catch{}}
 all('[data-complete-lesson]').forEach(button=>button.addEventListener('click',()=>{
  const lesson=button.dataset.completeLesson,next=completed.includes(lesson)?completed.filter(s=>s!==lesson):[...completed,lesson];
  try{localStorage.setItem('notex-understood',JSON.stringify(next));completed=next;update();}catch{const label=button.nextElementSibling;if(label)label.textContent='Browser storage is unavailable. Progress could not be saved.';}
 }));
 all('[data-course-resume]').forEach(link=>{const key=link.dataset.courseResume,slug=last[key];if(typeof slug==='string'&&new RegExp('^'+key+'/lessons/[a-z0-9-]+$').test(slug)){link.href=base+slug+'/';link.textContent='Continue learning →';}});
 update();
})();
