# If statements

## Enter a user name here, make sure to makeit a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

# ---------------
# ---------------

# Additional Relational Operators

x = 20
y = 20

if x == y:
    print("These numbers are the same")


credits = 120

if credits >= 120:
    print("You have enough credits to graduate!")

# Boolean Operators
## **and**

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120

gpa = 3.4

if credits >= 120 and gpa >= 2.0:
    print("You have enough credits to graduate!")


## **or**

alt_one = (2 - 1 > 3) or (-5 * 2 == -10)
alt_two = (9 + 5 <= 15) or (7 != 4 + 3)

if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")

## **not**

omega_one = not(4 + 5 <= 9)
omega_two = not(8 * 2) != 20 - 4

credits = 11
gpa = 1.9


if not credits >= 120:
    print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
    print("You do not meet either requirement to graduate")

# Else statement

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

## Elif statement

grade = 86

if grade >= 90: 
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")