from fastapi import APIRouter

router = APIRouter()


def add_id(book_id, storage=[]):
    storage.append(book_id)
    return storage


@router.post("/add-id")
async def add_id_view(new_id: int = 1):
    return {"result": add_id(new_id)}
