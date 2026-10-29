#!/usr/bin/env python3
"""Build static assets from the audited tables; no dependencies or network calls."""
from pathlib import Path
from collections import Counter
import csv, hashlib, html, json, shutil
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
DOMAINS={'noise':'Noise','light':'Light control','temperature':'Temperature','bedding':'Bedding','choice':'Guest choice'}
LABELS={'specific':'Specific','vague':'Vague','not_stated':'Not stated','not_accessible':'Not accessible'}
SYMBOLS={'specific':'S','vague':'V','not_stated':'—','not_accessible':'?'}
def read(name):return json.loads((ROOT/'data'/name).read_text())
def esc(s):return html.escape(str(s),quote=True)
def build():
 props=read('properties.json'); obs=read('observations.json');sources=read('sources.json');lit=read('literature.json'); source_map={s['source_id']:s for s in sources}
 candidates=list(csv.DictReader((ROOT/'data/candidate-panel.csv').open()))
 summary={'pilot_properties':len(props),'target_candidates':len(candidates),'observations':len(obs),'source_urls':len(sources),'overall':{s:sum(r['status']==s for r in obs) for s in LABELS},'by_domain':{d:{s:sum(r['domain']==d and r['status']==s for r in obs) for s in LABELS} for d in DOMAINS},'claim_quality_sensitivity':{'primary_specific':sum(r['status']=='specific' for r in obs),'looser_bedding_adjectives_specific':sum(r['status']=='specific' for r in obs)+sum(r['domain']=='bedding' and r['status']=='vague' for r in obs)}}
 (ROOT/'data/summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 data={'properties':props,'observations':obs,'sources':sources,'literature':lit,'summary':summary}
 (SITE/'data/pilot.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 rows=''
 for p in props:
  cells=''
  for d in DOMAINS:
   r=next(r for r in obs if r['property_id']==p['property_id'] and r['domain']==d);s=r['status'];label=LABELS[s]
   cells+=f'<td data-domain="{d}"><a class="cell {s}" href="#evidence-{r["observation_id"]}" data-observation="{r["observation_id"]}" aria-label="{esc(p["short_name"])}: {DOMAINS[d]}, {label}. Read evidence"><span class="symbol" aria-hidden="true">{SYMBOLS[s]}</span><span>{label}</span></a></td>'
  rows+=f'<tr><th scope="row"><span>{esc(p["short_name"])}</span><small>{esc(p["access"])}</small></th>{cells}</tr>'
 cards=''
 for p in props:
  entries=''
  for r in (r for r in obs if r['property_id']==p['property_id']):
   links=' · '.join(f'<a href="{esc(source_map[i]["url"])}">{esc(i)} — {esc(source_map[i]["title"])}</a>' for i in r['source_ids'])
   quote=f'<blockquote>{esc(r["evidence_excerpt"])}</blockquote>' if r['evidence_excerpt'] else ''
   entries+=f'<article class="evidence-entry" id="evidence-{r["observation_id"]}"><h4>{DOMAINS[r["domain"]]} <span class="badge {r["status"]}">{LABELS[r["status"]]}</span></h4>{quote}<p>{esc(r["rationale"])}</p><p class="fine">{esc(r["access_caveat"])}</p><p class="source-links">{links}</p><p class="fine">Scope: {esc(r["scope"])} · Locator: {esc(r["locator"])}</p></article>'
  cards+=f'<details class="property-record"><summary>{esc(p["name"])}<span>5 observations ↗</span></summary><p class="fine">{esc(p["address"])}. {esc(p["eligibility"])}</p>{entries}</details>'
 lit_html=''
 for l in lit:
  lit_html+=f'<article class="paper"><p class="eyebrow">{l["year"]} / {esc(l["id"])}</p><h3><a href="{esc(l["url"])}">{esc(l["title"])}</a></h3><p>{esc(l["design"])}.</p><p class="fine"><strong>Access:</strong> {esc(l["access"])}.</p><p class="fine">{esc(l["limitations"])}</p></article>'
 src_html=''.join(f'<li><a href="{esc(s["url"])}">{s["source_id"]} — {esc(s["title"])}</a><span>{esc(s["access_depth"].replace("_"," "))}</span><p>{esc(s["access_note"])}</p></li>' for s in sources)
 template=(ROOT/'scripts/template.html').read_text()
 for key,val in {'MATRIX_ROWS':rows,'EVIDENCE_CARDS':cards,'LITERATURE':lit_html,'SOURCE_LIST':src_html}.items():template=template.replace('{{'+key+'}}',val)
 (SITE/'index.html').write_text(template)
 dl=SITE/'downloads';dl.mkdir(exist_ok=True)
 for f in (ROOT/'data').iterdir():
  if f.is_file():shutil.copy2(f,dl/f.name)
 for f in (ROOT/'docs').glob('*.md'):shutil.copy2(f,dl/f.name)
 shutil.copy2(ROOT/'evidence/sha256sums.txt',dl/'evidence-note-checksums.sha256')
 with (dl/'checksums.sha256').open('w') as out:
  for f in sorted(dl.iterdir()):
   if f.is_file() and f.name!='checksums.sha256':out.write(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.name+'\n')
 print(f'Built site: {len(props)} hotels, {len(obs)} observations, {len(sources)} URL records.')
 return summary
if __name__=='__main__':build()
