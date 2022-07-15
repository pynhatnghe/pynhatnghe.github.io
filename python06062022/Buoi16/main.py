from typing import Union, List
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

@app.get("/")
def root():
    return "MAIN PAGE"

@app.get("/hello")
def say_hello(name: str):
    return f"Hello Mr./Ms. {name}"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Gõ lệnh:
# uvicorn main:app --reload
# Mở web test:
# http://localhost:8000/
# http://localhost:8000/docs


@app.post("/uploadfile/")
def upload_file_to_folder(file: UploadFile):
    try:
        # Copy/move đến thư mục chỉ định
        destination = os.path.join(os.getcwd(), "files", file.filename)
        print("destination", destination)

        with open(destination, "wb") as my_file:
            shutil.copyfileobj(file.file, my_file)

        return { "success": True, "file_name": file.filename}
    except Exception as ex:
        print(ex)
        return  { "success": False, "message": ex}

@app.post("/uploadfiles/")
def upload_files_to_folder(files: List[UploadFile]):
    try:
        for file in files:
            # Copy/move đến thư mục chỉ định
            destination = os.path.join(os.getcwd(), "files", file.filename)
            print("destination", destination)

            with open(destination, "wb") as my_file:
                shutil.copyfileobj(file.file, my_file)

        return { "success": True}
    except Exception as ex:
        print(ex)
        return { "success": False, "message": ex}


@app.get("/download/{filename}")
def download(filename: str):
    # my_full_path = os.path.join(os.getcwd(), "files", filename)
    return FileResponse(
        filename=filename,
        path=os.path.join(os.getcwd(), "files")
    )