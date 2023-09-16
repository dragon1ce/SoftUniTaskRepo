def perf(num):
    lst = []
    for i in range(1, num):
        if num % i == 0:
            lst.append(i)
    list_sum = sum(lst)
    if list_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perf(int(input())))
