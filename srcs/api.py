from fastapi import FastAPI
from load_rules import load_rules
from validate_password import validate_password
from nm_rules import InvalidPassword
from pydantic import BaseModel


class PwdValidation(BaseModel):
    login: str
    password: str


rules = load_rules("requirements.txt")
app = FastAPI()


@app.post("/validate")
def validate(pwd: PwdValidation):
    try:
        validate_password(rules, pwd.login, pwd.password)
        return {"strong": True}
    except InvalidPassword as e:
        return {"strong": False, "reason": e.message}
