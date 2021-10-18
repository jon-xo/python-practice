# basta.py

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return "{} menu available from {} to {}".format(self.name,self.start_time,self.end_time)

    def calculate_bill(self, purchased_items):
      item_total = 0
      for item in purchased_items:
        item_total += item
      return item_total

def convert_time(time):
  if "am" in time:
    return time.split("am")[0]
  elif "pm" in time:
    return time.split('pm')[0]

class Franchise:
  def __init__(self, address, menus) -> None:
      self.address = address
      self.menus = menus

  def __repr__(self) -> str:
      return self.address

  def available_menus(self, time):
    for menu in self.menus:
      if "am" in menu.start_time:
        if(int(convert_time(menu.start_time)) >= int(convert_time(time))):
          print(menu.items)
      if "pm" in menu.end_time:
        if(int(convert_time(menu.end_time)) <= int(convert_time(time))):
          print(menu.items)

class Business:
  def __init__(self, name, franchises) -> None:
      self.name = name
      self.franchises = franchises


brunch = Menu(
  "brunch", 
  {
    'pancakes': 7.50, 
    'waffles': 9.00, 
    'burger': 11.00, 
    'home fries': 4.50, 
    'coffee': 1.50, 
    'espresso': 3.00, 
    'tea': 1.00, 
    'mimosa': 10.50, 
    'orange juice': 3.50
  },
  "11am",
  "4pm"
)

print(brunch)

print(brunch.calculate_bill([brunch.items["pancakes"], brunch.items["home fries"], brunch.items["coffee"]]))


early_bird = Menu(
  "early_bird", 
  {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 
    'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 
    'espresso': 3.00,
  },
  "3pm",
  "6pm"
)

print(early_bird.calculate_bill([early_bird.items["salumeria plate"], early_bird.items["mushroom ravioli (vegan)"]]))

dinner = Menu(
  "dinner",
  {
    'crostini with eggplant caponata': 13.00, 
    'ceaser salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 
    'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 
    'espresso': 3.00,
  },
  "5pm",
  "11pm"
)

kids = Menu(
  "kids",
  {
    'chicken nuggets': 6.50, 
    'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
  },
  "11am",
  "9pm"
)

arepas_menu = Menu(
  "Take a' Arepa",
  {
    'arepa pabellon': 7.00, 
    'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 
    'jamon arepa': 7.50
  },
  "10am",
  "8pm"
)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

flagship_store.available_menus("12pm")
flagship_store.available_menus("5pm")

basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
take_a_arepa = Business("Take a' Arepa", [arepas_place])

# flagship_store.convert_time("9am")