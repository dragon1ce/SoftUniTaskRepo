def check_consecutive_count(string: str, sym: str) -> int:
    num_list = []
    count = 0
    for char in string:
        if char == sym:
            count += 1
        elif char != sym:
            num_list.append(count)
            count = 0
    else:
        num_list.append(count)
    return max(num_list)


NEED_FOR_JACKPOT = 10
NEED_FOR_WIN = 6
VALID_LENGTH_OF_TICKET = 20
tickets = input().split(", ")
tickets = [x.strip() for x in tickets]
winning_combos = ("@" * NEED_FOR_WIN, "#" * NEED_FOR_WIN, "$" * NEED_FOR_WIN, "^" * NEED_FOR_WIN)
jackpots = ("@" * NEED_FOR_JACKPOT, "#" * NEED_FOR_JACKPOT, "$" * NEED_FOR_JACKPOT, "^" * NEED_FOR_JACKPOT)
for ticket in tickets:
    if len(ticket) != VALID_LENGTH_OF_TICKET:
        print("invalid ticket")
        continue
    half_length = VALID_LENGTH_OF_TICKET//2
    left = ticket[0:half_length]
    right = ticket[half_length:]
    win = False
    jackpot = False
    symbol = ""
    counted = []
    for check in jackpots:
        if check in left and check in right:
            jackpot = True
            symbol = check[0]
            break
    else:
        for check in winning_combos:
            if check in left and check in right:
                win = True
                symbol = check[0]
                break
    if jackpot or win:
        counted.append(check_consecutive_count(left, symbol))
        counted.append(check_consecutive_count(right, symbol))

    if win is False and jackpot is False:
        print(f'ticket "{ticket}" - no match')
    if win is True and jackpot is False:
        print(f'ticket "{ticket}" - {min(counted)}{symbol}')
    if jackpot is True:
        print(f'ticket "{ticket}" - {max(counted)}{symbol} Jackpot!')
