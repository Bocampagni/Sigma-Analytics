import json

def cleaningData(stockList,data):

    file = open("data.json","w")
    file.write("[")
    for x in range(len(stockList)):
        file.write("[")
        dic_ticker = {"Ticker": stockList[x]}
        data[x] = data[x].reset_index()
        
        file.write(json.dumps(dic_ticker))
        file.write(",")
        var = data[x].to_json(orient="records",date_format="iso")
        parsed = json.loads(var)
        
        file.write(json.dumps(parsed, indent=4))
        file.write("]")
        if x != len(stockList) - 1:
            file.write(",")
        
    file.write("]")
    file.close()