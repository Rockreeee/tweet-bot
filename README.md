# TweetBot (宣伝用)
 
自作のアプリなどをtweeterで宣伝するためのBot。

簡単にTwitter上で宣伝できます。

1000viewなど簡単に得られるので、宣伝効果あります。

同じツイートはしないように設定されています。

<img src="https://user-images.githubusercontent.com/103748137/209810729-6c7d124e-4894-4a62-b633-fe9539e154d0.JPEG" width="250">
 
# Features
 
設定時間に一回ツイートします。  
ツイートの内容はカスタム可能ですが、デフォルトは以下のようになっています。  

<img src="https://user-images.githubusercontent.com/103748137/209810633-3350e324-e223-4ee4-88d2-48c7a11cc188.JPEG" width="500">

設定したメッセージとその時のトレンドを含んだ文章が一定時間に一回ツイートされます。
 
 
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
停止  
```
ctrl + c
```
バックグラウンド実行
```
nohup python tweet.py　> log.txt &
```
バックグラウンドタスク確認
```
ps u
```
バックグラウンド停止
```
kill -KILL PID
```

追記

Pyinstallerを活用してEXEファイルを作成する場合は個人でお願いします。
 
# Note

- 以下の４つを漏らさないこと
```setting.py
CONSUMER_KEY = '****'  
CONSUMER_SECRET = '****'  
ACCESS_TOKEN = '****'  
ACCESS_TOKEN_SECRET = '****'  
```

- 一時間に127ツイートが上限です。
 
# License

https://rockreeee.github.io/profile-web-page/