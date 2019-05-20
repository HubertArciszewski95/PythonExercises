# Please download the json file in the attachment and use Python
# to add a new employee to the content of the file

import json

# Open JSON file
with open("/Users/hubertarciszewski/Downloads/company1.json", "r") as json_file:

    # Parse JSON file to python object using method load.
    parsed = json.load(json_file)

    # Add new employee to dictionary.
    parsed["employees"].append(dict(firstName="Albert", lastName="Bert"))

# Open JSON file in write mode.
with open("/Users/hubertarciszewski/Downloads/company1.json", 'w') as fp:

    # Overwrite file with new dictionary using method dump.
    json.dump(parsed, fp, sort_keys=True, indent=4)
