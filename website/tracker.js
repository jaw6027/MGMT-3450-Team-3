/* No network calls or TikTok SDK. All workspace data is local. */
(() => {
'use strict';
const KEY='profitlane-tiktok-v1', VERSION=1;
const categories=['Education','Industry tips','Engagement','Product concept','Brand awareness'];
const statuses=['Idea','Planned','Ready','Published'];
const metrics=['views','likes','comments','shares'];
const textLimits={title:140,description:4000,url:2048,notes:4000,hook:500,format:500,caption:2200,hashtags:500,cta:500};
const $=s=>document.querySelector(s);
const escape=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=n=>new Intl.NumberFormat('en-US').format(n);
const uid=()=>globalThis.crypto?.randomUUID?.()||`post-${Date.now()}-${Math.random().toString(36).slice(2)}`;
const dateLabel=d=>new Date(d+'T12:00:00').toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric'});
const validDate=s=>typeof s==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(s)&&s>='2000-01-01'&&s<='2100-12-31'&&!isNaN(new Date(s+'T00:00:00Z'))&&new Date(s+'T00:00:00Z').toISOString().slice(0,10)===s;
const rate=p=>metrics.every(k=>typeof p[k]==='number'&&Number.isFinite(p[k]))&&p.views>0?(p.likes+p.comments+p.shares)/p.views*100:null;
const rateText=p=>rate(p)===null?'—':rate(p).toFixed(2)+'%';
function seed(){
 const planned=window.PROFITLANE_CONTENT.calendar.filter(p=>p.activity==='Publish').map((p,i)=>({id:`launch-${p.day}`,title:p.title,description:p.message,date:p.date,category:p.category,status:i<2?'Ready':'Planned',url:'',views:null,likes:null,comments:null,shares:null,notes:'Launch plan, not published. Review claims and captions before recording.',hook:p.hook,format:p.format,caption:p.caption,hashtags:p.hashtags,cta:p.cta}));
 const examples=[['Demo: The total-mile check','2026-11-02','Education',1840,68,9,12],['Demo: What do you check first?','2026-11-04','Engagement',920,31,14,4],['Demo: Meet the mission','2026-11-06','Brand awareness',2460,96,11,15]].map((a,i)=>({id:`demo-${i}`,title:a[0],description:'FICTIONAL published example for learning the tracker. This video was not actually posted.',date:a[1],category:a[2],status:'Published',url:'',views:a[3],likes:a[4],comments:a[5],shares:a[6],notes:'Fictional cumulative results, illustrated as of November 7, 2026. Replace with your own measured data at launch. Next step: compare equal seven-day observation windows.',hook:'',format:'Demo example',caption:'Fictional workspace sample',hashtags:'#ProfitLane #TruckDispatch',cta:'Review the example.'}));
 return [...examples,...planned];
}
function normalize(raw){
 if(!raw||typeof raw!=='object'||Array.isArray(raw)) throw Error('Each post must be an object.');
 const p={id:typeof raw.id==='string'?raw.id:uid()};
 if(!p.id||p.id.length>100)throw Error('Invalid post identifier.');
 for(const [k,limit] of Object.entries(textLimits)){
  if(raw[k]!==undefined&&typeof raw[k]!=='string')throw Error(`${k} must be text.`);
  p[k]=(raw[k]||'').trim();if(p[k].length>limit)throw Error(`${k} exceeds ${limit} characters.`);
 }
 if(!p.title||!p.description)throw Error('A title and description are required.');
 if(!validDate(raw.date))throw Error('Use a valid date between 2000 and 2100.');p.date=raw.date;
 if(!categories.includes(raw.category)||!statuses.includes(raw.status))throw Error('Choose a supported category and status.');
 p.category=raw.category;p.status=raw.status;
 if(p.url){let u;try{u=new URL(p.url);}catch{throw Error('Enter a full HTTPS video URL.');}if(u.protocol!=='https:'||u.username||u.password)throw Error('Video URLs must use HTTPS without embedded credentials.');}
 for(const k of metrics){const n=raw[k];if(n!==null&&n!==undefined&&(!Number.isSafeInteger(n)||n<0||n>999999999999))throw Error('Counts must be nonnegative whole numbers below one trillion.');p[k]=n??null;}
 return p;
}
function decode(payload){if(!payload||payload.version!==VERSION||!Array.isArray(payload.posts)||payload.posts.length>2000)throw Error('Expected a version 1 backup with at most 2,000 posts.');const list=payload.posts.map(normalize);if(new Set(list.map(p=>p.id)).size!==list.length)throw Error('Duplicate post identifiers are not allowed.');return list;}
let posts=seed(), storageLocked=false, storageMessage='';
try{const saved=localStorage.getItem(KEY);if(saved!==null)posts=decode(JSON.parse(saved));}catch(e){storageLocked=true;storageMessage='Saved data could not be read. Samples are shown; existing storage is untouched. Edits are session-only. Import a valid backup or reset explicitly to recover.';}
function say(message,warning=false){$('#feedback').textContent=message;$('#feedback').classList.toggle('warning',warning);}
function persist(message){
 if(storageLocked){$('#storage-state').textContent='Session-only changes; export a backup.';say(`${message} Session only: saved storage is locked to preserve unreadable data. Export before leaving.`,true);return;}
 try{localStorage.setItem(KEY,JSON.stringify({version:VERSION,posts}));$('#storage-state').textContent='Edits save in this browser.';say(message);}
 catch{ $('#storage-state').textContent='Session-only changes; export a backup.';say(`${message} Browser storage is unavailable or full. Changes are session-only; export a backup before leaving.`,true); }
}
const form=$('#post-form'), editor=$('#post-dialog');let month=new Date(2026,10,1);let previousFocus=null;
for(const sel of ['#category-filter','select[name="category"]']){for(const c of categories){const op=document.createElement('option');op.value=c;op.textContent=c;$(sel).append(op);}}
function badge(s){return `<span class="status status-${s.toLowerCase()}">${escape(s)}</span>`;}
function bar(label,value,max,amber=false){return `<div><div class="bar-label"><span>${escape(label)}</span><strong>${fmt(value)}</strong></div><div class="bar-track"><div class="bar-fill ${amber?'amber-fill':''}" style="width:${max?Math.max(0,Math.min(100,value/max*100)):0}%"></div></div></div>`;}
function renderOverview(){
 const pub=posts.filter(p=>p.status==='Published'), complete=pub.filter(p=>rate(p)!==null),views=pub.reduce((s,p)=>s+(p.views??0),0),denom=complete.reduce((s,p)=>s+p.views,0),interactions=complete.reduce((s,p)=>s+p.likes+p.comments+p.shares,0),pooled=denom?`${(interactions/denom*100).toFixed(2)}%`:'—';
 const stats=[['In the library',fmt(posts.length),'All saved content'],['Published',fmt(pub.length),'Manual status · demo included'],['Total views',fmt(views),'Published · known counts only'],['Engagement by views',pooled,`${complete.length} complete Published posts · pooled`]];
 $('#stats').innerHTML=stats.map(a=>`<article class="stat"><span>${a[0]}</span><strong>${a[1]}</strong><small>${a[2]}</small></article>`).join('');
 const counts=statuses.map(s=>posts.filter(p=>p.status===s).length),max=Math.max(...counts,1);
 $('#status-chart').innerHTML=statuses.map((s,i)=>bar(s,counts[i],max,s==='Ready')).join('');
 const catViews=categories.map(c=>pub.filter(p=>p.category===c).reduce((s,p)=>s+(p.views??0),0)),vmax=Math.max(...catViews,1);
 $('#category-chart').innerHTML=categories.map((c,i)=>bar(c,catViews[i],vmax,i%2===0)).join('');
 const next=posts.filter(p=>p.status!=='Published').sort((a,b)=>a.date.localeCompare(b.date)).slice(0,3);
 $('#up-next').innerHTML=next.length?next.map(p=>{const d=new Date(p.date+'T12:00:00');return `<div class="up-item"><div class="up-date">${d.toLocaleDateString('en-US',{month:'short'})}<b>${d.getDate()}</b></div><div><button data-edit="${escape(p.id)}">${escape(p.title)}</button><small>${escape(p.category)} · ${escape(p.status)} · ${d.getFullYear()}</small></div></div>`;}).join(''):'<p>No unpublished posts. Add an idea to start the next plan.</p>';
}
function filtered(){const q=$('#search').value.trim().toLowerCase(),s=$('#status-filter').value,c=$('#category-filter').value,from=$('#date-from').value,to=$('#date-to').value;return posts.filter(p=>(!q||[p.title,p.description,p.notes,p.caption,p.hook,p.hashtags].join(' ').toLowerCase().includes(q))&&(!s||p.status===s)&&(!c||p.category===c)&&(!from||p.date>=from)&&(!to||p.date<=to)).sort((a,b)=>a.date.localeCompare(b.date)||a.title.localeCompare(b.title));}
function renderTable(){
 const list=filtered();$('#result-count').textContent=`${list.length} of ${posts.length} posts · chronological order`;
 $('#post-rows').innerHTML=list.length?list.map(p=>`<tr><td><strong>${escape(p.title)}</strong><p>${escape(p.description)}</p>${p.notes?`<details><summary>Notes & next steps</summary><p>${escape(p.notes)}</p></details>`:''}${p.url?`<a href="${escape(p.url)}" target="_blank" rel="noopener noreferrer">Open video ↗</a>`:'<small>No video URL</small>'}</td><td>${escape(dateLabel(p.date))}</td><td>${escape(p.category)}</td><td>${badge(p.status)}</td>${metrics.map(k=>`<td>${p[k]===null?'—':fmt(p[k])}</td>`).join('')}<td>${rateText(p)}</td><td><button data-edit="${escape(p.id)}" aria-label="Edit ${escape(p.title)}">Edit</button><button class="danger" data-delete="${escape(p.id)}" aria-label="Delete ${escape(p.title)}">Delete</button></td></tr>`).join(''):'<tr><td colspan="10">No matching posts. Clear filters or add a new idea.</td></tr>';
}
function isoDate(d){return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;}
function renderCalendar(){
 $('#month-title').textContent=month.toLocaleDateString('en-US',{month:'long',year:'numeric'});
 const offset=(month.getDay()+6)%7,start=new Date(month.getFullYear(),month.getMonth(),1-offset);
 let cells='';for(let i=0;i<42;i++){const d=new Date(start);d.setDate(start.getDate()+i);const key=isoDate(d),dayPosts=posts.filter(p=>p.date===key),prompts=window.PROFITLANE_CONTENT.calendar.filter(p=>p.date===key&&p.activity!=='Publish');cells+=`<div class="day-cell ${d.getMonth()!==month.getMonth()?'outside':''}" aria-label="${dateLabel(key)}"><span class="day-number">${d.getDate()}</span>${dayPosts.map(p=>`<button class="calendar-post" data-edit="${escape(p.id)}">● ${escape(p.title)}<br>${escape(p.status)}</button>`).join('')}${prompts.map(p=>`<button class="calendar-prompt" data-prompt="${p.day}">○ ${escape(p.activity)}<br>${escape(p.title)}</button>`).join('')}</div>`;}
 $('#calendar-grid').innerHTML=cells;
}
function render(){renderOverview();renderTable();renderCalendar();}
function openEditor(id){
 const p=id?posts.find(p=>p.id===id):null;if(id&&!p)return;
 previousFocus=document.activeElement;form.reset();$('#form-error').textContent='';form.querySelector('details').open=false;
 for(const name of ['id',...Object.keys(textLimits),'date','category','status',...metrics]){const el=form.elements.namedItem(name);if(el)el.value=p?.[name]??'';}
 if(!p){form.elements.category.value='Education';form.elements.status.value='Idea';form.elements.date.value=isoDate(new Date());}
 $('#editor-title').textContent=p?'Edit post':'New post';updateRate();editor.showModal();form.elements.title.focus();
}
function closeEditor(){editor.close();if(previousFocus?.isConnected)previousFocus.focus();else $('#add-post').focus();}
function updateRate(){const p={};for(const k of metrics){const v=form.elements[k].value;p[k]=v===''?null:Number(v);}$('#rate-preview').textContent=`Engagement: ${rateText(p)}${p.views===0?' · zero views: rate undefined':''}`;}
$('#add-post').addEventListener('click',()=>openEditor());$('#close-editor').addEventListener('click',closeEditor);$('#cancel-editor').addEventListener('click',closeEditor);metrics.forEach(k=>form.elements[k].addEventListener('input',updateRate));
form.addEventListener('submit',e=>{
 e.preventDefault();$('#form-error').textContent='';
 try{const raw=Object.fromEntries(new FormData(form));raw.id=raw.id||uid();for(const k of metrics)raw[k]=raw[k]===''?null:Number(raw[k]);const p=normalize(raw),index=posts.findIndex(x=>x.id===p.id);if(index<0){if(posts.length>=2000)throw Error('Workspace limit: 2,000 posts. Export a backup before removing old posts.');posts.push(p);}else posts[index]=p;persist('Post saved.');render();closeEditor();}
 catch(err){$('#form-error').textContent=err.message;}
});
document.addEventListener('click',e=>{
 const edit=e.target.closest('[data-edit]');if(edit){openEditor(edit.dataset.edit);return;}
 const del=e.target.closest('[data-delete]');if(del){const p=posts.find(x=>x.id===del.dataset.delete);if(p&&confirm(`Delete “${p.title}”? Export a backup first if you may need it later.`)){posts=posts.filter(x=>x.id!==p.id);persist('Post deleted.');render();}return;}
 const prompt=e.target.closest('[data-prompt]');if(prompt){const p=window.PROFITLANE_CONTENT.calendar.find(x=>x.day===Number(prompt.dataset.prompt));if(!p)return;$('#prompt-title').textContent=`Day ${p.day} · ${p.title}`;$('#prompt-content').innerHTML=`<p><strong>${dateLabel(p.date)} · ${escape(p.activity)}</strong></p>`+[['Category',p.category],['Hook',p.hook],['Format',p.format],['Main message',p.message],['Caption',p.caption],['Hashtags',p.hashtags],['Call to action',p.cta]].map(([k,v])=>`<p><strong>${k}:</strong> ${escape(v)}</p>`).join('')+(p.activity!=='Publish'?'<p>This is a preparation or review day. Use the concept as a reserve idea, not an extra publishing requirement.</p>':'<p>The post library holds your editable publishing record. This is the original reference plan.</p>');$('#prompt-dialog').showModal();}
});
$('#close-prompt').addEventListener('click',()=>$('#prompt-dialog').close());
for(const selector of ['#search','#status-filter','#category-filter','#date-from','#date-to'])$(selector).addEventListener('input',renderTable);
$('#clear-filters').addEventListener('click',()=>{for(const s of ['#search','#status-filter','#category-filter','#date-from','#date-to'])$(s).value='';renderTable();});
$('#prev-month').addEventListener('click',()=>{month=new Date(month.getFullYear(),month.getMonth()-1,1);renderCalendar();});$('#next-month').addEventListener('click',()=>{month=new Date(month.getFullYear(),month.getMonth()+1,1);renderCalendar();});$('#launch-month').addEventListener('click',()=>{month=new Date(2026,10,1);renderCalendar();});
$('#daily-plan').innerHTML=window.PROFITLANE_CONTENT.calendar.map(p=>`<button class="plan-card" data-prompt="${p.day}"><small>DAY ${String(p.day).padStart(2,'0')} · ${dateLabel(p.date)}</small><b>${escape(p.title)}</b><span>${escape(p.activity)} · ${escape(p.category)}</span></button>`).join('');
const timecode=n=>`${String(Math.floor(n/60)).padStart(2,'0')}:${String(n%60).padStart(2,'0')}`;
$('#scripts').innerHTML=window.PROFITLANE_CONTENT.scripts.map(p=>`<details class="video-script" data-video="${p.number}"><summary><span>${String(p.number).padStart(2,'0')} · ${escape(p.title)}</span> <span class="script-duration">${escape(p.length)}</span></summary><p class="script-meta">${dateLabel(p.date)} · ${p.word_count} spoken words · ${escape(p.format)}</p><div class="production-brief">${[['Creative concept',p.concept],['Purpose',p.purpose],['Cast / roles',p.cast],['Props / materials',p.props],['Low-budget setup',p.setup]].map(([k,v])=>`<p><strong>${k}</strong><br>${escape(v)}</p>`).join('')}</div><p class="script-reader-note">Read only your role’s SAY lines. SHOW, CAMERA, EDIT, SOUND and ON-SCREEN TEXT are directions, not dialogue. Timecodes are rehearsal targets including visual holds. Angel’s lines are draft wording for his approval, not historical quotations.</p><ol class="script-timeline">${p.beats.map(b=>`<li class="script-beat"><h3>${timecode(b.start)}–${timecode(b.end)}</h3><div class="spoken-block"><span class="script-label">SAY</span>${b.dialogue.map(d=>`<p class="spoken-line" data-speaker="${escape(d.speaker)}"><strong>${escape(d.speaker)}:</strong> ${escape(d.line)}</p>`).join('')}</div><div class="visual-directions">${[['SHOW / ACTION',b.visual],['CAMERA / ANGLE',b.camera],['TRANSITION / GRAPHICS',b.edit],['ON-SCREEN TEXT',b.text],['SOUND / DELIVERY',b.audio]].map(([k,v])=>`<p><strong>${k}</strong><br>${escape(v)}</p>`).join('')}</div></li>`).join('')}</ol>${[['Caption',p.caption],['Hashtags',p.hashtags],['Natural CTA / production condition',p.cta]].map(([k,v])=>`<p><strong>${k}:</strong> ${escape(v)}</p>`).join('')}</details>`).join('');

$('#export').addEventListener('click',()=>{const blob=new Blob([JSON.stringify({version:VERSION,exportedAt:new Date().toISOString(),posts},null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=`profitlane-tiktok-${isoDate(new Date())}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);say('Backup downloaded. Keep it somewhere safe; it contains your current workspace, not the reference documents.');});
$('#import').addEventListener('change',async e=>{const file=e.target.files[0];if(!file)return;try{if(file.size>5000000)throw Error('Backup is too large (maximum 5 MB).');const list=decode(JSON.parse(await file.text()));if(confirm(`Replace this workspace with ${list.length} imported posts? Export current work first if needed.`)){posts=list;storageLocked=false;persist('Backup imported.');render();}}catch(err){say(`Import rejected: ${err.message} No posts were replaced.`,true);}finally{e.target.value='';}});
$('#reset-demo').addEventListener('click',()=>{if(confirm('Replace all current posts with fictional sample data? This cannot be undone without a backup.')){posts=seed();storageLocked=false;persist('Sample data restored.');render();}});
window.addEventListener('storage',e=>{if(e.key===KEY)say('This workspace changed in another tab. Export this tab before reloading if you have unsaved work. Avoid editing in multiple tabs.',true);});
const titles={overview:['Your content, in motion.','A clear plan. Useful conversations. One post at a time.'],calendar:['Make room for good content.','A sustainable launch rhythm, from first idea to final review.'],posts:['From idea to conversation.','Plan the post, record the result, decide what comes next.'],playbook:['A practical start for ProfitLane.','The mission, the plan and the first ten videos—ready for your review.']};
function route(){let v=location.hash.slice(1);if(!titles[v])v='overview';for(const key of Object.keys(titles))$(`#${key}-view`).hidden=key!==v;document.querySelectorAll('[data-view]').forEach(a=>{if(a.dataset.view===v)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});$('#page-title').textContent=titles[v][0];$('#page-subtitle').textContent=titles[v][1];document.title=`ProfitLane · ${v[0].toUpperCase()+v.slice(1)} · TikTok studio`;}
window.addEventListener('hashchange',route);render();route();if(storageMessage){$('#storage-state').textContent='Session only; existing storage could not be read.';say(storageMessage,true);}
})();
