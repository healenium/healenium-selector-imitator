from src.node import Node
from src.selector import Selector, SelectorType
from src.selector_imitator import SelectorImitator


def test_imitate_by_class_name():
    user_selector = Selector(
        selector_type=SelectorType.BY_CLASS_NAME, classes=["class1"]
    )
    target_node = Node(classes=["class2"])
    expected_result = Selector(
        selector_type=SelectorType.BY_CLASS_NAME, classes=["class2"]
    )
    imitated_selectors = SelectorImitator(user_selector, target_node).imitate()
    assert len(imitated_selectors) == 1
    assert imitated_selectors[0] == expected_result
