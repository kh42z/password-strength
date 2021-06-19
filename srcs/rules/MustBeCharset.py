from .RuleInterface import RuleInterface
from .InvalidPassword import InvalidPassword
import re


class MustBeCharset(RuleInterface):
    def __init__(self, conf):
        super().__init__(conf)
        self.regexp = re.compile(conf['charset'])
        self.min_length = conf['min_length']

    def validate(self, login: str, pwd: str):
        if len(pwd) < self.min_length:
            raise InvalidPassword("must_contain_charset")
        for l in pwd:
            if not self.regexp.match(l):
                raise InvalidPassword("must_contain_charset")


