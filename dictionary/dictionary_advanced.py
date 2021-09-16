# dictionary_advanced.py

# access list

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# Invalid key error
# This can be managed by using an if statement

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

key_to_check = "Landmark 81"
 
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# This can also be managed with a try/excecpt statement

try:
    print(building_heights[key_to_check])
except KeyError:
    print("That key doesn't exist!")

# get method
# this can be used to safely get a key, if there is no match, return none
# additionally, the returned value can be customized

print(building_heights.get("Shanghai Tower"))
print(building_heights.get("Wayne Manor"))
print(building_heights.get("Fortress of Solitude", "Kryptonian home not found"))

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder")
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)

# delete a key

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)


health_points += available_items.pop("power stew", 0)

print(available_items)
print(health_points)

# Get all keys

## Using the list function

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))

## Using the keys method
## this method returns a dict_keys object which can not be modified
## however, this object can be used for iteration

print(test_scores.keys())

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)
print(lessons)

# Get all values

print(test_scores.values())

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for workout in num_exercises.values():
  total_exercises += workout

print(total_exercises)

# Get all key/value pairs
## items method returns a dict_list of tuples

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, profit in biggest_brands.items():
  print(company + " has a value of " + str(profit) + " billion dollars.")

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for role, percent in pct_women_in_occupation.items():
  print("Women make up " + str(percent) + " percent of " + role + "s")