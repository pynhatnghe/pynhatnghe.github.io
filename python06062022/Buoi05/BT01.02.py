''''Tính tích các phần tử của mảng'''
def multiply(mang):
    tich = 1
    for phan_tu in mang:
        tich *= phan_tu
    return tich

''' Một dấu sao: số lượng phần tử ko hạn ché, giá trị 1 
phần tử là giá trị đơn'''
global tich
tich = 0
def multiply2(*mang):
    tich = 1
    for phan_tu in mang:
        tich *= phan_tu
    return tich
print("tich", tich)
print(multiply([1,2,3,4,5]))
print("tich", tich)
print(multiply((1,2,3,4,5)))
print(multiply2(1,2,3,4,5))

''' Hai dấu sao **args: số lượng phần tử ko hạn chế cách nhau
bởi dấu , và giá trị mỗi phần tử dạng key=value'''
def demo_kargs(**kargs):
    for key,value in kargs.items():
        print(key,value)

demo_kargs(ten="Nhất Nghệ",tuoi=19,phone=39292174)
