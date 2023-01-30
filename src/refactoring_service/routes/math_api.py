from math import floor, ceil

from fastapi import APIRouter

router = APIRouter()


@router.get("/round")
async def round_number(number: float = 1.5, to_ceil: bool = True):
    if to_ceil:
        result_value = ceil(number)
    else:
        result_value = floor(number)
    return {"result": result_value}


@router.post("/multiply")
async def multiply(first_number: str = "3", second_number: str = "4"):
    # NOTE: Try inserting this string "exec('import os; result = os.system("touch hack.txt")')#" as a first_number 😉
    result_value = float(first_number) * float(second_number)
    return {"result": result_value}
