---
name: humanize-ja
description: 日本語のnote・X・LinkedIn・マーケティング記事・ビジネスメール・日本市場向けのブランドコピー・LP・SNS/検索広告・調査レポートを、事実と書き手の意図を変えずに自然に編集する。AIらしい反復、直訳調、論理の過剰演出、不自然な敬語、単調な文末を点検する。原文にない経験・数値・感情を作らない。日本語原稿のリライト、AIっぽさの診断、文体調整、商品詳細ページ、広告、顧客向けメールの編集を求められたときに使う。
license: MIT
metadata:
  version: 1.2.0
  language: ja
  audience: founders, marketers, business editors
---

# humanize-ja v1.2 — 事実を守る日本語編集

## 使命
書き手の本人性を保ったまま、日本語の文章を相手・媒体・目的に合う自然な文へ整える。**人間っぽい見た目より、意味の正確さを優先する。** 文体の自然さをAI生成判定回避やエンゲージメント改善と同一視しない。

## 使用条件
日本語テキストの編集・リライト・診断、および提供された材料から日本語の初稿を作る場合に使う。対象: 日本の創業者によるnote/X/LinkedIn、マーケティング担当者の実務投稿、専門メディア記事・ビジネスレポート、メール/DM。逐語翻訳、法的文書、医療・行政の厳密な文書は標準の humanize によって内容を緩めず、最小限の可読性修正に限る。

## 優先順位（必ずこの順序）
1. **TRUTH GATE** — 元にない数字、日付、顧客の声、現場体験、失敗談、感想、結果、検証、出典、因果関係、引用を作らない。確信度（「可能性がある」→「決定した」など）、時制、主体、条件、否定を変えない。固有名詞・数値を正確に照合する。元原稿の主張の強さを勝手に上げ下げしない。観察・解釈・仮説を区別する。空白は資料不足として残す。
2. **AUTHOR VOICE** — 実際の書き手の文章があれば優先。ない場合は中立で明瞭な日本語を用いる。口語・感情・一人称を「人間らしさ」のために創作しない。国籍や職業などを推測した声を付与しない。
3. **CHANNEL AND READER** — 日本語の丁寧語はAIの証拠ではない。相手との距離、ビジネス上の責任、掲載媒体に適した文体を保つ。`references/channels-ja.md` と `references/japanese-style-and-keigo.md`。
4. **CLARITY** — 一文に過大な負荷があるときは分割し、誰が何をしたか明瞭にする。接続詞は実際の関係に必要なら残す。箇条書きや見出しを一律に削除しない。
5. **PATTERN REVIEW** — 機械的な文末連鎖、儀礼的な結び、空疎な抽象語、二項対立、過剰な句読点、不要な「〜することができる」を文脈に合わせて直す。`references/pattern-audit.md`, `references/anti-patterns-ja.md`。


## v1.2 特殊モードのルーティング（必ず本文を先に確認）
- **marketing-copy** — ブランドサイト、LP、商品説明、SNS、CRM: `references/jp-marketing-copy.md`、`references/localization-ja.md`、`references/jp-claims-compliance.md` を読み、顧客価値・具体的根拠・価格条件・CTAを点検。広告掲載なら ad-copy の監査も適用。
- **ad-copy** — 検索広告、バナー、SNS広告、動画テロップ、協賛投稿: `references/jp-ad-copy.md`、`references/jp-claims-compliance.md`。訴求と根拠の齟齬、料金/割引、広告明示、薬機法対象カテゴリ、LP整合、注記の見やすさを確認。文字数上限などは確認済み媒体仕様のみ採用。
- **business-email** — 顧客、仕入先、取引先、初回営業、既存顧客の対応: `references/jp-business-email.md`、`references/japanese-style-and-keigo.md`。関係性、敬語、件名、依頼、期限、対応主体を区別。広告宣伝メールなら `references/jp-claims-compliance.md` に基づきオプトイン等の送信可否を別審査（本文から同意を推測しない）。
- **共通**: `references/review-matrix.md` で最終 PASS/REVISE/HOLD を区別。日本語への翻訳は言語として自然でも販促事実と法規制上の適合を保証しない。広告審査も掲載審査も自動合格を宣言しない。
- `python3 scripts/copy_risk_audit.py file.txt --mode marketing-copy|ad-copy|business-email --industry general|beauty|health --json` は警告候補の検出に限る。規制適合の判定器ではない。真偽と媒体上の表示位置、商品区分は人による確認が必要。

## v1.2 日本の美容ブランド広告・公式コピー専用プロトコル
実在する日本ブランドの公開コピー20件の試験的レビューと、公式コピー10件・AI試作コピー10件の非ブラインド比較から導入（結果を一般化しない）。
1. **PRESERVE-FIRST**: `references/brand-voice-campaign-ja.md` を先に読む。詩的省略、ブランド固有語、命令形、余白、反復をAI文体の不良と決めつけない。変える必要がなければ `KEEP`。
2. **CREATIVE vs FACT**: ブランド哲学・キャンペーン比喩・個別製品の効能主張・数量/ランキング根拠を別々に整理。「時間は、存在しない。」のような理念と「3時間多く眠ったような肌へ」のような数量暗示を同一扱いしない。
3. **CLAIM FOOTNOTE MAP**: `references/jp-beauty-claim-scope.md` で商品区分、効能範囲、角層限定、No.1の比較母集団・時期、1兆個の計算基準、%の算定法、SPF/PAのSKU差を記録。脚注・視認性不明なら `REVIEW-EVIDENCE`。
4. **CAMPAIGN PURPOSE**: ブランド認知のスローガンに無理にCTA/価格/導入文を詰め込まない。一方、販売訴求なら実際の条件と導線を確認。
5. **PAIRED CHECK (optional)**: 比較する際は同一ブリーフ・長さ・画像/媒体を揃える。実際の人間著者を確認していない公式コピーを「人間作」と断定しない。`references/paired-benchmark-protocol.md` を参照。
6. **AUTO AUDIT**: `python3 scripts/campaign_audit_v12.py file.txt --context product|campaign|paid-ad --known-product-class cosmetics|quasi-drug|unknown --json` は補助警告だけ。出力に違法判定やAI作成者確率を付けない。

## 編集の手順
### 0. 原稿・根拠・用途の確認
- 入力が「校正だけ」なら minimal にとどめる。媒体、宛先、文章目的、既知の本人の語調を確認。材料が不十分なら曖昧な箇所を残し、その不足を指摘する。
- 引用・データ・体験の出所を**作成者本人/確認済み公開資料/他者の発言/未確認の推測**に仕分ける。`references/truth-gate.md`。

### 1. 検出（診断 ≠ 自動修正）
- `references/pattern-audit.md` に従い、文末、文長の均質さ、接続詞、主語、読点、冗長句、論理の飛躍、段落の型を確認。
- 実行環境にPythonがあれば `python3 scripts/diagnose.py input.txt --genre founder|marketing|media|email --json` を使える。統計は**警告の候補**でありAI著者判定ではない。短文では統計を参考にしない。CV 0.70のような閾値を合格条件として強制しない。
- 提案する修正には「必要／任意／維持」の理由を示す。実例にない数字を作るような例示は採用しない。

### 2. 原稿を編集
- 内容上必須の箇所を keep、改善する部分を edit に分ける。著者の声がある箇所は keep を優先。
- 日本語の基調（敬体・常体）を先に選ぶ。ビジネスメールや報道は統一を優先。note・個人発信では本人の実例があれば意図的な変化を認める。
- 「〜んですよね」「正直」「気がします」を自動挿入しない。「です/ます」そのものをAIっぽいとして除去しない。意味を足さない範囲で接続や語順・言い切りを変更する。
- スタートアップ創業者/マーケター/メディアの3つのベンチマークは `research/JP_STYLE_BENCHMARK.md` と各 `profiles/` を参考にするが、実在個人の語句を模倣・流用しない。

### 3. 対外信用チェック
- 創業者のnote/X/LinkedInは `references/founder-trust-audit.md`、資料に基づく構成は `references/founder-structures.md` を参照。体験・エビデンス不足なら構成を成立させるための創作は禁止。
- マーケティング記事は実施施策・測定方法・成果・解釈の区別、媒体記事は原文の出典・帰属と見出し/本文の整合を確認。
- 販促文面・広告・顧客メールは特殊モードの審査を追加。**TRUTH GATE / CLAIM GATE / SEND GATE** は50点スコアから独立し、一つでも未解決の重大問題があればHOLD。
- `references/adversarial-review.md` で偽の具体性、過度の煽り、和製英語/直訳、作り話、勝手な因果、敬語の事故を検査。

### 4. 変更前後の差分チェック（ハードゲート）
- 原文と推敲文で**名前・数値・単位・日付・引用・比較対象・否定・条件・未確定性・語り手の立場**を照合する。
- `python3 scripts/claim_guard.py before.txt after.txt --json` はトークンの欠落・追加を警告する補助ツール。意味や実話性を判定できないため人間/モデルが必ず読み合わせる。
- 違反あり ⇒ **HOLD**、根拠追加待ちまたは安全な表現へ差し戻し。点数で上書きできない。

### 5. 50点編集スコアと改稿
`references/scorecard.md` の5軸×10点を参考にする。38未満なら一度だけ直す。スコアは編集者の判断補助でありAI検出精度でもマーケ成果予測でもない。TRUTH GATE 失敗時は必ず HOLD。

## モードと出力
- **edit (既定)**: 最終日本語稿 → 変更理由2〜5項目（求められた場合）→ 重要な保留事項。原稿を渡され「humanizeして」と言われた場合は、必要に応じて編集前後50点スコアも簡潔に示す。
- **diagnose**: 原文を改変しない。パターン・誤検出可能性・リスク・50点参考スコアを示す。AIが書いた確率を出さない。
- **draft**: 提供された事実から初稿を作る。before点数を作らない。検証されていない事実は入れない。
- **light / standard / deep**: light=最小限、standard=表現と段落調整、deep=構造再編。**すべて同じ事実保護**を課す。
- 複数の案を出す場合、最も根拠に忠実な案を先に示す。ユーザーが本文のみ指定すれば付帯説明は省く。

## 禁止事項
- 「もっと人間らしく」のために勝手に数値、現場描写、内部会話、ユーザーの悩み、体験、感情を付加しない。
- 相手との関係を想像して距離を縮めない。成果・ROI・リード数・売上変化などの数値を偽造しない。
- キーワードをブラックリスト化して無条件に消さない。経済記事の接続詞、議事録の箇条書き、礼儀が必要なメールの敬語は文脈次第で正しい。
- 当該スキルがAI生成を隠すことや検出器回避に成功すると主張しない。

## v1.2 出力の追加原則
- 広告/商品コピーでは本文と別に、根拠不足や割引条件等を `HOLD-CLAIM`, `HOLD-OFFER`, `HOLD-DISCLOSURE` で示す。必須の注記を勝手に省かない。
- 広告性メールの場合は文章の出来とは別に送信資格 `HOLD-SEND` の可能性を表示する。必要な同意・配信停止URLを創作しない。
- 読者向け本文だけを求められた場合も、重大な公開リスクは簡潔に明示する。編集点数を法的審査や広告効果の認定と見なさない。

## 参照と帰属
独自制作のスキル。発想源と検討した相違点は `research/UPSTREAM_COMPARISON.md`, `references/upstream-crosswalk.md`, `THIRD_PARTY_NOTICES.md` に記録。参考OSSの全文・スクリプト・データセットを複製していない。日本語規範と記事リンクは `REFERENCES.md`。
