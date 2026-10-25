#!/usr/bin/env python3
"""Offline Markdown local-link check. Remote URLs are not fetched or certified."""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)')
CODE_BLOCK_RE = re.compile(r'^\s*```')

def clean_markdown(text):
    # Remove fenced code blocks so that code examples are not mistaken for links.
    lines=[]
    in_code=False
    for line in text.splitlines():
        if CODE_BLOCK_RE.match(line):
            in_code=not in_code
            continue
        if not in_code:
            lines.append(line)
    return '\n'.join(lines)

def check():
    errors=[]
    checked=0
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in LINK_RE.findall(clean_markdown(path.read_text(encoding='utf-8'))):
            if target.startswith(('http://','https://','mailto:','tel:','#','data:')):
                continue
            checked+=1
            loc=unquote(target.split('#',1)[0].split('?',1)[0])
            if not loc:
                continue
            resolved=(path.parent/loc).resolve()
            if ROOT.resolve() not in resolved.parents and resolved!=ROOT.resolve():
                errors.append(f'{path.relative_to(ROOT)}: outside repository: {target}')
            elif not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing: {target}')
    return checked,errors

if __name__=='__main__':
    count,errors=check()
    print(f'Checked {count} local Markdown links; errors: {len(errors)}')
    for error in errors:
        print('ERROR:',error)
    sys.exit(1 if errors else 0)
