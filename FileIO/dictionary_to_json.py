# Store the dictionary in a json file.
import json

d = {"employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"}
],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}
    ]
}

with open('data.json', 'w') as fp:
    json.dump(d, fp, sort_keys=True, indent=4)
