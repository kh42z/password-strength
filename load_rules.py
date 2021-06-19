from nm_rules import MustBeCharset
from nm_rules import RuleInterface
from nm_rules import MustContainCharset
from nm_rules import MustNotContainLoginPart
from pyhocon import ConfigFactory

from typing import List


def load_rules(filepath: str) -> List[RuleInterface]:
    rules_set = []
    try:
        conf = ConfigFactory.parse_file(filepath)
    except OSError:
        return rules_set
    for r in conf["rules"]:
        try:
            rules_set.append(dispatch[r["name"]](r))
        except KeyError as err:
            print("KeyError: {}".format(err))
    return rules_set


dispatch = {
    "must_be_charset": MustBeCharset,
    "must_contain_charset": MustContainCharset,
    "must_not_contain_login_part": MustNotContainLoginPart,
}
