from fastapi import APIRouter
from services.math_service import MathService

router = APIRouter()
math_service = MathService()


@router.get("/round")
async def round_number(number: float = 1.5, to_ceil: bool = True):
    result_value = math_service.round(number, to_ceil)
    return {"result": result_value}


@router.post("/multiply")
async def multiply(first_number: str = "3", second_number: str = "4"):
    # NOTE: Try inserting this string "exec('import os; result = os.system("touch hack.txt")')#" as a first_number 😉
    first_number_float = float(first_number)
    second_number_float = float(second_number)
    result_value = math_service.multiply(first_number_float, second_number_float)
    return {"result": result_value}
