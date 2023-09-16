words = input().split()
words = [x.lower() for x in words]
word_dict = {}
for i in range(len(words)):
    if words[i] not in word_dict:
        word_dict[words[i]] = 0
    word_dict[words[i]] +=1
for k,value in word_dict.items():
    if value % 2 != 0:
        print(k, end=" ")
