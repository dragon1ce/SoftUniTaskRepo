n_lines = int(input())
opening_brackets = 0
closing_brackets = 0
opened = False
for line in range(n_lines):
    entry = input()
    if opened:
        if entry == "(":
            print("UNBALANCED")
            break
        elif entry == ")":
            opened = False
    elif entry == "(":
        opened = True
    elif entry == ")":
        print("UNBALANCED")
        break
else:
    print("BALANCED")
