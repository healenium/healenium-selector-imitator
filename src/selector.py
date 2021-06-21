from dataclasses import dataclass
from enum import Enum
from .selector_parser import CSSSelectorParser
from .selector_to_string import CSSSelectorConstructor
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

    @classmethod
    def from_class_name(cls, class_name: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_CLASS_NAME, classes=[class_name])

    @classmethod
    def from_css(cls, css_selector: str) -> "Selector":
        parser = CSSSelectorParser(css_selector)
        return cls(
            selector_type=SelectorType.BY_CSS_SELECTOR,
            tag=parser.get_tag() or None,
            id=parser.get_id() or None,
            classes=parser.get_classes() or None,
            other_attributes=parser.get_attributes() or None,
        )

    @classmethod
    def from_id(cls, element_id: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_ID, id=element_id)

    @classmethod
    def from_link_text(cls, link_text: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_LINK_TEXT, inner_text=link_text)

    @classmethod
    def from_name(cls, name: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_NAME, other_attributes={"name": name})

    @classmethod
    def from_partial_link_text(cls, partial_link_text: str) -> "Selector":
        return cls(
            selector_type=SelectorType.BY_PARTIAL_LINK_TEXT,
            inner_text=partial_link_text,
        )

    @classmethod
    def from_tag_name(cls, tag_name: str) -> "Selector":
        return cls(selector_type=SelectorType.BY_TAG_NAME, tag=tag_name)

    def __eq__(self, other: "Selector") -> bool:
        return (
            self.selector_type == other.selector_type
            and self.tag == other.tag
            and self.id == other.id
            and set(self.classes or []) == set(other.classes or [])
            and self.index == other.index
            and self.other_attributes == other.other_attributes
            and self.inner_text == other.inner_text
        )

    def __str__(self):
        if self.selector_type == SelectorType.BY_CLASS_NAME:
            if self.classes is None or len(self.classes) == 0:
                raise ValueError(
                    "BY_CLASS_NAME selector must contain one class name, none provided."
                )
            if len(self.classes) == 1:
                return self.classes[0]
            elif len(self.classes) > 1:
                raise ValueError(
                    "Ambiguous BY_CLASS_NAME selector. "
                    "Only one class allowed for this selector type."
                )
        elif self.selector_type == SelectorType.BY_CSS_SELECTOR:
            return CSSSelectorConstructor(
                tag=self.tag,
                element_id=self.id,
                classes=self.classes,
                other_attributes=self.other_attributes,
            ).get_string_representation()
        elif self.selector_type == SelectorType.BY_ID:
            return self.id if self.id is not None else ""
        elif self.selector_type == SelectorType.BY_LINK_TEXT:
            return self.inner_text if self.inner_text is not None else ""
        elif self.selector_type == SelectorType.BY_NAME:
            if self.other_attributes is not None and "name" in self.other_attributes:
                return self.other_attributes["name"]
            else:
                raise ValueError("BY_NAME selector must contain name attribute.")
        elif self.selector_type == SelectorType.BY_PARTIAL_LINK_TEXT:
            return self.inner_text if self.inner_text is not None else ""
        elif self.selector_type == SelectorType.BY_TAG_NAME:
            return self.tag if self.tag is not None else ""
        else:
            return ""
