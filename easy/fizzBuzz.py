# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;
# The number as a string for other cases.


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


print(fizz_buzz(15)) # "Fizz Buzz", "15 is divisible by 3 and 5"
print(fizz_buzz(6)) # "Fizz", "6 is divisible by 3"
print(fizz_buzz(5)) # "Buzz", "5 is divisible by 5"
print(fizz_buzz(7)) # "7", "7 is not divisible by 3 or 5"
