#!/usr/bin/env python

# Order of argument position by type:
# 1. Stadard positional arguments
# 2. `*args`
# 3. Standard keyword arguments
# 4. `**kwargs`

def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)

single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', scoop1="Vanilla", scoop2="Cookies and Cream")

# Unpacking operators

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip ) / split
    print(split_price)

table_7_total = [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)