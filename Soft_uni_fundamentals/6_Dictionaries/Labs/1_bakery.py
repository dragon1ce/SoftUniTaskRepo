entry_list = input().split()
my_dict = {}
for item in range(0,len(entry_list),2):
    key = entry_list[item]
    value = entry_list[item+1]
    my_dict[key] = int(value)
print(my_dict)