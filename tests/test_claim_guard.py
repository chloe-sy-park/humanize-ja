import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from claim_guard import check

class ClaimGuardTests(unittest.TestCase):
    def test_added_number_flagged(self):
        x=check('改善しました。','30%改善しました。')
        self.assertEqual(x['status'],'REVIEW')
        self.assertTrue(any(y['direction']=='added_or_changed' for y in x['warnings']))
    def test_removed_number_flagged(self):
        x=check('2026年に公開。','公開。')
        self.assertEqual(x['status'],'REVIEW')
    def test_uncertainty_change_flagged(self):
        x=check('公開する予定です。','公開します。')
        self.assertTrue(any(y['type']=='uncertainty_marker_changed' for y in x['warnings']))
    def test_no_difference_is_not_pass(self):
        x=check('検討しています。','検討しています。')
        self.assertEqual(x['status'],'NO_LITERAL_DIFFERENCES_FOUND')
        self.assertIn('does NOT mean PASS',x['disclaimer'])

if __name__=='__main__': unittest.main()
