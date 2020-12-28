import pandas as pd
import yfinance as yf

stockNames = 'TSLA GOOG AAPL'
stockList = stockNames.split(" ")

tickers = yf.Tickers(stockNames)

data = []
for ticker in tickers.tickers:
    data.append(ticker.history(period="7d"))

for x in range(len(stockList)):
    data[x] = data[x].reset_index()
    data[x].to_json(stockList[x]+".json",orient="records",date_format="iso")


#Fazer ser um script que rode na abertura do mercado (Pegar horário da abertura do Bovespa)
#^10hrs -> 18h

#Implementar paralelismo para o yf.Tickers()

#EXTRAS#
# Dados da semana (Toda sexta)
# Dados do mês (Todo fim de mês)
