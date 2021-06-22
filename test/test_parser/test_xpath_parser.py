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


def test_parse_no_tag():
    assert XPathParser("//*[@class='cls1'][1]").get_tag() == ""
