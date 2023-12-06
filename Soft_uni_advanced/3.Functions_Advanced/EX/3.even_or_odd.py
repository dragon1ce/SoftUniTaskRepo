def even_odd(*args):
    if args[-1] == 'odd':
        return [x for x in args[0:-1] if x % 2 != 0]
    elif args[-1] == 'even':
        return [x for x in args[0:-1] if x % 2 == 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))