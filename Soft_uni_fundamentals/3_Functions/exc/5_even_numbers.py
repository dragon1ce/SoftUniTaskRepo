def even(a):
    return a % 2 == 0


nums = list(map(int, input().split()))
b = list(filter(even, nums))
print(b)

# print(list(filter(lambda a: a % 2 == 0, list(map(int, input().split())))))
