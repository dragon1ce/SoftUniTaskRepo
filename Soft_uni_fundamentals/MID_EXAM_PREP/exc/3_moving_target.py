target = list(map(int, input().split()))
command = ""
ended = False
while True:
    command = input()
    if command == "End":
        str_list = [str(x) for x in target]
        print(*target, sep="|")
        ended = True
        break
    split_command = command.split()
    type_command = split_command[0]
    index = int(split_command[1])
    value = int(split_command[2])
    if type_command == "Shoot" and 0 <= index < len(target):
        target[index] -= value
        if target[index] <= 0:
            target.pop(index)
    elif type_command == "Add":
        if 0 <= index < len(target):
            target.insert(index, value)
        else:
            print("Invalid placement!")

    elif type_command == "Strike":
        if index - value >= 0 and index + value < len(target):
            del target[index - value:(index + value) + 1]
        else:
            print("Strike missed!")
