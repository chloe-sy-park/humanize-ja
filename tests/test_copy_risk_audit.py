import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from copy_risk_audit import audit

class CopyRiskAuditTests(unittest.TestCase):
    def test_superlatives_are_flags_not_verdicts(self):
        r=audit('日本一！絶対に成功。',mode='ad-copy')
        self.assertTrue(any(x['rule']=='superlative_or_ranking' for x in r['flags']))
        self.assertIsNone(r['legal_compliance'])
        self.assertTrue(all(x['auto_violation_finding'] is False for x in r['flags']))
    def test_discount_requires_check(self):
        self.assertIn('HOLD-OFFER',[x['suggested_risk'] for x in audit('今日だけ50%OFF、通常価格2,000円。',mode='ad-copy')['flags']])
    def test_health_claim(self):
        r=audit('ニキビを治す美容液。',mode='ad-copy',industry='beauty')
        self.assertIn('HOLD-CLAIM',[x['suggested_risk'] for x in r['flags']])
    def test_health_word_context_no_legal_verdict(self):
        r=audit('医療の歴史について解説します。',industry='general')
        self.assertIsNone(r['legal_compliance'])
    def test_email_subject_omitted_is_only_review(self):
        r=audit('いつもお世話になっております。ご確認をお願いいたします。',mode='business-email')
        self.assertTrue(any(x['rule']=='subject_not_present' for x in r['flags']))
    def test_email_subject_exists(self):
        r=audit('件名: 資料確認のお願い\nいつもお世話になっております。',mode='business-email')
        self.assertFalse(any(x['rule']=='subject_not_present' for x in r['flags']))
    def test_hashtag_pr_never_certifies_disclosure(self):
        r=audit('商品をおすすめします #PR',mode='ad-copy')
        self.assertTrue(any(x['rule']=='sponsor_keyword' for x in r['flags']))
        self.assertIsNone(r['legal_compliance'])
    def test_empty_text_not_pass(self):
        r=audit('',mode='ad-copy')
        self.assertEqual(r['status'],'NO_KEYWORD_FLAGS')
        self.assertIsNone(r['legal_compliance'])
    def test_unicode_and_stable_offsets(self):
        r=audit('あいう今だけ50%OFF',mode='marketing-copy')
        self.assertEqual(next(x for x in r['flags'] if x['rule']=='discount_terms')['offset'],3)

if __name__=='__main__': unittest.main()
