chat = []
command = input()

while command != "end":
    split_command = command.split()
    if "Chat" in command:
        chat.append(split_command[1])
    elif "Delete" in command:
        if split_command[1] in chat:
            chat.remove(split_command[1])
    elif "Edit" in command:
        if split_command[1] in chat:
            index = chat.index(split_command[1])
            chat[index] = split_command[2]
    elif "Pin" in command:
        if split_command[1] in chat:
            index = chat.index(split_command[1])
            popped = chat.pop(index)
            chat.append(popped)
    elif "Spam" in command:
        chat = chat + split_command[1:]
    command = input()
print("\n".join(chat))
