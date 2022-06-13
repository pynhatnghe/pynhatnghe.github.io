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
product_found = tim_theo_ma_code(code, productList)

if product_found is None:
  print("Tìm không thấy sp mã ", code)
else:
  print("Tìm thấy sản phẩm",
        product_found["productName"],
        product_found.get("price", 0),
  )

# Mua hàng
orderList = []
while True:
  find_code = input("Nhập mã cần mua: ")
  found_product = tim_theo_ma_code(find_code, productList)
  if found_product:
    input_quantity = int(input("Số lượng mua: "))
    orderList.append(
      {
        'productCode': find_code,
        'qty': input_quantity,
        'total': input_quantity * found_product.get("price", 0)
      }
    )
    if input("Dừng mua (C/K)? ").upper() == "C":
      break

print(orderList)