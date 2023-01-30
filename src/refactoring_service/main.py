from fastapi import FastAPI
from routes import users_api, string_api, books_api, email_api, date_api, math_api

app = FastAPI()

SERVICE_FILENAME = "service.txt"

@app.get("/get-service-name")
async def service():
    with open(SERVICE_FILENAME, "r") as file:
        file_content = file.read()
        return {"result": file_content}


app.include_router(books_api.router)
app.include_router(date_api.router)
app.include_router(email_api.router)
app.include_router(math_api.router)
app.include_router(string_api.router)
app.include_router(users_api.router)
