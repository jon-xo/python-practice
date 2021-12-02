#control_flow1.py
## control flow challenge

## Part 1

## Large Power

def large_power(base, exponent):
	if(base**exponent > 5000):
		return True
	else:
		return False

## Over budget

def over_budget(budget, food_bill, electricity_bill, interent_bill, rent):
	if(food_bill + electricity_bill + interent_bill + rent > budget):
		return True
	else: 
		return False
		
## Twice as large

def twice_as_large(num1, num2):
	if(num1 > num2 * 2):
		return True
	else:
		return False
	
## Divisible by Ten

def divisible_by_ten(num):
	if (num % 10 == 0):
		return True
	else:
		return False

## Not sum to Ten

def not_sum_to_ten(num1, num2):
	if (num1 + num2 !== 10):
		return True
	else:
		return False
		
## Part 2
