def filter_valid(a: str) -> bool:
    length = False
    valid_symbols = True
    redundant = False
    if 3 <= len(a) <= 16:
        length = True

    for i in a:
        if i.isalnum() or i == "-" or i == "_":
            pass
        else:
            valid_symbols = False

    return length and valid_symbols


x = input().split(", ")
x = list(filter(filter_valid, x))
print("\n".join(x))