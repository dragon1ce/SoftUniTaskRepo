initial_list = list(map(int, input().split()))
command = ""
# finding all evens
even_list = [even for even in initial_list if even % 2 == 0]
# finding all odds
odd_list = [odd for odd in initial_list if odd % 2 != 0]

reversed_list = initial_list[::-1]
len_initial = len(initial_list)
while command != "end":
    empty_list = []
    command_list = command.split()
    # Exchange
    if "exchange" in command:
        exchange_index = int(command_list[1])
        if exchange_index >= len(initial_list) or exchange_index < 0:
            print("Invalid index")
        else:
            initial_list = initial_list[exchange_index + 1:] + initial_list[:exchange_index + 1]

        # finding all evens
        even_list = [even for even in initial_list if even % 2 == 0]
        # finding all odds
        odd_list = [odd for odd in initial_list if odd % 2 != 0]
        reversed_list = initial_list[::-1]
    # Max
    elif "max" in command:
        max_index = 0
        if "odd" in command and len(odd_list) > 0:
            max_odd = max(odd_list)
            max_index = reversed_list.index(max_odd)
        elif "even" in command and len(even_list) > 0:
            max_even = max(even_list)
            max_index = reversed_list.index(max_even)
        else:
            print("No matches")
            command = input()
            continue
        print(len(initial_list) - max_index - 1)
    # Min
    elif "min" in command:
        min_index = 0
        if "odd" in command and len(odd_list) > 0:
            min_odd = min(odd_list)
            min_index = reversed_list.index(min_odd)
        elif "even" in command and len(even_list) > 0:
            min_even = min(even_list)
            min_index = reversed_list.index(min_even)
        else:
            print("No matches")
            command = input()
            continue
        print(len(initial_list) - min_index - 1)
    # First
    elif "first" in command:
        f_number = int(command_list[1])
        if len_initial < f_number:
            print("Invalid count")
        elif "even" in command:
            if len(even_list) >= f_number:
                print(even_list[:f_number])
            else:
                print(even_list)
        elif "odd" in command:
            if len(odd_list) >= f_number:
                print(odd_list[:f_number])
            else:
                print(odd_list)

    # Last
    elif "last" in command:
        l_number = int(command_list[1])
        if len_initial < l_number:
            print("Invalid count")
        elif "even" in command:
            if len(even_list) >= l_number:
                print(even_list[-l_number:])
            elif len(even_list) == 0:
                print(empty_list)
            else:
                print(even_list[::-1])
        elif "odd" in command:
            if len(odd_list) >= l_number:
                print(odd_list[-l_number:])
            elif len(odd_list) == 0:
                print(empty_list)
            else:
                print(odd_list[::-1])
    command = input()
print(initial_list)
