from datetime import date

user_age = int(input("Type your age: "))
actual_year = int(date.today().strftime("%Y"))
year_of_birth = actual_year - user_age

print(f"We think you were born back in {year_of_birth}")
