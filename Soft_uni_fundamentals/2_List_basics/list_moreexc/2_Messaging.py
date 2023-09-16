input_line_1 = input().split()
entry = input()
a = len(entry)
# find the num
for num in input_line_1:
    number = 0
    for index in range(len(num)):
        number += int(num[index])
    while len(entry) <= number:
        number -= len(entry)
    print(entry[number], end="")
    entry = entry[:number] + entry[number+1:]
