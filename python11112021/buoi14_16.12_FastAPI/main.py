# pip install fastapi
# pip install uvicorn

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
        with open(filename, "r") as myfile:
            return {
                "success": True,
                "data": myfile.read()
            }
    else:
        return {
            "success": False,
            "message": "Customer not found"
        }
