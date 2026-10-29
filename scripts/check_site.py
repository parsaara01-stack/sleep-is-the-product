#!/usr/bin/env python3
"""Check local assets, downloads and fragment routes; optional live HTTP check."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import argparse,urllib.request
ROOT=Path(__file__).resolve().parents[1]/'site'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  for key in ('href','src'):
   if a.get(key):self.links.append(a[key])
def check(base_url=None):
 p=Page();p.feed((ROOT/'index.html').read_text())
 assert len(p.ids)==len(set(p.ids)),'Duplicate HTML IDs'
 assert p.h1==1
 paths={'index.html','data/pilot.json'}
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  if u.path:
   path=unquote(u.path);assert (ROOT/path).is_file(),f'Missing local route: {path}';paths.add(path)
  if u.fragment:assert u.fragment in p.ids,f'Missing fragment: {u.fragment}'
 if base_url:
  for path in sorted(paths):
   with urllib.request.urlopen(base_url.rstrip('/')+'/'+path,timeout=5) as r:assert r.status==200
 print(f'PASS: unique anchors, one h1, {len(paths)} local routes/assets/downloads'+(' returning HTTP 200.' if base_url else ' present.'))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-url');args=p.parse_args();check(args.base_url)
