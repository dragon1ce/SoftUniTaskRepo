def palindrome(string):
    a = string
    b = string[::-1]
    return str(a == b)


c = list(map(palindrome, input().split(", ")))
print("\n".join(c))
