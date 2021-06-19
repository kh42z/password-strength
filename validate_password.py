from typing import List

from nm_rules import RuleInterface


def validate_password(rules: List[RuleInterface], login: str, pwd: str):
    for rule in rules:
        rule.validate(login, pwd)

