# function_args.py

# Jiho's restaurunt

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

def assign_table(table_number, name, vip_status=False):
    # matched_table = tables.get(table_number)
    # matched_table.append(name)
    # matched_table.append(vip_status)

    # tables[table_number].append(name)
    # tables[table_number].append(vip_status)

    tables[table_number] = [name, vip_status]

assign_table(6, "Yoni", False)
assign_table(name="Martha", table_number=3, vip_status=True)
assign_table(4, "Karla")

print(tables)

# Unpacking operator

def my_function(*args):
  print(args)

my_function('Arg1', 245, False)
# prints: ('Arg1', 245, False)


def print_order(*order_items):
    print(order_items)

print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')

# Mutable function arguments
# To avoid mutating a function argument when it is called multiple times,
# A none work around can be used to avoid it

def update_order(new_item, current_order=None):
  if current_order is None:
    current_order = []
  current_order.append(new_item)
  return current_order

order1 = update_order({'item': 'burger', 'cost': '3.50'})
order2 = update_order({'item': 'soda', 'cost': '1.50'})

print(order2)