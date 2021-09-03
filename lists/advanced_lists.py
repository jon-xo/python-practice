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