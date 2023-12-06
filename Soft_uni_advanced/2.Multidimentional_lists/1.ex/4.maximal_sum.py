rows, cols = [int(x) for x in input().split()]
square = 3
matrix = [input().split() for _ in range(rows)]
max_sum = float("-inf")
max_row = 0
max_col = 0
new_matrix = []
for row in range(rows -(square-1)):
    for col in range(cols -(square-1)):
        current_sum = 0
        for r in range(row, row + square):
            for c in range(col, col + square):
                current_sum += int(matrix[r][c])
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {max_sum}")

for i in range(max_row,max_row+square):
    new_matrix.append(matrix[i][max_col:max_col+square])

[print(*x) for x in new_matrix]