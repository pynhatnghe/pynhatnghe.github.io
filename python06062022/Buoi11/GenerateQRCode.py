# pip install pyqrcode
# pip isntall pypng
import pyqrcode

# noi_dung = "PyNhatNghe chúc mừng bạn trúng thưởng 200 tỷ"
noi_dung = "PyNhatNghe"

myqrcode = pyqrcode.create(noi_dung, encoding="utf-8")

# Output
myqrcode.svg("NhatNgheQRCode.svg", scale=3)
myqrcode.png("NhatNgheQRCode.png", scale=8)
