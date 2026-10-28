# humanize-ja

**Make AI-generated Japanese sound natural without losing meaning, facts, or the writer's voice.**

humanize-ja is an open-source Agent Skill for Japanese writing and editing, designed for use with Claude Code and Codex.

It helps refine AI-generated Japanese text, awkward translations, and overly formulaic writing while preserving the original intent, factual accuracy, and brand voice.

## What makes it different?

Natural Japanese writing: Improve awkward phrasing, repetitive sentence patterns, unnatural keigo, and translation-like expressions.

Fact-preserving edits: Keep original numbers, claims, quotes, personal experiences, and uncertainty intact.

Japanese marketing & advertising: Refine product descriptions, landing pages, brand copy, and advertising messages.

Business communication: Edit Japanese business emails with context-appropriate politeness and clearer requests.

Brand voice protection: Preserve intentional metaphors, creative expressions, and distinctive writing styles.

Instead of rewriting everything to sound more human, humanize-ja helps you decide what to KEEP, REVISE, or HOLD for further review.

It is a writing and editorial skill, not an AI detector or a guarantee of advertising compliance.

**Languages: Japanese writing, with documentation for international users.**

**License: MIT · Version: 1.2.0**


# 日本語での説明

**日本語の「AIっぽさ」を消すためだけでなく、書き手の意図・事実・ブランドの声を守る編集スキル。**

日本語のnote・X・LinkedIn、マーケティング記事、ランディングページ、化粧品などの商品紹介、広告コピー、ビジネスメールの下書き・推敲・レビューを支援する、オープンソースのAgent Skillです。

> **人間らしさを演出するために、事実をつくらない。** 不自然な言い回しは直しますが、書き手の体験・数字・実績・引用・確信度を勝手に追加、変更しません。

**Version:** 1.2.0 · **Language:** Japanese (日本語) · **License:** MIT · **Python:** 3.10以上（補助スクリプトを使う場合のみ、外部パッケージ不要）

[インストール](docs/INSTALL_JA.md) · [使い方・プロンプト](docs/EXAMPLES_JA.md) · [FAQ](docs/FAQ_JA.md) · [調査と出典](REFERENCES.md) · [한국어 안내](README.ko.md)

## どんな文章に使える？

| モード・用途 | 対象 | とくに確認すること |
| --- | --- | --- |
| Founder / Editorial | 創業者のnote・X・LinkedIn、ビジネス記事 | 本人が経験したことと解釈の区別、読み手との距離、単調な定型表現 |
| `marketing-copy` | LP、商品詳細、CRM、ブランドSNS | 特徴の裏付け、ブランド固有表現、ベネフィット、導線 |
| `ad-copy` | 検索広告、ディスプレイ、SNS、動画広告 | 商品の効能・価格・比較表現、広告表示、注記と掲載面の整合 |
| `business-email` | 顧客・取引先・パートナーへのメール | 敬語、依頼の目的と期限、関係性、送信資格（販促メールの場合） |

特定の単語や「です・ます調」を機械的に削除するツールではありません。広告の比喩や詩的表現は、ブランドが意図している場合、原則として保護します。

## このスキルの特徴

- **Truth Gate:** 数値・日付・人名・製品性能・一次体験・引用・未確定性を照合。「見込み」を「確定」に変えません。
- **Voice First:** 実際の文章サンプルがあればそれを優先。書き手の人物像を推測・演技しません。
- **KEEP / REVISE / HOLD:** 表現を維持する判断も編集と考えます。根拠が不明な表現は公開前に確認事項を示します。
- **広告専用監査:** クリエイティブの文体と、商品・効能・価格などの主張を分けて確認します。
- **診断は補助:** Pythonスクリプトは警告候補を出すだけです。AI生成確率や法令適合、広告成果は判定しません。

## 30秒で使う

`SKILL.md` をエージェントに認識させたうえで、次のように依頼します。インストール先・機能はホストによって異なります。

**通常の推敲**

> humanize-jaを使って、この日本語のnote記事を自然に推敲してください。事実・数字・体験・主張の強さは変えず、修正理由を3点だけ説明してください。

**日本市場向けの商品コピー**

> humanize-jaのmarketing-copyモードで、商品説明文をレビューしてください。確認済みの特徴だけを使い、ブランドのトーンを維持してください。事実のない効能表現や注記が必要な箇所はHOLDにしてください。

**取引先向けメール**

> humanize-jaのbusiness-emailモードで、下書きを初めて連絡する取引先向けに整えてください。架空の紹介者や面識を作らず、依頼・回答期限を明確にしてください。

→ 入力例、改稿例、保持すべき表現、差し戻しの例は [使い方・プロンプト集](docs/EXAMPLES_JA.md) を参照。

## インストール

インストール前に[詳細手順](docs/INSTALL_JA.md)をご覧ください。公開後は次のように配置できます（`OWNER`は公開先のGitHubユーザー名に置き換える）。

**Codex（ユーザー全体）**

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/chloe-sy-park/humanize-ja.git ~/.agents/skills/humanize-ja
```

**Claude Code（ユーザー全体）**

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/chloe-sy-park/humanize-ja.git ~/.claude/skills/humanize-ja
```

**ChatGPT:** カスタムスキル対応環境ではスキルZIPをアップロード、または `SKILL.md` と必要な関連ファイルをプロジェクト/作業環境に提供します。ZIPのアップロード手順や利用条件は使用環境によって異なります。詳しくは[インストールガイド](docs/INSTALL_JA.md)を参照。

> **公開前の注意:** 上のGitHub URLは設置予定の例です。現時点で `OWNER/humanize-ja` が公開済みであることを示すリンクではありません。

## ローカル監査（任意）

Pythonの標準ライブラリだけで動作します。ツールの出力をそのまま「合法」「AI作成」と判定しないでください。

```bash
python3 scripts/diagnose.py examples/sample_input_ja.txt --genre marketing --json
python3 scripts/copy_risk_audit.py examples/sample_input_ja.txt --mode ad-copy --industry beauty --json
python3 scripts/campaign_audit_v12.py examples/sample_input_ja.txt --context paid-ad --known-product-class unknown --json
python3 scripts/claim_guard.py tests/before.txt tests/after.txt --json
python3 -m unittest discover -s tests -v
python3 scripts/validate_repo.py
python3 scripts/check_markdown_links.py
```

補助スクリプトの検査対象は主に表面上の文字列や簡易パターンです。原文との意味照合、根拠の確認、実際の広告表示やメール送信条件の判断は別途必要です。

## リポジトリの構成

```text
humanize-ja/
├── SKILL.md                    # 編集のメイン指示とハードゲート
├── references/                 # 日本語文体・媒体・広告・敬語・検証ルール
├── profiles/                   # 任意の文体プロファイル（実在人物の模倣ではない）
├── examples/                   # 架空の編集例
├── research/                   # 公開原文にリンクした調査、比較の限界
├── scripts/                    # ローカルの補助診断・パッケージ検証
├── tests/                      # 自動テスト
├── docs/                       # インストール・使用例・公開チェックリスト
├── .github/                    # CIとコミュニティ用テンプレート
├── REFERENCES.md               # 参照資料
└── THIRD_PARTY_NOTICES.md      # 第三者プロジェクトへの帰属
```

## リサーチ上の注意と権利

- [日本の化粧品ブランドの公開コピー20件](research/JP_COSMETICS_COPY_AUDIT_20.md)と[公式公開カピー10件・AI試作10件の比較](research/BRAND_VS_AI_PAIRED_10.md)は、**少数の非ブラインドな編集観察**です。誰が実際に広告コピーを書いたか、広告成果が上がるかは検証していません。
- `research/`には公開Webページの参照リンク、短い発言の引用、独自の解釈を含みます。記事本文や第三者のデータセットを再配布するものではありません。
- 日本国内の薬機法、景品表示法、ステルスマーケティング、特定電子メールに関するチェックは**公開前確認事項の整理**であり、法的な適法性の保証ではありません。該当商品の区分、出典資料、掲載媒体、表示位置に基づく確認が必要です。
- [LICENSE](LICENSE) (MIT) と [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) を維持してください。公開者名義・権利表示については [公開前チェックリスト](docs/PUBLISH_CHECKLIST_JA.md) を確認してください。

## 開発・貢献

不自然な日本語の例だけでなく、**その表現が適切になる反例**も歓迎します。提案時は使用場面と根拠、事実保護への影響を記載してください。個人情報やクライアントの機密資料は投稿しないでください。

[CONTRIBUTING](CONTRIBUTING.md) · [変更履歴](CHANGELOG.md) · [公開前チェックリスト](docs/PUBLISH_CHECKLIST_JA.md)

---

Version 1.2.0 · 調査資料の確認基準日: 2026-10-25 · 本リポジトリは他のHumanizerプロジェクトから独立した制作物であり、各プロジェクトの公式派生版ではありません。
