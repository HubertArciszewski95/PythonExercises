import string

counter = 0
letters = string.ascii_lowercase

while counter <= 26:
    file = open(f"{letters[counter]}.txt", "w")
    file.write(letters[counter])
    counter += 1
