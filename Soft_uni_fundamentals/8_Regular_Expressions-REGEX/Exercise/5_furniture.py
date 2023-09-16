import re

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"
total_money = 0
items = []
while True:
    entry = input()
    if entry == "Purchase":
        break
    matches = re.search(pattern, entry)
    if matches:
        furniture, price, quantity = matches.groups()
        total_money += (float(price) * int(quantity))
        items.append(furniture)
print("Bought furniture:")
for x in items:
    print(x)
print(f"Total money spend: {total_money:.2f}")
