from collections import deque

water_quant = int(input())
my_queue = deque()
command = input()
while command != "Start":
    my_queue.append(command)
    command = input()
entry = input().split()
while entry[0] != "End":
    if len(entry) != 1:
        water_quant += int(entry[1])
    else:
        n_water = int(entry[0])
        name = my_queue.popleft()
        if n_water <= water_quant:
            print(f"{name} got water")
            water_quant -= n_water
        else:
            print(f"{name} must wait")
    entry = input().split()
print(f"{water_quant} liters left")
