import datetime
import time

import requests
from bs4 import BeautifulSoup as bs

resources = ["니켈", "리튬", "고철", "코발트"]
now = datetime.datetime.now()
start = (now - datetime.timedelta(days=1)).strftime("%Y.%m.%d.%H.%M")
end = now.strftime("%Y.%m.%d.%H.%M")
issues = []

for resource in resources:
    cnt = 1
    while 1:
        url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={resource}&sort=1&photo=0&field=0&pd=4&ds={start}&de={end}&mynews=1&office_type=2&office_section_code=8&news_office_checked=1001&nso=so%3Ar%2Cp%3A1d&is_sug_officeid=0&office_category=0&service_area=0&nso=so:dd,p:1d,a:all&start={cnt}"
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        elements = soup.find_all("a", class_="news_tit")
        if not elements:
            break
        for element in elements:
            if resource in element["title"]:
                print(element["title"], element["href"])
                issue = {
                    "resource": resource,
                    "title": element["title"],
                    "url": element["href"],
                    "issueDate": now.strftime("%Y.%m.%d"),
                }
                issues.append(issue)
        cnt += len(elements)
        time.sleep(2)

print(issues)
