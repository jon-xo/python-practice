# func_argument_types.py
## There are three types of arguments:
## - Positional arguments: arguments called by their in the function definition
## - Keyword arguments: arguments that can be aclled by their name
## - Default arguments: arguments that are given default values



# example function:
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

## Positional arguments
calculate_taxi_price(100, 10, 5)

## Keyword arguments
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

## Default arguments
## Since a value has been set for discount, it can be ommited when the function is called

calculate_taxi_price(25, 3.5)


def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)
    
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")