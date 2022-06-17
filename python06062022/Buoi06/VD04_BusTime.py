'''
Xe BUS tuyến số 1 Công trường Mê linh - Chợ lớn
chuyến đầu 5g30, chuyến cuối là 20g30, cách nhau 8phút
Yêu cầu: In ra thời gian xuất bến các chuyến
'''
from datetime import datetime, timedelta

hom_nay = datetime.now()
thoi_gian_dau = datetime(
    year=hom_nay.year,
    month=hom_nay.month,
    day=hom_nay.day,
    hour=5, minute=30, second=0
)
thoi_gian_cuoi= datetime(
    hom_nay.year,hom_nay.month,hom_nay.day,
    20, 30, 0
)
print(thoi_gian_dau, thoi_gian_cuoi)
DELTA_BETWEEN_2TRIP = 8
while thoi_gian_dau <= thoi_gian_cuoi:
    print(thoi_gian_dau)
    thoi_gian_dau += timedelta(minutes=DELTA_BETWEEN_2TRIP)