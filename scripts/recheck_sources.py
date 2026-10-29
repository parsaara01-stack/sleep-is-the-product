#!/usr/bin/env python3
"""Optional ordinary HTTPS access check; never changes coding or disables TLS."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import argparse,hashlib,json,urllib.request,urllib.error
ROOT=Path(__file__).resolve().parents[1]
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
def check(s):
 result={'source_id':s['source_id'],'url':s['url'],'started_at_utc':now(),'method':'Python urllib HTTPS GET; default certificate validation','coding_changed':False}
 try:
  req=urllib.request.Request(s['url'],headers={'User-Agent':'SleepIsTheProductResearch/0.1 (read-only public-page access check)'})
  with urllib.request.urlopen(req,timeout=12) as r:
   content=r.read(5000000)
   result.update(http_status=r.status,final_url=r.url,response_bytes=len(content),sha256_response_bytes=hashlib.sha256(content).hexdigest(),content_type=r.headers.get('Content-Type',''),limit_bytes=5000000)
 except Exception as e:result['error']=str(e)
 result['completed_at_utc']=now();return result
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',default='work/access-recheck.json');args=parser.parse_args()
 sources=json.loads((ROOT/'data/sources.json').read_text())
 with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(check,sources))
 output=Path(args.output);output=output if output.is_absolute() else ROOT/output
 output.parent.mkdir(parents=True,exist_ok=True)
 output.write_text(json.dumps({'purpose':'Supplementary HTTP access diagnostics; not page-content verification or updated coding','results':results},indent=2)+'\n')
 print(f'Wrote {len(results)} ordinary HTTPS diagnostics to {output}; coding unchanged.')
