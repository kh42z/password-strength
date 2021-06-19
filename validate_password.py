from typing import List

from nm_rules import RuleInterface


def validate_password(rules_set: List[RuleInterface], login: str, pwd: str):
    for rule in rules_set:
        rule.validate(login, pwd)

