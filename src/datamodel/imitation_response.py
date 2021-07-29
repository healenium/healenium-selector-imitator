from pydantic import BaseModel, Field
from src.selector import SelectorType


class ImitationResponseModel(BaseModel):
    selector_type: SelectorType = Field(..., alias="selectorType")
    selector_value: str = Field(..., alias="selectorValue")

    class Config:
        allow_population_by_field_name = True
