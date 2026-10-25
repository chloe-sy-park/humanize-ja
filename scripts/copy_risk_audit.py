#!/usr/bin/env python3
"""Lightweight, deliberately non-authoritative Japanese promotional-copy risk flags.

No semantic inference, legal judgment, marketing lift scoring, or valid compliance PASS.
Use for editorial triage only; examine images, landing page, approvals and actual facts.
"""
import argparse
import json
import re
import sys
from pathlib import Path

RULES = [
    ('superlative_or_ranking', r'(?<![A-Za-z])(?:No\.?1|Ｎｏ．１|業界[一最]|日本一|世界一|最安|絶対|必ず|100[%％]|１００[%％])', 'HOLD-CLAIM', 'Substantiate scope, measurement, comparison and exceptions.'),
    ('outcome_or_speed', r'(?:即効|[0-9０-９]+日(?:で|以内に)|効果[がを]|満足度|売上[がを]|生産性[がを])', 'REVIEW', 'Check outcome basis, before/after context, product and timeframe.'),
    ('discount_terms', r'(?:[0-9０-９]+[%％]OFF|半額|通常価格|期間限定|今だけ|本日限り|無料体験|初回無料|永久無料|永年無料)', 'HOLD-OFFER', 'Verify current and former price, history, period, scope and continuation conditions.'),
    ('testimonial', r'(?:お客様の声|利用者(?:の声|の感想)|口コミ|実際に使ってみた|体験談)', 'REVIEW', 'Confirm authenticity, attribution, editing and sponsor context.'),
    ('medical_effect', r'(?:治療|治る|完治|病気が防げる|ニキビを治す|シミが消える|肌が再生|発毛する|医師(?:も|が)認め)', 'HOLD-CLAIM', 'Product classification and allowed/approved claims must be checked.'),
    ('sponsor_keyword', r'(?:#PR|#広告|スポンサー|提供：|タイアップ)', 'REVIEW', 'Disclosure keywords alone do not establish sufficient prominence or correct disclosure.'),
    ('urgent_subject', r'(?:【至急】|【重要】|至急ご対応|緊急のお願い)', 'REVIEW', 'Confirm urgency is genuine and subject describes the actual request.'),
]

def audit(text, mode='marketing-copy', industry='general'):
    warnings=[]
    for name,pattern,risk,reason in RULES:
        if mode == 'business-email' and name in ('superlative_or_ranking','outcome_or_speed','discount_terms','testimonial','medical_effect','sponsor_keyword'):
            # Only apply commercial-claim checks to business-email when these indicators appear.
            # The heuristic intentionally retains hits, but explains context dependence below.
            pass
        for match in list(re.finditer(pattern,text,re.I))[:20]:
            if name=='medical_effect' and industry=='general':
                risk='REVIEW'
            warnings.append({'rule':name,'match':match.group(0),'offset':match.start(),'suggested_risk':risk,
                'guidance':reason,'auto_violation_finding':False})
    if mode=='business-email':
        if '件名' not in text and 'Subject:' not in text:
            warnings.append({'rule':'subject_not_present','match':None,'offset':None,
                'suggested_risk':'REVIEW','guidance':'If this is a full email, confirm the subject is specific; snippets may omit it.',
                'auto_violation_finding':False})
        if not re.search(r'お世話になっております|初めてご連絡|ご連絡いたします|いつもありがとうございます', text):
            # Absence of a formula is NOT proof of impoliteness.
            pass
    notes=['Keyword matches indicate REVIEW CANDIDATES, not factual falsity or legal violations.',
           'The tool cannot know permissions, product approval, testimonial authenticity, layout visibility or sending consent.',
           'No findings does not constitute a legal, platform or factual pass.']
    if industry in ('beauty','health'):
        notes.append('Category-sensitive statements require external product classification and approved claim review, including visuals.')
    if mode=='business-email':
        notes.append('Business emails are not automatically promotional; opt-in/exception depends on purpose and recipients.')
    return {'mode':mode,'industry':industry,'status':'REVIEW_NEEDED' if warnings else 'NO_KEYWORD_FLAGS',
        'flags':warnings,'notes':notes,'legal_compliance':None,'ai_authorship_probability':None}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('file', help='UTF-8 file path or - for stdin')
    p.add_argument('--mode',choices=['marketing-copy','ad-copy','business-email'],default='marketing-copy')
    p.add_argument('--industry',choices=['general','beauty','health'],default='general')
    p.add_argument('--json',action='store_true')
    a=p.parse_args()
    body=sys.stdin.read() if a.file=='-' else Path(a.file).read_text(encoding='utf-8')
    report=audit(body,a.mode,a.industry)
    if a.json:
        print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(f"{report['mode']} ({report['industry']}) — {report['status']}")
        for x in report['flags']:
            print(f"- {x['suggested_risk']} {x['rule']}: {x['match']!r} @ {x['offset']}")
        for n in report['notes']:
            print('NOTE:',n)

if __name__=='__main__':
    main()
