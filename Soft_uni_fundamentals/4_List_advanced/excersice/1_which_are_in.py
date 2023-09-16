list_a = input().split(", ")
list_b = input().split(", ")
new_list = []
for item in list_a:
    for word in list_b:
        if item in word:
            new_list.append(item)
new_list2 = []
x = []
for i in new_list:
    if i not in x:
        x.append(i)

print(x)
