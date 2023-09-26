import json

import requests

url = "https://www.koimaindex.com/koimaindex/koima/price/retrieveChartAjax.do"

headers = {
    "cookie": "_ga=GA1.1.1055061791.1692929765; JSESSIONID=2CF87C4838494F04AF4B28EAE61FC494; _ga_DETEGWT578=GS1.1.1695085690.23.1.1695085723.27.0.0"
}

param1 = {
    "priceSearchVO.subItemName": "철스크랩(H2)",
    "priceSearchVO.subItemNo": "172",
    "priceSearchVO.mainItemNo": "80",
    "priceSearchVO.searchMainItemNo": "80",
    "priceSearchVO.searchSubItemNo": "172",
    "priceSearchVO.searchDate": "2023-09-15",
    "priceSearchVO.searchCondition": "-730",
}

param2 = {
    "priceSearchVO.subItemName": "코발트(3M Official)",
    "priceSearchVO.subItemNo": "41",
    "priceSearchVO.mainItemNo": "79",
    "priceSearchVO.searchMainItemNo": "79",
    "priceSearchVO.searchSubItemNo": "",
    "priceSearchVO.searchDate": "2023-09-15",
    "priceSearchVO.searchCondition": "-730",
}

params = [param1, param2]
unitChange = ["$/tonne", "$/ton"]
resourceName = ["니켈", "리튬", "철스크랩", "코발트"]
resourceSymbol = ["Ni", "Li", "Fe", "Co"]
datas = []

for j in range(len(params)):
    response = requests.post(url, headers=headers, data=params[j])
    json_data = json.loads(response.text)

    for i in range(len(json_data["subItemInfoList"])):
        resource = json_data["subItemInfoList"][i]["subItemName"]
        unit = json_data["subItemInfoList"][i]["subItemUnit"]
        if "(" in resource:
            resource = resource.split("(")[0]
        if unit in unitChange:
            unit = "USD/ton"
        data = {
            "resourceTbSymbol": resourceSymbol[resourceName.index(resource)],
            "resourceDatePk": json_data["subItemInfoList"][i]["priceDate"],
            "price": float(json_data["subItemInfoList"][i]["daySum"]),
            "unitIdName": unit,
        }
        datas.append(data)

# print(datas)
jsondata = json.dumps(datas)
post_url = f"http://10.10.10.105:8080/resource/infosave"

headers = {"Content-Type": "application/json"}
r = requests.post(post_url, headers=headers, data=jsondata)

print(f"response: {response}")
