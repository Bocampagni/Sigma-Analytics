import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from info import getInfo
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference

tickers = yf.Tickers('TSLA GOOG AAPL')
tickers_info = getInfo(tickers)

tickers_info[0][0].history(period="2d")["Open"].plot(figsize=(16,9))
# plt.subplot().bar(tickers_info[0][0].history(period="2d")["Open"])
plt.show()



# Dados do dia
# Dados da semana
# Dados do mês
# Dados do ano
# Dados dos últimos 5 anos
# Dados desde o começo
