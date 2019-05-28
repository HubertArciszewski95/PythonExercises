checklist = ["Portugal", "Germany", "Spain"]

with open("/Users/hubertarciszewski/Downloads/countries-missing.txt") as file:
    file = file.readlines()

file = [x.strip("\n") for x in file]
add_to_file = [file.append(x) for x in checklist]
file = sorted(file)
file = "\n".join(file)

with open("countries.txt", "w") as new_file:
    new_file = new_file.write(file)
