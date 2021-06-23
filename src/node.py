from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class Node:
    tag: str = ""
    id: str = ""
    classes: List[str] = field(default_factory=list)
    index: Optional[int] = None
    other_attributes: Dict[str, str] = field(default_factory=dict)
    inner_text: str = ""
