import datetime

from fastapi import APIRouter

router = APIRouter()


def weekend(weekday):
    if weekday == 5:
        return True
    else:
        if weekday == 6:
            return True
        else:
            return False


@router.get("/is-weekends")
async def is_today_weekend():
    is_weekend = weekend(datetime.datetime.now().weekday())
    # Check if true
    if is_weekend:
        return {"result": True}
    if not is_weekend:
        return {"result": False}


@router.get("/magic-day/")
async def magic_day():
    if datetime.datetime.now().weekday() == 0:
        return {"result": True}
    if datetime.datetime.now().weekday() == 2:
        return {"result": True}
    if datetime.datetime.now().weekday() == 4:
        return {"result": True}
    if datetime.datetime.now().weekday() == 6:
        return {"result": True}
    return {"result": False}
