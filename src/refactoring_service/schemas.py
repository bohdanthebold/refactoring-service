from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    title: str
    is_published: bool


class ItemList(BaseModel):
    response: List[Item]
