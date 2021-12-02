# String

## Concatanation

birthday = "I am "
age = 5
birthday_concat = " years old!"

### Concatanation can be used with int types if passed to the str() function

birthday_string = birthday + str(age) + birthday_concat
print(birthday_string)

### An int can also be stored in a variable and passed to print as an argument
print(birthday,age,birthday_concat)

## Multi-line strings
### To allow for spaces and line breaks

strange_text = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""

print(strange_text)