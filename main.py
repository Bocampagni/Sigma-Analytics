import sys
import pandas as pd
import yfinance as yf
import os
import shutil
import json
import glob
from DataCleaning import cleaningData


stockList = sys.argv
stockList.pop(0) #Used to remove the first parameter ( file's name )

stockNames = " ".join(stockList)
tickers = yf.Tickers(stockNames)


tickerNames = []
data = []
for index,ticker in enumerate(tickers.tickers):
    returnedValue = ticker.history(period="7d")
    if(returnedValue.size > 0):

        data.append(returnedValue)
    else:
        stockList.pop(index)

cleaningData(stockList,data)