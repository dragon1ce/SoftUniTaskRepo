number_of_lines = int(input())
search_word = input()
my_list = []
for line in range(number_of_lines):
    word = input()
    my_list.append(word)

print(my_list)
for string in my_list:
    if search_word not in string:
        my_list.remove(string)
# for i in range(len(my_list) - 1, -1 ,-1):
#     element = my_list[i]
#     if search_word not in element:
#         my_list.remove(element)
# print(my_list)