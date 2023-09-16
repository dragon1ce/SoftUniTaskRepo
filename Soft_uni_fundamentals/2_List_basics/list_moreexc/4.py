entry = input().split()
count = int(input())
new = []
# entry.insert(0,"Test")
a = count - 1
b = count - 1
while len(entry) > 0:

    if len(entry) > a:
        new.append(entry[a])
        del entry[a]
    else:
        while len(entry) <= a:
            a -= len(entry)
        new.append(entry[a])
        del entry[a]
    a += b

print(f"[{','.join(new)}]")


