import pyupbit

df = pyupbit.get_ohlcv("BTC")
df.to_excel("btc.xlsx")