def fetchTickers(tickers_info, size):

    #Matriz 2d, primeiro 0 corresponde a primeira lista,
    #segundo zero corresponde ao primeiro elemento da primeira lista (Ticker) 
    for x in range(size):
        buffer = tickers_info[x][0].history(period="7d")
        buffer = buffer.append(tickers_info[x][0].history(period="7d"))
        buffer = buffer.append(tickers_info[x][0].history(period="7d"))

    return buffer

