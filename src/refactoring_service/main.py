from fastapi import FastAPI
from routes import users_api, string_api, books_api, email_api, date_api, math_api

app = FastAPI()


@app.get("/get-service-name")
async def service():
    file = open("service.txt", "r")
    line = file.read()
    return {"result": line}

app.include_router(books_api.router)
app.include_router(date_api.router)
app.include_router(email_api.router)
app.include_router(math_api.router)
app.include_router(string_api.router)
app.include_router(users_api.router)
