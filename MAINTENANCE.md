# メンテナンスガイド

このドキュメントでは、GitHubプロファイルREADMEのカスタマイズ方法を説明します。

## 📁 ファイル構成

```
github-profile/
├── README.md                    # 生成される成果物（手動編集禁止）
├── profile-config.yaml          # ユーザー設定ファイル
├── src/
│   ├── template.md              # Jinja2テンプレート
│   └── generate.py              # 生成スクリプト
├── .github/
│   └── workflows/
│       └── main.yml             # GitHub Actionsワークフロー
├── requirements.txt             # Python依存関係
└── MAINTENANCE.md               # このファイル
```

## 🔧 設定変更方法

### 基本情報の変更

`profile-config.yaml` の `user` セクションを編集してください。

```yaml
user:
  name: "あなたの名前"
  github_username: "your-username"
  title: "Your Title"
  location: "Tokyo, Japan"
  bio: |
    自己紹介文をここに記載
```

### 技術スタックの追加・削除

`profile-config.yaml` の `skills` セクションを編集してください。

```yaml
skills:
  languages:
    - typescript
    - python
    - rust  # 追加
  frontend:
    - react
    - vue   # 追加
```

**利用可能なアイコン一覧**: https://github.com/tandpfun/skill-icons#icons-list

### SNSリンクの設定

```yaml
social:
  twitter: "your_twitter_handle"
  qiita: "your_qiita_id"
  zenn: "your_zenn_id"
```

空文字列 `""` を設定すると、そのSNSは非表示になります。

### カラーテーマの変更

```yaml
theme:
  accent_color: "58a6ff"      # 16進数カラーコード（#なし）
  stats_theme: "transparent"  # GitHub Statsのテーマ
  hide_border: true           # 枠線を非表示
```

**利用可能なテーマ**: https://github.com/anuraghazra/github-readme-stats#themes

### ブログフィードの設定

```yaml
rss:
  qiita: "https://qiita.com/YOUR_ID/feed"
  zenn: "https://zenn.dev/YOUR_ID/feed"
```

設定後、`.github/workflows/main.yml` の `feed_list` も更新してください。

## 🔄 手動更新方法

### ローカルで生成

```bash
cd ~/Projects/github-profile
pip install -r requirements.txt
python src/generate.py
```

### GitHub Actionsで手動実行

1. GitHubリポジトリの「Actions」タブを開く
2. 「Update Profile README」ワークフローを選択
3. 「Run workflow」ボタンをクリック

## ❓ トラブルシューティング

### README.mdが更新されない

1. GitHub Actionsの実行ログを確認
2. `profile-config.yaml` の構文エラーをチェック
3. 手動でワークフローを実行してみる

### Snakeアニメーションが表示されない

1. `output` ブランチが作成されているか確認
2. ワークフローの権限設定を確認（`permissions: contents: write`）
3. README内のパスが正しいか確認

### 統計カードが表示されない

1. GitHubユーザー名が正しいか確認
2. https://github-readme-stats.vercel.app のステータスを確認
3. プライベートリポジトリの統計を含める場合は `count_private: true` を設定

### ブログ記事が更新されない

1. RSSフィードのURLが正しいか確認
2. `blog-post-workflow` のログを確認
3. フィードが有効なRSS/Atomフォーマットか確認

## 📝 テンプレートのカスタマイズ

`src/template.md` を編集することで、レイアウトを変更できます。

### Jinja2の基本構文

```jinja2
{{ variable }}              # 変数の出力
{{ list|join(',') }}        # リストをカンマ区切りに
{% if condition %}...{% endif %}  # 条件分岐
```

### 利用可能な変数

- `user.*`: ユーザー情報
- `skills.*`: 技術スタック
- `social.*`: SNSリンク
- `theme.*`: デザイン設定
- `rss.*`: RSSフィード

## 🚀 新しいセクションの追加

1. `src/template.md` にセクションを追加
2. 必要に応じて `profile-config.yaml` に設定項目を追加
3. ローカルで動作確認
4. コミット&プッシュ

## 📋 更新スケジュール

- **毎週月曜日 9:00 (JST)**: 自動更新
- **設定ファイル変更時**: pushトリガーで自動更新
- **手動実行**: いつでも可能
