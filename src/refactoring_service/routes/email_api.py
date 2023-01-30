from fastapi import APIRouter
from services.email_service import EmailService

router = APIRouter()

email_service = EmailService()


@router.post("/send-email")
async def send_email(provider: str = "mailgun", m: str = "message"):
    result = email_service.send_email(provider, message=m)
    return {"ok": result}
