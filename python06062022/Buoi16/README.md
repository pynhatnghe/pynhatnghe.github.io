# Các bước tạo vietual environment 
## B1: Tạo virtual environment có tên myvenv
```python -m venv myvenv```

## B2: Start virtual environment
```.\myvenv\Scripts\activate```

Nếu chạy được đường dẫn có dạng:
```(myvenv) C:\xyx\abc```

## B3: Nếu muốn stop
```.\myvenv\Scripts\deactivate```

# Cài đặt thư viện FastAPI
```
pip install fastapi
pip install "uvicorn[standard]"
```
hoặc cài gộp:
```pip install fastapi "uvicorn[standard]"```

## Bổ sung thư viện cho upload file
```pip install python-multipart```

Export các thư viện đã trong project:
```pip freeze > requirements.txt```

## Làm sao dựng lại môi trường làm việc
* Tạo virtual environment
* Start virtual environment
* Cài thư viện trong virtual environment đó
    ```pip install -r requirements.txt```