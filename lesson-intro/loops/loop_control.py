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

# continue
## Paired with a conditional to allow to skip past a loop iteration

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for patron in ages:
    if patron < 21:
        continue
    else:
        print(patron)
