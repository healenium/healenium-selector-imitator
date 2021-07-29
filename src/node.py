from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class Node(BaseModel):
    tag: str = ""
    id: str = ""
    classes: List[str] = Field(default_factory=list)
    index: Optional[int] = None
    other_attributes: Dict[str, str] = Field(
        default_factory=dict, alias="otherAttributes"
    )
    inner_text: str = Field("", alias="innerText")

    class Config:
        ignore_extra = False
        allow_population_by_field_name = True
