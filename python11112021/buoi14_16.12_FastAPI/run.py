# python run.py
# uvicorn main:app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8888)