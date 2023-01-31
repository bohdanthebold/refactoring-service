from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas import ItemList
from services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/is-valid-user")
async def is_valid_user(
    user: str = "Ahmed", age: int = 30, job: str = "data scientist"
):
    result = user_service.is_valid_user(user, age, job)
    return {"result": result}


@router.get("/get-user-id")
async def get_user_id(username: str = "Paul"):
    user_ids = user_service.get_user_ids()
    if username not in user_ids:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return {"user_id": user_ids[username]}


@router.get("/items")
async def items() -> ItemList:
    return {"response": user_service.filter_items(is_published=True)}


@router.get("/key/{key_id}")
async def key(key_id: int = 2):
    result = user_service.get_key_by_id(key_id)
    return {"result": result}


@router.get("/number-in-both-lists/{key_id}")
async def number_in_both_lists(key_id: int = 3):
    # data should be moved to db, but not enough context
    array1 = [1, 2, 3, 4]
    array2 = [3, 4, 5, 6]
    out = set(array1) & set(array2)
    return {"result": key_id in out}
