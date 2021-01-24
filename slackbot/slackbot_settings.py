# coding: utf-8
import os 
# botアカウントのトークンを指定
API_TOKEN =os.environ["Key"] 

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "論文に関するキーワードを入力してね"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
