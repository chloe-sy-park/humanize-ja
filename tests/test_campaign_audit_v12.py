import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from campaign_audit_v12 import audit

class Tests(unittest.TestCase):
    def flag(self,text,cat,context='product'):
        return any(f['category']==cat for f in audit(text,context)['flags'])
    def test_product_number_and_footnote_needed(self): self.assertTrue(self.flag('1.6兆個※','quantified_metaphor'))
    def test_official_ranking_requires_scope(self): self.assertTrue(self.flag('最高峰','rank_scope'))
    def test_drug_claim_scope(self): self.assertTrue(self.flag('角層まで浸透','claim_scope'))
    def test_campaign_absolute_not_auto_illegal(self):
        flags=audit('ひとつ残らず応えるために。','campaign')['flags']
        self.assertTrue(any(f['category']=='guarantee' for f in flags))
        self.assertTrue(all(f['automatic_illegality'] is False for f in flags))
    def test_rhetorical_phrase_not_flagged(self): self.assertEqual(audit('時間は、存在しない。','campaign')['flags'],[])
    def test_brand_protected(self): self.assertTrue(self.flag('つや玉','protected_brand_term'))
    def test_alt_spelling_not_banned(self): self.assertTrue(self.flag('肌にスキを重ねていく','protected_brand_term','campaign'))
    def test_no_flags_not_certified(self): self.assertIn('limitations',audit('肌をケアする'))
    def test_offer(self): self.assertTrue(self.flag('初回半額','offer'))
    def test_claim_guarantee(self): self.assertTrue(self.flag('必ず','guarantee'))
    def test_no_age_discrimination_score(self): self.assertIsNone(audit('スキンケア')['flags'][0] if audit('スキンケア')['flags'] else None)
if __name__=='__main__': unittest.main()
