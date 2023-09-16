def smallest_of_three():
    lst = list()
    for i in range(3):
        num = int(input())
        lst.append(num)

    lst.sort()
    print(lst[0])
smallest_of_three()