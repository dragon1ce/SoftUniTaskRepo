lst = list(map(int, input().split(", ")))
new_list = [i for i in range(len(lst)) if lst[i] % 2 == 0 ]
print(new_list)