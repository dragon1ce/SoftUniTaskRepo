n = int(input())
my_stack = []
new_stack = []
for i in range(n):
    token = input().split()
    if token[0] == '1':
        my_stack.append(int(token[1]))
    else:
        if my_stack:
            if token[0] == '2':
                my_stack.pop()
            elif token[0] == '3':
                print(max(my_stack))
            elif token[0] == '4':
                print(min(my_stack))
while my_stack:
    new_stack.append(str(my_stack.pop()))
print(", ".join(new_stack))