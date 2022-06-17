import datetime

# Liệt kê xem thư viện datetime có những packages/module nào
print(dir(datetime))
print(datetime.MINYEAR, datetime.MAXYEAR)
ngay_hien_tai = datetime.datetime.now()
ngay_hien_tai_utc = datetime.datetime.utcnow()
print(ngay_hien_tai)
print(ngay_hien_tai_utc)
print(ngay_hien_tai.strftime("%a %m %d, %Y %I:%M:%S %p"))

