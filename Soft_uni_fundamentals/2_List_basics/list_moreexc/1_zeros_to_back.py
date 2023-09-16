my_list = input().split(", ")
for item in range(len(my_list) - 1, -1, -1):
    my_list[item] = int(my_list[item])
    if my_list[item] == 0:
        del my_list[item]
        my_list.append(0)
print(my_list)
