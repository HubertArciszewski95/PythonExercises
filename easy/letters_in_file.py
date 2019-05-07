# Create a script that generates a text file with all letters of English alphabet inside it,
# one letter per line.
import string

for x in string.ascii_lowercase:
    with open("file.txt", "a") as myfile:
        myfile.write(x + "\n")
