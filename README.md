README: 面接質問アプリ

概要

面接質問アプリは、面接対策のために質問に回答し、履歴を管理できるシンプルなWebアプリケーションです。新卒、経験者、未経験者向けのカテゴリから質問を選び、回答を練習できます。

主な機能

質問モード

練習モード: 回答を入力しながら質問に慣れる

テストモード: タイマー付きで質問に回答

カテゴリ選択

新卒

転職（経験あり）

転職（未経験）

履歴管理

回答の保存・閲覧

回答の削除や使用済み設定

使用技術

バックエンド: Flask (Python)

フロントエンド: HTML, CSS, Bootstrap

データベース: SQLite

セットアップ手順

リポジトリをクローン

git clone <リポジトリURL>
cd interview-app

仮想環境のセットアップとライブラリのインストール

python -m venv venv
source venv/bin/activate  # Windowsは `venv\Scripts\activate`
pip install -r requirements.txt

アプリの起動

python app.py

ブラウザで http://127.0.0.1:5001 にアクセス。

ディレクトリ構成

interview-app/
├── app.py                # アプリケーション本体
├── templates/            # HTMLテンプレート
├── interview.db          # SQLiteデータベース
├── requirements.txt      # 必要ライブラリ
└── README.md             # 本ファイル

今後の改善案

質問検索機能

回答編集機能

モバイル対応のデザイン

結果分析機能（回答の傾向や改善点の可視化）

新規登録・ログイン機能

開発者

蒼斗 東恩納

目標: Webやソフトウェア開発のバックエンドプログラマー

学習中スキル: Python, Flask, SQL, HTML/CSS/JavaScript など


