from datetime import datetime
import re
from googletrans import Translator
from time import sleep
import arxiv


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
    translator = Translator()
    return translator.translate(text, src=src, dest=dest).text


def translate_post(idx, result):

    title_jpn = get_translated(result.title.replace("\n",""), src="en", dest="ja")
    abst_jpn =  get_translated(result.summary.replace("\n",""), src="en", dest="ja")
    print("-------"+str(idx+1)+"ページ目-------")
    print("author: {}".format(result.author))
    print("url: {}".format(result.pdf_url))
    print("title: {}".format(title_jpn))
    print("date: {}".format(result.updated))
    print("Abstract: {}".format(abst_jpn))
    # sleep(5)


def main():

    keywords = ["情報学", "生物学"]

    input_txt = make_input_txt(keywords, prefix="abs:", condition="AND")

    query_text = get_translated(input_txt, src="ja", dest="en")
    results = arxiv.query(query = query_text, max_results=5, sort_by="submittedDate")

    for i, result in enumerate(results):

        translate_post(i, result)
        
    print("DONE")


if __name__ == "__main__":
    main()