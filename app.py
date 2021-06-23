import os
import uvicorn

from fastapi import FastAPI
from src.datamodel import ImitationRequestModel, ImitationResponseModel
from src.selector import Selector
from src.selector_imitator import SelectorImitator
from typing import List


app = FastAPI()


@app.get("/")
def main():
    return "this is an entry point of the selector imitator"


@app.post("/imitate", response_model=List[ImitationResponseModel])
def imitate(request: ImitationRequestModel):
    user_selector = Selector.from_type_and_value(
        selector_type=request.user_selector.type, value=request.user_selector.value
    )
    imitator = SelectorImitator(user_selector, request.target_node)
    result = [
        ImitationResponseModel(
            selector_type=selector.selector_type, selector_value=str(selector)
        )
        for selector in imitator.imitate()
    ]
    return result


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
