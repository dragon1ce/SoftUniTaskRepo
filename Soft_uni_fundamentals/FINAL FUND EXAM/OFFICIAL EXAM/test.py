a = [None,1,2,None]
a = [x for x in a if x is not None]
b = a.sort(reverse=True)
print(b)