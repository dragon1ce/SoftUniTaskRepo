from collections import deque

found = False
n = int(input())
petrol_distance_origin = deque()
start_index = 0
for i in range(n):
    petrol_distance_origin.append(input().split())


for z in range(len(petrol_distance_origin)):
    index = z
    fuel = 0
    distance = 0
    for x in range(len(petrol_distance_origin)):
        f,d = petrol_distance_origin[x]
        fuel += int(f)
        distance += int(d)
        if fuel<distance:
            petrol_distance_origin.rotate(-(1))
            break
    else:
        found = True
    if found:
        break
print(z)
# for i in range(len(petrol_distance_origin)):
#     if found:
#         break
#     petrol_distance = petrol_distance_origin.copy()
#     fuel = 0
#     distance = 0
#     while len(petrol_distance):
#         if distance > fuel:
#             break
#         f, d = petrol_distance.popleft()
#         fuel += int(f)
#         distance += int(d)
#     else:
#         found = True
#     if found:
#         break
#     start_index += 1
#     petrol_distance_origin.rotate(-start_index)
# print(start_index)