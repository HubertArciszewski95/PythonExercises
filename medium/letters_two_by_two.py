# Create a script that generates a file where all letters of English alphabet are listed two in each line.
import string

with open("file.txt", "a") as file:
    counter = 0
    for x in string.ascii_lowercase:
        if counter == 1:
            file.write(x + "\n")
            counter = 0
        else:
            file.write(x)
            counter += 1
