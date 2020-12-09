import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = yf.Ticker('TSLA')
tsla_df = ticker.history(period="max")
tsla_df["Close"].plot(title="TSLA's stock price")

plt.show()
