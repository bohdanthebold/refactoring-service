from fastapi import APIRouter
from services.book_service import BookService

router = APIRouter()
book_service = BookService()


@router.post("/add-id")
async def add_id_view(new_id: int = 1):
    updated_data = book_service.add_item_and_get_all(new_id)
    return {"result": updated_data}
