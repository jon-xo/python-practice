# shipping.py
## script accepts package weight and determines the least expensive
## choice from the list of shipping options:
## - Ground Shipping: flat charge + weight based rate
## - Ground Shipping Premium: higher single flat charge 
## - Drone Shipping: high weight based rate charge

## Prompt user with input for package weight

weight = 11

# Ground Shipping Cost
ground_flat = 20

if weight <= 2:
    weight = (weight * 1.50) + ground_flat
    print(weight)
elif weight > 2 and weight <= 6:
    weight = (weight * 3.00) + ground_flat
    print(weight)
elif weight > 6 and weight <= 10:
    weight = (weight * 4.00) + ground_flat
    print(weight)
else:
    weight = (weight * 4.75) + ground_flat
    print(weight)

## Determine which shipping method is the least expensive

## Provide total shipping cost to user