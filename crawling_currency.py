import datetime
import json
import re

import requests

now = datetime.datetime.now()
next = now
datas = []
while next > now - datetime.timedelta(days=10):
    url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=CL4oAp3eK5k3RrLGey77cdneNBFFb9BG&searchdate={next.strftime('%Y%m%d')}&data=AP01"

    response = requests.get(url)
    print(response.text)
    exchange_list = re.split("{*},", response.text)

    for i in range(len(exchange_list)):
        if "USD" in exchange_list[i]:
            info = re.split('"*"', exchange_list[i])
            for j in range(len(info)):
                if info[j] == "ttb":
                    data = {
                        "exchangeDatePk": next.strftime("%Y-%m-%d"),
                        "exchangeRate": info[j + 2],
                        "currencyName": "USD",
                    }
                    print(data)
                    datas.append(data)
        if "CNH" in exchange_list[i]:
            info = re.split('"*"', exchange_list[i])
            for j in range(len(info)):
                if info[j] == "ttb":
                    data = {
                        "exchangeDatePk": next.strftime("%Y-%m-%d"),
                        "exchangeRate": info[j + 2],
                        "currencyName": "RMB",
                    }
                    datas.append(data)
    next -= datetime.timedelta(days=1)

jsondata = json.dumps(datas)
post_url = f"http://10.10.10.105:8080/exchange/infosave"

headers = {"Content-Type": "application/json"}
r = requests.post(post_url, headers=headers, data=jsondata)

print(f"response: {response}")
