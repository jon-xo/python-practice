# Lists.py
## Introduction to lists

# heights = [61, 70, 67, 64, 65]
names = ["Noelle", "Ava", "Sam", "Mia"]

ints_and_strings = [1, 2, 3, "four", "five", "Maveric"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]

my_empty_list = []

## List methods

example_list = [1, 2, 3, 4]
print(example_list)

print()

example_list.append(5)
print(example_list)

example_list.reverse()
print(example_list)

example_list.remove(5)
print(example_list)

## Append method

orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)

## List concatanation
## Use the [+] sign to combine two lists

orders_two = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

new_orders = ["lilac", "iris"]

orders_combined = orders_two + new_orders

## Accessing List items
## List use 0 index

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[3]