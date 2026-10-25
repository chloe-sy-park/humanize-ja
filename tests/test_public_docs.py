import unittest
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_markdown_links import check

class PublicDocsTests(unittest.TestCase):
    def test_local_links(self):
        count, errors=check()
        self.assertGreater(count,10)
        self.assertEqual(errors,[])

    def test_documented_entrypoints(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        for name in ['docs/INSTALL_JA.md','docs/EXAMPLES_JA.md','SKILL.md','THIRD_PARTY_NOTICES.md']:
            self.assertIn(name,readme)
        self.assertIn('日本語',readme)

    def test_ci_and_license(self):
        self.assertIn('MIT License',(ROOT/'LICENSE').read_text(encoding='utf-8'))
        self.assertIn('permissions:',(ROOT/'.github/workflows/ci.yml').read_text(encoding='utf-8'))
        self.assertIn('1.2.0',(ROOT/'SKILL.md').read_text(encoding='utf-8'))

if __name__=='__main__': unittest.main()
