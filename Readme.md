# 概要
株式会社CARTA HOLDINGSのサポーターズ主催の2020年ウインターハッカソンvol6におけるチーム0.1専用のレポジトリ

# サービスのこと
### サービス名
論文サポートサービスArticleTant

### 概要
slackAPIとmecab-web-apiを連携し、"ブロックチェーンをデータベースに応用したものが欲しいなあ。"などのコメントをslack-botへ投げると、それに関した論文が出力される。

### 背景
役に立つものというお題の元、論文検索をslackの会話から自動レコメンドしてくれるものを作ろうというのがきっかけ。

### 使用フレームワーク、API
- Flask
- SlackAPI
- mecab-web-api

## 使い方
1. venvをactivateする。
2. requirements.txt内をインストールする。
```
pip install -r requirements.txt
```
3. Djangoモデルの変更を検出し、それをマイグレーションファイルとして出力する。
```
python3 manage.py makemigrations
```
4. マイグレーションファイルをデータベースに適用して、データベースを最新の状態に更新
```
python3 manage.py migrate
```
5. サーバを起動する。
```
python3 manage.py runserver
```
