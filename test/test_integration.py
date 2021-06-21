from src.node import Node
from src.selector import Selector
from src.selector_imitator import SelectorImitator


def test_integration_css_tag():
    user_selector = Selector.from_css("div[name='old_name']")
    target_node = Node(
        tag="div",
        id="my_div",
        classes=["cls1", "class2"],
        index=1,
        other_attributes={"name": "new_name", "href": "some_link"},
        inner_text="hello world",
    )
    assert (
        str(SelectorImitator(user_selector, target_node).imitate()[0])
        == "div[name='new_name']"
    )
