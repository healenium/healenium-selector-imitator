from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict


class SelectorType(Enum):
    BY_CLASS_NAME = 1
    BY_CSS_SELECTOR = 2
    BY_ID = 3
    BY_LINK_TEXT = 4
    BY_NAME = 5
    BY_PARTIAL_LINK_TEXT = 6
    BY_TAG_NAME = 7
    BY_XPATH = 8


@dataclass
class Selector:
    selector_type: SelectorType
    tag: Optional[str] = None
    id: Optional[str] = None
    classes: Optional[List[str]] = None
    index: Optional[int] = None
    other_attributes: Optional[Dict[str, str]] = None
    inner_text: Optional[str] = None
