from fastapi import APIRouter
from services.string_service import StringService

router = APIRouter()
string_service = StringService()


@router.post("/capitalize-string")
async def capitalize_string(s: str = "some text", is_uppercase: bool = True):
    result_string = string_service.transform_string(text=s, to_uppercase=is_uppercase)
    return {"result": result_string}


@router.post("/capitalize-list")
async def capitalize_list(s: str = "first,second,third"):
    capitalized_list = string_service.convert_to_list_and_capitalize(
        input_list_string=s
    )
    return {"result": capitalized_list}
