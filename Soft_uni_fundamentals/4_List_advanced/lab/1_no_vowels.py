vowels = [ 'a', 'o', 'u', 'e', 'i']
a = input()
b = [x for x in a if x not in vowels ]
print("".join(b))