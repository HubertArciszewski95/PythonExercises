# Please download the attached urls.txt file.
# The file contains some broken URLs. Here's what the file contains:
#
# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com
#
# Please use Python to remove the "s" from "https"
# and add another forward slash next to the existing slash

path = "/Users/hubertarciszewski/Downloads/urls.txt"

with open(path, "r") as file:
    file = file.readlines()

file = [x.strip() for x in file]
file = [x.replace("s", "", 1) for x in file]
file = [x[:5] + "/" + x[5:]for x in file]

for x in file:
    print(x)
