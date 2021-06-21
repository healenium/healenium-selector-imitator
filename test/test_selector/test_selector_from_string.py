from src.selector import Selector, SelectorType


def test_from_css_simple():
    css_selector = "div"
    assert Selector.from_css(css_selector) == Selector(
        selector_type=SelectorType.BY_CSS_SELECTOR, tag="div"
    )


def test_from_css_complex():
    css_selector = "div#hello.class_name.cls2[href='hello world']"
    assert Selector.from_css(css_selector) == Selector(
        selector_type=SelectorType.BY_CSS_SELECTOR,
        tag="div",
        id="hello",
        classes=["class_name", "cls2"],
        other_attributes={"href": "hello world"},
    )
