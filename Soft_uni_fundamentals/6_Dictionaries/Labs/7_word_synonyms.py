n = int(input())
synonyms = {}
lst = []
for i in range(n*2):
    lst.append(input())

for i in range(0,len(lst),2):
    if lst[i] not in synonyms:
        synonyms[lst[i]] = [lst[i+1]]
    else:
        synonyms[lst[i]].append(lst[i+1])

for k,v in synonyms.items():
    print(f"{k} - {', '.join(v)}")
