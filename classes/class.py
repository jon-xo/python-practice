# class.py

# template for a a data type, python style guide recommends 
# capatalizing name of class

class FirstClass:
    pass

# -------------
# Instantiate a class
# One method could be creating an object and assigning it to a variable

class XmenReboot:
    pass

x_reboot = XmenReboot()

# The type method reverses the object
print(type(x_reboot))
## Output:
## <class '__main__.XmenReboot'>
## main represents the current python script

# -------------
# Class variable
# This variable remains the same for each instance of a class
# the object's class can be accessed with dot notation

class Musician:
    role = "Rockstar"

drummer = Musician()
print(drummer.role)

# -------------
# Methods
# Methods are functions that are defined inside a class.
# The first argument in a method is always the object that is calling method
# The first argument is named `self`

class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

air_bud = Dog()
air_bud.time_explanation()

# Method arguments
# Methods can accept multiple arguments, but self should remain the first

class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile

converter = DistanceConverter()
five_miles_to_kms = converter.how_many_kms(5)
print(five_miles_to_kms)


# Constructors
# Methods with special methods include dunder methods,
# which can be identified by double underscores on either side of them
# the __init__() method can be used to initialize a newly created object

# __init__() can accept arguments like other methods

class Shouter:
    def __init__(self, phrase) -> None:
        if type(phrase) == str:        
            print(phrase.upper())
        else:
            print("...")

shout1 = Shouter("Anybody?!")
shout2 = Shouter(7)

