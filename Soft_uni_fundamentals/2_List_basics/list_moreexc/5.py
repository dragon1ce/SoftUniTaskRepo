line_one = input().split()
line_two = input().split()
line_three = input().split()
all_in_one = line_one + line_two + line_three
#print(all_in_one)
first_is_winner = False
second_is_winner = False
draw = True
if line_one.count("1") == 3 or line_two.count("1") == 3 or line_three.count("1") == 3:
    first_is_winner = True
elif line_one.count("2") == 3 or line_two.count("2") == 3 or line_three.count("2") == 3:
    second_is_winner = True
if not first_is_winner or not second_is_winner:
    for i in range(3):
        if line_one[i] == "1" and line_two[i] == "1" and line_three[i] == "1":
            first_is_winner = True
            break
        elif line_one[i] == "2" and line_two[i] == "2" and line_three[i] == "2":
            second_is_winner = True
            break
if not first_is_winner or not second_is_winner:
    if line_one[0] == "1" and line_two[1] == "1" and line_three[2] == "1":
        first_is_winner = True
    elif line_one[0] == "2" and line_two[1] == "2" and line_three[2] == "2":
        second_is_winner = True
    elif line_one[2] == "2" and line_two[1] == "2" and line_three[0] == "2":
        second_is_winner = True
    elif line_one[2] == "1" and line_two[1] == "1" and line_three[0] == "1":
        first_is_winner = True
if first_is_winner:
    print("First player won")
elif second_is_winner:
    print("Second player won")
else:
    print("Draw!")