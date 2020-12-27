import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from info import getInfo

tickers = yf.Tickers('TSLA GOOG AAPL')
tickers_info = getInfo(tickers)

#Matriz 2d, primeiro 0 corresponde a primeira lista, segundo zero corresponde ao primeiro elemento da primeira lista (Ticker)
for x in range(3):
    tickers_info[x][0].history(period="7d").to_csv("stockData.csv",mode='a', header=False)

#Adicionar um separador no csv para sabermos exatamente o IOF do ticker

#Adicionar gráficos dentro do csv para cada ticker

#Enviar o email

#Fazer ser no-hup 

#Fazer ser um script que rode na abertura do mercado (Pegar horário da abertura do Bovespa)

#Implementar paralelismo para o yf.Tickers()

#EXTRAS#
# Dados da semana (Toda sexta)
# Dados do mês (Todo fim de mês)
