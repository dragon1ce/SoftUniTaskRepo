def pass_check(password):
    digit_count = 0
    not_valid_symbol = False
    not_valid_length = False
    if not 6 <= len(password) <= 10:
        not_valid_length = True
    for i in range(len(password)):
        if password[i].isdigit():
            digit_count += 1
        elif password[i].isalpha():
            password.isalnum()
            continue
        else:
            not_valid_symbol = True
    if not_valid_length:
        print("Password must be between 6 and 10 characters")
    if not_valid_symbol:
        print("Password must consist only of letters and digits")
    if digit_count < 2:
        print("Password must have at least 2 digits")

    if not not_valid_symbol and not not_valid_length and (not digit_count < 2):
        print("Password is valid")
pass_check(input())
