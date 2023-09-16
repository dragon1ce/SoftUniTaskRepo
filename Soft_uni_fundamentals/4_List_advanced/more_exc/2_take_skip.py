input_list = [x for x in input()]
bonus_list = []
for i in range(len(input_list)-1,-1,-1):
    if input_list[i].isdigit():
        bonus_list.append(input_list.pop(i))
word = "".join(input_list)
take_list = []
skip_list = []
new_word = ""
bonus_list = reversed(bonus_list)
for index, item in enumerate(bonus_list):
    if index % 2 == 0:
        take_list.append(item)
    else:
        skip_list.append(item)
for i in range(len(take_list)):
    a = int(take_list[i])
    b = int(skip_list[i])
    new_word += word[:a]
    word = word[a:]
    word = word[b:]
print(new_word)
