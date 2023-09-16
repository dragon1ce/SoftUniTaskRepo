entry_data = input().split(", ")


def swap(lesson_1, lesson_2, entry_dat):
    if lesson_1 in entry_dat and lesson_2 in entry_dat:
        index_one = entry_dat.index(lesson_1)
        index_two = entry_dat.index(lesson_2)
        entry_dat[index_one], entry_dat[index_two] = entry_dat[index_two], entry_dat[index_one]
        valid_one = index_one + 1 in range(len(entry_dat))
        valid_two = index_two + 1 in range(len(entry_dat))
        ex_in_one = False
        ex_in_two = False
        if valid_one:
            ex_in_one = "Exercise" in entry_dat[index_one + 1]
        if valid_two:
            ex_in_two = "Exercise" in entry_dat[index_two + 1]

        if ex_in_one and ex_in_two:
            entry_dat[index_one + 1], entry_dat[index_two + 1] = entry_dat[index_two + 1], entry_dat[index_one + 1]
        elif ex_in_two and not ex_in_one:
            popped = entry_dat.pop(index_two + 1)
            entry_dat.insert(index_one + 1, popped)
        elif ex_in_one and not ex_in_two:
            popped = entry_dat.pop(index_one + 1)
            entry_dat.insert(index_two + 1, popped)

    return entry_dat


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_index = list_of_lessons.index(first_lesson)
        second_index = list_of_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_index + 1 in range(len(list_of_lessons)):
            first_has_exercise = "Exercise" in list_of_lessons[first_index + 1]
        if second_index + 1 in range(len(list_of_lessons)):
            second_has_exercise = "Exercise" in list_of_lessons[second_index + 1]
        list_of_lessons[first_index], list_of_lessons[second_index] = \
            list_of_lessons[second_index], list_of_lessons[
                first_index]
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_index + 1], list_of_lessons[second_index + 1] = \
                list_of_lessons[second_index + 1], list_of_lessons[first_index + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lessons.insert(first_index + 1, list_of_lessons.pop(second_index + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_index + 1, list_of_lessons.pop(first_index + 1))
    return list_of_lessons


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
        if lesson_command not in entry_data:
            entry_data.insert(index, lesson_command)

    elif type_command == "Remove":
        if lesson_command in entry_data:
            index = entry_data.index(lesson_command)
            if index + 1 in range(len(entry_data)):
                if "Exercise" in entry_data[index + 1]:
                    entry_data.pop(index + 1)
            entry_data.pop(index)

    elif type_command == "Swap":
        lesson_one = split_command[1]
        lesson_two = split_command[-1]
        entry_data = swap_lesson(entry_data, lesson_one, lesson_two)

    elif type_command == "Exercise":
        if lesson_command in entry_data and f"{lesson_command}-Exercise" not in entry_data:
            index = entry_data.index(lesson_command)
            entry_data.insert(index + 1, f"{lesson_command}-Exercise")
        elif lesson_command not in entry_data:
            entry_data.append(lesson_command)
            entry_data.append(f"{lesson_command}-Exercise")

for i, name in enumerate(entry_data):
    print(f"{i + 1}.{name}")
