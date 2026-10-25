#!/usr/bin/env python3
"""Conservative literal-difference warning for Japanese before/after editing.

Not a semantic entailment tool; manual review is mandatory. Exit code 2 if warnings found.
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

# Compares *visible numeric strings*, e.g. 2026, 10, 2.1%, 5,882円.
NUM_TOKEN = re.compile(r"(?<![0-9０-９A-Za-z])[0-9０-９][0-9０-９,，.．]*\s*(?:%|％|円|万円|億円|人|件|社|年|月|日|時間|分|倍|pt|ポイント)?")
# Latin tokens approximate product/company/metric mentions and are noisy, e.g. AI, LP, CPA.
LATIN_TOKEN = re.compile(r"\b[A-Za-z][A-Za-z0-9_-]{1,}\b")
UNCERTAINTY = ("予定", "検討", "可能性", "見込み", "未定", "推定", "かもしれない")
NEGATIVE = ("ない", "なかった", "未", "不")


def _bag(regex, text):
    return Counter(re.sub(r"\s+", "", token) for token in regex.findall(text))


def check(before, after):
    warnings=[]
    for label, rx in (("numbers_dates_units",NUM_TOKEN),("latin_identifiers",LATIN_TOKEN)):
        b,a=_bag(rx,before),_bag(rx,after)
        for k,n in (b-a).items():
            warnings.append({"type":label,"direction":"removed_or_changed","literal":k,"count":n})
        for k,n in (a-b).items():
            warnings.append({"type":label,"direction":"added_or_changed","literal":k,"count":n})
    for token in UNCERTAINTY:
        if (token in before)!=(token in after):
            warnings.append({"type":"uncertainty_marker_changed","literal":token,
                             "direction":"review_modality"})
    return {"status":"REVIEW" if warnings else "NO_LITERAL_DIFFERENCES_FOUND",
            "warnings": warnings,
            "disclaimer":"Cannot check Japanese names, quote semantics, negation scope, firsthand experience, causal claims, or paraphrase equivalence. No warnings does NOT mean PASS."}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('before'); p.add_argument('after'); p.add_argument('--json',action='store_true')
    a=p.parse_args()
    report=check(Path(a.before).read_text(encoding='utf-8'),Path(a.after).read_text(encoding='utf-8'))
    if a.json:
        print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(report['status'])
        for x in report['warnings']:
            print(f"- {x['type']}: {x['direction']}: {x['literal']}")
        print(report['disclaimer'])
    raise SystemExit(2 if report['warnings'] else 0)

if __name__=='__main__':
    main()
