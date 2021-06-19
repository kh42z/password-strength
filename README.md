## Intro

Write a microservice to validate password strength


## Python module

write a pure python method for validating a password strength against rules:

1. must be composed by a set of characters, with at least n chars (char set as parameter, n as parameter)
2. must contain a set of charset, with at least n chars
2. must not contain a part of the login (length of part as parameter, case insensitive)


Example of rules:

```
rules = [
    {"name": "must_be_charset", "charset": "[a-zA-Z0-9]", "min_length": 10},
    {"name": "must_contain_charset", "charset": "[/.;,?*$!#]", "min_length": 3},
    {"name": "must_not_contain_login_part", "part_length": 5}
]
```

* the charset is using the regular expression syntax
* all rules should validate
* write unit tests


## Flask or FastAPI micro service

build a micro service for password strength validation:

* path: `/validate`
* input: POST body application/json: `{"password": "VALUE"}`
* output: application/json: `{"strong": "true/false", "reason": "<name of invalid rule>"}`

1. use a requirements.txt so we can test your service
2. write a Dockerfile
3. write a docker-compose.yaml
4. write yaml for deploying the micro service to kubernetes

## Questions

* How would you secure this service ?
* How could we improve the validation rules so that it will reduce the risks for the user ?
* What could be done to allow a salesperson to edit the differents rules ?


