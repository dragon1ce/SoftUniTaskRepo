from collections import deque

initial_fuel = deque([int(x) for x in input().split()])
additional_fuel_consumption = deque([int(x) for x in input().split()])
distance = deque([int(x) for x in input().split()])
reached = 0
has_failed = False
for i in range(len(initial_fuel)):
    fuel_quant = initial_fuel.pop()
    addit_fuel_cons = additional_fuel_consumption.popleft()
    fuel_left = fuel_quant - addit_fuel_cons
    distance_to_reach = distance.popleft()
    if fuel_left >= distance_to_reach:
        reached += 1
        print(f"John has reached: Altitude {reached}")
    else:
        has_failed = True
        print(f"John did not reach: Altitude {reached + 1}")
        break

if has_failed:
    print(f"John failed to reach the top.")
    if reached > 0:
        lst = [f"Altitude {x}" for x in range(1, reached + 1)]
        print("Reached altitudes: " + ", ".join(lst))
    else:
        print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")
