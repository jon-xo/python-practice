# 2D_lists.py
## Two-Dimensional (2D) Lists are list contained in a parent list

## example

#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
        [["X"],["O"],["X"]], 
        [["O"],["X"],["O"]], 
        [["O"],["O"],["X"]]
]

## Pratice 1
heights = [
    ["Jenny", 61], 
    ["Alexus", 70], 
    ["Sam", 67], 
    ["Grace", 64],
    ["Vik", 68]
]

ages = [
    ["Aaron", 15],
    ["Dhruti", 16]
]

## Accessing 2D Lists
## Additional index brackets are used to access each additional level or dimension

class_name_test = [
    ["Jenny", 90], 
    ["Alexus", 85.5], 
    ["Sam", 83], 
    ["Ellie", 101.5]
]

print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)
print()
## Modifying 2D Lists

incoming_class = [
    ["Kenny", "American", 9], 
    ["Tanya", "Russian", 9], 
    ["Madison", "Indian", 7]
]

print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)