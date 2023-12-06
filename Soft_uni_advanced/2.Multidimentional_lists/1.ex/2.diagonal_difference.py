rows = int(input())

matrix = [input().split() for x in range(rows)]

primary = [int(matrix[i][i]) for i in range(len(matrix))]
secondary = [int(matrix[i][-i-1]) for i in range(len(matrix))]

print(abs(sum(primary)-sum(secondary)))

