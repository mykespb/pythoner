# myke's tests of FastAPI
# tes01.py 2022-06-14 2022-06-14 1.2
# simple test to starty with, gets current date&time 

from fastapi import FastAPI
from datetime import datetime as dt
import uuid

app = FastAPI()

counter = 0

@app.get("/")
def hello():
    global counter
    counter += 1
    return {"hello": "world", "time": dt.now(), "counter": counter, "uuid": uuid.uuid4().hex}

# {"hello":"world","time":"2022-06-14T11:42:27.779196"}
