#!/usr/bin/env python
"""This script script contains functions which update a tables dictionary,'
    using function and keyword arguments."""

tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': 'Orange Juice, Apple Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}
# print(tables)


def assign_table(table_number, name, vip_status=False):
    """Receives three arguments and updates the corresponding,
    dictionary value with the name, and default vip_status, unless vip_status
    is otherwise defined."""

    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''

def assign_and_print_order(table_number, *order_items):
    """Receives two arguments, table_number used to reference dictionary key,
    and a variable number of arguments which are assigned to a nested dictionary
    with the key of order"""

    tables[table_number]['order'] = order_items

    for order in order_items:
        print(order)

def assign_food_items(table_number, **order_items):
    """Receives two arguments, table_number used to reference dictionary key,
    and a keyword arguments which are accessed with the dictionary get method,
    and assigned to nested dictionaries order and subdictionaries food_items and
    drinks respectively. """

    food = order_items.get('food')
    drinks = order_items.get('drinks')
    # print(food)
    # print(drinks)
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks


assign_table(2, 'Arwa', True)
print('---tables with Arwa --- \n', tables, '\n')
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')

print(tables)

# assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

print('\n --- tables after update ---')
assign_table(3, 'Steve')
# assign_food_items(3, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)

def unassign_table(table_number):
    """Accepts single parameter used as dictionary key 
    and sets value to empty dictionary"""
    tables[table_number] = {}

unassign_table(2)
print('\n --- Table 2 Deleted ---')
print(tables)

