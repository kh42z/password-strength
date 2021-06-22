import unittest
from load_rules import load_rules
from validate_password import validate_password
from rules.InvalidPassword import InvalidPassword


class PwdRulesTestCase(unittest.TestCase):
    def test_validate_password(self):
        rules = load_rules("../requirements.txt")
        testcases = [
            {"name": "pwd too short", "login": "herve", "pwd": "###", "raise": True},
            {"name": "pwd not containing special symbols", "login": "herve", "pwd": "H3y3##", "raise": True},
            {"name": "unwanted char", "login": "herve", "pwd": "L3git/,?@", "raise": True},
            {"name": "contains login", "login": "herve", "pwd": "legit,,,herv", "raise": True},
            {"name": "login part_length equals login len", "login": "rve", "pwd": "rve#232,,,", "raise": True},
            {"name": "legit", "login": "herve", "pwd": "hey###123", "raise": False},
            {"name": "legit long", "login": "herve", "pwd": "/,?tOto", "raise": False},
        ]
        for case in testcases:
            if case['raise']:
                with self.assertRaises(InvalidPassword, msg="[{}] should raise exception".format(case["name"])):
                    validate_password(rules, case["login"], case["pwd"])
            else:
                try:
                    validate_password(rules, case["login"], case["pwd"])
                except Exception as err:
                    self.fail("[{}] raised an unexpected exception {}".format(case["name"], err))

    def test_validate_password_simplecase(self):
        rules = load_rules("./tests/simple.txt")
        testcases = [
            {"name": "pwd too short", "login": "george", "pwd": "0123", "raise": True},
            {"name": "pwd min length", "login": "george", "pwd": "01299", "raise": False},
            {"name": "pwd one special symbol", "login": "george", "pwd": "01288", "raise": True},
            {"name": "pwd not containing special symbols", "login": "george", "pwd": "234567", "raise": True},
            {"name": "pwd containing special symbols", "login": "george", "pwd": "0345699", "raise": False},
            {"name": "unwanted char", "login": "herve", "pwd": "A01234599", "raise": True},
            {"name": "contains login", "login": "01234", "pwd": "0123499", "raise": True},
            {"name": "login part_length equals login len", "login": "123", "pwd": "123099", "raise": True},
            {"name": "legit", "login": "990", "pwd": "909124", "raise": False},
            {"name": "legit long", "login": "herve", "pwd": "9900211", "raise": False},
        ]
        for case in testcases:
            if case['raise']:
                with self.assertRaises(InvalidPassword, msg="[{}] should raise exception".format(case["name"])):
                    validate_password(rules, case["login"], case["pwd"])
            else:
                try:
                    validate_password(rules, case["login"], case["pwd"])
                except Exception as err:
                    self.fail("[{}] raised an unexpected exception {}".format(case["name"], err))


if __name__ == '__main__':
    unittest.main()
