from collections import deque

chocolate = deque([int(x) for x in input().split(', ')])
milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0
while True:
    if milkshakes == 5 or len(chocolate) == 0 or len(milk) == 0:
        break
    c = chocolate[-1]
    m = milk[0]
    if c <= 0 and m <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if c <= 0:
        chocolate.pop()
        continue
    if m <= 0:
        milk.popleft()
        continue
    if c == m:
        chocolate.pop()
        milk.popleft()
        milkshakes += 1
    else:
        milk.rotate(-1)
        chocolate[-1] -= 5

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")
