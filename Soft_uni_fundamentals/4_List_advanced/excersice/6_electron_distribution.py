number_of_electrons = int(input())
lst = []
counter = 0


def calc_max_in_cell(x):
    return 2 * (x ** 2)


while number_of_electrons > 0:
    lst.append(0)
    indices = len(lst)
    returned_num = calc_max_in_cell(indices)
    if number_of_electrons - returned_num < 0:
        lst[indices - 1] = number_of_electrons
        break
    else:
        lst[indices - 1] = returned_num
        number_of_electrons -= returned_num
print(lst)
