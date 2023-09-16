input_string = input()
new = input_string[0]
for i in range(1,len(input_string)):
    if new[-1] != input_string[i]:
        new += input_string[i]
print(new)
