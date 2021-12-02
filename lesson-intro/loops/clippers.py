# clippers.py

## Comprehensive loops example

## Section 1

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for cost in prices:
    total_price += cost

# print(total_price)
average_price = total_price / len(prices)
print("Average Haircut Price:")
print(average_price)

new_prices = [new_price - 5 for new_price in prices]
print(new_prices)

## Section 2

total_revenue = 0


for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
    i += 1

print("Total Revenue:")
print(total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)