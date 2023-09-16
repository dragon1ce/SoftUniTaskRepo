number_of_lines = int(input())
my_list = []
new_list = []
for i in range(number_of_lines):
    my_list.append(int(input()))
command = input()
if command == "even":
    new_list = [num for num in my_list if num % 2 == 0]
elif command == "odd":
    new_list = [num for num in my_list if num % 2 != 0]
elif command == "negative":
    new_list = [num for num in my_list if num < 0]
elif command == "positive":
    new_list = [num for num in my_list if num >= 0]
print(new_list)
