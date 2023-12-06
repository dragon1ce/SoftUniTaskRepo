def overflow(x, y):
    nx = x
    ny = y
    if x < 0:
        nx = SIZE - 1
    elif x == SIZE:
        nx = 0
    elif y < 0:
        ny = SIZE - 1
    elif y == SIZE:
        ny = 0
    return [nx, ny]


SIZE = int(input())
QUOTA = 20
matrix = []
boat_pos = [0, 0]
fish_caught = 0
whirlpool = False
for r in range(SIZE):
    raw_data = list(input())
    matrix.append(raw_data)
    if "S" in raw_data:
        boat_pos = [r, raw_data.index("S")]
        matrix[r][raw_data.index("S")] = "-"
while True:
    command = input()
    if command == "collect the nets":
        break
    if command == "up":
        boat_pos_x = boat_pos[0] - 1
        boat_pos_y = boat_pos[1]
        boat_pos = overflow(boat_pos_x, boat_pos_y)
    elif command == "down":
        boat_pos_x = boat_pos[0] + 1
        boat_pos_y = boat_pos[1]
        boat_pos = overflow(boat_pos_x, boat_pos_y)
    elif command == "left":
        boat_pos_x = boat_pos[0]
        boat_pos_y = boat_pos[1] - 1
        boat_pos = overflow(boat_pos_x, boat_pos_y)
    elif command == "right":
        boat_pos_x = boat_pos[0]
        boat_pos_y = boat_pos[1] + 1
        boat_pos = overflow(boat_pos_x, boat_pos_y)
    symbol_at_current_pos = matrix[boat_pos[0]][boat_pos[1]]
    if symbol_at_current_pos == "W":
        whirlpool = True
        print(
            f"You fell into a whirlpool!"
            f" The ship sank and you lost the fish you caught. Last coordinates of the ship: [{boat_pos[0]},{boat_pos[1]}]")
        break

    elif symbol_at_current_pos == "-":

        continue
    elif symbol_at_current_pos.isdigit():
        num = int(symbol_at_current_pos)
        fish_caught += num
        matrix[boat_pos[0]][boat_pos[1]] = "-"
matrix[boat_pos[0]][boat_pos[1]] = "S"
if fish_caught>= QUOTA and not whirlpool:
    print("Success! You managed to reach the quota!")
    print(f"Amount of fish caught: {fish_caught} tons.")
    for i in matrix:
        print(*i, sep="")
elif fish_caught<QUOTA and not whirlpool:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA-fish_caught} tons of fish more.")
    if fish_caught>0:
        print(f"Amount of fish caught: {fish_caught} tons.")
    for i in matrix:
        print(*i, sep="")
