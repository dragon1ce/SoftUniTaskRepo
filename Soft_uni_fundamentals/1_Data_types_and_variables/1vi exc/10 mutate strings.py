first_string = input()
second_string = input()
new_word=""
check_word = first_string # tupiq judge
for i in range(len(first_string)+1):
    new_word = second_string[:i+1]+first_string[i+1:]
    if check_word != new_word:
        print(new_word)
    check_word = new_word
#     #kitty doggy
#     #01234 01234
#     #doggy
# mylist = []
# first_string = input()
# second_string = input()
# new_word=""
# check_word = ""
# for i in range(len(first_string)):
#     new_word = second_string[:i+1]+first_string[i+1:]
#
#     if new_word not in mylist:
#         print(new_word)
#     mylist.append(new_word)
#     check_word = new_word
#     #kitty doggy
#     #01234 01234
#     #doggy