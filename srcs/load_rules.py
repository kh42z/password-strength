from nm_rules import MustBeCharset
from nm_rules import MustContainCharset
from nm_rules import MustNotContainLoginPart
from pyhocon import ConfigFactory


def load_rules(filepath: str):
    rules_set = []
    conf = ConfigFactory.parse_file(filepath)
    for r in conf["rules"]:
        rules_set.append(dispatch[r["name"]](r))
    return rules_set


dispatch = {
    "must_be_charset": MustBeCharset,
    "must_contain_charset": MustContainCharset,
    "must_not_contain_login_part": MustNotContainLoginPart,
}
