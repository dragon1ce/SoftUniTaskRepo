sequence = input().split()
mid = len(sequence) // 2
first_car = 0
second_car = 0
i = 0
for index in range(mid):
    i -= 1
    left_side = int(sequence[index])
    right_side = int(sequence[i])
    first_car += left_side
    second_car += right_side
    if left_side == 0:
        first_car *= .8
    if right_side == 0:
        second_car *= 0.8

if first_car < second_car:
    winner = "left"
    total_time = first_car
else:
    winner = "right"
    total_time = second_car

print(f"The winner is {winner} with total time: {total_time:.1f}")
