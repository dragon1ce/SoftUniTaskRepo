key = int(input())
n_lines = int(input())
for line in range(n_lines):
    char = input()
    new_char = chr(ord(char) + key)
    print(new_char, end="")
    