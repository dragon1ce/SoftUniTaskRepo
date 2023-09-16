n = int(input())
my_list = [list(input().split()) for _ in range(n)]
dot_list_a = []
for row in range(len(my_list)):
    for column in range(len(my_list[row])):
        if my_list[row][column] == ".":
            dot_list_a.append([row, column])
f = []
connected = 1
dot_list = dot_list_a.copy()
# for index in range(len(dot_list) -1):
#     if dot_list[index][0] + 1 == dot_list_a[index+1][0]:
#         connected += 1
#     elif dot_list[index][1] +1 == dot_list_a[index+1][1]:
#         connected += 1
#     else:
#         f.append(connected)
#         connected = 1
# else:
#     f.append(connected)
# dot_list = dot_list_a.copy()
for index in range(len(dot_list) - 1):
    dot_list[index][0] = dot_list[index][0] + 1
    if dot_list[index] in dot_list_a:
        connected += 1
    else:
        dot_list[index][1] = dot_list[index][1] + 1
        dot_list[index][0] = dot_list[index][0] - 1
        if dot_list[index] in dot_list_a:
            connected += 1
        else:
            f.append(connected)
            connected = 1
else:
    f.append(connected)
print(max(f))
