import re

from .RuleInterface import RuleInterface
from .InvalidPassword import InvalidPassword


class MustNotContainLoginPart(RuleInterface):
    def __init__(self, conf):
        self.part_length = conf['part_length']

    def validate(self, login: str, pwd: str):
        if len(login) < self.part_length:
            return
        for i in range(len(login) + 1 - self.part_length):
            substr = login[i:i+self.part_length]
            if re.search(substr, pwd, re.IGNORECASE):
                raise InvalidPassword("must_not_contain_login_part")
