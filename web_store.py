# web_store.py
## List Review Pratice

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

customer_data = [
    ["Ainsley", "Small", True],
    ["Ben", "Large", False],
    ["Chani", "Medium", True],
    ["Depak", "Medium", False]   
]

print(customer_data)

## Toggle Chani's shipping option
customer_data[2][-1] = False

## Remove Ben's shipping preference
customer_data[1].remove(False)

# [["Amit", "Large", True], ["Karim", "X-Large", False]]

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)