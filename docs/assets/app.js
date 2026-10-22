/* Notex — MIT licensed. No services, telemetry or network dependencies. */
(()=>{'use strict';
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const base=document.body.dataset.base||'./';
let saved=[];try{saved=JSON.parse(localStorage.getItem('notex-saved')||'[]');if(!Array.isArray(saved))saved=[];}catch{}
function notify(message){const t=$('.toast');t.textContent=message;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2200)}
const search=$('.search-dialog'),input=$('input',search),results=$('#search-results');let dataPromise;
function loadIndex(){return dataPromise??=fetch(base+'assets/search.json').then(r=>{if(!r.ok)throw Error('Search index unavailable');return r.json()}).catch(e=>{dataPromise=null;throw e;});}
function safe(s){return s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
async function renderSearch(){const query=input.value.trim().toLowerCase();results.innerHTML='<p class="search-empty">Loading notes…</p>';try{const data=await loadIndex();if(query!==input.value.trim().toLowerCase())return;const terms=query.split(/\s+/).filter(Boolean);const found=data.filter(x=>x.title!=='Page Not Found').map(x=>({...x,score:terms.reduce((n,t)=>n+(x.title.toLowerCase().includes(t)?10:0)+(x.category.toLowerCase().includes(t)?4:0)+(x.text.toLowerCase().includes(t)?1:0),0)})).filter(x=>!query||terms.every(t=>(x.title+' '+x.category+' '+x.text).toLowerCase().includes(t))).sort((a,b)=>b.score-a.score).slice(0,18);results.innerHTML=found.length?found.map(x=>{const pos=query?Math.max(0,x.text.toLowerCase().indexOf(terms[0])-45):0;return `<a class="search-result" href="${base+x.url}"><small>${safe(x.category)}</small><strong>${safe(x.title)}</strong><p>${safe(x.text.slice(pos,pos+145))}…</p></a>`}).join(''):`<p class="search-empty">No notes found for “${safe(query)}”. Try Python, SQL, Git, or a concept.</p>`;}catch{results.innerHTML='<p class="search-empty">Search could not load. Please try again or browse the library.</p>';}}
function openSearch(){search.showModal();input.focus();renderSearch();}
$$('[data-search]').forEach(b=>b.addEventListener('click',openSearch));input.addEventListener('input',renderSearch);
document.addEventListener('keydown',e=>{if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();search.open?search.close():openSearch();}if(e.key==='Escape')closeDropdowns();});
$$('[data-close]').forEach(b=>b.addEventListener('click',()=>b.closest('dialog').close()));
$$('dialog').forEach(d=>d.addEventListener('click',e=>{if(e.target===d){const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)d.close();}}));
const menu=$('.menu-dialog');$('[data-menu]').addEventListener('click',()=>menu.showModal());$$('a',menu).forEach(a=>a.addEventListener('click',()=>menu.close()));
function closeDropdowns(except){$$('[data-dropdown]').filter(b=>b!==except).forEach(b=>b.setAttribute('aria-expanded','false'));}
$$('[data-dropdown]').forEach(b=>b.addEventListener('click',()=>{const open=b.getAttribute('aria-expanded')==='true';closeDropdowns();b.setAttribute('aria-expanded',String(!open));}));document.addEventListener('click',e=>{if(!e.target.closest('.dropdown'))closeDropdowns();});
$('[data-dismiss]').addEventListener('click',()=>{$('.announcement').remove();try{sessionStorage.setItem('notex-announcement-hidden','1')}catch{}});try{if(sessionStorage.getItem('notex-announcement-hidden'))$('.announcement').remove()}catch{}
function updateSaved(){ $$('[data-save]').forEach(b=>{const on=saved.includes(b.dataset.save);b.textContent=on?'Saved ✓':'Save note';b.setAttribute('aria-pressed',String(on));});}
$$('[data-save]').forEach(b=>b.addEventListener('click',()=>{const key=b.dataset.save;saved=saved.includes(key)?saved.filter(x=>x!==key):[...saved,key];try{localStorage.setItem('notex-saved',JSON.stringify(saved));notify(saved.includes(key)?'Note saved in this browser':'Note removed from saved');}catch{notify('Browser storage is unavailable. Notes cannot be saved.');}updateSaved();}));updateSaved();
$$('[data-filter]').forEach(b=>b.addEventListener('click',()=>{$$('[data-filter]').forEach(x=>{x.classList.toggle('active',x===b);x.setAttribute('aria-pressed',String(x===b));});let count=0;$$('.note-row').forEach(a=>{const visible=b.dataset.filter==='all'||(b.dataset.filter==='saved'?saved.includes(a.dataset.url):a.dataset.category===b.dataset.filter);a.hidden=!visible;if(visible)count++;});const empty=$('.empty-state');if(empty)empty.hidden=count!==0;}));
const sidebar=$('[data-sidebar]');if(sidebar)sidebar.addEventListener('click',()=>{const show=$('.sidebar').classList.toggle('visible');sidebar.setAttribute('aria-expanded',String(show));});
})();
/* Landing interactions: a rotating headline, real preview, and FAQ disclosures. */
(()=>{
 const demo=document.querySelector('.demo-dialog');
 document.querySelectorAll('[data-demo]').forEach(button=>button.addEventListener('click',()=>demo?.showModal()));
 const word=document.querySelector('[data-rotate-word]'),article=document.querySelector('[data-rotate-article]');
 if(word&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
  const companies=['Anthropic','Google','Microsoft','Meta','Stripe','Amazon','NVIDIA'];let index=0;
  setInterval(()=>{if(document.hidden||document.querySelector('dialog[open]'))return;word.classList.add('changing');setTimeout(()=>{index=(index+1)%companies.length;word.textContent=companies[index];if(article)article.textContent=/^[AEIOU]/.test(companies[index])?'an':'a';word.classList.remove('changing');},200);},3500);
 }
 document.querySelectorAll('.home .faq details').forEach(item=>item.addEventListener('toggle',()=>{if(item.open)document.querySelectorAll('.home .faq details[open]').forEach(other=>{if(other!==item)other.open=false;});}));
})();
