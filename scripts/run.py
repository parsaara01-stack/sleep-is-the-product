#!/usr/bin/env python3
"""One-command build, integrity validation and loopback preview."""
import argparse,http.server,functools
from build import build,ROOT
from validate import validate
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8783);args=p.parse_args()
 build();validate()
 handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT/'site'))
 with http.server.ThreadingHTTPServer(('127.0.0.1',args.port),handler) as server:
  print(f'Sleep Is the Product: http://127.0.0.1:{args.port}',flush=True)
  try:server.serve_forever()
  except KeyboardInterrupt:pass
