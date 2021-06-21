from typing import List, Dict, Optional


class CSSSelectorConstructor:
    def __init__(
        self,
        tag: Optional[str] = None,
        element_id: Optional[str] = None,
        classes: Optional[List[str]] = None,
        other_attributes: Optional[Dict[str, str]] = None,
    ):
        self.tag = tag
        self.element_id = element_id
        if classes is not None:
            self.classes = classes
        else:
            self.classes = []
        if other_attributes is not None:
            self.other_attributes = other_attributes
        else:
            self.other_attributes = {}

    def get_string_representation(self):
        result = ""
        if self.tag is not None:
            result += self.tag
        if self.element_id is not None:
            result += f"#{self.element_id}"
        for class_name in self.classes:
            result += f".{class_name}"
        for attr_name, attr_value in self.other_attributes.items():
            result += f"[{attr_name}='{attr_value}']"
        return result
