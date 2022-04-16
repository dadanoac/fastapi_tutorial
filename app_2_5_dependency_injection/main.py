from typing import Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

app = FastAPI()


items = ({"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"})


class PydanticParams(BaseModel):
    q: Optional[str] = Field(None, min_length=2)
    offset: int = Field(0, ge=0)
    limit: int = Field(100, gt=0)


@app.get("/items/pydantic")
async def get_items_with_pydantic(params: PydanticParams = Depends()):
    response = {}
    if params.q:
        response.update({"q": params.q})

    result = items[params.offset: params.offset + params.limit]
    response.update({"items": result})

    return response
