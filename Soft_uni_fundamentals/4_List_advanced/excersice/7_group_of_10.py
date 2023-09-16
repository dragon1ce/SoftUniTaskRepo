list_of_numbers = list(map(int, input().split(", ")))
biggest_number = max(list_of_numbers)
convert = str(biggest_number)
first = int(convert[0])
length = 10 ** (len(convert) - 1)

number_of_list_to_create = int(first * (length / 10))
if int(convert[-1]) > 0:
    for lists in range(1, number_of_list_to_create + 2):
        my_list = [i for i in list_of_numbers if i <= lists * 10]
        list_of_numbers = [i for i in list_of_numbers if i not in my_list]
        print(f"Group of {lists * 10}'s: {my_list}")
else:
    for lists in range(1, number_of_list_to_create + 1):
        my_list = [i for i in list_of_numbers if i <= lists * 10]
        list_of_numbers = [i for i in list_of_numbers if i not in my_list]
        print(f"Group of {lists * 10}'s: {my_list}")