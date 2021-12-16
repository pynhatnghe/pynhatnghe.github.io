# pip install fastapi
# pip install uvicorn
# pip install python-multipart # Liên quan tới upload file

from typing import cast
from KhachHang import khach_hang
from fastapi import FastAPI, File, UploadFile
import os
import json
import shutil

app = FastAPI()


# Lấy thư mục hiện tại chứa file đang chạy
UPLOAD_DIRECTORY = os.getcwd()


@app.post("/images/single")
def upload_single_file(image: UploadFile = File(...)):
    try:
        filename = os.path.join(UPLOAD_DIRECTORY, "data", image.filename)
        with open(filename, "wb") as mybinfile:
            shutil.copyfileobj(image.file, mybinfile)

        return {"success": True, "filename": image.filename}
    except Exception as ex:
        print(ex)
        return {"success": False}


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
