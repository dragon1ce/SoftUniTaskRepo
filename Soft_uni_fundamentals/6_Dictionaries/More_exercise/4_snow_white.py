dwarfs = {}
while True:
    command = input()
    if "Once upon a time" in command:
        break
    dwarf_name, dwarf_color, dwarf_physics = command.split(" ")
    dwarf_physics = int(dwarf_physics)
    if dwarf_color not in dwarfs.keys():
        dwarfs[dwarf_color] = {}
        dwarfs[dwarf_color][dwarf_name] = dwarf_physics
    elif dwarf_color in dwarfs.keys():
        if dwarf_name not in dwarfs[dwarf_color]:
            dwarfs[dwarf_color][dwarf_name] = dwarf_physics
        elif dwarf_name in dwarfs[dwarf_color] and \
                dwarfs[dwarf_color][dwarf_name] < dwarf_physics:
            dwarfs[dwarf_color][dwarf_name] = dwarf_physics

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: -sum(x[1].values())))
for hat_color, value in sorted_dwarfs.items():
    for name, physics in value.items():
        print(f"({hat_color}) {name} <-> {physics}")
