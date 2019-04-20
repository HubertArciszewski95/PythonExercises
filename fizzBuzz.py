# Napisz program FizzBuzz
# Wypisz wszystkie liczby od 1 do 100
# Jeśli liczba jest podzielna przez trzy wypisz “Fizz“
# Jeśli liczba jest podzielna przez pięć wypisz “Buzz“
# Jeśli liczba jest podzielna przez trzy i pięć wypisz “FizzBuzz“

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(f"{x}-FizzBuzz")
    elif x % 3 == 0:
        print(f"{x}-Fizz")
    elif x % 5 == 0:
        print(f"{x}-Buzz")
