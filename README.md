# 面接質問アプリ

## 概要

面接質問アプリは、練習やテスト形式で面接質問に回答できるWebアプリケーションです。ユーザーは新卒、経験者、未経験者といったカテゴリを選択し、質問をくじ引き形式で取得できます。回答履歴を保存・閲覧でき、面接対策に役立つツールです。

---

## 主な機能

1. **質問モード選択**:
    - 練習用モード
    - テスト用モード
2. **質問カテゴリ**:
    - 新卒
    - 転職（経験あり）
    - 転職（未経験）
3. **回答管理**:
    - 回答の保存・履歴の閲覧
    - 回答の削除、使用済みマーク
4. **質問進行状況**:
    - 現在の質問進捗の表示
    - 自動タイマー機能（テストモード）
5. **履歴管理**:
    - 全履歴の削除
    - 個別履歴の削除、使用済み設定

---

## 使用技術

- **バックエンド**: Flask (Python)
- **フロントエンド**: HTML, CSS, Bootstrap 5
- **データベース**: SQLite
- **その他**: JavaScript

---

## インストール手順

### 1. リポジトリのクローン

```
$ git clone <リポジトリURL>
$ cd interview-app
```

### 2. 仮想環境のセットアップ

```
$ python -m venv venv
$ source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
```

### 3. 必要なライブラリのインストール

```
$ pip install -r requirements.txt
```

### 4. データベースの初期化

初回起動時にデータベースが自動で初期化されます。

### 5. アプリの起動

```
$ python app.py
```

ブラウザで以下のURLにアクセスしてください。

```
http://127.0.0.1:5001
```

---

## ディレクトリ構成

```
interview-app/
├── app.py                # アプリケーションのメインファイル
├── templates/            # HTMLテンプレート
│   ├── index.html        # トップページ
│   ├── interview.html    # 面接質問ページ
│   ├── history.html      # 履歴ページ
│   └── finish.html       # 完了ページ
├── interview.db        # SQLiteデータベース
└── README.md             # 本ファイル
```

---

## アプリの使用方法

1. **モードとカテゴリを選択**: トップページで質問モード（練習またはテスト）とカテゴリを選択します。
2. **質問の回答**: 質問に対して回答を入力し、次の質問に進むかスキップします。
3. **回答履歴の確認**: 回答履歴ページで過去の回答を確認できます。
4. **回答履歴の管理**: 必要に応じて履歴を削除、または「使用済み」にマークできます。

---

## 注意点

- データはローカルのSQLiteデータベースに保存されます。アプリを再インストールする際はデータベースファイル (`interview.db`) をバックアップしてください。
- セッション情報はアプリの動作中に一時的に保持されます。

---



## 今後の改善案

- フィードバック機能
- 業別選択機能
- 質問検索機能
- 回答の編集機能
- 新規登録・ログイン機能
- モバイルデバイス向けのデザイン最適化
- 結果分析機能: 回答の傾向や改善点を可視化する機能を追加。

---


