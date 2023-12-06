rows = int(input())

matrix = [input().split(", ") for x in range(rows)]

primary = [matrix[i][i] for i in range(len(matrix))]
secondary = []

# for i in range(len(matrix)):
#     primary.append(matrix[i][i])

for i in range(len(matrix)):
    print(secondary.append(matrix[i][-(i+1)]))
print(f"Primary diagonal:{', '.join(primary)}. Sum: {sum([int(x) for x in primary])}")
print(f"Secondary diagonal:{', '.join(secondary)}. Sum: {sum([int(x) for x in secondary])}")

#(matrix)