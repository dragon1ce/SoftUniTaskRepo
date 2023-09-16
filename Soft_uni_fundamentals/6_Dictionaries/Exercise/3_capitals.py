a = input().split(", ")
b = input().split(", ")
c = zip(a,b)
d = {key: value for key,value in c}
for x in d:
    print("{} -> {}".format(x,d[x]))
