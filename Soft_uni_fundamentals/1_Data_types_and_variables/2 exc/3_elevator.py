n = int(input())
p = int(input())
courses = 0
while n > 0:
    courses += 1
    n = n - p
print(courses)
