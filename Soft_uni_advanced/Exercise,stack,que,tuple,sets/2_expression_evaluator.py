from collections import deque


def calc(first, second, operators):
    if operators == "*":
        return first * second
    elif operators == "/":
        return first / second
    elif operators == "+":
        return first + second
    elif operators == "-":
        return first - second


data = deque(input().split())

current_nums = deque()
while data:
    x = data.popleft()
    if x not in "*/+-":
        current_nums.append(int(x))
    else:
        while len(current_nums) > 1:
            a = current_nums.popleft()
            b = current_nums.popleft()
            c = calc(a, b, x)
            current_nums.appendleft(int(c))

print(int(current_nums[0]))