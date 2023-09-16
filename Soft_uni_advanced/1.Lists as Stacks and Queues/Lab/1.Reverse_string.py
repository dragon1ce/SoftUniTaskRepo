entry = list(input())
rev = []
for i in range(len(entry)):
    rev.append(entry.pop())
print("".join(rev))