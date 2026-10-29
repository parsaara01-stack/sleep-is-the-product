#!/usr/bin/env python3
"""Meaningful data/provenance checks, deliberately independent of rendering."""
from pathlib import Path
from datetime import datetime
import csv,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def validate():
 def read(name):return json.loads((ROOT/'data'/name).read_text())
 obs=read('observations.json');sources=read('sources.json');props=read('properties.json');sm={s['source_id']:s for s in sources}
 panel=list(csv.DictReader((ROOT/'data/candidate-panel.csv').open()))
 assert len(panel)==30 and len({r['candidate_id'] for r in panel})==30
 assert len(props)==5 and len(obs)==25
 assert {p['property_id'] for p in props}=={r['candidate_id'] for r in panel if r['stage']=='pilot'}
 assert sorted(r['name'] for r in panel)[:5]==[r['name'] for r in panel if r['stage']=='pilot']
 assert len({r['observation_id'] for r in obs})==25
 for p in props:
  rr=[r for r in obs if r['property_id']==p['property_id']]
  assert {r['domain'] for r in rr}=={'noise','light','temperature','bedding','choice'}
  assert len(p['source_ids'])<=4
 for s in sources:
  assert s['url'].startswith('https://')
  assert len(s['evidence_excerpt'].split())<=25
  assert datetime.fromisoformat(s['retrieval_window_start_utc'].replace('Z','+00:00'))<datetime.fromisoformat(s['retrieval_window_end_utc'].replace('Z','+00:00'))
  assert json.loads((ROOT/'evidence'/f"{s['source_id']}.json").read_text())==s
 for r in obs:
  assert r['disclosure_status']=={'not_stated':'not_found_in_review','not_accessible':'undetermined'}.get(r['status'],r['status'])
  assert r['access_coverage'] in {'partial','unavailable','reviewed_text_only'}
  assert r['verification_status']=='not_independently_verified'
  assert r['status'] in {'specific','vague','not_stated','not_accessible'}
  assert r['source_ids'] and all(i in sm and sm[i]['property_id']==r['property_id'] for i in r['source_ids'])
  if r['status'] in {'specific','vague'}:
   assert r['evidence_excerpt'] and any(r['evidence_excerpt']==sm[i]['evidence_excerpt'] and sm[i]['access_depth'] in {'page_text','page_text_partial'} for i in r['source_ids'])
  else:assert r['evidence_excerpt']==''
  if all(sm[i]['access_depth'].startswith('unavailable') for i in r['source_ids']):assert r['status']=='not_accessible'
 for line in (ROOT/'evidence/sha256sums.txt').read_text().splitlines():
  digest,name=line.split('  ',1);assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
 csvobs=list(csv.DictReader((ROOT/'data/observations.csv').open()))
 assert len(csvobs)==len(obs)
 for a,b in zip(obs,csvobs):
  assert {**a,'source_ids':';'.join(a['source_ids'])}==b
 summary=read('summary.json')
 for status,count in summary['overall'].items():assert count==sum(r['status']==status for r in obs)
 assert sum(summary['overall'].values())==25
 for domain,counts in summary['by_domain'].items():
  assert sum(counts.values())==5
  for status,count in counts.items():assert count==sum(r['domain']==domain and r['status']==status for r in obs)
 bundled=json.loads((ROOT/'site/data/pilot.json').read_text())
 assert bundled['study']==read('study.json')
 assert bundled['properties']==props and bundled['literature']==read('literature.json')
 assert bundled['observations']==obs and bundled['sources']==sources and bundled['summary']==summary
 page=(ROOT/'site/index.html').read_text()
 assert '{{' not in page and 'Exploratory pilot' in page
 assert all(f'id="evidence-{r["observation_id"]}"' in page for r in obs)
 for name in ['observations.csv','sources.json','protocol.md','methods.md','data-dictionary.md']:
  assert (ROOT/'site/downloads'/name).is_file()
 print('PASS: sample/keys, five domains, 25 rows, access-state safeguards, positive-claim provenance, excerpt limits, note hashes, CSV parity, aggregate denominators, site/data parity and static evidence anchors.')
if __name__=='__main__':validate()
