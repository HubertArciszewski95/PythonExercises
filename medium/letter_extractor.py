# Write a script that iterates throught each of the 26 text files,
# checks is the letter inside the text file is in string "python"
# and puts the letter in a list if the letter is a character of "python"
import string

counter = 0
letters = string.ascii_lowercase
extracted_letters = []

while counter < len(letters):
    with open(f"/Users/hubertarciszewski/Downloads/letters/{letters[counter]}.txt", "r") as data:

        read_data = data.read().split()
        to_string = " ".join(read_data)

        if to_string in "python":
            extracted_letters.append(to_string)
        counter += 1

print(extracted_letters)
