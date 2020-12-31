import os
import time
import datetime
import pyupbit
from slacker import Slacker


# 변수 선언
state_delay = 5
trade_delay = 10
current_hour = None
ma_count = 15
up_flag = True
trade_flag = True


def get_upbit_key():
    path = os.getcwd() + "/.key/upbit key.txt"
    key = None
    secret = None

    with open(path) as f:
        lines = f.readlines()
        key = lines[0].strip()
        secret = lines[1].strip()
        
    return pyupbit.Upbit(key, secret)


def get_slack_key():
    path = os.getcwd() + "/.key/slackToken.txt"
    token = None
    with open(path) as f:
        lines = f.readlines()
        token = lines[0].strip()
        
    return token


def get_ma(ticker, cnt=15):
    df = pyupbit.get_ohlcv(ticker, "minute10")
    close = df['close']
    ma = close.rolling(cnt).mean()
    return ma[-1]


def get_close_10min(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute10")
    close = df['close']
    return close


# 구매
def buy_order(ticker, krw):
    unit = krw - (krw * 0.001) # 수수료
    buy_no = upbit.buy_market_order(ticker, unit)
    print("구매 : ", unit, "주문번호 : ", buy_no)
    slack.chat.post_message("#trading-event", " -> 구매 : " + str(unit) + " / " + str(buy_no), as_user=True)


# 판매
def sell_order(ticker, coin):
    sell_no = upbit.sell_market_order(ticker, coin)
    print("판매 : ", coin, "주문번호 : ", sell_no)
    slack.chat.post_message("#trading-event", " <- 판매 : " + str(coin) + " / " + str(sell_no), as_user=True)


# 티커 선택
def select_ticker():
    ticker = input("## ticker 입력 : KRW-")
    ticker = "KRW-" + ticker
    print("Selected Ticker : ", ticker)
    return ticker


# 가동 알림
def start_alert(now, ticker, ma, slack):
    print("\n트레이딩봇 가동합니다. " + str(now), " - Ticker : " + ticker, " - MA : " + str(ma), sep='\n')
    slack.chat.post_message("#trading-log", "=============================", as_user=True)
    slack.chat.post_message("#trading-log", "트레이딩봇 가동합니다. " + str(now), as_user=True)
    slack.chat.post_message("#trading-log", " - Ticker : " + ticker, as_user=True)
    slack.chat.post_message("#trading-log", " - MA : " + str(ma), as_user=True)
    print("\n", "=============================")


# init
upbit = get_upbit_key()
slack = Slacker(get_slack_key())

# Select Ticker
ticker = select_ticker()

# Standby
current_hour = time.localtime(time.time()).tm_hour - 1
ma = get_ma(ticker, ma_count)
start_alert(datetime.datetime.now(), ticker, ma, slack)

# 트레이딩 루프
while True:
    try:
        tm = time.localtime(time.time())
        current_price = pyupbit.get_current_price(ticker)
        ma = get_ma(ticker, ma_count)
        krw = upbit.get_balance(ticker.split('-')[0])
        coin = upbit.get_balance(ticker.split('-')[1])

        # 10분마다 1번씩
        if tm.tm_min % trade_delay == 0 and trade_flag:
            trade_flag = False

            # 하락세
            if (get_close_10min(ticker)[-2] > get_close_10min(ticker)[-1]) and (coin is not None):
                # Sell
                sell_order(ticker, coin)
            else:
                # Buy
                if (current_price > ma) and (up_flag == False):
                    up_flag = True
                    if krw is not None:
                        buy_order(ticker, krw)
                elif (current_price < ma) and (up_flag == True):
                    up_flag = False
        elif tm.tm_min % trade_delay > 0:
            trade_flag = True

        if tm.tm_sec % state_delay == 0:
            print("현재가 : ", current_price)
            print("MA : ", ma)
            print(ticker.split('-')[0], " : ", krw)
            print(ticker.split('-')[1], " : ", coin)
            print("------------------------")
        if tm.tm_hour != current_hour:
            current_hour = tm.tm_hour
            slack.chat.post_message("#trading-log", ("------------------------"), as_user=True)
            slack.chat.post_message("#trading-log", "[현재 현황]" + str(datetime.datetime.now()), as_user=True)
            slack.chat.post_message("#trading-log", ticker + " 현재가 : " + str(current_price), as_user=True)
            slack.chat.post_message("#trading-log", ticker + " : " + str(coin), as_user=True)
            slack.chat.post_message("#trading-log", "KRW : " + str(krw), as_user=True)
            slack.chat.post_message("#trading-log", ("------------------------"), as_user=True)
    except:
        print("에러 발생")
        slack.chat.post_message("#trading-log", "에러 발생", as_user=True)
    time.sleep(1)

# TODO : 1분마다 급락 모니터링해서 위험방지