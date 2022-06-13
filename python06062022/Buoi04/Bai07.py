'''
Cho danh sách mặt hàng (theo mã, tên), giá.
YC nhập vào mã (code) in ra tên sp & giá
'''
productList = [
  {"code": "IP13", "productName": "Iphone 13", "price": 1300},
  {"code": "IP8", "productName": "Iphone 8", "price": 890},
  {"code": "IP110", "productName": "Iphone X", "price": 1110},
  {"code": "IP12", "productName": "Iphone 12", "price": 1289},
  {"code": "IP22", "productName": "Iphone 22"},
]
print(productList)

def tim_theo_ma_code(code: str, productList: list):
  '''Hàm tìm sản phẩm theo mã code'''
  for product_item in productList:
    if product_item.get("code") == code:
      return product_item

  return None

code = input("Nhập mã code: ")
product_found = None
for product_item in productList:
  if product_item.get("code") == code:
    product_found = product_item
    break

if product_found is None:
  print("Tìm không thấy sp mã ", code)
else:
  print("Tìm thấy sản phẩm",
        product_found["productName"],
        product_found.get("price", 0),
  )