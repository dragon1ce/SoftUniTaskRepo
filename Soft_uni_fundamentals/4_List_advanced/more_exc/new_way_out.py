def search_k(lst):
    index_of_k = 0
    maze_row_of_k = 0
    for index, item in enumerate(lst):
        if "k" in item:
            index_of_k = item.index("k")
            maze_row_of_k = index
    return index_of_k, maze_row_of_k


def up(lst, k):
    found_up = False
    m = []
    for row, item in enumerate(lst):
        if " " in item and " " == item[k]:
            lst[row] = item[:k - 1] + "k" + item[k + 1:]
            if lst[row] + 1 in range(len(lst)):
                lst[row + 1] = lst[row + 1].replace("k", "#")
            found_up = True
            break
    return lst, m


def down(lst, k, row_k):
    found_down = False
    m = []
    for row, item in enumerate(lst):
        if " " in item and " " == item[k] and row > row_k:
            lst[row] = item[:k - 1] + "k" + item[k + 1:]
            if lst[row] - 1 in range(len(lst)):
                lst[row + -1] = lst[row - 1].replace("k", "#")
            found_down = True
            break
    return lst, m


"""4
######
##  k#
## ###
## ###"""


def left_right(lst, k):
    found_left = False
    found_right = False
    found_both = False
    lst_b = []
    for j, item in enumerate(lst):
        if " " in item and (" " == item[k - 1] and " " == item[k + 1]):
            found_both = True
            lst_b = lst.copy()
            lst[j] = lst[j][:k - 1] + "k#" + lst[j][k + 1:]
            lst_b[j] = lst[j][:k] + "#k" + lst[j][k + 1:]

        elif " " == item[k - 1]:
            found_left = True
            lst_b = lst.copy()
            lst_b[j] = lst[j][:k - 1] + "#k" + lst[j][k + 1:]
        elif " " == item[k + 1]:
            lst[j] = lst[j][:k] + "k#" + lst[j][k + 1:]
            found_right = True
        if found_left or found_right or found_both:
            break
    return lst, lst_b


def check_way(listed_one, l_two, original):
    changed = False
    if listed_one != original and original != l_two:
        # found a way left and right
        changed = True
        print("ow no")
    elif listed_one != original:
        # found a way left or right
        original = listed_one
        changed = True
    return original, changed


def path_finder(lst):
    c = 0
    valid_range = range(len(lst))
    v_range = range(len(lst[0]))
    k_i, r_i = search_k(lst)
    up_check = down_check = left_check = right_check = False
    if r_i - 1 in valid_range:
        if lst[r_i - 1][k_i] == " ":
            c += 1
            up_check = True
    if r_i + 1 in valid_range:
        if lst[r_i + 1][k_i] == " ":
            c += 1
            down_check = True
    if k_i + 1 in v_range:
        if lst[r_i][k_i + 1] == " ":
            c += 1
            left_check = True
    if k_i - 1 in v_range:
        if lst[r_i][k_i + -1] == " ":
            c += 1
    return c, up_check, down_check, left_check, right_check


# def found_a_way(lst):
maze_rows = int(input())
maze = []
for _ in range(maze_rows):
    maze.append(input())
maze_whitespace = []
count_list = []
# for i in maze:
#     if i[0] == "k" or i[-1] == "k" or "k" in maze[0] or "k" in maze[-1]:
#         found_way = True

# ## main file
# find how many paths I have
my_tuple = path_finder(maze)

for _ in range(my_tuple[0]):
    count = 0
    maze_search = maze.copy()
    found_way = False
    while not found_way and count != 100:
        split_path = False
        count += 1
        for i in maze:
            if i[0] == "k" or i[-1] == "k" or "k" in maze[0] or "k" in maze[-1]:
                found_way = True
        # find k
        k_index, row_index = search_k(maze_search)
        # check paths
        list_one, list_two = up(maze_search, k_index)
        maze_search, diff = check_way(list_one, list_two, maze_search)
        if diff:
            continue
        list_one, list_two = down(maze_search, k_index, row_index)
        maze_search, diff = check_way(list_one, list_two, maze_search)
        if diff:
            continue
        list_one, list_two = left_right(maze_search, k_index)
        maze_search, diff = check_way(list_one, list_two, maze_search)
        if diff:
            continue

    count_list.append(count)
print(count_list)