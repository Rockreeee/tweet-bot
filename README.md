#  宣伝TweetBot
 
<<<<<<< HEAD
=======
自作のアプリなどをtweeterで宣伝するためのBot。

簡単にTwitter上で宣伝できます。

1000viewなど簡単に得られるので、宣伝効果あります。

同じツイートはしないように設定されています。
>>>>>>> 7e3e0c45ca1fe6cab4907d0774a13e9e2d6e66af

<img src="https://user-images.githubusercontent.com/103748137/209810729-6c7d124e-4894-4a62-b633-fe9539e154d0.JPEG" width="250">
 
商品などをtwitterで宣伝するためのBotです

# Features
 
設定時間に一回ツイートします。  
ツイートの内容はカスタム可能ですが、デフォルトは以下のようになっています。  

<img src="assets/images/intro.jpg" alt="Image" width="400" >

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

<<<<<<< HEAD
- 使用は自己責任でお願いします

- Twitterの規約変更により一日のAPIの呼び出しが600?程に制限されました。そのため、ツイート頻度に注意。
=======
- 一時間に127ツイートが上限です。
>>>>>>> 7e3e0c45ca1fe6cab4907d0774a13e9e2d6e66af
 
# License

https://rockreeee.github.io/profile-web-page/