from pydantic import BaseModel
from src.node import Node
from src.selector import SelectorType


class UserSelector(BaseModel):
    type: SelectorType
    value: str


class ImitationRequestModel(BaseModel):
    user_selector: UserSelector
    target_node: Node
