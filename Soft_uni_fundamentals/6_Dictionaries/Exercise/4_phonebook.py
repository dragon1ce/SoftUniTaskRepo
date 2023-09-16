phonebook = {}
n = 0
while True:
    token = input().split("-")
    if len(token) > 1:
        phonebook[token[0]] = token[1]
    else:
        n = int(token[0])
        break
for _ in range(n):
    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")