entry = input()
dic = {}
for char in entry:
    if char not in dic and char != " ":
        dic[char] = entry.count(char)
for k,v in dic.items():
    print(f"{k} -> {v}")