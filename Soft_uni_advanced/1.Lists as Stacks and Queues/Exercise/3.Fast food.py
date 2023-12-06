from collections import deque
broken = False
quantity = int(input())
leftover = []
orders = deque([int(x) for x in input().split()])
print(max(orders))
while orders:
    a = orders.popleft()
    if quantity - a >= 0 and not broken:
        quantity -= a
    else:
        broken = True
        leftover.append(str(a))
if not leftover:
    print("Orders complete")
elif leftover:
    print(f"Orders left: {' '.join(leftover)}")