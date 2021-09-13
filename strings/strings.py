# Strings.py
# Strings are immutable

## Strings as a list

favorite_fruit = "blueberry"
print(favorite_fruit[3])

## Slicing a string
## The second number in the slice will terminate the selection before that character

print(favorite_fruit[4:6])


first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

## Concatanate

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)
print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
    # def reverse_length(name):
    #     return len(name) - 1
     
    # first_length = reverse_length(first_name)
    # print(first_length)
    # second_length = reverse_length(last_name)
    # print(second_length)
    return first_name[-3:] + last_name[-3:]

print(password_generator(first_name, last_name))

## Escape characters
## Special characters must be escaped when defining a string

password = "theycallme\"crazy\"91"

## string iteration

def get_length(string):
    x = 0
    for character in string:
        x +=1
    return x

## Conditionals
## in can be used to identify a character or part of a string

print("s" in "strawberry")
print("bat" in "batmobile")

def contains(big_string, little_string):
    if(little_string in big_string):
        return True
    else:
        return False

def common_letters(string_one, string_two):
    common_list = []
    for first_character in string_one:
        for second_character in string_two:
            if(first_character == second_character and 0 == common_list.count(first_character)):
                common_list.append(first_character)

    return common_list

## Review

def username_generator(first_name, last_name):
    username1 = ""
    username2 = ""

    if(len(first_name) <= 3):
        username1 = first_name
    else:
        username1 = first_name[:3]

    if(len(last_name) <= 4):
        username2 = last_name
    else:
        username2 = last_name[:4]

    return username1 + username2

def password_generator(username):
    password = ""

    for int in range(0,len(username)):
        password += username[int-1]
    return password


    
new_user = username_generator("Abe", "Simpson")
print(new_user)

print(password_generator(new_user))