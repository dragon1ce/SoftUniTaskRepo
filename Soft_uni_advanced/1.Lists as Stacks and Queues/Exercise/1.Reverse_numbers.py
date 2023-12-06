from collections import deque
entry = deque(input().split())
f = []
for i in range(len(entry)):
    f.append(entry.pop())
print(" ".join(f))