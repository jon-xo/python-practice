# modules.py
from datetime import datetime
from decimal import Decimal
import random

## datetime
current_time = datetime.now()
print(current_time)


## random
## random.choice - accepts a list of ints as an argument 
## and returns a number at random
random_list = []
random_list = [random.randint(1, 100) for num in range(101)]
# print(random_list)

## random.randint - accepts two numbers as arguments and produces 
## a random int between the two values

randomer_number = random.choice(random_list)
print(randomer_number)

## decimals
cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')
 
cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)