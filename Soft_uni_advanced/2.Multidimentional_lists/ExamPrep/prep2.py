def is_in_area(dr, dc):
    return 0 <= dr < ROWS and 0 <= dc < COLS


ROWS, COLS = [int(x) for x in input().split(',')]
direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
matrix = []
total_cheese = 0
mouse_position = None
for i in range(ROWS):
    row_data = list(input())
    if 'M' in row_data:
        mouse_position = [i, row_data.index("M")]
    if 'C' in row_data:
        total_cheese += row_data.count("C")
    matrix.append(row_data)
while True:
    direction = input()
    if direction == "danger":
        print("Mouse will come back later!")
        break
    current_row, current_col = mouse_position
    row_to_go, col_to_go = direction_mapper[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go
    if not is_in_area(desired_row, desired_col):
        print("No more cheese for tonight!")
        break
    elif matrix[desired_row][desired_col] == "C":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        total_cheese -= 1
        mouse_position = [desired_row,desired_col]
        if total_cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[desired_row][desired_col] == "T":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        print("Mouse is trapped!")
        break
    elif matrix[desired_row][desired_col] == "@":
        continue
    elif matrix[desired_row][desired_col] == "*":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        mouse_position = [desired_row, desired_col]
for i in matrix:
    print(*i,sep="")