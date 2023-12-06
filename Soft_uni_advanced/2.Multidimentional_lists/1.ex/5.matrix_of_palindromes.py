rows, cols = [int(x) for x in input().split()]
matrix = []
helper = []
for row in range(rows):
    helper = []
    for col in range(cols):
        helper.append(chr(97 + row) + chr(97 + col+row) + chr(97 + row))
    print(*helper)
