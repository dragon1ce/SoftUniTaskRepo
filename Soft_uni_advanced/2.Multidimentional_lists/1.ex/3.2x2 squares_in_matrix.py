rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
# print(matrix)
found = 0

for i in range(rows-1):
    for j in range(cols-1):

        a = matrix[i][j]
        b = matrix[i][1 + j]
        c = matrix[1 + i][j]
        d = matrix[1 + i][1 + j]
        if a == b == c == d:
            found += 1

print(found)