maze_rows = int(input())
maze = []
for i in range(maze_rows):
    maze.append([input()])

maze_row = 0
k_found_index = 0
# for i in range(len(maze)):
#     print(maze[i])
for item in maze:
    for x in item:
        if "k" in x:
            maze_row = maze.index(item)
            k_found_index = x.index("k")


# for item in maze:
#     if item[0] == " " or item[0] == "k" or item[-1] == "0" or item[-1] == "k"
#         has_path ==
#     for i in item:
#         if


def outside(my_list):
    maze_row = 0
    k_found_index = 0
    for item in maze:
        for x in item:
            if "k" in x:
                maze_row = my_list.index(item)
                k_found_index = x.index("k")
    # check up and down
    up = False
    down = False
    left = False
    right = False
    for i, row in enumerate(my_list):
        if row[k_found_index] == " ":
            if i < maze_row:
                up = True

            elif i > maze_row:
                down = True


# count the "" and find index for each row
for row in range(len(maze)):
    for column in range(row):
        if maze[row] and row[column]:
            pass
