from fastapi import FastAPI
from  typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name:Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

@app.get("/")
def read_root():
    return  " Hello World Welcome Gokul! :)"

#Created EndPoint with GET Method
@app.get('/about')
def about():
    return {"About":"I'm Gokulapriyan Python Developer"}

#path parameters
inventory = {
    1:{
        "name":"milk",
        "price": 10,
        "brand" :"Hatsun"
    },
    2:{
        "name":"Bag",
        "price": 100,
        "brand" :"Winner Bags"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory[item_id]


# Query Parameters
@app.get("/get-by-name")
def get_item(name: str ):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return "Data Not Found"


# create by using Post method.
@app.post("/create-Item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return "Error Item ID Already exists."

    inventory[item_id] = {"name": item.name,"price":item.price,"brand":item.brand}
    return inventory[item_id]

# Update by using Put method.
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return "Error Item ID doesn't exists."

    inventory[item_id].update(item)
    return inventory[item_id]


    # if item.name != None:
    #     inventory[item_id].name = item.name
    #
    # if item.price != None:
    #     inventory[item_id].price = item.price
    #
    # if item.brand != None:
    #     inventory[item_id].brand = item.brand
    #
    # return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int):
    if item_id not in inventory:
        return "Id does not exist"

    del inventory[item_id]
    return "succesfully deleted!"