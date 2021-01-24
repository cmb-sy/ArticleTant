# coding: utf-8
import sys
sys.path.append("../search")
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from get_paper_info import main
# from search.get_paper_info import make_input_txt

@respond_to('はじめる')
def mention_func(message):
    message.reply("論文キーワードを入力してね")

@listen_to('!essay(.*)$')
def comment_log(message, text):
    essay = main(text)
    # text = essay[0].encode('utf-8')
    message.reply(essay) 

# @respond_to('/essay')
# def essay(message):
#     essay = main()
#     message.reply(essay) 


# @respond_to('input_txt')
# def mention_func(message):
#     essay = main()
#     message.reply(essay) 
