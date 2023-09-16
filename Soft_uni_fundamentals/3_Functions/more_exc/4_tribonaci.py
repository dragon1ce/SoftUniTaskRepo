def tribonacci(t):
    a = 0
    b = 0
    c = 1
    print(c, end=" ")
    for i in range(t - 1):
        d = a + b + c
        a = b
        b = c
        c = d
        print(d, end=" ")


n = int(input())
tribonacci(n)
