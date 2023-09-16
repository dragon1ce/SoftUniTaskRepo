TRAIN_TICKET = 150
line_of_input = input().split("|")
budget = float(input())
starting_budget = budget
type_value_list = [x.split("->") for x in line_of_input]
new_prices = []

for item in type_value_list:
    we_buy = False
    item_type = item[0]
    item_price = float(item[1])

    if item_type == "Clothes" and item_price <= 50:
        we_buy = True
    elif item_type == "Shoes" and item_price <= 35:
        we_buy = True
    elif item_type == "Accessories" and item_price <= 20.5:
        we_buy = True

    if we_buy and budget - item_price >= 0:
        new_prices.append(item_price * 1.4)
        budget -= item_price
        print(f"{new_prices[-1]:.2f}", end=" ")

print()
print(f"Profit: {sum(new_prices) - starting_budget + budget:.2f}")
if TRAIN_TICKET <= sum(new_prices) + budget:
    print("Hello, France!")
else:
    print("Not enough money.")
