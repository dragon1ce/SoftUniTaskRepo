number_of_orders = int(input())
total = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if not 0.01 <= price_per_capsule <= 100.:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= capsules_needed <= 2000:
        continue
    total_per_day = price_per_capsule * capsules_needed * days
    total += total_per_day
    print(f"The price for the coffee is: ${total_per_day:.2f}")
print(f"Total: ${total:.2f}")
