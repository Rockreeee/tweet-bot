# TweetBot (宣伝用)
 
自作のアプリなどをtweeterで宣伝するためのBot
 
# Features
 
設定時間に一回tweetします。  
tweetの内容はカスタム可能ですが、デフォルトは以下のようになっています。  

![img](https://user-images.githubusercontent.com/103748137/209785890-f2722484-46a5-4a35-bfdf-07cba5db712d.png)
 
 
# Installation&Setup

https://developer.twitter.com/en/portal/dashboard
で以下の4つ作成
- Consumer Key(API Key)
- Consumer Secret(API Secret)
- Access Token
- Access Token Secret

(許可設定はreadとwriteとapiの解析ができるように設定してください。)

同じ階層にsetting.pyファイルを作る  
中身は  
```setting.py
CONSUMER_KEY = '****'  
CONSUMER_SECRET = '****'  
ACCESS_TOKEN = '****'  
ACCESS_TOKEN_SECRET = '****'  
```
 
tweepyのインストール
 
```
python pip install tweepy
```

実行
 
```
python tweet.py
```
 
# Note

以下の４つを漏らさないこと
```setting.py
CONSUMER_KEY = '****'  
CONSUMER_SECRET = '****'  
ACCESS_TOKEN = '****'  
ACCESS_TOKEN_SECRET = '****'  
```
 
# License

https://rockreeee.github.io/profile-web-page/