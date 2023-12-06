from collections import deque

material_box = deque([int(x) for x in input().split()])
magic_value = deque([int(x) for x in input().split()])

points = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
presents = {
    # "Doll": 0,
    # "Wooden train": 0,
    # "Teddy bear": 0,
    # "Bicycle": 0,
}

while material_box and magic_value:
    total_magic = material_box[-1] * magic_value[0]
    if total_magic in points:
        if points[total_magic] not in presents:
            presents[points[total_magic]] = 0
        presents[points[total_magic]] += 1
        material_box.pop()
        magic_value.popleft()

    elif total_magic < 0:
        material_box.append(material_box.pop() + magic_value.popleft())
    elif total_magic > 0:
        magic_value.popleft()
        material_box[-1] += 15
    elif magic_value[0] == 0 and material_box[-1] == 0:
        magic_value.popleft()
        material_box.pop()
    elif material_box[-1] == 0:
        material_box.pop()
    elif magic_value[0] == 0:
        magic_value.popleft()


if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_box:
    print(f"Materials left: {', '.join([str(x) for x in reversed(material_box)])}")

if magic_value:
    print(f"Magic left: {', '.join([str(x) for x in magic_value])}")

print_dict = dict(sorted(presents.items(), key=lambda item: item[0]))

for i,j in print_dict.items():
    print(f"{i}: {j}")