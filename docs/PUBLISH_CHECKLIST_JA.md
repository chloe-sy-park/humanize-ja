# GitHub公開前チェックリスト

**公開状態:** このパッケージの作成時点ではGitHubに`humanize-ja`の新規公開リポジトリを作成していません。ローカルの公開準備です。

## 1. 権利・個人情報

- [ ] `LICENSE` の `humanize-ja contributors` 表記を維持するか、正しい著作権者名に更新する。
- [ ] `THIRD_PARTY_NOTICES.md` の参照元名義・リンク・ライセンスを再確認する。
- [ ] `research/` の第三者引用は短く、出典リンクを維持する。引用が正確か公開時点で再確認する。
- [ ] 顧客の未公開資料、アカウントID、認証トークン、メールアドレス、個人情報を含めていないことを確認する。
- [ ] 研究資料の「公式コピー」の著者が実際の人間カピーライターかは未検証と明記する。

## 2. コード・品質

- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `python3 scripts/validate_repo.py`
- [ ] `python3 scripts/check_markdown_links.py`
- [ ] `.github/workflows/ci.yml` が `main` に対して成功する。
- [ ] セキュリティや法令に関するツールを「合格判定器」と誤表記していない。
- [ ] Markdownのローカル相対リンクがすべて機能する。

## 3. GitHub リポジトリ作成

推奨名称: `humanize-ja`。公開説明文（コピペ用）:

> Open-source Japanese writing humanizer skill for founders, marketers, brand copy, advertising and business email — fact-preserving, voice-first.

推奨トピック: `agent-skills`, `japanese`, `writing`, `editing`, `copywriting`, `claude-code`, `codex`, `marketing`。

GitHubで新規の**空リポジトリ**（自動README / LICENSE / .gitignore 生成なし）を作成し、ローカルのフォルダから次を実行します。`OWNER` を実際のユーザー名に置き換えてください。

```bash
git init -b main
git add .
git commit -m "docs: prepare humanize-ja v1.2 for public release"
git remote add origin https://github.com/OWNER/humanize-ja.git
git push -u origin main
```

**注意:** `git commit` は利用者のGit本人設定（`user.name`/`user.email`）を使用します。公開前にそれらを確認してください。`git remote add origin` は既存remoteがある場合は失敗します。事前に `git remote -v` で確認してください。

## 4. 公開後

- [ ] GitHub上で `README.md` と相対リンクが正しく表示される。
- [ ] GitHub Actionsの初回テストが成功する。
- [ ] `OWNER` 仮文字列を正式な所有者へ差し替える（README、INSTALLガイド）。
- [ ] v1.2.0としてタグとリリースノートを追加する。
- [ ] インストール手順を新規フォルダで再実行し、スキル検出を確認する。

## 5. 配布と責任範囲

このリポジトリは**文章編集指示・参考資料・補助的なローカル検査スクリプト**を配布するものです。文章の法的適法性、AI由来の判定、広告成果、原語ネイティブによる最終品質認定を保証するものではありません。
