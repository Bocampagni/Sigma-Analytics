import json

def cleaningData(stockList,data):
    with open('data.json', 'w', encoding='utf-8') as f:
        output = []
        for x in range(len(stockList)):
            stock = [{"Ticker": stockList[x]}]
            data[x] = data[x].reset_index()
            stock.append(json.loads(data[x].to_json(orient="records",date_format="iso")))
            output.append(stock)

        json.dump(output, f, indent=4)