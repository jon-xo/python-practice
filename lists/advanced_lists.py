# advanced_lists.py
## Python list manipulation using built-in methods

## .count() -- List method to count the number of matching occurences in a list
## .insert() -- List method to insert an element into a specific list index
## .pop() -- List method to remove an element from a specific index / end of a list
## range() -- Built-in function to create a sequence of integers
## len() -- Built-in function to get the length of a list
## .sort() / .sorted() -- A method & built-in function to sort a list

## Insert
## Method takes two inputs, the index you want to insert into
##  and the element you want to insert into

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)
front_display_list.insert(0, "Pineapple")
print(front_display_list)

## Pop
## Method takes an single (optional) input
## Once called the original list is modified and the removed value is dropped
## To retain the removed information, set the output of a method equal to a declared variable

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]

data_science_topics.pop()
print(data_science_topics)
data_science_topics.pop(3)
print(data_science_topics)

## Range
## Function generates numbers starting at 0 up to the last digit that is less then the parameter
## Default output is a range object, when combined with the list() function a standard list is created

number_list = range(9)
print(number_list)

zero_to_seven = range(8)
print(list(zero_to_seven))

## The starting int can be set by adding a second digit to the range parameters

my_list = range(2, 9)
print(list(my_list))

## Adding a third digit to the same example outputs a list that 
## outputs a list counting by that increment

my_list = range(2, 9, 2)
print(list(my_list))

range_five_three = range(5, 15, 3)

range_diff_five = range(0, 40, 5)


## Length
## Built in function that can be applied to determine the length of a list

range_list = range(2, 3000, 100)

range_list_length = len(range_list)
print(range_list_length)