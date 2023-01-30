from fastapi import APIRouter

router = APIRouter()


def transform_text(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()


@router.post("/capitalize-string")
async def capitalize_string(s: str = "some text", is_uppercase: bool = True):
    return {"result": transform_text(s, is_uppercase)}


@router.post("/capitalize-list")
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
