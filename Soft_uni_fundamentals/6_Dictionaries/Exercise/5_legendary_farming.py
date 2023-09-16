junk = {}
rare_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
found = False

while not found:
    entry = input().split()
    for i in range(0, len(entry), 2):
        material = entry[i + 1].lower()
        quantity = int(entry[i])
        if material in rare_materials:
            rare_materials[material] += quantity
            if rare_materials[material] >= 250:
                mat_of_found = material
                found = True
                break
        elif material not in junk:
            junk[material] = quantity
        else:
            junk[material] += quantity
if mat_of_found == "motes":
    item = "Dragonwrath"
    rare_materials[mat_of_found] -= 250
elif mat_of_found == "fragments":
    item = "Valanyr"
    rare_materials[mat_of_found] -= 250
elif mat_of_found == "shards":
    item = "Shadowmourne"
    rare_materials[mat_of_found] -= 250
print(f"{item} obtained!")

ordered_key_materials = sorted(rare_materials.items(), key=lambda x: (-x[1], x[0]))
ordered_junk = sorted(junk.items(), key=lambda x: x[0])
print("\n".join(f"{k}: {v}" for k, v in rare_materials.items()))
print("\n".join(f"{k}: {v}" for k, v in junk.items()))
