n = int(input())
total = 255
for i in range(n):
    a = int(input())
    if total - a < 0:
        print("Insufficient capacity!")
    else:
        total -= a
print(255 - total)
