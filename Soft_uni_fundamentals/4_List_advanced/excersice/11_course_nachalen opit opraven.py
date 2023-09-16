entry_data = input().split(", ")


def swap(lesson_one, lesson_two, entry_dat):
    if lesson_one in entry_dat and lesson_two in entry_dat:
        index_one = entry_dat.index(lesson_one)
        index_two = entry_dat.index(lesson_two)
        entry_dat[index_one], entry_dat[index_two] = entry_dat[index_two], entry_dat[index_one]
        valid_one = len(entry_dat) > index_one + 1
        valid_two = len(entry_dat) > index_two + 1
        ex_in_one = False
        ex_in_two = False
        if valid_one:
            ex_in_one = "Exercise" in entry_dat[index_one + 1]
        if valid_two:
            ex_in_two = "Exercise" in entry_dat[index_two + 1]

        if ex_in_one and ex_in_two:
            entry_dat[index_one + 1], entry_dat[index_two + 1] = entry_dat[index_two + 1], entry_dat[index_one + 1]
        elif ex_in_one:
            popped = entry_dat.pop(index_one + 1)
            entry_dat.insert(index_two + 1, popped)
        elif ex_in_two:
            popped = entry_dat.pop(index_two + 1)
            entry_dat.insert(index_one + 1, popped)
    return entry_dat


while True:
    command = input()
    if command == "course start":
        break
    split_command = command.split(":")
    type_command = split_command[0]
    lesson_command = split_command[1]

    if type_command == "Add":
        if lesson_command not in entry_data:
            entry_data.append(lesson_command)

    elif type_command == "Insert":
        index = int(split_command[2])
        if len(entry_data) > index + 1 and lesson_command not in entry_data:
            if "Exercise" not in entry_data[index + 1]:
                entry_data.insert(index, lesson_command)
            else:
                entry_data.insert(index + 1, lesson_command)
        elif lesson_command not in entry_data:
            entry_data.insert(index, lesson_command)
    elif type_command == "Remove":
        if lesson_command in entry_data:
            index = entry_data.index(lesson_command)
            if len(entry_data) > index + 1:
                if "Exercise" in entry_data[index + 1]:
                    entry_data.pop(index + 1)
                    entry_data.pop(index)
                else:
                    entry_data.pop(index)
            else:
                entry_data.pop(index)

    elif type_command == "Swap":
        lesson_one = split_command[1]
        lesson_two = split_command[-1]
        entry_data = swap(lesson_one, lesson_two, entry_data)

    elif type_command == "Exercise":
        if lesson_command in entry_data and f"{lesson_command}-Exercise" not in entry_data:
            index = entry_data.index(lesson_command)
            entry_data.insert(index + 1, f"{lesson_command}-Exercise")
        elif lesson_command not in entry_data:
            entry_data.append(lesson_command)
            entry_data.append(f"{lesson_command}-Exercise")
for i in range(len(entry_data)):
    print(f"{i + 1}.{entry_data[i]}")