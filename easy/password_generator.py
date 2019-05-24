# generate password with 6 random char a-zA-Z0-9 and special chars

import string
import random

letters = string.ascii_letters
nums = string.digits
special_char = string.punctuation

all_char = letters + nums + special_char


password_list = []
for x in range(0, 6):
    rand = random.choice(all_char)
    password_list.append(rand)
password = "".join(password_list)

print(password)
