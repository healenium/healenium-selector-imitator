from src.selector import Selector, SelectorType


def test_css_selector_to_string():
    assert (
        str(Selector(selector_type=SelectorType.BY_CSS_SELECTOR, tag="h2", id="hello"))
        == "h2#hello"
    )
