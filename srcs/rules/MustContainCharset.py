from .RuleInterface import RuleInterface
from .InvalidPassword import InvalidPassword
import re


class MustContainCharset(RuleInterface):
    def __init__(self, conf):
        self.regexp = re.compile(conf['charset'])
        self.min_length = conf['min_length']

    def validate(self, login: str, pwd: str):
        if len(self.regexp.findall(pwd)) < self.min_length:
            raise InvalidPassword("must_contain_charset")