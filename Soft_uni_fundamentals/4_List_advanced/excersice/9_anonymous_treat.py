def split_the_word(word, parts, chars_per):
    new_word = word
    lst = []
    for i in range(parts):
        a = new_word[:chars_per]
        lst.append(a)
        new_word = new_word[chars_per:]
    if len(new_word) > 0:
        lst[-1] = lst[-1] + new_word
    return lst


entry = input().split()
while True:
    command = input()
    if command == "3:1":
        break
    split = command.split()
    split_command = split[0]
    split_start = int(split[1])
    split_end = int(split[2])
    # check if in range
    # command dependency
    if split_command == "merge":
        if split_start < 0:
            split_start = 0
        if split_end >= len(entry):
            split_end = len(entry)
        word = "".join(entry[split_start:split_end + 1])
        entry = entry[:split_start] + [word] + entry[split_end + 1:]
    elif split_command == "divide":
        chars_per_partition = len(entry[split_start]) // split_end
        string_to_split = entry[split_start]
        after_func = split_the_word(string_to_split, split_end, chars_per_partition)
        entry = entry[:split_start] + after_func + entry[split_start + 1:]
        if len(entry[split_start]) % split_end == 0:
            split_word = []
print(" ".join(entry))
