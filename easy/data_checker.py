# Filter out from list checklist none country object
with open("/Users/hubertarciszewski/Downloads/countries-clean.txt") as file:
    file = file.readlines()

file = [x.strip("\n") for x in file]

checklist = ["Portugal", "Germany", "Munster", "Spain"]

for x in checklist:
    if x not in file:
        item_to_del = checklist.index(x)
        checklist.pop(item_to_del)
print(checklist)





