import requests
from bs4 import BeautifulSoup

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
    result = soup.find_all('tr')
    for tr_item in result:
        print(tr_item)
