# loop_control.py

# break
## break allows to stop iteration through using a conditional

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list...")
print()

for item in items_on_sale:
    print(item)
    if item == "red headband":
        break
print()
print("End of search!")

