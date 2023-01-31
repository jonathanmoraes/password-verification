import pytest
import resolvers
from schema import Rule

PASSWORD = "TesteSenhaForte!12103&"

@pytest.mark.parametrize("password, rule, result_verify, result_rules",[
    ("teste",[Rule(rule= "minSize",value= 12)],True,["minSize"]), 
    ("testee",[Rule(rule= "minSpecialChars",value= 2)],True,["minSpecialChars"]), 
    ("t@@tes",[Rule(rule= "noRepeted",value= 0)],True,["noRepeted"]),
    ("teste",[Rule(rule= "minUppercase",value= 1)],True,["minUppercase"]), 
    ("testee",[Rule(rule= "minDigit",value= 7)],True,["minDigit"]), 
    ("t@@tes",[Rule(rule= "minLowercase",value= 9)],True,["minLowercase"])
])
def test_verify_password(password, rule, result_verify, result_rules):
   verify,new_rules = resolvers.verifyPassword(password=password, rules = rule)
   assert verify == result_verify
   assert new_rules == result_rules


def test_minSize(password=PASSWORD):
   assert resolvers.minSize(password, 3)


def test_noRepeted(password=PASSWORD):
   assert resolvers.noRepeted(password)


def test_minSpecialChars(password=PASSWORD):
   assert resolvers.minSpecialChars(password, 1)


def test_minUppercase(password=PASSWORD):
   assert resolvers.minUppercase(password, 3)


def test_minDigit(password=PASSWORD):
   assert resolvers.minDigit(password, 3)


def test_minLowercase(password=PASSWORD):
   assert resolvers.minLowercase(password, 3)