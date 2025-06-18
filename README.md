# シンプルなFlaskアプリケーション

## 概要

このプロジェクトは、Python Flaskを使った初心者向けのサンプルアプリケーションです。
Webブラウザでアクセスすると「こんにちはセカイ」と表示される、最もシンプルなWebアプリケーションを作成します。

### このアプリで学べること
- PythonでWebアプリケーションを作る基本的な方法
- Flaskフレームワークの基本的な使い方
- Webサーバーの起動とアクセス方法

## 必要なもの

- Python 3.7以上
- pip（Pythonパッケージマネージャー）
- Git（GitHubからクローンする場合）

## インストール方法

### 方法1: GitHubからクローンする場合

1. ターミナル（コマンドプロンプト）を開きます
2. 作業したいディレクトリに移動します
3. 以下のコマンドでリポジトリをクローンします：
```bash
git clone https://github.com/[ユーザー名]/simple_flask.git
cd simple_flask
```

### 方法2: ZIPファイルでダウンロードする場合

1. GitHubのリポジトリページにアクセス
2. 「Code」ボタンをクリック → 「Download ZIP」を選択
3. ダウンロードしたZIPファイルを解凍
4. ターミナルで解凍したフォルダに移動：
```bash
cd simple_flask
```

## 起動方法

### 1. 事前準備
まず、必要なパッケージ（Flask）をインストールします：
```bash
pip install -r requirements.txt
```

### 2. アプリケーションの起動
以下のコマンドでWebサーバーを起動します：
```bash
python app.py
```

成功すると、以下のようなメッセージが表示されます：
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[あなたのIPアドレス]:5000
```

### 3. ブラウザでアクセス
Webブラウザを開いて、以下のURLにアクセスします：
```
http://localhost:5000
```

「こんにちはセカイ」と表示されれば成功です！

### 4. サーバーの停止
アプリケーションを停止するには、ターミナルで `Ctrl + C` を押します。

## ファイル構成

- `app.py` - メインのアプリケーションファイル
- `requirements.txt` - 必要なPythonパッケージのリスト
- `README.md` - このファイル（説明書）

## 学習ポイント

1. **Flaskのインポート**: Webフレームワークを使うための準備
2. **ルーティング**: URLとPython関数を結びつける仕組み
3. **デコレーター**: `@app.route()`のような特殊な記法
4. **サーバーの起動**: `app.run()`でWebサーバーを立ち上げる

## トラブルシューティング

- **「ModuleNotFoundError: No module named 'flask'」エラーが出る場合**
  - Flaskがインストールされていません。`pip install -r requirements.txt`を実行してください。

- **「Address already in use」エラーが出る場合**
  - すでに5000番ポートが使用されています。他のFlaskアプリが起動していないか確認してください。

- **ブラウザで「このサイトにアクセスできません」と表示される場合**
  - Flaskアプリが正常に起動しているか確認してください。
  - URLが正しいか（http://localhost:5000）確認してください。