import pyupbit


timingEnum = {
    '1일': 'day', '1주': 'week', '한 달': 'month',
    '1분': 'minute1', '3분': 'minute3', '5분': 'minute5',
    '10분': 'minute10', '15분': 'minute15', '30분': 'minute30',
    '1시간': 'minute60', '4시간': 'minute240'
}


# 원화 보유량
def get_krw_balance(upbit):
    krw = upbit.get_balance("krw")
    return krw


# 코인 보유량
def get_coin_balance(upbit, ticker):
    coin = upbit.get_balance(ticker)
    return coin


#MA
def get_ma(upbit, ticker, cnt, timing):
    df = pyupbit.get_ohlcv(ticker, "minute10")
    close = df['close']
    ma = close.rolling(cnt).mean()
    return ma[-1]


# 구매
def buy_order(upbit, ticker, krw):
    unit = krw - (krw * 0.001) # 수수료
    buy_no = upbit.buy_market_order(ticker, unit)
    print("구매 : ", unit, "주문번호 : ", buy_no)


# 판매
def sell_order(upbit, ticker, coin):
    sell_no = upbit.sell_market_order(ticker, coin)
    print("판매 : ", coin, "주문번호 : ", sell_no)
