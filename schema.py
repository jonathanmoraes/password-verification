import typing
import strawberry
from resolvers import verifyPassword


@strawberry.input
class Rule:
    rule: str
    value: int


@strawberry.input
class PasswordInput:
    password: str
    rules: typing.List["Rule"]


@strawberry.type
class Verify:
    verify: bool
    noMatch: typing.List["str"]


@strawberry.type
class Query:
    @strawberry.field
    def verify(password: str, rules: typing.List["Rule"]) -> Verify:
        verify, new_rules = verifyPassword(password, rules)
        return Verify(verify=verify, noMatch=new_rules)
