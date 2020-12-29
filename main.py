import pandas as pd
import yfinance as yf
import os
import shutil
import json
import glob
from DataCleaning import cleaningData

stockNames = 'TSLA GOOG AAPL'
stockList = stockNames.split(" ")

tickers = yf.Tickers(stockNames)

data = []
for ticker in tickers.tickers:
    data.append(ticker.history(period="7d"))

cleaningData(stockList,data)