from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Phone"}, {"item_name": "Tablete"}]


items = {"Iphone", "Macbook", "Desktop", "Thieb"}


@app.get("/items/")
def read_item():
    return fake_items_db
