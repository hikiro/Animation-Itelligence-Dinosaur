#!/usr/bin/env python3
"""Dependency-free query tool for canonical missing/unverified source register."""
from pathlib import Path
import argparse,csv,json,sys
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--query',default='');p.add_argument('--id',default='');p.add_argument('--status',default='');p.add_argument('--priority',default='');p.add_argument('--list',action='store_true');p.add_argument('--json',action='store_true')
a=p.parse_args()
with (ROOT/'15_MISSING_AND_UNVERIFIED_SOURCES/REGISTER.csv').open(encoding='utf8',newline='') as f: rows=list(csv.DictReader(f))
q=a.query.casefold()
rows=[r for r in rows if (not a.id or r['id'].casefold()==a.id.casefold()) and (not a.status or r['status'].casefold()==a.status.casefold()) and (not a.priority or r['priority'].casefold()==a.priority.casefold()) and (not q or q in ' '.join(str(v) for v in r.values()).casefold())]
if a.json:print(json.dumps(rows,indent=2,ensure_ascii=False));sys.exit(0)
if not rows: print('No matching register entry. That does not prove the material exists or is accessible.');sys.exit(0)
for r in rows:
 print(f"{r['id']} [{r['status']}, {r['priority']}] {r['requested_material']}")
 if not a.list:
  print('  Why:',r['reason']);print('  Access:',r['access_attempt']);print('  Manual request:',r['user_can_provide']);print('  Related:',r['related_id'])
print('Matches:',len(rows))
