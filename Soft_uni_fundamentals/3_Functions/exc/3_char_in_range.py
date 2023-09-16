a = input()
b = input()


def return_ascii(a, b):
    range_a = ord(a)
    range_b = ord(b)
    for char in range(range_a + 1, range_b):
        print(chr(char), end=" ")


return_ascii(a, b)
