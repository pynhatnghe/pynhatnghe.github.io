import requests


def tra_cuu_lich_cup_dien(pe: str):
    '''Tra cứu lịch cúp điện theo mã khách hàng tại TPHCM'''
    url = 'https://cskh.evnhcmc.vn/Tracuu/ajax_thongTinCungCapDien_result'
    obj_data = {
        "loai_input": "ma_kh",
        "input_makh": pe,
        "tungay": "18/12/2021",
        "denngay": "25/12/2021"
    }
    response = requests.post(url, data=obj_data)
    print(response.text)


tra_cuu_lich_cup_dien('PE03000084356')
