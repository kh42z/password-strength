class RuleInterface:
    def __init__(self, conf):
        pass

    def validate(self, login: str, pwd: str):
        pass


class InvalidPassword(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class MustBeCharset(RuleInterface):
    def __init__(self, conf):
        charset = conf['charset']
        min_length = conf['min_length']

    def validate(self, login: str, pwd: str):
        raise InvalidPassword("must_be_charset")


class MustContainCharset(RuleInterface):
    def __init__(self, conf):
        charset = conf['charset']
        min_length = conf['min_length']

    def validate(self, login: str, pwd: str):
        raise InvalidPassword("must_contain_charset")


class MustNotContainLoginPart(RuleInterface):
    def __init__(self, conf):
        part_length = conf['part_length']

    def validate(self, login: str, pwd: str):
        raise InvalidPassword("must_not_contain_login_part")
