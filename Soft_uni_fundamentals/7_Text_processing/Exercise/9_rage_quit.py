entry_string = input()
new_string = ""
found_number = 0
for i, char in enumerate(entry_string):
    if char.isdigit():
        num = int(char)
        if i + 1 in range(len(entry_string)):
            if entry_string[i + 1].isdigit():
                num = int(entry_string[i] + entry_string[i + 1])
        new_string += entry_string[found_number:i].upper() * num
        found_number = i + 1
a = set(new_string)
print(f"Unique symbols used: {len(a)}")
print(new_string)
