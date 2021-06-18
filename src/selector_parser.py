import re

from typing import List


class ParsingError(Exception):
    pass


class CSSSelectorParser:
    def __init__(self, selector: str):
        self.selector = selector
        self.validate()

    def validate(self):
        expression = re.compile(r"^(\w+)(\.\w+|#\w+|\[.+])*$")
        if expression.match(self.selector) is None:
            raise ParsingError("Cannot parse CSS selector")

    def remove_quoted_text(self, text: str) -> str:
        result = text
        single_quote_expression = re.compile("'.*'")
        double_quote_expression = re.compile('".*"')
        for expression in [single_quote_expression, double_quote_expression]:
            while expression.search(result) is not None:
                idx_from, idx_to = expression.search(result).span()
                result = result[:idx_from] + result[idx_to:]
        return result

    def get_tag(self) -> str:
        expression = re.compile(r"^\w+")
        search_result = expression.search(self.selector)
        if search_result is None:
            raise ParsingError(f"Cannot extract tag from {self.selector}")
        else:
            return search_result.group()

    def get_id(self) -> str:
        expression = re.compile(r"#(\w+)")
        search_result = expression.search(self.remove_quoted_text(self.selector))
        if search_result is None:
            return ""
        else:
            return search_result.group(1)

    def get_classes(self) -> List[str]:
        expression = re.compile(r"\.(\w+)")
        return expression.findall(self.remove_quoted_text(self.selector))
