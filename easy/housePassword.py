# The password will be considered strong enough
# if its length is greater than or equal to 10 symbols,
# it has at least one digit,
# as well as containing one uppercase letter and one lowercase letter in it.
# The password contains only ASCII latin letters or digits.


def password_validator(data):
    if len(data) >= 10:
        digit = None
        lower = None
        upper = None
        for x in data:
            if x.isdigit():
                digit = True
            elif x.islower():
                lower = True
            elif x.isupper():
                upper = True
        if digit and lower and upper is True:
            return True
    return False


print(password_validator('A1213pokl')) # False
print(password_validator('bAse730onE')) # True
print(password_validator('asasasasasasasaas')) # False
print(password_validator('QWERTYqwerty')) # False
print(password_validator('123456123456')) # False
print(password_validator('QwErTy911poqqqq')) # True
