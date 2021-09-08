# while_loops.py

# while loops execute a set of instructions while a given conditon is true

count = 0
while count <= 3:
    print(count)
    count += 1

# Can also be expressed as a one-line expression by using semi-colon to seperate indented lines

countdown = 10
while countdown >= 0: print(countdown); countdown -= 1
print("We have liftoff!")

# While loops with Lists
## By using the len function, while loops can interact with the contents of a list

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
# print(length)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1
