# http://westplain.sakuraweb.com/translate/twitter/API-Overview/Error-Codes-and-Responses.cgi

import tweepy
import setting
import pandas as pd
import time
import datetime

# custom parameter
woeid = 23424856 # 日本のWOEID
sentence = "OneTalkはランダムな人と通話ができます！！\n一期一会の会話ができます！！\n嫌な人は簡単にブロック！！\nhttps://apps.apple.com/jp/app/onetalk/id1660444348"
interval = 40

beforeMessage = []
dummyNumber = 0

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

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

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
            message = tweet(resultDf, client)
            # dummyNumber += 1
            print(f'ツイートしました。\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n{message}\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑\n======================================================', flush=True)
        
        except tweepy.errors.Forbidden:
            print('前回メッセージと同じなので今回はツイートできませんでした。', flush=True)

        # 呼ばれないはず
        # except tweepy.errors.BadRequest:
        #     print('メッセージが長すぎて今回はツイートできませんでした。', flush=True)
        
        time.sleep(interval)

# ツイートする関数（トレンド配列, クライアント):
def tweet(resultDf, client):

    global dummyNumber, beforeMessage
    i = 0

    while True:
        if i == 0:
            message = f'{sentence}'
        message +=  f'\n#{resultDf[i]}'
        i += 1
        # 次ループで140文字を超えたら終了
        if len(message) + len(f'\n#{resultDf[i]}') > 140:
            break

    # 前回メッセージと被っていないか
    if (message in beforeMessage) == False:
        beforeMessage.append(message)
        client.create_tweet(text=message)
    else:
        if dummyNumber == 99:
            dummyNumber = 0
        if len(message) <= 138:
            message += f'\n{dummyNumber}'
            dummyNumber += 1
        else:
            message = message[0:-2] + f'\n{dummyNumber}'
            dummyNumber += 1
        beforeMessage.append(message)
        client.create_tweet(text=message)
        
    print("beforeMessage = ", beforeMessage)

    return message

if __name__ == "__main__":
    main()