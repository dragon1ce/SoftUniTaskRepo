sentence = input().split()
lst = []
for word in sentence:
    number = [c for c in word if c.isdigit()]
    stringer = [c for c in word if c.isalpha()]
    number_convert = chr(int("".join(number)))
    stringerer = "".join(stringer)
    if len(stringerer) > 1:
        lst.append(number_convert + stringerer[-1] + stringerer[1:-1] + stringerer[0])
    else:
        lst.append(number_convert + stringerer)
print(" ".join(lst))