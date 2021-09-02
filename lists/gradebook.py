# gradebook.py

## Organize a student's subjects and grades

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

print(gradebook)

gradebook[-1][-1] = gradebook[-1][-1] + 5

print(gradebook)

