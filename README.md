# TweetBot (宣伝用)
 
自作のアプリなどをtweeterで宣伝するためのBot
<img src="https://user-images.githubusercontent.com/103748137/209794987-1981a63e-e6aa-4ebe-9e1a-0cf9ce60db25.JPEG" width="200">
 
# Features
 
設定時間に一回ツイートします。  
ツイートの内容はカスタム可能ですが、デフォルトは以下のようになっています。  

<img src="https://user-images.githubusercontent.com/103748137/209789009-31313ae6-3391-4633-ab79-d29011c05476.JPEG" width="300">

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

追記

Pyinstallerを活用してEXEファイルを作成する場合は個人でお願いします。
 
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