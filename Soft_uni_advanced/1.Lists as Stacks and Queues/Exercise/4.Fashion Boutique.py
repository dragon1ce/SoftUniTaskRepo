from collections import deque

entry = deque([int(x) for x in input().split()])
capacity = int(input())

racks = 0
current_sum = 0

while entry:
    racks += 1
    current_sum = 0
    while entry and current_sum + entry[-1] <= capacity:
        current_sum += entry.pop()

print(racks)