def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == 'odd':
            kwargs[k] = [x for x in v if x % 2 != 0]
        elif k == 'even':
            kwargs[k] = [x for x in v if x % 2 == 0]
    f = sorted(kwargs.items(), key=lambda kvp: -len(kvp[1]))
    return dict(f)



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
