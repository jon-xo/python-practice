# dictionary.py

# A dictionary is an unordered set of [key: value] pairs

menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print(menu)

# keys and values can support multiple types
# values can include other dictionaries

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

translation = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "rock"}

# keys can not contain lists, dictionaries keys are typically string or numbers, which allow for specific hash values

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

# Add single [keys: value]
# If the key already exists in the dictionary, this will update the value

menu["cheesecake"] = 8

print(menu)

# Add multiple [keys: value] with the update method
# update accepts one or more key value pairs in the form of a dictionary

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print()

# List comprehensions
# Python will allow you to create a dictionary using two seperate lists
names = ["Jenny", "Alexis", "Samantha", "Grace"]
heights = [61, 74, 99, 82]

students = {key:value for key, value in zip(names, heights)}
print(students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

print(drinks_to_caffeine)