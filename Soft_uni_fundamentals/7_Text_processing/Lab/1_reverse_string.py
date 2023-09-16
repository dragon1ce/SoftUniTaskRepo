def reverse_string(string):
    return f"{string} = {string[::-1]}"


while True:
    entry = input()
    if entry == 'end':
        break
    print(reverse_string(entry))
