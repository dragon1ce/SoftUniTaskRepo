def find_factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


def factorial_division(n1, n2):
    a = find_factorial(n1)
    b = find_factorial(n2)
    return f"{a / b:.2f}"

a = int(input())
b = int(input())
print(factorial_division(a,b))
