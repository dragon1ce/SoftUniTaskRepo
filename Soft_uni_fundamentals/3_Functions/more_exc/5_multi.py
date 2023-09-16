def check(a, b, c):
    negative = 0
    if a == 0 or b == 0 or c == 0:
        return "zero"
    elif a < 0 or b < 0 or c < 0:
        if a < 0: negative += 1
        if b < 0: negative += 1
        if c < 0: negative += 1
        if negative != 2:
            return "negative"
        else:
            return "positive"
    else:
        return "positive"

a = int(input())
b = int(input())
c = int(input())

print(check(a, b, c))
