from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


"""
http://127.0.0.1:8000/docs

"""