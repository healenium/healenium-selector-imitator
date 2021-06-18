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
