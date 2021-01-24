import arxiv
from datetime import datetime
from sklearn.datasets import fetch_20newsgroups
import MeCab
import numpy as np
from time import sleep
from sklearn.feature_extraction.text import TfidfVectorizer
from googletrans import Translator
import re

# keywordをいくつまで考慮するか。
KEYWORD_NUM = 2

# arxiv.query()の引数設定

MAX_RESULTS = 3
SORT_BY = "submittedDate"
text = ""

def make_input_txt(keywords, prefix, condition):

    input_txt = ""
    _condition = " " + condition + " "
    for i, keyword in enumerate(keywords):
        if not i==len(keywords)-1:
           input_txt += prefix + keyword + _condition
        else:
           input_txt += prefix + keyword 
    
    return input_txt

def get_translated(text, src="en", dest="ja"):
    # translator = Translator()
    translator = Translator(service_urls=['translate.googleapis.com'])
    return translator.translate(text, src=src, dest=dest).text

def translate_post(idx, result):

    title_jpn = get_translated(result.title.replace("\n",""), src="en", dest="ja")
    abst_jpn =  get_translated(result.summary.replace("\n",""), src="en", dest="ja")
    result_text =str("author: {}".format(result.author)+ '\n'+ "url: {}".format(result.pdf_url) + '\n'+ "title: {}".format(title_jpn)+ '\n'+"date: {}".format(result.updated)+ '\n'+"Abstract: {}".format(abst_jpn))+'\n'+'\n'+'\n'+'\n'+'\n'
    return result_text
    # print("-------"+str(idx+1)+"ページ目-------")
    # print("author: {}".format(result.author))
    # print("url: {}".format(result.pdf_url))
    # print("title: {}".format(title_jpn))
    # print("date: {}".format(result.updated))
    # print("Abstract: {}".format(abst_jpn))
    # sleep(5)

def get_keyword(input_txt):

    # 単語の分かちわけができていること前提
    docs = [extract(input_txt)]

    vectorizer = TfidfVectorizer(min_df=0.03)
    tfidf_X = vectorizer.fit_transform(docs).toarray()

    index = tfidf_X.argsort(axis=1)[:,::-1] # 各文書のTF-IDF値にもとづいて降順ソートされたindexを得る.
    # print('index:', index)
    feature_names = np.array(vectorizer.get_feature_names())
    # print('feature_names:', feature_names)
    feature_words = feature_names[index]
    print('feature_words:', feature_words)

    return feature_words[0][:KEYWORD_NUM]
 

def extract(text):

    # Taggerオブジェクトを生成
    # デフォルトの辞書を読み込む.
    # tokenizer = MeCab.Tagger("-Ochasen")
    # 新語に対応した辞書を読み込む
    tokenizer = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    tokenizer.parse("")

    words = []

    # 単語の特徴リストを生成
    node = tokenizer.parseToNode(text)

    while node:
        # 品詞情報(node.feature)が名詞ならば
        if node.feature.split(",")[0] == u"名詞":
            # 単語(node.surface)をwordsに追加
            words.append(node.surface)
        node = node.next

    # 半角スペース区切りで文字列を結合
    text_result = ' '.join(words)
    return text_result


def main(INPUT_TXT):

    global text

    keywords = get_keyword(INPUT_TXT) # ex: keywords = ["情報学", "生物学"]

    print(keywords)

    query_txt_jp = make_input_txt(keywords, prefix="abs:", condition="AND")

    query_txt_en = get_translated(query_txt_jp, src="ja", dest="en")

    print(query_txt_en)
    query_txt_en += ' AND (cs.AI OR cs.CV)'
    print(query_txt_en)

    results = arxiv.query(query = query_txt_en, max_results=MAX_RESULTS, sort_by=SORT_BY)

    # if not len(results)==0:
    for i, result in enumerate(results):
        print(i)
        text += translate_post(i, result) + '\n'
    return text
    # else:
    #     return ("文章を変えてみてね。")
    print("DONE.")

if __name__ == "__main__":
    main()

