number_of_inputs =  int(input())
tuple_of_restriction = (",",".","_")
forbidden = "_"
is_pure = True
for i in range(number_of_inputs):
    entry = input()
    is_pure = True
    for x in entry:
        if x in tuple_of_restriction:
            is_pure = False
            break
        else:
            continue
    if is_pure:
        print(f"{entry} is pure.")
    else:
        print(f"{entry} is not pure!")