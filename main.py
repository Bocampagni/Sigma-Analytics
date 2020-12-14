import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import json

tickers = yf.Tickers('TSLA GOOG AAPL')

#Getting info
#Alocar em uma variavel o endereço de memória do objeto da iteração
#Alocar em uma variavel o .info da iteração

keys = ["longBusinessSummary", "city", "state", "country","industry","currency"]

tickers_info = []
for ticker in tickers.tickers:
   present_ticker = ticker
   info = ticker.info
   present_dict = {x:info[x] for x in keys}
   tickers_info.append([present_ticker, present_dict])

print(tickers_info)
   



