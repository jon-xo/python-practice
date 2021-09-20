# json_files.py

import json

# Read json file

with open('purchase_test.json') as purchase_json:
    purchase_data = json.load(purchase_json)

    print(purchase_data['user'])


# Write to json file

write_json = False

turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}


if (write_json):
    with open('output.json', 'w') as json_file:
        json.dump(turn_to_json, json_file)

