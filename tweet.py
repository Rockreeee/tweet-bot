# http://westplain.sakuraweb.com/translate/twitter/API-Overview/Error-Codes-and-Responses.cgi

import tweepy
import setting
import pandas as pd
import time
import datetime
import re

# custom parameter
woeid = 23424856 # 日本のWOEID
sentence = "OneTalkはランダムな人と通話ができます!!\n一期一会の会話ができます!!\n嫌な人は簡単にブロック!!\nhttps://apps.apple.com/jp/app/onetalk/id1660444348"# 54 + 22
interval = 40

beforeMessage = []
dummyNumber = 0
sentenceLength = 0

CONSUMER_KEY = setting.CONSUMER_KEY
CONSUMER_SECRET = setting.CONSUMER_SECRET
ACCESS_TOKEN = setting.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = setting.ACCESS_TOKEN_SECRET

def main():
    print("----------------------TweetBot------------------------")
    print(" \|/        \|/       \|/      \|/      \|/      \|/  ")
    print("  |          |        \|/      \|/      \|/      \|/  ")
    print("  |   \/     |    //   |        |   \/   |/       |   ")
    print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
    print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
    print("□□□■■■■■■■□□□■□□■■□□■□□□■■■■■■□□□■■■■■■□□□■■■■■■■□□□□□")
    print("□□□□□□■□□□□□□■□□■■□□■□□□■□□□□□□□□■□□□□□□□□□□□■□□□□□□□□")
    print("□□□□□□■□□□□□□■□□■■□□■□□□■□□□□□□□□■□□□□□□□□□□□■□□□□□□□□")
    print("□□□□□□■□□□□□□■□□■■□□■□□□■□□□□□□□□■□□□□□□□□□□□■□□□□□□□□")
    print("□□□□□□■□□□□□□■□■□□■□■□□□■■■■■■□□□■■■■■■□□□□□□■□□□□□□□□")
    print("□□□□□□■□□□□□□■□■□□■□■□□□■□□□□□□□□■□□□□□□□□□□□■□□□□□□□□")
    print("□□□□□□■□□□□□□□■□□□□■□□□□■□□□□□□□□■□□□□□□□□□□□■□□□□□□□□")
    print("□□□□□□■□□□□□□□■□□□□■□□□□■□□□□□□□□■□□□□□□□□□□□■□□□□□□□□")
    print("□□□□□□■□□□□□□□■□□□□■□□□□■■■■■■□□□■■■■■■□□□□□□■□□□□□□□□")
    print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
    print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
    print(" \|/        \|/       \|/      \|/      \|/      \|/  ")
    print("  |          |        \|/      \|/      \|/      \|/  ")
    print("  |   \/     |    //   |        |   \/   |/       |   ")
    print("----------------------TweetBot------------------------")

    global dummyNumber, sentenceLength

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

    sentenceLength = countLengthOfSentence()
    print("sentenceの長さは", sentenceLength)

    while True:
        # 現在時刻表示
        now = datetime.datetime.now() # 現在時刻の取得
        print('======================================================')
        print(now)

        # トレンド取得
        trends = api.get_place_trends(woeid)
        df = pd.DataFrame(trends[0]["trends"]).name
        resultDf = []

        # #タグ消す処理
        for item in df:
            resultDf.append(item.replace("#", ''))
        
        try:
            # message作成
            message = makeSentence(resultDf)
            client.create_tweet(text=message)
            print(f'ツイートしました。\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n{message}\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑\n======================================================', flush=True)
        
        except tweepy.errors.Forbidden:
            print('前回メッセージと同じなので今回はツイートできませんでした。', flush=True)

        # 呼ばれないはず
        # except tweepy.errors.BadRequest:
        #     print('メッセージが長すぎて今回はツイートできませんでした。', flush=True)
        
        time.sleep(interval)

# ツイートする関数（トレンド配列, クライアント):
def makeSentence(resultDf):

    global dummyNumber, beforeMessage
    i = 0

    while True:
        if i == 0:
            message = f'{sentence}'
        message +=  f'\n#{resultDf[i]}'
        i += 1
        # 次ループで140文字を超えたら終了(URLは22文字になる)
        if sentenceLength + (len(message) - len(sentence)) + len(f'\n#{resultDf[i]}') > 140:
            break

    # beforeMessageが増えすぎないように(最大保持数99)
    if len(beforeMessage) == 99:
        del beforeMessage[0]

    # 前回メッセージと被っていないか
    if (message in beforeMessage) == False:
        beforeMessage.append(message)
    else:
        # dummyNumberが増えすぎないように
        if dummyNumber == 99:
            dummyNumber = 0
        if len(message) <= 138:
            message += f'\n{dummyNumber}'
            dummyNumber += 1
        else:
            message = message[0:-2] + f'\n{dummyNumber}'
            dummyNumber += 1
        beforeMessage.append(message)
        
    print("beforeMessage = ", beforeMessage)

    return message

def countLengthOfSentence():

    splitedSentence = re.split(r'(?=http)|(\n)', sentence)
    print(splitedSentence)

    # httpを取り除いた分の長さ
    result = ""
    httpCount = 0
    for string in splitedSentence:
        if string == None:
            continue
        if ("http" in string) == False:
            result += string
        else:
            httpCount += 1

    return len(result) + 22 * httpCount

if __name__ == "__main__":
    main()