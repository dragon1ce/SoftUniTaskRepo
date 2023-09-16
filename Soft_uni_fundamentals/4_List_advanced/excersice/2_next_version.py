x = input().split(".")
new_str = ""
for i in x:
    new_str += i
str_int = int(new_str)
if str_int + 1 % 10 == 0:
    str_int += 2
else:
    str_int += 1
new_str = str(str_int)
lst = []
for i in range(len(new_str)):
    lst.append(new_str[i])
print(".".join(lst))
