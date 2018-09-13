def checkio(password):
    return len(password) >= 10 and (any(x.isupper() for x in password)) and (any(y.islower() for y in password)) and \
           (any(z.isdigit() for z in password))


def tests():
    print(checkio('A1213pokl'))
    print(checkio('bAse730onE'))
    print(checkio('asasasasasasasaas'))
    print(checkio('QWERTYqwerty'))
    print(checkio('123456123456'))
    print(checkio('QwErTy911poqqqq'))

tests()