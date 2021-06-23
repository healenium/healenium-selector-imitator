from pydantic import BaseModel
from src.selector import SelectorType


class ImitationResponseModel(BaseModel):
    selector_type: SelectorType
    selector_value: str
