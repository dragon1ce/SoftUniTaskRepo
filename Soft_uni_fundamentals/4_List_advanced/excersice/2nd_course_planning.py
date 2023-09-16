lesson_list = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    split_command = command.split(":")

    if split_command[0] == "Add":
        if split_command[1] not in lesson_list:
            lesson_list.append(split_command[1])

    elif split_command[0] == "Insert":
        if split_command[1] not in lesson_list:
            lesson_list.insert(int(split_command[2]), split_command[1])

    elif split_command[0] == "Remove":
        if split_command[1] in lesson_list:
            index_lesson = lesson_list.index(split_command[1])
            if split_command[1] + "-Exercise" in lesson_list:
                lesson_list.pop(index_lesson)
                index_exercise = lesson_list.index(split_command[1] + "-Exercise")
                lesson_list.pop(index_exercise)
            else:
                lesson_list.pop(index_lesson)

    elif split_command[0] == "Exercise":
        if split_command[1] not in lesson_list:
            lesson_list.append(split_command[1])
            lesson_list.append(split_command[1] + "-Exercise")
        elif split_command in lesson_list:
            if split_command[1] + "-Exercise" not in lesson_list:
                index = lesson_list.index(split_command[1])
                lesson_list.insert(index, split_command[1] + "-Exercise")

    elif split_command[0] == "Swap":
        if (split_command[1] in lesson_list) and (split_command[2] in lesson_list):
            index_one = lesson_list.index(split_command[1])
            index_two = lesson_list.index(split_command[2])
            lesson_list[index_one], lesson_list[index_two] = lesson_list[index_two], lesson_list[index_one]
            if (split_command[1] + "-Exercise" in lesson_list) and (split_command[2]+"-Exercise" in lesson_list):
                index_ex_one = lesson_list.index(split_command[1] + "-Exercise")
                index_ex_two = lesson_list.index(split_command[2] + "-Exercise")
                lesson_list[index_ex_one], lesson_list[index_ex_two] = \
                    lesson_list[index_ex_two], lesson_list[index_ex_one]
            elif split_command[1] + "-Exercise" in lesson_list:
                index_ex_one = lesson_list.index(split_command[1] + "-Exercise")
                index_one = lesson_list.index(split_command[1])
                popped = lesson_list.pop(index_ex_one)
                lesson_list.insert(index_one + 1, popped)
            elif split_command[2] + "-Exercise" in lesson_list:
                index_ex_two = lesson_list.index(split_command[2] + "-Exercise")
                index_two = lesson_list.index(split_command[2])
                popped = lesson_list.pop(index_ex_two)
                lesson_list.insert(index_two + 1, popped)

for i in range(len(lesson_list)):
    print(f"{i + 1}.{lesson_list[i]}")
