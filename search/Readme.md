# backendについて

- 実行プログラム
    - get_paper_info.py: INPUT_TXTにユーザが調べたい分野について呟くと, arxiv上で提出日が最新の論文を１つ出力する. 
    - mecab-ipadic-neologd/ : 多数のWeb上の言語資源から得た新語を追加することでカスタマイズした MeCab用のシステム辞書.
    (https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md)


- 環境構築
    - mecabインストール
    - for mac: https://qiita.com/paulxll/items/72a2bea9b1d1486ca751, brew install mecab-ipadic
    - for windows:  https://qiita.com/menon/items/f041b7c46543f38f78f7s
    - ※　mecab-ipadic-NEologdもインストールするように。（新語に対応）

    - python library insall
    - pip install -r requirement.txt
