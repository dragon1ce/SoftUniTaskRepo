lst = []
while True:
    command = input()
    if command == "stop":
        break
    lst.append(command)
dic = {}
for i in range(0,len(lst),2):
    if lst[i] not in dic:
        dic[lst[i]] = int(lst[i+1])
    else:
        dic[lst[i]] += int(lst[i+1])
for key in dic:
    print("{} -> {}".format(key,dic[key]))