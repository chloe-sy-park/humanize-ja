#!/usr/bin/env python3
"""v1.2 cosmetic copy triage: keyword WARNINGS + external context. NEVER pass/fail law or prove AI source.

Input: text file, optionally --context product|campaign, --known-product-class cosmetics|quasi-drug|unknown.
Output: suspected claims and contextual questions; no changes to source text.
"""
import argparse, json, re, sys
from pathlib import Path

RULES = (
    ('rank_scope',r'(?:No[.．]?\s*[１1]|最高峰|日本一|世界一|業界(?:初|最高)|売上(?:No[.．]?\s*[１1]|第[１1]位))','REVIEW-EVIDENCE','比較母集団・期間・商品定義・統計出典・注記を確かめる'),
    ('quantified_metaphor',r'(?:[0-9０-９]+\s*時間(?:多く|長く)|\+\s*[0-9０-９]+\s*時間|[0-9０-９]+\s*(?:兆|億|万)個|[0-9０-９]+\s*[%％])','REVIEW-EVIDENCE','数字の実測・換算条件・比喩・比較対象の区別を確認する'),
    ('claim_scope',r'(?:浸透|角層|真皮|美白|シワ改善|再生|修復|治る|完治)','REVIEW-SCOPE','商品区分、承認効能、到達範囲、注記とビジュアルの一体性を確認する'),
    ('guarantee',r'(?:絶対|必ず|確実|一度で|永久|全員|ひとつ残らず)','REVIEW-CONTEXT','ブランド理念か商品保証かを区別し、誤認の可能性を確認する'),
    ('offer',r'(?:初回(?:無料|半額)|期間限定|[0-9０-９]+\s*[%％]OFF|送料無料|定期購入)','REVIEW-OFFER','価格・適用対象・期間・税・継続条件を確認する'),
)

BRAND_STYLE = re.compile(r'(?:つや玉|セラミドケア|NO MORE RULES|肌にスキ|全方位ファンデーション)')

def audit(text,context='product',product_class='unknown'):
    flags=[]
    for category,regex,status,action in RULES:
        for m in list(re.finditer(regex,text,re.I))[:30]:
            flags.append({'category':category,'span':m.group(),'status':status,'question':action,'automatic_illegality':False})
    for m in list(BRAND_STYLE.finditer(text))[:30]:
        flags.append({'category':'protected_brand_term','span':m.group(),'status':'PRESERVE-VOICE','question':'ブランド固有語の表記・意味を維持（効能許諾の証拠ではない）','automatic_illegality':False})
    return {'context':context,'product_class':product_class,'flags':flags,
            'status':'CONTEXT_REVIEW_REQUIRED' if any(f['status'].startswith('REVIEW') for f in flags) else 'NO_AUTOMATED_CLAIM_FLAGS',
            'limitations':['語の有無では法違反も適法性も判定できない','公式ブランド文面でも独立した裏付けを確認したわけではない',
             '注意書きが原文/LP内に存在する場合でも、その見せ方・商品適合は別途確認が必要',
             '比喩的スローガンや意図的な反復を自動的に置換しない','AI著者検出機能ではない']}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('file')
    p.add_argument('--context',choices=['product','campaign','paid-ad'],default='product')
    p.add_argument('--known-product-class',choices=['cosmetics','quasi-drug','unknown'],default='unknown')
    p.add_argument('--json',action='store_true')
    a=p.parse_args(); text=sys.stdin.read() if a.file=='-' else Path(a.file).read_text(encoding='utf-8')
    r=audit(text,a.context,a.known_product_class)
    if a.json: print(json.dumps(r,ensure_ascii=False,indent=2))
    else:
        print(r['status'])
        for x in r['flags']: print(x['status'],x['span'],x['question'])
        for x in r['limitations']: print('LIMIT:',x)
if __name__=='__main__': main()
