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

# -------------
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

# -------------
# Instance variables
# The data held by an object is referred to as an instance varaible
# these are variables that are specific to the object

class FakeDict:
    pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)

# -------------
# Objects

# Attributes can be added to objects after instantation,
# the dir() function can list all available attributes,
# including ones that were not a part of the object constructor

print(dir(fake_dict1))

# Attribute functions

# If you attempt to access an attribute that doesn't exist
# Python will throw an AttributeError

try:
    fake_dict1.fake_lock
except AttributeError:
    print("This text gets printed!")

# the hasattr() function can be used to return true/false
# if the attribute exists

print(hasattr(fake_dict1, "fake_lock"))

# getattr() can be used to return the value of an attribute,
# or a default value

print(getattr(fake_dict1, "test_lock", 550))

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(") 

# Self
# The self keyword refers to the object and not the class being called
# this can be used to store private information in a class

class SearchEngineEntry:
    secure_prefix = "https://"
    def __init__(self, url):
        self.url = url
    
    def secure(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix,site=self.url)

apple = SearchEngineEntry("www.apple.com")
github = SearchEngineEntry("www.github.com")

print(apple.secure())
print(github.secure())


class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))

        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

