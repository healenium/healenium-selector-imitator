import re


class ParsingError(Exception):
    pass


class CSSSelectorParser:
    def __init__(self, selector: str):
        self.selector = selector
        self.validate()

    def validate(self):
        expression = re.compile(r"^(\w+)(\.\w+|#\w+|\[.+\])*$")
        if expression.match(self.selector) is None:
            raise ParsingError("Cannot parse CSS selector")

    def get_tag(self) -> str:
        expression = re.compile(r"^\w+")
        search_result = expression.search(self.selector)
        if search_result is None:
            raise ParsingError(f"Cannot extract tag from {self.selector}")
        else:
            return search_result.group()
