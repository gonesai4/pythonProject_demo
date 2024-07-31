from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return {"Hello": "World"}

@app.get("/home")
def welcome():
    return {"Message": "Welcome Home"}


@app.post("/data")
def demo(data):
    return {"Message": data}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}


