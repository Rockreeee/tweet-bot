# http://westplain.sakuraweb.com/translate/twitter/API-Overview/Error-Codes-and-Responses.cgi

# NextBuzzzz

import tweepy
import setting
import pandas as pd 
import time
import datetime
import re
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os


# カスタムパラメーター===================================
# 投稿する文章のリスト
tweetList = [
    ["/\n「OneTalk」でランダムな人と通話。\n\ \n\n", ["./assets/images/onetalk4.jpg", "./assets/images/onetalk5.jpg", "./assets/images/onetalk6.jpg", "./assets/images/onetalk7.jpg"], ["iphoneの方はこちらから→\nhttps://apps.apple.com/jp/app/onetalk/id1660444348", "Androidの方はこちらから→\nhttps://play.google.com/store/apps/details?id=com.gmail.mmakt122.onetalk"]],
    # ["/\n「インチキルーレット」で確率は思いのまま!!\n\ \nルーレットで当たるものを操作できる!?\n当てたい項目を100%当てろ!!\n\n\nhttps://apps.apple.com/jp/app/%E3%82%A4%E3%83%B3%E3%83%81%E3%82%AD%E3%83%AB%E3%83%BC%E3%83%AC%E3%83%83%E3%83%88/id1666018138\n\n", ["./assets/images/roulette1.jpg", "./assets/images/roulette2.jpg", "./assets/images/roulette3.jpg"]],
    # ["/\n「早押しクイズで暗記」で楽しく暗記!!\n\ \n単語帳はもう買わなくていい!\nみんなで単語帳を作ろう♪\n資格勉強、暗記に最適('ω')\n\n\nhttps://rockreeee.github.io/MemorizationByQuiz-web-page/\n\n", ["./assets/images/study1.jpg", "./assets/images/study2.jpg", "./assets/images/study3.jpg", "./assets/images/study4.jpg"]],
    # ["＼ ￥5,000キャッシュバック中💰 ／\n\n為替相場が上がるか下がるか予測するだけの簡単取引👀‼️\n無料のクイックデモで体験しよう🔥\n\n詳細はこちら：https://onl.bz/BRQ1VHP\n\n", ["./assets/images/ask_004.mp4"]]
    ["/\n「WhoAreU???」でグローバルビデオ通話!!\n\ \n\n", ["./assets/images/who4.jpg", "./assets/images/who1.jpg", "./assets/images/who2.jpg", "./assets/images/who3.jpg"], ["iphoneの方はこちらから→\nhttps://apps.apple.com/jp/app/id6469033245", "Androidの方はこちらから→\nhttps://play.google.com/store/apps/details?id=com.gmail.mmakt122.whoareu"]],
]
# 投稿間隔
interval = 288
# Chrome Driverのパスを指定
chrome_driver_path = "D:\\application\\ChromeDriver\\chromedriver.exe"
# ======================================================


# Chrome Driver
driver = webdriver.Chrome()
# 投稿する文章
randomSentence = ""
# 前回送信したメッセージ
beforeMessage = []
# 前回の文章と同じにならないように毎回数字をつける
dummyNumber = 0
# 文章の長さ計測
sentenceLength = 0
# tweetの最大の長さ
maxLength = 140


CONSUMER_KEY = setting.CONSUMER_KEY
CONSUMER_SECRET = setting.CONSUMER_SECRET
ACCESS_TOKEN = setting.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = setting.ACCESS_TOKEN_SECRET


def main():
    print("-------------------------------TweetBot--------------------------------")
    print("  \|/        \|/       \|/       \|/       \|/      \|/        \|/     ")
    print("   |          |        \|/       \|/       \|/      \|/        \|/     ")
    print("   |   \/     |    //   |         |    \/   |/       |         \|/     ")
    print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
    print("□■■■■■■■□□■□□■■□□■□□■■■■■■□□■■■■■■□□■■■■■■■□□■■■■■□□□□□■■■□□□□■■■■■■■□□")
    print("□□□□■□□□□□■□□■■□□■□□■□□□□□□□■□□□□□□□□□□■□□□□□■□□□□■□□□■□□□■□□□□□□■□□□□□")
    print("□□□□■□□□□□■□□■■□□■□□■□□□□□□□■□□□□□□□□□□■□□□□□■□□□□■□□■□□□□□■□□□□□■□□□□□")
    print("□□□□■□□□□□■□■□□■□■□□■■■■■■□□■■■■■■□□□□□■□□□□□■■■■□□□□■□□□□□■□□□□□■□□□□□")
    print("□□□□■□□□□□■□■□□■□■□□■□□□□□□□■□□□□□□□□□□■□□□□□■□□□□■□□■□□□□□■□□□□□■□□□□□")
    print("□□□□■□□□□□□■□□□□■□□□■□□□□□□□■□□□□□□□□□□■□□□□□■□□□□■□□□■□□□■□□□□□□■□□□□□")
    print("□□□□■□□□□□□■□□□□■□□□■■■■■■□□■■■■■■□□□□□■□□□□□■■■■■□□□□□■■■□□□□□□□■□□□□□")
    print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
    print("  \|/        \|/       \|/       \|/       \|/      \|/        \|/     ")
    print("   |          |        \|/       \|/       \|/      \|/        \|/     ")
    print("   |   \/     |    //   |         |    \/   |/       |         \|/     ")
    print("-------------------------------TweetBot--------------------------------")


    global dummyNumber, sentenceLength, randomSentence


    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

    # 画像をアップロード
    mediaIdList = []
    for images in tweetList:
        tempList = []
        for image in images[1]:
            filename = image
            media = api.media_upload(filename)
            tempList.append(media.media_id)

        mediaIdList.append(tempList)


    # Chrome Driver 起動
    start_chrome_driver()


    while True:
        # 現在時刻表示
        now = datetime.datetime.now() # 現在時刻の取得
        print('======================================================')
        print(now)

        # トレンド取得
        trends = get_trends()

        # #タグ消す処理
        resultDf = []
        for item in trends:
            resultDf.append(item.replace("#", ''))
        
        # 文章と画像決定
        randomNum = random.randrange(0, len(tweetList))
        randomSentence = tweetList[randomNum][0]
        randomMediaIdList = mediaIdList[randomNum]

        # ios版とandroid版の文
        replySentence1 = tweetList[randomNum][2][0]
        replySentence2 = tweetList[randomNum][2][1]
        
        # 文章の長さ取得
        sentenceLength = count_length_of_sentence(randomSentence)
        print("sentenceの長さは", sentenceLength)

        # message作成
        message = make_sentence(resultDf, randomSentence)
        
        try:
            # ツイートを投稿する
            tweet = client.create_tweet(text=message, media_ids=randomMediaIdList)

            print(f'ツイートしました。\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n{message}\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑', flush=True)

            # ID取得
            tweet_id = tweet.data['id']
            print("tweet_idは", tweet_id)

            # リプライ
            client.create_tweet(text=replySentence1, in_reply_to_tweet_id=tweet_id)
            print(f'リプライしました。\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n{replySentence1}\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑', flush=True)
            client.create_tweet(text=replySentence2, in_reply_to_tweet_id=tweet_id)
            print(f'リプライしました。\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n{replySentence2}\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑', flush=True)
            print('======================================================')

        
        except tweepy.errors.Forbidden:
            print('前回メッセージと同じなので今回はツイートできませんでした。', flush=True)

        except tweepy.errors.TwitterServerError:
            print('サーバーエラーです。0', flush=True)
            time.sleep(60)

        except requests.exceptions.ConnectionError:
            print('サーバーエラーです。1', flush=True)
            time.sleep(60)

        except tweepy.errors.TooManyRequests:
            print('サーバーエラーです。2', flush=True)
            time.sleep(60)
            
        except tweepy.errors.TweepyException:
            print('サーバーエラーです。3', flush=True)
            time.sleep(120)
            
        # 呼ばれないはず
        # except tweepy.errors.BadRequest:
        #     print('メッセージが長すぎて今回はツイートできませんでした。', flush=True)
        
        time.sleep(interval)


# デフォルトの文章の文字数カウント
def count_length_of_sentence(sentence):

    splitedSentence = re.split(r'(?=http)|(\n)', sentence)

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


# ツイートする文章作成（トレンド配列, message):
def make_sentence(resultDf, sentence):

    global dummyNumber, beforeMessage
    i = 0

    while True:
        if i == 0:
            message = f'{sentence}'
        message +=  f'\n#{resultDf[i]}'
        i += 1
        # 次ループで140文字を超えたら終了(URLは22文字になる)
        if sentenceLength + (len(message) - len(sentence)) + len(f'\n#{resultDf[i]}') > maxLength:
            break

    # beforeMessageが増えすぎないように(最大保持数99)
    if len(beforeMessage) == 99:
        del beforeMessage[0]

    # 前回メッセージと被っていないか
    if (message in beforeMessage) == False:
        beforeMessage.append(message)
    else:
        # dummyNumberが増えすぎないように
        if dummyNumber == 100:
            dummyNumber = 0
        if len(message) <= 138:
            message += f'\n{dummyNumber}'
            dummyNumber += 1
        else:
            message = message[0:-2] + f'\n{dummyNumber}'
            dummyNumber += 1
        beforeMessage.append(message)
        
    # print("beforeMessage = ", beforeMessage)

    return message


# トレンド取得
def get_trends():

    url = "https://twitter.com/explore/tabs/trending"

    # ページが開くまで待つ最大時間
    wait_time = 30

    # ページを開く
    driver.get(url)
    
    # ページが開くまで待機
    try:
        element_present = EC.presence_of_element_located((By.TAG_NAME, 'body'))
        WebDriverWait(driver, wait_time).until(element_present)
        print("ページが開かれました！")
    except TimeoutException:
        print("ページの読み込みに失敗しました。")

    time.sleep(10)

    # 複数の要素を取得
    elements = driver.find_elements(By.CLASS_NAME, "css-901oao")

    # 取得した要素のテキストを表示
    elements_list = []
    for element in elements:
        elements_list.append(element.text)
        
    # データ成型
    # 最初によくわからないものが入っているためそれを削除
    search_string = "For you"
    index = elements_list.index(str(search_string))
    del elements_list[:index]

    # print(elements_list)

    # トレンド1位から10位まで取得
    trends = []
    for i in range(10):
        search_string = i + 1
        index = elements_list.index(str(search_string))
        trends.append(elements_list[index + 6])

    # print(trends)

    return trends


def start_chrome_driver():

    # 環境変数にChrome Driverのパスを設定
    os.environ["webdriver.chrome.driver"] = chrome_driver_path

    # twitterを開く
    driver.get('https://twitter.com/explore/tabs/trending')

    # ブラウザが閉じられないように一時停止（Enterキーを押すまで待機）
    input("ログインが完了したらEnterキーを押してください...")


if __name__ == "__main__":
    main()