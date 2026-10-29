(() => {
  'use strict';
  const labels={specific:'Specific',vague:'Vague',not_stated:'Not stated',not_accessible:'Not accessible'};
  const domains={noise:'Noise',light:'Light control',temperature:'Temperature',bedding:'Bedding',choice:'Guest choice'};
  const get=id=>document.getElementById(id);
  const node=(tag,text,cls)=>{const el=document.createElement(tag);if(text)el.textContent=text;if(cls)el.className=cls;return el;};
  let data;
  function showObservation(id,moveFocus=false){
    if(!data)return;
    const r=data.observations.find(x=>x.observation_id===id);
    if(!r)return;
    const p=data.properties.find(x=>x.property_id===r.property_id);
    get('inspector-title').textContent=`${p.short_name} / ${domains[r.domain]}`;
    get('inspector-status').textContent=labels[r.status];
    get('inspector-status').className=`badge ${r.status}`;
    const body=get('inspector-body');body.replaceChildren();
    if(r.evidence_excerpt)body.append(node('blockquote',r.evidence_excerpt));
    body.append(node('p',r.rationale),node('p',r.access_caveat,'fine'),node('p',`Scope: ${r.scope}. Retrieval window: October 29, 2026, 18:55–19:01 UTC.`,'fine'));
    const links=node('p',null,'source-links');
    r.source_ids.forEach((id,index)=>{const s=data.sources.find(x=>x.source_id===id);if(index)links.append(document.createTextNode(' · '));const a=node('a',`${id} — ${s.title} ↗`);a.href=s.url;links.append(a);});body.append(links);
    body.append(node('p',`Locator: ${r.locator}`,'fine'));
    document.querySelectorAll('[data-observation]').forEach(a=>{const selected=a.dataset.observation===id;a.classList.toggle('selected',selected);if(selected)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current');});
    if(moveFocus){get('inspector').focus({preventScroll:true});get('inspector').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'nearest'});}
  }
  function focusDomain(domain){
    document.querySelectorAll('[data-focus]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.focus===domain)));
    document.querySelectorAll('[data-domain]').forEach(cell=>cell.classList.toggle('focused-column',cell.dataset.domain===domain));
    const counts=domain==='all'?data.summary.overall:data.summary.by_domain[domain];
    get('readout-title').textContent=domain==='all'?'All five domains / 25 cells':`${domains[domain]} / 5 properties`;
    get('readout-counts').textContent=`${counts.specific} specific · ${counts.vague} vague · ${counts.not_stated} not stated · ${counts.not_accessible} not accessible`;
    get('readout-note').textContent=domain==='all'?'Descriptive counts for these pages only. No overall score or hotel ranking.':'Each category stays separate. These counts describe the five reviewed properties, not Milwaukee as a whole.';
  }
  // Static matrix links stay usable if the data request fails or JavaScript is disabled.
  document.querySelectorAll('a[data-observation]').forEach(a=>a.addEventListener('click',e=>{if(!data){const target=get(a.hash.slice(1));if(target)target.closest('details').open=true;return;}e.preventDefault();showObservation(a.dataset.observation,true);}));
  function openHashRecord(){const id=location.hash.slice(1),target=get(id);if(target&&target.closest('details')){target.closest('details').open=true;requestAnimationFrame(()=>target.scrollIntoView());}}
  window.addEventListener('hashchange',openHashRecord);openHashRecord();
  fetch('data/pilot.json').then(r=>{if(!r.ok)throw Error('Data unavailable');return r.json();}).then(result=>{data=result;document.querySelectorAll('[data-focus]').forEach(b=>b.addEventListener('click',()=>focusDomain(b.dataset.focus)));showObservation('H04-noise');}).catch(()=>{get('readout-note').textContent='Interactive data could not load. The static matrix, full records and downloads below remain available.';document.querySelectorAll('[data-focus]').forEach(b=>b.disabled=true);});
})();
