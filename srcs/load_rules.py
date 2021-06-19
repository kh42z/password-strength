from rules.MustBeCharset import MustBeCharset
from rules.MustContainCharset import MustContainCharset
from rules.MustNotContainLoginPart import MustNotContainLoginPart
from pyhocon import ConfigFactory


def load_rules(filepath: str):
    rules_set = []
    conf = ConfigFactory.parse_file(filepath)
    for rule in conf["rules"]:
        rules_set.append(dispatch[rule["name"]](rule))
    return rules_set


dispatch = {
    "must_be_charset": MustBeCharset,
    "must_contain_charset": MustContainCharset,
    "must_not_contain_login_part": MustNotContainLoginPart,
}
