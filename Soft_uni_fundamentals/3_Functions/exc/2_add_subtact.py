int1 = int(input())
int2 = int(input())
int3 = int(input())


def sum_numbers(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def add_and_subtract(n1, n2, n3):
    sumn = sum_numbers(n1, n2)
    subs = subtract(sumn, n3)
    print(subs)


add_and_subtract(int1, int2, int3)
