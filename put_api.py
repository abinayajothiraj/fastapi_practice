from fastapi import FastAPI
from pydantic import BaseModel

# create FastAPI app
app = FastAPI()

#create pydantic model (request model)
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

# PUT API(update item)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return{
        "item_id": item_id,
        "name": item.name,
        "price": item.price,
        "is_offer": item.is_offer
    }
