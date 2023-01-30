import datetime

from math import ceil, floor
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()


class DB:
    # Fake db
    def get_user_items(self):
        return [
            {"title": "1 item", "is_published": True},
            {"title": "2 item", "is_published": False},
            {"title": "3 item", "is_published": False},
            {"title": "4 item", "is_published": True},
        ]


db = DB()


class Item(BaseModel):
    title: str


class ItemList(BaseModel):
    response: List[Item]


@app.get("/get-service-name")
async def service():
    file = open("service.txt", "r")
    line = file.read()
    return {"result": line}


@app.get("/magic-day/")
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


def weekend(weekday):
    if weekday == 5:
        return True
    else:
        if weekday == 6:
            return True
        else:
            return False


@app.get("/is-weekends")
async def is_today_weekend():

    is_weekend = weekend(datetime.datetime.now().weekday())
    # Check if true
    if is_weekend:
        return {"result": True}
    if not is_weekend:
        return {"result": False}


@app.get("/is-valid-user")
async def is_valid_user(
    user: str = "Ahmed", age: int = 30, job: str = "data scientist"
):
    if age >= 30:
        if user == "Ahmed":
            if job == "data scientist":
                return {"result": True}
            else:
                return {"result": False}
    return {"result": False}


def transform_text(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()


@app.post("/capitalize-string")
async def capitalize_string(s: str = "some text", is_uppercase: bool = True):
    return {"result": transform_text(s, is_uppercase)}


@app.post("/capitalize-list")
async def capitalize_list(s: str = "first,second,third"):
    input_list = s.split(",")
    print(input_list)
    # iterate over list
    i = 0
    while True:
        input_list[i] = input_list[i].upper()
        if i >= len(input_list) - 1:
            break
        i = i + 1
    return {"result": input_list}


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


@app.post("/send-email")
async def send_email(provider: str = "mailgun", m: str = "message"):
    message = m
    if provider == "mailgun":
        SendEmailMailgun().send(message=message)
    if provider == "sendgrid":
        SendEmailSendgrid().send(message=message)
    return {"ok": True}


@app.get("/get-user-id")
async def exc(username: str = "Paul"):
    user_ids = {"John": 12, "Anna": 2, "Jack": 10}

    try:
        return {"user_id": user_ids[username]}
    except:
        pass
    return {"message": "User not found"}


def filter_items(is_published, items_list):
    if is_published:
        return list(filter(lambda x: x["is_published"], items_list))
    else:
        return list(filter(lambda x: not x["is_published"], items_list))


@app.get("/items")
async def items():
    return {"response": filter_items(True, db.get_user_items())}


@app.get("/key/{key_id}")
async def key(key_id: int = 2):
    array = ["key1", "key2", "key3", "key4"]
    for item_id in range(len(array)):
        if item_id + 1 == key_id:
            return {"result": array[item_id]}


@app.get("/number-in-both-lists/{key_id}")
async def number_in_both_lists(key_id: int = 3):
    array1 = [1, 2, 3, 4]
    array2 = [3, 4, 5, 6]
    for item1 in array1:
        for item2 in array2:
            if item1 == key_id and item2 == key_id:
                return {"result": True}
    return {"result": False}


def add_id(book_id, storage=[]):
    storage.append(book_id)
    return storage


@app.post("/add-id")
async def add_id_view(new_id: int = 1):
    return {"result": add_id(new_id)}


@app.get("/round")
async def round_number(number: float = 1.5, to_ceil: bool = True):
    if to_ceil:
        result_value = ceil(number)
    else:
        result_value = floor(number)
    return {"result": result_value}


@app.post("/multiply")
async def multiply(first_number: str = "3", second_number: str = "4"):
    # NOTE: Try inserting this string "exec('import os; result = os.system("touch hack.txt")')#" as a first_number 😉
    result_value = float(first_number) * float(second_number)
    return {"result": result_value}
