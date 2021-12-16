# pip install fastapi
# pip install uvicorn
# pip install python-multipart # Liên quan tới upload file

from typing import cast
from KhachHang import khach_hang
from fastapi import FastAPI, File, UploadFile
import os
import json
import shutil
from typing import List
from router.khach_hang_router import router as kh_router

app = FastAPI()
app.include_router(kh_router)

# Lấy thư mục hiện tại chứa file đang chạy
UPLOAD_DIRECTORY = os.getcwd()


@app.post("/images/multiple", tags=["UploadFile"])
def upload_multiple_file(images: List[UploadFile] = File(...)):
    try:
        filenames = []
        for image in images:
            filename = os.path.join(UPLOAD_DIRECTORY, "data", image.filename)
            with open(filename, "wb") as mybinfile:
                shutil.copyfileobj(image.file, mybinfile)
            filenames.append(image.filename)

        return {"success": True, "filename": filenames}
    except Exception as ex:
        print(ex)
        return {"success": False}


@app.post("/images/single", tags=["UploadFile"])
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
