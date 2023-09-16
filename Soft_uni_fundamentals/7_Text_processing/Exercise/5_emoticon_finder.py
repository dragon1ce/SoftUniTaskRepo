entry = input()
for index in range(len(entry)):
    if entry[index] == ":":
        if index+1 in range(len(entry)):
            print(entry[index]+entry[index+1])

