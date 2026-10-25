import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from diagnose import analyze

class DiagnoseTests(unittest.TestCase):
    def test_short_text_has_no_cv(self):
        x=analyze('今日は会議です。明日も会議です。','email')
        self.assertIsNone(x['sentence_length_cv'])
        self.assertIsNone(x['classification'])
    def test_repetitive_connectors_flag(self):
        x=analyze('また、確認します。さらに、共有します。加えて、検討します。')
        self.assertGreaterEqual(len([i for i in x['flags'] if i['type']=='repetitive-connectors']),3)
    def test_cv_has_no_pass(self):
        x=analyze('短い。長い内容を詳しく説明します。説明。短め。さらに詳しい内容をここで確認できます。')
        self.assertIsNotNone(x['sentence_length_cv'])
        self.assertFalse('pass' in x)

if __name__=='__main__': unittest.main()
