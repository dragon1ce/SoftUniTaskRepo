from collections import deque

entry = deque(input())
n = len(entry) / 2
ob = "([{"
cb = ")]}"
steps = 0
unbalanced = False
if len(entry) % 2 != 0:
    unbalanced = True
while entry:
    if unbalanced:
        break
    if entry[0] in ob:
        entry.rotate(-1)
        steps += 1
        continue
    if entry[0] in cb:
        obi = ob.index(entry[-1])
        cbi = cb.index(entry[0])
        if obi == cbi:
            entry.pop()
            entry.popleft()
        else:
            unbalanced = True
if unbalanced:
    print("NO")
else:
    print("YES")
