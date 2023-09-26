import datetime
import json
import re
import time
from collections import deque

import requests

# request로 크롤링
urls = [
    "https://www.komis.or.kr/komis/price/mineralprice/basemetals/pricetrend/baseMetals.do",
    "https://www.komis.or.kr/komis/price/mineralprice/minormetals/pricetrend/minorMetals.do",
]

param1 = {
    "mc_seq": "1010001",
    "mnrl_pc_mc_seq": "502",
    "avg_type": "K_PC_STAT",
    "from_ymd": "2021-09-26",
    "to_ymd": "2023-09-26",
    "lem_check": "Y",
    "mc_seq2": "",
    "mnrl_pc_mc_seq2": "",
}

param2 = {
    "mc_seq": "1020004",
    "mnrl_pc_mc_seq_p": "탄산리튬",
    "mnrl_pc_mc_seq": "516",
    "avg_type": "K_PC_STAT",
    "from_ymd": "2021-09-26",
    "to_ymd": "2023-09-26",
    "mc_seq2": "",
    "mnrl_pc_mc_seq_p2": "",
    "mnrl_pc_mc_seq2": "",
}

params = [param1, param2]

datas = []
resourceName = ["니켈", "리튬", "철스크랩", "코발트"]
resourceSymbol = ["Ni", "Li", "Fe", "Co"]
units = ["USD/ton", "RMB/kg"]

for i in range(len(urls)):
    response = requests.post(urls[i], data=params[i])
    content_list = deque(response.text.split("\n"))

    while content_list:
        line = content_list.popleft()

        if line.strip() == "series: [{":
            line = content_list.popleft()
            new_list = list(line.split())
            unit = new_list[-1][1:-2].split("(")[-1][:-1]

        if "var data1" in line:
            prices = []
            while line.strip() != "];":
                new_list = list(line.split())
                prices.append(float(new_list[-1]))
                line = line = content_list.popleft()

        if "xAxis" in line:
            line = content_list.popleft()
            dates = []
            while line.strip() != "]":
                new_list = list(line.split())
                dates.append(new_list[-1])
                line = line = content_list.popleft()

        if "광종선택" in line:
            line = content_list.popleft()
            while line.strip() != "</select>":
                if "selected" in line:
                    new_list = list(line.split())
                    resource = new_list[-1][1:-9]
                line = content_list.popleft()

    for i in range(len(prices)):
        data = {
            "resourceTbSymbol": resourceSymbol[resourceName.index(resource)],
            "resourceDatePk": dates[i][1:11],
            "price": float(prices[i]),
            "unitIdName": unit,
        }
        datas.append(data)

# print(datas)
jsondata = json.dumps(datas)
post_url = f"http://10.10.10.105:8080/resource/infosave"

headers = {"Content-Type": "application/json"}
r = requests.post(post_url, headers=headers, data=jsondata)

print(f"response: {response}")
