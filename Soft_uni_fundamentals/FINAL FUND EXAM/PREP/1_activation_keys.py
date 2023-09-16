def sliced(original_key, token):
    start_index = int(token[1])
    end_index = int(token[2])
    new_string = original_key[:start_index]+original_key[end_index:]
    return new_string

def flip(original_key, token):
    command, case, start_index, end_index = token
    start_index = int(start_index)
    end_index = int(end_index)
    new_key = ""
    left = original_key[0:start_index]
    changing_part = original_key[start_index:end_index]
    right = original_key[end_index:]
    if case == "Upper":
        new_key = left + changing_part.upper() + right
    elif case == "Lower":
        new_key = left + changing_part.lower() + right
    return new_key


def contains(original_key, substring):
    if substring in original_key:
        return f"{original_key} contains {substring}"
    return "Substring not found!"


first_string = input()
while True:
    entry = input()
    if entry == "Generate":
        print(f"Your activation key is: {first_string}")
        break
    entry = entry.split(">>>")
    if "Contains" in entry[0]:
        print_string = contains(first_string, entry[1])
        print(print_string)
    elif "Flip" in entry[0]:
        first_string = flip(first_string, entry)
        print(first_string)
    elif "Slice" in entry[0]:
        first_string = sliced(first_string, entry)
        print(first_string)

