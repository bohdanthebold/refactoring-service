from typing import List

from fastapi import APIRouter
from pydantic import BaseModel


class DB:
    # Fake db
    def get_user_items(self):
        return [
            {"title": "1 item", "is_published": True},
            {"title": "2 item", "is_published": False},
            {"title": "3 item", "is_published": False},
            {"title": "4 item", "is_published": True},
        ]


db = DB()


class Item(BaseModel):
    title: str


class ItemList(BaseModel):
    response: List[Item]


router = APIRouter()


@router.get("/is-valid-user")
async def is_valid_user(
    user: str = "Ahmed", age: int = 30, job: str = "data scientist"
):
    if age >= 30:
        if user == "Ahmed":
            if job == "data scientist":
                return {"result": True}
            else:
                return {"result": False}
    return {"result": False}


@router.get("/get-user-id")
async def exc(username: str = "Paul"):
    user_ids = {"John": 12, "Anna": 2, "Jack": 10}

    try:
        return {"user_id": user_ids[username]}
    except:
        pass
    return {"message": "User not found"}


def filter_items(is_published, items_list):
    if is_published:
        return list(filter(lambda x: x["is_published"], items_list))
    else:
        return list(filter(lambda x: not x["is_published"], items_list))


@router.get("/items")
async def items():
    return {"response": filter_items(True, db.get_user_items())}


@router.get("/key/{key_id}")
async def key(key_id: int = 2):
    array = ["key1", "key2", "key3", "key4"]
    for item_id in range(len(array)):
        if item_id + 1 == key_id:
            return {"result": array[item_id]}


@router.get("/number-in-both-lists/{key_id}")
async def number_in_both_lists(key_id: int = 3):
    array1 = [1, 2, 3, 4]
    array2 = [3, 4, 5, 6]
    for item1 in array1:
        for item2 in array2:
            if item1 == key_id and item2 == key_id:
                return {"result": True}
    return {"result": False}
