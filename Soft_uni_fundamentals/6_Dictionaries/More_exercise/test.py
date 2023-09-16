dwarfs = {}

while True:
    command = input()
    if command == "Once upon a time":
        break

    dwarf_name, dwarf_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    if dwarf_name not in dwarfs:
        dwarfs[dwarf_name] = {}

    if dwarf_color not in dwarfs[dwarf_name]:
        dwarfs[dwarf_name][dwarf_color] = dwarf_physics
    elif dwarfs[dwarf_name][dwarf_color] < dwarf_physics:
        dwarfs[dwarf_name][dwarf_color] = dwarf_physics

sorted_dwarfs = {}
for name, value in dwarfs.items():
    sorted_values = dict(sorted(value.items(), key=lambda x: (x[1], x[0])))
    sorted_dwarfs[name] = sorted_values

#sorted_dwarfs = dict(sorted(sorted_dwarfs.items(), key=lambda x: (-sum(x[1].values()), -len(x[1])), reverse=False))

for name, value in sorted_dwarfs.items():
    for hat_color, physics in value.items():
        print(f"({hat_color}) {name} <-> {physics}")
