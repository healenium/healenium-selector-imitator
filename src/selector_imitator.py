from node import Node
from selector import Selector, SelectorType
from typing import List


class ImitationError(Exception):
    pass


class SelectorImitator:
    def __init__(self, user_selector: Selector, target_node: Node):
        self.user_selector = user_selector
        self.target_node = target_node

    def imitate_css_or_xpath(self) -> Selector:
        target_selector = Selector(selector_type=self.user_selector.selector_type)
        if self.user_selector.tag is not None:
            if self.target_node.tag:
                target_selector.tag = self.target_node.tag
            else:
                raise ImitationError("Target node does not have any tag")
        if self.user_selector.id is not None:
            if self.target_node.id:
                target_selector.id = self.target_node.id
            else:
                raise ImitationError("Target node does not have any id")
        if self.user_selector.classes is not None:
            if self.target_node.classes:
                target_selector.classes = self.target_node.classes
            else:
                raise ImitationError("Target node does not belong to any classes")
        if self.user_selector.index is not None:
            if self.target_node.index:
                target_selector.index = self.target_node.index
            else:
                raise ImitationError("Target node does not have any index")
        if self.user_selector.inner_text is not None:
            if self.target_node.inner_text:
                target_selector.inner_text = self.target_node.inner_text
            else:
                raise ImitationError("Target node does not have any inner text")
        if self.user_selector.other_attributes is not None:
            target_selector.other_attributes = {}
            for attribute in self.user_selector.other_attributes:
                if attribute in self.target_node.other_attributes:
                    target_selector.other_attributes[
                        attribute
                    ] = self.target_node.other_attributes[attribute]
                else:
                    raise ImitationError(
                        f"Target node does not have an attribute {attribute}"
                    )
        return target_selector

    def imitate(self) -> List[Selector]:
        """Return a list of possible selectors for a target node that imitates a user selector.
        Raise ImitationError if the target node cannot be imitated.
        """
        if self.user_selector.selector_type == SelectorType.BY_CLASS_NAME:
            if self.target_node.classes:
                return [
                    Selector(
                        selector_type=SelectorType.BY_CLASS_NAME,
                        classes=[target_class],
                    )
                    for target_class in self.target_node.classes
                ]
            else:
                raise ImitationError("Target node does not belong to any class.")
        elif self.user_selector.selector_type in [
            SelectorType.BY_CSS_SELECTOR,
            SelectorType.BY_XPATH,
        ]:
            return [self.imitate_css_or_xpath()]
