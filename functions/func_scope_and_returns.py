# func_variable_access.py
## The scope of a functions argument is limited to the running function

## returns
## returns can be used with a variable to store the result of a function
## this pratice is called a returned function value

## example 1

def calculate_exchange_usd(us_dollars, exchange_rate):
    return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("$100 USD to NZW Dollars: " + str(new_zealand_exchange))

## example 2

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
    return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print_remaining_budget(new_budget_after_shirt)

## Multiple returns

## Multiple values can be returned by comma sepearting the variables in a return statement
## Likewise, the returned data can be stored in multiple, comma-seperated variables

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)