initial_loot = input().split("|")
while True:
    command = input()
    if command == "Yohoho!":
        break
    command_type = command.split()
    if command_type[0] == "Loot":
        for i in range(1, len(command_type)):
            if command_type[i] not in initial_loot:
                initial_loot.insert(0, command_type[i])
    elif command_type[0] == "Drop" and 0 <= int(command_type[1]) < len(initial_loot):
        a = initial_loot[int(command_type[1])]
        del initial_loot[int(command_type[1])]
        initial_loot.append(a)
    elif command_type[0] == "Steal":
        if len(initial_loot) > int(command_type[1]):
            print(", ".join(initial_loot[-int(command_type[1]):]))
            del initial_loot[-int(command_type[1]):]
        else:
            print(", ".join(initial_loot))
            initial_loot = []

if len(initial_loot) > 0:
    treasure_gain = [len(x) for x in initial_loot]
    treasure_gain_pints = sum(treasure_gain) / len(initial_loot)
    print(f"Average treasure gain: {treasure_gain_pints:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
