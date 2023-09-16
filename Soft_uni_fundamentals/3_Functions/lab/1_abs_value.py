def absolute(num):
    l = list(map(float, num.split()))
    return [abs(f) for f in l]
print(absolute(input()))
