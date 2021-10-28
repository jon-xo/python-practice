# function_intro.py

## define function
## def = function header
## function_name = snake_case

def auto_hello():
    print("Automated")
    print("Hello!")

auto_hello()

## parameters and arguments

## function parameters allow functions to accept data as input


def trip_welcome(destination):
    if(str(type(destination)) == "<class 'str'>"):
        print("Welcome to Trip Planner!")
        print("Looks like you're heading to " + destination + " today.")
    else:
        print("Whoops!")
        print("Please enter a valid destination!")        


## arguments are the specific data passed to the function

trip_welcome("NYC")

## multiple parameters

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    
    print("Trip Total: ")
    print(car_rental_total + hotel_total + plane_ticket_price)
    
calculate_expenses(200, 100, 100, 5)