fire_input = input().split("#")
total_water = int(input())
total_fire = 0
# print(fire_input)
kon = [x.split(" = ") for x in fire_input]
# print(kon)
effort = 0
value_list = []
is_valid = False
for fire in kon:
    is_valid = False
    value = int(fire[1])
    if fire[0] == "High" and 81 <= value <= 125:
        is_valid = True
    elif fire[0] == "Medium" and 51 <= value <= 80:
        is_valid = True
    elif fire[0] == "Low" and 1 <= value <= 50:
        is_valid = True
    if is_valid and total_water - value >= 0:
        total_water -= value
        effort += value * 0.25
        value_list.append(value)
print("Cells:")
for i in value_list:
    print(f" - {i}")
    total_fire += i
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
