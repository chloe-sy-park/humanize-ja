#!/usr/bin/env python3
"""Offline structural validation. Does not validate upstream citations or writing quality."""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
'SKILL.md','README.md','README.ko.md','docs/INSTALL_JA.md','docs/EXAMPLES_JA.md','docs/FAQ_JA.md','docs/PUBLISH_CHECKLIST_JA.md','docs/PUBLISH_KO.md','docs/RELEASE_NOTES_JA.md','.github/workflows/ci.yml','LICENSE','THIRD_PARTY_NOTICES.md','REFERENCES.md',
'CHANGELOG.md','CONTRIBUTING.md','research/UPSTREAM_COMPARISON.md',
'research/JP_STYLE_BENCHMARK.md','references/pattern-audit.md',
'references/anti-patterns-ja.md','references/japanese-style-and-keigo.md',
'references/channels-ja.md','references/truth-gate.md',
'references/founder-structures.md','references/founder-trust-audit.md',
'references/adversarial-review.md','references/scorecard.md',
'references/upstream-crosswalk.md','profiles/japanese-founder.md',
'profiles/jp-marketer.md','profiles/jp-business-media.md',
'examples/founder-before-after.md','examples/marketer-before-after.md',
'examples/media-before-after.md','examples/email-before-after.md',
'examples/sample_input_ja.txt','scripts/diagnose.py','scripts/claim_guard.py',
'tests/test_diagnose.py','tests/test_claim_guard.py','tests/before.txt','tests/after.txt',
'references/jp-marketing-copy.md','references/jp-ad-copy.md','references/jp-business-email.md',
'references/jp-claims-compliance.md','references/localization-ja.md','references/review-matrix.md',
'profiles/jp-brand-copy.md','examples/marketing-lp-before-after.md',
'examples/ads-platform-before-after.md','examples/client-email-3-cases.md',
'research/JP_MARKETING_EMAIL_BENCHMARK.md','scripts/copy_risk_audit.py','tests/test_copy_risk_audit.py',
'research/JP_COSMETICS_COPY_AUDIT_20.md','research/BRAND_VS_AI_PAIRED_10.md','research/cosmetics_copy_20.json','research/COPY_RULE_EXECUTION_20.json','research/REPORT_20_CASES.html',
'references/brand-voice-campaign-ja.md','references/jp-beauty-claim-scope.md','references/paired-benchmark-protocol.md',
'scripts/campaign_audit_v12.py','tests/test_campaign_audit_v12.py']

def check():
    issues=[]
    for rel in REQUIRED:
        path=ROOT/rel
        if not path.is_file() or path.stat().st_size==0:
            issues.append(f'missing/empty: {rel}')
    meta=(ROOT/'SKILL.md').read_text(encoding='utf-8')
    if not re.search(r'^---\s*\nname: humanize-ja\s*\n',meta):
        issues.append('bad YAML front matter/name')
    if not re.search(r'^\s*version: 1\.2\.0\s*$',meta,re.M):
        issues.append('missing version 1.2.0')
    for name in ('UPSTREAM_COMPARISON.md','JP_STYLE_BENCHMARK.md','JP_MARKETING_EMAIL_BENCHMARK.md','JP_COSMETICS_COPY_AUDIT_20.md','BRAND_VS_AI_PAIRED_10.md'):
        if len((ROOT/'research'/name).read_text(encoding='utf-8').splitlines())<40:
            issues.append(f'analysis too short: {name}')
    files=list(ROOT.rglob('*'))
    return issues, sum(p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts for p in files)

if __name__=='__main__':
    errors,count=check()
    print(f'Files: {count}; required: {len(REQUIRED)}; errors: {len(errors)}')
    for e in errors: print('ERROR:',e)
    sys.exit(1 if errors else 0)
