# インストールガイド（日本語）

**対象:** humanize-ja v1.2.0。`SKILL.md`を使えるエージェント環境向けです。Pythonスクリプトは任意で、エージェント本体のインストールとは別です。

## 1. まず配布物を確認

ZIPを展開したとき、次のように**同じフォルダ内**にファイルがあることを確認してください。

```text
humanize-ja/
  SKILL.md
  references/
  profiles/
  examples/
  scripts/
  tests/
```

`SKILL.md`だけをコピーすると、本文から参照する補助ルールが読み込めません。`research/`はベンチマークの詳細を確認するときに必要です。

## 2. Codex にインストール

OpenAI公式の現在のローカル配置方式ではユーザー用のスキルディレクトリは `~/.agents/skills/`、リポジトリ用は `.agents/skills/` です。

### A. このZIPからインストール（未公開でも使えます）

1. ZIPを展開してフォルダ名を `humanize-ja` にします。
2. Macのターミナルで次を実行します。

```bash
mkdir -p ~/.agents/skills
cp -R /path/to/unzipped/humanize-ja ~/.agents/skills/humanize-ja
```

`/path/to/unzipped/humanize-ja` は実際の展開先に書き換えてください。すでに同名フォルダがある場合は、重複コピーを避けてバックアップ・差分を確認してください。

### B. GitHub公開後にインストール

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/OWNER/humanize-ja.git ~/.agents/skills/humanize-ja
```

`OWNER` は実際の公開先ユーザー名に置き換えます。存在するリポジトリURLを確認してから実行してください。

### C. プロジェクトだけで使う

```bash
mkdir -p .agents/skills
cp -R /path/to/unzipped/humanize-ja .agents/skills/humanize-ja
```

Codexで `$humanize-ja` を指定して編集依頼を送ります。認識しない場合は、保存場所と `SKILL.md` の先頭YAMLを確認し、Codexを再起動してください。

参照: [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills)

## 3. Claude Code にインストール

個人利用なら `~/.claude/skills/humanize-ja/`、プロジェクトに同梱するなら `.claude/skills/humanize-ja/` を使います。

### ZIPから

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/unzipped/humanize-ja ~/.claude/skills/humanize-ja
```

### GitHub公開後

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/OWNER/humanize-ja.git ~/.claude/skills/humanize-ja
```

Claude Codeでは `/humanize-ja` というスキル名で呼び出せます。検出方法が変更される場合があるため、実行環境でスキル一覧を確認してください。

参照: [Anthropic — Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

## 4. ChatGPTで使う

- **カスタムスキルに対応した環境:** `humanize-ja/` フォルダを丸ごと含むZIPを用意し、環境の「スキルの作成・追加」機能で読み込ませます。実際のアップロードUI、プラン、利用可否は環境で異なります。
- **プロジェクト・ファイル参照型の環境:** `SKILL.md`と重要な`references/`資料をファイルとして渡し、「この指示を日本語編集時に適用して」と指定します。これは環境によってはネイティブなスキルインストールとは異なります。

参照: [ChatGPT Learn — Skills](https://learn.chatgpt.com/docs/build-skills)

## 5. Pythonの補助検査（任意）

Python 3.10以上がある場合、リポジトリ内で次を実行できます。追加のパッケージは不要です。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_repo.py
python3 scripts/check_markdown_links.py
python3 scripts/diagnose.py examples/sample_input_ja.txt --genre marketing
```

Pythonなしでも文章編集の指示ファイルは利用できます。各スクリプトはAI判定器や法令適合性認証ではありません。

## 6. アップデート・アンインストール

GitHubからcloneしたフォルダでは `git pull --ff-only` を使えます。ZIPからコピーした場合はバックアップ後、新バージョンのフォルダと差し替えてください。アンインストールは該当の `humanize-ja` ディレクトリを削除します（他のスキルを誤削除しないこと）。

## 7. よくある失敗

| 症状 | 確認点 |
| --- | --- |
| スキルが検出されない | `humanize-ja/SKILL.md` の位置、YAMLの `name`、再起動 |
| 補助ルールを参照できない | `references/` を含めてコピーしたか |
| `git clone` が失敗する | URLが公開済みか、OWNERを実際の名前に変更したか、Gitの設定 |
| Pythonの補助検査が動かない | Python 3.10以上か、リポジトリのルートで実行しているか |
| 法令について断定的な結果が出る | `HOLD`は確認事項。商品区分、媒体と表示を別途確認 |
