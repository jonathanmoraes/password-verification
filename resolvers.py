import re


def verifyPassword(password, rules):
    new_rules = []
    verify = False
    for rule in rules:
        rule.rule
        rule.value
        match rule.rule:
            case "minSize":
                if minSize(password, rule.value):
                    verify = True
                    new_rules.append(rule)
            case "minUppercase":
                if minUppercase(password, rule.value):
                    verify = True
                    new_rules.append(rule)
            case "minLowercase":
                if minLowercase(password, rule.value):
                    verify = True
                    new_rules.append(rule)
            case "minSpecialChars":
                if minSpecialChars(password, rule.value):
                    verify = True
                    new_rules.append(rule)
            case "noRepeted":
                if noRepeted(password):
                    verify = True
                    new_rules.append(rule)
            case "minDigit":
                if minDigit(password, rule.value):
                    verify = True
                    new_rules.append(rule)
    return verify, new_rules


def minSize(password, value):
    return len(password) < value


def minSpecialChars(password, value):
    especialCaract = list("!@#$%^&*()-+\/{}[]")
    count = 0
    for caracter in especialCaract:
        if password.count(caracter):
            count += 1
    return count < value


def noRepeted(password):
    count = 0
    caracters = list(password)
    for caracter in caracters:
        count += len(re.findall(f"{caracter}{{2}}", password))
    return count > 0


def minDigit(password, value):
    if len(password) > value:
        return False
    return True


def minUppercase(password, value):
    qtt_upper = countLetters(password)
    return qtt_upper > value


def minLowercase(password, value):
    qtt_lower = countLetters(password)
    return qtt_lower > value


def countLetters(password):
    qtt_lower = 0
    qtt_upper = 0

    for cont in range(len(password)):
        if password[cont].islower():
            qtt_lower += 1
        elif password[cont].isupper():
            qtt_upper += 1

    return qtt_lower, qtt_upper
