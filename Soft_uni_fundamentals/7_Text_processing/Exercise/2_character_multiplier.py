x = input().split()
a, b = x
first_list = [ord(x) for x in a]
second_list = [ord(x) for x in b]
length = abs(len(first_list) - len(second_list))
total = 0
if len(first_list) > len(second_list):
    for i in range(length):
        second_list.append(1)
elif len(first_list) < len(second_list):
    for i in range(length):
        first_list.append(1)
for i in range(len(first_list)):
    total += first_list[i] * second_list[i]
print(total)
