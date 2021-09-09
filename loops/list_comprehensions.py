# list_comprehensions.py

# List comprehensions allow for clean, inline modification of existing lists

numbers = [2, 4, 6, 8, 10]
doubled = [num * 2 for num in numbers]
print(doubled)

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [score + 10 for score in grades]
print(scaled_grades)

# Conditionals
## if statement

alt_numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in alt_numbers if num < 0]
print(negative_doubled)

## else statement
negative_alt = [num * 2 if num < 0 else num * 3 for num in alt_numbers]
print(negative_alt)

# rando_list = [x + 3 if x % 3 == 0 else x + 5 for x in range(15)]
# print(modulo_list)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)