import random
import tweepy
import setting
import pandas as pd

# custom parameter
# 日本のWOEID
woeid = 23424856
sentence = "OneTalkはワンタップでランダムな人と通話ができます。\n一期一会の会話がここではできます\n嫌な人は簡単にブロック\nhttps://apps.apple.com/jp/app/onetalk/id1660444348"

CONSUMER_KEY = setting.CONSUMER_KEY
CONSUMER_SECRET = setting.CONSUMER_SECRET
ACCESS_TOKEN = setting.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = setting.ACCESS_TOKEN_SECRET

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# トレンド取得
trends = api.get_place_trends(woeid)
df = pd.DataFrame(trends[0]["trends"])

# ツイート
message = f'{sentence}\n#{df.name[0]}\n#{df.name[1]}\n#{df.name[2]}'
client.create_tweet(text=message)