n = int(input())
ships = []
for _ in range(n):
    ships.append(list(map(int, input().split())))
unsplit_attack = input().split()
attack_list = [x.split("-") for x in unsplit_attack]
ship_destroyed = 0
for attack in range(len(attack_list) - 1, -1, -1):
    attack_row = int(attack_list[attack][0])
    attack_col = int(attack_list[attack][1])
    ships[attack_row][attack_col] -= 1
    if ships[attack_row][attack_col] == 0:
        ship_destroyed += 1
print(ship_destroyed)