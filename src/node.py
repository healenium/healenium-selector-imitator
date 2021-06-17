from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class Node:
    tag: str
    id: str
    classes: List[str]
    index: int
    other_attributes: Dict[str, str]
    inner_text: str
    parent: Optional["Node"]
    children: Optional[List["Node"]]
