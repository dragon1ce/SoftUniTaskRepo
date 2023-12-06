from collections import deque

armor = deque([int(x) for x in input().split(',')])
attack = deque([int(x) for x in input().split(',')])
monsters_killed = 0
while attack and armor:
    monster = armor.popleft()
    soldier = attack.pop()
    if soldier >= monster:
        monsters_killed += 1
        soldier -= monster
        if soldier > 0 and attack:
            attack[-1] += soldier
        elif soldier > 0 and not attack:
            attack.append(soldier)
    elif soldier < monster:
        monster -= soldier
        armor.append(monster)

if not armor:
    print("All monsters have been killed!")
if not attack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")
