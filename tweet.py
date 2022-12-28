import random
import tweepy
import setting
import pandas as pd
import time
import datetime

# custom parameter
# 日本のWOEID
woeid = 23424856
sentence = "OneTalkはワンタップでランダムな人と通話ができます！！\n一期一会の会話がここではできます！！\n嫌な人は簡単にブロック！！\nhttps://apps.apple.com/jp/app/onetalk/id1660444348"
interval = 900

CONSUMER_KEY = setting.CONSUMER_KEY
CONSUMER_SECRET = setting.CONSUMER_SECRET
ACCESS_TOKEN = setting.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = setting.ACCESS_TOKEN_SECRET

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

beforeMessage = ''

while True:
    # 現在時刻表示
    now = datetime.datetime.now() # 現在時刻の取得
    today = now.strftime('%Y年%m月%d日') # 現在時刻を年月曜日で表示
    print(today)

    # トレンド取得
    trends = api.get_place_trends(woeid)
    df = pd.DataFrame(trends[0]["trends"]).name
    resultDf = []

    # #タグ消す処理
    for item in df:
        resultDf.append(item.replace("#", ''))
    
    # message作成
    message = f'{sentence}\n#{resultDf[0]}\n#{resultDf[1]}\n#{resultDf[2]}\n#{resultDf[3]}\n#{resultDf[4]}\n#{resultDf[5]}'
    if beforeMessage != message:
        client.create_tweet(text=message)
        beforeMessage = message
        print(f'ツイートしました。\n================={message}\n=================')
    else:
        print('前回メッセージと同じなので今回はツイートしません。')

    time.sleep(interval)