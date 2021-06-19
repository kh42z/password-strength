import unittest
import pwd_rules


class PwdRulesTestCase(unittest.TestCase):
    def test_assert_legit(self):
        testcases = [
            {"name": "pwd too short", "login": "herve", "pwd": "hey", "result": False},
            {"name": "pwd not containing special symbols", "login": "herve", "pwd": "H3y3##", "result": False},
            {"name": "unwanted char", "login": "herve", "pwd": "L3git/,?@", "result": False},
            {"name": "contains login", "login": "herve", "pwd": "legit,,,rve", "result": False},
            {"name": "legit", "login": "herve", "pwd": "hey###123", "result": True},
            {"name": "legit long", "login": "herve", "pwd": "/,?tOto", "result": True},
        ]
        for case in testcases:
            self.assertEqual(pwd_rules.assert_legit(case["login"], case["pwd"]), case["result"],
                             "[{}] expect {} got {}".format(case["name"], case["result"], case["result"] == False))


if __name__ == '__main__':
    unittest.main()
