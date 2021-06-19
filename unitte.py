import unittest
from load_rules import load_rules
from validate_password import validate_password
from nm_rules import InvalidPassword


class PwdRulesTestCase(unittest.TestCase):
    def test_assert_legit(self):
        rules = load_rules("requirements.txt")
        testcases = [
            {"name": "pwd too short", "login": "herve", "pwd": "hey", "raise": True},
            {"name": "pwd not containing special symbols", "login": "herve", "pwd": "H3y3##", "raise": True},
            {"name": "unwanted char", "login": "herve", "pwd": "L3git/,?@", "raise": True},
            {"name": "contains login", "login": "herve", "pwd": "legit,,,rve", "raise": True},
            {"name": "legit", "login": "herve", "pwd": "hey###123", "raise": False},
            {"name": "legit long", "login": "herve", "pwd": "/,?tOto", "raise": False},
        ]
        for case in testcases:
            if case['raise']:
                with self.assertRaises(InvalidPassword, msg="[{}] got an unexpected exception".format(case["name"])):
                    validate_password(rules, case["login"], case["pwd"])
            else:
                try:
                    validate_password(rules, case["login"], case["pwd"])
                except Exception as err:
                    self.fail("[{}] raised an unexpected exception {}".format(case["name"], err))


if __name__ == '__main__':
    unittest.main()
