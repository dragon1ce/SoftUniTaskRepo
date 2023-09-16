while True:
    entry = input()
    if entry == "End":
        break
    elif entry == "SoftUni":
        continue
    word=""
    for i in entry:
        word += i + i
    print(word)