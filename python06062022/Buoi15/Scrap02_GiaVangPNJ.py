import requests
from bs4 import BeautifulSoup
import schedule
import time

def scrap_pnj_price():
    pnj_url = "https://giavang.pnj.com.vn"
    r = requests.get(pnj_url)
    if r.status_code == 200:
        # print(r.text)

        # Save kết quả ra file text
        # with open("pnj_price.txt", "w", encoding="utf-8") as mf:
        #     mf.write(r.text)

        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup.prettify()) # html format (đẹp)
        # Lấy tất cả thẻ tr của trang
        result = soup.find_all('td')
        for td_item in result:
            # print(td_item)
            if td_item.get("valign") == "middle" and \
                td_item.get("align") == "center":
                print(td_item.text)


schedule.every(20).seconds.do(scrap_pnj_price)
while True:
    schedule.run_pending()
    time.sleep(1)