a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
n = int(input())
for _ in range(n):
    entry = input().split()
    command = entry[0:2]
    numbers = [int(num) for num in entry[2:]]
    if "Add" in entry:
        if "First" in entry:
            a.update(numbers)
        elif "Second" in entry:
            b.update(numbers)
    elif "Remove" in entry:
        if "First" in entry:
            a.difference_update(numbers)
        elif "Second" in entry:
            b.difference_update(numbers)
    elif "Check" in entry:
        print(a.issubset(b) or b.issubset(a))
print(*sorted(a),sep=", ")
print(*sorted(b),sep=", ")
