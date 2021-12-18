import requests
from bs4 import BeautifulSoup


def scrap_gold_data():
    url = 'https://www.pnj.com.vn/blog/gia-vang/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Lấy khối aside chứa bảng giá vàng (id = ty_gia_gia_vang_widget-2)
    result = soup.find(id='ty_gia_gia_vang_widget-2')
    ten_loais = result.find_all('td', class_='colorGrey')
    gia_muas = result.find_all('td', class_='price_in')
    gia_bans = result.find_all('td', class_='price_out')
    tens = []
    muas = []
    bans = []
    for item in ten_loais:
        tens.append(item.text.strip())
    for item in gia_muas:
        data_process_gia_mua = item.find_all('span', class_='fixW')
        if len(data_process_gia_mua) > 0:
            muas.append("".join(item.text.split(',')))
    for item in gia_bans:
        data_process_gia_ban = item.find_all('span', class_='fixW')
        if len(data_process_gia_ban) > 0:
            bans.append("".join(item.text.split(',')))
    print(tens, muas, bans)

    gold_prices = []
    if len(tens) == len(muas) and len(muas) == len(bans):
        for index in range(0, len(tens)):
            gold_prices.append({
                "loai": tens[index],
                "mua": int(muas[index]),
                "ban": int(bans[index])
            })

        # Lưu kết quả xuống file json
        from datetime import datetime
        import json
        file_name = "gold_price_" + \
            datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".json"
        with open(file_name, "w", encoding="utf-8") as myfile:
            json.dump(gold_prices, myfile, indent=4, ensure_ascii=False)


scrap_gold_data()
