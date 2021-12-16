from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def api_root():
    return {"message": "Welcome to FastAPI"}


@app.get("/hello/{name}")  # host/hello/Admin
def say_hello(name: str):
    return f"Hello {name}"
