import os
import pyupbit


def get_upbit_key():
    path = os.getcwd() + "/.key/upbit key.txt"
    key = None
    secret = None

    with open(path) as f:
        lines = f.readlines()
        key = lines[0].strip()
        secret = lines[1].strip()
        
    return pyupbit.Upbit(key, secret)


# init
upbit = get_upbit_key()


# ticker split
def ticker_split():
    ticker = "KRW-BTC"
    print(ticker.split('-'))


# 10분간격 과거 내역 가져오기
def the_get_ohlcv_min10():
    df = pyupbit.get_ohlcv(ticker, "minute10")
    close = df['close']
    print(close[-2])
    print(close[-1])
    return close


# 비트코인 소유내역
def the_get_balance_BTC():
    unit = upbit.get_balance("BTC")
    return unit


# 모든 자산 소유내역
def the_get_balances():
    return upbit.get_balances()


# close에서 MA15 가져오기
def get_ma15(close):
    ma = close.rolling(15).mean()
    return ma


# 돈 넣는지 테스트
def buy_test():
    a = int(upbit.get_balance("KRW"))
    c = a - (a % 1000)
    buy_no = upbit.buy_market_order("KRW-BTC", c)
    print("구매 : ", c, "주문번호 : ", buy_no)
    

# 돈 빼는지 테스트
def sell_test():
    unit = upbit.get_balance("BTC")
    sell_no = upbit.sell_market_order("KRW-BTC", unit)
    print("매도 : ", unit, "주문번호 : ", sell_no)
