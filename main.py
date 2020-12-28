import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from info import getInfo
from sincronousExtractor import fetchTickers

tickers = yf.Tickers('TSLA GOOG AAPL')
tickers_info = getInfo(tickers)
data = fetchTickers(tickers_info,3).to_csv("stockData.csv")
    










#Adicionar gráficos dentro do csv para cada ticker

#Enviar o email

#Fazer ser no-hup 

#Fazer ser um script que rode na abertura do mercado (Pegar horário da abertura do Bovespa)
#^10hrs -> 18h

#Implementar paralelismo para o yf.Tickers()

#EXTRAS#
# Dados da semana (Toda sexta)
# Dados do mês (Todo fim de mês)
