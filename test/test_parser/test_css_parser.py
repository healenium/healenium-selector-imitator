import pytest

from src.selector_parser import CSSSelectorParser, ParsingError


def test_validation_success_simple():
    CSSSelectorParser("p")


def test_validation_success_complex():
    CSSSelectorParser("div#hello.class_name[href='hello world']")


def test_validation_error():
    with pytest.raises(ParsingError):
        CSSSelectorParser("div#hello_world span.some_class")


def test_parse_tag():
    selector = "div#hello.class_name[href='hello world']"
    assert CSSSelectorParser(selector).get_tag() == "div"
