# shipping.py
## script accepts package weight and determines the least expensive
## choice from the list of shipping options:
## - Ground Shipping: flat charge + weight based rate
## - Ground Shipping Premium: higher single flat charge 
## - Drone Shipping: high weight based rate charge

## Prompt user with input for package weight

weight = float(input("Enter package weight (lbs): "))

# Ground Shipping Cost
ground_flat = 20

if weight <= 2:
    ground_cost = (weight * 1.50) + ground_flat
    # print(ground_cost)
elif weight > 2 and weight <= 6:
    ground_cost = (weight * 3.00) + ground_flat
    # print(ground_cost)
elif weight > 6 and weight <= 10:
    ground_cost = (weight * 4.00) + ground_flat
    # print(ground_cost)
else:
    ground_cost = (weight * 4.75) + ground_flat
    # print(ground_cost)

print()
# Ground Total Cost
print("Standard Ground Shipping: $" + str(ground_cost))

# Premium Ground Total Cost
ground_premium_cost = 125.00
print("Premium Ground: $" + str(ground_premium_cost))

# Drone Ship

if weight <= 2:
    drone_cost = (weight * 4.50)
    # print(drone_cost)
elif weight > 2 and weight <= 6:
    drone_cost = (weight * 9.00)
    # print(drone_cost)
elif weight > 6 and weight <= 10:
    drone_cost = (weight * 12.00)
    # print(drone_cost)
else:
    drone_cost = (weight * 14.25)
    # print(drone_cost)

# Ground Total Cost
print("Drone Shipping: $" + str(drone_cost))

## Determine which shipping method is the least expensive

## Provide total shipping cost to user