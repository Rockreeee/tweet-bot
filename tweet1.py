# http://westplain.sakuraweb.com/translate/twitter/API-Overview/Error-Codes-and-Responses.cgi

import tweepy
import setting
import pandas as pd 
import time
import datetime
import re
import random


# カスタムパラメーター＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 日本のWOEID
woeid = 23424856 
# 投稿する文章のリスト
sentenceList = [
    # ["OneTalkでランダム通話しよ～!!\n寝落ち、暇つぶしに!!\nビデオ通話なしで安心\nhttps://apps.apple.com/jp/app/onetalk/id1660444348\n#koemo\n#コエモ\n#オルカ\n#ロンリー\n#Maum", ["./assets/images/onetalk1.jpg", "./assets/images/onetalk2.jpg", "./assets/images/onetalk3.jpg"]],
    # ["「OneTalk」でランダムな人と通話しよ!!\n寝落ち、いろんな相談、暇つぶしに!\nビデオ通話はできないから安心!\nhttps://apps.apple.com/jp/app/onetalk/id1660444348", ["./assets/images/onetalk1.jpg", "./assets/images/onetalk2.jpg", "./assets/images/onetalk3.jpg"]],
    # ["「OneTalk」で通話しよ!!\n通話相手は「完全ランダム」!\n寝落ち、いろんな相談、暇つぶしに!\nビデオ通話はできないから安心!\nhttps://apps.apple.com/jp/app/onetalk/id1660444348", ["./assets/images/onetalk1.jpg", "./assets/images/onetalk2.jpg", "./assets/images/onetalk3.jpg"]],
    # ["「OneTalk」で一期一会の会話しよ!!\nランダムで通話する楽しさ!\n寝落ち通話、暇つぶし通話など!!\nhttps://apps.apple.com/jp/app/onetalk/id1660444348", ["./assets/images/onetalk1.jpg", "./assets/images/onetalk2.jpg", "./assets/images/onetalk3.jpg"]],
    # ["/\n「OneTalk」でランダムな人と通話。\n\ \n相談、眠れない、心の寂しさを埋めます。\n登録不要で通話し放題。\n「OneTalk」は心の拠り所になります。\n\n\nhttps://apps.apple.com/jp/app/onetalk/id1660444348\n\n", ["./assets/images/onetalk4.jpg", "./assets/images/onetalk5.jpg", "./assets/images/onetalk6.jpg", "./assets/images/onetalk7.jpg"]],
    # ["「LibertyMCバトル」でラップバトル&サイファー!!\n60種類を超えるビート!\nオンラインでマッチした相手とMCバトル!!\nhttps://rockreeee.github.io/LibertyMCBattle-web-page/", ["./assets/images/liberty1.png", "./assets/images/liberty2.png", "./assets/images/liberty3.png", "./assets/images/liberty4.png"]],
    # ["/\n「インチキルーレット」で確率は思いのまま!!\n\ \nルーレットで当たるものを操作できる!?\n当てたい項目を100%当てろ!!\n\n\nhttps://apps.apple.com/jp/app/%E3%82%A4%E3%83%B3%E3%83%81%E3%82%AD%E3%83%AB%E3%83%BC%E3%83%AC%E3%83%83%E3%83%88/id1666018138\n\n", ["./assets/images/roulette1.jpg", "./assets/images/roulette2.jpg", "./assets/images/roulette3.jpg"]],
    # ["/\n「早押しクイズで暗記」で楽しく暗記!!\n\ \n単語帳はもう買わなくていい!\nみんなで単語帳を作ろう♪\n資格勉強、暗記に最適('ω')\n\n\nhttps://rockreeee.github.io/MemorizationByQuiz-web-page/\n\n", ["./assets/images/study1.jpg", "./assets/images/study2.jpg", "./assets/images/study3.jpg", "./assets/images/study4.jpg"]],
    ["/\n「WhoAreU???」でグローバルビデオ通話!!\n\ \n言語も違う国の人と友達になろう\n言語の勉強、友達作りに最適!\n\niphoneの方\nhttps://apps.apple.com/jp/app/id6469033245\nAndroidの方\n", ["./assets/images/who1.jpg", "./assets/images/who2.jpg", "./assets/images/who3.jpg", "./assets/images/who4.jpg"]],
    # ["＼ ￥5,000キャッシュバック中💰 ／\n\n為替相場が上がるか下がるか予測するだけの簡単取引👀‼️\n無料のクイックデモで体験しよう🔥\n\n詳細はこちら：https://onl.bz/BRQ1VHP\n\n", ["./assets/images/ask_004.mp4"]]
]
# 投稿間隔
interval = 288
# カスタムパラメーター＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝



# 投稿する文章
randomSentence = ""
# 前回送信したメッセージ
beforeMessage = []
# 前回の文章と同じにならないように毎回数字をつける
dummyNumber = 0
# 文章の長さ計測
sentenceLength = 0

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
    for images in sentenceList:
        tempList = []
        for image in images[1]:
            filename = image
            media = api.media_upload(filename)
            tempList.append(media.media_id)

        mediaIdList.append(tempList)

    while True:
        # 現在時刻表示
        now = datetime.datetime.now() # 現在時刻の取得
        print('======================================================')
        print(now)
        
        # 文章と画像決定
        randomNum = random.randrange(0, len(sentenceList))
        randomSentence = sentenceList[randomNum][0]
        randomMediaIdList = mediaIdList[randomNum]
        
        # 文章の長さ取得
        sentenceLength = count_length_of_sentence(randomSentence)
        print("sentenceの長さは", sentenceLength)

        # トレンド取得
        trends = api.get_place_trends(woeid)
        df = pd.DataFrame(trends[0]["trends"]).name
        resultDf = []

        # #タグ消す処理
        for item in df:
            resultDf.append(item.replace("#", ''))

        # message作成
        message = make_sentence(resultDf, randomSentence)
        
        try:
            # ツイートを投稿する
            tweet = api.update_status(status=message, media_ids=randomMediaIdList)
            # client.create_tweet(text=message, media_ids=[media.media_key])
            print(f'ツイートしました。\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n{message}\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑\n======================================================', flush=True)
        
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
    # print(splitedSentence)

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


if __name__ == "__main__":
    main()