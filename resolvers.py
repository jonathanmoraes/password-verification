import re
from typing import Any, Tuple


def minSize(password: str, value: int) -> bool:
    return len(password) >= value


def minSpecialChars(password: str, value: int) -> bool:
    especialCaract = list("!@#$%^&*()-+\/{}[]")
    counter = 0
    for caracter in especialCaract:
        counter += password.count(caracter)
    return counter >= value


def noRepeted(password: str) -> bool:
    counter = 0
    caracters = list(password)
    for caracter in caracters:
        counter += len(re.findall(f"{caracter}{{2}}", password))
    return counter == 0


def minDigit(password: str, value: int) -> bool:
    return len(password) >= value


def minUppercase(password: str, value: int) -> bool:
    return len(re.findall(r"[A-Z]", password)) >= value


def minLowercase(password: str, value: int) -> bool:
    return len(re.findall(r"[a-z]", password)) >= value


def verifyPassword(password: str, rules: Any) -> Tuple[bool, Any]:
    noMatchRules = []
    verify = False
    for rule in rules:
        kwargs = {"password": password}

        if rule.value:
            kwargs.update({"value": rule.value})

        try:
            verificationFn = rulesVerificationFn[rule.rule]
        except KeyError:
            verify = True
            noMatchRules.append("rule inexistente")
            continue

        if not verificationFn(**kwargs):
            verify = True
            noMatchRules.append(rule.rule)

    return verify, noMatchRules


rulesVerificationFn = {
    "minSize": minSize,
    "minUppercase": minUppercase,
    "minLowercase": minLowercase,
    "minSpecialChars": minSpecialChars,
    "minDigit": minDigit,
    "noRepeted": noRepeted,
}
