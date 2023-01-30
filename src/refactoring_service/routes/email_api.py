from fastapi import APIRouter

router = APIRouter()


class SendEmailSendgrid:
    api_key = "api:sendgrid"

    def send(self, message):
        # Some implementation
        print(
            f"Sending email via Sendgrid provider with content: {message}. api key: {self.api_key}"
        )


class SendEmailMailgun(SendEmailSendgrid):
    api_key = "api:mailgun"

    def send(self, message):
        # Some implementation
        print(
            f"Sending email via Mailgun provider with content: {message}. api key: {self.api_key}"
        )


@router.post("/send-email")
async def send_email(provider: str = "mailgun", m: str = "message"):
    message = m
    if provider == "mailgun":
        SendEmailMailgun().send(message=message)
    if provider == "sendgrid":
        SendEmailSendgrid().send(message=message)
    return {"ok": True}
