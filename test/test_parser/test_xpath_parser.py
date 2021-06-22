import pytest

from src.selector_parser import XPathParser, ParsingError


def test_validation_success_simple():
    XPathParser("//p")


def test_validation_success_complex():
    XPathParser("//label[@id='message23']")


def test_validation_success_no_tag():
    XPathParser("//*[@class='cls1'][1]")


def test_validation_error():
    with pytest.raises(ParsingError):
        XPathParser("//*[@type='text']//following::input")


def test_parse_tag():
    assert XPathParser("//label[@id='message23']").get_tag() == "label"


def test_parse_tag_simple():
    assert XPathParser("//h2").get_tag() == "h2"


def test_parse_no_tag():
    assert XPathParser("//*[@class='cls1'][1]").get_tag() == ""


def test_parse_id():
    assert XPathParser("//*[@id='rt-feature']").get_id() == "rt-feature"


def test_parse_no_id():
    assert XPathParser("//*[@class='cls1'][1]").get_id() == ""


def test_parse_classes_single_class():
    assert XPathParser("//*[@class='cls1'][1]").get_classes() == ["cls1"]


def test_parse_classes_multiple_classes():
    assert XPathParser("//*[@class='cls1 cls2'][1]").get_classes() == ["cls1", "cls2"]


def test_parse_classes_single_class_with_contains():
    assert XPathParser("//*[contains(@class,'btn')]").get_classes() == ["btn"]


def test_parse_classes_no_class():
    assert XPathParser("//label[@id='message23']").get_classes() == []
