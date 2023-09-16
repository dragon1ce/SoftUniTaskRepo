budget = float(input())
flour_price_per_kilo = float(input())
eggs_price = flour_price_per_kilo * .75
milk_price_liter = flour_price_per_kilo * 1.25
milk_per_quarter = milk_price_liter / 4
price_per_loaf = flour_price_per_kilo + milk_per_quarter + eggs_price

current_loafs = 0
colored_eggs = 0
counter_to_three = 0

while budget > price_per_loaf:
    budget -= price_per_loaf
    colored_eggs += 3
    counter_to_three += 1
    current_loafs += 1
    if counter_to_three == 3:
        calc = current_loafs - 2
        colored_eggs -= calc
        counter_to_three = 0

print(f"You made {current_loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")