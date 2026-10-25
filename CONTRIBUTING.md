# Contribution Guide / コントリビューション

日本語の編集品質を改善するIssue・Pull Requestを歓迎します。使用する文章について、**誤検出を起こす可能性がある反例**をセットで提示してください。特定の表現が常にAI生成であると断定するルールは採用しません。

## 変更提案に必要な内容

1. 対象読者・文書種類（創業者のnote、広告、B2Bメール、専門記事など）
2. 問題となる日本語の短い例（できれば架空・自作）
3. その表現が**正しい**場面の反例
4. 変更による数字・経験・根拠・確信度への影響
5. 公式資料または公開ソースへのリンク（出典は短く引用）

個人の文章や顧客情報を許可なく公開しないでください。他者の著作物の長文転載、コピーライター名義の模倣、架空の成果や体験の追加は避けます。

## Pull Request前に実行

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_repo.py
python3 scripts/check_markdown_links.py
```

GitHub ActionsはPython 3.10と3.13で同様のチェックを実施します。
