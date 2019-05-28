# Please download the attached countries-raw.txt file. The file contains the list of country names,
# but it also contains some unnecessary text among the countries.
#
# Please clean the list with Python by generating a new text file that contains
# a flawless list of country names without any other text or break lines in it.
# The new file content should look like in the expected output.

import string
with open("/Users/hubertarciszewski/Downloads/countries-raw.txt") as file:
    file = file.readlines()

invalid_char = ["Top of Page"]
[invalid_char.append(x) for x in list(string.ascii_uppercase)]

clear_list = [x.strip("\n") for x in file]
clear_list = [x for x in clear_list if x != ""]
clear_list = [x for x in clear_list if not x in invalid_char]

with open("countries.txt", "w") as clear_file:
    for x in clear_list:
        clear_file.write(x + "\n")

