# Variable basics

## Variables can't begin with numbers
## Use underscores in place of spaces


bike_part = "tires"
print("Bike Shop -- Now Repairing " + bike_part)

bike_part = "brakes"
print("Bike Shop -- Now Repairing " + bike_part)

bike_part = "derauiller"
print("Bike Shop -- Now Repairing " + bike_part)

print("Last part used:")
print(bike_part)
print()

# Plus Equals

## Can be used to increment int stored in variable
miles_traveled = 12
miles_traveled += 2

print(miles_traveled)
print()

## Can also be used for string concatonation
beastie_boys = "No sleep..."
beastie_boys += "till Brooklyn!!"

print(beastie_boys)
