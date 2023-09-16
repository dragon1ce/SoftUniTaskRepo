entry_string = input()
new_string = ""
boomed_chars = 0
for i, char in enumerate(entry_string):
    if char == ">":
        boomed_chars += int(entry_string[i + 1])
        new_string += char
    elif boomed_chars > 0 and char.isalnum():
        boomed_chars -= 1
        continue
    else:
        new_string += char
print(new_string)
