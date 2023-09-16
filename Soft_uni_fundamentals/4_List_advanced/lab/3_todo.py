to_do_list = [""] * 10
while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("-")
    to_do_list.pop(int(split_command[0]) - 1)
    to_do_list.insert(int(split_command[0]) - 1, " ".join(split_command[1:]))
to_do_list = [x for x in to_do_list if x != ""]
print(to_do_list)
