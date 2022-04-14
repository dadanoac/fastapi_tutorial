from typing import List

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()
    
inventory = []

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, title="이름")
    price: float = Field(None, ge=0)
    amount: int = Field(
        default=1,
        gt=0,
        le=100,
        title="수량",
        description="아이템 갯수. 1~100 개 까지 소지 가능",
    )

@app.get("/users/{user_id}/inventory", response_model=List[Item])
def get_item(
    user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),
    name: str = Query(None, min_length=1, max_length=2, title="아이템 이름"),
):
    user_items = []
    for item in inventory:
        if item["user_id"] == user_id:
            user_items.append(item)

    response = []
    for item in user_items:
        if name is None:
            response = user_items
            break
        if item["name"] == name:
            response.append(item)

    return response

@app.post("/users/{user_id}/item")
def create_item(item: Item):
    inventory.append(item)
    return item

if __name__ == "__main__":
    uvicorn.run(app = "main:app")