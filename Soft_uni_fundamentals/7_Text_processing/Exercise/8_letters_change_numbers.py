entry_string = input().split()
num = ""
num_list = []
for item in entry_string:
    left, num, right = item[0], int(item[1:-1]), item[-1]
    if left.isupper():
        letter_place = ord(left) - 64
        num = num / letter_place
    elif left.islower():
        letter_place = ord(left) - 96
        num = num * letter_place
    if right.isupper():
        letter_place = ord(right) - 64
        num = num - letter_place
    elif right.islower():
        letter_place = ord(right) - 96
        num = num + letter_place

    num_list.append(num)
print(f"{sum(num_list):.2f}")

