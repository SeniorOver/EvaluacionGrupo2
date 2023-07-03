from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


#@app.get("/")
#def read_root():
#    return {"Hello1iii": "World1iii"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9069)