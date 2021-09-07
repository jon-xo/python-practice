# adv_list_review.py

# Combined review of concepts covered in advanced_lists.py

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

first = inventory.pop(0)
# OR: first = inventory[0]

last = inventory.pop(-1)
#OR: last = inventory[-1]

inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]

twin_beds = inventory.count("twin bed")

removed_item = inventory[4]

inventory.insert(10, "19th Century Bed Frame")

invetory.sort()
print(inventory)