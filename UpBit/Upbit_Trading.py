import time
import datetime
import pyupbit
from slacker import Slacker

# 업비트
access = "qGOOWWtGAUIUTxmniGlha3uk0BSw2ihjkonnilhI"
secret = "sC9m0CxhcqheUYgOJffhVrhtpFGJB7e1Zn2yrr3v"
upbit = pyupbit.Upbit(access, secret)
# 슬랙
token = "xoxb-1627268376848-1600348788949-op5i8D7MdCi1v4Gk2A1bFIYn"
slack = Slacker(token)


def buy_crypto_currency(ticker):
    krw = upbit.get_balance("KRW")[2]
    orderbook = pyupbit.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    upbit.buy_market_order(ticker, unit)
    slack.chat.post_message(
        "#trading-event", " -> 구매 : " + str(unit), as_user=True)


def sell_crypto_currency(ticker):
    unit = upbit.get_balance("KRW")[0]
    upbit.sell_market_order(ticker, unit)
    slack.chat.post_message("#trading-event", " <- 판매 : " + str(unit), as_user=True)


def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target


def get_yesterday_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]


# 티커 리스트
print("[Ticker List]\n")
tickers = pyupbit.get_tickers()
number = 0
for itme in tickers:
    number = number + 1
    print("{0} : {1}".format(number, itme))
    
# 티커 선택
ticker_select = eval(input("\nticker 리스트 번호 : "))
ticker = tickers[ticker_select - 1]
print("Selected Ticker : ", ticker)

# 초기화
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_yesterday_ma5(ticker)
target_price = get_target_price(ticker)

# 가동 알림
print("\n트레이딩봇 가동합니다. " + str(now), " - Ticker : " + ticker,
      " - 타겟 가격 : " + str(target_price), " - MA5 : " + str(ma5), sep='\n')
slack.chat.post_message("#bitcoin", "트레이딩봇 가동합니다. " + str(now), as_user=True)
slack.chat.post_message("#bitcoin", " - Ticker : " + ticker, as_user=True)
slack.chat.post_message("#bitcoin", " - 타겟 가격 : " + str(target_price), as_user=True)
slack.chat.post_message("#bitcoin", " - MA5 : " + str(ma5), as_user=True)

# 트레이딩 루프
while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.delta(seconds=10):
            target_price = get_target_price(ticker)
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5 = get_yesterday_ma5(ticker)
            sell_crypto_currency(ticker)

        current_price = pyupbit.get_current_price(ticker)
        print("현재가 : " + str(current_price))
        if (current_price > target_price) and (current_price > ma5):
            buy_crypto_currency(ticker)
    except:
        print("에러 발생")
        #slack.chat.post_message("#bitcoin", "에러 발생", as_user=True)
    time.sleep(1)