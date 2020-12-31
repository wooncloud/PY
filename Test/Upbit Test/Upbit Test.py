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
ticker = "KRW-BTC"
print(ticker.split('-'))



df = pyupbit.get_ohlcv(ticker, "minute10")
close = df['close']
print(close[-2])
print(close[-1])
print(close)

btc = upbit.get_balance("BTC")
print(btc)
print(upbit.get_balances())



#ma = close.rolling(15).mean()




#balances = upbit.get_balances()
#print(balances)

#krw = upbit.get_balance("KRW")
#print(krw == None)

#btc = upbit.get_balance("BTC")
#print(btc == None)

#ada = upbit.get_balance("ADA")
#print(ada == None)