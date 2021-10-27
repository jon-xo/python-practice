# function_challenge.py

# tenth power function

def tenth_power(num):
    return num ** 10

# square root function

def square_root(num):
    return int(num ** .5)

# win percentage function

def win_percentage(win, losses):
    return (win / (win + losses)) * 100

print(win_percentage(5, 5))

# Average function

def average(num1, num2):
    return int((num1 + num2) / 2)

# Remainder function

def remainder(num1, num2):
    return (num1 * 2) % (num2 / 2)

print(remainder(15, 14))

# ------------
# Advanced Functions

# First three multiples

def first_three_multiples(num):
    for x in range(4):
        if x <= 2:
            print(num * x)
        else:
            print(num * x)
            return num * x
    
first_three_multiples(7)

# Tip

def tip(total, percentage):
    return (total * percentage) / 100

print(tip(10, 25))

# Bond, James bond

def introduction(first_name, last_name):
    return last_name + ', ' + first_name + ' ' + last_name

# Dog Years

def dog_years(name, age):
    dog_age = age * 7
    return "{}, you are {} years old in dog years".format(name, dog_age)

# All Operations
# - Add the first two inputs
# - Subtract the third and fourth input
# - Multiple the two results

def lots_of_math(a, b, c, d):
    r1 = a + b
    print(r1)
    r2 = c - d
    print(r2)
    r3 = r1 * r2
    print(r3)
    return r3 % a