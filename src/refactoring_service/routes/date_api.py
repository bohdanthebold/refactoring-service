import datetime

from fastapi import APIRouter
from services.date_service import DateService

router = APIRouter()
date_service = DateService()


@router.get("/is-weekends")
async def is_today_weekend():
    result = date_service.is_today_weekend()
    return {"result": result}


@router.get("/magic-day/")
async def magic_day():
    result = date_service.is_today_magic_day()
    return {"result": result}
