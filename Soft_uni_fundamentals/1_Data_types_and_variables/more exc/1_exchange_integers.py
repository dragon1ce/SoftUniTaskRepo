a = int(input())
b = int(input())
print("Before:")
print(f"a = {a}")
print(f"b = {b}")
print("After:")
a, b = b, a
print(f"a = {a}")
print(f"b = {b}")
