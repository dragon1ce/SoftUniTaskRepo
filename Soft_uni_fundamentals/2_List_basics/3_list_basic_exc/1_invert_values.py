single_string = input()
numb_list = list(map(int,single_string.split()))
numb_list = [num * -1 for num in numb_list]
print(numb_list)