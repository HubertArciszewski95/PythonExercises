# Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt.
# Each file should contain a letter reflecting its filename.

# More complex solution
import string

counter = 0
letters = string.ascii_lowercase

while counter <= 26:
    with open(f"{letters[counter]}.txt", "w") as file:
        file.write(letters[counter])
    counter += 1

# Simplest version
for x in string.ascii_lowercase:
    with open(f"{x}.txt", "w") as file1:
        file1.write(x)
