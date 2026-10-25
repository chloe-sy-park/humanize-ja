#!/usr/bin/env python3
"""Conservative Japanese editorial diagnostics. NOT an AI detector.

Stdlib only; intentionally avoids morphology claims and strict metric targets.
"""
import argparse
import json
import re
import statistics
from pathlib import Path

FLAGS = {
    "self-introduction": r"本記事では|今回は.{0,18}紹介していきたいと思います|以下のようにまとめ",
    "repetitive-connectors": r"(?:また|さらに|加えて|一方で|つまり)[、，]",
    "empty-importance": r"本質的|非常に重要|大きな可能性|今後の動向に注目",
    "redundant-capability": r"(?:することができる|することができます|行うことが可能)",
    "hedged-verdict": r"(?:といえるでしょう|と言えるでしょう|といえます|と言えます)",
    "over-polite": r"(?:させていただき|いただけますと幸いです)",
    "artificial-frame": r"(?:単なる.{0,28}ではなく|〜ではなく|だけではありません)",
    "performed-familiarity": r"(?:正直|なんですよね|と思いませんか)[。、]",
}
SPLIT = re.compile(r"[。！？!?]+")


def analyze(text, genre="founder"):
    # approximate sentence length by Japanese punctuation, ignore markup-only/very short cases
    sentences = [s.strip() for s in SPLIT.split(text) if s.strip()]
    lengths = [len(re.sub(r"\s+", "", s)) for s in sentences]
    mean_len = (sum(lengths) / len(lengths)) if lengths else 0.0
    cv = round(statistics.pstdev(lengths) / mean_len, 3) if len(lengths) >= 5 and mean_len else None
    matches = []
    for label, pattern in FLAGS.items():
        for m in list(re.finditer(pattern, text))[:12]:
            matches.append({"type": label, "text": m.group(0), "offset": m.start(),
                            "warning": "Contextual editorial candidate; not proof of AI authorship."})
    connector_count = sum(1 for x in matches if x["type"] == "repetitive-connectors")
    notes = []
    if len(lengths) < 5:
        notes.append("Too few sentences for meaningful sentence-length CV; no CV reported.")
    if cv is not None:
        notes.append("CV is descriptive only; no universal pass threshold (including 0.70).")
    if connector_count >= 3:
        notes.append("Repeated explicit connectors: review for genuine logical relation; do not delete blindly.")
    if genre in ("email", "media"):
        notes.append("Protect genre-appropriate formal expressions, citations, and consistent register.")
    return {"genre": genre, "sentences": len(lengths), "mean_sentence_length_chars": round(mean_len,1),
            "sentence_length_cv": cv, "commas": text.count("、"), "periods": text.count("。"),
            "flags": matches, "notes": notes, "classification": None,
            "disclaimer": "Not an AI detector or semantic truth validator."}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("file", help="Japanese UTF-8 file path, or '-' for stdin")
    p.add_argument("--genre", choices=["founder","marketing","media","email"], default="founder")
    p.add_argument("--json",action="store_true")
    a=p.parse_args()
    if a.file=="-":
        import sys
        txt=sys.stdin.read()
    else:
        txt=Path(a.file).read_text(encoding="utf-8")
    report=analyze(txt,a.genre)
    if a.json:
        print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(f"Genre: {a.genre} | sentences: {report['sentences']} | mean chars: {report['mean_sentence_length_chars']} | CV: {report['sentence_length_cv']}")
        for issue in report['flags']:
            print(f"- {issue['type']} @ {issue['offset']}: {issue['text']}")
        for note in report['notes']:
            print("NOTE:",note)
        print(report['disclaimer'])

if __name__=="__main__":
    main()
