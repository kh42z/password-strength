import os

from fastapi import FastAPI
from load_rules import load_rules
from validate_password import validate_password
from rules.InvalidPassword import InvalidPassword
from pydantic import BaseModel


class PwdValidation(BaseModel):
    login: str
    password: str


rules = load_rules(os.getenv("REQUIREMENTS_PATH"))
app = FastAPI()


@app.post("/validate")
def validate(pwd: PwdValidation):
    try:
        validate_password(rules, pwd.login, pwd.password)
    except InvalidPassword as e:
        return {"strong": False, "reason": e.message}
    return {"strong": True}
