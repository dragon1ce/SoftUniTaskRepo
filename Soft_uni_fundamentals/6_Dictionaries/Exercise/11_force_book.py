def by_pipe(side, user, force_dict: dict) -> dict:
    found_user = False
    for key_forces, value_users in force_dict.items():
        if user in value_users:
            found_user = True
            break
    if found_user:
        return force_dict
    if side not in force_dict:
        force_dict[side] = [user]
    elif side in force_dict:
        force_dict[side].append(user)
    return force_dict


def by_arrow(side, user, force_dict) -> dict:

    for key_forces, value_users in force_dict.items():
        if user in value_users:
            value_users.remove(user)
            break

    if side in force_dict.keys() and user not in force_dict[side]:
        force_dict[side].append(user)
    elif side not in force_dict.keys():
        force_dict[side] = [user]

    print(f"{user} joins the {side} side!")
    return force_dict


sides = {}
force_users, force_side = "", ""
while True:
    split_by_pipe = False
    entry = input()
    if entry == "Lumpawaroo":
        break
    if "|" in entry:
        force_side, force_users = entry.split(" | ")
        split_by_pipe = True
    elif "->" in entry:
        force_users, force_side = entry.split(" -> ")

    if split_by_pipe:
        sides = by_pipe(force_side, force_users, sides)
    elif split_by_pipe is False:
        sides = by_arrow(force_side, force_users, sides)

for key, value in sides.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(sides[key])}")
        for i in range(len(value)):
            print(f"! {value[i]}")
