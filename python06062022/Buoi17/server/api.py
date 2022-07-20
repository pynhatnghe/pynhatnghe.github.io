# File api.py
from fastapi import FastAPI
from .database_util import MySqlUtil

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.get("/loai", tags=["Category"])
def get_all_loai():
    data = MySqlUtil.query("SELECT * FROM loai")
    print(data)
    return data