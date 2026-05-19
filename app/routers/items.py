from fastapi import APIRouter, HTTPException
from app.schemas import ItemCreate, ItemResponse
from typing import List

router = APIRouter()

_items: dict[int, ItemResponse] = {}
_counter = 0


@router.get("/items", response_model=List[ItemResponse], tags=["items"])
async def list_items():
    return list(_items.values())


@router.post("/items", response_model=ItemResponse, status_code=201, tags=["items"])
async def create_item(item: ItemCreate):
    global _counter
    _counter += 1
    new_item = ItemResponse(id=_counter, **item.model_dump())
    _items[_counter] = new_item
    return new_item


@router.get("/items/{item_id}", response_model=ItemResponse, tags=["items"])
async def get_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    return _items[item_id]


@router.delete("/items/{item_id}", status_code=204, tags=["items"])
async def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
