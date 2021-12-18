# pip install beautifulsoup4
# pip install schedule

from typing import Iterator
import requests
from bs4 import BeautifulSoup
import schedule
import time


def scrap_gia_vang_pnj():
    print('BEGIN SCRAPPING DATA')
    # Bước 1: Gọi trang/API để lấy kết quả
    r = requests.get('https://giavang.pnj.com.vn/')

    print('Status:', r.status_code)
    # print(r.text)  # Content của trang

    # In nội dung craw được vào file text
    with open("giavang_pnj_raw.txt", "w", encoding="utf-8") as myfile:
        myfile.write(r.text)

    # Bước 2: Xử lý kết quả trả về
    soup = BeautifulSoup(r.text, features="html.parser")
    # print(soup.prettify())
    td_list = soup.find_all('td')
    # print(td_list)
    result = []
    for item in td_list:
        # print(item.text)
        # valign="middle" align="center"
        if item.get_attribute_list("valign") == ["middle"] and \
                item.get_attribute_list("align") == ["center"]:
            result.append(item.text)

    print(result)

    # Process data nhận được

    print("END SCRAPPING...")


schedule.every(7).seconds.do(scrap_gia_vang_pnj)
while True:
    schedule.run_pending()
    time.sleep(1)
