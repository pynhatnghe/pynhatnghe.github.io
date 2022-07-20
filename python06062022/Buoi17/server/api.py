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


@app.get("/loai/{ma_loai}", tags=["Category"])
def get_loai(ma_loai: int):
    sql = f"SELECT * FROM loai WHERE MaLoai = {ma_loai}"
    data = MySqlUtil.query(sql)
    if len(data) == 0:
        return None
    return data[0]

@app.get("/loai/search/by", tags=["Category"])
def search_loai(keyword: str):
    sql = f"SELECT * FROM loai WHERE TenLoai LIKE '%{keyword}%'"
    print(sql)
    data = MySqlUtil.query(sql)
    print(data)
    return data

from pydantic import BaseModel
class Loai(BaseModel):
    TenLoai: str
    Hinh: str

@app.post("/loai", tags=["Category"])
def insert_loai(model: Loai):
    sql = f'''
    INSERT INTO `loai` (`MaLoai`, `TenLoai`, `Hinh`) 
    VALUES (NULL, '{model.TenLoai}', '{model.Hinh}');
    '''
    new_loai_id = MySqlUtil.insert_and_get_lasted_id(sql)
    if new_loai_id:
        return {
            "success": True,
            "data": MySqlUtil.query(
                f"SELECT * FROM loai WHERE MaLoai = {new_loai_id}"
            )
        }
    else:
        return {
            "success": False,
            "message": "Thêm loại không thành công"
        }


@app.delete("/loai/{ma_loai}", tags=["Category"])
def delete_loai(ma_loai: int):
    sql = f"DELETE FROM loai WHERE MaLoai = {ma_loai}"
    if MySqlUtil.execute(sql):
        return {"success": True}
    return {"success": True}

@app.put("/loai/{ma_loai}", tags=["Category"])
def update_loai(ma_loai: int, model: Loai):
    sql = f'''
    UPDATE loai SET TenLoai = '{model.TenLoai}', Hinh = '{model.Hinh}' 
    WHERE MaLoai = {ma_loai}
'''
    if MySqlUtil.execute(sql):
        return {"success": True}
    return {"success": True}