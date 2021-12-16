# pip install fastapi
# pip install uvicorn

from KhachHang import khach_hang
from fastapi import FastAPI
import os
import json

app = FastAPI()


# Chạy: uvicorn main:app
@app.get("/")
def api_root():
    return {"message": "Welcome to FastAPI"}


@app.get("/hello/{name}")  # host/hello/Admin
def say_hello(name: str):
    return f"Hello {name}"


@app.get("/khachhang/{maso}")
def read_data_customer(maso: int):
    # Đọc file json tương ứng với maso và trả về
    filename = f"data/kh{str(maso).zfill(3)}.json"
    if os.path.exists(filename):  # Nếu có
        with open(filename, "r", encoding="utf-8") as myfile:
            return {
                "success": True,
                "data": json.loads(myfile.read())
            }
    else:
        return {
            "success": False,
            "message": "Customer not found"
        }


#from KhachHang import khach_hang


@app.post("/khachhang")
def store_customer(model: khach_hang):
    try:
        mydata = {
            "ma_so": model.ma_so,
            "ho_ten": model.ho_ten,
            "email": model.email,
            "doanh_so": model.doanh_so,
            "active": model.active
        }
        json_string = json.dumps(mydata, indent=4)
        filename = f"data/kh{str(model.ma_so).zfill(3)}.json"
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(json_string)
        return {"succes": True, "message": "Create customer success"}
    except Exception as ex:
        print(ex)
        return {"succes": False, "message": "Create customer unsuccess"}
