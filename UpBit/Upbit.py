import pyupbit
import time

access = "qGOOWWtGAUIUTxmniGlha3uk0BSw2ihjkonnilhI"
secret = "sC9m0CxhcqheUYgOJffhVrhtpFGJB7e1Zn2yrr3v"

upbit = pyupbit.Upbit(access, secret)
ticker = "KRW-BTC"
print(ticker.split('-'))


df = pyupbit.get_ohlcv(ticker, "minute10")
close = df['close']
print(close[-2])
print(close[-1])
print(close)

tm = time.localtime(time.time())
print("year:", tm.tm_year)
print("month:", tm.tm_mon)
print("day:", tm.tm_mday)
print("hour:", tm.tm_hour)
print("minute:", tm.tm_min)
print("second:", tm.tm_sec)

print("\n\n\n")
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