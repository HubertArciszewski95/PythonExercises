# Please download the JSON file in the attachment and use Python to print out its content.
import json

with open("/Users/hubertarciszewski/Downloads/company1.json", "r") as json_file:
    parsed = json.load(json_file)

print(json.dumps(parsed, indent=2, sort_keys=True))
