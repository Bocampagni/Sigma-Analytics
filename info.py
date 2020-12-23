
def getInfo(tickers):
    # Getting info
    # Alocar em uma variavel o endereço de memória do objeto da iteração
    # Alocar em uma variavel o .info da iteração
    keys = ["longBusinessSummary", "city", "state", "country", "industry", "currency"]
    tickers_info = []
    for ticker in tickers.tickers:
        present_ticker = ticker
        info = ticker.info
        present_dict = {x: info[x] for x in keys}
        tickers_info.append([present_ticker, present_dict])

    return tickers_info