import yfinance as yf, pandas as pd, shutil, os, time, glob,smtplib, ssl
from get_all_ticjers import get_tickers as gt

tickers = gt.get_tickers_filtered(mktcap_min=150000, mktcap_max=10000000)
print("The amount of stockes chosen to oberse: " + str(len(tickers)))

