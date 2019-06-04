# Create a program that asks the user to input values separated by commas
# and stores those values in a text file, each value in a separate line.

user_input = input("Enter values: ").split(",")

with open("user_data.txt", "a") as file:
    for x in user_input:
        file.write(x + "\n")
