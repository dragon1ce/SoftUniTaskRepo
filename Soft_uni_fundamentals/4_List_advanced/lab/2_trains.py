trains = [0 for x in range(int(input()))]
command = ""
while command != "End":
    split_command = command.split()
    if "add" in split_command:
        trains[-1] += int(split_command[1])
    elif "insert" in split_command:
        trains[int(split_command[1])] += int(split_command[2])
    elif "leave" in split_command:
        trains[int(split_command[1])] -= int(split_command[2])
    command = input()
print(trains)
