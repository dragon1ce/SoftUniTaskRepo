products = {}
while True:
    token = input().split(" ")
    if token[0] == "buy":
        break

    name = token[0]
    price = float(token[1])
    quantity = int(token[2])

    if name not in products:
        products[name] = [price, quantity]
    elif name in products:
        products[name][1] += quantity
    if products[name][0] != price:
        products[name][0] = price

for k, v in products.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")

