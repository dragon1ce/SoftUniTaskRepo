num = float(input())
if num == 0:
    print("zero")
elif num > 0:
    if 0 < num < 1:
        print("small positive")
    elif 0 < num < 1000000:
        print("positive")
    elif 0 < num:
        print("large positive")
else:
    if num > -1:
        print("small negative")
    elif num > - 1000000:
        print("negative")
    else:
        print("large negative")
